"""Unit tests for the subject-vocabulary harvest.

`fetch_venue_topics` adds a second vocabulary per venue — what it publishes about,
taken from the titles of its own articles — beside the one derived from each pack's
prose. Everything network-facing is left to the maintainer pass; what is tested here is
the part that decides *whose* titles a venue gets, and that is the part where a mistake
does not degrade the ranking but replaces it.

The three failure modes the fixtures below are drawn from:

* **an alternate title that belongs to someone else.** Crossref returns *American
  Economic Journal: Economic Policy* for a search on *Economic Policy*, and it carries
  "Economic Policy" among its alternate titles — so an alias rule handed the Oxford
  journal the AEJ's article stream, silently and plausibly.
* **a conference series that nobody writes the same way twice.** The index says "ACM
  SIGCOMM"; DBLP says "ACM SIGCOMM Conference (SIGCOMM)". Requiring string equality
  across that gap resolved none of the first ninety conferences.
* **a gold paper harvested back into the index it is used to score.** The gold set is
  the packs' exemplar libraries: real papers, published in the venue being harvested.
"""

from __future__ import annotations

import unittest
import unittest.mock
from pathlib import Path

from . import context  # noqa: F401  (import for the sys.path side effect)

import fetch_venue_topics as fvt


class TestNormalisation(unittest.TestCase):
    def test_article_words_do_not_make_a_different_journal(self):
        self.assertEqual(fvt.norm_name("The Journal of Finance"),
                         fvt.norm_name("Journal of Finance"))

    def test_an_ampersand_reads_as_and(self):
        self.assertEqual(fvt.norm_name("Accounting & Finance"),
                         fvt.norm_name("Accounting and Finance"))

    def test_punctuation_and_case_are_not_differences(self):
        self.assertEqual(fvt.norm_name("AEJ: Microeconomics"),
                         fvt.norm_name("aej microeconomics"))

    def test_two_different_journals_stay_different(self):
        self.assertNotEqual(fvt.norm_name("Economic Policy"),
                            fvt.norm_name("American Economic Journal Economic Policy"))

    def test_cjk_survives_normalisation(self):
        self.assertEqual(fvt.norm_name("《经济研究》"), "经济研究")


class TestCleanTitle(unittest.TestCase):
    def test_publisher_markup_is_stripped(self):
        self.assertEqual(
            fvt.clean_title("Debiasing and <i>t</i>-Tests for Synthetic Controls"),
            "Debiasing and t -Tests for Synthetic Controls")

    def test_entities_are_unescaped(self):
        self.assertEqual(fvt.clean_title("Risk &amp; Return"), "Risk & Return")

    def test_deposited_layout_whitespace_collapses(self):
        self.assertEqual(
            fvt.clean_title("The Effect of Education Policy on Crime:\n"
                            "                    An Intergenerational Perspective"),
            "The Effect of Education Policy on Crime: An Intergenerational Perspective")


