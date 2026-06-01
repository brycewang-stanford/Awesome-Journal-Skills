#!/usr/bin/env python3
"""Find likely find-replace clones among journal skill files.

The detector is intentionally heuristic and dependency-free. It is meant to
surface review targets, not to prove plagiarism or semantic duplication.
"""

from __future__ import annotations

import argparse
import heapq
import itertools
import re
import sys
import unicodedata
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

IMPORTED_ROOTS = {
    "AER-Skills",
    "AER-skills",
    "Nature-Skills",
    "nature-skills",
    "nature-paper-skills",
    "claude-scholar",
    "codex-claude-academic-skills",
}

BREADTH_BUNDLES = {
    "Chinese-SocialScience-Journal-Skills",
    "Computer-Science-Conference-Skills",
    "English-SocialScience-Journal-Skills",
    "English-NaturalScience-Journal-Skills",
}

WORD_RE = re.compile(r"[a-z0-9]+")
KEEP_RE = re.compile(r"[a-z0-9\u4e00-\u9fff]+")
FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n?", re.DOTALL)
URL_RE = re.compile(r"https?://\S+")
FENCED_CODE_RE = re.compile(r"```.*?```|~~~.*?~~~", re.DOTALL)


@dataclass(frozen=True)
class SkillDoc:
    path: Path
    group: str
    normalized: str
    shingles: frozenset[str]


@dataclass(frozen=True)
class ClonePair:
    score: float
    group: str
    left: Path
    right: Path


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def top_level(path: Path) -> str:
    return path.relative_to(ROOT).parts[0]


def is_hidden_or_git(path: Path) -> bool:
    return any(part == ".git" for part in path.parts)


def is_nature_plugin_mirror(path: Path) -> bool:
    parts = [part.casefold() for part in path.relative_to(ROOT).parts]
    return len(parts) >= 4 and parts[:3] == ["nature-skills", "plugins", "nature-skills"]


def split_slug(value: str) -> set[str]:
    return {word for word in WORD_RE.findall(value.casefold()) if len(word) > 2}


def local_terms(path: Path) -> set[str]:
    terms: set[str] = set()
    for part in path.relative_to(ROOT).parts:
        if part in {"skills", "SKILL.md"}:
            continue
        terms.update(split_slug(part))
    return terms


def normalize_text(path: Path, text: str) -> str:
    text = FRONTMATTER_RE.sub("", text)
    text = FENCED_CODE_RE.sub(" ", text)
    text = unicodedata.normalize("NFKC", text).casefold()
    text = URL_RE.sub(" URL ", text)
    text = re.sub(r"\d+", "0", text)

    for term in sorted(local_terms(path), key=len, reverse=True):
        text = re.sub(rf"\b{re.escape(term)}\b", " ", text)

    return "".join(KEEP_RE.findall(text))


def shingles(text: str, width: int) -> frozenset[str]:
    if len(text) <= width:
        return frozenset({text}) if text else frozenset()
    return frozenset(text[index : index + width] for index in range(len(text) - width + 1))


def role_group(path: Path, force_group: str | None = None) -> str:
    if force_group:
        return force_group

    root = top_level(path)
    if root in BREADTH_BUNDLES:
        return f"breadth:{root}"

    slug = path.parent.name
    pieces = slug.split("-")
    if len(pieces) > 1:
        return "role:" + "-".join(pieces[1:])
    return f"skill:{slug}"


def iter_skill_files(scope: str, bundle: str | None) -> list[Path]:
    base = ROOT / bundle if bundle else ROOT
    files = []
    for path in sorted(base.rglob("SKILL.md")):
        if is_hidden_or_git(path) or is_nature_plugin_mirror(path):
            continue
        imported = top_level(path) in IMPORTED_ROOTS
        if scope == "first-party" and imported:
            continue
        if scope == "imported" and not imported:
            continue
        files.append(path)
    return files


