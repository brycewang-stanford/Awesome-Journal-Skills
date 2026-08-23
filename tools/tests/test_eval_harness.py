"""Unit tests for the eval harness's own honesty rules.

The retrieval number is only worth publishing if the machinery around it is sound: a
split that cannot drift, a lane-violation rule that does not flatter itself, and a
coverage floor that withholds a configuration rather than reporting it from a handful
of papers. Those rules are what these tests hold in place — the recall figure itself is
measured by `tools/eval_journal_match.py` against the committed gold set.
"""

from __future__ import annotations

import unittest
from collections import Counter

from . import context  # noqa: F401  (import for the sys.path side effect)

import eval_journal_match as ev
from build_eval_set import clean, split_of


class TestSplit(unittest.TestCase):
    """`dev` tunes, `test` reports. The split has to survive the repository growing."""

    def test_the_same_title_always_lands_on_the_same_side(self):
        self.assertEqual(split_of("Minimum Wages and Employment"),
                         split_of("Minimum Wages and Employment"))

    def test_the_assignment_is_case_insensitive(self):
        # Titles are re-harvested from prose, so casing drifts between rebuilds. If
        # that moved a paper across the split, `dev` and `test` would slowly mix and
        # the headline would quietly become a number the constants were fitted to.
        self.assertEqual(split_of("The Garbage Can"), split_of("the garbage can"))

    def test_the_halves_come_out_roughly_even(self):
        counts = Counter(split_of(f"paper number {i}") for i in range(2000))
        self.assertEqual(set(counts), {"dev", "test"})
        self.assertLess(abs(counts["dev"] - counts["test"]) / 2000, 0.05)


class TestClean(unittest.TestCase):
    def test_collapses_whitespace_and_strips_markup(self):
        self.assertEqual(clean("**Minimum**   wages\nand   employment"),
                         "Minimum wages and employment")

    def test_strips_trailing_punctuation(self):
        self.assertEqual(clean("A study of firms,"), "A study of firms")


class TestLanesConflict(unittest.TestCase):
    """Only the unambiguous direction counts as a violation."""

    def test_an_empirical_paper_at_a_theory_only_venue_is_a_violation(self):
        self.assertTrue(ev.lanes_conflict("empirical", "theory"))

    def test_a_theory_paper_at_an_empirical_venue_is_not(self):
        # Theory papers appear in empirical venues routinely; counting that would
        # inflate the violation rate with cases no author would call an error.
        self.assertFalse(ev.lanes_conflict("theory", "empirical"))

    def test_a_venue_that_publishes_both_is_never_a_violation(self):
        self.assertFalse(ev.lanes_conflict("empirical", "empirical+theory"))

    def test_a_paper_with_no_declared_lane_is_never_a_violation(self):
        self.assertFalse(ev.lanes_conflict("", "theory"))


class TestBuildQuery(unittest.TestCase):
    ROW = {"paper_title": "Minimum Wages and Employment",
           "context": "a natural experiment in fast food"}

    def test_the_headline_query_is_the_bare_title(self):
        self.assertEqual(ev.build_query(self.ROW, "title", {}),
                         "Minimum Wages and Employment")

    def test_the_discipline_configurations_query_the_same_text(self):
        # They differ in the *prior*, not in the words; if they differed in both, the
        # comparison between them would measure two changes at once.
        for mode in ("title", "title+discipline", "oracle-discipline"):
            self.assertEqual(ev.build_query(self.ROW, mode, {}),
                             "Minimum Wages and Employment")

    def test_the_context_configuration_appends_the_exemplar_gloss(self):
        query = ev.build_query(self.ROW, "title+context", {})
        self.assertIn("natural experiment", query)
        self.assertTrue(query.startswith("Minimum Wages and Employment"))

    def test_a_row_without_a_gloss_falls_back_to_the_title(self):
        row = dict(self.ROW, context="")
        self.assertEqual(ev.build_query(row, "title+context", {}), row["paper_title"])

    def test_the_abstract_configuration_skips_papers_with_no_abstract(self):
        # Returning the bare title instead would silently pad the abstract row with
        # title-only results and report the blend as `title+abstract`.
        self.assertIsNone(ev.build_query(self.ROW, "title+abstract", {}))

    def test_the_abstract_configuration_appends_the_term_bag(self):
        abstracts = {"minimum wages and employment": "employment fast food wages"}
        query = ev.build_query(self.ROW, "title+abstract", abstracts)
        self.assertIn("fast food", query)

    def test_every_mode_the_harness_runs_is_one_build_query_understands(self):
        for mode in ev.MODES:
            ev.build_query({"paper_title": "t", "context": "c"}, mode, {})

    def test_an_unknown_configuration_is_an_error_not_a_silent_title(self):
        with self.assertRaises(ValueError):
            ev.build_query(self.ROW, "title+telepathy", {})


class TestCoverageFloor(unittest.TestCase):
    def test_the_floor_is_a_quarter_of_the_split(self):
        # A configuration measured on 5% of the papers is a different experiment, not
        # a comparable row; the harness withholds it and says so.
        self.assertEqual(ev.MIN_CONFIG_COVERAGE, 0.25)

    def test_every_reported_configuration_is_described(self):
        # An undescribed row in RESULTS.md is a number with no stated interpretation.
        for mode in ev.MODES:
            self.assertIn(mode, ev.DESCRIPTIONS, mode)


if __name__ == "__main__":
    unittest.main()
