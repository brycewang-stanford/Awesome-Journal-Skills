#!/usr/bin/env python3
"""SkillOpt-style validation gate for count-preserving skill edits.

The upstream SkillOpt loop treats a skill document as trainable text, proposes
bounded edits, then keeps a candidate only if held-out validation improves. This
repository cannot always run model rollouts for every journal pack, so this tool
turns the existing local audit stack into a deterministic proxy gate:

  snapshot -> bounded edit -> gate against the snapshot

The gate is conservative by default: inventory counts must stay fixed, hard
checks must pass, score-floor signals must not regress, warning counts must not
increase, clone fail hits must remain zero, and edits inside claim-sensitive pack
directories are blocked unless explicitly allowed.
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
COUNTS_RE = {
    "skills": re.compile(r"EXPECTED_SKILL_COUNT\s*=\s*(\d+)"),
    "packs": re.compile(r"EXPECTED_PACK_COUNT\s*=\s*(\d+)"),
    "root_entries": re.compile(r"EXPECTED_ROOT_JOURNAL_ENTRIES\s*=\s*(\d+)"),
}
CLONE_PAIR_RE = re.compile(r"^- ([0-9.]+) \[([^]]+)] (.+) <=> (.+)$")

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


def run_capture(command: list[str], *, allow_failure: bool = False) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)
    if result.returncode and not allow_failure:
        raise ToolError(command, result.returncode, result.stdout, result.stderr)
    return result


def parse_counts(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for key, pattern in COUNTS_RE.items():
        match = pattern.search(text)
        if not match:
            raise ValueError(f"Could not parse {key} from audit_repo.py --counts output")
        counts[key] = int(match.group(1))
    return counts


def quality_summary(rows: list[dict[str, Any]], score_target: float) -> dict[str, Any]:
    scores = [float(row["score"]) for row in rows]
    worst = sorted(rows, key=lambda row: (float(row["score"]), str(row["pack"])))[:10]
    return {
        "pack_count": len(rows),
        "mean": round(mean(scores), 3) if scores else 0.0,
        "min": round(min(scores), 3) if scores else 0.0,
        "below_target": sum(score < score_target for score in scores),
        "worst": [
            {
                "pack": str(row["pack"]),
                "score": float(row["score"]),
                "weakest_skill": (row.get("weak_skills") or [{}])[0].get("path", ""),
            }
            for row in worst
        ],
    }


def source_summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    warnings = [row for row in rows if row.get("warnings")]
    max_unresolved = max((int(row["unresolved_flags"]) for row in rows), default=0)
    return {
        "map_count": len(rows),
        "warnings": len(warnings),
        "max_unresolved": max_unresolved,
    }


def root_summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    warnings = [row for row in rows if row.get("warnings")]
    enriched = [row for row in rows if row.get("enriched")]
    return {
        "entry_count": len(rows),
        "enriched": len(enriched),
        "machine_only": len(rows) - len(enriched),
        "warnings": len(warnings),
    }


def clone_summary(text: str, fail_threshold: float) -> dict[str, Any]:
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
        "top_pairs": pairs[:10],
    }


def git_status() -> dict[str, Any]:
    result = run_capture(["git", "status", "--short", "--branch", "--untracked-files=all"])
    lines = result.stdout.strip().splitlines()
    return {"branch": lines[0] if lines else "", "dirty_lines": lines[1:]}


def changed_paths() -> list[str]:
    result = run_capture(["git", "diff", "--name-only"])
    cached = run_capture(["git", "diff", "--cached", "--name-only"])
    untracked = run_capture(["git", "ls-files", "--others", "--exclude-standard"])
    paths = {
        line.strip()
        for line in (result.stdout + cached.stdout + untracked.stdout).splitlines()
        if line.strip()
    }
    return sorted(paths)


def read_claim_rows() -> tuple[dict[str, dict[str, str]], str]:
    if not CLAIMS_PATH.exists():
        return {}, ""
    text = CLAIMS_PATH.read_text(encoding="utf-8", errors="replace")
    rows: dict[str, dict[str, str]] = {}
    for line in text.splitlines():
        match = CLAIM_ROW_RE.match(line)
        if not match:
            continue
        pack, agent, status = (part.strip() for part in match.groups())
        if pack in {"Pack", "------"} or set(pack) == {"-"}:
            continue
        rows[pack] = {"agent": agent, "status": status}
    return rows, text


def active_claim_status(status: str) -> bool:
    normalized = status.strip().lower()
    if normalized in {"done", "n/a"}:
        return False
    return any(marker in normalized for marker in ("in progress", "queued", "uncommitted", "待验收"))


def pack_base(pack: str) -> str:
    return pack.removesuffix("-Skills")


def claim_reason_for_pack(pack: str, rows: dict[str, dict[str, str]], claims_text: str) -> str:
    base = pack_base(pack)
    row = rows.get(pack) or rows.get(base)
    if row and active_claim_status(row["status"]):
        return f"Claims table: {row['agent']} status {row['status']}"

    text_lower = claims_text.lower()
    base_lower = base.lower()
    if "agent a" in text_lower and any(keyword in base_lower for keyword in AGENT_A_KEYWORDS):
        return "Agent A lane covers econ/finance/management/Chinese packs"
    if "agent b" in text_lower and base in AGENT_B_EXACT_PACKS:
        return "Agent B lane covers this natural-science/medicine pack"
    if "agent c" in text_lower and any(keyword in base_lower for keyword in AGENT_C_KEYWORDS):
        return "Agent C social-science/humanities lane is marked uncommitted or awaiting review"
    return ""


def claim_sensitive_changed_packs(paths: list[str]) -> list[dict[str, str]]:
    rows, text = read_claim_rows()
    sensitive: list[dict[str, str]] = []
    seen: set[str] = set()
    for path in paths:
        top = path.split("/", 1)[0]
        if not top.endswith("-Skills") or top in seen:
            continue
        seen.add(top)
        reason = claim_reason_for_pack(top, rows, text)
        if reason:
            sensitive.append({"pack": top, "reason": reason})
    return sensitive


def collect_snapshot(args: argparse.Namespace) -> dict[str, Any]:
    quality_rows = json.loads(run_capture([PYTHON, "tools/quality_scorecard.py", "--json"]).stdout)
    source_rows = json.loads(run_capture([PYTHON, "tools/source_map_audit.py", "--json"]).stdout)
    root_rows = json.loads(run_capture([PYTHON, "tools/root_entry_audit.py", "--json"]).stdout)
    clone = None
    if not args.skip_clone:
        clone_output = run_capture(
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
        ).stdout
        clone = clone_summary(clone_output, args.clone_fail_threshold)

    paths = changed_paths()
    return {
        "schema": "ajs-skillopt-gate-v1",
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "score_target": args.score_target,
        "clone_threshold": args.clone_threshold,
        "clone_fail_threshold": args.clone_fail_threshold,
        "counts": parse_counts(run_capture([PYTHON, "tools/audit_repo.py", "--counts"]).stdout),
        "quality": quality_summary(quality_rows, args.score_target),
        "source_maps": source_summary(source_rows),
        "root_entries": root_summary(root_rows),
        "clone_audit": clone,
        "git": git_status(),
        "changed_paths": paths,
        "claim_sensitive_changed_packs": claim_sensitive_changed_packs(paths),
    }


def load_snapshot(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema") != "ajs-skillopt-gate-v1":
        raise ValueError(f"{path} is not an ajs-skillopt-gate-v1 snapshot")
    return data


def add_check(checks: list[dict[str, Any]], name: str, ok: bool, evidence: str) -> None:
    checks.append({"name": name, "ok": ok, "evidence": evidence})


def compare_snapshots(
    baseline: dict[str, Any],
    candidate: dict[str, Any],
    args: argparse.Namespace,
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []

    add_check(
        checks,
        "Inventory counts",
        args.allow_count_change or candidate["counts"] == baseline["counts"],
        f"baseline {baseline['counts']} -> candidate {candidate['counts']}",
    )
    add_check(
        checks,
        "Quality minimum",
        float(candidate["quality"]["min"]) + args.score_epsilon >= float(baseline["quality"]["min"]),
        f"baseline {baseline['quality']['min']} -> candidate {candidate['quality']['min']}",
    )
    add_check(
        checks,
        "Quality below-target count",
        int(candidate["quality"]["below_target"]) <= int(baseline["quality"]["below_target"]),
        f"baseline {baseline['quality']['below_target']} -> candidate {candidate['quality']['below_target']}",
    )
    add_check(
        checks,
        "Source-map warnings",
        int(candidate["source_maps"]["warnings"]) <= int(baseline["source_maps"]["warnings"]),
        f"baseline {baseline['source_maps']['warnings']} -> candidate {candidate['source_maps']['warnings']}",
    )
    add_check(
        checks,
        "Root-card warnings",
        int(candidate["root_entries"]["warnings"]) <= int(baseline["root_entries"]["warnings"]),
        f"baseline {baseline['root_entries']['warnings']} -> candidate {candidate['root_entries']['warnings']}",
    )
    add_check(
        checks,
        "Root-card machine-only count",
        int(candidate["root_entries"]["machine_only"]) <= int(baseline["root_entries"]["machine_only"]),
        f"baseline {baseline['root_entries']['machine_only']} -> candidate {candidate['root_entries']['machine_only']}",
    )

    clone = candidate.get("clone_audit")
    if clone is None:
        add_check(checks, "Clone fail threshold", True, "clone audit skipped by user")
    else:
        add_check(
            checks,
            "Clone fail threshold",
            int(clone["fail_hits"]) == 0,
            f"{clone['fail_hits']} hits >= {candidate['clone_fail_threshold']}",
        )

    sensitive = candidate.get("claim_sensitive_changed_packs") or []
    add_check(
        checks,
        "Claim-sensitive pack edits",
        args.allow_claimed_pack or not sensitive,
        "none" if not sensitive else "; ".join(f"{row['pack']}: {row['reason']}" for row in sensitive),
    )
    return checks


def run_hard_checks() -> dict[str, Any]:
    result = run_capture([PYTHON, "tools/run_checks.py", "--skip-reports"], allow_failure=True)
    return {
        "command": f"{PYTHON} tools/run_checks.py --skip-reports",
        "returncode": result.returncode,
        "stdout_tail": "\n".join(result.stdout.splitlines()[-25:]),
        "stderr_tail": "\n".join(result.stderr.splitlines()[-25:]),
    }


def print_gate_report(report: dict[str, Any]) -> None:
    print("# SkillOpt Gate Report")
    print()
    print(f"Generated: {report['candidate']['generated_at']}")
    print(f"Result: {'PASS' if report['passed'] else 'FAIL'}")
    print()
    print("| Check | Status | Evidence |")
    print("|---|---|---|")
    for check in report["checks"]:
        evidence = str(check["evidence"]).replace("|", "/")
        print(f"| {check['name']} | {'OK' if check['ok'] else 'Review'} | {evidence} |")

    hard = report.get("hard_checks")
    if hard:
        print()
        print("## Hard Checks")
        print()
        print(f"- Command: `{hard['command']}`")
        print(f"- Exit code: {hard['returncode']}")
        if hard["stdout_tail"]:
            print()
            print("```text")
            print(hard["stdout_tail"])
            print("```")
        if hard["stderr_tail"]:
            print()
            print("```text")
            print(hard["stderr_tail"])
            print("```")


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def add_common_options(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--score-target", type=float, default=90.0, help="score floor target")
    parser.add_argument("--skip-clone", action="store_true", help="skip clone_audit.py in the snapshot")
    parser.add_argument("--clone-threshold", type=float, default=0.75, help="clone audit reporting threshold")
    parser.add_argument("--clone-fail-threshold", type=float, default=0.90, help="clone audit fail threshold")
    parser.add_argument("--clone-top", type=int, default=20, help="clone audit top-pair display count")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)

    snap = sub.add_parser("snapshot", help="write a baseline or candidate snapshot")
    add_common_options(snap)
    snap.add_argument("--out", required=True, help="path to write JSON snapshot")

    gate = sub.add_parser("gate", help="compare current state with a baseline snapshot")
    add_common_options(gate)
    gate.add_argument("--baseline", required=True, help="baseline JSON from the snapshot subcommand")
    gate.add_argument("--out", help="optional JSON report path")
    gate.add_argument("--allow-count-change", action="store_true", help="allow inventory count changes")
    gate.add_argument("--allow-claimed-pack", action="store_true", help="allow edits in claim-sensitive pack dirs")
    gate.add_argument(
        "--score-epsilon",
        type=float,
        default=0.0,
        help="allowed tiny score-min decrease for floating-point churn",
    )
    gate.add_argument(
        "--no-run-checks",
        action="store_true",
        help="skip tools/run_checks.py --skip-reports during gate evaluation",
    )

    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    try:
        if args.cmd == "snapshot":
            snapshot = collect_snapshot(args)
            write_json((ROOT / args.out).resolve(), snapshot)
            print(f"Wrote SkillOpt gate snapshot to {args.out}")
            return 0

        baseline = load_snapshot((ROOT / args.baseline).resolve())
        candidate = collect_snapshot(args)
        checks = compare_snapshots(baseline, candidate, args)
        hard_checks = None
        if not args.no_run_checks:
            hard_checks = run_hard_checks()
            add_check(
                checks,
                "Repository hard checks",
                int(hard_checks["returncode"]) == 0,
                f"{hard_checks['command']} exited {hard_checks['returncode']}",
            )
        passed = all(bool(check["ok"]) for check in checks)
        report = {
            "schema": "ajs-skillopt-gate-report-v1",
            "passed": passed,
            "checks": checks,
            "baseline": baseline,
            "candidate": candidate,
            "hard_checks": hard_checks,
        }
        if args.out:
            write_json((ROOT / args.out).resolve(), report)
        print_gate_report(report)
        return 0 if passed else 1
    except (ToolError, ValueError, json.JSONDecodeError) as exc:
        print(f"skillopt_gate.py: {exc}", file=sys.stderr)
        if isinstance(exc, ToolError):
            if exc.stdout:
                print(exc.stdout, file=sys.stderr)
            if exc.stderr:
                print(exc.stderr, file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