def load_docs(paths: list[Path], group_all: bool, shingle_width: int, min_chars: int) -> list[SkillDoc]:
    docs: list[SkillDoc] = []
    forced_group = "bundle" if group_all else None
    for path in paths:
        normalized = normalize_text(path, path.read_text(encoding="utf-8", errors="replace"))
        if len(normalized) < min_chars:
            continue
        docs.append(
            SkillDoc(
                path=path,
                group=role_group(path, forced_group),
                normalized=normalized,
                shingles=shingles(normalized, shingle_width),
            )
        )
    return docs


def jaccard(left: frozenset[str], right: frozenset[str]) -> float:
    if not left or not right:
        return 0.0
    intersection = len(left & right)
    union = len(left | right)
    return intersection / union if union else 0.0


def find_pairs(docs: list[SkillDoc], top: int) -> list[ClonePair]:
    groups: dict[str, list[SkillDoc]] = defaultdict(list)
    for doc in docs:
        groups[doc.group].append(doc)

    heap: list[tuple[float, str, str, ClonePair]] = []
    for group, grouped_docs in groups.items():
        if len(grouped_docs) < 2:
            continue
        for left, right in itertools.combinations(grouped_docs, 2):
            score = jaccard(left.shingles, right.shingles)
            pair = ClonePair(score, group, left.path, right.path)
            item = (score, rel(left.path), rel(right.path), pair)
            if len(heap) < top:
                heapq.heappush(heap, item)
            elif score > heap[0][0]:
                heapq.heapreplace(heap, item)

    return [item[3] for item in sorted(heap, reverse=True)]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--scope",
        choices=("first-party", "all", "imported"),
        default="first-party",
        help="which skill roots to scan; default excludes imported upstream packs",
    )
    parser.add_argument(
        "--bundle",
        help="limit the scan to one top-level pack directory, e.g. Chinese-SocialScience-Journal-Skills",
    )
    parser.add_argument("--top", type=int, default=30, help="number of highest-similarity pairs to print")
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.70,
        help="only print pairs at or above this similarity score",
    )
    parser.add_argument(
        "--fail-threshold",
        type=float,
        help="exit non-zero if any reported pair reaches this score",
    )
    parser.add_argument(
        "--shingle-width",
        type=int,
        default=8,
        help="character shingle width used for Jaccard similarity",
    )
    parser.add_argument(
        "--min-chars",
        type=int,
        default=400,
        help="skip very small normalized files",
    )
    parser.add_argument(
        "--group-all",
        action="store_true",
        help="compare every scanned skill against every other scanned skill",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    if args.top < 1:
        print("--top must be positive", file=sys.stderr)
        return 2
    if args.shingle_width < 2:
        print("--shingle-width must be at least 2", file=sys.stderr)
        return 2

    paths = iter_skill_files(args.scope, args.bundle)
    docs = load_docs(paths, args.group_all, args.shingle_width, args.min_chars)
    pairs = find_pairs(docs, args.top)
    reported = [pair for pair in pairs if pair.score >= args.threshold]

    print(
        "Clone audit scanned "
        f"{len(docs)} skills in {len({doc.group for doc in docs})} comparison groups "
        f"(scope={args.scope})."
    )

    if not reported:
        print(f"No pairs at or above threshold {args.threshold:.3f}.")
    else:
        print(f"Pairs at or above threshold {args.threshold:.3f}:")
        for pair in reported:
            print(
                f"- {pair.score:.3f} [{pair.group}] "
                f"{rel(pair.left)} <=> {rel(pair.right)}"
            )

    if args.fail_threshold is not None:
        failures = [pair for pair in pairs if pair.score >= args.fail_threshold]
        if failures:
            print(
                f"Clone audit failed: {len(failures)} pair(s) reached "
                f"fail threshold {args.fail_threshold:.3f}.",
                file=sys.stderr,
            )
            return 1

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
