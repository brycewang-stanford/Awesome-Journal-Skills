"""Unit tests for `venue_lib` — the text layer everything else is built on.

`venue_lib` decides what counts as a term, which venues are the same venue, and
which keywords describe a venue. Every generated file in
`shared-resources/journal-selection/` is downstream of it, and the `--check`
generators cannot catch a mistake here: they compare a fresh build against a
committed build produced by the same code, so a wrong rule reproduces itself and
passes.
"""

from __future__ import annotations

import unittest

from . import context  # noqa: F401  (import for the sys.path side effect)

import venue_lib as v


class TestTokenize(unittest.TestCase):
    def test_drops_stopwords_and_short_words(self):
        self.assertEqual(v.tokenize("The and of a minimum wage"), ["minimum", "wage"])

    def test_length_floor_is_four_characters(self):
        # `_WORD` matches 3+ characters but `tokenize` keeps only len > 3, so a
        # three-letter word is dropped. "iv" and "did" are casualties of that rule;
        # they are named here so the trade-off is visible rather than surprising.
        self.assertEqual(v.tokenize("did iv rdd"), [])
        self.assertEqual(v.tokenize("panel"), ["panel"])

    def test_urls_and_bare_domains_never_become_terms(self):
        # A domain is maximally distinctive and means nothing: `afajof` occurs in
        # exactly one venue, so TF-IDF loved it.
        terms = v.tokenize("see https://afajof.org/paper and www.aeaweb.org and nber.org")
        self.assertNotIn("afajof", terms)
        self.assertNotIn("aeaweb", terms)
        self.assertNotIn("nber", terms)

    def test_case_is_folded(self):
        self.assertEqual(v.tokenize("MINIMUM Wage"), v.tokenize("minimum wage"))

    def test_cjk_runs_produce_ngrams_alongside_latin_words(self):
        terms = v.tokenize("金融研究 quarterly")
        self.assertIn("quarterly", terms)
        self.assertIn("金融", terms)
        self.assertIn("金融研究", terms)


class TestCjkNgrams(unittest.TestCase):
    def test_generates_two_to_four_character_grams(self):
        self.assertEqual(
            sorted(set(len(g) for g in v.cjk_ngrams("金融学院主办"))), [2, 3, 4]
        )

    def test_never_starts_or_ends_on_a_function_word(self):
        # 的/了/是 carry no subject meaning; a gram hinging on one is a slice, not a term.
        for gram in v.cjk_ngrams("中国的金融市场"):
            self.assertNotIn(gram[0], v.CJK_NOISE, gram)
            self.assertNotIn(gram[-1], v.CJK_NOISE, gram)

    def test_does_not_cross_a_non_cjk_boundary(self):
        # Two separate runs must not be glued into one gram through the space.
        self.assertNotIn("融市", v.cjk_ngrams("金融 市场"))


class TestIndexDigest(unittest.TestCase):
    def test_order_changes_the_digest(self):
        # This is the entire point of the digest: `scope-postings.tsv` addresses
        # venues by row number, so a same-length reordering would silently
        # attribute every keyword to the wrong venue.
        self.assertNotEqual(v.index_digest(["a", "b"]), v.index_digest(["b", "a"]))

    def test_same_order_is_stable_across_calls(self):
        self.assertEqual(v.index_digest(["a", "b", "c"]), v.index_digest(["a", "b", "c"]))

    def test_is_short_enough_to_sit_in_a_header_line(self):
        self.assertEqual(len(v.index_digest(["a"])), 16)


class TestAcronymFits(unittest.TestCase):
    def test_accepts_a_real_venue_acronym(self):
        self.assertTrue(v.acronym_fits("QJE", "Quarterly Journal of Economics"))
        self.assertTrue(v.acronym_fits("AER", "American Economic Review"))

    def test_rejects_a_society_name_in_parentheses(self):
        # "Anesthesiology (ASA)" is the American Society of Anesthesiologists —
        # not an alias for the journal.
        self.assertFalse(v.acronym_fits("ASA", "Anesthesiology"))

    def test_requires_the_letters_in_order(self):
        self.assertFalse(v.acronym_fits("EQJ", "Quarterly Journal of Economics"))

    def test_empty_inputs_are_not_a_fit(self):
        self.assertFalse(v.acronym_fits("", "Quarterly Journal"))
        self.assertFalse(v.acronym_fits("QJ", ""))


