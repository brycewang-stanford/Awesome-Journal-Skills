#!/usr/bin/env python3
"""Set one version across every manifest a pack owns, plus the root marketplace.

A pack's version is written in four places that ``audit_repo.py`` requires to agree:

1. ``<pack>/.claude-plugin/plugin.json`` → ``version``
2. ``<pack>/.claude-plugin/marketplace.json`` → ``version``
3. ``<pack>/.claude-plugin/marketplace.json`` → ``plugins[].version``
4. ``.claude-plugin/marketplace.json`` (root) → ``plugins[].version``

Editing those by hand across ~300 packs is how versions drift. Imported third-party
packs are left alone.

Usage:
    python3 tools/set_version.py --set 1.0.0
    python3 tools/set_version.py --set 1.1.0 --pack Research-Toolkit-Skills
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from venue_lib import IMPORTED, ROOT

ROOT_MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def first_party_packs() -> list[Path]:
    return [
        plugin.parent.parent
        for plugin in sorted(ROOT.glob("*/.claude-plugin/plugin.json"))
        if plugin.parent.parent.name not in IMPORTED
    ]


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--set", dest="version", required=True, help="semver to write")
    parser.add_argument("--pack", action="append", default=None,
                        help="limit to these pack directories (repeatable)")
    args = parser.parse_args(argv)

    if not SEMVER.match(args.version):
        print(f"FAIL: {args.version!r} is not a semver like 1.0.0", file=sys.stderr)
        return 1

    packs = first_party_packs()
    if args.pack:
        wanted = set(args.pack)
        packs = [p for p in packs if p.name in wanted]
        missing = wanted - {p.name for p in packs}
        if missing:
            print(f"FAIL: unknown pack(s): {', '.join(sorted(missing))}", file=sys.stderr)
            return 1

    touched = set()
    for pack in packs:
        plugin_path = pack / ".claude-plugin" / "plugin.json"
        plugin = load(plugin_path)
        plugin["version"] = args.version
        dump(plugin_path, plugin)

        market_path = pack / ".claude-plugin" / "marketplace.json"
        if market_path.exists():
            market = load(market_path)
            if "version" in market:
                market["version"] = args.version
            for entry in market.get("plugins", []):
                entry["version"] = args.version
            dump(market_path, market)
        touched.add(pack.name)

    root = load(ROOT_MARKETPLACE)
    updated = 0
    for entry in root.get("plugins", []):
        source = entry.get("source", "").lstrip("./").rstrip("/")
        if source in touched:
            entry["version"] = args.version
            updated += 1
    dump(ROOT_MARKETPLACE, root)

    print(f"set version {args.version} on {len(touched)} pack(s); "
          f"{updated} root marketplace entries updated")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
