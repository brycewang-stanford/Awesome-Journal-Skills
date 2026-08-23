#!/usr/bin/env python3
"""Resolve gold-set papers to a bibliographic API and store a **term bag** per abstract.

Why this exists: the headline eval queries a paper *title*, because that is the only
text the gold set carries. No author picks a journal from a title — they paste an
abstract. Without abstracts the eval measured the hardest possible version of the task
and reported it as the capability.

Why a term bag and not the abstract: the abstracts are the publishers', not ours. What
retrieval actually consumes is the deduplicated set of content words, which is what gets
committed — sorted, stopword-filtered, no word order, not readable as prose. It is
enough to score the matcher and not a redistribution of the text.

Four sources, because the free ones are each partial
----------------------------------------------------
No single free API covers this gold set. Each of the three defaults is strong where
the others are weak, and asking them in order costs one extra request only for the
papers the cheaper source could not answer:

* ``crossref``  — everything with a DOI, but only where the publisher deposited an
  abstract, which many do not. Broad and shallow.
* ``europepmc`` — near-complete for medicine and the life sciences, irrelevant
  elsewhere. Narrow and deep.
* ``arxiv``     — preprints, so it reaches computer science, physics and quantitative
  economics that never deposit an abstract with Crossref. Note the abstract is the
  *preprint's*; for retrieval terms that is a difference without much distinction, but
  it is a difference, and the ``source`` column records it.

``openalex`` has the best coverage of the four and now bills per request. An exhausted
budget answers ``429`` with ``{"error": "Rate limit exceeded", ... "retryAfter": N}``
and a dollar figure, which is a different thing from a rate limit and is reported as
such. It is opt-in (``--source openalex`` / ``--source all``) because spending money
is the maintainer's decision, not this script's.

Coverage is therefore uneven by discipline, and that unevenness is a property of the
resulting `title+abstract` row — see the Limitations section of ``eval/README.md``.

Declined is not absent
----------------------
The one invariant worth stating twice: a source that *declines* to answer — 401, 402,
403, 429, 5xx, a timeout — has said nothing about whether the paper has an abstract.
Recording that as a miss is how a throttled run quietly produces a small, biased corpus
that looks like a complete one. Only a source that answers, and answers "no", makes a
miss. An earlier version of this script folded 403 into "no such paper" and cached 50
false misses in a single run; the ``Answer`` type below exists so that cannot recur.

Network is required, so this is **not** part of ``tools/run_checks.py``. Its output is
committed; CI reads the file and never fetches. Rerun it when the gold set grows:

    python3 tools/fetch_abstracts.py                    # fill gaps from the free sources
    python3 tools/fetch_abstracts.py --source all       # add OpenAlex (costs money)
    python3 tools/fetch_abstracts.py --source arxiv     # one source only
    python3 tools/fetch_abstracts.py --refresh          # re-resolve everything
    python3 tools/fetch_abstracts.py --limit 50         # a quick sample
    python3 tools/fetch_abstracts.py --retry-misses     # re-ask about cached misses

Set ``OPENALEX_MAILTO`` to your address for OpenAlex's polite pool. The address is not
hard-coded here — it goes to a third party, so publishing it is the maintainer's
decision. ``CROSSREF_MAILTO`` does the same for Crossref's polite pool.

Output: ``shared-resources/journal-selection/eval/abstract-terms.tsv``
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field

from venue_lib import ROOT, tokenize

GOLD = ROOT / "shared-resources/journal-selection/eval/gold-set.tsv"
OUT = ROOT / "shared-resources/journal-selection/eval/abstract-terms.tsv"
# Papers a source answered "no" about. Cached, not committed: it is a fact about the
# lookup rather than about the repository, and re-asking costs quota that a budgeted
# run does not have. Only genuine answers land here — see `Answer` below.
MISSES = ROOT / "tools/.cache/abstract-misses.tsv"

COLUMNS = ["paper_title", "source", "work_id", "term_count", "abstract_terms"]

TIMEOUT = 25
# A fuzzy title search will happily return a different paper. Require most of the
# query's words to be present in what comes back before believing the match.
MIN_TITLE_OVERLAP = 0.7
# Bound the *abstract*, not the term list. Truncating a sorted term list keeps the words
# beginning with a-c and throws away the rest of the alphabet, which is not a sample of
# anything. Bounding the text first keeps a contiguous, order-faithful opening.
MAX_ABSTRACT_CHARS = 4000
# Below this many content words it is a teaser line, not an abstract.
MIN_TERMS = 8
# Retries are for a hiccup, not for a budget. A source that declines twice in a row is
# treated as unavailable for the rest of the run rather than hammered: when the reason
# is an exhausted daily budget, every further request is both futile and billable.
RETRIES = 2
BACKOFF = 10.0
# A `retryAfter` longer than this means "come back tomorrow", so the run stops and
# checkpoints instead of sleeping through it.
MAX_WAIT = 120.0

USER_AGENT = ("awesome-journal-skills abstract-term harvester "
              "(+https://github.com/brycewang-stanford/Awesome-Journal-Skills)")


# --- the answer type --------------------------------------------------------------

@dataclass
class Answer:
    """What a source said. `kind` is the distinction the whole script turns on.

    * ``found``    — here is the abstract.
    * ``absent``   — I looked; this paper has no abstract I can give you. A real miss.
    * ``declined`` — I did not look. Says nothing about the paper. Never a miss.
    """

    kind: str
    work_id: str = ""
    terms: str = ""
    retry_after: float = 0.0
    detail: str = ""


FOUND, ABSENT, DECLINED = "found", "absent", "declined"


# --- shared helpers ---------------------------------------------------------------

def normalize(title: str) -> set[str]:
    return {w for w in re.findall(r"[a-z0-9]+", title.lower()) if len(w) > 2}


def title_matches(query: str, found: str) -> bool:
    a, b = normalize(query), normalize(found or "")
    if not a or not b:
        return False
    return len(a & b) / len(a) >= MIN_TITLE_OVERLAP


def terms_of(abstract: str) -> str:
    """Deduplicated, sorted content words — a retrieval input, not the publisher's prose."""
    return " ".join(sorted(set(tokenize(abstract[:MAX_ABSTRACT_CHARS]))))


