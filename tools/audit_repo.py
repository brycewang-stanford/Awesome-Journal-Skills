#!/usr/bin/env python3
"""Repository-level consistency checks for Awesome Journal Skills.

The checks are intentionally dependency-free so they can run in CI and on a
fresh clone with first-level submodules populated.
"""

from __future__ import annotations

import json
import re
import sys
import urllib.parse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

EXPECTED_SKILL_COUNT = 844
EXPECTED_PACK_COUNT = 44
EXPECTED_ROOT_JOURNAL_ENTRIES = 200

IMPORTED_ROOTS = {
    "AER-Skills",
    "AER-skills",
    "Nature-Skills",
    "nature-skills",
    "nature-paper-skills",
    "claude-scholar",
    "codex-claude-academic-skills",
}

README_FILES = [ROOT / "README.md", ROOT / "README.zh-CN.md"]
ROOT_ENTRY_MARKER = "AJS-ROOT-JOURNAL-ENTRY"
LINK_RE = re.compile(
    r"(?<!!)\[[^\]]*]\(([^)]+)\)"
    r"|<a\s+[^>]*href=[\"']([^\"']+)[\"']"
    r"|<img\s+[^>]*src=[\"']([^\"']+)[\"']",
    re.IGNORECASE,
)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def is_hidden_or_git(path: Path) -> bool:
    return any(part == ".git" for part in path.parts)


def is_nature_plugin_mirror(path: Path) -> bool:
    parts = [part.casefold() for part in path.relative_to(ROOT).parts]
    return len(parts) >= 4 and parts[:3] == ["nature-skills", "plugins", "nature-skills"]


def iter_skill_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("SKILL.md")
        if not is_hidden_or_git(path) and not is_nature_plugin_mirror(path)
    )


def top_level(path: Path) -> str:
    return path.relative_to(ROOT).parts[0]


def load_json(path: Path, errors: list[str]) -> dict | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - report any parse/read issue.
        errors.append(f"{rel(path)}: invalid JSON: {exc}")
        return None


def check_counts(errors: list[str]) -> None:
    skill_count = len(iter_skill_files())
    if skill_count != EXPECTED_SKILL_COUNT:
        errors.append(f"expected {EXPECTED_SKILL_COUNT} canonical SKILL.md files, found {skill_count}")

    pack_roots = {
        path.parent.parent
        for path in ROOT.glob("*/.claude-plugin/plugin.json")
        if path.parent.parent.is_dir()
    }
    for extra in ("nature-paper-skills", "codex-claude-academic-skills"):
        root = ROOT / extra
        if any(root.rglob("SKILL.md")):
            pack_roots.add(root)
    if len(pack_roots) != EXPECTED_PACK_COUNT:
        names = ", ".join(sorted(rel(path) for path in pack_roots))
        errors.append(f"expected {EXPECTED_PACK_COUNT} curated pack roots, found {len(pack_roots)}: {names}")

    root_entries = []
    for path in ROOT.glob("*/README.md"):
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if ROOT_ENTRY_MARKER in text:
            root_entries.append(path)
            skills = list(path.parent.rglob("SKILL.md"))
            if skills:
                errors.append(f"{rel(path.parent)} is a root journal entry but contains SKILL.md")
    if len(root_entries) != EXPECTED_ROOT_JOURNAL_ENTRIES:
        errors.append(
            f"expected {EXPECTED_ROOT_JOURNAL_ENTRIES} root journal entries, found {len(root_entries)}"
        )


def check_readme_badges(errors: list[str]) -> None:
    for path in README_FILES:
        text = path.read_text(encoding="utf-8")
        if str(EXPECTED_SKILL_COUNT) not in text:
            errors.append(f"{rel(path)} does not mention expected skill count {EXPECTED_SKILL_COUNT}")
        if str(EXPECTED_PACK_COUNT) not in text:
            errors.append(f"{rel(path)} does not mention expected pack count {EXPECTED_PACK_COUNT}")


