#!/usr/bin/env python3
"""Build the **subject** half of the venue vocabulary: what each venue publishes about.

Why this exists
---------------
``scope-postings.tsv`` is derived from each pack's own prose — submission rules, review
mechanics, formatting, editorial policy. That is what the repository *knows* about a
venue, and it is the wrong register for the query it has to answer. An author's title is
about a subject; a pack's prose is about a process. So the matcher was asked to connect
"Deep Contextualized Word Representations" to ACL through a vocabulary in which ACL is
mostly a set of anonymity rules, and it could not: on the gold set's dev half, 14% of
papers never retrieved their true venue **at any depth**, and R@10 sat at 46.9%.

This tool adds the missing register. For every venue it resolves a bibliographic source
and harvests the titles of articles the venue actually published, then derives a second
ranked vocabulary from those titles alone. Two vocabularies, one merge, measured
separately — see ``eval/RESULTS.md``.

Free sources only, by venue type
--------------------------------
* **journals → Crossref.** ``/journals?query=`` resolves a title to an ISSN, then
  ``/journals/{issn}/works`` returns deposited article titles. Free, no key, and the
  ISSN it lands on is written into ``venue-sources.tsv`` so a wrong resolution is a
  reviewable line rather than an invisible one.
* **conferences → DBLP.** ``/search/venue/api`` resolves a name to a stream key
  (``conf/recsys``), then ``/search/publ/api?q=stream:conf/recsys:`` pages the titles.
  DBLP is the only free source that models a conference *series* as one thing.
* **OpenAlex is opt-in** (``--source openalex``), on the same reasoning as
  ``fetch_abstracts.py``: it bills per request, and spending money is the maintainer's
  decision.

**The 105 Chinese-language journals have no subject vocabulary and cannot get one this
way.** That is a measurement, not an assumption: 28 of them state an ISSN in their own
pack, and Crossref's journal endpoint knows **none** of the 28 — these venues do not
deposit article-level DOIs. Neither does DBLP index them. Closing the gap means reading
the journals' own sites (magtech, SUFE, CNKI-hosted, and several bespoke platforms), which
is a different tool from this one. Do not spend another pass re-asking Crossref.

Resolution is exact or it does not happen
-----------------------------------------
A fuzzy venue match is worse than no match: it does not degrade the ranking, it fills a
venue's vocabulary with another venue's subjects. Every rule below requires **exact
equality after normalisation**, and the rule that fired is recorded per row.

The one rule that is not a plain equality exists because of a real failure. Searching
Crossref for *Economic Policy* (Oxford) returns *American Economic Journal: Economic
Policy*, which carries "Economic Policy" among its alternate titles — so an
alternate-title rule matched it and gave the Oxford journal the AEJ's article stream.
An alternate title is therefore only accepted when it is **not itself the display name
of some other venue in the index**. That keeps ``AEJ Microeconomics`` (which the index
stores under its abbreviation and only an alternate title can reach) and rejects
``Economic Policy``.

And exact is not always enough
------------------------------
An exact name match is evidence about *words*. For a Chinese-language journal the index
carries a **translated** name, which is not a registered title, and Crossref's registry
holds unrelated journals carrying each such translation. Six Chinese venues resolved on
name equality before this was checked, and at least three were the wrong journal:
《金融研究》 (ISSN 1002-7246) matched the Southern Finance Association's *Journal of
Financial Research* (0270-2592); 《世界经济》 (1002-9621) matched an unrelated *Journal of
World Economy* (2709-3999); 《中国社会科学》 (1002-4921) matched its own English translation
edition (0252-9203), a different serial. Each would have been handed another journal's
subject vocabulary — which does not rank a venue badly, it ranks a *different* venue in
its place.

So ``issn_veto`` adds two conditions on top of the name rules. Where the pack states an
ISSN (121 of 744 do), the candidate must carry it. Where the venue is Chinese-language
and nothing corroborates the name, the match is refused outright and the venue keeps its
prose vocabulary. Refusals are written to ``venue-sources.tsv`` as decisions, not as
absences, so the next pass does not re-ask and a reader can see why a venue has no
subject vocabulary.

Politeness and resumption
-------------------------
The lookups are independent and latency-bound, so they run in a small thread pool. Two
things keep that from becoming a burst: requests are capped and paced **per host** (a
DBLP venue search takes six to twelve seconds and answers a burst with 503, so it runs
three at a time while Crossref runs unthrottled), and every response is cached on disk.
Only *permanent* refusals — 404 and 410 — are cached alongside them; caching a 503 would
freeze a rate-limit into "this venue has no source", which is the same declined-is-not-
absent mistake ``fetch_abstracts.py`` exists to prevent. Rerun to fill gaps; the cache
makes a second pass cost only what the first one could not finish.

Leakage
-------
The gold set is the repository's exemplar libraries: real papers, published in the venue
being harvested. A harvested title that *is* a gold paper would let the eval retrieve a
paper by having previously read it, so every harvested title is compared against the
gold set's titles and dropped on a match. The comparison is on the normalised title, and
the count of what it dropped is printed and stored in the postings header, because a
leak guard nobody can see the size of is a claim rather than a control.

What that guard does **not** remove is the residual optimism of harvesting a venue's own
publication stream at all: a gold paper's companion piece, its authors' later work, and
its subfield's subsequent vocabulary are all still in there. That is not a defect to fix
— it is what any real recommender has and what makes this vocabulary useful — but it
means the topic rows in ``eval/RESULTS.md`` are a *different measurement* from the scope
rows, not merely a better one, and they say so.

Usage
-----
    python3 tools/fetch_venue_topics.py --resolve            # network: rebuild the map
    python3 tools/fetch_venue_topics.py --harvest            # network: rebuild postings
    python3 tools/fetch_venue_topics.py --resolve --harvest  # both, in one pass
    python3 tools/fetch_venue_topics.py --source openalex    # add the paid fallback
    python3 tools/fetch_venue_topics.py --check              # offline: index still matches
    python3 tools/fetch_venue_topics.py                      # offline: coverage report

Network is required for ``--resolve`` and ``--harvest``, so neither is part of
``tools/run_checks.py``. The outputs are committed; CI reads them and never fetches.

Outputs
-------
``shared-resources/journal-selection/venue-sources.tsv``  (reviewable resolution map)
``shared-resources/journal-selection/topic-postings.tsv`` (the inverted vocabulary)
"""

from __future__ import annotations

import argparse
import contextlib
import csv
import hashlib
import html
import json
import math
import os
import re
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from venue_lib import ROOT, index_digest, tokenize

INDEX = ROOT / "shared-resources/journal-selection/venue-index.tsv"
GOLD = ROOT / "shared-resources/journal-selection/eval/gold-set.tsv"
SOURCES = ROOT / "shared-resources/journal-selection/venue-sources.tsv"
POSTINGS = ROOT / "shared-resources/journal-selection/topic-postings.tsv"
CACHE = ROOT / "tools/.cache/venue-topics"