def _retry_after(error: urllib.error.HTTPError, body: bytes) -> float:
    """Seconds the server asked us to wait, from the header or the JSON body."""
    header = error.headers.get("Retry-After") if error.headers else None
    if header:
        try:
            return float(header)
        except ValueError:
            pass
    try:
        payload = json.loads(body.decode("utf-8", "replace"))
    except (ValueError, UnicodeDecodeError):
        return 0.0
    value = payload.get("retryAfter")
    return float(value) if isinstance(value, (int, float)) else 0.0


def _explain(body: bytes) -> str:
    """A one-line reason from an error body, for the operator rather than the parser."""
    try:
        payload = json.loads(body.decode("utf-8", "replace"))
    except (ValueError, UnicodeDecodeError):
        return body[:120].decode("utf-8", "replace").strip()
    for key in ("message", "error", "detail"):
        if payload.get(key):
            return str(payload[key])[:200]
    return ""


def get_json(url: str, headers: dict) -> tuple[dict | None, Answer | None]:
    """(payload, None) on success, or (None, declined-or-absent Answer) on failure."""
    request = urllib.request.Request(url, headers=headers)
    for attempt in range(RETRIES):
        try:
            with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
                return json.load(response), None
        except urllib.error.HTTPError as error:
            body = error.read()
            error.close()
            if error.code == 404:
                return None, Answer(ABSENT)
            wait = _retry_after(error, body)
            detail = f"HTTP {error.code}"
            reason = _explain(body)
            if reason:
                detail = f"{detail}: {reason}"
            # 401/402/403 are "not for you", 429 is "not now", 5xx is "not working".
            # None of them is "this paper has no abstract", so none of them is a miss.
            if error.code in (429, 500, 502, 503, 504) and attempt + 1 < RETRIES \
                    and wait <= MAX_WAIT:
                time.sleep(max(wait, BACKOFF))
                continue
            return None, Answer(DECLINED, retry_after=wait, detail=detail)
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError) as error:
            if attempt + 1 < RETRIES:
                time.sleep(BACKOFF)
                continue
            return None, Answer(DECLINED, detail=f"{type(error).__name__}: {error}")
    return None, Answer(DECLINED, detail="retries exhausted")