def check_plugin_metadata(errors: list[str]) -> None:
    for plugin_path in sorted(ROOT.glob("*/.claude-plugin/plugin.json")):
        pack_root = plugin_path.parent.parent
        if top_level(plugin_path) in IMPORTED_ROOTS:
            continue
        plugin = load_json(plugin_path, errors)
        marketplace_path = plugin_path.parent / "marketplace.json"
        marketplace = load_json(marketplace_path, errors) if marketplace_path.exists() else None
        if not plugin or not marketplace:
            continue

        plugin_version = plugin.get("version")
        market_version = marketplace.get("version")
        if market_version is not None and market_version != plugin_version:
            errors.append(
                f"{rel(marketplace_path)} version {market_version!r} != plugin.json {plugin_version!r}"
            )

        entries = marketplace.get("plugins") or []
        if len(entries) != 1:
            errors.append(f"{rel(marketplace_path)} should contain exactly one plugin entry")
            continue

        entry = entries[0]
        if entry.get("version") != plugin_version:
            errors.append(
                f"{rel(marketplace_path)} plugin entry version {entry.get('version')!r} "
                f"!= plugin.json {plugin_version!r}"
            )

        actual = sorted(
            f"skills/{path.parent.name}"
            for path in (pack_root / "skills").glob("*/SKILL.md")
        )
        declared = sorted(entry.get("skills") or [])
        if declared and actual and actual != declared:
            missing = sorted(set(actual) - set(declared))
            extra = sorted(set(declared) - set(actual))
            errors.append(
                f"{rel(marketplace_path)} skills list drift: "
                f"missing={missing or []}, extra={extra or []}"
            )


def check_skill_frontmatter(errors: list[str]) -> None:
    for path in iter_skill_files():
        text = path.read_text(encoding="utf-8", errors="replace")
        if not text.startswith("---\n"):
            errors.append(f"{rel(path)}: missing YAML frontmatter")
            continue
        end = text.find("\n---", 4)
        if end == -1:
            errors.append(f"{rel(path)}: unterminated YAML frontmatter")
            continue
        frontmatter = text[4:end]
        if not re.search(r"^name:\s*\S+", frontmatter, re.MULTILINE):
            errors.append(f"{rel(path)}: frontmatter missing name")
        if not re.search(r"^description:\s*\S+", frontmatter, re.MULTILINE):
            errors.append(f"{rel(path)}: frontmatter missing description")


def markdown_files_to_check() -> list[Path]:
    files = set(README_FILES)
    files.update((ROOT / ".maintenance").glob("*.md"))
    for path in ROOT.glob("*/README*.md"):
        if top_level(path) in IMPORTED_ROOTS:
            continue
        files.add(path)
    return sorted(files)


def is_external_target(target: str) -> bool:
    lowered = target.lower()
    return lowered.startswith(("http://", "https://", "mailto:", "data:")) or target.startswith("#")


def check_markdown_links(errors: list[str]) -> None:
    for path in markdown_files_to_check():
        text = path.read_text(encoding="utf-8", errors="replace")
        for lineno, line in enumerate(text.splitlines(), 1):
            for match in LINK_RE.finditer(line):
                target = next(group for group in match.groups() if group)
                target = target.strip()
                if not target or is_external_target(target):
                    continue
                if "<" in target or ">" in target:
                    continue
                target = target.split("#", 1)[0].split("?", 1)[0]
                if not target:
                    continue
                target = urllib.parse.unquote(target)
                resolved = (path.parent / target).resolve()
                try:
                    resolved.relative_to(ROOT)
                except ValueError:
                    continue
                if not resolved.exists():
                    errors.append(f"{rel(path)}:{lineno}: broken local link {target!r}")


def main() -> int:
    errors: list[str] = []
    check_counts(errors)
    check_readme_badges(errors)
    check_plugin_metadata(errors)
    check_skill_frontmatter(errors)
    check_markdown_links(errors)

    if errors:
        print("Repository audit failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "Repository audit passed: "
        f"{EXPECTED_SKILL_COUNT} canonical skills, "
        f"{EXPECTED_PACK_COUNT} curated packs, "
        f"{EXPECTED_ROOT_JOURNAL_ENTRIES} root journal entries."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