SOURCE_COLUMNS = ["venue_id", "provider", "source_key", "issns", "source_name",
                  "works", "rule"]

# A provider value that means "a candidate was found and rejected". See `issn_veto`.
REFUSED = "refused"

# Venues no exact rule can reach, resolved by hand and verified against DBLP on
# 2026-08-27. Each is here because automatic resolution is either impossible or wrong,
# never merely absent — an entry is a claim that someone opened the page.
#
# The rules below cannot get these because the index writes an acronym and DBLP writes
# something with no word in common ("ATC" against "USENIX Annual Technical Conference"),
# or because two real conferences share the acronym and the pack's own prose names both
# — `ITCS-Skills` warns its reader off *Information Technology and Computer Science*, so
# the phrase test finds that name in the pack as readily as its own.
SOURCE_OVERRIDES: dict[str, tuple[str, str, str]] = {
    # venue_id: (provider, key, the name that key resolves to on the provider)
    "atc": ("dblp", "conf/usenix", "USENIX Annual Technical Conference (USENIX ATC)"),
    "vis": ("dblp", "conf/visualization", "IEEE Visualization Conference (VIS)"),
    "usenix-security": ("dblp", "conf/uss", "USENIX Security Symposium"),
    "itcs": ("dblp", "conf/innovations",
             "Innovations in Theoretical Computer Science (ITCS)"),
    "conext": ("dblp", "conf/conext",
               "Conference on Emerging Network Experiment and Technology (CoNEXT)"),
    "acm-conext": ("dblp", "conf/conext",
                   "Conference on Emerging Network Experiment and Technology (CoNEXT)"),
    "acm-sigmod-international-conference-on-management-of-data":
        ("dblp", "conf/sigmod", "ACM SIGMOD Conference (SIGMOD)"),
}
HARVESTABLE = ("crossref", "dblp", "openalex")

# How many published titles to read per venue. Measured on the dev half at the pilot
# stage: 400 titles is where the vocabulary stops changing much and the harvest still
# fits in one polite pass over 744 venues. Crossref and DBLP both page at 200-1000.
HARVEST_TITLES = 400
# Only recent output. A venue's subject vocabulary is a claim about what it publishes
# *now* — the question an author is asking — and a 1990s back catalogue answers a
# different one. It also keeps most of the (older, famous) gold papers out of the
# harvest before the leak guard has to.
FROM_YEAR = 2012
# Terms kept per venue, ranked. Measured on the gold set's `dev` half by truncating a
# built index on rank, which is exactly what a shallower build produces:
#
#     depth    150    300    450    600    900
#     R@10    59.6   61.6   63.1   63.1   63.3     (dev)
#     R@1     23.9   24.6   24.5   25.0   25.8
#     size     1.3    2.9    4.7    6.8   11.0 MB  (topic-postings.tsv)
#
# R@10 has stopped moving by 450. What keeps improving past it is the head of the
# ranking — R@1 and MRR — and that is worth something to a shortlist, so this sits at
# 600 rather than at the flattest point: it holds R@10, keeps most of the R@1, and
# leaves the committed file about the size of the scope index beside it. 900 buys 0.2
# points of R@10 for another four megabytes rewritten on every harvest.
TOPIC_DEPTH = 600
# A term more than half the corpus uses cannot separate one venue from another.
DF_CEILING = 0.5

_TAG = re.compile(r"<[^>]+>")
_WS = re.compile(r"\s+")
_NORM = re.compile(r"[^a-z0-9一-鿿]+")
# Dropped from a venue *name* before comparison: they are noise in the name, not in the
# subject. "The Journal of Finance" and "Journal of Finance" are the same journal.
_NAME_NOISE = re.compile(r"\b(the|of|for|in|and|on|a|an)\b")


# --------------------------------------------------------------------------- http


class Declined(RuntimeError):
    """The source refused to answer. That is not the same as answering 'nothing'."""


def _mailto() -> str:
    return os.environ.get("CROSSREF_MAILTO") or os.environ.get("OPENALEX_MAILTO") or ""


def _cache_path(url: str) -> Path:
    return CACHE / (hashlib.sha1(url.encode("utf-8")).hexdigest() + ".json")


# Per-host concurrency cap and a floor on the gap between requests.
#
# The lookups are independent and latency-bound, so they run in a thread pool — but a
# pool is a burst, and DBLP answers a burst with 503. Retrying through the burst is the
# obvious fix and the wrong one: it turns a throttle into a five-attempt backoff per
# venue, and the pass then spends its wall clock waiting to be refused.
#
# Serialising DBLP entirely is the *other* wrong fix, and it is the one measured here:
# a DBLP request takes five to twelve seconds to answer, so one-at-a-time puts a floor of
# half an hour on the conference lookups alone. Two at a time, a second apart, is where
# the refusals stop; three drew them back on the harvest pass, which asks four times as
# many requests as the resolution pass does. Throttling is per host, so Crossref keeps
# running at full rate while a DBLP request is in flight; its entry is present and
# unthrottled on purpose, so the next person to add a source has somewhere to put its
# rate rather than discovering this comment after the fact.
#
# Even at that rate a long harvest eventually draws a block that lasts minutes and
# refuses *everything*, static pages included — DBLP budgets by client, not by burst. So
# the harvest is built to converge rather than to succeed: anything refused comes back
# empty, successful pages are cached, and re-running picks up exactly what was missed.
# Two or three passes with a pause between them is the intended way to run it, and the
# warning printed at the end of `--harvest` says how much is still outstanding.
#
# The cache is what makes that safe rather than merely cheap. `--harvest` rebuilds the
# whole postings file each time, so without it a venue that succeeded on one pass could
# lose its vocabulary on the next; because every successful page is on disk, a re-run
# re-reads it instead of re-asking, and coverage only ever moves up. Clearing
# `tools/.cache/venue-topics/` therefore means committing to one complete pass.
_HOST_LIMITS = {                       # host -> (max concurrent, min seconds between)
    "dblp.org": (2, 0.75),
    "api.crossref.org": (8, 0.0),
    "api.openalex.org": (8, 0.0),
}
_HOST_GATES: dict = {}
_HOST_TABLE_LOCK = threading.Lock()


def _host_gate(url: str):
    """Context manager holding one host's slot at its minimum interval."""
    host = urllib.parse.urlsplit(url).hostname or ""
    limit = _HOST_LIMITS.get(host)
    if not limit:
        return contextlib.nullcontext()
    concurrency, interval = limit
    with _HOST_TABLE_LOCK:
        if host not in _HOST_GATES:
            _HOST_GATES[host] = (threading.Semaphore(concurrency),
                                 threading.Lock(), [0.0])
        semaphore, pace_lock, last = _HOST_GATES[host]

    @contextlib.contextmanager
    def gate():
        with semaphore:
            if interval:
                with pace_lock:
                    wait = interval - (time.monotonic() - last[0])
                    if wait > 0:
                        time.sleep(wait)
                    last[0] = time.monotonic()
            yield

    return gate()


