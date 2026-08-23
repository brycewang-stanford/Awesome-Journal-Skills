"""Unit tests for `match_lib` — the retrieval step behind every venue recommendation.

Both the product (`tools/match_venues.py`) and the metric (`tools/eval_journal_match.py`)
go through this module, so a change here moves the recommendation an author sees *and*
the number CI gates, in the same direction. The eval measures whether the ranking is
good on average. These tests pin the *behaviours* the weighting constants were chosen to
produce, each of which was a real failure once: a design conference topping a
minimum-wage paper on the word "design", a cancer paper offered a text-generation
conference on the word "generation", a hard discipline filter deleting the true venue.

Every fixture is a hand-built index written to a temp directory. Reading the committed
743-venue index instead would make these tests re-measure the eval, and would let a
wrong rule pass as long as the committed data agreed with it.
"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from . import context  # noqa: F401  (import for the sys.path side effect)

import match_lib
from match_lib import VenueMatcher, IndexMismatch
from venue_lib import index_digest


def venue(venue_id: str, discipline: str = "economics", *, lane: str = "empirical",
          region: str = "international", venue_type: str = "journal",
          coverage: str = "depth") -> dict:
    return {
        "venue_id": venue_id,
        "display_name": venue_id,
        "coverage": coverage,
        "venue_type": venue_type,
        "discipline": discipline,
        "region": region,
        "lane": lane,
        "tier": "field",
    }


def write_postings(path: Path, venues: list[dict], postings: dict[str, list[tuple[int, int]]],
                   *, depth: int = 300, declared_rows: int | None = None,
                   digest: str | None = None) -> None:
    """Write a `scope-postings.tsv` for `venues`, term -> [(row, rank), ...]."""
    lines = [
        f"#venues\t{len(venues) if declared_rows is None else declared_rows}",
        f"#digest\t{digest if digest is not None else index_digest([v['venue_id'] for v in venues])}",
        f"#depth\t{depth}",
        "#term\trow:rank,...",
    ]
    for term, refs in sorted(postings.items()):
        lines.append(term + "\t" + ",".join(f"{row}:{rank}" for row, rank in refs))
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


# A corpus this small would make every term worthless: IDF is log(n / (1 + df)), so in
# a two-venue index even a term unique to one venue scores log(2/2) = 0 and is dropped.
# Padding the fixtures to a realistic corpus size is not a workaround — it is the
# condition the weighting assumes, and stating it here keeps a future reader from
# "fixing" a test by loosening IDF.
CORPUS_SIZE = 40


class MatcherFixture(unittest.TestCase):
    """Base class giving each test a scratch directory to build indexes in."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)

    def build(self, venues: list[dict], postings: dict[str, list[tuple[int, int]]],
              adjacency: dict[str, set[str]] | None = None, *,
              pad: bool = True, **kwargs) -> VenueMatcher:
        """Build a matcher over `venues`, padded out to a realistic corpus size.

        The padding venues carry no postings, so they never appear in a result; they
        exist only to give IDF a denominator that behaves the way it does in production.
        """
        venues = list(venues)
        if pad:
            venues += [venue(f"_pad-{i}", "other")
                       for i in range(max(0, CORPUS_SIZE - len(venues)))]
        path = self.tmp / "postings.tsv"
        write_postings(path, venues, postings, **kwargs)
        return VenueMatcher(venues=venues, postings_path=path, adjacency=adjacency or {})

    def ranked_ids(self, hits) -> list[str]:
        return [hit.venue["venue_id"] for hit in hits]


