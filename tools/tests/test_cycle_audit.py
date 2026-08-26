"""Unit tests for the conference cycle parser.

`cycle_audit` answers a question `freshness_audit` structurally cannot: not "when was
this file re-read?" but "which edition was it re-read *about*?". Both halves of that
parse are easy to get wrong in a way no one notices:

* reading a year that is not an edition — a copyright line, an ISSN, a history note —
  makes a stale pack look current, which is the failure the tool exists to prevent;
* reading a retirement claim that belongs to some *other* venue retires a conference
  that is still running, which silently excuses it from the gate forever.

The second one is not hypothetical. Both false-retirement shapes tested below were
found in this repository's own source maps by the first draft of the tool.

The fixtures are written here rather than read from the packs on purpose: a test that
reads generated or committed content cannot tell "the parser is right" from "the parser
and the file are wrong in the same way".
"""

from __future__ import annotations

import datetime as dt
import unittest

from . import context  # noqa: F401  (import for the sys.path side effect)

from cycle_audit import edition_years, is_retired, latest_stated_month, status_of

TODAY = dt.date(2026, 8, 26)


def record(edition, month=None, retired=False):
    return {"pack": "X-Skills", "alias": "X", "edition": edition,
            "month": month, "retired": retired, "note": ""}


class TestEditionYears(unittest.TestCase):
    def test_reads_a_four_digit_edition(self):
        self.assertEqual(edition_years("NeurIPS 2026 is the 40th.", ("NeurIPS",)),
                         [2026])

    def test_reads_a_two_digit_edition(self):
        self.assertEqual(edition_years("The AAAI-27 call is open.", ("AAAI",)), [2027])

    def test_reads_an_apostrophe_edition(self):
        self.assertEqual(edition_years("Sec '26 proceedings.", ("Sec",)), [2026])

    def test_reads_an_edition_carrying_a_co_hosted_partner(self):
        # IJCAI writes itself as "IJCAI-ECAI 2026" in the year it co-hosts ECAI. Without
        # the partner slot the pack looks unlabelled and drops out of the audit.
        self.assertEqual(edition_years("The IJCAI-ECAI 2026 call.", ("IJCAI",)), [2026])

    def test_every_edition_is_returned_ascending(self):
        text = "ICML 2025 introduced the policy; ICML 2026 kept it."
        self.assertEqual(edition_years(text, ("ICML",)), [2025, 2026])

    def test_a_year_not_attached_to_the_venue_is_not_an_edition(self):
        # The failure that matters: any loose year search finds 2027 here and calls a
        # pack anchored to a 2019 edition current.
        text = "KDD 2019 rules. Copyright 2027 ACM. Retrieved in 2027."
        self.assertEqual(edition_years(text, ("KDD",)), [2019])

    def test_a_year_inside_a_url_is_not_an_edition(self):
        # A source map that cites `https://aistats.org/aistats2027/` to record that the
        # page 404s would otherwise be read as announcing a 2027 edition — and the
        # newest-year rule would then call the pack current on the strength of a page
        # that does not exist. Found by writing exactly such a note.
        text = ("AISTATS 2026 is the newest edition page. "
                "https://aistats.org/aistats2027/ returns 404.")
        self.assertEqual(edition_years(text, ("AISTATS",)), [2026])

    def test_a_year_inside_a_code_span_is_not_an_edition(self):
        # Writing the same dead path without its scheme does not make it prose — the
        # first fix for the URL case was defeated by exactly that, so a quoted literal
        # is dropped whether or not it still looks like a URL.
        text = "AISTATS 2026 is the newest edition page. `aistats.org/aistats2027/` 404s."
        self.assertEqual(edition_years(text, ("AISTATS",)), [2026])

    def test_a_longer_acronym_ending_in_this_one_is_a_different_venue(self):
        # The real finding: `ACL-Skills` was reported as anchored to ACL 2027 by one
        # line about the **EACL 2027** commitment deadline. The pack holds no 2027 fact,
        # and the check meant to notice that it describes a closed cycle was reading a
        # sibling conference's calendar as proof that it does not.
        self.assertEqual(
            edition_years("May cycle commitment feeds EACL 2027.", ("ACL",)), [])

    def test_the_venues_own_edition_still_reads_beside_a_sibling(self):
        self.assertEqual(
            edition_years("ACL 2026 runs in July; the May cycle feeds EACL 2027.",
                          ("ACL",)),
            [2026])

    def test_a_prefixed_acronym_is_not_a_match_either(self):
        # PVLDB volumes are numbered by year and sit in the same sentence as VLDB's.
        self.assertEqual(edition_years("PVLDB 2018 volume 11.", ("VLDB",)), [])

    def test_a_hyphen_before_the_name_is_a_co_host_not_a_different_venue(self):
        # The boundary rule must not undo the co-hosted case: "IJCAI-ECAI 2026" is an
        # ECAI edition, written the way the organisers write it.
        self.assertEqual(edition_years("IJCAI-ECAI 2026 in Bologna.", ("ECAI",)), [2026])

    def test_a_year_outside_the_plausible_window_is_ignored(self):
        self.assertEqual(edition_years("STOC 1998 and STOC 2099.", ("STOC",)), [])

    def test_matching_is_case_insensitive(self):
        # The pack directory shouts (`INTERSPEECH-Skills`); the venue does not.
        self.assertEqual(edition_years("Interspeech 2027 call.", ("INTERSPEECH",)),
                         [2027])

    def test_any_alias_can_carry_the_edition(self):
        self.assertEqual(edition_years("CCS 2027 deadlines.", ("CCS", "ACM CCS")),
                         [2027])