def fetch(url: str, *, tries: int = 5, pause: float = 0.34) -> dict:
    """GET JSON, with a cache on disk and a backoff on the two sources' throttles.

    DBLP answers 503 to a burst and 200 to the same request a few seconds later, so a
    single attempt would silently produce a venue with no vocabulary rather than an
    error. Cached responses make a re-run of a partially finished harvest cheap.

    *Permanent* refusals are cached too, as a marker rather than a payload: without that,
    a re-run re-attempts every URL the source declined — five tries each behind an
    increasing backoff — and a pass over 744 venues spends most of its wall clock
    re-learning what the last pass already found out.

    Only 404 and 410 qualify. A 503 or a 429 is the source saying *not now*, and caching
    it would freeze a rate-limit burst into a permanent "this venue has no source" — the
    same declined-is-not-absent rule `fetch_abstracts.py` exists to enforce, arriving
    here through the cache rather than through the parser. Delete
    `tools/.cache/venue-topics/` to re-ask about everything.
    """
    CACHE.mkdir(parents=True, exist_ok=True)
    path = _cache_path(url)
    if path.exists():
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except ValueError:
            path.unlink()
        else:
            if isinstance(payload, dict) and payload.get("__declined__"):
                raise Declined(f"{url}: {payload['__declined__']} (cached refusal)")
            return payload
    last: Exception | None = None
    agent = "AJS-venue-topics/1.0 (+https://github.com/brycewang-stanford/Awesome-Journal-Skills"
    agent += f"; mailto:{_mailto()})" if _mailto() else ")"
    for attempt in range(tries):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": agent})
            with _host_gate(url):
                with urllib.request.urlopen(request, timeout=60) as handle:
                    payload = json.loads(handle.read().decode("utf-8", "replace"))
            path.write_text(json.dumps(payload), encoding="utf-8")
            time.sleep(pause)
            return payload
        except urllib.error.HTTPError as error:
            last = error
            if error.code in (404, 410):                 # the source answered "no such thing"
                path.write_text(json.dumps({"__declined__": f"HTTP {error.code}"}),
                                encoding="utf-8")
                raise Declined(f"{url}: HTTP {error.code}") from error
            time.sleep(1.5 * (attempt + 1))
        except Exception as error:                       # noqa: BLE001 - reported below
            last = error
            time.sleep(1.5 * (attempt + 1))
    raise Declined(f"{url}: {last}")


# --------------------------------------------------------------------------- text


def clean_title(raw: str) -> str:
    """Publisher-deposited titles carry markup, entities and layout whitespace."""
    return _WS.sub(" ", html.unescape(_TAG.sub(" ", raw))).strip()


def norm_name(raw: str) -> str:
    """Venue-name normal form: case, punctuation, ampersands and article words."""
    text = raw.lower().replace("&", " and ")
    text = _NORM.sub(" ", text)
    text = _NAME_NOISE.sub(" ", text)
    return " ".join(text.split())


def norm_title(raw: str) -> str:
    """Paper-title normal form, used only by the leak guard."""
    return " ".join(_NORM.sub(" ", clean_title(raw).lower()).split())


# An ISSN as the packs write it: "ISSN 1002-9621", "ISSN | 1002-9621", "ISSN: 1002-9621".
_ISSN = re.compile(r"\bISSN[^0-9A-Za-z]{0,15}(\d{4}\s?-\s?\d{3}[\dXx])")


def stated_issns(venue: dict) -> set[str]:
    """The ISSNs the venue's own pack writes down, if any.

    Used as a **veto**, never as a lookup key: only 121 of 744 venues state one, so
    requiring it would refuse most of the corpus, but where it exists it settles the
    question a name match cannot.
    """
    out: set[str] = set()
    for field in ("source_map", "profile_path"):
        if venue.get(field):
            out |= _issns_in(ROOT / venue[field])
    if venue.get("pack_dir"):
        out |= _issns_in(ROOT / venue["pack_dir"] / "README.md")
    return out


def _issns_in(path: Path) -> set[str]:
    if not path.exists() or not path.is_file():
        return set()
    text = path.read_text(encoding="utf-8", errors="replace")
    return {m.group(1).replace(" ", "").upper() for m in _ISSN.finditer(text)}


def issn_veto(venue: dict, found: dict) -> str | None:
    """Why this resolution must be refused, or None if it may stand.

    Two rules, both learned from wrong answers this tool produced.

    **A stated ISSN that the candidate does not carry.** 《金融研究》 is ISSN 1002-7246;
    Crossref's exact-title match for "Journal of Financial Research" is 0270-2592, the
    Southern Finance Association's US journal. Same words, different serial, and the
    vocabulary of one would have been attached to the other.

    **A Chinese-language venue with nothing to corroborate a name.** For a Chinese
    serial the index's Latin display name is a *translation*, not a registered title, and
    Crossref's registry holds several unrelated journals carrying each such translation —
    "Journal of World Economy", "Journal of Management World", "Journal of Finance and
    Economics" all matched something, and none of them matched the journal meant. Where
    the pack states no ISSN there is no evidence left, so the venue keeps its prose
    vocabulary and `match_venues.py` marks it. Six of these resolved before this rule
    existed and at least three were the wrong journal, which is worse than none: a wrong
    vocabulary does not rank a venue badly, it ranks a different venue in its place.
    """
    stated = stated_issns(venue)
    candidate = {i.upper() for i in (found.get("issns") or []) if i}
    if stated:
        if candidate and not (stated & candidate):
            return (f"ISSN mismatch: pack states {sorted(stated)}, "
                    f"{found['provider']} candidate carries {sorted(candidate)}")
        if candidate:
            return None                       # corroborated; region no longer matters
    if venue.get("region") == "china" and found["provider"] != "dblp":
        return ("Chinese-language venue matched on a translated name with no ISSN "
                "to corroborate it")
    return None


def load_index() -> list[dict]:
    with INDEX.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def gold_titles() -> set[str]:
    if not GOLD.exists():
        return set()
    with GOLD.open(encoding="utf-8") as handle:
        return {norm_title(row["paper_title"]) for row in csv.DictReader(handle, delimiter="\t")}


# --------------------------------------------------------------------------- resolve


def _crossref_search(query: str) -> dict | None:
    url = f"https://api.crossref.org/journals?query={urllib.parse.quote(query)}&rows=20"
    if _mailto():
        url += f"&mailto={urllib.parse.quote(_mailto())}"
    try:
        return fetch(url)
    except Declined:
        return None


