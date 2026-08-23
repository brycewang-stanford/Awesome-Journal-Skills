"""Unit tests for the scorecard's two measurements.

The scorecard's job is to point at work. It stopped doing that once its dimensions
saturated — five of six sat at maximum for 299 of 299 packs, and the "quality score"
was arithmetically `94 + freshness`. These tests pin the properties that keep the
replacement honest:

* conformance is pass/fail and names what is missing;
* the backlog score is built only from things that differ between packs;
* a pack is never penalised for a dimension that does not apply to it;
* the tool reports its own saturation, so the next dead dimension is visible.

The scoring function reads a pack from disk, so each test builds a small pack in a
temporary directory. That keeps the assertions about the *rule* rather than about
whichever pack happens to be worst this month.
"""

from __future__ import annotations

import datetime as dt
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from . import context  # noqa: F401  (import for the sys.path side effect)

import quality_scorecard as qs

SKILL = """---
name: {slug}
description: Use when preparing a submission to the Journal of Testing. {pad}
---

# {slug}

{body}

```stata
regress y x
```
"""


class PackBuilder(unittest.TestCase):
    """Builds a conforming depth pack, so each test can break exactly one thing."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name)
        # `score_pack` reports skill paths relative to the repository root, so the
        # fixture directory has to stand in as that root.
        patch = mock.patch.object(qs, "ROOT", self.root)
        patch.start()
        self.addCleanup(patch.stop)

    def build(self, *, name: str = "Journal-of-Testing-Skills",
              skills: int = 12, body_units: int = 700,
              thin_units: int | None = None, flags: int = 0,
              verified_days_ago: int | None = 30, code: bool = True,
              exec_bridge: int = 0, readme_zh: bool = True,
              worked: bool = True, exemplars: bool = True,
              use_when: bool = True, venue_cue: bool = True) -> Path:
        # The skill slug carries the venue cue too (a prefix shared by most of a
        # pack's skills counts as naming the venue), so a fixture that removes the
        # cue has to remove it from both places.
        prefix = "testing" if venue_cue else "generic"
        pack = self.root / name
        (pack / ".claude-plugin").mkdir(parents=True)
        (pack / ".claude-plugin" / "plugin.json").write_text("{}", encoding="utf-8")
        (pack / "README.md").write_text("# Journal of Testing\n", encoding="utf-8")
        if readme_zh:
            (pack / "README.zh-CN.md").write_text("# 测试学报\n", encoding="utf-8")

        for i in range(skills):
            slug = f"{prefix}-skill-{i:02d}"
            units = thin_units if (thin_units is not None and i == 0) else body_units
            body = " ".join(f"word{j:04d}" for j in range(units))
            if i < exec_bridge:
                body += "\nSee shared-resources/execution-with-mcp.md for the bridge."
            desc_pad = "x" * 240
            text = SKILL.format(slug=slug, body=body, pad=desc_pad)
            if not use_when:
                text = text.replace("Use when preparing", "Preparing")
            if not venue_cue:
                text = text.replace("Journal of Testing", "Some Publication")
            (pack / "skills" / slug).mkdir(parents=True)
            (pack / "skills" / slug / "SKILL.md").write_text(text, encoding="utf-8")

        res = pack / "resources"
        res.mkdir()
        (res / "README.md").write_text("Resources for the pack.\n", encoding="utf-8")
        if worked:
            (res / "worked-examples").mkdir()
        if exemplars:
            (res / "exemplars").mkdir()
        if code:
            (res / "code").mkdir()
        source = "# Aims and scope\n"
        if verified_days_ago is not None:
            date = dt.date.today() - dt.timedelta(days=verified_days_ago)
            source += f"Accessed {date.isoformat()}.\n"
        source += "待核实\n" * flags
        (res / "official-source-map.md").write_text(source, encoding="utf-8")
        return pack


class TestConformance(PackBuilder):
    def test_a_complete_pack_conforms(self):
        row = qs.score_pack(self.build())
        self.assertTrue(row["conforms"], row["conformance_failures"])

    def test_a_missing_chinese_readme_is_named(self):
        row = qs.score_pack(self.build(readme_zh=False))
        self.assertFalse(row["conforms"])
        self.assertIn("no README.zh-CN.md", row["conformance_failures"])

    def test_missing_worked_examples_and_exemplars_are_both_named(self):
        row = qs.score_pack(self.build(worked=False, exemplars=False))
        self.assertEqual(len(row["conformance_failures"]), 2)

    def test_a_pack_outside_the_lifecycle_band_fails(self):
        self.assertFalse(qs.score_pack(self.build(skills=4))["conforms"])

    def test_a_description_that_does_not_say_when_fails(self):
        row = qs.score_pack(self.build(use_when=False))
        self.assertTrue(any("when to use" in f for f in row["conformance_failures"]))

    def test_a_description_that_does_not_name_the_venue_fails(self):
        row = qs.score_pack(self.build(venue_cue=False))
        self.assertTrue(any("name the venue" in f for f in row["conformance_failures"]))

    def test_a_missing_code_library_with_no_stated_reason_fails(self):
        row = qs.score_pack(self.build(code=False))
        self.assertTrue(any("resources/code/" in f for f in row["conformance_failures"]))

    def test_a_missing_code_library_with_a_stated_reason_conforms(self):
        pack = self.build(code=False)
        (pack / "resources" / "README.md").write_text(
            "This is a theory venue, so no econometric code is vendored.\n",
            encoding="utf-8")
        self.assertTrue(qs.score_pack(pack)["conforms"])

    def test_conformance_is_independent_of_the_backlog_score(self):
        # A conforming pack can still have a lot left to do — that is the whole point
        # of separating them.
        row = qs.score_pack(self.build(flags=15, verified_days_ago=300, exec_bridge=0))
        self.assertTrue(row["conforms"])
        self.assertLess(row["score"], 50)


class TestBacklogScore(PackBuilder):
    def test_a_freshly_verified_flagless_deep_pack_scores_near_the_top(self):
        row = qs.score_pack(self.build(verified_days_ago=5, flags=0, exec_bridge=3))
        self.assertGreater(row["score"], 95)

    def test_unresolved_flags_cost_score(self):
        clean = qs.score_pack(self.build(flags=0))["score"]
        flagged = qs.score_pack(self.build(name="Flagged-Journal-Skills", flags=8))["score"]
        self.assertLess(flagged, clean)

    def test_the_flag_penalty_bottoms_out_rather_than_going_negative(self):
        row = qs.score_pack(self.build(flags=200))
        self.assertEqual(row["_breakdown"]["verified"], 0.0)
        self.assertGreater(row["score"], 0)

    def test_a_stale_source_map_costs_score(self):
        fresh = qs.score_pack(self.build(verified_days_ago=10))["score"]
        stale = qs.score_pack(
            self.build(name="Stale-Journal-Skills", verified_days_ago=300))["score"]
        self.assertLess(stale, fresh)

    def test_a_source_map_with_no_date_scores_no_currency(self):
        row = qs.score_pack(self.build(verified_days_ago=None))
        self.assertEqual(row["_breakdown"]["currency"], 0.0)

    def test_the_thinnest_skill_drives_the_floor_not_the_average(self):
        """The average is the statistic that saturated, and it hides the weak file."""
        even_row = qs.score_pack(self.build(body_units=700))
        lopsided_row = qs.score_pack(
            self.build(name="Lopsided-Journal-Skills", body_units=1400, thin_units=200))
        # The lopsided pack has double the average substance and a much worse score.
        self.assertGreater(lopsided_row["avg_substance_units"],
                           even_row["avg_substance_units"])
        self.assertLess(lopsided_row["score"], even_row["score"])

    def test_min_substance_units_is_reported(self):
        row = qs.score_pack(self.build(body_units=700, thin_units=200))
        self.assertLess(row["min_substance_units"], 400)

    def test_execution_wiring_raises_the_score_where_it_applies(self):
        unwired = qs.score_pack(self.build(exec_bridge=0))["score"]
        wired = qs.score_pack(
            self.build(name="Wired-Journal-Skills", exec_bridge=3))["score"]
        self.assertGreater(wired, unwired)

    def test_a_pack_with_no_code_library_is_not_penalised_for_not_wiring_it(self):
        """The dimension leaves the denominator rather than scoring zero.

        A theory venue has nothing to wire to Stata; charging it ten points for that
        would rank it below an empirical pack that is otherwise identical.
        """
        pack = self.build(code=False)
        (pack / "resources" / "README.md").write_text(
            "This is a theory venue, so no econometric code is vendored.\n",
            encoding="utf-8")
        row = qs.score_pack(pack)
        self.assertIsNone(row["_breakdown"]["wiring"])
        wired = qs.score_pack(self.build(name="Wired-Journal-Skills", exec_bridge=3))
        self.assertAlmostEqual(row["score"], wired["score"], delta=1.0)

    def test_the_score_stays_inside_zero_to_one_hundred(self):
        best = qs.score_pack(self.build(verified_days_ago=1, flags=0, exec_bridge=12,
                                        body_units=2000))
        worst = qs.score_pack(self.build(name="Worst-Journal-Skills",
                                         verified_days_ago=None, flags=50,
                                         body_units=1, thin_units=1, exec_bridge=0))
        self.assertLessEqual(best["score"], 100)
        self.assertGreaterEqual(worst["score"], 0)


class TestSaturationReport(unittest.TestCase):
    def test_it_counts_how_many_packs_sit_at_each_ceiling(self):
        rows = [
            {"_breakdown": {"currency": qs.CURRENCY_WEIGHT, "verified": 0.0,
                            "floor": qs.FLOOR_WEIGHT, "evenness": 5.0, "wiring": None}},
            {"_breakdown": {"currency": qs.CURRENCY_WEIGHT, "verified": 10.0,
                            "floor": 5.0, "evenness": 5.0, "wiring": qs.WIRING_WEIGHT}},
        ]
        report = "\n".join(qs.saturation_report(rows))
        self.assertIn("currency    2/2 at ceiling", report)
        self.assertIn("floor       1/2 at ceiling", report)

    def test_a_dimension_that_applies_to_nobody_is_omitted(self):
        rows = [{"_breakdown": {"currency": 1.0, "verified": 1.0, "floor": 1.0,
                                "evenness": 1.0, "wiring": None}}]
        self.assertNotIn("wiring", "\n".join(qs.saturation_report(rows)))


class TestWeights(unittest.TestCase):
    def test_the_scored_dimensions_sum_to_one_hundred(self):
        self.assertEqual(
            qs.CURRENCY_WEIGHT + qs.VERIFIED_WEIGHT + qs.FLOOR_WEIGHT
            + qs.EVENNESS_WEIGHT + qs.WIRING_WEIGHT, 100)

    def test_the_currency_bands_run_from_strict_to_the_hard_gate(self):
        limits = [limit for limit, _ in qs.CURRENCY_BANDS]
        self.assertEqual(limits, sorted(limits))
        # 365 days is the hard failure in tools/freshness_audit.py; a pack at that
        # edge must have no currency credit left.
        self.assertEqual(dict(qs.CURRENCY_BANDS)[365], 4)
        self.assertEqual(qs.CURRENCY_BANDS[-1][1], 0)


if __name__ == "__main__":
    unittest.main()
