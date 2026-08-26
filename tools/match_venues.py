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


# A shortlist whose top entries each rest on one or two words is not a shortlist, it is
# a coincidence. Saying so is the difference between a coverage gap the author can act
# on and a confidently wrong recommendation they cannot see through.
WEAK_EVIDENCE_TERMS = 2
WEAK_EVIDENCE_DEPTH = 3


# A shortlist is a comparison, and a comparison between venues that were searched over
# different amounts of evidence is not a fair one. Below this share of prose-only
# candidates in the top slots, the asymmetry is a footnote; above it, the ranking itself
# is partly an artefact of who could be resolved to a bibliographic source.
PROSE_ONLY_SHARE = 0.34


def warnings_for(hits, discipline: str | None, matcher=None) -> list[str]:
    out: list[str] = []
    top = hits[:WEAK_EVIDENCE_DEPTH]
    if top and max(len(h.terms) for h in top) <= WEAK_EVIDENCE_TERMS:
        out.append(
            "⚠ Weak evidence: every leading candidate matched on "
            f"{WEAK_EVIDENCE_TERMS} scope terms or fewer. A ranking built on one or two "
            "shared words is close to noise — reuse of a word across fields ('sensor', "
            "'generation', 'network') will beat a genuine subject match. Add the "
            "abstract, and treat the list as a lead rather than a shortlist.")
    if discipline and not any(h.venue["discipline"] == discipline for h in hits):
        out.append(
            f"⚠ Coverage gap: nothing in `{discipline}` matched this text at all — the "
            "prior can only re-rank venues that scored, not conjure one. Either the "
            "discipline label is wrong (check `--list-disciplines`), or this subject "
            "area is thin in the index. Say so rather than recommending what did "
            "surface; `rt-venue-integrity` covers venues this repository does not.")
    if matcher is not None and matcher.topics_loaded and hits:
        prose_only = [h for h in hits
                      if h.venue["venue_id"] not in matcher.subject_venues]
        if len(prose_only) >= max(1, int(PROSE_ONLY_SHARE * len(hits))):
            out.append(
                f"⚠ Uneven evidence: {len(prose_only)} of {len(hits)} candidates "
                "(marked °) were searched over their pack's prose only. No "
                "bibliographic source could be resolved for them, so the subject "
                "vocabulary — what the venue actually publishes about — is missing on "
                "one side of this comparison. It is mostly Chinese-language journals "
                "that neither Crossref nor DBLP indexes. Their absence from the top of "
                "the list is weak evidence about fit; read them before ruling them out.")
    return out


def render_text(hits, query_terms: int, discipline: str | None = None,
                matcher=None) -> str:
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
        prose_only = (matcher is not None and matcher.topics_loaded
                      and v["venue_id"] not in matcher.subject_venues)
        mark = "°" if prose_only else ""
        lines.append(
            f"{i:>3}. {v['display_name']}{mark}  [{v['venue_id']}]\n"
            f"     {v['discipline']} · {v['venue_type']} · {v['lane']} · {v['region']} · "
            f"tier: {v['tier']} · {v['coverage']}\n"
            f"     match {hit.score / top:.2f} via: {hit.why()}\n"
            f"     read: {where_to_read(v)}"
        )
    for warning in warnings_for(hits, discipline, matcher):
        lines += ["", warning]
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
        payload = [{
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
            "subject_vocabulary": h.venue["venue_id"] in matcher.subject_venues,
        } for h in hits]
        print(json.dumps({"candidates": payload,
                          "warnings": warnings_for(hits, args.discipline, matcher)},
                         ensure_ascii=False, indent=2))
    else:
        print(render_text(hits, len(matcher.query_terms(query)), args.discipline,
                          matcher))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
