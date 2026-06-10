#!/usr/bin/env python3
"""Smoke-check an ML reproduction package for common missing files.

This is intentionally lightweight and dependency-free. It does not validate
scientific correctness; it only catches packaging gaps an agent should flag
before review or public release.
"""

from __future__ import annotations

import argparse
from pathlib import Path

README_NAMES = {"README", "README.md", "README.rst", "README.txt"}
ENV_NAMES = {
    "environment.yml",
    "environment.yaml",
    "requirements.txt",
    "pyproject.toml",
    "Pipfile",
    "poetry.lock",
    "conda.yml",
}
SCRIPT_HINTS = {"run", "train", "eval", "evaluate", "reproduce", "main", "make"}
CONFIG_DIRS = {"configs", "config", "experiments"}


def has_named(path: Path, names: set[str]) -> bool:
    return any((path / name).exists() for name in names)


def has_script(path: Path) -> bool:
    for child in path.rglob("*"):
        if not child.is_file():
            continue
        stem = child.stem.lower()
        suffix = child.suffix.lower()
        if stem in SCRIPT_HINTS or any(h in stem for h in SCRIPT_HINTS):
            if suffix in {"", ".py", ".sh", ".R", ".jl", ".ipynb", ".mk"}:
                return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package", type=Path, help="Path to the reproduction package root")
    args = parser.parse_args()

    root = args.package.resolve()
    if not root.exists() or not root.is_dir():
        print(f"ERROR: {root} is not a directory")
        return 2

    checks = [
        ("README present", has_named(root, README_NAMES)),
        ("environment/dependency file present", has_named(root, ENV_NAMES)),
        ("run/eval/reproduce script present", has_script(root)),
        ("config directory or file present", any((root / name).exists() for name in CONFIG_DIRS)),
    ]

    failures = [name for name, ok in checks if not ok]
    for name, ok in checks:
        print(f"{'PASS' if ok else 'WARN'}: {name}")

    if failures:
        print("\\nWarnings do not prove the package is unusable, but they are reviewer-risk items:")
        for item in failures:
            print(f"- {item}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
