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
from collections import Counter, defaultdict
from pathlib import Path

from venue_lib import ROOT, acronym_fits, read

INDEX = ROOT / "shared-resources/journal-selection/venue-index.tsv"
OUT = ROOT / "shared-resources/journal-selection/ladder.tsv"

COLUMNS = ["from_venue", "to_venue", "to_display_name", "mentions", "same_discipline",
           "to_coverage", "to_tier", "to_region"]

MIN_MENTIONS = 2
MAX_EDGES_PER_VENUE = 8

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

    # longest alias first, so "American Economic Review" wins over a contained acronym
    ordered = sorted(alias_to_venue, key=len, reverse=True)

    edges: dict[str, Counter] = defaultdict(Counter)
    for venue_id, text in prose.items():
        if not text:
            continue
        for alias in ordered:
            target = alias_to_venue[alias]
            if target == venue_id:
                continue
            count = text.count(alias)
            if count:
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


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="fail if the committed ladder differs from a fresh build")
    args = parser.parse_args(argv)

    edges = build()
    text = render(edges)

    if args.check:
        current = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if current != text:
            print(f"FAIL: {OUT.relative_to(ROOT)} is stale — run "
                  "`python3 tools/gen_ladder.py`", file=sys.stderr)
            return 1
        print(f"OK: ladder current ({len(edges)} edges)")
        return 0

    OUT.write_text(text, encoding="utf-8")
    sources = len({e["from_venue"] for e in edges})
    same = sum(1 for e in edges if e["same_discipline"] == "yes")
    print(f"wrote {len(edges)} adjacency edges for {sources} venues -> "
          f"{OUT.relative_to(ROOT)}")
    print(f"  same-discipline edges: {same} ({same * 100 // max(len(edges), 1)}%)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
