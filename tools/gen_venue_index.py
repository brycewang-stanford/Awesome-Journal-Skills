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
    keywords = derive_keywords({r["venue_id"]: r["_scope"] for r in records})
    for record in records:
        terms = keywords.get(record["venue_id"]) or record["venue_id"].split("-")
        record["scope_keywords"] = ";".join(terms)
        del record["_scope"]

    records.sort(key=lambda r: (r["discipline"], r["venue_id"]))
    print(f"  dropped {dropped} breadth profiles already covered by a depth pack")
    return records


def render(records: list[dict]) -> str:
    lines = ["\t".join(COLUMNS)]
    for record in records:
        lines.append("\t".join(str(record[c]) for c in COLUMNS))
    return "\n".join(lines) + "\n"


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="fail if the committed index differs from a fresh generation")
    args = parser.parse_args(argv)

    records = collect()
    text = render(records)

    if args.check:
        current = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if current != text:
            print(f"FAIL: {OUT.relative_to(ROOT)} is stale — run "
                  "`python3 tools/gen_venue_index.py`", file=sys.stderr)
            return 1
        print(f"OK: venue index current ({len(records)} venues)")
        return 0

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(text, encoding="utf-8")

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
