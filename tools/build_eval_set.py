#!/usr/bin/env python3
"""Build the journal-match gold set from the repository's own exemplar libraries.

Each depth pack ships ``resources/exemplars/library.md`` — real papers that were
verified (with volume/issue/pages) to have appeared in that venue. That is exactly a
labelled ``(paper -> venue)`` corpus, so we can measure whether the venue index can
retrieve the true venue from a paper's title.

Output: ``shared-resources/journal-selection/eval/gold-set.tsv``

Known limitation, stated up front and repeated in the eval README: the exemplar prose
was written by the same authors as the packs, so the *context* field shares vocabulary
with the index. The headline metric therefore uses the **paper title only** — the
paper's own words, which no pack author chose.

Usage:  python3 tools/build_eval_set.py [--check]
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
from pathlib import Path

from venue_lib import ROOT, normalize_identity, read

INDEX = ROOT / "shared-resources/journal-selection/venue-index.tsv"
OUT = ROOT / "shared-resources/journal-selection/eval/gold-set.tsv"

# `context` sits mid-row rather than last: it is often empty, and an empty final field
# leaves a trailing tab that `git diff --check` rejects.
COLUMNS = ["paper_title", "true_venue_id", "context", "discipline", "region",
           "venue_type", "lane", "split"]


def split_of(title: str) -> str:
    """Assign a paper to `dev` or `test`, deterministically and for good.

    The matcher's weighting constants are chosen by looking at numbers, and numbers you
    tune against stop measuring anything. Tuning reads `dev`; the headline that CI gates
    is computed on `test`, which no constant has ever been fitted to. Splitting on a
    hash of the title (not on position) keeps the assignment stable as packs are added,
    so a paper never changes sides and the two halves stay comparable across releases.
    """
    digest = hashlib.sha1(title.lower().encode("utf-8")).hexdigest()
    return "dev" if int(digest, 16) % 2 == 0 else "test"

# Citation entries wrap across lines in many packs, so the bold run is matched with
# DOTALL and a length bound rather than anchored to a single line.
ENTRY = re.compile(r"^[ \t]*[-*][ \t]+\*\*(.{10,500}?)\*\*", re.M | re.S)
TITLE = re.compile(r"[\"“]([^\"”]{12,220})[\"”]")
CJK_TITLE = re.compile(r"[《「]([^》」]{6,120})[》」]")
WHY = re.compile(r"\*\*Why it is an exemplar:?\*\*\s*(.+?)(?=\n[ \t]*[-*][ \t]+\*\*|\n\n|\Z)",
                 re.S)


def clean(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"[*_`]", "", text)
    return text.strip(" ,.;:")


def harvest() -> list[dict]:
    rows = list(csv.DictReader(INDEX.open(encoding="utf-8"), delimiter="\t"))
    by_pack = {r["pack_dir"]: r for r in rows if r["coverage"] == "depth"}

    gold: list[dict] = []
    seen_titles: set[str] = set()
    for pack_dir, venue in sorted(by_pack.items()):
        library = ROOT / pack_dir / "resources" / "exemplars" / "library.md"
        if not library.exists():
            continue
        text = read(library)
        # Walk entries positionally so each title keeps its own "why" block; pairing
        # two independent findall() lists silently misaligns whenever one is missing.
        # Only entries that actually carry a paper title bound a block. Using every
        # bold list item would put the "Why it is an exemplar" bullet itself at the
        # block boundary, leaving no room to find the context.
        citations = []
        for entry in ENTRY.finditer(text):
            match = TITLE.search(entry.group(1)) or CJK_TITLE.search(entry.group(1))
            if match:
                citations.append((entry, match))
        for i, (entry, match) in enumerate(citations):
            title = clean(match.group(1))
            if len(title.split()) < 3 and not re.search(r"[一-鿿]", title):
                continue
            # 《刊名》 in a citation is the journal, not the paper
            if normalize_identity(title) == normalize_identity(venue["display_name"]):
                continue
            key = title.lower()
            if key in seen_titles:           # a paper cited by two packs is not a label
                continue
            seen_titles.add(key)
            block_end = citations[i + 1][0].start() if i + 1 < len(citations) else len(text)
            why = WHY.search(text, entry.end(), block_end)
            gold.append({
                "paper_title": title,
                "true_venue_id": venue["venue_id"],
                "discipline": venue["discipline"],
                "region": venue["region"],
                "venue_type": venue["venue_type"],
                "lane": venue["lane"],
                "split": split_of(title),
                "context": clean(why.group(1))[:300] if why else "",
            })
    gold.sort(key=lambda r: (r["true_venue_id"], r["paper_title"]))
    return gold


def render(gold: list[dict]) -> str:
    lines = ["\t".join(COLUMNS)]
    for row in gold:
        lines.append("\t".join(row[c].replace("\t", " ") for c in COLUMNS))
    return "\n".join(lines) + "\n"


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="fail if the committed gold set differs from a fresh build")
    args = parser.parse_args(argv)

    gold = harvest()
    text = render(gold)

    if args.check:
        current = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if current != text:
            print(f"FAIL: {OUT.relative_to(ROOT)} is stale — run "
                  "`python3 tools/build_eval_set.py`", file=sys.stderr)
            return 1
        print(f"OK: gold set current ({len(gold)} papers)")
        return 0

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(text, encoding="utf-8")
    venues = len({r["true_venue_id"] for r in gold})
    with_ctx = sum(1 for r in gold if r["context"])
    print(f"wrote {len(gold)} labelled papers across {venues} venues -> "
          f"{OUT.relative_to(ROOT)}")
    print(f"  with exemplar context: {with_ctx}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
