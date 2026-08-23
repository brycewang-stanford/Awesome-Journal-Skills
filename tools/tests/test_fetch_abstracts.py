"""Unit tests for `fetch_abstracts` — specifically, for the distinction it exists to keep.

A bibliographic API can say three things, and only two of them are about the paper:

* **found**    — here is the abstract;
* **absent**   — I looked, and there is none. A real miss, worth caching.
* **declined** — I did not look (401, 402, 403, 429, 5xx, timeout). Says nothing.

Folding *declined* into *absent* is the failure mode that matters, because it is
invisible: the run completes, the file looks populated, and the eval reports a
configuration measured on a small biased sample as though it were the corpus. It has
happened once here — OpenAlex began billing per request, answered 403, and 50 papers
were cached as "no abstract" in a single run before anyone looked.

No network: every test drives the HTTP layer through a stub.
"""

from __future__ import annotations

import contextlib
import io
import json
import unittest
import urllib.error
import warnings
from unittest import mock

from . import context  # noqa: F401  (import for the sys.path side effect)

import fetch_abstracts as fa
from fetch_abstracts import ABSENT, DECLINED, FOUND, Answer, Source


def http_error(code: int, body: dict | bytes = b"", headers: dict | None = None):
    payload = json.dumps(body).encode() if isinstance(body, dict) else body
    return urllib.error.HTTPError(
        url="https://example.test", code=code, msg="err",
        hdrs=headers or {}, fp=io.BytesIO(payload))


def ok(body: dict):
    response = mock.MagicMock()
    response.__enter__.return_value = io.BytesIO(json.dumps(body).encode())
    return response


class TestGetJson(unittest.TestCase):
    """The classifier every source depends on."""

    def call(self, side_effect):
        # The HTTPError doubles wrap a BytesIO, not a socket, so the interpreter's
        # "you left a response open" warning is about the stub rather than the code.
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", ResourceWarning)
            with mock.patch("urllib.request.urlopen", side_effect=side_effect):
                with mock.patch("time.sleep"):
                    return fa.get_json("https://example.test", {})

    def test_a_200_returns_the_payload(self):
        payload, failure = self.call([ok({"hello": "world"})])
        self.assertIsNone(failure)
        self.assertEqual(payload, {"hello": "world"})

    def test_404_is_absent(self):
        _, failure = self.call([http_error(404)])
        self.assertEqual(failure.kind, ABSENT)

    def test_403_is_declined_not_absent(self):
        # The exact regression: a paywalled or blocked API is not an empty shelf.
        _, failure = self.call([http_error(403, {"message": "forbidden"})])
        self.assertEqual(failure.kind, DECLINED)
        self.assertIn("403", failure.detail)

    def test_402_payment_required_is_declined(self):
        _, failure = self.call([http_error(402, {"message": "add funds"})])
        self.assertEqual(failure.kind, DECLINED)

    def test_a_budget_429_is_declined_and_carries_its_wait(self):
        body = {"error": "Rate limit exceeded",
                "message": "Insufficient budget. Resets at midnight UTC",
                "retryAfter": 39189}
        _, failure = self.call([http_error(429, body), http_error(429, body)])
        self.assertEqual(failure.kind, DECLINED)
        self.assertEqual(failure.retry_after, 39189)
        self.assertIn("Insufficient budget", failure.detail)

    def test_a_short_429_is_retried_and_can_succeed(self):
        payload, failure = self.call([
            http_error(429, {"retryAfter": 1}),
            ok({"recovered": True}),
        ])
        self.assertIsNone(failure)
        self.assertEqual(payload, {"recovered": True})

    def test_a_retry_after_beyond_the_ceiling_is_not_slept_through(self):
        # "Come back in eleven hours" is a stop, not a pause.
        self.assertLess(fa.MAX_WAIT, 3600)
        _, failure = self.call([http_error(429, {"retryAfter": 39189})])
        self.assertEqual(failure.kind, DECLINED)

    def test_a_retry_after_header_is_read_when_the_body_has_none(self):
        _, failure = self.call([http_error(503, b"", {"Retry-After": "7200"})])
        self.assertEqual(failure.retry_after, 7200)

    def test_a_network_failure_is_declined(self):
        _, failure = self.call([urllib.error.URLError("dns"), urllib.error.URLError("dns")])
        self.assertEqual(failure.kind, DECLINED)

    def test_a_5xx_is_declined_after_retries(self):
        _, failure = self.call([http_error(500), http_error(500)])
        self.assertEqual(failure.kind, DECLINED)


