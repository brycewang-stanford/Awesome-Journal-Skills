#!/usr/bin/env python3
"""Repository-level consistency checks for Awesome Journal Skills.

The checks are intentionally dependency-free so they can run in CI and on a
fresh clone.
"""

from __future__ import annotations

import json
import re
import sys
import urllib.parse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

# Tripwire counts: these guard against accidental bulk deletion or stray
# additions. When you intentionally add/remove packs, update these three values
# (and the README badges) in the same commit. Run `python3 tools/audit_repo.py
# --counts` to print the live numbers to copy in.
EXPECTED_SKILL_COUNT = 2902
EXPECTED_PACK_COUNT = 195
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

README_FILES = [ROOT / "README.md", ROOT / "README.en.md"]
CHINESE_DEPTH_PACKS_REQUIRING_SOURCE_MAPS = {
    "Accounting-Research-Skills",
    "China-Economic-Quarterly-Skills",
    "China-Industrial-Economics-Skills",
    "China-Rural-Economy-Skills",
    "Chinese-Public-Administration-Skills",
    "Economic-Research-Journal-Skills",
    "Journal-of-Finance-and-Economics-Skills",
    "Journal-of-Financial-Research-Skills",
    "Journal-of-Management-Sciences-in-China-Skills",
    "Journal-of-Management-World-Skills",
    "Journal-of-Quantitative-and-Technological-Economics-Skills",
    "Journal-of-World-Economy-Skills",
    "Nankai-Business-Review-Skills",
    "Social-Sciences-in-China-Skills",
    "Sociological-Studies-Skills",
}
ROOT_ENTRY_MARKER = "AJS-ROOT-JOURNAL-ENTRY"
LINK_RE = re.compile(
    r"(?<!!)\[[^\]]*]\(([^)]+)\)"
    r"|<a\s+[^>]*href=[\"']([^\"']+)[\"']"
    r"|<img\s+[^>]*src=[\"']([^\"']+)[\"']",
    re.IGNORECASE,
)
FENCE_RE = re.compile(r"^\s*(```|~~~)")
INLINE_CODE_RE = re.compile(r"`[^`]*`")
FRONTMATTER_KEY_RE = re.compile(r"^([A-Za-z0-9_-]+):", re.MULTILINE)
FRONTMATTER_NAME_RE = re.compile(r"^name:\s*[\"']?([^\"'\n]+)", re.MULTILINE)
FRONTMATTER_DESCRIPTION_RE = re.compile(r"^description:\s*\S+", re.MULTILINE)
ROOT_CANONICAL_RE = re.compile(r"^- Canonical skill:\s*\[[^\]]+]\(([^)]+)\)", re.MULTILINE)
ROOT_SKILL_NAME_RE = re.compile(r"^- Skill name:\s*`([^`]+)`", re.MULTILINE)
ROOT_BUNDLE_RE = re.compile(r"^- Bundle:\s*\[[^\]]+]\(([^)]+)\)", re.MULTILINE)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def is_hidden_or_git(path: Path) -> bool:
    return any(part == ".git" for part in path.parts)


def is_nature_plugin_mirror(path: Path) -> bool:
    parts = [part.casefold() for part in path.relative_to(ROOT).parts]
    return len(parts) >= 4 and parts[:3] == ["nature-skills", "plugins", "nature-skills"]


def is_imported_root(path: Path) -> bool:
    return top_level(path) in IMPORTED_ROOTS


def iter_skill_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("SKILL.md")
        if not is_hidden_or_git(path) and not is_nature_plugin_mirror(path)
    )


def top_level(path: Path) -> str:
    return path.relative_to(ROOT).parts[0]


def first_party_plugin_roots() -> list[Path]:
    return sorted(
        path.parent.parent
        for path in ROOT.glob("*/.claude-plugin/plugin.json")
        if path.parent.parent.is_dir() and top_level(path) not in IMPORTED_ROOTS
    )


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

    pack_roots = set(first_party_plugin_roots())
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


