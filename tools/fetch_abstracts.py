#!/usr/bin/env python3
"""Resolve gold-set papers to OpenAlex and store a **term bag** for each abstract.

Why this exists: the headline eval queries a paper *title*, because that is the only
text the gold set carries. No author picks a journal from a title — they paste an
abstract. Without abstracts the eval measured the hardest possible version of the task
and reported it as the capability.

Why a term bag and not the abstract: the abstracts are the publishers', not ours. What
retrieval actually consumes is the deduplicated set of content words, which is what gets
committed — sorted, stopword-filtered, no word order, not readable as prose. It is
enough to score the matcher and not a redistribution of the text.

Network is required, so this is **not** part of `tools/run_checks.py`. Its output is
committed; CI reads the file and never fetches. Rerun it when the gold set grows:

    python3 tools/fetch_abstracts.py                # fill in what is missing
    python3 tools/fetch_abstracts.py --refresh      # re-resolve everything
    python3 tools/fetch_abstracts.py --limit 50     # a quick sample
    python3 tools/fetch_abstracts.py --pause 5      # back off further when throttled

Set ``OPENALEX_MAILTO`` to your address before a full run. OpenAlex's anonymous pool
throttled a full 1,738-paper run hard enough that it could not complete; the polite pool
is the documented remedy. The address is not hard-coded here — it goes to a third party,
so publishing it is the maintainer's decision, not this script's.

Output: ``shared-resources/journal-selection/eval/abstract-terms.tsv``
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

from venue_lib import ROOT, tokenize

GOLD = ROOT / "shared-resources/journal-selection/eval/gold-set.tsv"
OUT = ROOT / "shared-resources/journal-selection/eval/abstract-terms.tsv"
# Papers OpenAlex answered "no" about. Cached, not committed: it is a fact about the
# lookup rather than about the repository, and re-asking costs quota that a throttled
# run does not have. Only genuine answers land here — a rate-limit raises RateLimited
# and is never recorded, which is the whole reason that exception exists.
MISSES = ROOT / "tools/.cache/openalex-misses.txt"

COLUMNS = ["paper_title", "openalex_id", "term_count", "abstract_terms"]

API = "https://api.openalex.org/works"
# OpenAlex's polite pool wants a contact address. It is not hard-coded here: an email
# address in a public repository is the maintainer's to publish, not this script's.
# Set OPENALEX_MAILTO to join the polite pool and get a far higher rate allowance.
MAILTO = os.environ.get("OPENALEX_MAILTO", "")
DEFAULT_PAUSE = 0.4 if MAILTO else 2.0
TIMEOUT = 25
# 429s and 5xx are the API saying "later", not the answer "this paper has no abstract".
# Treating them as misses is how a rate-limited run quietly produces a small, biased
# corpus that looks like a complete one.
#
# The anonymous pool's throttle is not a simple requests-per-second limit — observed
# behaviour from one address was ~20 requests through, then 429 for minutes, and 429 on
# 2 of 12 requests even at four seconds apart. Retries are therefore few but long, and
# the run gives up and checkpoints rather than hammering. **Set `OPENALEX_MAILTO` to
# your address**: the polite pool is the documented remedy and is much less restrictive.
RETRIES = 5
BACKOFF = 15.0
# A fuzzy title search will happily return a different paper. Require most of the
# query's words to be present in what comes back before believing the match.
MIN_TITLE_OVERLAP = 0.7
# Bound the *abstract*, not the term list. Truncating a sorted term list keeps the words
# beginning with a-c and throws away the rest of the alphabet, which is not a sample of
# anything. Bounding the text first keeps a contiguous, order-faithful opening.
MAX_ABSTRACT_CHARS = 4000


def normalize(title: str) -> set[str]:
    return {w for w in re.findall(r"[a-z0-9]+", title.lower()) if len(w) > 2}


def title_matches(query: str, found: str) -> bool:
    a, b = normalize(query), normalize(found or "")
    if not a or not b:
        return False
    return len(a & b) / len(a) >= MIN_TITLE_OVERLAP


def reconstruct(inverted: dict) -> str:
    """OpenAlex ships abstracts as {word: [positions]}; put the words back in order."""
    if not inverted:
        return ""
    slots: list[tuple[int, str]] = []
    for word, positions in inverted.items():
        slots.extend((p, word) for p in positions)
    slots.sort()
    return " ".join(word for _, word in slots)


class RateLimited(RuntimeError):
    """The API declined to answer. Not the same as answering 'no such paper'."""


def request_works(title: str) -> dict:
    params = {
        "filter": f"title.search:{title[:250]}",
        "per_page": "1",
        "select": "id,title,abstract_inverted_index",
    }
    if MAILTO:
        params["mailto"] = MAILTO
    request = urllib.request.Request(
        f"{API}?{urllib.parse.urlencode(params)}",
        headers={"User-Agent": "awesome-journal-skills abstract-term harvester"})

    for attempt in range(RETRIES):
        try:
            with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
                return json.load(response)
        except urllib.error.HTTPError as error:
            if error.code in (429, 500, 502, 503, 504):
                time.sleep(BACKOFF * (2 ** attempt))
                continue
            return {}                       # 4xx other than 429: a real "no"
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError):
            time.sleep(BACKOFF * (2 ** attempt))
    raise RateLimited(title)


def fetch(title: str) -> tuple[str, str] | None:
    payload = request_works(title)
    results = payload.get("results") or []
    if not results:
        return None
    work = results[0]
    if not title_matches(title, work.get("title") or ""):
        return None
    abstract = reconstruct(work.get("abstract_inverted_index") or {})
    if not abstract:
        return None
    # Deduplicated, sorted content words — a retrieval input, not the publisher's prose.
    terms = sorted(set(tokenize(abstract[:MAX_ABSTRACT_CHARS])))
    if len(terms) < 8:
        return None
    return work.get("id", "").rsplit("/", 1)[-1], " ".join(terms)


def load_existing() -> dict[str, dict]:
    if not OUT.exists():
        return {}
    with OUT.open(encoding="utf-8") as handle:
        return {row["paper_title"]: row for row in csv.DictReader(handle, delimiter="\t")}


def render(rows: list[dict]) -> str:
    lines = ["\t".join(COLUMNS)]
    for row in sorted(rows, key=lambda r: r["paper_title"]):
        lines.append("\t".join(str(row[c]).replace("\t", " ") for c in COLUMNS))
    return "\n".join(lines) + "\n"


def load_misses() -> set[str]:
    if not MISSES.exists():
        return set()
    return {line for line in MISSES.read_text(encoding="utf-8").split("\n") if line}


def save_misses(titles: set[str]) -> None:
    MISSES.parent.mkdir(parents=True, exist_ok=True)
    MISSES.write_text("\n".join(sorted(titles)) + "\n", encoding="utf-8")


def save(rows: list[dict]) -> None:
    """Write the term bags — or leave no file at all when there are none.

    A header-only TSV is worse than a missing one: it is a committable artefact that
    says "this data exists" while carrying nothing, and the eval would report a
    configuration covering zero papers instead of saying the data has not been built.
    """
    if not rows:
        return
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(render(rows), encoding="utf-8")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--refresh", action="store_true",
                        help="re-resolve papers already in the file")
    parser.add_argument("--limit", type=int, help="stop after this many lookups")
    parser.add_argument("--pause", type=float, default=DEFAULT_PAUSE,
                        help="seconds between lookups; raise it if the API throttles "
                             f"(default {DEFAULT_PAUSE})")
    args = parser.parse_args(argv)

    with GOLD.open(encoding="utf-8") as handle:
        gold = list(csv.DictReader(handle, delimiter="\t"))
    existing = {} if args.refresh else load_existing()

    misses = load_misses() if not args.refresh else set()
    todo = [row for row in gold
            if row["paper_title"] not in existing and row["paper_title"] not in misses]
    if args.limit:
        todo = todo[:args.limit]
    print(f"{len(gold)} gold papers · {len(existing)} already resolved · "
          f"{len(misses)} known misses · {len(todo)} to look up")

    resolved = dict(existing)
    found = failed = 0
    for i, row in enumerate(todo, 1):
        title = row["paper_title"]
        try:
            hit = fetch(title)
        except RateLimited:
            save(list(resolved.values()))
            save_misses(misses)
            print(f"\nSTOPPED at {i}/{len(todo)}: the API is rate-limiting and retries "
                  "were exhausted.\nWhat is written so far is kept; rerun later to "
                  "continue where this left off.\nSet OPENALEX_MAILTO=<your address> "
                  "for the polite pool's higher allowance.", file=sys.stderr)
            return 2
        if hit:
            openalex_id, terms = hit
            resolved[title] = {
                "paper_title": title,
                "openalex_id": openalex_id,
                "term_count": len(terms.split()),
                "abstract_terms": terms,
            }
            found += 1
        else:
            misses.add(title)
            failed += 1
        if i % 50 == 0 or i == len(todo):
            print(f"  {i}/{len(todo)}  resolved={found}  unresolved={failed}",
                  flush=True)
            save(list(resolved.values()))
            save_misses(misses)
        time.sleep(args.pause)

    save(list(resolved.values()))
    save_misses(misses)
    coverage = len(resolved) / max(len(gold), 1)
    print(f"wrote {len(resolved)} abstract term bags -> {OUT.relative_to(ROOT)} "
          f"({coverage:.0%} of the gold set)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
