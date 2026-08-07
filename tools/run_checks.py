#!/usr/bin/env python3
"""Run the standard local maintenance checks for this repository."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def run(command: list[str]) -> int:
    printable = " ".join(command)
    print(f"\n$ {printable}", flush=True)
    result = subprocess.run(command, cwd=ROOT, check=False)
    if result.returncode:
        print(f"\nCommand failed with exit code {result.returncode}: {printable}", file=sys.stderr)
    return result.returncode


def python_tool_files() -> list[str]:
    return [rel(path) for path in sorted((ROOT / "tools").glob("*.py"))]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--skip-reports",
        action="store_true",
        help="skip report-only source-map and root-entry audits",
    )
    parser.add_argument(
        "--strict-reports",
        action="store_true",
        help="make report-only audits fail on warnings",
    )
    parser.add_argument(
        "--skip-diff-check",
        action="store_true",
        help="skip git diff --check; useful outside a git working tree",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    failures = 0

    hard_checks = [
        ["python3", "-m", "py_compile", *python_tool_files()],
        ["python3", "tools/audit_repo.py"],
        ["python3", "tools/quality_scorecard.py", "--top", "15", "--min-score", "94"],
        [
            "python3",
            "tools/clone_audit.py",
            "--threshold",
            "0.75",
            "--fail-threshold",
            "0.90",
            "--top",
            "20",
        ],
        # Generated data must match a fresh build, so a new pack cannot silently
        # leave the matcher, the ladder, the eval or the catalog behind.
        ["python3", "tools/gen_venue_index.py", "--check"],
        ["python3", "tools/gen_ladder.py", "--check"],
        ["python3", "tools/build_eval_set.py", "--check"],
        ["python3", "tools/gen_catalog.py", "--check"],
        ["python3", "tools/freshness_audit.py", "--check"],
        # Retrieval floor: an index or matcher regression fails the build instead of
        # quietly degrading every venue recommendation. Measured on the gold set's
        # held-out `test` half, and set below the current headline (40.5%) so normal
        # content churn does not trip it. Raise it when the headline rises.
        ["python3", "tools/eval_journal_match.py", "--min-recall-at-10", "0.36"],
    ]
    if not args.skip_diff_check:
        hard_checks.append(["git", "diff", "--check"])

    for command in hard_checks:
        failures += 1 if run(command) else 0

    if not args.skip_reports:
        report_suffix = ["--strict"] if args.strict_reports else []
        for command in (
            ["python3", "tools/source_map_audit.py", *report_suffix],
            ["python3", "tools/root_entry_audit.py", *report_suffix],
        ):
            failures += 1 if run(command) else 0

    if failures:
        print(f"\n{failures} check(s) failed.", file=sys.stderr)
        return 1

    print("\nAll hard checks passed.")
    if not args.skip_reports and not args.strict_reports:
        print("Report-only audits may still list warnings above.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