def crossref_by_issn(issns: set[str]) -> dict | None:
    """Resolve straight from an ISSN the pack itself states.

    An ISSN identifies a serial; a title identifies some words. Where the pack has
    written one down this is the only lookup worth doing, and it is tried first — the
    name search had already offered *Manufacturing and Service Operations Management*
    (2616-3349) for M&SOM (1523-4614) and *Journal of Software* (1796-217X) for
    《软件学报》 (1000-9825), both of them different journals wearing the same title.
    Both are one request away from being right.
    """
    for issn in sorted(issns):
        url = f"https://api.crossref.org/journals/{urllib.parse.quote(issn)}"
        if _mailto():
            url += f"?mailto={urllib.parse.quote(_mailto())}"
        try:
            payload = fetch(url)
        except Declined:
            continue                          # 404 here means Crossref has no such serial
        message = payload.get("message") or {}
        if not message.get("title"):
            continue
        return {"provider": "crossref", "key": issn,
                "issns": [i for i in (message.get("ISSN") or []) if i] or [issn],
                "name": message["title"], "rule": "crossref-issn",
                "works": message.get("counts", {}).get("total-dois", 0)}
    return None


def crossref_journal(name: str, taken_names: set[str]) -> dict | None:
    # Two query forms, because Crossref's journal search is sensitive to the words the
    # index happens to spell out. "Agriculture Ecosystems and Environment" returns
    # nothing; the normalised "agriculture ecosystems environment" returns the journal,
    # whose registered title is "Agriculture Ecosystems & Environment". The *matching*
    # rule is unchanged — still exact equality after normalisation — so a looser query
    # widens what is offered, never what is accepted.
    target = norm_name(name)
    payload = _crossref_search(name)
    if not _crossref_candidates(payload, target, taken_names) and target != name.lower():
        payload = _crossref_search(target) or payload
    return _best(_crossref_candidates(payload, target, taken_names))


def _best(pool: list[dict]) -> dict | None:
    if not pool:
        return None
    pool.sort(key=lambda c: -(c["works"] or 0))
    best = dict(pool[0])
    best["provider"] = "crossref"
    return best


def _crossref_candidates(payload: dict | None, target: str,
                         taken_names: set[str]) -> list[dict]:
    if not payload:
        return []
    exact: list[dict] = []
    alias: list[dict] = []
    for item in payload.get("message", {}).get("items", []):
        issns = [i for i in (item.get("ISSN") or []) if i]
        if not issns:
            continue
        title = item.get("title") or ""
        if norm_name(title) == target:
            exact.append({"key": issns[0], "issns": issns, "name": title,
                          "rule": "crossref-title",
                          "works": item.get("counts", {}).get("total-dois", 0)})
            continue
        for other in item.get("alt-titles") or []:
            if norm_name(other) != target:
                continue
            # See the module docstring: an alternate title that is some *other* index
            # venue's display name is that venue's name, not this one's alias.
            if target in taken_names:
                continue
            alias.append({"key": issns[0], "issns": issns, "name": title,
                          "rule": "crossref-alt-title",
                          "works": item.get("counts", {}).get("total-dois", 0)})
            break
    return exact or alias


# Words a conference name carries or drops without becoming a different conference.
# The index stores "ACM SIGCOMM"; DBLP stores "ACM SIGCOMM Conference (SIGCOMM)" and
# "International ACM SIGACCESS Conference on Computers and Accessibility (ASSETS)".
# Requiring bare string equality across that gap resolved 0 of the first 90 conferences.
_ORG_WORDS = {"acm", "ieee", "usenix", "aaai", "siam", "ifip", "eurographics", "acl",
              "international", "annual", "joint", "symposium", "conference", "workshop",
              "european", "asia", "asian", "ai"}

# The subset that may be dropped from *both* names before comparing. Deliberately
# smaller than `_ORG_WORDS`: sponsoring bodies and "international / annual / joint" are
# decoration, but "conference", "symposium" and "workshop" are not — dropping those would
# let a workshop match the conference it attaches to, and dropping regional qualifiers
# would collapse the International, European and Asian conferences on machine learning
# into one venue. Both of those are in this corpus.
_DECORATION = {"acm", "ieee", "usenix", "aaai", "siam", "ifip", "acl",
               "international", "annual", "joint", "the"}
_CORE_MIN_WORDS = 3


def _core_name(text: str) -> str:
    return " ".join(w for w in text.split() if w not in _DECORATION)


def _dblp_rules(target: str, venue: str, acronym: str) -> str | None:
    """Which rule, if any, makes this DBLP venue the venue the index named.

    Four rules, each an equality after normalisation — never a similarity score. A fuzzy
    conference match does not produce a slightly worse vocabulary, it produces another
    conference's vocabulary, and DBLP's own search is fuzzy enough to offer ER, MoDELS
    and CAiSE for "International Conference on Software Engineering".
    """
    # DBLP prints the acronym in the display string: "... (RecSys)".
    bare = re.sub(r"\s*\([^()]*\)\s*$", "", venue)
    normalised_bare = norm_name(bare)
    if target in {norm_name(venue), normalised_bare}:
        return "dblp-venue"
    if not acronym:
        return None
    normalised_acronym = norm_name(acronym)
    if target == normalised_acronym:
        return "dblp-acronym"
    # "ACM MobiCom" = an organisation prefix the index keeps and DBLP's title does not.
    target_words = target.split()
    if (len(target_words) > 1 and " ".join(target_words[1:]) == normalised_acronym
            and target_words[0] in _ORG_WORDS):
        return "dblp-org-acronym"
    # "ACM SIGACCESS Conference on Computers and Accessibility" against DBLP's
    # "International ACM SIGACCESS Conference on Computers and Accessibility": the same
    # name with a generic word in front. Only generic words may be dropped, and the
    # match must land on a token boundary.
    bare_words = normalised_bare.split()
    if len(bare_words) > len(target_words):
        cut = len(bare_words) - len(target_words)
        if (bare_words[cut:] == target_words
                and all(word in _ORG_WORDS for word in bare_words[:cut])):
            return "dblp-generic-prefix"
    # "ACM Conference on Intelligent User Interfaces" and DBLP's "International
    # Conference on Intelligent User Interfaces" are the same meeting described by two
    # sponsoring bodies. Strip the decoration from both sides and compare what is left —
    # but only when what is left is long enough to name something, so that two short
    # titles cannot meet at a shared generic remainder.
    core = _core_name(target)
    if len(core.split()) >= _CORE_MIN_WORDS and core == _core_name(normalised_bare):
        return "dblp-core-name"
    return None


# Words that carry no evidence about which conference a name refers to.
_EMPTY_WORDS = {"conference", "symposium", "workshop", "international", "annual",
                "joint", "meeting", "acm", "ieee", "usenix", "aaai", "siam", "ifip",
                "european", "proceedings", "series"}
# How many content words of a DBLP venue's full name must also appear in the pack's own
# description before a bare-acronym match is believed.
_CORROBORATING_WORDS = 2
# The score for "the pack writes this venue's name out in full", which outranks any
# amount of word overlap.
_NAMED = 1000
# How much each rule is trusted, so a full-name match is never displaced by an acronym.
_RULE_STRENGTH = {"dblp-venue": 3, "dblp-generic-prefix": 2, "dblp-core-name": 2,
                  "dblp-org-acronym": 1, "dblp-acronym": 1}


