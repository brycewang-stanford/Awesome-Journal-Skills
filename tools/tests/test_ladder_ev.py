"""Unit tests for `ladder_ev` — the only tool in the repository that does arithmetic
an author will act on.

Step 6 of the journal-match method prices a *sequence* of submissions: how long the
ladder takes to resolve, how likely it is to place the paper at all, and what happens
if the acceptance probabilities are optimistic. Those numbers go into a decision about
where someone sends a year of their work, and unlike the retrieval score nothing else
in the repository would notice if they were wrong. The worked examples below are small
enough to check by hand, and the hand calculation is written out beside each one.
"""

from __future__ import annotations

import argparse
import math
import unittest

from . import context  # noqa: F401  (import for the sys.path side effect)

from ladder_ev import Rung, band, evaluate, parse_rung


class TestParseRung(unittest.TestCase):
    def test_parses_name_probability_and_months(self):
        rung = parse_rung("QJE:0.05:6")
        self.assertEqual((rung.name, rung.p_accept, rung.months), ("QJE", 0.05, 6.0))

    def test_a_name_may_contain_colons(self):
        # Only the last two colons are separators, so a venue named with one survives.
        self.assertEqual(parse_rung("AEJ: Applied:0.1:4").name, "AEJ: Applied")

    def test_rejects_a_malformed_spec(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            parse_rung("QJE:0.05")

    def test_rejects_a_non_numeric_probability(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            parse_rung("QJE:likely:6")

    def test_rejects_a_probability_outside_zero_to_one(self):
        # A percentage typed as "5" instead of "0.05" would otherwise place the paper
        # with certainty on the first rung and report a confident, meaningless answer.
        with self.assertRaises(argparse.ArgumentTypeError):
            parse_rung("QJE:5:6")
        with self.assertRaises(argparse.ArgumentTypeError):
            parse_rung("QJE:-0.1:6")

    def test_rejects_negative_months(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            parse_rung("QJE:0.05:-1")


class TestEvaluate(unittest.TestCase):
    """Two coin-flip rungs, two months of review each, one month of revision.

    P(placed)      = 0.5 + 0.5·0.5                      = 0.75
    P(exhausted)   = 0.5 · 0.5                          = 0.25
    E[months]      = 1·(2 + 0.5·1) + 0.5·(2 + 0.5·1)    = 3.75
    E[months | placed] = (0.5·3 + 0.25·5) / 0.75        = 3.667
    """

    def setUp(self):
        self.result = evaluate([Rung("A", 0.5, 2.0), Rung("B", 0.5, 2.0)], 1.0)

    def test_probability_of_placing(self):
        self.assertAlmostEqual(self.result["p_placed"], 0.75)

    def test_probability_of_exhausting_the_ladder(self):
        self.assertAlmostEqual(self.result["p_exhausted"], 0.25)

    def test_placed_and_exhausted_partition_the_outcomes(self):
        self.assertAlmostEqual(self.result["p_placed"] + self.result["p_exhausted"], 1.0)

    def test_expected_months_until_the_ladder_resolves(self):
        self.assertAlmostEqual(self.result["expected_months"], 3.75)

    def test_expected_months_conditional_on_placing(self):
        self.assertAlmostEqual(self.result["months_if_placed"], 11 / 3)

    def test_reach_decays_by_the_previous_rungs_rejection(self):
        first, second = self.result["per_rung"]
        self.assertAlmostEqual(first["p_reach"], 1.0)
        self.assertAlmostEqual(second["p_reach"], 0.5)

    def test_elapsed_time_accumulates_down_the_ladder(self):
        first, second = self.result["per_rung"]
        self.assertAlmostEqual(first["months_elapsed"], 3.0)
        self.assertAlmostEqual(second["months_elapsed"], 5.0)

    def test_a_certain_first_rung_makes_the_rest_unreachable(self):
        result = evaluate([Rung("sure", 1.0, 1.0), Rung("never", 0.9, 12.0)], 0.0)
        self.assertAlmostEqual(result["p_placed"], 1.0)
        self.assertAlmostEqual(result["p_exhausted"], 0.0)
        self.assertAlmostEqual(result["expected_months"], 1.0)
        self.assertAlmostEqual(result["per_rung"][1]["p_reach"], 0.0)

    def test_a_hopeless_ladder_still_costs_its_review_time(self):
        # Every rung is paid for whether it accepts or rejects. A ladder of zeroes is
        # the clearest statement of that: no chance of placing, four months spent.
        result = evaluate([Rung("A", 0.0, 2.0), Rung("B", 0.0, 2.0)], 1.0)
        self.assertAlmostEqual(result["p_placed"], 0.0)
        self.assertAlmostEqual(result["expected_months"], 4.0)
        self.assertTrue(math.isnan(result["months_if_placed"]))

    def test_an_empty_ladder_is_not_a_crash(self):
        result = evaluate([], 1.0)
        self.assertEqual(result["p_placed"], 0.0)
        self.assertEqual(result["p_exhausted"], 1.0)
        self.assertTrue(math.isnan(result["months_if_placed"]))

    def test_adding_a_rung_can_only_raise_the_chance_of_placing(self):
        short = evaluate([Rung("A", 0.2, 3.0)], 1.0)
        long = evaluate([Rung("A", 0.2, 3.0), Rung("B", 0.2, 3.0)], 1.0)
        self.assertGreater(long["p_placed"], short["p_placed"])
        self.assertGreater(long["expected_months"], short["expected_months"])


class TestSensitivityScale(unittest.TestCase):
    """`p_accept` is a judgement, not a measurement, so the tool reports a band."""

    def test_scaling_down_lowers_the_chance_of_placing(self):
        base = evaluate([Rung("A", 0.2, 3.0), Rung("B", 0.3, 3.0)], 1.0)
        pessimistic = evaluate([Rung("A", 0.2, 3.0), Rung("B", 0.3, 3.0)], 1.0, scale=0.5)
        self.assertLess(pessimistic["p_placed"], base["p_placed"])

    def test_scaling_up_cannot_push_a_probability_past_one(self):
        result = evaluate([Rung("A", 0.8, 3.0)], 1.0, scale=10.0)
        self.assertAlmostEqual(result["p_placed"], 1.0)
        self.assertAlmostEqual(result["p_exhausted"], 0.0)

    def test_a_scale_of_one_is_the_base_case(self):
        rungs = [Rung("A", 0.2, 3.0)]
        self.assertEqual(evaluate(rungs, 1.0), evaluate(rungs, 1.0, scale=1.0))


class TestBand(unittest.TestCase):
    def test_orders_the_endpoints_regardless_of_which_arrives_first(self):
        self.assertEqual(band(3.2, 1.1), "1.1-3.2")
        self.assertEqual(band(1.1, 3.2), "1.1-3.2")


if __name__ == "__main__":
    unittest.main()
