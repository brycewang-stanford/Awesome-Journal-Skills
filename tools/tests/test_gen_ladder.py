"""Unit tests for the alias matcher behind the resubmission ladder.

`gen_ladder` builds the venue-adjacency graph by scanning every pack's prose for the
names of other venues. That scan runs 743 aliases over the whole corpus, so it uses a
hand-rolled Aho-Corasick automaton — no dependency, and one pass instead of 743. Two
things can go wrong with it and neither shows up as a crash:

* a **missed** alias silently thins the ladder, and
* a **spurious** alias wires two unrelated venues together, which is worse: the ladder
  is advice about where to send a rejected paper next.

The substring trap is the concrete one. "AER" occurs inside "AERONAUTICS"; matching raw
substrings once made every aerospace pack adjacent to the American Economic Review.
"""

from __future__ import annotations

import unittest

from . import context  # noqa: F401  (import for the sys.path side effect)

from gen_ladder import alias_automaton, alias_mentions, aliases_for


def mentions(text: str, aliases: list[str]) -> set[str]:
    return set(alias_mentions(text, alias_automaton(aliases)))


class TestAliasMatching(unittest.TestCase):
    def test_finds_a_free_standing_name(self):
        self.assertEqual(
            mentions("Consider submitting to the Journal of Finance next.",
                     ["Journal of Finance"]),
            {"Journal of Finance"})

    def test_finds_several_aliases_in_one_pass(self):
        found = mentions("Alternatives include QJE, AER and the Review of Economic Studies.",
                         ["QJE", "AER", "Review of Economic Studies"])
        self.assertEqual(found, {"QJE", "AER", "Review of Economic Studies"})

    def test_an_acronym_inside_a_longer_word_is_not_a_mention(self):
        # The failure this guard exists for: "AER" inside "AERONAUTICS".
        self.assertEqual(mentions("Journal of AERONAUTICS and space", ["AER"]), set())

    def test_a_name_touching_punctuation_still_matches(self):
        # Only letters and digits block a boundary; a comma or bracket does not.
        self.assertEqual(mentions("(AER), among others", ["AER"]), {"AER"})
        self.assertEqual(mentions("AER.", ["AER"]), {"AER"})

    def test_a_trailing_letter_blocks_the_match(self):
        self.assertEqual(mentions("AERx", ["AER"]), set())

    def test_a_leading_letter_blocks_the_match(self):
        self.assertEqual(mentions("xAER", ["AER"]), set())

    def test_a_chinese_alias_matches_without_a_word_boundary(self):
        # Chinese prose has no spaces, so the Latin boundary rule cannot apply to it.
        self.assertEqual(mentions("可以考虑投稿《经济研究》或其他期刊", ["经济研究"]),
                         {"经济研究"})

    def test_an_alias_that_is_a_prefix_of_another_is_still_found(self):
        # The automaton's failure links exist for exactly this: a shorter alias ending
        # inside a longer one must still be reported.
        found = mentions("the Journal of Finance and Economics is separate",
                         ["Journal of Finance", "Journal of Finance and Economics"])
        self.assertIn("Journal of Finance and Economics", found)

    def test_an_absent_alias_is_not_invented(self):
        self.assertEqual(mentions("no venues named here", ["QJE"]), set())

    def test_an_empty_corpus_yields_nothing(self):
        self.assertEqual(mentions("", ["QJE"]), set())


class TestAliasesFor(unittest.TestCase):
    def row(self, display_name: str, venue_id: str = "some-venue") -> dict:
        return {"display_name": display_name, "venue_id": venue_id}

    def test_a_long_english_name_is_its_own_alias(self):
        aliases = aliases_for(self.row("Quarterly Journal of Economics"), "")
        self.assertIn("Quarterly Journal of Economics", aliases)

    def test_a_chinese_name_is_an_alias(self):
        self.assertIn("经济研究", aliases_for(self.row("经济研究"), ""))

    def test_a_declared_acronym_that_fits_the_name_is_an_alias(self):
        aliases = aliases_for(
            self.row("Quarterly Journal of Economics", "quarterly-journal-of-economics"),
            "The Quarterly Journal of Economics (QJE) publishes ...")
        self.assertIn("QJE", aliases)

    def test_a_society_acronym_that_fits_nothing_is_not_an_alias(self):
        # "Anesthesiology (ASA)" is the American Society of Anesthesiologists. Left
        # unguarded, it made every sociology pack look adjacent to Anesthesiology.
        aliases = aliases_for(self.row("Anesthesiology", "anesthesiology"),
                              "Anesthesiology (ASA) is published by ...")
        self.assertNotIn("ASA", aliases)

    def test_aliases_shorter_than_three_characters_are_dropped(self):
        self.assertTrue(all(len(a) >= 3 for a in aliases_for(self.row("AI"), "")))

    def test_a_short_generic_english_name_is_not_an_alias_on_its_own(self):
        # A common short word as a venue name would match everywhere. Only long names
        # and acronym-shaped ones become aliases.
        self.assertNotIn("Science", aliases_for(self.row("Science", "science"), ""))


if __name__ == "__main__":
    unittest.main()