def pack_title_text(venue: dict) -> str:
    """The repository's own words about which venue this row is, and only this row.

    For a breadth profile that is the venue's own `SKILL.md`; for a depth pack it is the
    plugin description plus the README head. The distinction matters: a breadth row's
    `pack_dir` is the *bundle* it lives in, whose README describes 155 conferences and
    says nothing in particular about any of them — reading that instead refused
    `acm-sigcomm` for want of the word "SIGCOMM".
    """
    profile = venue.get("profile_path")
    if profile:
        path = ROOT / profile
        if path.exists():
            return norm_name(path.read_text(encoding="utf-8", errors="replace")[:1200])
    pack = venue.get("pack_dir")
    if not pack:
        return ""
    parts = []
    plugin = ROOT / pack / ".claude-plugin" / "plugin.json"
    try:
        parts.append(json.loads(plugin.read_text(encoding="utf-8")).get("description", ""))
    except (OSError, ValueError):
        pass
    # The source map is included because it is the one file guaranteed to spell the
    # venue out: a depth pack's README and plugin description are written about the
    # *process* and can go six hundred words without naming the conference in full.
    # `IJCAI-Skills` is exactly that — its opening never says "artificial intelligence".
    for name, limit in (("README.md", 1200), ("resources/official-source-map.md", 4000)):
        path = ROOT / pack / name
        if path.exists():
            parts.append(path.read_text(encoding="utf-8", errors="replace")[:limit])
    return norm_name(" ".join(parts))


def corroboration(venue: dict, dblp_name: str) -> tuple[int, int]:
    """(content words of `dblp_name` the pack also uses, how many are required).

    An acronym is not an identifier. `FAST-Skills` is the USENIX Conference on File and
    Storage Technologies; DBLP's first venue hit for "FAST" is *Formal Aspects in
    Security and Trust*, and the acronym rule took it — handing a storage pack a security
    conference's subject vocabulary. What the repository does know is what the pack says
    about itself, so a bare-acronym match has to overlap that.

    The count is returned rather than a verdict because "does it pass" is the wrong
    question when two candidates both do. Searching DBLP for `ITCS` offers *Information
    Technology Convergence and Services* and *Innovations in Theoretical Computer
    Science*, and a first-past-the-post rule takes whichever DBLP ranked first.

    A pack with nothing to say about itself, or a candidate whose name is all
    organisation words, corroborates trivially: silence is not disagreement.
    """
    text = pack_title_text(venue)
    bare = norm_name(re.sub(r"\s*\([^()]*\)\s*$", "", dblp_name))
    words = [w for w in bare.split() if len(w) > 3 and w not in _EMPTY_WORDS]
    if not text or not words:
        return (_NAMED, 0)
    haystack = f" {text} "
    # The pack writing the candidate's name out in full settles it, and nothing else
    # does. Bag overlap saturates: every word of *Information Technology Convergence and
    # Services* appears somewhere in `ITCS-Skills`, and so does every word of
    # *Innovations in Theoretical Computer Science*, which is the conference it means.
    # Only one of the two is written there as a phrase.
    if bare and f" {bare} " in haystack:
        return (_NAMED, 0)
    # A name that *is* its acronym ("ACM SIGMOD Conference") leaves one content word,
    # and demanding two of one is a rejection dressed as a rule. Ask for all of what
    # there is, up to the threshold.
    need = min(_CORROBORATING_WORDS, len(words))
    return (sum(1 for w in words if f" {w} " in haystack), need)


def acronym_corroborated(venue: dict, dblp_name: str) -> bool:
    matched, need = corroboration(venue, dblp_name)
    return matched >= need


def dblp_conference(name: str, venue: dict | None = None) -> dict | None:
    query = urllib.parse.quote(name, safe="")
    url = f"https://dblp.org/search/venue/api?q={query}&h=30&format=json"
    try:
        payload = fetch(url)
    except Declined:
        return None
    hits = payload.get("result", {}).get("hits", {}).get("hit") or []
    target = norm_name(name)
    candidates = []
    for hit in hits:
        info = hit.get("info", {})
        venue_name = info.get("venue") or ""
        rule = _dblp_rules(target, venue_name, info.get("acronym") or "")
        if not rule:
            continue
        match = re.search(r"/db/(conf/[^/]+)", info.get("url") or "")
        if not match:
            continue
        matched, need = ((1, 0) if venue is None
                         else corroboration(venue, venue_name))
        # Only the acronym rules are weak enough to need corroboration; the others
        # already matched on the venue's full name.
        if rule in ("dblp-acronym", "dblp-org-acronym") and matched < need:
            continue
        candidates.append((_RULE_STRENGTH[rule], matched, len(candidates), rule,
                           match.group(1), venue_name))
    if not candidates:
        return None
    # Strongest rule first, then best corroborated, then DBLP's own order as the
    # tie-break so the result is reproducible.
    candidates.sort(key=lambda c: (-c[0], -c[1], c[2]))
    _, _, _, rule, key, venue_name = candidates[0]
    return {"provider": "dblp", "key": key, "name": venue_name,
            "works": 0, "rule": rule}


def openalex_source(name: str, taken_names: set[str]) -> dict | None:
    query = urllib.parse.quote(name)
    url = f"https://api.openalex.org/sources?search={query}&per_page=20"
    if _mailto():
        url += f"&mailto={urllib.parse.quote(_mailto())}"
    try:
        payload = fetch(url)
    except Declined:
        return None
    target = norm_name(name)
    exact: list[dict] = []
    alias: list[dict] = []
    for item in payload.get("results", []):
        identifier = (item.get("id") or "").rsplit("/", 1)[-1]
        if not identifier:
            continue
        record = {"provider": "openalex", "key": identifier,
                  "issns": [i for i in (item.get("issn") or []) if i],
                  "name": item.get("display_name") or "",
                  "works": item.get("works_count") or 0}
        if norm_name(record["name"]) == target:
            exact.append({**record, "rule": "openalex-name"})
            continue
        others = list(item.get("alternate_titles") or [])
        if item.get("abbreviated_title"):
            others.append(item["abbreviated_title"])
        if any(norm_name(o) == target for o in others) and target not in taken_names:
            alias.append({**record, "rule": "openalex-alt-title"})
    pool = exact or alias
    if not pool:
        return None
    pool.sort(key=lambda c: -(c["works"] or 0))
    return pool[0]