class TestCleanJats(unittest.TestCase):
    def test_strips_markup_and_the_redundant_label(self):
        raw = "<jats:title>Abstract</jats:title><jats:p>We study minimum wages.</jats:p>"
        self.assertEqual(fa.clean_jats(raw), "We study minimum wages.")

    def test_unescapes_entities(self):
        self.assertEqual(fa.clean_jats("<jats:p>firms &amp; workers</jats:p>"),
                         "firms & workers")

    def test_collapses_whitespace(self):
        self.assertEqual(fa.clean_jats("<p>a</p>\n\n  <p>b</p>"), "a b")

    def test_an_empty_abstract_stays_empty(self):
        self.assertEqual(fa.clean_jats(""), "")


class TestCrossref(unittest.TestCase):
    def resolve(self, payload_or_failure):
        target = "fetch_abstracts.get_json"
        if isinstance(payload_or_failure, Answer):
            value = (None, payload_or_failure)
        else:
            value = (payload_or_failure, None)
        with mock.patch(target, return_value=value):
            return fa.crossref("A Garbage Can Model of Organizational Choice")

    def test_a_matching_title_with_an_abstract_is_found(self):
        answer = self.resolve({"message": {"items": [{
            "title": ["A Garbage Can Model of Organizational Choice"],
            "abstract": "<jats:p>Organized anarchies make choices under ambiguous "
                        "preferences and unclear technology across universities.</jats:p>",
            "DOI": "10.2307/2392088",
        }]}})
        self.assertEqual(answer.kind, FOUND)
        self.assertEqual(answer.work_id, "10.2307/2392088")
        self.assertIn("anarchies", answer.terms)

    def test_terms_are_deduplicated_and_sorted(self):
        answer = self.resolve({"message": {"items": [{
            "title": ["A Garbage Can Model of Organizational Choice"],
            "abstract": "choice choice ambiguous preferences universities anarchies "
                        "technology unclear organized decisions",
            "DOI": "x",
        }]}})
        terms = answer.terms.split()
        self.assertEqual(terms, sorted(terms))
        self.assertEqual(len(terms), len(set(terms)))

    def test_a_different_paper_coming_back_is_absent_not_found(self):
        # Bibliographic search is fuzzy and will hand back a neighbour paper.
        answer = self.resolve({"message": {"items": [{
            "title": ["Something Entirely Different About Photosynthesis"],
            "abstract": "<jats:p>Chloroplasts and light harvesting complexes.</jats:p>",
        }]}})
        self.assertEqual(answer.kind, ABSENT)
        self.assertEqual(answer.detail, "title mismatch")

    def test_a_record_without_a_deposited_abstract_is_absent(self):
        answer = self.resolve({"message": {"items": [{
            "title": ["A Garbage Can Model of Organizational Choice"],
        }]}})
        self.assertEqual(answer.kind, ABSENT)

    def test_a_teaser_too_short_to_be_an_abstract_is_absent(self):
        answer = self.resolve({"message": {"items": [{
            "title": ["A Garbage Can Model of Organizational Choice"],
            "abstract": "<jats:p>Read more.</jats:p>",
        }]}})
        self.assertEqual(answer.kind, ABSENT)

    def test_no_results_is_absent(self):
        self.assertEqual(self.resolve({"message": {"items": []}}).kind, ABSENT)

    def test_a_declined_request_passes_the_decline_through(self):
        answer = self.resolve(Answer(DECLINED, detail="HTTP 429"))
        self.assertEqual(answer.kind, DECLINED)


class TestOpenAlex(unittest.TestCase):
    def test_the_inverted_index_is_put_back_in_order(self):
        self.assertEqual(
            fa.reconstruct({"wage": [1], "minimum": [0], "effects": [2]}),
            "minimum wage effects")

    def test_an_empty_inverted_index_reconstructs_to_nothing(self):
        self.assertEqual(fa.reconstruct({}), "")

    def test_a_work_without_an_abstract_is_absent(self):
        with mock.patch("fetch_abstracts.get_json",
                        return_value=({"results": [{"id": "https://openalex.org/W1",
                                                    "title": "Panel data methods"}]}, None)):
            self.assertEqual(fa.openalex("Panel data methods").kind, ABSENT)


