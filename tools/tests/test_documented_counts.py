"""Unit tests for the documented-count reconciliation in `audit_repo`.

The journal-selection capability layer is four generated artefacts plus two prose files
that describe them. Both prose files had drifted: they told an agent the venue index held
743 venues (it held 744), that 289 of them had a depth pack (290 did), that the retrieval
vocabulary was "300 terms deep" (900, since the depth was measured and raised), and — in
two files, disagreeing with each other — that the ladder had 1,725 and 1,507 adjacency
edges (1,511). Every one of those numbers is a `wc -l` away from the sentence stating it.

Nothing caught it because the counts that *were* guarded are the ones on the front page:
`check_readme_badges` reconciles the two root READMEs, which is where a reader meets a
number. These files are where the *agent* meets one, at match time, and an agent told the
index is 300 terms deep will go on to describe a tool that no longer exists.

The tests build both halves from scratch, so a failure means the rule changed — except
the last one in each class, which asserts the committed repository satisfies it today.
"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest import mock

from . import context  # noqa: F401  (import for the sys.path side effect)

import audit_repo


VENUE_HEADER = "venue_id\tdisplay_name\tcoverage\n"
VENUE_ROWS = ("a\tA\tdepth\n" "b\tB\tdepth\n" "c\tC\tbreadth\n")


class TestLiveCounts(unittest.TestCase):
    """The live half: numbers read off the artefacts, not off a constant."""

    def build(self, root: Path, *, venues: str = VENUE_HEADER + VENUE_ROWS,
              depth_header: str | None = "900", ladder_rows: int = 4,
              gold_rows: int = 7) -> list[str]:
        sel = root / "shared-resources/journal-selection"
        (sel / "eval").mkdir(parents=True)
        (sel / "venue-index.tsv").write_text(venues, encoding="utf-8")
        header = f"#depth\t{depth_header}\n" if depth_header is not None else ""
        (sel / "scope-postings.tsv").write_text(header + "term\t0:1\n", encoding="utf-8")
        (sel / "ladder.tsv").write_text(
            "from_venue\tto_venue\n" + "".join(f"a\tb{i}\n" for i in range(ladder_rows)),
            encoding="utf-8")
        (sel / "eval/gold-set.tsv").write_text(
            "paper_title\ttrue_venue_id\n" + "".join(f"t{i}\ta\n" for i in range(gold_rows)),
            encoding="utf-8")
        return []

    def live(self, **kwargs) -> tuple[dict[str, int], list[str]]:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.build(root, **kwargs)
            errors: list[str] = []
            with mock.patch.object(audit_repo, "ROOT", root), \
                 mock.patch.object(audit_repo, "VENUE_INDEX",
                                   root / "shared-resources/journal-selection/venue-index.tsv"), \
                 mock.patch.object(audit_repo, "SCOPE_POSTINGS",
                                   root / "shared-resources/journal-selection/scope-postings.tsv"), \
                 mock.patch.object(audit_repo, "LADDER",
                                   root / "shared-resources/journal-selection/ladder.tsv"), \
                 mock.patch.object(audit_repo, "GOLD_SET",
                                   root / "shared-resources/journal-selection/eval/gold-set.tsv"):
                return audit_repo.live_documented_counts(errors), errors

    def test_venue_rows_do_not_count_the_header(self):
        values, _ = self.live()
        self.assertEqual(values["venues"], 3)

    def test_coverage_splits_depth_from_breadth(self):
        values, _ = self.live()
        self.assertEqual((values["depth_venues"], values["breadth_venues"]), (2, 1))

    def test_the_retrieval_depth_comes_from_the_postings_header(self):
        values, _ = self.live(depth_header="1200")
        self.assertEqual(values["postings_depth"], 1200)

    def test_a_postings_file_with_no_depth_header_is_an_error(self):
        values, errors = self.live(depth_header=None)
        self.assertNotIn("postings_depth", values)
        self.assertEqual(len(errors), 1)
        self.assertIn("#depth", errors[0])

    def test_ladder_and_gold_rows_are_counted(self):
        values, _ = self.live(ladder_rows=11, gold_rows=5)
        self.assertEqual((values["ladder_edges"], values["gold_papers"]), (11, 5))


class TestDocumentedCounts(unittest.TestCase):
    """The prose half: every stated number must equal the artefact it describes."""

    def run_check(self, prose: str) -> list[str]:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs").mkdir()
            (root / "docs/capability.md").write_text(prose, encoding="utf-8")
            errors: list[str] = []
            entry = ("docs/capability.md", r"index of \*\*([\d,]+) venues\*\*", "venues")
            with mock.patch.object(audit_repo, "ROOT", root), \
                 mock.patch.object(audit_repo, "DOCUMENTED_COUNTS", [entry]), \
                 mock.patch.object(audit_repo, "live_documented_counts",
                                   lambda errs: {"venues": 744}):
                audit_repo.check_documented_counts(errors)
            return errors

    def test_a_matching_count_passes(self):
        self.assertEqual(self.run_check("an index of **744 venues** covering everything"), [])

    def test_the_actual_drift_fails(self):
        errors = self.run_check("an index of **743 venues** covering everything")
        self.assertEqual(len(errors), 1)
        self.assertIn("states 743", errors[0])
        self.assertIn("744", errors[0])

    def test_a_thousands_separator_is_not_a_difference(self):
        # "1,511 adjacency edges" and "1511" describe the same file.
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs").mkdir()
            (root / "docs/capability.md").write_text("**1,511 adjacency edges**",
                                                     encoding="utf-8")
            errors: list[str] = []
            entry = ("docs/capability.md", r"\*\*([\d,]+) adjacency edges\*\*",
                     "ladder_edges")
            with mock.patch.object(audit_repo, "ROOT", root), \
                 mock.patch.object(audit_repo, "DOCUMENTED_COUNTS", [entry]), \
                 mock.patch.object(audit_repo, "live_documented_counts",
                                   lambda errs: {"ladder_edges": 1511}):
                audit_repo.check_documented_counts(errors)
            self.assertEqual(errors, [])

    def test_every_occurrence_is_checked_not_just_the_first(self):
        errors = self.run_check(
            "an index of **744 venues**\n\nlater: an index of **743 venues**\n")
        self.assertEqual(len(errors), 1)
        self.assertIn("states 743", errors[0])

    def test_deleting_the_sentence_fails_rather_than_passing_silently(self):
        # The failure mode a "check what is written" rule invites: a count that stops
        # being stated stops being wrong. That is not the same as being right.
        errors = self.run_check("the index covers a lot of venues")
        self.assertEqual(len(errors), 1)
        self.assertIn("no longer states", errors[0])

    def test_the_committed_capability_docs_agree_with_their_artefacts(self):
        errors: list[str] = []
        audit_repo.check_documented_counts(errors)
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