class TestLatestStatedMonth(unittest.TestCase):
    def test_finds_a_month_named_with_the_edition_year(self):
        self.assertEqual(latest_stated_month("Held December 6-12, 2026.", 2026), 12)

    def test_takes_the_latest_of_several(self):
        text = "Abstracts May 2026; papers September 2026."
        self.assertEqual(latest_stated_month(text, 2026), 9)

    def test_ignores_months_belonging_to_another_year(self):
        self.assertIsNone(latest_stated_month("Held December 2025.", 2026))

    def test_no_month_is_not_month_zero(self):
        # None and 0 diverge in `status_of`: None means the file is silent (report it),
        # 0 would mean every month has passed (call it stale). Silence is not evidence.
        self.assertIsNone(latest_stated_month("NeurIPS 2026 is the 40th.", 2026))


class TestIsRetired(unittest.TestCase):
    def test_a_venue_that_merged_away_is_retired(self):
        self.assertTrue(is_retired("IPSN merged into SenSys in 2025.", ("IPSN",)))

    def test_a_venue_that_stopped_running_is_retired(self):
        self.assertTrue(
            is_retired("IPSN and IoTDI stopped running as standalone conferences.",
                       ("IPSN",))
        )

    def test_merged_review_outcomes_do_not_retire_the_conference(self):
        # From `OOPSLA-Skills`: it is the *review outcomes* that were merged. A
        # same-sentence test reads this as OOPSLA shutting down.
        text = ('OOPSLA\'25\'s separate "Conditional Accept" and "Minor Revision" '
                'outcomes were merged into a single "Minor Revision" for 2026.')
        self.assertFalse(is_retired(text, ("OOPSLA",)))

    def test_a_longer_acronym_ending_in_this_one_cannot_retire_it(self):
        # Same boundary rule, second reader: "EACL was discontinued" must not retire ACL.
        self.assertFalse(is_retired("EACL was discontinued in 2029.", ("ACL",)))

    def test_a_sibling_venue_shutting_down_does_not_retire_this_one(self):
        # From `USENIX-Security-Skills`: ATC is the venue that was discontinued, and
        # USENIX Security is named later in the same sentence as its beneficiary.
        text = ("Confirmation that USENIX ATC was discontinued after 2025, making "
                "USENIX Security the association's flagship summer event.")
        self.assertFalse(is_retired(text, ("USENIX Security", "USENIX Sec")))


class TestStatusOf(unittest.TestCase):
    def test_a_future_edition_is_current(self):
        self.assertEqual(status_of(record(2027), TODAY), "current")

    def test_a_past_edition_is_stale(self):
        self.assertEqual(status_of(record(2025), TODAY), "stale")

    def test_this_years_edition_with_a_month_still_ahead_is_current(self):
        self.assertEqual(status_of(record(2026, month=12), TODAY), "current")

    def test_this_years_edition_with_every_stated_month_passed_is_due(self):
        self.assertEqual(status_of(record(2026, month=1), TODAY), "due")

    def test_this_years_edition_with_no_stated_month_is_due(self):
        # NeurIPS 2026 (December) and AAAI 2026 (January) are indistinguishable from a
        # file that names neither month. `due` says so instead of guessing.
        self.assertEqual(status_of(record(2026), TODAY), "due")

    def test_the_current_month_still_counts_as_ahead(self):
        self.assertEqual(status_of(record(2026, month=8), TODAY), "current")

    def test_no_edition_label_is_unknown_not_stale(self):
        self.assertEqual(status_of(record(None), TODAY), "unknown")

    def test_a_retired_venue_is_not_stale(self):
        self.assertEqual(status_of(record(2024, retired=True), TODAY), "retired")

    def test_a_retirement_claim_cannot_retire_a_venue_with_an_edition_ahead(self):
        # The second guard on the misreading above: whatever the prose says, a venue
        # with a 2027 edition has not stopped running.
        self.assertEqual(status_of(record(2027, retired=True), TODAY), "current")


if __name__ == "__main__":
    unittest.main()