def resolve_one(venue: dict, taken: set[str], use_openalex: bool) -> dict | None:
    name = venue["display_name"]
    # A venue's own name never counts as "some other venue's name" for itself.
    others = taken - {norm_name(name)}
    order = ((dblp_conference, crossref_journal) if venue["venue_type"] == "conference"
             else (crossref_journal, dblp_conference))
    override = SOURCE_OVERRIDES.get(venue["venue_id"])
    if override:
        provider, key, source_name = override
        return {"provider": provider, "key": key, "issns": [], "name": source_name,
                "works": 0, "rule": "override"}

    # An ISSN the pack states beats every name rule below it, and settles the region
    # question at the same time: a Chinese serial Crossref actually registers is not a
    # translated-name guess, it is that serial.
    stated = stated_issns(venue)
    if stated:
        found = crossref_by_issn(stated)
        if found:
            return found

    refusals: list[str] = []
    finders = list(order) + ([openalex_source] if use_openalex else [])
    for finder in finders:
        found = (finder(name, others) if finder is not dblp_conference
                 else finder(name, venue))
        if not found:
            continue
        refusal = issn_veto(venue, found)
        if refusal:
            refusals.append(f"{found['provider']}:{found['key']} — {refusal}")
            continue
        return found
    if refusals:
        # A refusal is a decision, and it is worth as much as a match: it records that
        # something was found and rejected, so the next pass does not re-ask and a
        # maintainer reading `venue-sources.tsv` can see *why* a venue has no subject
        # vocabulary rather than assuming nothing was ever offered.
        return {"provider": REFUSED, "key": "-", "issns": [], "name": name,
                "works": 0, "rule": f"refused: {refusals[0]}"}
    return None


def resolve_all(venues: list[dict], *, use_openalex: bool, limit: int | None,
                existing: dict[str, dict], jobs: int = 8) -> dict[str, dict]:
    """venue_id -> resolution record. Rows already resolved are kept, not re-asked.

    Resolution is one independent lookup per venue and dominated by round-trip latency,
    so it runs in a small thread pool. Small on purpose: both APIs are free, neither
    charges for politeness, and DBLP answers a burst with 503. Responses are cached on
    disk, so an interrupted pass resumes without re-asking.
    """
    # Every display name in the index, so an alternate-title rule can tell an alias
    # apart from a different venue's actual name.
    taken = {norm_name(v["display_name"]) for v in venues}
    resolved = dict(existing)
    pending = [v for v in venues if v["venue_id"] not in resolved]
    if limit:
        pending = pending[:limit]
    done = 0
    with ThreadPoolExecutor(max_workers=jobs) as pool:
        # Submission order, so the progress line counts up the way the index reads.
        futures = {pool.submit(resolve_one, v, taken, use_openalex): v for v in pending}
        for future, venue in futures.items():
            try:
                found = future.result()
            except Exception as error:                   # noqa: BLE001 - reported below
                found = None
                print(f"  {venue['venue_id']}: {error}", file=sys.stderr, flush=True)
            done += 1
            if found:
                resolved[venue["venue_id"]] = found
                print(f"  [{done}/{len(pending)}] {venue['venue_id']} -> "
                      f"{found['provider']}:{found['key']} ({found['rule']})", flush=True)
            else:
                print(f"  [{done}/{len(pending)}] {venue['venue_id']} -> unresolved",
                      flush=True)
    return resolved


def write_sources(resolved: dict[str, dict], venues: list[dict]) -> None:
    order = [v["venue_id"] for v in venues]
    lines = ["\t".join(SOURCE_COLUMNS)]
    for venue_id in order:
        record = resolved.get(venue_id)
        if not record:
            continue
        lines.append("\t".join([
            venue_id, record["provider"], str(record["key"]),
            ";".join(record.get("issns") or []),
            clean_title(str(record.get("name") or "")).replace("\t", " "),
            str(record.get("works") or 0), record["rule"],
        ]))
    SOURCES.write_text("\n".join(lines) + "\n", encoding="utf-8")


def read_sources() -> dict[str, dict]:
    if not SOURCES.exists():
        return {}
    with SOURCES.open(encoding="utf-8") as handle:
        return {row["venue_id"]: {"provider": row["provider"], "key": row["source_key"],
                                  "issns": [i for i in (row.get("issns") or "").split(";") if i],
                                  "name": row["source_name"],
                                  "works": int(row["works"] or 0), "rule": row["rule"]}
                for row in csv.DictReader(handle, delimiter="\t")}


# --------------------------------------------------------------------------- harvest


def crossref_titles(issns: list[str], want: int) -> list[str]:
    """Titles for a journal, trying each ISSN the record carries.

    A serial has a print ISSN and an electronic one, and `/journals/{issn}/works` only
    answers for the one the publisher deposited under. *Nature Plants* resolves on its
    print ISSN 2055-026X — whose journal record reports 2,968 DOIs — and whose `/works`
    endpoint returns **zero**; the same journal under 2055-0278 returns all of them.
    Reading only the first ISSN silently gave a venue an empty vocabulary while every
    surrounding number said the resolution had worked.
    """
    for issn in issns or []:
        titles = _crossref_titles_for(issn, want)
        if titles:
            return titles
    return []


def _crossref_titles_for(issn: str, want: int) -> list[str]:
    titles: list[str] = []
    cursor = "*"
    while len(titles) < want and cursor:
        url = (f"https://api.crossref.org/journals/{urllib.parse.quote(issn)}/works"
               f"?rows=200&select=title&cursor={urllib.parse.quote(cursor)}"
               f"&filter=type:journal-article,from-pub-date:{FROM_YEAR}-01-01")
        if _mailto():
            url += f"&mailto={urllib.parse.quote(_mailto())}"
        try:
            payload = fetch(url)
        except Declined:
            break
        message = payload.get("message", {})
        items = message.get("items") or []
        if not items:
            break
        for item in items:
            for raw in item.get("title") or []:
                cleaned = clean_title(raw)
                if cleaned:
                    titles.append(cleaned)
        cursor = message.get("next-cursor")
    return titles[:want]


# DBLP's publication API caps a page at 100 hits and answers a larger `h` with a 503 or
# a closed connection — it does not clamp. Asking for 1000 therefore returned nothing at
# all, so every conference resolved through DBLP got an empty vocabulary while the
# resolution map showed it correctly mapped. Results come back newest-first, so four
# pages of 100 are the four hundred most recent papers, which is what is wanted.
DBLP_PAGE = 100


def dblp_titles(stream: str, want: int) -> list[str]:
    titles: list[str] = []
    offset = 0
    while len(titles) < want:
        # `safe=""` matters: `quote` leaves "/" alone by default, and DBLP answers
        # `q=stream:conf/aies:` with a closed connection rather than an error. Left
        # unencoded, every conference in the corpus harvested zero titles while its
        # resolution row said it was correctly mapped — the failure looked like a venue
        # DBLP had never heard of.
        query = urllib.parse.quote(f"stream:{stream}:", safe="")
        url = (f"https://dblp.org/search/publ/api?q={query}"
               f"&h={DBLP_PAGE}&f={offset}&format=json")
        try:
            payload = fetch(url, pause=1.0)
        except Declined:
            break
        hits = payload.get("result", {}).get("hits", {})
        rows = hits.get("hit") or []
        if not rows:
            break
        for hit in rows:
            info = hit.get("info", {})
            if info.get("type") not in (None, "Conference and Workshop Papers"):
                continue
            try:
                if int(info.get("year") or 0) < FROM_YEAR:
                    continue
            except ValueError:
                continue
            cleaned = clean_title(info.get("title") or "").rstrip(".")
            if cleaned:
                titles.append(cleaned)
        offset += len(rows)
        if offset >= int(hits.get("@total") or 0):
            break
    return titles[:want]


