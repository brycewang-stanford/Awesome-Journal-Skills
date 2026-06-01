#!/usr/bin/env python3
"""Report source-map verification anchors across first-party journal packs.

This is intentionally a reporting tool by default: it exits 0 even when it
finds warnings, so maintainers can use it during source-backed cleanup without
blocking unrelated lanes. Pass --strict when a batch should fail on warnings.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
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

URL_RE = re.compile(r"https?://[^\s<>)\"']+")
DATE_RE = re.compile(r"\b20\d{2}-\d{2}(?:-\d{2})?\b")
UNVERIFIED_RE = re.compile(
    r"\bUNVERIFIED\b|"
    r"\u5f85\u6838\u5b9e|"  # 待核实
    r"could not|blocked|forbidden|captcha|403|"
    r"\u767b\u5f55|"  # 登录
    r"javascript|js-rendered",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class SourceMapReport:
    path: str
    chars: int
    urls: int
    dates: int
    unresolved_flags: int
    warnings: list[str]


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def top_level(path: Path) -> str:
    return path.relative_to(ROOT).parts[0]


def is_hidden_or_git(path: Path) -> bool:
    return any(part == ".git" for part in path.parts)


def is_imported_root(path: Path) -> bool:
    return top_level(path) in IMPORTED_ROOTS


def expand_target(target: str) -> list[Path]:
    path = (ROOT / target).resolve()
    try:
        path.relative_to(ROOT)
    except ValueError:
        raise ValueError(f"{target!r} is outside the repository") from None

    if path.is_file():
        return [path]
    if path.is_dir():
        return sorted(path.rglob("resources/official-source-map.md"))
    raise ValueError(f"{target!r} does not exist")


def iter_source_maps(targets: list[str]) -> list[Path]:
    if targets:
        paths: list[Path] = []
        for target in targets:
            paths.extend(expand_target(target))
    else:
        paths = sorted(ROOT.glob("*/resources/official-source-map.md"))

    return sorted(
        {
            path
            for path in paths
            if not is_hidden_or_git(path) and not is_imported_root(path)
        }
    )


def analyze(path: Path, min_chars: int) -> SourceMapReport:
    text = path.read_text(encoding="utf-8", errors="replace")
    stripped = text.strip()
    urls = sorted(set(URL_RE.findall(text)))
    dates = DATE_RE.findall(text)
    unresolved = UNVERIFIED_RE.findall(text)

    warnings: list[str] = []
    if len(stripped) < min_chars:
        warnings.append(f"shorter than {min_chars} chars")
    if not urls:
        warnings.append("no source URL")
    if not dates:
        warnings.append("no visible access/check date")

    return SourceMapReport(
        path=rel(path),
        chars=len(stripped),
        urls=len(urls),
        dates=len(dates),
        unresolved_flags=len(unresolved),
        warnings=warnings,
    )


def print_text(reports: list[SourceMapReport], show_all: bool) -> None:
    warnings = [report for report in reports if report.warnings]
    print(f"Source-map audit scanned {len(reports)} first-party official source maps.")
    print(f"Warnings: {len(warnings)}")

    rows = reports if show_all else warnings
    if rows:
        print()
    for report in rows:
        suffix = "; ".join(report.warnings) if report.warnings else "ok"
        print(
            f"- {report.path}: chars={report.chars}, urls={report.urls}, "
            f"dates={report.dates}, unresolved_flags={report.unresolved_flags} [{suffix}]"
        )

    top_unresolved = sorted(reports, key=lambda item: item.unresolved_flags, reverse=True)[:5]
    if top_unresolved:
        print("\nHighest unresolved-flag counts:")
        for report in top_unresolved:
            print(f"- {report.unresolved_flags:>3} {report.path}")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        help="optional source-map files or pack directories to audit",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="print every source map instead of only warnings",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="emit machine-readable JSON",
    )
    parser.add_argument(
        "--min-chars",
        type=int,
        default=400,
        help="minimum stripped character count before a source map is considered too thin",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="exit non-zero if any source map has warnings",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    if args.min_chars < 1:
        print("--min-chars must be positive", file=sys.stderr)
        return 2

    try:
        paths = iter_source_maps(args.paths)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 2

    reports = [analyze(path, args.min_chars) for path in paths]
    if args.json:
        print(json.dumps([asdict(report) for report in reports], ensure_ascii=False, indent=2))
    else:
        print_text(reports, args.all)

    if args.strict and any(report.warnings for report in reports):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