def get_text(url: str, headers: dict) -> tuple[str | None, Answer | None]:
    """Same contract as `get_json`, for the one source that answers in XML."""
    request = urllib.request.Request(url, headers=headers)
    for attempt in range(RETRIES):
        try:
            with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
                return response.read().decode("utf-8", "replace"), None
        except urllib.error.HTTPError as error:
            body = error.read()
            error.close()
            if error.code == 404:
                return None, Answer(ABSENT)
            wait = _retry_after(error, body)
            if error.code in (429, 500, 502, 503, 504) and attempt + 1 < RETRIES \
                    and wait <= MAX_WAIT:
                time.sleep(max(wait, BACKOFF))
                continue
            return None, Answer(DECLINED, retry_after=wait, detail=f"HTTP {error.code}")
        except (urllib.error.URLError, TimeoutError, ET.ParseError, OSError) as error:
            if attempt + 1 < RETRIES:
                time.sleep(BACKOFF)
                continue
            return None, Answer(DECLINED, detail=f"{type(error).__name__}: {error}")
    return None, Answer(DECLINED, detail="retries exhausted")


# --- Crossref ---------------------------------------------------------------------

CROSSREF_API = "https://api.crossref.org/works"
CROSSREF_MAILTO = os.environ.get("CROSSREF_MAILTO", "")
_JATS_TAG = re.compile(r"<[^>]+>")


def clean_jats(abstract: str) -> str:
    """Crossref returns JATS XML. Strip the markup and the redundant 'Abstract' label."""
    text = _JATS_TAG.sub(" ", abstract)
    text = html.unescape(text)
    text = re.sub(r"^\s*abstract\b[:.]?", " ", text, flags=re.I)
    return re.sub(r"\s+", " ", text).strip()


def crossref(title: str) -> Answer:
    params = {
        "query.bibliographic": title[:250],
        "rows": "1",
        "select": "title,abstract,DOI",
    }
    if CROSSREF_MAILTO:
        params["mailto"] = CROSSREF_MAILTO
    payload, failure = get_json(f"{CROSSREF_API}?{urllib.parse.urlencode(params)}",
                                {"User-Agent": USER_AGENT})
    if failure:
        return failure
    items = (payload.get("message") or {}).get("items") or []
    if not items:
        return Answer(ABSENT, detail="no result")
    item = items[0]
    found_title = (item.get("title") or [""])[0]
    if not title_matches(title, found_title):
        return Answer(ABSENT, detail="title mismatch")
    abstract = clean_jats(item.get("abstract") or "")
    terms = terms_of(abstract)
    if len(terms.split()) < MIN_TERMS:
        return Answer(ABSENT, detail="no abstract deposited")
    return Answer(FOUND, work_id=item.get("DOI", ""), terms=terms)


# --- OpenAlex ---------------------------------------------------------------------

OPENALEX_API = "https://api.openalex.org/works"
OPENALEX_MAILTO = os.environ.get("OPENALEX_MAILTO", "")


def reconstruct(inverted: dict) -> str:
    """OpenAlex ships abstracts as {word: [positions]}; put the words back in order."""
    if not inverted:
        return ""
    slots: list[tuple[int, str]] = []
    for word, positions in inverted.items():
        slots.extend((p, word) for p in positions)
    slots.sort()
    return " ".join(word for _, word in slots)


def openalex(title: str) -> Answer:
    params = {
        "filter": f"title.search:{title[:250]}",
        "per_page": "1",
        "select": "id,title,abstract_inverted_index",
    }
    if OPENALEX_MAILTO:
        params["mailto"] = OPENALEX_MAILTO
    payload, failure = get_json(f"{OPENALEX_API}?{urllib.parse.urlencode(params)}",
                                {"User-Agent": USER_AGENT})
    if failure:
        return failure
    results = payload.get("results") or []
    if not results:
        return Answer(ABSENT, detail="no result")
    work = results[0]
    if not title_matches(title, work.get("title") or ""):
        return Answer(ABSENT, detail="title mismatch")
    terms = terms_of(reconstruct(work.get("abstract_inverted_index") or {}))
    if len(terms.split()) < MIN_TERMS:
        return Answer(ABSENT, detail="no abstract")
    return Answer(FOUND, work_id=work.get("id", "").rsplit("/", 1)[-1], terms=terms)


# --- Europe PMC -------------------------------------------------------------------

EUROPEPMC_API = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"


def europepmc(title: str) -> Answer:
    params = {
        "query": f'TITLE:"{title[:200]}"',
        "format": "json",
        "pageSize": "1",
        "resultType": "core",
    }
    payload, failure = get_json(f"{EUROPEPMC_API}?{urllib.parse.urlencode(params)}",
                                {"User-Agent": USER_AGENT})
    if failure:
        return failure
    items = (payload.get("resultList") or {}).get("result") or []
    if not items:
        return Answer(ABSENT, detail="no result")
    item = items[0]
    if not title_matches(title, item.get("title") or ""):
        return Answer(ABSENT, detail="title mismatch")
    terms = terms_of(item.get("abstractText") or "")
    if len(terms.split()) < MIN_TERMS:
        return Answer(ABSENT, detail="no abstract")
    return Answer(FOUND, work_id=item.get("id", ""), terms=terms)


