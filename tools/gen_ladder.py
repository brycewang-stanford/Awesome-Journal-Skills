#!/usr/bin/env python3
"""Generate ``ladder.tsv`` — the venue-adjacency graph behind the resubmission ladder.

Step 6 of ``journal-match.md`` asks for a *downgrade ladder*: after a rejection, which
venue is the next rung that keeps the audience and needs the least reframing? That
relation used to be improvised at match time. This builds it from evidence the
repository already contains: **which venues each pack's own prose names as siblings,
alternatives or fallbacks**.

The graph is deliberately labelled as *candidate adjacency*, not a ranking. A high
co-mention count means the two venues are discussed together as realistic
alternatives by the pack that knows the venue best; the agent still applies the
fit / audience / odds judgement from ``journal-match.md``.

Usage:  python3 tools/gen_ladder.py [--check]
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter, defaultdict, deque
from pathlib import Path

from venue_lib import ROOT, acronym_fits, read

INDEX = ROOT / "shared-resources/journal-selection/venue-index.tsv"
OUT = ROOT / "shared-resources/journal-selection/ladder.tsv"
ADJACENCY_OUT = ROOT / "shared-resources/journal-selection/discipline-adjacency.tsv"

COLUMNS = ["from_venue", "to_venue", "to_display_name", "mentions", "same_discipline",
           "to_coverage", "to_tier", "to_region"]

ADJACENCY_COLUMNS = ["discipline", "adjacent_discipline", "edges", "share_pct"]

MIN_MENTIONS = 2
MAX_EDGES_PER_VENUE = 8

# Discipline adjacency is read off the venue graph rather than asserted. A pair has to
# clear both bars: enough edges to not be one pack's quirk, and a large enough share of
# the source discipline's outgoing edges to be a habit rather than a stray citation.
MIN_ADJACENCY_EDGES = 3
MIN_ADJACENCY_SHARE = 4.0

# An alias only counts if it cannot plausibly appear as ordinary prose. Latin aliases
# must be long, or carry an internal capital (NeurIPS, CVPR, QJE, AEJ) — which rules
# out bare venue names that are also common words (Nature, Science, Cell, Mind).
_ACRONYMISH = re.compile(r"^[A-Z][A-Za-z0-9]*[A-Z][A-Za-z0-9-]*$")
_CJK = re.compile(r"[一-鿿]")


def aliases_for(row: dict, profile_text: str) -> set[str]:
    out: set[str] = set()
    name = row["display_name"].strip()
    if _CJK.search(name):
        if len(name) >= 3:
            out.add(name)
    elif len(name) >= 10 or _ACRONYMISH.match(name):
        out.add(name)
    # Acronyms the venue's own profile declares, e.g. "... (QJE) ...". Guarded: these
    # parentheses hold society names as often as venue names, and an unguarded "ASA"
    # made every sociology pack look adjacent to Anesthesiology.
    for match in re.findall(r"\(([A-Z][A-Za-z0-9&-]{1,9})\)", profile_text[:4000]):
        if not (_ACRONYMISH.match(match) or match.isupper()):
            continue
        if acronym_fits(match, name) or acronym_fits(match, row["venue_id"].replace("-", " ")):
            out.add(match)
    return {a for a in out if len(a) >= 3}


def alias_automaton(aliases: list[str]):
    """Build a dependency-free Aho-Corasick matcher for all venue aliases."""
    transitions: list[dict[str, int]] = [{}]
    failures = [0]
    outputs: list[list[str]] = [[]]
    for alias in aliases:
        state = 0
        for char in alias:
            if char not in transitions[state]:
                transitions[state][char] = len(transitions)
                transitions.append({})
                failures.append(0)
                outputs.append([])
            state = transitions[state][char]
        outputs[state].append(alias)

    queue = deque(transitions[0].values())
    while queue:
        state = queue.popleft()
        for char, child in transitions[state].items():
            queue.append(child)
            fallback = failures[state]
            while fallback and char not in transitions[fallback]:
                fallback = failures[fallback]
            failures[child] = transitions[fallback].get(char, 0)
            outputs[child].extend(outputs[failures[child]])
    return transitions, failures, outputs


def alias_mentions(text: str, automaton):
    """Yield aliases as free-standing names, never raw Latin substrings."""
    transitions, failures, outputs = automaton
    state = 0
    for end, char in enumerate(text):
        while state and char not in transitions[state]:
            state = failures[state]
        state = transitions[state].get(char, 0)
        for alias in outputs[state]:
            start = end - len(alias) + 1
            if not _CJK.search(alias):
                left_blocked = start > 0 and bool(re.match(r"[A-Za-z0-9]", text[start - 1]))
                right_blocked = end + 1 < len(text) and bool(re.match(r"[A-Za-z0-9]", text[end + 1]))
                if left_blocked or right_blocked:
                    continue
            yield alias


def pack_prose(row: dict) -> str:
    """All venue-facing prose for a row — skills only; source maps are URL-heavy."""
    if row["coverage"] == "depth":
        pack = ROOT / row["pack_dir"]
        parts = [read(p) for p in sorted((pack / "skills").glob("*/SKILL.md"))]
        readme = pack / "README.md"
        if readme.exists():
            parts.append(read(readme))
        return "\n".join(parts)
    return read(ROOT / row["profile_path"])


def build() -> list[dict]:
    rows = list(csv.DictReader(INDEX.open(encoding="utf-8"), delimiter="\t"))
    by_id = {r["venue_id"]: r for r in rows}

    prose = {r["venue_id"]: pack_prose(r) for r in rows}

    alias_to_venue: dict[str, str] = {}
    collisions: set[str] = set()
    for row in rows:
        for alias in aliases_for(row, prose[row["venue_id"]]):
            if alias in alias_to_venue and alias_to_venue[alias] != row["venue_id"]:
                collisions.add(alias)
            alias_to_venue[alias] = row["venue_id"]
    for alias in collisions:                      # ambiguous — cannot attribute a mention
        alias_to_venue.pop(alias, None)

    # One multi-pattern scan replaces the former venue × alias nested regex loop,
    # while still reporting contained aliases independently as the old counters did.
    ordered = sorted(alias_to_venue, key=len, reverse=True)
    automaton = alias_automaton(ordered)

    edges: dict[str, Counter] = defaultdict(Counter)
    for venue_id, text in prose.items():
        if not text:
            continue
        mention_counts = Counter(alias_mentions(text, automaton))
        # Preserve the historical longest-alias insertion order so equal-count
        # targets keep stable output ordering.
        for alias in ordered:
            count = mention_counts.get(alias, 0)
            if not count:
                continue
            target = alias_to_venue[alias]
            if target == venue_id:
                continue
            edges[venue_id][target] += count

    out: list[dict] = []
    for venue_id, counter in edges.items():
        src = by_id[venue_id]
        ranked = [(t, c) for t, c in counter.most_common() if c >= MIN_MENTIONS]
        for target, count in ranked[:MAX_EDGES_PER_VENUE]:
            dst = by_id[target]
            out.append({
                "from_venue": venue_id,
                "to_venue": target,
                "to_display_name": dst["display_name"],
                "mentions": count,
                "same_discipline": "yes" if dst["discipline"] == src["discipline"] else "no",
                "to_coverage": dst["coverage"],
                "to_tier": dst["tier"],
                "to_region": dst["region"],
            })
    out.sort(key=lambda e: (e["from_venue"], -int(e["mentions"]), e["to_venue"]))
    return out


def render(edges: list[dict]) -> str:
    lines = ["\t".join(COLUMNS)]
    for edge in edges:
        lines.append("\t".join(str(edge[c]) for c in COLUMNS))
    return "\n".join(lines) + "\n"


def build_adjacency(edges: list[dict]) -> list[dict]:
    """Which disciplines routinely stand in for one another, per the venue graph.

    Step 1 of ``journal-match.md`` asks for the paper's discipline, and Step 2 then
    filters on it. A labour-economics paper belongs in ``economics/labor``, but its real
    shortlist also runs through ``economics``, ``economics/public`` and sometimes
    ``demography`` — a fact the method stated in prose and left the agent to remember.

    Collapsing the venue-level adjacency graph by discipline turns it into data: if the
    packs that know labour economics keep naming general-economics venues as the
    alternative, those disciplines are adjacent. The matcher uses it to *widen* a
    discipline prior, never to override it.
    """
    rows = list(csv.DictReader(INDEX.open(encoding="utf-8"), delimiter="\t"))
    disc = {r["venue_id"]: r["discipline"] for r in rows}

    pairs: dict[str, Counter] = defaultdict(Counter)
    totals: Counter = Counter()
    for edge in edges:
        source, target = disc.get(edge["from_venue"]), disc.get(edge["to_venue"])
        if not source or not target:
            continue
        totals[source] += 1
        if source != target:
            pairs[source][target] += 1

    out: list[dict] = []
    for source, counter in pairs.items():
        for target, count in counter.items():
            share = 100.0 * count / max(totals[source], 1)
            if count < MIN_ADJACENCY_EDGES or share < MIN_ADJACENCY_SHARE:
                continue
            out.append({
                "discipline": source,
                "adjacent_discipline": target,
                "edges": count,
                "share_pct": f"{share:.1f}",
            })
    out.sort(key=lambda r: (r["discipline"], -int(r["edges"]), r["adjacent_discipline"]))
    return out


def render_adjacency(rows: list[dict]) -> str:
    lines = ["\t".join(ADJACENCY_COLUMNS)]
    for row in rows:
        lines.append("\t".join(str(row[c]) for c in ADJACENCY_COLUMNS))
    return "\n".join(lines) + "\n"


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="fail if the committed ladder differs from a fresh build")
    args = parser.parse_args(argv)

    edges = build()
    text = render(edges)
    adjacency = build_adjacency(edges)
    adjacency_text = render_adjacency(adjacency)

    if args.check:
        for path, fresh in ((OUT, text), (ADJACENCY_OUT, adjacency_text)):
            current = path.read_text(encoding="utf-8") if path.exists() else ""
            if current != fresh:
                print(f"FAIL: {path.relative_to(ROOT)} is stale — run "
                      "`python3 tools/gen_ladder.py`", file=sys.stderr)
                return 1
        print(f"OK: ladder current ({len(edges)} edges, "
              f"{len(adjacency)} discipline pairs)")
        return 0

    OUT.write_text(text, encoding="utf-8")
    ADJACENCY_OUT.write_text(adjacency_text, encoding="utf-8")
    sources = len({e["from_venue"] for e in edges})
    same = sum(1 for e in edges if e["same_discipline"] == "yes")
    print(f"wrote {len(edges)} adjacency edges for {sources} venues -> "
          f"{OUT.relative_to(ROOT)}")
    print(f"  same-discipline edges: {same} ({same * 100 // max(len(edges), 1)}%)")
    print(f"wrote {len(adjacency)} discipline pairs -> "
          f"{ADJACENCY_OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