class TestEuropePmc(unittest.TestCase):
    def resolve(self, payload):
        with mock.patch("fetch_abstracts.get_json", return_value=(payload, None)):
            return fa.europepmc("A Programmable Dual-RNA-Guided DNA Endonuclease")

    def test_a_matching_record_with_an_abstract_is_found(self):
        answer = self.resolve({"resultList": {"result": [{
            "id": "22745249",
            "title": "A programmable dual-RNA-guided DNA endonuclease",
            "abstractText": "Bacteria and archaea use CRISPR loci and Cas proteins to "
                            "silence invading nucleic acids through targeted cleavage.",
        }]}})
        self.assertEqual(answer.kind, FOUND)
        self.assertEqual(answer.work_id, "22745249")
        self.assertIn("crispr", answer.terms)

    def test_a_neighbouring_paper_is_absent(self):
        answer = self.resolve({"resultList": {"result": [{
            "id": "1", "title": "Contributions to anti-racist science",
            "abstractText": "An entirely different paper with a long enough abstract "
                            "to pass the length floor comfortably here.",
        }]}})
        self.assertEqual(answer.kind, ABSENT)

    def test_no_results_is_absent(self):
        self.assertEqual(self.resolve({"resultList": {"result": []}}).kind, ABSENT)


ATOM_FEED = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <entry>
    <id>http://arxiv.org/abs/1706.03762v5</id>
    <title>Attention Is All You Need</title>
    <summary>The dominant sequence transduction models are based on complex recurrent
    or convolutional neural networks that include an encoder and a decoder.</summary>
  </entry>