class TestIndexIntegrity(MatcherFixture):
    def test_a_row_count_mismatch_is_refused(self):
        venues = [venue("a"), venue("b")]
        with self.assertRaises(IndexMismatch):
            self.build(venues, {"panel": [(0, 0)]}, pad=False, declared_rows=3)

    def test_a_reordered_index_is_refused(self):
        """The failure the digest exists for, and the only one a count cannot catch.

        Postings address venues by row number. Reorder the index without rebuilding
        them and every file still parses, every row count still agrees, and every
        keyword is now attributed to the wrong venue — plausibly, and in silence.
        """
        venues = [venue("a"), venue("b")]
        path = self.tmp / "postings.tsv"
        write_postings(path, venues, {"panel": [(0, 0)]})
        with self.assertRaises(IndexMismatch):
            VenueMatcher(venues=[venues[1], venues[0]], postings_path=path, adjacency={})

    def test_a_matching_pair_loads(self):
        venues = [venue("a"), venue("b")]
        matcher = self.build(venues, {"panel": [(0, 0)]}, pad=False)
        self.assertEqual(len(matcher.venues), 2)

    def test_a_postings_file_without_a_digest_still_loads(self):
        # Older postings files carry no digest line. Refusing them would break the
        # matcher on any checkout predating the digest rather than degrade gracefully:
        # the count check still applies, only the ordering check is skipped.
        venues = [venue(f"v{i}") for i in range(CORPUS_SIZE)]
        path = self.tmp / "postings.tsv"
        path.write_text(f"#venues\t{CORPUS_SIZE}\n#depth\t300\npanel\t0:0\n",
                        encoding="utf-8")
        matcher = VenueMatcher(venues=venues, postings_path=path, adjacency={})
        self.assertEqual(self.ranked_ids(matcher.rank("panel")), ["v0"])


class TestQueryTerms(unittest.TestCase):
    def test_a_query_carries_both_words_and_adjacent_bigrams(self):
        terms = VenueMatcher.query_terms("minimum wage employment")
        self.assertIn("minimum", terms)
        self.assertIn("minimum wage", terms)
        self.assertIn("wage employment", terms)
        # not a bigram: the words are not adjacent
        self.assertNotIn("minimum employment", terms)


class TestRanking(MatcherFixture):
    def test_a_venue_matching_many_terms_beats_one_lucky_rare_word(self):
        """The coordination rule, and the case that produced it.

        A design conference topped a minimum-wage paper's shortlist on the single word
        "design" while the labour-economics journals under it matched six terms each.
        One term is a coincidence; agreement across several is evidence.
        """
        venues = [venue("labour"), venue("design-conf")]
        # The lone term is given rank 0 (the strongest position) in its venue, and each
        # of the many terms is given a weaker rank, so coordination has to do the work.
        postings = {
            "minimum": [(0, 5)],
            "wage": [(0, 5)],
            "employment": [(0, 5)],
            "labour": [(0, 5)],
            "design": [(1, 0)],
        }
        matcher = self.build(venues, postings)
        self.assertEqual(
            self.ranked_ids(matcher.rank("minimum wage employment labour design"))[0],
            "labour",
        )

    def test_an_early_keyword_outweighs_a_late_one(self):
        # Term 1 of 300 is what a venue is about; term 280 is something it mentioned.
        venues = [venue("about-it"), venue("mentioned-it")]
        matcher = self.build(venues, {"panel": [(0, 0), (1, 299)]})
        self.assertEqual(self.ranked_ids(matcher.rank("panel"))[0], "about-it")

    def test_a_rarer_term_outweighs_a_common_one(self):
        venues = [venue(f"v{i}") for i in range(10)]
        postings = {
            "common": [(i, 0) for i in range(9)],   # in nearly every venue
            "rare": [(9, 0)],                        # in exactly one
        }
        matcher = self.build(venues, postings, pad=False)
        self.assertEqual(self.ranked_ids(matcher.rank("common rare"))[0], "v9")

    def test_a_term_in_every_venue_contributes_nothing(self):
        # IDF is non-positive once a term is everywhere, and the loader drops it, so a
        # query of only that term retrieves no candidates at all rather than all of them.
        venues = [venue(f"v{i}") for i in range(4)]
        matcher = self.build(venues, {"everywhere": [(i, 0) for i in range(4)]},
                             pad=False)
        self.assertEqual(matcher.rank("everywhere"), [])

    def test_ties_break_deterministically_by_venue_id(self):
        venues = [venue("zzz"), venue("aaa")]
        matcher = self.build(venues, {"panel": [(0, 0), (1, 0)]})
        self.assertEqual(self.ranked_ids(matcher.rank("panel")), ["aaa", "zzz"])

    def test_a_query_matching_nothing_returns_nothing(self):
        matcher = self.build([venue("a")], {"panel": [(0, 0)]})
        self.assertEqual(matcher.rank("cosmology"), [])

    def test_limit_truncates_from_the_top(self):
        venues = [venue(f"v{i}") for i in range(5)]
        matcher = self.build(venues, {"panel": [(i, i) for i in range(5)]})
        self.assertEqual(len(matcher.rank("panel", limit=2)), 2)
        self.assertEqual(
            self.ranked_ids(matcher.rank("panel", limit=2)),
            self.ranked_ids(matcher.rank("panel"))[:2],
        )

    def test_hits_carry_the_terms_that_earned_them(self):
        """A nonsense hit has to be visible as one, which means naming its terms."""
        venues = [venue("a")]
        matcher = self.build(venues, {"minimum": [(0, 0)], "wage": [(0, 1)]})
        hit = matcher.rank("minimum wage")[0]
        self.assertEqual(set(t for t, _ in hit.terms), {"minimum", "wage"})
        self.assertIn("minimum", hit.why())


