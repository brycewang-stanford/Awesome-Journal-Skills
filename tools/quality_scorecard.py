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
  python3 tools/quality_scorecard.py --top 5 --show-skills
  python3 tools/quality_scorecard.py --json         # machine-readable
  python3 tools/quality_scorecard.py --min-score 70 # exit 1 if any pack < 70

The ``unit`` column is a cross-language substance measure: Latin/technical
tokens count as one unit, and two CJK characters count as one unit.
"""

from __future__ import annotations

import argparse
from collections import Counter
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# External third-party imports are out of scope: we don't own their content.
IMPORTED_ROOTS = {
    "AER-Skills",
    "AER-skills",
    "Nature-Skills",
    "nature-skills",
    "nature-paper-skills",
    "claude-scholar",
    "codex-claude-academic-skills",
}

CONFERENCE_DEPTH_PACKS = {
    "AAAI-Skills",
    "AISTATS-Skills",
    "ICLR-Skills",
    "ICML-Skills",
    "IJCAI-Skills",
    "NeurIPS-Skills",
}

TOOLKIT_PACKS = {
    "Research-Toolkit-Skills",
}

FRONTMATTER_DESCRIPTION_RE = re.compile(r"^description:\s*(.+)$", re.MULTILINE)
LATIN_TOKEN_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9_+./-]*")
CJK_RE = re.compile(r"[\u3400-\u9fff]")
NO_CODE_MARKERS = (
    "no econometric",
    "why no econometrics code",
    "why no econometric",
    "does not vendor",
    "not vendor",
    "not vendored",
    "no code kit",
    "no `code/`",
    "no vendored econometrics",
    "not an economics venue",
    "not a generic causal-inference",
    "theory venue",
    "multidisciplinary",
    "clinical",
    "humanities",
    "theorem",
    "proof architecture",
)

USE_WHEN_MARKERS = (
    "use when",
    "use this",
    "use after",
    "use before",
    "use if",
    "use for",
    "use as",
)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


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


def substance_units(text: str) -> float:
    r"""Approximate body substance across English and CJK prose.

    Whitespace word counts severely undercount Chinese skills, where a dense
    paragraph can be a single ``\S+`` token. Count Latin/technical tokens as
    words and count two CJK characters as roughly one English word-equivalent.
    """
    latin_tokens = len(LATIN_TOKEN_RE.findall(text))
    cjk_units = len(CJK_RE.findall(text)) / 2
    return latin_tokens + cjk_units


def pack_cue_words(pack: Path, skills: list[Path] | None = None) -> set[str]:
    words = [w for w in pack.name.replace("-Skills", "").replace("-", " ").lower().split() if len(w) > 2]
    cue_words = {w for w in words if len(w) > 3}
    acronym = "".join(w[0] for w in words if w not in {"and", "the", "of"})
    if len(acronym) >= 3:
        cue_words.add(acronym)
    if skills:
        prefixes = [
            sf.parent.name.split("-", 1)[0].lower()
            for sf in skills
            if "-" in sf.parent.name and 3 <= len(sf.parent.name.split("-", 1)[0]) <= 8
        ]
        for prefix, count in Counter(prefixes).items():
            if count >= max(2, len(skills) // 2):
                cue_words.add(prefix)
    return cue_words


def score_pack(pack: Path) -> dict:
    skills = skill_files(pack)
    n = len(skills)
    is_toolkit = pack.name in TOOLKIT_PACKS or pack.name.endswith("Toolkit-Skills")
    # Breadth bundles are venue-fit-card collections (one fit card per venue + a
    # router), so their capability layer is routing, not a depth-pack code library.
    # Two signals mark a breadth bundle, either of which is sufficient:
    #   1. Size: single-venue depth packs top out at ~18 skills, while most breadth
    #      bundles run from the low-30s up to 150+; a threshold of 25 sits cleanly
    #      between the two.
    #   2. A router skill named "*-journal-workflow". This is the canonical breadth
    #      router across all eight breadth bundles and never appears in a depth pack,
    #      so it correctly recognises a small focused breadth bundle (e.g. the
    #      12-journal sport-science bundle) that the size cutoff alone would miss.
    # Either signal avoids penalising a genuine breadth bundle for "missing" a
    # depth-pack code library it is not meant to ship.
    has_breadth_router = any(
        sf.parent.name.endswith("-journal-workflow") for sf in skills
    )
    is_breadth = not is_toolkit and (n >= 25 or has_breadth_router)
    is_conference_depth = pack.name in CONFERENCE_DEPTH_PACKS

    line_counts: list[int] = []
    unit_counts: list[float] = []
    desc_lengths: list[int] = []
    desc_use_when = 0
    desc_has_journal_cue = 0
    code_block_skills = 0
    exec_bridge_skills = 0
    shared_resource_skills = 0
    skill_rows: list[dict] = []

    pack_words = pack_cue_words(pack, skills)
    if is_toolkit:
        pack_words.update(
            {
                "execution",
                "journal",
                "manuscript",
                "readiness",
                "referee",
                "replication",
                "submission",
                "toolkit",
                "venue",
                "workflow",
            }
        )

    for sf in skills:
        text = sf.read_text(encoding="utf-8", errors="replace")
        body = body_after_frontmatter(text)
        line_count = body.count("\n") + 1
        unit_count = substance_units(body)
        line_counts.append(line_count)
        unit_counts.append(unit_count)
        has_code_block = "```" in body
        if "```" in body:
            code_block_skills += 1
        # Execution-bridge signal: does the skill wire guidance to the StatsPAI /
        # Stata MCP execution layer (links the shared execution-with-mcp playbook)?
        # Report-only — tracks the guidance→execution rollout; does not affect score.
        if "execution-with-mcp" in body:
            exec_bridge_skills += 1
        if "shared-resources/" in body:
            shared_resource_skills += 1
        desc = ""
        desc_len = 0
        has_use_when = False
        has_journal_cue = False
        m = FRONTMATTER_DESCRIPTION_RE.search(text)
        if m:
            desc = m.group(1).strip()
            desc_len = len(desc)
            desc_lengths.append(len(desc))
            low = desc.lower()
            if (
                any(marker in low for marker in USE_WHEN_MARKERS)
                or low.startswith("use to ")
                or "用于" in low
                or "当" in low
            ):
                desc_use_when += 1
                has_use_when = True
            # journal-specificity cue: the description names (part of) the venue
            if any(w in low for w in pack_words):
                desc_has_journal_cue += 1
                has_journal_cue = True
        skill_rows.append(
            {
                "path": rel(sf),
                "substance_units": round(unit_count),
                "lines": line_count,
                "desc_chars": desc_len,
                "desc_use_when": has_use_when,
                "desc_journal_cue": has_journal_cue,
                "code_block": has_code_block,
            }
        )

    res = pack / "resources"
    has_code = (res / "code").is_dir()
    has_worked = (res / "worked-examples").is_dir()
    has_exemplars = (res / "exemplars").is_dir()
    has_resources_readme = (res / "README.md").exists()
    has_source_map = (res / "official-source-map.md").exists()
    has_external = (res / "external_tools.md").exists()
    resources_readme_text = ""
    if has_resources_readme:
        resources_readme_text = (res / "README.md").read_text(encoding="utf-8", errors="replace").lower()
        resources_readme_text = re.sub(r"[*_`]", "", resources_readme_text)
    no_code_explained = bool(resources_readme_text) and any(marker in resources_readme_text for marker in NO_CODE_MARKERS)
    has_roster = any((res / name).exists() for name in ("conference-roster.md", "journal-roster.md", "source-basis.md"))
    has_readme = (pack / "README.md").exists()
    has_readme_zh = (pack / "README.zh-CN.md").exists()
    has_router = any("workflow" in sf.parent.name or "router" in sf.parent.name for sf in skills)

    avg_units = sum(unit_counts) / n if n else 0
    avg_desc = sum(desc_lengths) / len(desc_lengths) if desc_lengths else 0

    # ---- composite score (0-100) ----
    # Depth: SKILL bodies that actually carry substance. Journal depth packs are
    # scored against a flagship ~600 unit/skill target. Large breadth bundles,
    # toolkit packs, and compressed AI-conference depth packs have shorter,
    # routing-heavy profiles, so they use smaller targets tied to that role.
    depth_target = 300 if is_toolkit else (350 if is_breadth or is_conference_depth else 600)
    depth = min(35, (avg_units / depth_target) * 35)
    # Trigger precision: descriptions that say WHEN and name the venue.
    trigger = 0.0
    if n:
        trigger += min(8, (avg_desc / 200) * 8)
        trigger += (desc_use_when / n) * 4
        trigger += (desc_has_journal_cue / n) * 8
    # Resources / capability assets. Breadth bundles should not be penalized for
    # lacking a depth-pack code library; their capability layer is routing,
    # roster/source discipline, worked routing examples, and selection patterns.
    if is_toolkit:
        shared_coverage = (shared_resource_skills / n) if n else 0
        resources = (
            (6 if has_resources_readme else 0)
            + min(8, shared_coverage * 8)
            + (5 if has_router else 0)
            + (5 if exec_bridge_skills else 0)
            + (4 if no_code_explained else 0)
        )
    elif is_breadth:
        resources = (
            (6 if has_resources_readme else 0)
            + (8 if has_worked else 0)
            + (6 if has_exemplars else 0)
            + (5 if has_source_map else 0)
            + (3 if has_roster else 0)
        )
    else:
        source_anchor = has_source_map or has_external
        resources = (
            (10 if has_code or no_code_explained else 0)
            + (8 if has_worked else 0)
            + (6 if has_exemplars else 0)
            + (3 if source_anchor else 0)
            + (1 if has_resources_readme else 0)
        )
    # Runnable code inside skill bodies (empirical capability signal).
    runnable = min(5, (code_block_skills / n) * 5) if n else 0
    # Structure hygiene.
    structure = 0.0
    if is_toolkit:
        structure += 3 if 5 <= n <= 10 and has_router else (1 if n else 0)
    elif is_breadth:
        structure += 3 if n >= 50 and has_router else (1 if n else 0)
    else:
        structure += 3 if 8 <= n <= 14 else (1 if n else 0)
    structure += 1.5 if has_readme else 0
    structure += 1.5 if has_readme_zh else 0

    total = round(depth + trigger + resources + runnable + structure, 1)
    weak_skills = sorted(
        skill_rows,
        key=lambda row: (
            row["substance_units"],
            0 if row["desc_use_when"] else -1,
            0 if row["desc_journal_cue"] else -1,
            row["path"],
        ),
    )[:5]

    return {
        "pack": pack.name,
        "pack_type": "toolkit"
        if is_toolkit
        else ("breadth" if is_breadth else ("conference" if is_conference_depth else "depth")),
        "skills": n,
        "avg_words": round(avg_units),
        "avg_substance_units": round(avg_units),
        "avg_desc_chars": round(avg_desc),
        "desc_use_when": desc_use_when,
        "desc_journal_cue": desc_has_journal_cue,
        "code_lib": has_code,
        "code_status": "not_applicable"
        if is_breadth or is_toolkit
        else ("present" if has_code else ("not_applicable" if no_code_explained else "missing")),
        "worked_examples": has_worked,
        "exemplars": has_exemplars,
        "source_map": has_source_map,
        "exec_bridge": exec_bridge_skills > 0,
        "exec_bridge_skills": exec_bridge_skills,
        "score": total,
        "weak_skills": weak_skills,
        "_breakdown": {
            "depth": round(depth, 1),
            "depth_target": depth_target,
            "trigger": round(trigger, 1),
            "resources": resources,
            "runnable": round(runnable, 1),
            "structure": round(structure, 1),
        },
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--top", type=int, default=0, help="show only the N lowest-scoring packs")
    ap.add_argument(
        "--show-skills",
        action="store_true",
        help="under each displayed pack, show its thinnest SKILL.md files",
    )
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
        p10 = scores[int((len(scores) - 1) * 0.10)] if scores else 0
        median = scores[len(scores) // 2] if scores else 0
        low_counts = {cutoff: sum(1 for score in scores if score < cutoff) for cutoff in (86, 88, 90)}
        # Execution-bridge rollout: only depth packs that ship/justify a code library
        # are empirical candidates for wiring; breadth bundles and theory venues are not.
        empirical = [r for r in rows if r["pack_type"] == "depth" and r["code_status"] == "present"]
        wired = [r for r in empirical if r["exec_bridge"]]
        print(f"Quality scorecard — {len(rows)} first-party packs · mean score {mean:.1f}/100")
        print(
            f"Distribution: min {scores[0]:.1f} · p10 {p10:.1f} · median {median:.1f} · "
            f"below 86/88/90 = {low_counts[86]}/{low_counts[88]}/{low_counts[90]}"
        )
        pct = (len(wired) / len(empirical) * 100) if empirical else 0
        print(
            f"Execution bridge (StatsPAI/Stata MCP) wired: {len(wired)}/{len(empirical)} "
            f"empirical depth packs ({pct:.0f}%)"
        )
        print(f"(worst first){' · showing bottom ' + str(args.top) if args.top else ''}\n")
        hdr = f"{'score':>6}  {'type':>10} {'skl':>3} {'unit':>5} {'desc':>4}  {'code':>4} {'wex':>3} {'exm':>3} {'exb':>3}  pack"
        print(hdr)
        print("-" * len(hdr))
        for r in shown:
            code_label = "yes" if r["code_status"] == "present" else ("n/a" if r["code_status"] == "not_applicable" else "-")
            print(
                f"{r['score']:>6}  {r['pack_type']:>10} {r['skills']:>3} {r['avg_words']:>5} {r['avg_desc_chars']:>4}  "
                f"{code_label:>4} "
                f"{'y' if r['worked_examples'] else '-':>3} "
                f"{'y' if r['exemplars'] else '-':>3} "
                f"{'y' if r['exec_bridge'] else '-':>3}  {r['pack']}"
            )
            if args.show_skills:
                for skill in r["weak_skills"]:
                    cue = []
                    if not skill["desc_use_when"]:
                        cue.append("no-use-when")
                    if not skill["desc_journal_cue"]:
                        cue.append("no-journal-cue")
                    cue_text = f" [{', '.join(cue)}]" if cue else ""
                    print(
                        f"        - {skill['substance_units']:>4}u/{skill['desc_chars']:>3}d "
                        f"{skill['path']}{cue_text}"
                    )

    if args.min_score is not None:
        below = [r for r in rows if r["score"] < args.min_score]
        if below:
            print(f"\n{len(below)} pack(s) below min-score {args.min_score}", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