</feed>
"""


class TestArxiv(unittest.TestCase):
    def resolve(self, body, title="Attention Is All You Need"):
        value = (None, body) if isinstance(body, Answer) else (body, None)
        with mock.patch("fetch_abstracts.get_text", return_value=value):
            return fa.arxiv(title)

    def test_a_matching_entry_is_found(self):
        answer = self.resolve(ATOM_FEED)
        self.assertEqual(answer.kind, FOUND)
        self.assertEqual(answer.work_id, "1706.03762v5")
        self.assertIn("transduction", answer.terms)

    def test_an_empty_feed_is_absent(self):
        empty = '<feed xmlns="http://www.w3.org/2005/Atom"></feed>'
        self.assertEqual(self.resolve(empty).kind, ABSENT)

    def test_a_different_preprint_coming_back_is_absent(self):
        # arXiv title search is fuzzy enough to return a paper that merely cites this one.
        self.assertEqual(self.resolve(ATOM_FEED, title="Deep Residual Learning").kind,
                         ABSENT)

    def test_an_unparseable_feed_is_declined_not_absent(self):
        # A truncated response is the server failing, not the preprint being missing.
        self.assertEqual(self.resolve("<feed><entry>").kind, DECLINED)

    def test_a_declined_request_passes_through(self):
        self.assertEqual(self.resolve(Answer(DECLINED, detail="HTTP 503")).kind, DECLINED)


class TestSourceRoster(unittest.TestCase):
    def test_the_default_roster_is_the_free_sources_in_order(self):
        names = [s.name for s in fa.build_sources("free", None)]
        self.assertEqual(names, list(fa.FREE_SOURCES))

    def test_openalex_is_never_in_the_default_roster(self):
        # It bills per request; spending money is the maintainer's decision.
        self.assertNotIn("openalex", fa.FREE_SOURCES)
        self.assertNotIn("openalex", [s.name for s in fa.build_sources("free", None)])

    def test_all_appends_openalex_after_the_free_sources(self):
        names = [s.name for s in fa.build_sources("all", None)]
        self.assertEqual(names, list(fa.FREE_SOURCES) + ["openalex"])

    def test_a_single_source_can_be_selected(self):
        self.assertEqual([s.name for s in fa.build_sources("arxiv", None)], ["arxiv"])

    def test_the_slowest_source_is_asked_last(self):
        # Only the residue the cheap sources could not answer pays arXiv's three
        # seconds per request.
        sources = fa.build_sources("free", None)
        self.assertEqual(max(sources, key=lambda s: s.pause).name, sources[-1].name)

    def test_pause_can_be_overridden_for_every_source(self):
        self.assertEqual({s.pause for s in fa.build_sources("free", 0.0)}, {0.0})


class TestTitleMatching(unittest.TestCase):
    def test_a_near_identical_title_matches(self):
        self.assertTrue(fa.title_matches(
            "RRT-Connect: An Efficient Approach to Single-Query Path Planning",
            "RRT-connect: An efficient approach to single-query path planning"))

    def test_an_unrelated_title_does_not(self):
        self.assertFalse(fa.title_matches("A Feature-Integration Theory of Attention",
                                          "Chloroplast light harvesting complexes"))

    def test_an_empty_side_never_matches(self):
        self.assertFalse(fa.title_matches("", "anything"))
        self.assertFalse(fa.title_matches("anything", ""))


class TestResolveAcrossSources(unittest.TestCase):
    """`resolve` is where one source's silence must not become the corpus's answer."""

    @staticmethod
    def source(name, answer):
        return Source(name, lambda _title, a=answer: a, pause=0.0)

    @staticmethod
    def resolve(title, sources):
        """`fetch_abstracts.resolve`, with its operator notices kept out of the log."""
        with contextlib.redirect_stderr(io.StringIO()):
            return fa.resolve(title, sources)

    def test_the_first_source_that_finds_it_wins_and_is_recorded(self):
        first = self.source("crossref", Answer(FOUND, work_id="10.1/x", terms="a b c"))
        second = self.source("openalex", Answer(FOUND, work_id="W1", terms="d e f"))
        answer, said_no = self.resolve("t", [first, second])
        self.assertEqual(answer.kind, FOUND)
        self.assertEqual(answer.detail, "crossref")
        self.assertEqual(said_no, set())

    def test_a_source_that_says_no_falls_through_to_the_next(self):
        first = self.source("crossref", Answer(ABSENT))
        second = self.source("openalex", Answer(FOUND, work_id="W1", terms="d e f"))
        answer, said_no = self.resolve("t", [first, second])
        self.assertEqual(answer.kind, FOUND)
        self.assertEqual(said_no, {"crossref"})

    def test_only_the_sources_that_answered_no_are_cached_as_misses(self):
        # The miss cache is keyed by source precisely so that adding a source later
        # re-opens every paper the previous one could not find.
        first = self.source("crossref", Answer(ABSENT))
        second = self.source("openalex", Answer(DECLINED, detail="HTTP 402"))
        answer, said_no = self.resolve("t", [first, second])
        self.assertEqual(answer.kind, ABSENT)
        self.assertEqual(said_no, {"crossref"})

    def test_every_source_declining_is_declined_and_never_a_miss(self):
        first = self.source("crossref", Answer(DECLINED, detail="HTTP 503"))
        second = self.source("openalex", Answer(DECLINED, detail="HTTP 429"))
        answer, said_no = self.resolve("t", [first, second])
        self.assertEqual(answer.kind, DECLINED)
        self.assertEqual(said_no, set())

    def test_a_declining_source_is_taken_out_of_the_run(self):
        # Asking an out-of-budget API 1,600 more times is futile and billable.
        calls = []

        def flaky(_title):
            calls.append(1)
            return Answer(DECLINED, detail="HTTP 429")

        source = Source("openalex", flaky, pause=0.0)
        self.resolve("t1", [source])
        self.assertFalse(source.available)
        self.resolve("t2", [source])
        self.assertEqual(len(calls), 1)


class TestMissCacheFormat(unittest.TestCase):
    def test_round_trips_through_the_cache_file(self):
        with mock.patch.object(fa, "MISSES", fa.ROOT / "tools/.cache/_test-misses.tsv"):
            try:
                fa.save_misses({"A paper": "crossref", "B paper": "crossref,openalex"})
                self.assertEqual(fa.load_misses(),
                                 {"A paper": "crossref", "B paper": "crossref,openalex"})
            finally:
                fa.MISSES.unlink(missing_ok=True)

    def test_a_missing_cache_reads_as_empty(self):
        with mock.patch.object(fa, "MISSES", fa.ROOT / "tools/.cache/_absent.tsv"):
            self.assertEqual(fa.load_misses(), {})


if __name__ == "__main__":
    unittest.main()