class TestDblpRules(unittest.TestCase):
    """Four rules, each an equality. DBLP's own search is fuzzy; this must not be."""

    def rule(self, target: str, venue: str, acronym: str = "") -> str | None:
        return fvt._dblp_rules(fvt.norm_name(target), venue, acronym)

    def test_the_full_name_matches_with_the_acronym_stripped(self):
        self.assertEqual(
            self.rule("ACM Conference on Recommender Systems",
                      "ACM Conference on Recommender Systems (RecSys)", "RecSys"),
            "dblp-venue")

    def test_an_index_name_that_is_the_acronym_matches(self):
        self.assertEqual(self.rule("RecSys", "ACM Conference on ... (RecSys)", "RecSys"),
                         "dblp-acronym")

    def test_an_organisation_prefix_the_index_keeps_is_not_a_difference(self):
        self.assertEqual(
            self.rule("ACM MobiCom",
                      "International Conference on Mobile Computing and Networking "
                      "(MobiCom)", "MobiCom"),
            "dblp-org-acronym")

    def test_a_generic_word_dblp_adds_in_front_is_not_a_difference(self):
        self.assertEqual(
            self.rule("ACM SIGACCESS Conference on Computers and Accessibility",
                      "International ACM SIGACCESS Conference on Computers and "
                      "Accessibility (ASSETS)", "ASSETS"),
            "dblp-generic-prefix")

    def test_a_different_conference_does_not_match(self):
        # What DBLP actually offers first for "International Conference on Software
        # Engineering".
        self.assertIsNone(
            self.rule("International Conference on Software Engineering",
                      "International Conference on Conceptual Modeling (ER)", "ER"))

    def test_a_meaningful_word_in_front_is_a_different_conference(self):
        # "Workshop on X" is not "X", and neither is a subject word.
        self.assertIsNone(
            self.rule("Conference on Robot Learning",
                      "Wireless Conference on Robot Learning (WCoRL)", "WCoRL"))

    def test_an_acronym_alone_cannot_carry_an_unrelated_series(self):
        self.assertIsNone(self.rule("ACM MobiCom", "Some Other Meeting (SOM)", "SOM"))

    def test_two_sponsors_describing_one_meeting_are_one_meeting(self):
        self.assertEqual(
            self.rule("ACM Conference on Intelligent User Interfaces",
                      "International Conference on Intelligent User Interfaces (IUI)",
                      "IUI"),
            "dblp-core-name")

    def test_a_regional_sibling_conference_is_not_the_same_conference(self):
        # The reason "european" is not droppable: the International, European and Asian
        # conferences on machine learning are three venues, and two of them are here.
        self.assertIsNone(
            self.rule("International Conference on Machine Learning",
                      "European Conference on Machine Learning (ECML)", "ECML"))

    def test_a_workshop_is_not_the_conference_it_attaches_to(self):
        # The reason "workshop" is not droppable either.
        self.assertIsNone(
            self.rule("Conference on Neural Information Processing Systems",
                      "Workshop on Neural Information Processing Systems (WNIPS)",
                      "WNIPS"))

    def test_a_short_remainder_cannot_carry_a_match(self):
        # Two titles that meet only at a two-word remainder have not been shown to be
        # the same venue; `_CORE_MIN_WORDS` is what stops them.
        self.assertIsNone(
            self.rule("ACM Conference on Data", "IEEE Symposium on Data (SD)", "SD"))

    def test_a_longer_formal_name_does_not_match_a_shorter_official_one(self):
        # DBLP calls it "ACM SIGMOD Conference"; the breadth profile spells out
        # "International Conference on Management of Data". Unresolved is the right
        # answer here — a guess would hand this venue some other series' vocabulary.
        self.assertIsNone(
            self.rule("ACM SIGMOD International Conference on Management of Data",
                      "ACM SIGMOD Conference (SIGMOD)", "SIGMOD"))


class TestAcronymCorroboration(unittest.TestCase):
    """An acronym is not an identifier, and DBLP's first hit for one may be anyone."""

    def check(self, description: str, dblp_name: str) -> bool:
        with unittest.mock.patch.object(fvt, "pack_title_text",
                                        lambda v: fvt.norm_name(description)):
            return fvt.acronym_corroborated({"pack_dir": "X-Skills"}, dblp_name)

    STORAGE = ("A 12-skill depth pack for USENIX FAST, the USENIX Conference on File "
               "and Storage Technologies")

    def test_the_wrong_conference_behind_a_shared_acronym_is_refused(self):
        # The real finding: `FAST-Skills` is USENIX's storage conference; DBLP's first
        # venue hit for "FAST" is Formal Aspects in Security and Trust, and the acronym
        # rule took it.
        self.assertFalse(self.check(self.STORAGE,
                                    "Formal Aspects in Security and Trust (FAST)"))

    def test_the_right_conference_is_believed(self):
        self.assertTrue(self.check(
            self.STORAGE, "USENIX Conference on File and Storage Technologies (FAST)"))

    def test_organisation_and_structure_words_carry_no_evidence(self):
        # Every conference is an "International ACM Conference on" something.
        self.assertFalse(self.check(
            "A depth pack for the study of volcanoes",
            "International ACM Conference on Distributed Computing (X)"))

    def test_a_name_that_is_its_own_acronym_needs_only_that_word(self):
        # "ACM SIGMOD Conference" leaves one content word; demanding two of one would
        # be a rejection dressed as a rule.
        self.assertTrue(self.check("Twelve skills for papers at ACM SIGMOD",
                                   "ACM SIGMOD Conference (SIGMOD)"))

    def test_a_pack_that_says_nothing_about_itself_is_not_disagreement(self):
        with unittest.mock.patch.object(fvt, "pack_title_text", lambda v: ""):
            self.assertTrue(fvt.acronym_corroborated({"pack_dir": "X"}, "Anything (X)"))

    def test_a_breadth_profile_has_no_pack_to_read(self):
        self.assertTrue(fvt.acronym_corroborated({"pack_dir": ""}, "Anything (X)"))