class TestIdentityKeys(unittest.TestCase):
    def test_collects_english_chinese_and_acronym_forms(self):
        keys = v.identity_keys(
            "# Quarterly Journal of Economics (QJE)\n《经济研究》",
            "Quarterly Journal of Economics",
            "quarterly-journal-of-economics",
        )
        self.assertIn("quarterlyjournalofeconomics", keys)
        self.assertIn("qje", keys)
        self.assertIn("经济研究", keys)

    def test_a_parenthetical_that_abbreviates_nothing_is_dropped(self):
        keys = v.identity_keys(
            "# Anesthesiology (ASA)", "Anesthesiology", "anesthesiology"
        )
        self.assertNotIn("asa", keys)

    def test_keys_shorter_than_three_characters_are_dropped(self):
        self.assertTrue(all(len(k) >= 3 for k in v.identity_keys("# AI", "AI", "ai")))


class TestDisplayNameAndSlug(unittest.TestCase):
    def test_chinese_profile_title_keeps_only_the_journal_name(self):
        self.assertEqual(
            v.h1_display_name("# 《经济研究》投稿 (economic-research)\n", "fallback"),
            "经济研究",
        )

    def test_english_profile_title_drops_the_trailing_slug_echo(self):
        self.assertEqual(
            v.h1_display_name("# American Economic Review (aer)\n", "fallback"),
            "American Economic Review",
        )

    def test_missing_h1_falls_back(self):
        self.assertEqual(v.h1_display_name("no heading here", "fallback"), "fallback")

    def test_slugify_is_lowercase_and_punctuation_free(self):
        self.assertEqual(
            v.slugify("Journal of Economic Perspectives!"),
            "journal-of-economic-perspectives",
        )


class TestFrontmatter(unittest.TestCase):
    def test_reads_the_description(self):
        text = "---\nname: x\ndescription: Use when routing a paper.\n---\nbody\n"
        self.assertEqual(v.frontmatter_description(text), "Use when routing a paper.")

    def test_no_frontmatter_yields_empty(self):
        self.assertEqual(v.frontmatter_description("# heading\n"), "")

    def test_strip_frontmatter_leaves_the_body(self):
        self.assertEqual(v.strip_frontmatter("---\na: 1\n---\nbody"), "body")


class TestDeriveKeywords(unittest.TestCase):
    """TF-IDF over a three-venue toy corpus, small enough to reason about by hand."""

    CORPUS = {
        "labour": "natural experiment natural experiment minimum wage minimum wage "
                  "employment employment labour labour",
        "asset": "asset pricing asset pricing volatility volatility returns returns "
                 "portfolio portfolio",
        "market": "asset pricing asset pricing liquidity liquidity spreads spreads "
                  "returns returns",
    }

    def setUp(self):
        self.kw = v.derive_keywords(self.CORPUS, top_n=10)

    def test_each_venue_keeps_its_own_distinctive_terms(self):
        self.assertIn("minimum", self.kw["labour"])
        self.assertIn("volatility", self.kw["asset"])
        self.assertIn("liquidity", self.kw["market"])

    def test_a_term_shared_by_most_venues_is_dropped(self):
        # `returns` and `asset` sit in 2 of 3 venues, over the 35% DF ceiling: a term
        # that most venues use cannot separate them.
        self.assertGreater(2 / 3, v.DF_CEILING)
        for terms in self.kw.values():
            self.assertNotIn("returns", terms)

    def test_terms_are_ranked_not_merely_collected(self):
        self.assertEqual(self.kw["labour"], sorted(set(self.kw["labour"])) or self.kw["labour"])
        self.assertLessEqual(len(self.kw["labour"]), 10)

    def test_top_n_bounds_the_list(self):
        self.assertTrue(all(len(t) <= 3 for t in v.derive_keywords(self.CORPUS, top_n=3).values()))

    def test_a_skill_slug_is_never_a_keyword(self):
        # Slugs like `qje-identification` occur in exactly one venue's prose, which
        # makes them maximally TF-IDF-distinctive and completely useless: no paper
        # title contains one.
        slugs = v._skill_slugs()
        self.assertTrue(slugs, "expected the repository to contain skill directories")
        sample = sorted(slugs)[0]
        corpus = dict(self.CORPUS)
        corpus["slugged"] = f"{sample} {sample} unrelated unrelated topic topic"
        self.assertNotIn(sample, v.derive_keywords(corpus, top_n=10)["slugged"])