def check_external_import_policy(errors: list[str]) -> None:
    gitmodules = ROOT / ".gitmodules"
    if gitmodules.exists():
        errors.append(f"{rel(gitmodules)} must not exist; third-party packs are external links")

    submodule_workflow = ROOT / ".github" / "workflows" / "sync-submodules.yml"
    if submodule_workflow.exists():
        errors.append(
            f"{rel(submodule_workflow)} must not exist; this index no longer vendors submodules"
        )

    for name in sorted(IMPORTED_ROOTS):
        path = ROOT / name
        if path.exists():
            errors.append(f"{name}/ must stay external-only, not vendored into this repository")


def resolve_local_link(base: Path, target: str) -> Path:
    target = target.split("#", 1)[0].split("?", 1)[0]
    return (base / urllib.parse.unquote(target)).resolve()


def check_root_journal_entries(errors: list[str]) -> None:
    for readme in sorted(ROOT.glob("*/README.md")):
        text = readme.read_text(encoding="utf-8", errors="replace")
        if ROOT_ENTRY_MARKER not in text:
            continue

        entry_root = readme.parent
        canonical_match = ROOT_CANONICAL_RE.search(text)
        skill_name_match = ROOT_SKILL_NAME_RE.search(text)
        bundle_match = ROOT_BUNDLE_RE.search(text)

        if not canonical_match:
            errors.append(f"{rel(readme)}: root journal entry missing canonical skill link")
            continue
        if not skill_name_match:
            errors.append(f"{rel(readme)}: root journal entry missing skill name")
            continue
        if not bundle_match:
            errors.append(f"{rel(readme)}: root journal entry missing bundle link")
            continue

        canonical = resolve_local_link(entry_root, canonical_match.group(1))
        bundle = resolve_local_link(entry_root, bundle_match.group(1))
        skill_name = skill_name_match.group(1).strip()

        try:
            canonical.relative_to(ROOT)
            bundle.relative_to(ROOT)
        except ValueError:
            errors.append(f"{rel(readme)}: root journal entry links outside repository")
            continue

        skill_file = canonical / "SKILL.md"
        if not skill_file.exists():
            errors.append(f"{rel(readme)}: canonical skill target lacks SKILL.md")
            continue
        if canonical.name != skill_name:
            errors.append(
                f"{rel(readme)}: skill name {skill_name!r} != canonical folder {canonical.name!r}"
            )
        if not bundle.exists() or not bundle.is_dir():
            errors.append(f"{rel(readme)}: bundle target does not exist")
        else:
            try:
                canonical.relative_to(bundle / "skills")
            except ValueError:
                errors.append(
                    f"{rel(readme)}: canonical skill is not under declared bundle's skills/"
                )

        frontmatter = skill_file.read_text(encoding="utf-8", errors="replace")
        name_match = FRONTMATTER_NAME_RE.search(frontmatter)
        if name_match and name_match.group(1).strip() != skill_name:
            errors.append(
                f"{rel(readme)}: skill name {skill_name!r} "
                f"!= canonical frontmatter {name_match.group(1).strip()!r}"
            )


def check_readme_badges(errors: list[str]) -> None:
    for path in README_FILES:
        text = path.read_text(encoding="utf-8")
        if str(EXPECTED_SKILL_COUNT) not in text:
            errors.append(f"{rel(path)} does not mention expected skill count {EXPECTED_SKILL_COUNT}")
        if str(EXPECTED_PACK_COUNT) not in text:
            errors.append(f"{rel(path)} does not mention expected pack count {EXPECTED_PACK_COUNT}")