class TestCrossrefAliasGuard(unittest.TestCase):
    """An alternate title that is another venue's *name* is that venue's, not an alias."""

    PAYLOAD = {"message": {"items": [
        {"title": "American Economic Journal: Economic Policy",
         "ISSN": ["1945-7731"], "alt-titles": ["Economic Policy", "AEJ Policy"],
         "counts": {"total-dois": 900}},
    ]}}

    def resolve(self, name: str, taken: set[str]):
        with unittest.mock.patch.object(fvt, "fetch", lambda url: self.PAYLOAD):
            return fvt.crossref_journal(name, taken)

    def test_the_alias_is_refused_when_it_is_another_venues_name(self):
        # `Economic Policy` (Oxford) is its own row in the index.
        self.assertIsNone(self.resolve("Economic Policy",
                                       {fvt.norm_name("Economic Policy")}))

    def test_an_alias_nobody_else_claims_still_resolves(self):
        found = self.resolve("AEJ Policy", {fvt.norm_name("Economic Policy")})
        self.assertIsNotNone(found)
        self.assertEqual(found["rule"], "crossref-alt-title")

    def test_an_exact_title_match_needs_no_alias_rule(self):
        found = self.resolve("American Economic Journal Economic Policy", set())
        self.assertEqual(found["rule"], "crossref-title")
        self.assertEqual(found["key"], "1945-7731")

    def test_a_candidate_without_an_issn_is_not_usable(self):
        payload = {"message": {"items": [{"title": "Economic Policy", "ISSN": [],
                                          "counts": {"total-dois": 10}}]}}
        with unittest.mock.patch.object(fvt, "fetch", lambda url: payload):
            self.assertIsNone(fvt.crossref_journal("Economic Policy", set()))


class TestIssnVeto(unittest.TestCase):
    """A name match is evidence about words. An ISSN is evidence about a serial."""

    def veto(self, venue, found, issns=frozenset()):
        with unittest.mock.patch.object(fvt, "stated_issns", lambda v: set(issns)):
            return fvt.issn_veto(venue, found)

    CROSSREF = {"provider": "crossref", "key": "0270-2592",
                "issns": ["0270-2592", "1475-6803"], "name": "x", "rule": "crossref-title"}

    def test_a_stated_issn_the_candidate_does_not_carry_is_refused(self):
        # The real case: 《金融研究》 is 1002-7246; Crossref's exact-title match for
        # "Journal of Financial Research" is the Southern Finance Association's journal.
        refusal = self.veto({"region": "china"}, self.CROSSREF, {"1002-7246"})
        self.assertIn("ISSN mismatch", refusal)

    def test_a_corroborating_issn_settles_it_whatever_the_region(self):
        self.assertIsNone(self.veto({"region": "china"}, self.CROSSREF, {"0270-2592"}))

    def test_a_chinese_venue_with_nothing_to_corroborate_a_name_is_refused(self):
        # 《管理世界》 states no ISSN, and "Journal of Management World" matches an
        # unrelated registered title exactly. A translated name is not an identifier.
        refusal = self.veto({"region": "china"},
                            {**self.CROSSREF, "issns": ["2994-3191"]})
        self.assertIn("translated name", refusal)

    def test_an_international_venue_with_no_stated_issn_still_resolves(self):
        # The display name of an English-language journal *is* its registered title,
        # so an exact match on it is the evidence. Most of the corpus is in this case.
        self.assertIsNone(self.veto({"region": "international"}, self.CROSSREF))

    def test_a_dblp_conference_is_not_subject_to_the_translation_rule(self):
        # DBLP keys a conference *series*, not a serial: there is no ISSN to state and
        # no translated-title registry to collide with.
        self.assertIsNone(self.veto(
            {"region": "china"},
            {"provider": "dblp", "key": "conf/x", "issns": [], "name": "x",
             "rule": "dblp-venue"}))

    def test_a_candidate_with_no_issn_cannot_contradict_a_stated_one(self):
        # Absence of an ISSN on the candidate says nothing; only a *different* one does.
        found = {**self.CROSSREF, "issns": []}
        self.assertIsNone(self.veto({"region": "international"}, found, {"1002-7246"}))