class TestPhraseHandling(MatcherFixture):
    def test_a_phrase_keyword_is_weaker_evidence_than_an_equally_rare_word(self):
        """`PHRASE_BONUS` is below 1.0, which is the counter-intuitive half of it.

        TF-IDF bigrams pulled out of prose are mostly incidental collocations ("recent
        work", "panel data"); a rare unigram is usually a subject term. Setting this
        above 1.0 — the intuitive choice — cost 17 points of recall@10.

        Asserted on the stored weights rather than on a ranking, because a query
        containing a phrase also contains its words: the phrase venue would win any
        head-to-head on coordination alone, which is a different rule being tested
        elsewhere and would hide a sign error here.
        """
        self.assertLess(match_lib.PHRASE_BONUS, 1.0)
        venues = [venue("phrase-venue"), venue("word-venue")]
        matcher = self.build(venues, {
            "natural experiment": [(0, 0)],
            "instrument": [(1, 0)],
        })
        (_, phrase_weight), = matcher.postings["natural experiment"]
        (_, word_weight), = matcher.postings["instrument"]
        self.assertLess(phrase_weight, word_weight)

    def test_a_phrase_keyword_is_also_reachable_by_its_parts(self):
        # A query that says "experiment" without "natural" should still find the venue,
        # at a discount — the words inside a phrase add little, but not nothing.
        self.assertGreater(match_lib.PART_DISCOUNT, 0)
        venues = [venue("a")]
        matcher = self.build(venues, {"natural experiment": [(0, 0)]})
        whole = matcher.rank("natural experiment")[0].score
        part = matcher.rank("experiment")[0].score
        self.assertGreater(part, 0)
        self.assertGreater(whole, part)


class TestDisciplineSpread(MatcherFixture):
    def test_a_term_spread_across_disciplines_is_discounted(self):
        """Why entropy and not document frequency.

        "sensor" and "generation" are used by the same *number* of venues as a real
        subject term, so IDF cannot separate them — but they are used across a dozen
        unrelated subjects, which is why a paper on a cytosolic DNA sensor was offered
        SenSys and IPSN, and why "Hallmarks of Cancer: The Next Generation" was offered
        a natural-language-generation conference.
        """
        # `focused` and `spread` have identical document frequency (four venues each);
        # only the discipline mix differs.
        venues = [
            venue("bio-1", "life-sciences"), venue("bio-2", "life-sciences"),
            venue("bio-3", "life-sciences"), venue("bio-4", "life-sciences"),
            venue("net", "cs-ai"), venue("med", "medicine"),
            venue("econ", "economics"), venue("phys", "physics"),
        ]
        postings = {
            "focused": [(0, 0), (1, 0), (2, 0), (3, 0)],   # one discipline
            "spread": [(4, 0), (5, 0), (6, 0), (7, 0)],    # four disciplines
        }
        matcher = self.build(venues, postings)
        focused_score = matcher.rank("focused")[0].score
        spread_score = matcher.rank("spread")[0].score
        self.assertGreater(focused_score, spread_score)

    def test_a_term_in_a_single_venue_is_not_discounted(self):
        # One posting has no discipline distribution to measure; the guard exists so a
        # zero-entropy term is not silently scaled.
        venues = [venue("a"), venue("b", "cs-ai")]
        matcher = self.build(venues, {"unique": [(0, 0)], "other": [(1, 0)]})
        self.assertGreater(matcher.rank("unique")[0].score, 0)