def check_root_marketplace(errors: list[str]) -> None:
    marketplace_path = ROOT / ".claude-plugin" / "marketplace.json"
    marketplace = load_json(marketplace_path, errors)
    if not marketplace:
        return

    entries = marketplace.get("plugins")
    if not isinstance(entries, list):
        errors.append(f"{rel(marketplace_path)} plugins must be a list")
        return

    expected_roots = {rel(path) for path in first_party_plugin_roots()}
    seen_roots: set[str] = set()
    seen_names: set[str] = set()

    if len(entries) != len(expected_roots):
        errors.append(
            f"{rel(marketplace_path)} expected {len(expected_roots)} plugin entries, "
            f"found {len(entries)}"
        )

    for index, entry in enumerate(entries, 1):
        if not isinstance(entry, dict):
            errors.append(f"{rel(marketplace_path)} plugins[{index}] must be an object")
            continue

        name = str(entry.get("name") or "").strip()
        source = str(entry.get("source") or "").strip()
        if not name:
            errors.append(f"{rel(marketplace_path)} plugins[{index}] missing name")
        elif name in seen_names:
            errors.append(f"{rel(marketplace_path)} duplicate plugin name {name!r}")
        else:
            seen_names.add(name)

        if not source.startswith("./"):
            errors.append(f"{rel(marketplace_path)} plugin {name or index!r} source must start with './'")
            continue

        source_root = source[2:].rstrip("/")
        source_path = ROOT / source_root
        if source_root in IMPORTED_ROOTS:
            errors.append(f"{rel(marketplace_path)} plugin {name!r} points to external import {source_root!r}")
            continue
        if source_root in seen_roots:
            errors.append(f"{rel(marketplace_path)} duplicate plugin source {source!r}")
        else:
            seen_roots.add(source_root)
        if not source_path.is_dir():
            errors.append(f"{rel(marketplace_path)} plugin {name!r} source {source!r} does not exist")
            continue

        plugin_path = source_path / ".claude-plugin" / "plugin.json"
        plugin = load_json(plugin_path, errors)
        if not plugin:
            continue
        if name and name != plugin.get("name"):
            errors.append(
                f"{rel(marketplace_path)} plugin {source!r} name {name!r} "
                f"!= {rel(plugin_path)} {plugin.get('name')!r}"
            )
        version = entry.get("version")
        if version != plugin.get("version"):
            errors.append(
                f"{rel(marketplace_path)} plugin {name!r} version {version!r} "
                f"!= {rel(plugin_path)} {plugin.get('version')!r}"
            )

    missing = sorted(expected_roots - seen_roots)
    extra = sorted(seen_roots - expected_roots)
    if missing or extra:
        errors.append(
            f"{rel(marketplace_path)} source coverage drift: "
            f"missing={missing or []}, extra={extra or []}"
        )


def check_plugin_metadata(errors: list[str]) -> None:
    for plugin_path in sorted(ROOT.glob("*/.claude-plugin/plugin.json")):
        pack_root = plugin_path.parent.parent
        if top_level(plugin_path) in IMPORTED_ROOTS:
            continue
        plugin = load_json(plugin_path, errors)
        marketplace_path = plugin_path.parent / "marketplace.json"
        if not marketplace_path.exists():
            errors.append(f"{rel(marketplace_path)} is missing")
            continue
        marketplace = load_json(marketplace_path, errors)
        if not plugin or not marketplace:
            continue

        plugin_version = plugin.get("version")
        if not plugin_version:
            errors.append(f"{rel(plugin_path)} missing version")

        if plugin.get("name") != marketplace.get("name"):
            errors.append(
                f"{rel(marketplace_path)} name {marketplace.get('name')!r} "
                f"!= plugin.json {plugin.get('name')!r}"
            )

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
        if entry.get("name") != plugin.get("name"):
            errors.append(
                f"{rel(marketplace_path)} plugin entry name {entry.get('name')!r} "
                f"!= plugin.json {plugin.get('name')!r}"
            )
        if entry.get("version") != plugin_version:
            errors.append(
                f"{rel(marketplace_path)} plugin entry version {entry.get('version')!r} "
                f"!= plugin.json {plugin_version!r}"
            )
        if entry.get("license") != plugin.get("license"):
            errors.append(
                f"{rel(marketplace_path)} plugin entry license {entry.get('license')!r} "
                f"!= plugin.json {plugin.get('license')!r}"
            )

        actual = sorted(
            f"skills/{path.parent.name}"
            for path in (pack_root / "skills").glob("*/SKILL.md")
        )
        declared = sorted(entry.get("skills") or [])
        if actual and not declared:
            errors.append(f"{rel(marketplace_path)} plugin entry has no declared skills")
        elif declared and actual and actual != declared:
            missing = sorted(set(actual) - set(declared))
            extra = sorted(set(declared) - set(actual))
            errors.append(
                f"{rel(marketplace_path)} skills list drift: "
                f"missing={missing or []}, extra={extra or []}"
            )