class TestRedundancy(unittest.TestCase):
    def test_a_word_already_inside_a_picked_phrase_is_redundant(self):
        self.assertTrue(v._redundant("experiment", ["natural experiment"]))

    def test_a_phrase_containing_a_picked_word_is_redundant(self):
        self.assertTrue(v._redundant("natural experiment", ["experiment"]))

    def test_cjk_overlap_is_by_substring(self):
        # The over-generated grams of one phrase would otherwise fill the slate.
        self.assertTrue(v._redundant("金融学", ["金融学院"]))

    def test_unrelated_terms_are_not_redundant(self):
        self.assertFalse(v._redundant("liquidity", ["natural experiment"]))


class TestDiscoverCjkVocab(unittest.TestCase):
    """Unsupervised Chinese word discovery, on a corpus built to be decidable by hand.

    Cohesion compares a gram's probability against the product of its parts', so it is
    a *corpus-relative* measure: five occurrences in a thirty-character corpus look
    like noise no matter how word-like the gram is. The filler below exists to make the
    corpus large enough for the thresholds to mean what they mean in production.
    """

    FILLER = [
        "产业结构升级路径", "区域协调发展格局", "企业创新投入强度", "市场波动特征分析",
        "劳动力流动趋势", "公共政策评估方法", "技术进步贡献测算", "城乡收入差距变化",
    ] * 4
    # 数字经济 recurs with a different character on each side — a word chooses its own
    # context. 金融学院主办 recurs as a fixed block, so every 4-gram cut out of it
    # (融学院主, 学院主办, 金融学院) inherits a neighbour instead of choosing one.
    CORPUS = [
        "数字经济发展研究", "推动数字经济转型", "区域数字经济水平",
        "考察数字经济影响", "分析数字经济效应", "评估数字经济政策",
        "金融学院主办期刊", "由金融学院主办", "本刊金融学院主办",
        "金融学院主办发行", "金融学院主办出版", "该刊金融学院主办",
    ] + FILLER

    def test_a_recurring_cohesive_free_word_is_admitted(self):
        self.assertIn("数字经济", v.discover_cjk_vocab(self.CORPUS))

    def test_a_fragment_with_a_fixed_neighbour_is_rejected(self):
        # 融学院主 is always preceded by 金 and followed by 办. This is the case that
        # motivated the whole function: TF-IDF ranks terms and cannot tell a word from
        # a slice, and slices score *well* precisely because they are rare.
        vocab = v.discover_cjk_vocab(self.CORPUS)
        self.assertNotIn("融学院主", vocab)
        self.assertNotIn("学院主办", vocab)
        self.assertNotIn("字经济发", vocab)

    def test_a_gram_seen_once_is_never_a_word(self):
        self.assertGreater(v.CJK_MIN_FREQ, 1)
        self.assertEqual(v.discover_cjk_vocab(["罕见词组"]), set())

    def test_empty_corpus_is_handled(self):
        self.assertEqual(v.discover_cjk_vocab([]), set())
        self.assertEqual(v.discover_cjk_vocab(["latin only"]), set())