class TestDisciplinePrior(MatcherFixture):
    def setUp(self):
        super().setUp()
        self.venues = [venue("econ-journal", "economics"),
                       venue("finance-journal", "finance"),
                       venue("bio-journal", "life-sciences")]
        self.postings = {"panel": [(0, 0), (1, 0), (2, 0)]}

    def test_the_named_discipline_is_boosted_but_others_survive(self):
        matcher = self.build(self.venues, self.postings)
        ids = self.ranked_ids(matcher.rank("panel", discipline="finance"))
        self.assertEqual(ids[0], "finance-journal")
        # A prior, not a filter: the rest are ranked below, not deleted.
        self.assertEqual(len(ids), 3)

    def test_an_adjacent_discipline_is_boosted_less_than_the_named_one(self):
        self.assertLess(match_lib.ADJACENT_BOOST, match_lib.DISCIPLINE_BOOST)
        matcher = self.build(self.venues, self.postings,
                             adjacency={"finance": {"economics"}})
        ids = self.ranked_ids(matcher.rank("panel", discipline="finance"))
        self.assertEqual(ids, ["finance-journal", "econ-journal", "bio-journal"])

    def test_only_discipline_hard_filters_and_keeps_adjacents(self):
        matcher = self.build(self.venues, self.postings,
                             adjacency={"finance": {"economics"}})
        ids = self.ranked_ids(
            matcher.rank("panel", discipline="finance", only_discipline=True))
        self.assertEqual(ids, ["finance-journal", "econ-journal"])
        self.assertNotIn("bio-journal", ids)

    def test_a_wrong_discipline_guess_costs_ranking_not_the_answer(self):
        """Why the default is a prior. Step 1 is a judgement and will sometimes be
        wrong; under a hard filter a wrong guess deletes the true venue outright."""
        matcher = self.build(self.venues, self.postings)
        ids = self.ranked_ids(matcher.rank("panel", discipline="life-sciences"))
        self.assertIn("finance-journal", ids)


class TestFilters(MatcherFixture):
    def setUp(self):
        super().setUp()
        self.venues = [
            venue("a", lane="empirical", region="china", venue_type="journal",
                  coverage="depth"),
            venue("b", lane="theory", region="international", venue_type="conference",
                  coverage="breadth"),
        ]
        self.postings = {"panel": [(0, 0), (1, 0)]}

    def test_exclude_drops_a_venue_that_already_rejected_the_paper(self):
        matcher = self.build(self.venues, self.postings)
        self.assertEqual(self.ranked_ids(matcher.rank("panel", exclude={"a"})), ["b"])

    def test_lane_matches_as_a_substring(self):
        # `lane` holds compound values such as "empirical+theory", so the filter is a
        # containment test rather than equality.
        matcher = self.build(self.venues, self.postings)
        self.assertEqual(self.ranked_ids(matcher.rank("panel", lane="empirical")), ["a"])

    def test_region_type_and_coverage_filter_exactly(self):
        matcher = self.build(self.venues, self.postings)
        self.assertEqual(self.ranked_ids(matcher.rank("panel", region="china")), ["a"])
        self.assertEqual(
            self.ranked_ids(matcher.rank("panel", venue_type="conference")), ["b"])
        self.assertEqual(
            self.ranked_ids(matcher.rank("panel", coverage="breadth")), ["b"])

    def test_filters_compose(self):
        matcher = self.build(self.venues, self.postings)
        self.assertEqual(
            matcher.rank("panel", region="china", venue_type="conference"), [])


if __name__ == "__main__":
    unittest.main()