def check_pack_documentation(errors: list[str]) -> None:
    for plugin_path in sorted(ROOT.glob("*/.claude-plugin/plugin.json")):
        pack_root = plugin_path.parent.parent
        if top_level(plugin_path) in IMPORTED_ROOTS:
            continue

        for name in ("README.md", "README.zh-CN.md", "LICENSE"):
            if not (pack_root / name).exists():
                errors.append(f"{rel(pack_root)} missing {name}")


def check_source_maps(errors: list[str]) -> None:
    for pack_name in sorted(CHINESE_DEPTH_PACKS_REQUIRING_SOURCE_MAPS):
        source_map = ROOT / pack_name / "resources" / "official-source-map.md"
        if not source_map.exists():
            errors.append(f"{rel(source_map)} is missing")
            continue

        text = source_map.read_text(encoding="utf-8", errors="replace")
        if len(text.strip()) < 400:
            errors.append(f"{rel(source_map)} is too short to be a useful source map")
        if not re.search(r"https?://", text):
            errors.append(f"{rel(source_map)} has no source URL")
        if not re.search(r"\b20\d{2}-\d{2}(?:-\d{2})?\b", text):
            errors.append(f"{rel(source_map)} has no visible access/check date")


def check_skill_frontmatter(errors: list[str]) -> None:
    first_party_names: dict[str, list[Path]] = {}

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
        name_match = FRONTMATTER_NAME_RE.search(frontmatter)
        if not name_match:
            errors.append(f"{rel(path)}: frontmatter missing name")
        if not FRONTMATTER_DESCRIPTION_RE.search(frontmatter):
            errors.append(f"{rel(path)}: frontmatter missing description")

        if is_imported_root(path):
            continue

        keys = FRONTMATTER_KEY_RE.findall(frontmatter)
        extra_keys = sorted(set(keys) - {"name", "description"})
        if extra_keys:
            errors.append(f"{rel(path)}: first-party frontmatter has extra keys {extra_keys}")

        if name_match:
            name = name_match.group(1).strip()
            first_party_names.setdefault(name, []).append(path)
            if name != path.parent.name:
                errors.append(
                    f"{rel(path)}: frontmatter name {name!r} != folder {path.parent.name!r}"
                )

    for name, paths in sorted(first_party_names.items()):
        if len(paths) > 1:
            locations = ", ".join(rel(path) for path in paths)
            errors.append(f"duplicate first-party skill name {name!r}: {locations}")


def markdown_files_to_check() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if not is_hidden_or_git(path) and not is_imported_root(path)
    )


def iter_markdown_link_lines(text: str) -> list[tuple[int, str]]:
    lines: list[tuple[int, str]] = []
    in_fence = False

    for lineno, line in enumerate(text.splitlines(), 1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        lines.append((lineno, INLINE_CODE_RE.sub("", line)))

    return lines


def is_external_target(target: str) -> bool:
    lowered = target.lower()
    return lowered.startswith(("http://", "https://", "mailto:", "data:")) or target.startswith("#")


def check_markdown_links(errors: list[str]) -> None:
    for path in markdown_files_to_check():
        text = path.read_text(encoding="utf-8", errors="replace")
        for lineno, line in iter_markdown_link_lines(text):
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


def print_live_counts() -> int:
    skill_count = len(iter_skill_files())
    pack_roots = set(first_party_plugin_roots())
    root_entries = sum(
        1
        for path in ROOT.glob("*/README.md")
        if ROOT_ENTRY_MARKER in path.read_text(encoding="utf-8", errors="replace")
    )
    print("Live repository inventory (copy into the EXPECTED_* tripwires + README badges):")
    print(f"  EXPECTED_SKILL_COUNT          = {skill_count}")
    print(f"  EXPECTED_PACK_COUNT           = {len(pack_roots)}")
    print(f"  EXPECTED_ROOT_JOURNAL_ENTRIES = {root_entries}")
    return 0


def main() -> int:
    if "--counts" in sys.argv[1:]:
        return print_live_counts()
    errors: list[str] = []
    check_counts(errors)
    check_external_import_policy(errors)
    check_root_journal_entries(errors)
    check_readme_badges(errors)
    check_root_marketplace(errors)
    check_plugin_metadata(errors)
    check_pack_documentation(errors)
    check_source_maps(errors)
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