# --- arXiv ------------------------------------------------------------------------

ARXIV_API = "http://export.arxiv.org/api/query"
ATOM = "{http://www.w3.org/2005/Atom}"


def arxiv(title: str) -> Answer:
    # A title-field query rather than a free-text one: arXiv's default `all:` search
    # matches abstract words too and happily returns a paper that merely cites this one.
    params = {"search_query": f'ti:"{title[:200]}"', "max_results": "1"}
    body, failure = get_text(f"{ARXIV_API}?{urllib.parse.urlencode(params)}",
                             {"User-Agent": USER_AGENT})
    if failure:
        return failure
    try:
        feed = ET.fromstring(body)
    except ET.ParseError:
        return Answer(DECLINED, detail="unparseable Atom feed")
    entry = feed.find(f"{ATOM}entry")
    if entry is None:
        return Answer(ABSENT, detail="no result")
    found_title = (entry.findtext(f"{ATOM}title") or "").strip()
    if not title_matches(title, found_title):
        return Answer(ABSENT, detail="title mismatch")
    terms = terms_of(entry.findtext(f"{ATOM}summary") or "")
    if len(terms.split()) < MIN_TERMS:
        return Answer(ABSENT, detail="no abstract")
    return Answer(FOUND, work_id=(entry.findtext(f"{ATOM}id") or "").rsplit("/", 1)[-1],
                  terms=terms)


@dataclass
class Source:
    name: str
    resolve: object
    pause: float
    available: bool = True
    reason: str = ""
    stats: dict = field(default_factory=lambda: {FOUND: 0, ABSENT: 0, DECLINED: 0})


# Asked in this order. Cheapest and broadest first, so the narrow sources are only
# consulted about the papers the broad one could not answer.
FREE_SOURCES = ("crossref", "europepmc", "arxiv")


def build_sources(selected: str, pause: float | None) -> list[Source]:
    catalogue = {
        # Crossref asks for one request at a time from a polite client; the polite pool
        # (a mailto) buys a higher allowance rather than a different etiquette.
        "crossref": Source("crossref", crossref, 0.4 if CROSSREF_MAILTO else 1.0),
        "europepmc": Source("europepmc", europepmc, 0.8),
        # arXiv's terms ask for one request every three seconds. It is the slowest
        # source and the last one asked, so only the residue pays that price.
        "arxiv": Source("arxiv", arxiv, 3.2),
        "openalex": Source("openalex", openalex, 0.4 if OPENALEX_MAILTO else 2.0),
    }
    if selected == "free":
        names = list(FREE_SOURCES)
    elif selected == "all":
        names = list(FREE_SOURCES) + ["openalex"]
    else:
        names = [selected]
    sources = [catalogue[n] for n in names]
    if pause is not None:
        for source in sources:
            source.pause = pause
    return sources


# --- storage ----------------------------------------------------------------------

def load_existing() -> dict[str, dict]:
    if not OUT.exists():
        return {}
    rows = {}
    with OUT.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            # Rows written before the file recorded a source came from OpenAlex, which
            # was the only source this script had.
            row.setdefault("source", "openalex")
            row.setdefault("work_id", row.get("openalex_id", ""))
            rows[row["paper_title"]] = {c: row.get(c, "") for c in COLUMNS}
    return rows


def render(rows: list[dict]) -> str:
    lines = ["\t".join(COLUMNS)]
    for row in sorted(rows, key=lambda r: r["paper_title"]):
        lines.append("\t".join(str(row[c]).replace("\t", " ") for c in COLUMNS))
    return "\n".join(lines) + "\n"


def load_misses() -> dict[str, str]:
    """title -> the source that answered 'no', so one source's no is not treated as all."""
    if not MISSES.exists():
        return {}
    out = {}
    with MISSES.open(encoding="utf-8") as handle:
        for line in handle:
            title, _, sources = line.rstrip("\n").partition("\t")
            if title:
                out[title] = sources
    return out


def save_misses(misses: dict[str, str]) -> None:
    MISSES.parent.mkdir(parents=True, exist_ok=True)
    MISSES.write_text(
        "".join(f"{title}\t{sources}\n" for title, sources in sorted(misses.items())),
        encoding="utf-8")


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