def openalex_titles(source_id: str, want: int) -> list[str]:
    titles: list[str] = []
    cursor = "*"
    while len(titles) < want and cursor:
        url = (f"https://api.openalex.org/works?filter=primary_location.source.id:"
               f"{source_id},from_publication_date:{FROM_YEAR}-01-01,type:article"
               f"&per_page=200&select=title&cursor={urllib.parse.quote(cursor)}")
        if _mailto():
            url += f"&mailto={urllib.parse.quote(_mailto())}"
        try:
            payload = fetch(url)
        except Declined:
            break
        rows = payload.get("results") or []
        if not rows:
            break
        for row in rows:
            cleaned = clean_title(row.get("title") or "")
            if cleaned:
                titles.append(cleaned)
        cursor = payload.get("meta", {}).get("next_cursor")
    return titles[:want]


def harvest_titles(record: dict, want: int = HARVEST_TITLES) -> list[str]:
    if record["provider"] == "crossref":
        return crossref_titles(record.get("issns") or [record["key"]], want)
    if record["provider"] == "dblp":
        return dblp_titles(record["key"], want)
    if record["provider"] == "openalex":
        return openalex_titles(record["key"], want)
    return []


# --------------------------------------------------------------------------- vocabulary


def title_terms(title: str) -> list[str]:
    words = tokenize(title)
    return words + [f"{a} {b}" for a, b in zip(words, words[1:])]


def derive_topics(corpus: dict[str, list[str]], depth: int) -> dict[str, list[str]]:
    """TF-IDF over the harvested titles, one document per venue.

    Deliberately the same shape as ``venue_lib.derive_keywords`` so the two vocabularies
    weigh comparably once merged: a rare unigram that occurs twice is a subject term, a
    term half the corpus uses is not, and only the *rank* survives into the postings.
    """
    frequencies = {vid: Counter(t for title in titles for t in title_terms(title))
                   for vid, titles in corpus.items()}
    document_frequency: Counter = Counter()
    for counts in frequencies.values():
        document_frequency.update(counts.keys())
    n_docs = max(len(frequencies), 1)
    out: dict[str, list[str]] = {}
    for venue_id, counts in frequencies.items():
        total = sum(counts.values()) or 1
        scored = []
        for term, count in counts.items():
            if count < 2 and " " not in term:
                continue
            frequency = document_frequency[term]
            if frequency > n_docs * DF_CEILING:
                continue
            idf = math.log(n_docs / (1 + frequency))
            if idf <= 0:
                continue
            scored.append(((count / total) * idf, term))
        scored.sort(key=lambda pair: (-pair[0], pair[1]))
        out[venue_id] = [term for _, term in scored[:depth]]
    return out


def render_postings(topics: dict[str, list[str]], venues: list[dict],
                    dropped: int, harvested: int,
                    built_from: dict[str, str] | None = None) -> str:
    row_of = {venue["venue_id"]: row for row, venue in enumerate(venues)}
    postings: dict[str, list[str]] = {}
    for venue_id, terms in topics.items():
        row = row_of.get(venue_id)
        if row is None:
            continue
        for rank, term in enumerate(terms):
            postings.setdefault(term, []).append(f"{row}:{rank}")
    lines = [
        f"#venues\t{len(venues)}",
        f"#digest\t{index_digest([v['venue_id'] for v in venues])}",
        f"#depth\t{TOPIC_DEPTH}",
        f"#covered\t{len(topics)}",
        f"#titles\t{harvested}",
        f"#gold-titles-dropped\t{dropped}",
    ]
    # Which source each venue's vocabulary was built from. One line per covered venue,
    # so the file says whose articles it is holding — and so a later pass can tell a
    # vocabulary that is merely un-refreshed from one that belongs to a venue whose
    # resolution has since changed. The second is not safe to keep.
    for venue_id in sorted(built_from or {}):
        if venue_id in topics:
            lines.append(f"#built\t{venue_id}\t{built_from[venue_id]}")
    lines.append("#term\trow:rank,...")
    lines += [f"{term}\t{','.join(refs)}" for term, refs in sorted(postings.items())]
    return "\n".join(lines) + "\n"


def read_built_from(path: Path = POSTINGS) -> dict[str, str]:
    """venue_id -> the source key its committed vocabulary was built from."""
    out: dict[str, str] = {}
    if not path.exists():
        return out
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.startswith("#"):
                break
            parts = line[1:].rstrip("\n").split("\t")
            if parts[0] == "built" and len(parts) == 3:
                out[parts[1]] = parts[2]
    return out


def read_postings(venues: list[dict], path: Path = POSTINGS) -> dict[str, list[str]]:
    """venue_id -> its committed ranked vocabulary, or {} if there is no file.

    Read back so that a pass can *retain* what it could not re-fetch. `--harvest`
    rewrites the whole file, and the sources it reads are flaky enough that a venue which
    answered last time may not answer this time — DBLP refuses under load and a killed
    run can leave a half-written cache entry behind. Without this, coverage walks
    sideways: one pass adds eight venues and drops nine others, and the committed
    artefact is whichever run happened to be last.
    """
    if not path.exists():
        return {}
    order = [venue["venue_id"] for venue in venues]
    ranked: dict[str, dict[int, str]] = {}
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.startswith("#") or not line.strip():
                continue
            term, _, refs = line.rstrip("\n").partition("\t")
            for ref in refs.split(","):
                row, _, rank = ref.partition(":")
                row = int(row)
                if row < len(order):
                    ranked.setdefault(order[row], {})[int(rank)] = term
    return {venue_id: [terms[rank] for rank in sorted(terms)]
            for venue_id, terms in ranked.items()}


def postings_header(path: Path = POSTINGS) -> dict[str, str]:
    header: dict[str, str] = {}
    if not path.exists():
        return header
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.startswith("#"):
                break
            key, _, value = line[1:].rstrip("\n").partition("\t")
            header[key] = value
    return header


# --------------------------------------------------------------------------- commands


def command_check(venues: list[dict]) -> int:
    if not POSTINGS.exists():
        print(f"{POSTINGS.name} is missing — rebuild with --resolve --harvest",
              file=sys.stderr)
        return 1
    header = postings_header()
    problems = []
    if header.get("venues") != str(len(venues)):
        problems.append(f"describes {header.get('venues')} venues, index holds {len(venues)}")
    digest = index_digest([v["venue_id"] for v in venues])
    if header.get("digest") != digest:
        problems.append(f"built against venue ordering {header.get('digest')}, index is {digest}")
    if problems:
        for problem in problems:
            print(f"{POSTINGS.name}: {problem}", file=sys.stderr)
        print("regenerate with: python3 tools/fetch_venue_topics.py --resolve --harvest",
              file=sys.stderr)
        return 1
    print(f"OK: {POSTINGS.name} matches the current venue index "
          f"({header.get('covered', '?')}/{len(venues)} venues have a subject vocabulary)")
    return 0


