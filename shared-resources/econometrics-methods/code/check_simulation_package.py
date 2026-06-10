#!/usr/bin/env python3
"""Smoke-check an econometrics simulation or replication package layout."""

from __future__ import annotations

import argparse
from pathlib import Path

README_NAMES = {"README", "README.md", "README.txt", "readme.md"}
ENV_NAMES = {
    "requirements.txt",
    "environment.yml",
    "environment.yaml",
    "pyproject.toml",
    "renv.lock",
    "DESCRIPTION",
    "stata.trk",
}
MASTER_HINTS = {"master", "run_all", "main", "simulate", "monte", "replicate", "make"}
DATA_DIRS = {"data", "input", "raw", "processed"}
OUTPUT_DIRS = {"output", "outputs", "results", "tables", "figures"}


def exists_named(root: Path, names: set[str]) -> bool:
    return any((root / name).exists() for name in names)


def has_master_script(root: Path) -> bool:
    for child in root.rglob("*"):
        if not child.is_file():
            continue
        stem = child.stem.lower()
        suffix = child.suffix.lower()
        if any(hint in stem for hint in MASTER_HINTS) and suffix in {
            ".py",
            ".R",
            ".do",
            ".m",
            ".jl",
            ".sh",
            ".mk",
            "",
        }:
            return True
    return False


def has_seed_note(root: Path) -> bool:
    for child in root.rglob("*"):
        if not child.is_file() or child.stat().st_size > 250_000:
            continue
        if child.suffix.lower() not in {".md", ".txt", ".py", ".R", ".do", ".jl", ".m"}:
            continue
        text = child.read_text(encoding="utf-8", errors="ignore").lower()
        if "seed" in text or "random_state" in text or "set.seed" in text or "set seed" in text:
            return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package", type=Path, help="Path to the package root")
    args = parser.parse_args()

    root = args.package.resolve()
    if not root.exists() or not root.is_dir():
        print(f"ERROR: {root} is not a directory")
        return 2

    checks = [
        ("README present", exists_named(root, README_NAMES)),
        ("environment/software file present", exists_named(root, ENV_NAMES)),
        ("master simulation or replication script present", has_master_script(root)),
        ("data/input directory or access note present", any((root / d).exists() for d in DATA_DIRS)),
        ("output/results directory present", any((root / d).exists() for d in OUTPUT_DIRS)),
        ("seed or random-state note present", has_seed_note(root)),
    ]

    failures = [name for name, ok in checks if not ok]
    for name, ok in checks:
        print(f"{'PASS' if ok else 'WARN'}: {name}")

    if failures:
        print("\\nWarnings are reviewer-risk items, not proof that the package is unusable:")
        for item in failures:
            print(f"- {item}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
