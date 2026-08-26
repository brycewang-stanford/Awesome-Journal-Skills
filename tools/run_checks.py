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
        # The unit suite runs first: it is offline, takes under a second, and every
        # check below it depends on the text and retrieval layers it covers. A syntax
        # check was the only thing standing behind these tools before it existed.
        ["python3", "-m", "unittest", "discover", "-s", "tools/tests", "-t", "tools"],
        ["python3", "tools/audit_repo.py"],
        # Conformance is the gate: every pack must meet every structural requirement.
        # The backlog score below it is a ranking, not a standard, so its floor is set
        # well under the current minimum (51.5) — low enough that only a genuinely
        # broken new pack trips it, and it is not a target to be optimised against.
        [
            "python3", "tools/quality_scorecard.py", "--top", "15",
            "--require-conformance", "--min-score", "40",
        ],
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
        [
            "python3", "tools/freshness_audit.py", "--check",
            "--max-age-days", "365", "--max-unknown", "0",
        ],
        # Freshness says when a source map was re-read; this says which conference
        # edition it was re-read about. `--max-stale 0` is a hard gate because a past
        # edition is unambiguous — the meeting happened, so the page caps, chairs and
        # deadlines in the pack belong to a cycle no reader can still submit to. The
        # softer `due` state stays advisory: whether this year's edition has met is
        # a fact most source maps never state.
        ["python3", "tools/cycle_audit.py", "--check", "--max-stale", "0"],
        # The subject vocabulary is harvested over the network, so it is committed and
        # never rebuilt here. What CI can check offline is the half that goes wrong
        # silently: the postings address venues by row number, so a topic file built
        # against a different venue ordering parses cleanly and attributes every term to
        # the wrong venue. The digest catches that; `match_lib` refuses the same
        # mismatch at load time, and this makes it a failing build instead of a failing
        # run.
        ["python3", "tools/fetch_venue_topics.py", "--check"],
        # Retrieval floor: an index or matcher regression fails the build instead of
        # quietly degrading every venue recommendation. Measured on the gold set's
        # held-out `test` half, and set a few points below the current headline (65.3%)
        # so normal content churn does not trip it. Raise it when the headline rises.
        #
        # It also now guards something the headline alone would not. Roughly half of that
        # figure comes from `topic-postings.tsv`, which is harvested over the network and
        # committed; a truncated or half-finished harvest would leave the file valid, the
        # digest correct, and the recommendations quietly a third worse. A floor at 0.60
        # is above anything the scope index can reach on its own (46.7%), so a build that
        # passes it has a subject vocabulary that actually arrived.
        ["python3", "tools/eval_journal_match.py", "--min-recall-at-10", "0.60"],
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