# --- driver -----------------------------------------------------------------------

def resolve(title: str, sources: list[Source]) -> tuple[Answer, set[str]]:
    """Ask each available source in turn. Returns the answer and who said 'no'."""
    said_no: set[str] = set()
    for source in sources:
        if not source.available:
            continue
        answer = source.resolve(title)
        source.stats[answer.kind] += 1
        time.sleep(source.pause)
        if answer.kind == FOUND:
            answer.detail = source.name
            return answer, said_no
        if answer.kind == ABSENT:
            said_no.add(source.name)
            continue
        # Declined. One source being unavailable must not end the run while another
        # can still answer, but asking it again 1,600 more times is pure waste.
        source.available = False
        source.reason = answer.detail
        wait = f", retry in {answer.retry_after / 3600:.1f}h" if answer.retry_after else ""
        print(f"  {source.name} unavailable: {answer.detail}{wait}", file=sys.stderr)
    if said_no:
        return Answer(ABSENT), said_no
    return Answer(DECLINED, detail="every source declined"), said_no


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--source",
                        choices=("free", "crossref", "europepmc", "arxiv",
                                 "openalex", "all"),
                        default="free",
                        help="which API(s) to ask, in order. `free` is Crossref then "
                             "Europe PMC then arXiv; `all` adds OpenAlex, which bills "
                             "per request and is therefore never a default")
    parser.add_argument("--refresh", action="store_true",
                        help="re-resolve papers already in the file")
    parser.add_argument("--retry-misses", action="store_true",
                        help="re-ask about titles cached as misses")
    parser.add_argument("--limit", type=int, help="stop after this many lookups")
    parser.add_argument("--pause", type=float, default=None,
                        help="seconds between lookups; overrides the per-source default")
    args = parser.parse_args(argv)

    sources = build_sources(args.source, args.pause)
    source_names = {s.name for s in sources}

    with GOLD.open(encoding="utf-8") as handle:
        gold = list(csv.DictReader(handle, delimiter="\t"))
    existing = {} if args.refresh else load_existing()
    misses = {} if (args.refresh or args.retry_misses) else load_misses()

    todo = []
    for row in gold:
        title = row["paper_title"]
        if title in existing:
            continue
        # A cached miss only rules out the sources that actually answered "no". Adding
        # a source to the run must re-open every paper the old source could not find.
        if set(filter(None, misses.get(title, "").split(","))) >= source_names:
            continue
        todo.append(row)
    if args.limit:
        todo = todo[:args.limit]

    print(f"{len(gold)} gold papers · {len(existing)} already resolved · "
          f"{len(misses)} cached misses · {len(todo)} to look up "
          f"· sources: {', '.join(s.name for s in sources)}")

    resolved = dict(existing)
    found = absent = 0

    def checkpoint() -> None:
        save(list(resolved.values()))
        save_misses(misses)

    for i, row in enumerate(todo, 1):
        title = row["paper_title"]
        answer, said_no = resolve(title, sources)
        if said_no:
            already = set(filter(None, misses.get(title, "").split(",")))
            misses[title] = ",".join(sorted(already | said_no))
        if answer.kind == FOUND:
            resolved[title] = {
                "paper_title": title,
                "source": answer.detail,
                "work_id": answer.work_id,
                "term_count": len(answer.terms.split()),
                "abstract_terms": answer.terms,
            }
            found += 1
        elif answer.kind == ABSENT:
            absent += 1
        else:
            checkpoint()
            print(f"\nSTOPPED at {i}/{len(todo)}: every source declined to answer.\n"
                  + "\n".join(f"  {s.name}: {s.reason}" for s in sources if s.reason)
                  + "\nWhat is written so far is kept; rerun later to continue where "
                    "this left off.", file=sys.stderr)
            return 2
        if i % 50 == 0 or i == len(todo):
            print(f"  {i}/{len(todo)}  resolved={found}  no-abstract={absent}", flush=True)
            checkpoint()

    checkpoint()
    coverage = len(resolved) / max(len(gold), 1)
    print(f"wrote {len(resolved)} abstract term bags -> {OUT.relative_to(ROOT)} "
          f"({coverage:.0%} of the gold set)")
    for source in sources:
        print(f"  {source.name}: {source.stats[FOUND]} found, "
              f"{source.stats[ABSENT]} no-abstract, {source.stats[DECLINED]} declined")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
