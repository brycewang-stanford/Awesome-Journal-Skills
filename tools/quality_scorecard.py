#!/usr/bin/env python3
"""Per-pack quality scorecard for Awesome Journal Skills.

Objective, dependency-free scoring of every first-party skill pack so the
maintenance team can SEE where depth/capability work pays off, instead of
guessing. Complements tools/audit_repo.py (which is pass/fail correctness) and
tools/clone_audit.py (which is similarity). This tool is a *report*: it never
fails CI by itself, but the JSON it emits can be diffed over time to track the
repo's quality trajectory.

Usage:
  python3 tools/quality_scorecard.py                # full table, worst first
  python3 tools/quality_scorecard.py --top 20       # 20 lowest-scoring packs
  python3 tools/quality_scorecard.py --json         # machine-readable
  python3 tools/quality_scorecard.py --min-score 70 # exit 1 if any pack < 70
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Imported submodule packs are out of scope: we don't own their content.
IMPORTED_ROOTS = {
    "AER-Skills",
    "AER-skills",
    "Nature-Skills",
    "nature-skills",
    "nature-paper-skills",
    "claude-scholar",
    "codex-claude-academic-skills",
}

FRONTMATTER_DESCRIPTION_RE = re.compile(r"^description:\s*(.+)$", re.MULTILINE)
WORD_RE = re.compile(r"\S+")


def first_party_packs() -> list[Path]:
    packs = []
    for plugin in sorted(ROOT.glob("*/.claude-plugin/plugin.json")):
        pack = plugin.parent.parent
        if pack.name in IMPORTED_ROOTS:
            continue
        if (pack / "skills").is_dir():
            packs.append(pack)
    return packs


def skill_files(pack: Path) -> list[Path]:
    return sorted((pack / "skills").glob("*/SKILL.md"))


def body_after_frontmatter(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            return text[end + 4 :]
    return text


def score_pack(pack: Path) -> dict:
    skills = skill_files(pack)
    n = len(skills)
    is_breadth = n >= 50

    line_counts: list[int] = []
    word_counts: list[int] = []
    desc_lengths: list[int] = []
    desc_use_when = 0
    desc_has_journal_cue = 0
    code_block_skills = 0

    pack_token = pack.name.replace("-Skills", "").replace("-", " ").lower()
    pack_words = {w for w in pack_token.split() if len(w) > 3}

    for sf in skills:
        text = sf.read_text(encoding="utf-8", errors="replace")
        body = body_after_frontmatter(text)
        line_counts.append(body.count("\n") + 1)
        word_counts.append(len(WORD_RE.findall(body)))
        if "```" in body:
            code_block_skills += 1
        m = FRONTMATTER_DESCRIPTION_RE.search(text)
        if m:
            desc = m.group(1).strip()
            desc_lengths.append(len(desc))
            low = desc.lower()
            if "use when" in low or "use this" in low or "用于" in low or "当" in low:
                desc_use_when += 1
            # journal-specificity cue: the description names (part of) the venue
            if any(w in low for w in pack_words):
                desc_has_journal_cue += 1

    res = pack / "resources"
    has_code = (res / "code").is_dir()
    has_worked = (res / "worked-examples").is_dir()
    has_exemplars = (res / "exemplars").is_dir()
    has_resources_readme = (res / "README.md").exists()
    has_source_map = (res / "official-source-map.md").exists()
    has_external = (res / "external_tools.md").exists()
    has_roster = any((res / name).exists() for name in ("conference-roster.md", "journal-roster.md", "source-basis.md"))
    has_readme = (pack / "README.md").exists()
    has_readme_zh = (pack / "README.zh-CN.md").exists()
    has_router = any("workflow" in sf.parent.name or "router" in sf.parent.name for sf in skills)

    avg_words = sum(word_counts) / n if n else 0
    avg_desc = sum(desc_lengths) / len(desc_lengths) if desc_lengths else 0

    # ---- composite score (0-100) ----
    # Depth: SKILL bodies that actually carry substance. Depth packs are scored
    # against a flagship ~700 words/skill target; breadth packs are scored
    # against shorter profile cards plus strong routing resources.
    depth = min(35, (avg_words / (350 if is_breadth else 600)) * 35)
    # Trigger precision: descriptions that say WHEN and name the venue.
    trigger = 0.0
    if n:
        trigger += min(8, (avg_desc / 200) * 8)
        trigger += (desc_use_when / n) * 4
        trigger += (desc_has_journal_cue / n) * 8
    # Resources / capability assets. Breadth bundles should not be penalized for
    # lacking a depth-pack code library; their capability layer is routing,
    # roster/source discipline, worked routing examples, and selection patterns.
    if is_breadth:
        resources = (
            (6 if has_resources_readme else 0)
            + (8 if has_worked else 0)
            + (6 if has_exemplars else 0)
            + (5 if has_source_map else 0)
            + (3 if has_roster else 0)
        )
    else:
        resources = (
            (10 if has_code else 0)
            + (8 if has_worked else 0)
            + (6 if has_exemplars else 0)
            + (3 if has_source_map else 0)
            + (1 if has_external else 0)
        )
    # Runnable code inside skill bodies (empirical capability signal).
    runnable = min(5, (code_block_skills / n) * 5) if n else 0
    # Structure hygiene.
    structure = 0.0
    if is_breadth:
        structure += 3 if n >= 50 and has_router else (1 if n else 0)
    else:
        structure += 3 if 8 <= n <= 14 else (1 if n else 0)
    structure += 1.5 if has_readme else 0
    structure += 1.5 if has_readme_zh else 0

    total = round(depth + trigger + resources + runnable + structure, 1)

    return {
        "pack": pack.name,
        "pack_type": "breadth" if is_breadth else "depth",
        "skills": n,
        "avg_words": round(avg_words),
        "avg_desc_chars": round(avg_desc),
        "desc_use_when": desc_use_when,
        "desc_journal_cue": desc_has_journal_cue,
        "code_lib": has_code,
        "worked_examples": has_worked,
        "exemplars": has_exemplars,
        "source_map": has_source_map,
        "score": total,
        "_breakdown": {
            "depth": round(depth, 1),
            "trigger": round(trigger, 1),
            "resources": resources,
            "runnable": round(runnable, 1),
            "structure": round(structure, 1),
        },
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--top", type=int, default=0, help="show only the N lowest-scoring packs")
    ap.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    ap.add_argument("--min-score", type=float, default=None, help="exit 1 if any pack scores below this")
    args = ap.parse_args()

    rows = sorted((score_pack(p) for p in first_party_packs()), key=lambda r: r["score"])

    if args.json:
        print(json.dumps(rows, ensure_ascii=False, indent=2))
    else:
        shown = rows[: args.top] if args.top else rows
        scores = [r["score"] for r in rows]
        mean = sum(scores) / len(scores) if scores else 0
        print(f"Quality scorecard — {len(rows)} first-party packs · mean score {mean:.1f}/100")
        print(f"(worst first){' · showing bottom ' + str(args.top) if args.top else ''}\n")
        hdr = f"{'score':>6}  {'type':>7} {'skl':>3} {'wrds':>5} {'desc':>4}  {'code':>4} {'wex':>3} {'exm':>3}  pack"
        print(hdr)
        print("-" * len(hdr))
        for r in shown:
            print(
                f"{r['score']:>6}  {r['pack_type']:>7} {r['skills']:>3} {r['avg_words']:>5} {r['avg_desc_chars']:>4}  "
                f"{'yes' if r['code_lib'] else '  -':>4} "
                f"{'y' if r['worked_examples'] else '-':>3} "
                f"{'y' if r['exemplars'] else '-':>3}  {r['pack']}"
            )

    if args.min_score is not None:
        below = [r for r in rows if r["score"] < args.min_score]
        if below:
            print(f"\n{len(below)} pack(s) below min-score {args.min_score}", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
