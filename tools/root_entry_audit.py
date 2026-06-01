#!/usr/bin/env python3
"""Report quality signals for root-level journal entry folders.

The repository audit enforces hard invariants for these folders. This tool is a
softer companion for the root-card enrichment lane: it reports how many cards
are still machine-only and which enriched cards need stronger source anchors.
It exits 0 by default; pass --strict to fail on warnings.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

ROOT_ENTRY_MARKER = "AJS-ROOT-JOURNAL-ENTRY"
CANONICAL_RE = re.compile(r"^- Canonical skill:\s*\[[^\]]+]\(([^)]+)\)", re.MULTILINE)
SKILL_NAME_RE = re.compile(r"^- Skill name:\s*`([^`]+)`", re.MULTILINE)
BUNDLE_RE = re.compile(r"^- Bundle:\s*\[[^\]]+]\(([^)]+)\)", re.MULTILINE)
URL_RE = re.compile(r"https?://[^\s<>)\"']+")
DATE_RE = re.compile(r"\b20\d{2}-\d{2}(?:-\d{2})?\b")
FACT_LABEL_RE = re.compile(
    r"\b(Field|Publisher|Founded|ISSN|Frequency|Standing|Official)\b|"
    r"\u5b66\u79d1|\u4e3b\u529e|\u521b\u520a|\u520a\u53f7|\u5468\u671f|\u5b98\u7f51"
)


@dataclass(frozen=True)
class RootEntryReport:
    path: str
    chars: int
    canonical: bool
    skill_name: bool
    bundle: bool
    external_urls: int
    dates: int
    enriched: bool
    warnings: list[str]


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def iter_root_entries() -> list[Path]:
    entries: list[Path] = []
    for readme in sorted(ROOT.glob("*/README.md")):
        text = readme.read_text(encoding="utf-8", errors="replace")
        if ROOT_ENTRY_MARKER in text:
            entries.append(readme)
    return entries


def looks_enriched(text: str) -> bool:
    if "|---" in text and FACT_LABEL_RE.search(text):
        return True
    if len(text.strip()) > 900 and "Root-level journal entry folder for visual browsing." not in text:
        return True
    return False


def analyze(path: Path) -> RootEntryReport:
    text = path.read_text(encoding="utf-8", errors="replace")
    urls = sorted(set(URL_RE.findall(text)))
    dates = DATE_RE.findall(text)
    enriched = looks_enriched(text)

    warnings: list[str] = []
    if not CANONICAL_RE.search(text):
        warnings.append("missing canonical skill line")
    if not SKILL_NAME_RE.search(text):
        warnings.append("missing skill name line")
    if not BUNDLE_RE.search(text):
        warnings.append("missing bundle line")
    if list(path.parent.rglob("SKILL.md")):
        warnings.append("root entry contains SKILL.md")
    if enriched and not urls:
        warnings.append("enriched card has no external URL")
    if enriched and FACT_LABEL_RE.search(text) and not dates:
        warnings.append("enriched factual card has no visible check date")

    return RootEntryReport(
        path=rel(path),
        chars=len(text.strip()),
        canonical=bool(CANONICAL_RE.search(text)),
        skill_name=bool(SKILL_NAME_RE.search(text)),
        bundle=bool(BUNDLE_RE.search(text)),
        external_urls=len(urls),
        dates=len(dates),
        enriched=enriched,
        warnings=warnings,
    )


def print_text(reports: list[RootEntryReport], show_all: bool) -> None:
    warnings = [report for report in reports if report.warnings]
    enriched = [report for report in reports if report.enriched]
    print(f"Root-entry audit scanned {len(reports)} root journal entries.")
    print(f"Enriched cards: {len(enriched)}")
    print(f"Machine-only cards: {len(reports) - len(enriched)}")
    print(f"Warnings: {len(warnings)}")

    rows = reports if show_all else warnings
    if rows:
        print()
    for report in rows:
        suffix = "; ".join(report.warnings) if report.warnings else "ok"
        state = "enriched" if report.enriched else "machine-only"
        print(
            f"- {report.path}: {state}, urls={report.external_urls}, "
            f"dates={report.dates}, chars={report.chars} [{suffix}]"
        )


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--all",
        action="store_true",
        help="print every root entry instead of only warnings",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="emit machine-readable JSON",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="exit non-zero if any root entry has warnings",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    reports = [analyze(path) for path in iter_root_entries()]
    if args.json:
        print(json.dumps([asdict(report) for report in reports], ensure_ascii=False, indent=2))
    else:
        print_text(reports, args.all)

    if args.strict and any(report.warnings for report in reports):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
