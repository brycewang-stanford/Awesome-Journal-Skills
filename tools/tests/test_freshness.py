"""Unit tests for the freshness parser.

`freshness_audit` decides how stale each pack's source map is by reading the dates the
map itself states. That parse is a hard CI gate — an unparsed date counts as "unknown"
and fails the build — so it has to tell an *access date* apart from every other date a
publisher's page happens to mention: a volume year, a founding date, a deadline in the
future. Getting that wrong in the permissive direction is the dangerous one: a source
map with no verification date would silently inherit the year printed in a citation and
report itself as fresh.
"""

from __future__ import annotations

import datetime as dt
import unittest

from . import context  # noqa: F401  (import for the sys.path side effect)

from freshness_audit import last_verified, parse_date

TODAY = dt.date(2026, 8, 23)


class TestParseDate(unittest.TestCase):
    def test_reads_an_iso_date(self):
        self.assertEqual(parse_date("2026-01-31"), dt.date(2026, 1, 31))

    def test_an_impossible_date_is_not_a_date(self):
        self.assertIsNone(parse_date("2026-13-01"))
        self.assertIsNone(parse_date("not-a-date"))


class TestLastVerified(unittest.TestCase):
    def test_a_date_next_to_a_verification_word_is_stated(self):
        for phrasing in ("Accessed 2026-06-01.",
                         "Access date: 2026-06-01",
                         "Re-verified 2026-06-01",
                         "Live-checked 2026-06-01",
                         "last checked 2026-06-01"):
            with self.subTest(phrasing=phrasing):
                self.assertEqual(last_verified(phrasing, TODAY),
                                 (dt.date(2026, 6, 1), "stated"))

    def test_a_bare_date_elsewhere_in_the_text_is_only_inferred(self):
        # A volume year is not a claim that anyone re-read the page. Marking it
        # `inferred` is what lets the dashboard separate "checked" from "mentioned".
        self.assertEqual(last_verified("Published 2019-03-04, volume 2.", TODAY),
                         (dt.date(2019, 3, 4), "inferred"))

    def test_a_stated_date_wins_over_a_more_recent_bare_one(self):
        text = "Volume dated 2026-08-01. Accessed 2026-06-01."
        self.assertEqual(last_verified(text, TODAY), (dt.date(2026, 6, 1), "stated"))

    def test_the_most_recent_stated_date_is_the_answer(self):
        text = "Accessed 2026-05-01. Re-verified 2026-07-15."
        self.assertEqual(last_verified(text, TODAY)[0], dt.date(2026, 7, 15))

    def test_a_future_date_is_ignored(self):
        # Submission deadlines and "next issue" dates live in source maps. Reading one
        # as a verification date would make the stalest pack look like the freshest.
        self.assertEqual(last_verified("Accessed 2027-01-01.", TODAY), (None, "none"))

    def test_tomorrows_date_is_a_time_zone_not_a_typo(self):
        # "Today" is not one date. A source map re-read in UTC+8 carries a date the UTC
        # runner has not reached yet, and rejecting it made the generated dashboard
        # rebuild differently on the two machines — a byte-checked artefact that failed
        # for eight hours a day. This is what a live-check pass on 2026-08-27 did to CI
        # running on 08-26.
        tomorrow = (TODAY + dt.timedelta(days=1)).isoformat()
        self.assertEqual(last_verified(f"Accessed {tomorrow}.", TODAY),
                         (TODAY + dt.timedelta(days=1), "stated"))

    def test_the_allowance_is_a_day_and_not_a_week(self):
        later = (TODAY + dt.timedelta(days=2)).isoformat()
        self.assertEqual(last_verified(f"Accessed {later}.", TODAY), (None, "none"))

    def test_a_future_date_does_not_hide_a_real_one(self):
        text = "Deadline 2027-01-01. Accessed 2026-06-01."
        self.assertEqual(last_verified(text, TODAY), (dt.date(2026, 6, 1), "stated"))

    def test_no_date_at_all_is_reported_as_none(self):
        self.assertEqual(last_verified("Editor-in-chief: someone.", TODAY),
                         (None, "none"))
        self.assertEqual(last_verified("", TODAY), (None, "none"))

    def test_a_verification_word_far_from_the_date_does_not_claim_it(self):
        # The context window is bounded so a "verified" sixty characters upstream of an
        # unrelated year cannot adopt it.
        text = "verified " + "x" * 200 + " 2026-06-01"
        self.assertEqual(last_verified(text, TODAY)[1], "inferred")


if __name__ == "__main__":
    unittest.main()
