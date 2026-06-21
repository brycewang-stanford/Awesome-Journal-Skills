#!/usr/bin/env python3
"""Aggregate the monthly uplift health signals into one report.

This tool is a read-only dashboard over the existing maintenance commands. It
does not replace the hard gates; it makes the quality trajectory easy to check
before choosing the next count-preserving improvement batch.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from statistics import mean
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PYTHON = sys.executable or "python3"
CLAIMS_PATH = ROOT / ".maintenance" / "CLAIMS.md"
CLAIM_ROW_RE = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|")

AGENT_A_KEYWORDS = (
    "accounting",
    "administrative-science",
    "association-for-information",
    "business",
    "china",
    "chinese",
    "consumer",
    "econom",
    "entrepreneur",
    "finance",
    "financial",
    "human-relations",
    "informs",
    "mis",
    "management",
    "marketing",
    "money",
    "operations",
    "organization",
    "organis",
    "research-policy",
    "risk",
    "uncertainty",
)
AGENT_B_EXACT_PACKS = {
    "Annals-of-Mathematics",
    "Cancer-Cell",
    "Cell",
    "JAMA",
    "Journal-of-the-American-Chemical-Society",
    "Lancet",
    "NEJM",
    "Physical-Review-Letters",
    "PNAS",
    "Science",
}
AGENT_C_KEYWORDS = (
    "anthropolog",
    "art-bulletin",
    "communication",
    "criminology",
    "critical-inquiry",
    "demography",
    "educational",
    "geography",
    "historical",
    "marriage-and-family",
    "mind",
    "politic",
    "psycholog",
    "public-opinion",
    "religion",
    "social-forces",
    "sociolog",
)


class ToolError(RuntimeError):
    def __init__(self, command: list[str], returncode: int, stdout: str, stderr: str) -> None:
        self.command = command
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr
        super().__init__(f"{' '.join(command)} failed with exit code {returncode}")


def run(command: list[str]) -> str:
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)
    if result.returncode:
        raise ToolError(command, result.returncode, result.stdout, result.stderr)
    return result.stdout


def parse_counts(text: str) -> dict[str, int]:
    fields = {
        "skills": r"EXPECTED_SKILL_COUNT\s*=\s*(\d+)",
        "packs": r"EXPECTED_PACK_COUNT\s*=\s*(\d+)",
        "root_entries": r"EXPECTED_ROOT_JOURNAL_ENTRIES\s*=\s*(\d+)",
    }
    counts: dict[str, int] = {}
    for key, pattern in fields.items():
        match = re.search(pattern, text)
        if not match:
            raise ValueError(f"Could not parse {key} from audit_repo.py --counts output")
        counts[key] = int(match.group(1))
    return counts


def score_summary(rows: list[dict[str, Any]], target: float, limit: int) -> dict[str, Any]:
    scores = [float(row["score"]) for row in rows]
    worst = sorted(rows, key=lambda row: (float(row["score"]), str(row["pack"])))[:limit]
    return {
        "pack_count": len(rows),
        "mean": round(mean(scores), 1) if scores else 0.0,
        "min": round(min(scores), 1) if scores else 0.0,
        "below_target": sum(score < target for score in scores),
        "worst": worst,
    }


def source_summary(rows: list[dict[str, Any]], limit: int) -> dict[str, Any]:
    warnings = [row for row in rows if row.get("warnings")]
    sorted_rows = sorted(rows, key=lambda row: int(row["unresolved_flags"]), reverse=True)
    return {
        "map_count": len(rows),
        "warnings": len(warnings),
        "max_unresolved": int(sorted_rows[0]["unresolved_flags"]) if sorted_rows else 0,
        "highest_unresolved": sorted_rows[:limit],
    }


def weakest_skill_path(row: dict[str, Any]) -> str:
    weak = row.get("weak_skills") or []
    if not weak:
        return ""
    first = weak[0]
    return str(first.get("path", "")) if isinstance(first, dict) else ""


def root_summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    warnings = [row for row in rows if row.get("warnings")]
    enriched = [row for row in rows if row.get("enriched")]
    return {
        "entry_count": len(rows),
        "enriched": len(enriched),
        "machine_only": len(rows) - len(enriched),
        "warnings": len(warnings),
    }


def pack_from_path(path: str) -> str:
    return str(path).split("/", 1)[0]


def pack_base_name(pack: str) -> str:
    return pack.removesuffix("-Skills")


def read_claims_context() -> dict[str, Any]:
    if not CLAIMS_PATH.exists():
        return {"present": False, "path": ".maintenance/CLAIMS.md", "rows": {}, "text": ""}

    text = CLAIMS_PATH.read_text(encoding="utf-8")
    rows: dict[str, dict[str, str]] = {}
    for line in text.splitlines():
        match = CLAIM_ROW_RE.match(line)
        if not match:
            continue
        pack, agent, status = (part.strip() for part in match.groups())
        if pack in {"Pack", "------"} or set(pack) == {"-"}:
            continue
        rows[pack] = {"agent": agent, "status": status}
    return {"present": True, "path": ".maintenance/CLAIMS.md", "rows": rows, "text": text}


def active_claim_status(status: str) -> bool:
    normalized = status.strip().lower()
    if normalized in {"done", "n/a"}:
        return False
    return any(marker in normalized for marker in ("in progress", "queued", "uncommitted", "待验收"))


def active_claim_text_near_pack(base: str, claims_text: str) -> bool:
    text_lower = claims_text.lower()
    aliases = {base.lower(), base.lower().replace("-", " ")}
    for alias in sorted(aliases, key=len, reverse=True):
        start = text_lower.find(alias)
        while start != -1:
            window = text_lower[max(0, start - 700) : start + len(alias) + 700]
            if any(marker in window for marker in ("in progress", "queued", "uncommitted", "待验收")):
                return True
            start = text_lower.find(alias, start + len(alias))
    return False


def claim_reason_for_pack(pack: str, claims: dict[str, Any]) -> str:
    if not claims.get("present"):
        return ""

    rows: dict[str, dict[str, str]] = claims["rows"]
    base = pack_base_name(pack)
    row = rows.get(pack) or rows.get(base)
    if row and active_claim_status(row["status"]):
        return f"Claims table: {row['agent']} status {row['status']}"

    text_lower = str(claims.get("text", "")).lower()
    base_lower = base.lower()
    if "agent a" in text_lower and any(keyword in base_lower for keyword in AGENT_A_KEYWORDS):
        return "Agent A lane covers econ/finance/management/Chinese packs"
    if "agent b" in text_lower and base in AGENT_B_EXACT_PACKS:
        return "Agent B lane covers this natural-science/medicine pack"
    if "agent c" in text_lower and any(keyword in base_lower for keyword in AGENT_C_KEYWORDS):
        return "Agent C social-science/humanities lane is marked uncommitted or awaiting review"
    if active_claim_text_near_pack(base, str(claims.get("text", ""))):
        return "Claims text mentions this pack in an active, queued, uncommitted, or awaiting-review lane"
    return ""


def claims_summary(
    quality: dict[str, Any],
    source_maps: dict[str, Any],
    claims: dict[str, Any],
) -> dict[str, Any]:
    sensitive_packs: dict[str, str] = {}
    current_targets: list[dict[str, str]] = []

    for row in quality["worst"]:
        pack = str(row["pack"])
        reason = claim_reason_for_pack(pack, claims)
        if reason:
            sensitive_packs[pack] = reason
            current_targets.append({"kind": "score-floor", "pack": pack, "reason": reason})

    for row in source_maps["highest_unresolved"]:
        pack = pack_from_path(str(row["path"]))
        reason = claim_reason_for_pack(pack, claims)
        if reason:
            sensitive_packs[pack] = reason
            current_targets.append({"kind": "source-map", "pack": pack, "reason": reason})

    return {
        "path": claims["path"],
        "present": bool(claims.get("present")),
        "sensitive_packs": sensitive_packs,
        "sensitive_current_targets": current_targets,
    }


CLONE_PAIR_RE = re.compile(r"^- ([0-9.]+) \[([^]]+)] (.+) <=> (.+)$")


def clone_summary(text: str, fail_threshold: float, limit: int) -> dict[str, Any]:
    pairs: list[dict[str, Any]] = []
    for line in text.splitlines():
        match = CLONE_PAIR_RE.match(line)
        if not match:
            continue
        pairs.append(
            {
                "score": float(match.group(1)),
                "group": match.group(2),
                "left": match.group(3),
                "right": match.group(4),
            }
        )
    return {
        "reported_pairs": len(pairs),
        "max_score": round(max((pair["score"] for pair in pairs), default=0.0), 3),
        "fail_hits": sum(pair["score"] >= fail_threshold for pair in pairs),
        "top_pairs": pairs[:limit],
    }


def candidate_pool(
    quality_rows: list[dict[str, Any]],
    source_rows: list[dict[str, Any]],
    claims: dict[str, Any],
    limit: int,
) -> dict[str, list[dict[str, Any]]]:
    score_candidates: list[dict[str, Any]] = []
    for row in sorted(quality_rows, key=lambda item: (float(item["score"]), str(item["pack"]))):
        pack = str(row["pack"])
        if claim_reason_for_pack(pack, claims):
            continue
        score_candidates.append(
            {
                "score": float(row["score"]),
                "pack": pack,
                "weakest_skill": weakest_skill_path(row),
            }
        )
        if len(score_candidates) >= limit:
            break

    source_candidates: list[dict[str, Any]] = []
    sorted_source_rows = sorted(source_rows, key=lambda item: int(item["unresolved_flags"]), reverse=True)
    for row in sorted_source_rows:
        unresolved = int(row["unresolved_flags"])
        if unresolved <= 0:
            break
        path = str(row["path"])
        if claim_reason_for_pack(pack_from_path(path), claims):
            continue
        source_candidates.append({"unresolved_flags": unresolved, "path": path})
        if len(source_candidates) >= limit:
            break

    return {
        "score_unclaimed": score_candidates,
        "source_map_unclaimed": source_candidates,
    }


def git_status() -> dict[str, Any]:
    result = subprocess.run(
        ["git", "status", "--short", "--branch", "--untracked-files=all"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode:
        raise ToolError(
            ["git", "status", "--short", "--branch", "--untracked-files=all"],
            result.returncode,
            result.stdout,
            result.stderr,
        )
    lines = result.stdout.strip().splitlines()
    return {
        "branch": lines[0] if lines else "",
        "dirty_lines": lines[1:],
    }


def build_summary(args: argparse.Namespace) -> dict[str, Any]:
    counts = parse_counts(run([PYTHON, "tools/audit_repo.py", "--counts"]))
    quality_rows = json.loads(run([PYTHON, "tools/quality_scorecard.py", "--json"]))
    source_rows = json.loads(run([PYTHON, "tools/source_map_audit.py", "--json"]))
    root_rows = json.loads(run([PYTHON, "tools/root_entry_audit.py", "--json"]))
    quality = score_summary(quality_rows, args.score_target, args.limit)
    source_maps = source_summary(source_rows, args.limit)
    claims_context = read_claims_context()
    claims = claims_summary(quality, source_maps, claims_context)
    clone = None
    if not args.skip_clone:
        clone_output = run(
            [
                PYTHON,
                "tools/clone_audit.py",
                "--threshold",
                f"{args.clone_threshold:.3f}",
                "--fail-threshold",
                f"{args.clone_fail_threshold:.3f}",
                "--top",
                str(args.clone_top),
            ]
        )
        clone = clone_summary(clone_output, args.clone_fail_threshold, args.limit)

    return {
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "counts": counts,
        "quality": quality,
        "source_maps": source_maps,
        "root_entries": root_summary(root_rows),
        "clone_audit": clone,
        "claims": claims,
        "candidate_pool": candidate_pool(quality_rows, source_rows, claims_context, args.limit),
        "git": git_status(),
        "targets": {
            "score_floor": args.score_target,
            "clone_fail_threshold": args.clone_fail_threshold,
            "display_limit": args.limit,
        },
    }


def status_label(ok: bool, skipped: bool = False) -> str:
    if skipped:
        return "Skipped"
    return "OK" if ok else "Review"


def readiness_rows(summary: dict[str, Any]) -> list[tuple[str, str, str]]:
    quality = summary["quality"]
    source_maps = summary["source_maps"]
    root_entries = summary["root_entries"]
    clone = summary["clone_audit"]
    git = summary["git"]
    target = summary["targets"]["score_floor"]

    rows = [
        (
            "Score floor",
            status_label(int(quality["below_target"]) == 0),
            f"min {quality['min']}, below {target:g}: {quality['below_target']}",
        ),
        (
            "Source-map warnings",
            status_label(int(source_maps["warnings"]) == 0),
            f"{source_maps['warnings']} warnings; max unresolved {source_maps['max_unresolved']}",
        ),
        (
            "Root-card warnings",
            status_label(int(root_entries["warnings"]) == 0 and int(root_entries["machine_only"]) == 0),
            f"{root_entries['warnings']} warnings; {root_entries['machine_only']} machine-only cards",
        ),
    ]
    if clone is None:
        rows.append(("Clone fail threshold", status_label(False, skipped=True), "clone audit skipped"))
    else:
        fail_threshold = summary["targets"]["clone_fail_threshold"]
        rows.append(
            (
                "Clone fail threshold",
                status_label(int(clone["fail_hits"]) == 0),
                f"{clone['fail_hits']} hits >= {fail_threshold:g}; {clone['reported_pairs']} reported pairs",
            )
        )
    rows.append(
        (
            "Working tree review",
            status_label(len(git["dirty_lines"]) == 0),
            f"{git['branch']}; {len(git['dirty_lines'])} dirty entries",
        )
    )
    return rows


def pack_list(rows: list[dict[str, Any]], limit: int = 3) -> str:
    return ", ".join(str(row["pack"]) for row in rows[:limit])


def source_map_list(rows: list[dict[str, Any]], limit: int = 3) -> str:
    return ", ".join(f"`{row['path']}`" for row in rows[:limit])


def claim_pack_reason(summary: dict[str, Any], pack: str) -> str:
    return str(summary.get("claims", {}).get("sensitive_packs", {}).get(pack, ""))


def unclaimed_score_rows(summary: dict[str, Any]) -> list[dict[str, Any]]:
    return list(summary.get("candidate_pool", {}).get("score_unclaimed", []))


def unclaimed_source_rows(summary: dict[str, Any]) -> list[dict[str, Any]]:
    return list(summary.get("candidate_pool", {}).get("source_map_unclaimed", []))


def next_batches(summary: dict[str, Any]) -> list[str]:
    quality = summary["quality"]
    source_maps = summary["source_maps"]
    root_entries = summary["root_entries"]
    clone = summary["clone_audit"]
    target = summary["targets"]["score_floor"]

    batches: list[str] = []
    score_candidates = unclaimed_score_rows(summary)
    if int(quality["below_target"]) > 0:
        if score_candidates:
            batches.append(
                f"Restore the score floor by deepening below-{target:g} packs first; "
                f"start with {pack_list(score_candidates)}."
            )
        else:
            batches.append(
                f"The below-{target:g} score-floor candidates are claim-sensitive; get owner clearance before editing them."
            )
    else:
        if score_candidates:
            batches.append(
                "Protect the score floor by sampling the current unclaimed bottom band before expansion work: "
                f"{pack_list(score_candidates)}."
            )
        else:
            batches.append(
                "Current bottom-band packs are claim-sensitive; keep the score floor under monitoring "
                "and prefer tooling or owner-cleared content work."
            )

    if int(source_maps["warnings"]) > 0:
        batches.append("Fix source-map structural warnings before chasing lower-priority unresolved flags.")
    elif int(source_maps["max_unresolved"]) > 0:
        source_candidates = unclaimed_source_rows(summary)
        if source_candidates:
            batches.append(
                "Reduce unresolved source-map flags only where official sources are reachable; "
                f"current unclaimed top targets: {source_map_list(source_candidates)}."
            )
        else:
            batches.append(
                "Current top source-map debt is claim-sensitive; skip it unless the owning lane clears the pack."
            )
    else:
        batches.append("Keep source-map audit in the final gate; no unresolved source-map debt is currently reported.")

    if int(root_entries["warnings"]) > 0 or int(root_entries["machine_only"]) > 0:
        batches.append("Repair root-card provenance before any homepage or gallery changes.")
    else:
        batches.append("Leave root cards alone unless `root_entry_audit.py` reports a new warning.")

    if clone is None:
        batches.append("Run clone audit before choosing a clone-risk batch; this snapshot skipped it.")
    elif int(clone["fail_hits"]) > 0:
        batches.append("Treat clone fail-threshold hits as the next urgent cleanup batch.")
    elif int(clone["reported_pairs"]) > 0:
        top_pair = clone["top_pairs"][0]
        batches.append(
            "Differentiate the top reported clone pair with real venue-routing substance: "
            f"`{top_pair['left']}` <=> `{top_pair['right']}`."
        )
    else:
        batches.append("Keep clone audit as a regression gate; no pairs currently report at the configured threshold.")

    batches.append("Before staging, re-read `.maintenance/CLAIMS.md` and use path-scoped `git add` only.")
    return batches


def markdown(summary: dict[str, Any]) -> str:
    counts = summary["counts"]
    quality = summary["quality"]
    source_maps = summary["source_maps"]
    root_entries = summary["root_entries"]
    clone = summary["clone_audit"]
    claims = summary["claims"]
    git = summary["git"]
    target = summary["targets"]["score_floor"]

    lines = [
        "# Monthly Uplift Health Snapshot",
        "",
        f"Generated: {summary['generated_at']}",
        "",
        "## Summary",
        "",
        "| Signal | Current |",
        "|---|---:|",
        f"| Inventory | {counts['skills']} skills / {counts['packs']} packs / {counts['root_entries']} root entries |",
        f"| Quality scorecard | mean {quality['mean']}, min {quality['min']}, below {target:g}: {quality['below_target']} |",
        f"| Source maps | {source_maps['map_count']} maps, {source_maps['warnings']} warnings, max unresolved {source_maps['max_unresolved']} |",
        f"| Root entries | {root_entries['enriched']} enriched, {root_entries['machine_only']} machine-only, {root_entries['warnings']} warnings |",
    ]
    if clone is None:
        lines.append("| Clone audit | skipped |")
    else:
        lines.append(
            f"| Clone audit | max reported {clone['max_score']:.3f}, fail hits {clone['fail_hits']}, reported pairs {clone['reported_pairs']} |"
        )
    lines.append(f"| Git status | {git['branch']} with {len(git['dirty_lines'])} dirty entries |")

    lines.extend(["", "## Goal-readiness Signals", "", "| Check | Status | Evidence |", "|---|---|---|"])
    for check, status, evidence in readiness_rows(summary):
        lines.append(f"| {check} | {status} | {evidence} |")

    lines.extend(["", "## Lowest Scorecard Packs", "", "| Score | Pack | Weakest skill |", "|---:|---|---|"])
    for row in quality["worst"]:
        weakest = weakest_skill_path(row)
        lines.append(f"| {float(row['score']):.1f} | {row['pack']} | `{weakest}` |")

    lines.extend(["", "## Highest Source-map Unresolved Flags", "", "| Flags | Source map |", "|---:|---|"])
    for row in source_maps["highest_unresolved"]:
        lines.append(f"| {int(row['unresolved_flags'])} | `{row['path']}` |")

    if claims["sensitive_current_targets"]:
        lines.extend(["", "## Claim-sensitive Current Targets", "", "| Target | Pack | Reason |", "|---|---|---|"])
        for target in claims["sensitive_current_targets"]:
            reason = str(target["reason"]).replace("|", "/")
            lines.append(f"| {target['kind']} | `{target['pack']}` | {reason} |")

    candidate_pool_data = summary.get("candidate_pool", {})
    score_candidates = candidate_pool_data.get("score_unclaimed", [])
    source_candidates = candidate_pool_data.get("source_map_unclaimed", [])
    if score_candidates or source_candidates:
        lines.extend(
            [
                "",
                "## Unclaimed Candidate Pool",
                "",
                "These are selected from the full audit outputs, not just the displayed top rows; re-check claims before editing.",
            ]
        )
        if score_candidates:
            lines.extend(["", "| Score | Pack | Weakest skill |", "|---:|---|---|"])
            for row in score_candidates:
                lines.append(f"| {float(row['score']):.1f} | {row['pack']} | `{row['weakest_skill']}` |")
        if source_candidates:
            lines.extend(["", "| Flags | Source map |", "|---:|---|"])
            for row in source_candidates:
                lines.append(f"| {int(row['unresolved_flags'])} | `{row['path']}` |")

    if clone is not None:
        lines.extend(["", "## Top Clone Pairs", "", "| Score | Group | Pair |", "|---:|---|---|"])
        if clone["top_pairs"]:
            for pair in clone["top_pairs"]:
                lines.append(
                    f"| {pair['score']:.3f} | {pair['group']} | `{pair['left']}` <=> `{pair['right']}` |"
                )
        else:
            lines.append("| n/a | n/a | No clone pairs reported at the requested threshold. |")

    if git["dirty_lines"]:
        lines.extend(["", "## Dirty Working Tree", "", "```text", *git["dirty_lines"], "```"])

    lines.extend(["", "## Next Count-preserving Batches", ""])
    for batch in next_batches(summary):
        lines.append(f"- {batch}")
    lines.append("- Re-run `python3 tools/run_checks.py --skip-reports` before handoff or publish.")
    return "\n".join(lines) + "\n"


def positive_int(value: str) -> int:
    try:
        number = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("must be an integer") from exc
    if number < 1:
        raise argparse.ArgumentTypeError("must be at least 1")
    return number


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="emit the aggregate summary as JSON")
    parser.add_argument("--skip-clone", action="store_true", help="skip the slower clone-audit summary")
    parser.add_argument(
        "--limit",
        type=positive_int,
        default=5,
        help="number of low-score, high-source-map, claim-sensitive, clone, and unclaimed-candidate rows to display",
    )
    parser.add_argument("--clone-top", type=int, default=40, help="number of clone pairs to request")
    parser.add_argument("--clone-threshold", type=float, default=0.75, help="clone reporting threshold")
    parser.add_argument("--clone-fail-threshold", type=float, default=0.90, help="clone failure threshold")
    parser.add_argument("--score-target", type=float, default=90.0, help="score floor target to summarize")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    try:
        summary = build_summary(args)
    except (ToolError, ValueError, json.JSONDecodeError) as exc:
        print(f"monthly_uplift_report failed: {exc}", file=sys.stderr)
        if isinstance(exc, ToolError):
            if exc.stdout:
                print(exc.stdout, file=sys.stderr)
            if exc.stderr:
                print(exc.stderr, file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        print(markdown(summary), end="")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
