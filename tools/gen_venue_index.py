#!/usr/bin/env python3
"""Generate the STABLE venue index that powers the journal-match capability.

Covers BOTH tiers of repository coverage:

* **depth packs** — one venue per pack, many venue-specific skills, a live-checked
  ``resources/official-source-map.md``;
* **breadth-bundle profiles** — one venue per ``SKILL.md`` inside a discipline bundle.
  These are the long tail that used to exist only as prose and therefore could not be
  shortlisted or ranked by an agent.

Where a breadth profile duplicates a venue that already has a depth pack, the depth row
wins and the breadth row is dropped (the depth pack strictly dominates it for matching).

Stable fields only. No fees, acceptance rates, turnaround or page limits are ever
written here — those stay in each pack's ``official-source-map.md`` and are read at
match time by the agent. ``ranking_labels`` records only labels the pack's own text
asserts; nothing bibliometric is inferred.

Usage:  python3 tools/gen_venue_index.py [--check]
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path

import json
import re

from venue_lib import (
    BUNDLES,
    CHINA,
    NON_EMPIRICAL_DISCIPLINES,
    ROOT,
    THEORY,
    TIER,
    breadth_scope_text,
    depth_scope_text,
    derive_keywords,
    discipline_of,
    frontmatter_description,
    h1_display_name,
    identity_keys,
    index_digest,
    is_depth_pack,
    ranking_labels,
    read,
    slugify,
)


def depth_title_snippet(pack: Path, display: str) -> str:
    """Title-area text for identity matching: plugin description + README H1."""
    parts = [display]
    plugin = pack / ".claude-plugin" / "plugin.json"
    try:
        parts.append(json.loads(plugin.read_text(encoding="utf-8")).get("description", "")[:220])
    except (OSError, ValueError):
        pass
    readme = pack / "README.md"
    if readme.exists():
        head = read(readme, 400)
        parts.append(head.split("\n\n")[0])
    return "\n".join(parts)

# `scope_keywords` is last on purpose: `profile_path` and `source_map` are empty for
# breadth and depth rows respectively, and an empty final field leaves a trailing tab
# that `git diff --check` rejects. Keywords are guaranteed non-empty (see collect()).
COLUMNS = [
    "venue_id", "display_name", "coverage", "venue_type", "discipline", "region",
    "lane", "tier", "ranking_labels", "pack_dir", "profile_path", "source_map",
    "scope_keywords",
]

OUT = ROOT / "shared-resources/journal-selection/venue-index.tsv"
POSTINGS_OUT = ROOT / "shared-resources/journal-selection/scope-postings.tsv"

# Two consumers, two depths. A human (or an agent skimming the index) wants the handful
# of terms that characterise a venue; a retrieval pass wants the long tail, because the
# term a given paper happens to share with its venue is usually not in the top forty.
# Publishing both from one ranked list keeps them consistent by construction.
#
# The retrieval depth was 300 by assumption until it was measured against the gold set's
# `dev` half. Recall@10 rises the whole way out and flattens, and the file grows roughly
# linearly with it:
#
#     depth   300   600   900  1200  2000
#     R@10   41.0  45.5  46.9  47.7  48.5     (dev)
#     size    3.3   5.2   7.8   9.8  14 MB    (scope-postings.tsv)
#
# 900 is the knee: 600→900 buys 1.4 points, 900→1200 buys 0.8, and 1200→2000 buys 0.8
# more for another four megabytes of committed index that is rewritten on every
# regeneration. Two things that looked like they should help do not, and are recorded
# here so they are not retried: relaxing the `c < 2` rule in `derive_keywords` (±0.0
# points — the vocabulary is not what the rule removes), and widening the per-skill
# scope-text bounds by 3x (-0.7 points at this depth; the scope text is already long
# enough that the extra prose is off-topic).
KEYWORD_DEPTH = 900
INDEX_KEYWORDS = 40


def collect() -> list[dict]:
    records: list[dict] = []
    seen: dict[str, str] = {}

    # --- depth packs --------------------------------------------------------
    for plugin in sorted(ROOT.glob("*/.claude-plugin/plugin.json")):
        pack = plugin.parent.parent
        if not is_depth_pack(pack):
            continue
        name = pack.name
        display = name.replace("-Skills", "").replace("-", " ")
        disc = discipline_of(name)
        lane = THEORY.get(name) or (
            "interpretive/theory" if disc in NON_EMPIRICAL_DISCIPLINES else "empirical"
        )
        source_map = f"{name}/resources/official-source-map.md"
        scope = depth_scope_text(pack)
        vid = slugify(name.replace("-Skills", ""))
        for key in identity_keys(depth_title_snippet(pack, display), display, vid):
            seen[key] = name
        records.append({
            "venue_id": vid,
            "display_name": display,
            "coverage": "depth",
            "venue_type": "conference" if "conference" in disc else "journal",
            "discipline": disc,
            "region": "china" if name in CHINA else "international",
            "lane": lane,
            "tier": TIER.get(name, "field"),
            "ranking_labels": ";".join(ranking_labels(scope)),
            "scope_keywords": "",
            "pack_dir": name,
            "profile_path": "",
            "source_map": source_map if (ROOT / source_map).exists() else "",
            "_scope": scope,
        })

    # --- breadth-bundle venue profiles -------------------------------------
    dropped = 0
    for bundle_name, meta in sorted(BUNDLES.items()):
        bundle = ROOT / bundle_name
        if not bundle.is_dir():
            continue
        for skill in sorted((bundle / "skills").glob("*/SKILL.md")):
            slug = skill.parent.name
            # the bundle's own router skill is not a venue
            if slug.endswith("-journal-workflow") or slug.endswith("-workflow"):
                continue
            body = read(skill)
            display = h1_display_name(body, slug.replace("-", " ").title())
            # Title area only. The body names sibling venues as alternatives, and
            # scanning it merged distinct journals that merely cite each other.
            h1 = re.search(r"^#\s+.+$", body, re.M)
            title_snippet = "\n".join([
                display, frontmatter_description(body).split(" or ")[0],
                h1.group(0) if h1 else "",
            ])
            keys = identity_keys(title_snippet, display, slug)
            if keys & seen.keys():
                dropped += 1
                continue
            disc = discipline_of(
                "-".join(w.capitalize() for w in slug.split("-")), meta["discipline"]
            )
            lane = "interpretive/theory" if disc in NON_EMPIRICAL_DISCIPLINES else "empirical"
            scope = breadth_scope_text(skill)
            for key in keys:
                seen[key] = bundle_name
            records.append({
                "venue_id": slug,
                "display_name": display,
                "coverage": "breadth",
                "venue_type": "conference" if meta["type"] == "conference" or "conference" in disc
                              else "journal",
                "discipline": disc,
                "region": meta["region"],
                "lane": lane,
                "tier": "field",
                "ranking_labels": ";".join(ranking_labels(scope)),
                "scope_keywords": "",
                "pack_dir": bundle_name,
                "profile_path": f"{bundle_name}/skills/{slug}/SKILL.md",
                "source_map": "",
                "_scope": scope,
            })

    # --- scope keywords, derived across the whole corpus --------------------
    keywords = derive_keywords({r["venue_id"]: r["_scope"] for r in records},
                               top_n=KEYWORD_DEPTH)
    for record in records:
        terms = keywords.get(record["venue_id"]) or record["venue_id"].split("-")
        record["_keywords"] = terms
        record["scope_keywords"] = ";".join(terms[:INDEX_KEYWORDS])
        del record["_scope"]

    records.sort(key=lambda r: (r["discipline"], r["venue_id"]))
    print(f"  dropped {dropped} breadth profiles already covered by a depth pack")
    return records


def render_postings(records: list[dict]) -> str:
    """The inverted index behind `tools/match_venues.py`, as `term -> venue:rank` pairs.

    Venues are referenced by their **row number in `venue-index.tsv`**, which is what
    keeps this file small enough to commit. That makes the two files a matched pair, so
    the header carries the row count and a digest of the venue-id order; the matcher
    refuses to run against a postings file that does not describe the index it loaded.

    Only the *rank* of a term within its venue is stored, never a score. Weighting is the
    matcher's business and can be retuned without regenerating three megabytes of data.
    """
    postings: dict[str, list[str]] = {}
    for row, record in enumerate(records):
        for position, term in enumerate(record["_keywords"]):
            postings.setdefault(term, []).append(f"{row}:{position}")
    lines = [
        f"#venues\t{len(records)}",
        f"#digest\t{index_digest([r['venue_id'] for r in records])}",
        f"#depth\t{KEYWORD_DEPTH}",
        "#term\trow:rank,...",
    ]
    lines += [f"{term}\t{','.join(refs)}" for term, refs in sorted(postings.items())]
    return "\n".join(lines) + "\n"




def render(records: list[dict]) -> str:
    lines = ["\t".join(COLUMNS)]
    for record in records:
        lines.append("\t".join(str(record[c]) for c in COLUMNS))
    return "\n".join(lines) + "\n"


def stale(path: Path, text: str, tool: str) -> bool:
    current = path.read_text(encoding="utf-8") if path.exists() else ""
    if current == text:
        return False
    print(f"FAIL: {path.relative_to(ROOT)} is stale — run `{tool}`", file=sys.stderr)
    return True


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="fail if the committed index differs from a fresh generation")
    args = parser.parse_args(argv)

    records = collect()
    text = render(records)
    postings_text = render_postings(records)

    if args.check:
        tool = "python3 tools/gen_venue_index.py"
        if stale(OUT, text, tool) or stale(POSTINGS_OUT, postings_text, tool):
            return 1
        print(f"OK: venue index current ({len(records)} venues)")
        return 0

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(text, encoding="utf-8")
    POSTINGS_OUT.write_text(postings_text, encoding="utf-8")
    print(f"wrote {POSTINGS_OUT.relative_to(ROOT)} "
          f"({postings_text.count(chr(10)) - 4} terms, depth {KEYWORD_DEPTH})")

    coverage = Counter(r["coverage"] for r in records)
    print(f"wrote {len(records)} venues -> {OUT.relative_to(ROOT)}")
    print(f"  coverage: {dict(coverage)}")
    print(f"  types:    {dict(Counter(r['venue_type'] for r in records))}")
    print(f"  regions:  {dict(Counter(r['region'] for r in records))}")
    empty = [r['venue_id'] for r in records if not r['scope_keywords']]
    print(f"  venues without derived keywords: {len(empty)} {empty[:8]}")
    other = [r["venue_id"] for r in records if r["discipline"] == "other"]
    print(f"  discipline='other' (needs curation): {len(other)} {other[:12]}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