def command_report(venues: list[dict]) -> int:
    resolved = read_sources()
    header = postings_header()
    by_type: Counter = Counter()
    resolved_by_type: Counter = Counter()
    by_provider: Counter = Counter()
    refused = []
    for venue in venues:
        key = f"{venue['venue_type']}/{venue['region']}"
        by_type[key] += 1
        record = resolved.get(venue["venue_id"])
        if not record:
            continue
        if record["provider"] == REFUSED:
            refused.append(venue["venue_id"])
            continue
        resolved_by_type[key] += 1
        by_provider[record["provider"]] += 1
    matched = sum(resolved_by_type.values())
    print(f"Venue subject vocabulary — {matched}/{len(venues)} venues resolved, "
          f"{len(refused)} candidates found and refused")
    for key in sorted(by_type):
        total = by_type[key]
        got = resolved_by_type[key]
        print(f"  {key:24s} {got:4d}/{total:<4d} {got / total * 100:5.1f}%")
    print("  by provider: " + ", ".join(f"{k}={v}" for k, v in sorted(by_provider.items())))
    if header:
        print(f"  postings: depth {header.get('depth')}, "
              f"{header.get('covered', '?')} venues, {header.get('titles', '?')} titles read, "
              f"{header.get('gold-titles-dropped', '?')} gold titles dropped by the leak guard")
    if refused:
        print(f"  refused ({len(refused)}), first 10: {', '.join(refused[:10])} "
              "— see the `rule` column for why")
    unresolved = [v["venue_id"] for v in venues
                  if v["venue_id"] not in resolved
                  or resolved[v["venue_id"]]["provider"] == REFUSED]
    unmatched = [v for v in unresolved if v not in refused]
    if unmatched:
        print(f"  nothing offered ({len(unmatched)}), first 20: "
              f"{', '.join(unmatched[:20])}")
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--resolve", action="store_true",
                        help="network: map venues to bibliographic sources")
    parser.add_argument("--harvest", action="store_true",
                        help="network: read published titles and rebuild the postings")
    parser.add_argument("--check", action="store_true",
                        help="offline: the postings still describe the current index")
    parser.add_argument("--source", choices=("free", "openalex"), default="free",
                        help="'openalex' adds the paid fallback for what Crossref and "
                             "DBLP cannot resolve (it bills per request)")
    parser.add_argument("--refresh", action="store_true",
                        help="re-resolve venues that already have a source row")
    parser.add_argument("--limit", type=int, default=None,
                        help="stop after N venues (for a quick sample)")
    parser.add_argument("--jobs", type=int, default=8,
                        help="concurrent lookups (default 8; both APIs are free and "
                             "latency-bound, but DBLP answers a burst with 503)")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    venues = load_index()

    if args.check:
        return command_check(venues)

    if args.resolve:
        existing = {} if args.refresh else read_sources()
        print(f"Resolving {len(venues)} venues "
              f"({len(existing)} already mapped){' + OpenAlex' if args.source == 'openalex' else ''}")
        resolved = resolve_all(venues, use_openalex=(args.source == "openalex"),
                               limit=args.limit, existing=existing, jobs=args.jobs)
        write_sources(resolved, venues)
        print(f"Wrote {SOURCES.relative_to(ROOT)} — {len(resolved)}/{len(venues)} resolved")

    if args.harvest:
        resolved = read_sources()
        if not resolved:
            print("no venue-sources.tsv — run --resolve first", file=sys.stderr)
            return 1
        drop = gold_titles()
        corpus: dict[str, list[str]] = {}
        dropped = 0
        harvested = 0
        order = [v["venue_id"] for v in venues if v["venue_id"] in resolved
                 and resolved[v["venue_id"]]["provider"] in HARVESTABLE]
        if args.limit:
            order = order[:args.limit]
        # Same shape as the resolution pass: independent, latency-bound, small pool.
        with ThreadPoolExecutor(max_workers=args.jobs) as pool:
            futures = {pool.submit(harvest_titles, resolved[v]): v for v in order}
            for position, (future, venue_id) in enumerate(futures.items(), 1):
                try:
                    titles = future.result()
                except Exception as error:               # noqa: BLE001 - reported below
                    print(f"  {venue_id}: {error}", file=sys.stderr, flush=True)
                    titles = []
                harvested += len(titles)
                kept = [title for title in titles if norm_title(title) not in drop]
                dropped += len(titles) - len(kept)
                if kept:
                    corpus[venue_id] = kept
                print(f"  [{position}/{len(order)}] {venue_id}: {len(kept)} titles "
                      f"({len(titles) - len(kept)} dropped as gold)", flush=True)
        topics = derive_topics(corpus, TOPIC_DEPTH)
        # Retain, do not lose — but only what still belongs to this venue. A venue that
        # came back empty keeps the vocabulary it had, *provided* it is still resolved to
        # the same source; if the resolution changed, the old vocabulary is some other
        # venue's articles and dropping it is the whole point. `FAST` is the case that
        # made this concrete: it was resolved to *Formal Aspects in Security and Trust*
        # until the acronym rule learned to check, and silently keeping that would have
        # undone the fix. Delete the file to rebuild from nothing.
        built_from = {vid: str(resolved[vid]["key"]) for vid in order}
        previous_source = read_built_from()
        previous = read_postings(venues)
        retained = 0
        stale = 0
        for venue_id in order:
            if topics.get(venue_id) or not previous.get(venue_id):
                continue
            if previous_source.get(venue_id) not in (None, built_from[venue_id]):
                stale += 1
                continue
            topics[venue_id] = previous[venue_id][:TOPIC_DEPTH]
            retained += 1
        POSTINGS.write_text(
            render_postings(topics, venues, dropped, harvested, built_from),
            encoding="utf-8")
        # A venue that resolved but harvested nothing is the failure mode this tool is
        # least able to see from inside: the resolution row says it is correctly mapped,
        # the postings file is written, and only the empty vocabulary is wrong. Both
        # harvest bugs found so far — a page size DBLP answers with a closed connection,
        # and a print ISSN whose `/works` endpoint returns zero — presented exactly this
        # way, so the count is printed rather than left to be noticed.
        empty = [venue_id for venue_id in order
                 if venue_id not in corpus and venue_id not in topics]
        print(f"Wrote {POSTINGS.relative_to(ROOT)} — {len(topics)} venues, "
              f"{harvested} titles read, {dropped} dropped by the leak guard"
              + (f", {retained} kept from the previous build" if retained else "")
              + (f", {stale} dropped because their source changed" if stale else ""))
        if empty:
            print(f"WARNING: {len(empty)} resolved venues have no vocabulary at all "
                  f"— first 10: {', '.join(empty[:10])}. Re-run to try them again.",
                  file=sys.stderr)

    if not (args.resolve or args.harvest):
        return command_report(venues)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
