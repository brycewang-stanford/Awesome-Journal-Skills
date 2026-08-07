#!/usr/bin/env python3
"""Shortlist candidate venues for a paper — step 2 of the journal-match method.

    python3 tools/match_venues.py --title "..." --abstract "..." \
            --discipline finance --lane empirical --top 15

    python3 tools/match_venues.py --file paper.txt --json          # for piping
    python3 tools/match_venues.py --title "..." --exclude journal-of-finance
            # after a reject: rank the remaining field

Output is a **reading list, not a recommendation.** Every row points at the venue's own
pack (``source_map`` for a depth pack, ``profile_path`` for a breadth profile); fit,
acceptance odds, cost and audience are judged there, against live facts, in steps 3-6 of
``shared-resources/journal-selection/journal-match.md``. Nothing volatile — fees,
acceptance rates, turnaround, page limits — is stored in or printed by this tool.

``--discipline`` is a prior, not a filter: venues in that discipline and in disciplines
adjacent to it (``discipline-adjacency.tsv``) are boosted, but a strong lexical match
elsewhere still surfaces, because Step-1 profiling is a judgement call that is sometimes
wrong. Pass ``--only-discipline`` when you are certain and want the field narrowed hard.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from match_lib import VenueMatcher, load_venues
from venue_lib import ROOT


def read_query(args) -> str:
    parts = [args.title or "", args.abstract or ""]
    if args.file:
        parts.append(Path(args.file).read_text(encoding="utf-8", errors="replace"))
    if not args.title and not args.abstract and not args.file and not sys.stdin.isatty():
        parts.append(sys.stdin.read())
    return "\n".join(p for p in parts if p).strip()


def where_to_read(venue: dict) -> str:
    return venue["source_map"] or venue["profile_path"] or venue["pack_dir"]


def render_text(hits, query_terms: int) -> str:
    if not hits:
        return ("No venue shared a scope term with this text.\n"
                "Widen the query (add the abstract), or drop --discipline / "
                "--only-discipline — and if the field really is outside the index, say "
                "so rather than forcing a poor fit.")
    top = hits[0].score or 1.0
    lines = [f"{len(hits)} candidates · {query_terms} query terms · "
             "scores are relative, not probabilities", ""]
    for i, hit in enumerate(hits, 1):
        v = hit.venue
        lines.append(
            f"{i:>3}. {v['display_name']}  [{v['venue_id']}]\n"
            f"     {v['discipline']} · {v['venue_type']} · {v['lane']} · {v['region']} · "
            f"tier: {v['tier']} · {v['coverage']}\n"
            f"     match {hit.score / top:.2f} via: {hit.why()}\n"
            f"     read: {where_to_read(v)}"
        )
    lines += [
        "",
        "Next: open each candidate's pack before ranking it. Live facts (fees, "
        "acceptance, turnaround, page limits) are only in the source map.",
    ]
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--title", help="the paper's title")
    parser.add_argument("--abstract", help="the paper's abstract")
    parser.add_argument("--file", help="read the paper text from a file")
    parser.add_argument("--discipline", help="Step-1 discipline; a prior, not a filter")
    parser.add_argument("--only-discipline", action="store_true",
                        help="hard-filter to the discipline and its adjacents")
    parser.add_argument("--lane", help="empirical / theory / review / qualitative")
    parser.add_argument("--region", help="international / china")
    parser.add_argument("--venue-type", help="journal / conference")
    parser.add_argument("--coverage", help="depth / breadth")
    parser.add_argument("--exclude", action="append", default=[],
                        help="venue_id to drop (repeatable) — e.g. one that just rejected it")
    parser.add_argument("--top", type=int, default=15, help="candidates to print")
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    parser.add_argument("--list-disciplines", action="store_true",
                        help="print the discipline vocabulary and exit")
    args = parser.parse_args(argv)

    venues = load_venues()

    if args.list_disciplines:
        counts: dict[str, int] = {}
        for v in venues:
            counts[v["discipline"]] = counts.get(v["discipline"], 0) + 1
        for name, count in sorted(counts.items()):
            print(f"{count:>4}  {name}")
        return 0

    query = read_query(args)
    if not query:
        parser.error("give the paper's text via --title/--abstract, --file, or stdin")

    matcher = VenueMatcher(venues)
    hits = matcher.rank(
        query,
        discipline=args.discipline,
        lane=args.lane,
        region=args.region,
        venue_type=args.venue_type,
        coverage=args.coverage,
        exclude=set(args.exclude),
        only_discipline=args.only_discipline,
        limit=args.top,
    )

    if args.json:
        print(json.dumps([{
            "venue_id": h.venue["venue_id"],
            "display_name": h.venue["display_name"],
            "score": round(h.score, 4),
            "discipline": h.venue["discipline"],
            "venue_type": h.venue["venue_type"],
            "lane": h.venue["lane"],
            "region": h.venue["region"],
            "tier": h.venue["tier"],
            "coverage": h.venue["coverage"],
            "read": where_to_read(h.venue),
            "matched_terms": [t for t, _ in h.terms],
        } for h in hits], ensure_ascii=False, indent=2))
    else:
        print(render_text(hits, len(matcher.query_terms(query))))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