class TestStatedIssns(unittest.TestCase):
    def test_the_three_shapes_the_packs_write(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "m.md"
            path.write_text("ISSN 1002-9621\n| ISSN | 1002-7246 |\nISSN: 0012-968X\n",
                            encoding="utf-8")
            self.assertEqual(fvt._issns_in(path),
                             {"1002-9621", "1002-7246", "0012-968X"})

    def test_a_bare_number_that_is_not_labelled_is_not_an_issn(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "m.md"
            path.write_text("volume 1002-9621 of something", encoding="utf-8")
            self.assertEqual(fvt._issns_in(path), set())

    def test_a_missing_file_is_not_an_error(self):
        self.assertEqual(fvt._issns_in(Path("/nonexistent/x.md")), set())


class TestDeriveTopics(unittest.TestCase):
    def test_a_term_the_whole_corpus_uses_is_dropped(self):
        corpus = {v: [f"Evidence on {v} outcomes", f"Evidence about {v} effects",
                      f"More evidence for {v}"] for v in ("a", "b", "c", "d")}
        topics = fvt.derive_topics(corpus, depth=50)
        self.assertNotIn("evidence", topics["a"])

    def test_a_term_one_venue_repeats_survives(self):
        corpus = {"a": ["Electrolyte transport in cells",
                        "Electrolyte gradients revisited"],
                  "b": ["Wage inequality and schooling",
                        "Schooling returns in panel data"],
                  "c": ["Distributed consensus under churn", "Consensus lower bounds"]}
        self.assertIn("electrolyte", fvt.derive_topics(corpus, depth=50)["a"])

    def test_the_depth_caps_the_list(self):
        corpus = {"a": [f"Term{i} and term{i} again" for i in range(40)],
                  "b": ["something else entirely twice", "something else entirely"]}
        self.assertLessEqual(len(fvt.derive_topics(corpus, depth=5)["a"]), 5)

    def test_a_venue_with_no_usable_titles_gets_an_empty_list(self):
        self.assertEqual(fvt.derive_topics({"a": []}, depth=10)["a"], [])


class TestRenderPostings(unittest.TestCase):
    VENUES = [{"venue_id": "a"}, {"venue_id": "b"}, {"venue_id": "c"}]

    def header(self, text: str) -> dict[str, str]:
        out = {}
        for line in text.splitlines():
            if not line.startswith("#"):
                break
            key, _, value = line[1:].partition("\t")
            out[key] = value
        return out

    def test_venues_are_referenced_by_row_not_by_id(self):
        rendered = fvt.render_postings({"c": ["alpha"]}, self.VENUES, 0, 1)
        self.assertIn("alpha\t2:0\n", rendered)

    def test_the_header_carries_the_ordering_digest(self):
        rendered = fvt.render_postings({"a": ["alpha"]}, self.VENUES, 0, 1)
        from venue_lib import index_digest
        self.assertEqual(self.header(rendered)["digest"], index_digest(["a", "b", "c"]))

    def test_the_leak_guard_publishes_what_it_dropped(self):
        # A control nobody can see the size of is a claim, not a control.
        header = self.header(fvt.render_postings({"a": ["alpha"]}, self.VENUES, 17, 400))
        self.assertEqual(header["gold-titles-dropped"], "17")
        self.assertEqual(header["titles"], "400")

    def test_a_venue_absent_from_the_index_is_not_written(self):
        rendered = fvt.render_postings({"zz": ["alpha"]}, self.VENUES, 0, 1)
        self.assertNotIn("alpha", rendered)

    def test_uncovered_venues_are_counted_honestly(self):
        header = self.header(fvt.render_postings({"a": ["x"]}, self.VENUES, 0, 1))
        self.assertEqual(header["covered"], "1")
        self.assertEqual(header["venues"], "3")

    def test_the_file_records_which_source_each_vocabulary_came_from(self):
        # So a later pass can tell a vocabulary that is merely un-refreshed from one
        # that belongs to a venue whose resolution has since changed.
        rendered = fvt.render_postings({"a": ["x"], "b": ["y"]}, self.VENUES, 0, 2,
                                       {"a": "0022-1082", "b": "conf/sigcomm",
                                        "c": "unused"})
        self.assertIn("#built\ta\t0022-1082\n", rendered)
        self.assertIn("#built\tb\tconf/sigcomm\n", rendered)
        # `c` has no vocabulary in this build, so it has no provenance line either.
        self.assertNotIn("#built\tc", rendered)

    def test_the_provenance_reads_back(self):
        import tempfile
        rendered = fvt.render_postings({"a": ["x"]}, self.VENUES, 0, 1,
                                       {"a": "0022-1082"})
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "topics.tsv"
            path.write_text(rendered, encoding="utf-8")
            self.assertEqual(fvt.read_built_from(path), {"a": "0022-1082"})
            self.assertEqual(fvt.read_postings(self.VENUES, path), {"a": ["x"]})

    def test_a_file_with_no_provenance_reads_back_empty_not_wrong(self):
        import tempfile
        rendered = fvt.render_postings({"a": ["x"]}, self.VENUES, 0, 1)
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "topics.tsv"
            path.write_text(rendered, encoding="utf-8")
            self.assertEqual(fvt.read_built_from(path), {})
            self.assertEqual(fvt.read_postings(self.VENUES, path), {"a": ["x"]})

    def test_a_ranked_vocabulary_survives_the_round_trip_in_order(self):
        import tempfile
        terms = ["alpha", "beta", "gamma", "delta"]
        rendered = fvt.render_postings({"b": terms}, self.VENUES, 0, 1)
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "topics.tsv"
            path.write_text(rendered, encoding="utf-8")
            self.assertEqual(fvt.read_postings(self.VENUES, path)["b"], terms)


if __name__ == "__main__":
    unittest.main()