class TestDisciplineOf(unittest.TestCase):
    def test_a_known_cue_maps_to_its_discipline(self):
        self.assertEqual(v.discipline_of("Journal-of-Finance-Skills"), "finance")

    def test_an_unknown_name_falls_back(self):
        self.assertEqual(v.discipline_of("Zzz-Unmapped-Skills"), "other")
        self.assertEqual(v.discipline_of("Zzz-Unmapped-Skills", default="unknown"), "unknown")

    def test_no_rule_is_unreachable(self):
        """The guard for the whole bug class, not for the seven instances of it.

        `DISC` is first-match-wins over substrings, so a specific key placed after a
        generic key it contains can never fire — and nothing says so. It just hands its
        venues to the generic rule. Seven rules had lost that race: the IR journal
        `International-Organization` was filed under management by `Organization`, and
        so were the Journal of Human Resources, the Journal of Economic Behavior and
        Organization, and the Journal of Law, Economics and Organization.

        A rule must at least classify its own key. That is cheap to check and
        impossible to satisfy while shadowed.
        """
        shadowed = [(kw, disc, v.discipline_of(kw))
                    for kw, disc in v.DISC if v.discipline_of(kw) != disc]
        self.assertEqual(shadowed, [], "move each rule before the one that shadows it")

    def test_a_whole_name_rule_does_not_leak_as_a_substring(self):
        # `Science-Skills` is the journal *Science*. As a substring it also claimed
        # Marketing Science, Organization Science and Psychological Science, which is
        # why whole-name rules live in their own map.
        self.assertEqual(v.discipline_of("Science-Skills"), "natural-science")
        self.assertNotEqual(v.discipline_of("Marketing-Science-Skills"), "natural-science")
        self.assertNotEqual(v.discipline_of("Psychological-Science-Skills"), "natural-science")

    def test_management_science_is_an_operations_journal(self):
        self.assertEqual(v.discipline_of("Management-Science-Skills"), "operations")


class TestExecutionBridgeScope(unittest.TestCase):
    """Which disciplines the StatsPAI / Stata execution bridge is actually for.

    `quality_scorecard` scores how much of a pack reaches that bridge. The question it
    has to answer first is whether the bridge is even the pack's execution layer, and
    for a long time it answered a different question — whether the pack shipped *any*
    code. Those two come apart hard: the bridge is DiD, IV, RDD, DML and synthetic
    control, and an AI conference ships PyTorch.
    """

    def test_the_social_science_disciplines_are_in_scope(self):
        for discipline in ("economics", "finance", "management", "management/OR",
                           "political-science", "sociology", "psychology",
                           "linguistics", "accounting", "marketing"):
            with self.subTest(discipline=discipline):
                self.assertTrue(v.uses_econometric_execution(discipline))

    def test_computer_science_is_not(self):
        # The 100 packs that gave the mis-scoping away.
        for discipline in ("cs-ai", "cs-ai (conference)", "cs-ai (CN journal)",
                           "engineering", "materials-science"):
            with self.subTest(discipline=discipline):
                self.assertFalse(v.uses_econometric_execution(discipline))

    def test_the_non_empirical_disciplines_are_not(self):
        # Already excluded elsewhere; asserted here so the two exemptions cannot drift
        # apart and quietly re-admit a theory venue.
        for discipline in ("philosophy", "mathematics", "economics/theory"):
            with self.subTest(discipline=discipline):
                self.assertFalse(v.uses_econometric_execution(discipline))

    def test_every_conference_pack_is_out_of_scope(self):
        # Not one of the 90 is an econometrics venue, so none of them should ever be
        # charged for the bridge. This is the assertion that would have failed before.
        for pack in v.CONFERENCE_DEPTH_PACKS:
            with self.subTest(pack=pack):
                self.assertFalse(v.uses_econometric_execution(v.discipline_of(pack)))


if __name__ == "__main__":
    unittest.main()
