#!/usr/bin/env python3
"""Aggregate the monthly uplift health signals into one report.

This tool is a read-only dashboard over the existing maintenance commands. When
`--output` is supplied, it also writes the rendered snapshot to disk for the
monthly worklog. It can render a full Markdown report, JSON, a compact handoff
note, or a worklog entry template, and it can check that a worklog keeps the
required loop evidence. It does not replace the hard gates; it makes the
quality trajectory easy to check before choosing the next count-preserving
improvement batch.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shlex
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
WORKLOG_HEADING_RE = re.compile(r"^### \d{4}-\d{2}-\d{2} - .+", re.MULTILINE)
WORKLOG_FILE_RE = re.compile(r"^MONTHLY-UPLIFT-(\d{4}-\d{2}-\d{2})\.md$")
WORKLOG_PLACEHOLDER_RE = re.compile(r"\[(?:describe|list|summarize|copy)[^\]]*]", re.IGNORECASE)
WORKLOG_PLANNED_EVIDENCE_RE = re.compile(
    r"("
    r"scheduled for this loop|expected to include|expected after this append|"
    r"pass expected|pending final run|pending validation|pending rerun|"
    r"should (?:pass|report|include|show)|not yet run|to be run|\bTODO\b|- \[ \]"
    r")",
    re.IGNORECASE,
)
WORKLOG_REQUIRED_MARKERS = (
    "- Scope:",
    "- Rationale:",
    "- Files:",
    "- Result:",
    "- Validation:",
)
NEXT_LOOP_VALIDATION_COMMANDS = (
    "python3 tools/monthly_uplift_report.py --check --handoff --limit 20",
    "python3 tools/monthly_uplift_report.py --check --publish-plan --limit 20",
    "python3 tools/monthly_uplift_report.py --check --goal-audit --limit 20",
    "python3 tools/monthly_uplift_report.py --check --debt-audit --limit 20",
    "python3 tools/monthly_uplift_report.py --check --worklog-template --limit 20 --output /tmp/ajs-monthly-worklog-template.md",
    "python3 tools/monthly_uplift_report.py --check-worklog latest",
    "python3 tools/monthly_uplift_report.py --check-only --limit 20 --skip-clone",
    "python3 tools/monthly_uplift_report.py --check --limit 20 --output /tmp/ajs-monthly-uplift.md",
    "python3 tools/quality_scorecard.py --top 15 --min-score 90",
    "python3 tools/run_checks.py --skip-reports",
    "python3 tools/run_checks.py",
    "git diff --check",
)
NEXT_LOOP_MEASUREMENT_COMMANDS = (
    "python3 tools/monthly_uplift_report.py --check --json --limit 20 --skip-clone --output /tmp/ajs-monthly-baseline.json",
    "python3 tools/audit_repo.py --counts",
    "python3 tools/quality_scorecard.py",
    "python3 tools/source_map_audit.py",
    "python3 tools/root_entry_audit.py",
    "python3 tools/clone_audit.py --threshold 0.75 --fail-threshold 0.90 --top 20",
    "python3 tools/external_link_audit.py --cache-summary --json",
)
DASHBOARD_SCHEMA_NAME = "monthly_uplift_report"
DASHBOARD_SCHEMA_VERSION = 25
DASHBOARD_SCHEMA_CONTRACT = "monthly-uplift-dashboard-v25"
DASHBOARD_SCHEMA_REQUIRED_TOP_LEVEL_FIELDS = (
    "schema",
    "generated_at",
    "counts",
    "quality",
    "execution_bridge",
    "source_maps",
    "root_entries",
    "external_links",
    "clone_audit",
    "claims",
    "candidate_pool",
    "loop_control",
    "worklog",
    "git",
    "worktree_boundary",
    "publish_units",
    "measurement_commands",
    "validation_commands",
    "command_plan",
    "targets",
    "owner_clearance_queue",
    "execution_bridge_tail",
    "safe_content_queue",
    "content_edit_policy",
    "remaining_debt",
    "next_batches",
    "next_batch_plan",
    "publish_policy",
    "goal_progress",
    "completion_audit",
    "handoff_manifest",
    "skillopt_gate_plan",
    "current_next_queue",
)
DASHBOARD_SCHEMA_NESTED_CONTRACT_FIELDS = (
    "external_links",
    "owner_clearance_queue",
    "execution_bridge_tail",
    "safe_content_queue",
    "content_edit_policy",
    "remaining_debt",
    "next_batch_plan",
    "publish_policy",
    "goal_progress",
    "completion_audit",
    "handoff_manifest",
    "skillopt_gate_plan",
    "current_next_queue",
)


def schema_nested_contracts(summary: dict[str, Any] | None = None) -> dict[str, str]:
    contracts: dict[str, str] = {}
    source = summary or {}
    for field in DASHBOARD_SCHEMA_NESTED_CONTRACT_FIELDS:
        value = source.get(field)
        contracts[field] = str(value.get("contract", "")) if isinstance(value, dict) else ""
    return contracts


def schema_nested_contracts_fingerprint(contracts: dict[str, str]) -> str:
    return hashlib.sha256(
        json.dumps(contracts, ensure_ascii=False, sort_keys=True).encode("utf-8")
    ).hexdigest()[:12]


def schema_summary(summary: dict[str, Any] | None = None) -> dict[str, Any]:
    nested_contracts = schema_nested_contracts(summary)
    return {
        "schema": {
            "name": DASHBOARD_SCHEMA_NAME,
            "version": DASHBOARD_SCHEMA_VERSION,
            "contract": DASHBOARD_SCHEMA_CONTRACT,
            "required_top_level_fields": list(DASHBOARD_SCHEMA_REQUIRED_TOP_LEVEL_FIELDS),
            "nested_contracts": nested_contracts,
            "nested_contracts_fingerprint": schema_nested_contracts_fingerprint(nested_contracts),
        }
    }


def schema_line(summary: dict[str, Any]) -> str:
    schema = summary.get("schema")
    if not isinstance(schema, dict):
        return "unavailable"
    return (
        f"{schema.get('name', 'unknown')} v{schema.get('version', 'unknown')}; "
        f"{schema.get('contract', 'unknown')}"
    )


def validate_schema_contract(summary: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    schema = summary.get("schema")
    expected = schema_summary(summary)["schema"]
    if not isinstance(schema, dict):
        return ["schema missing or not an object"]
    for key in (
        "name",
        "version",
        "contract",
        "required_top_level_fields",
        "nested_contracts",
        "nested_contracts_fingerprint",
    ):
        if schema.get(key) != expected[key]:
            errors.append(f"schema.{key} expected {expected[key]!r}, observed {schema.get(key)!r}")
    required = schema.get("required_top_level_fields", [])
    if not isinstance(required, list):
        errors.append("schema.required_top_level_fields must be a list")
        return errors
    for field in required:
        if not isinstance(field, str):
            errors.append("schema.required_top_level_fields must contain only strings")
            continue
        if field not in summary:
            errors.append(f"schema required field {field!r} missing from summary")
    return errors


def command_plan_fingerprint(measurement: list[str], validation: list[str]) -> str:
    payload = json.dumps(
        {"measurement_commands": measurement, "validation_commands": validation},
        ensure_ascii=False,
        sort_keys=True,
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:12]


def command_plan_summary() -> dict[str, Any]:
    measurement = list(NEXT_LOOP_MEASUREMENT_COMMANDS)
    validation = list(NEXT_LOOP_VALIDATION_COMMANDS)
    return {
        "measurement_commands": measurement,
        "validation_commands": validation,
        "command_plan": {
            "measurement_count": len(measurement),
            "validation_count": len(validation),
            "fingerprint": command_plan_fingerprint(measurement, validation),
        },
    }


def summary_command_list(summary: dict[str, Any], key: str, fallback: tuple[str, ...]) -> list[str]:
    value = summary.get(key)
    if isinstance(value, list) and value and all(isinstance(command, str) for command in value):
        return value
    return list(fallback)


def summary_measurement_commands(summary: dict[str, Any]) -> list[str]:
    return summary_command_list(summary, "measurement_commands", NEXT_LOOP_MEASUREMENT_COMMANDS)


def summary_validation_commands(summary: dict[str, Any]) -> list[str]:
    return summary_command_list(summary, "validation_commands", NEXT_LOOP_VALIDATION_COMMANDS)


def strict_latest_heading_command(heading: str) -> str:
    return (
        "python3 tools/monthly_uplift_report.py --check-worklog latest --limit 20 "
        f"--expect-latest-heading {shlex.quote(heading)}"
    )


def summary_latest_heading_command(summary: dict[str, Any]) -> str:
    worklog = summary.get("worklog", {}) if isinstance(summary.get("worklog"), dict) else {}
    heading = str(worklog.get("latest_heading", "") or "").strip()
    if not heading:
        heading = worklog_template_heading(summary)
    return strict_latest_heading_command(heading)


def summary_validation_commands_with_latest_heading(summary: dict[str, Any]) -> list[str]:
    commands = summary_validation_commands(summary)
    strict_command = summary_latest_heading_command(summary)
    if strict_command not in commands:
        commands.append(strict_command)
    return commands


def command_plan_line(summary: dict[str, Any]) -> str:
    plan = summary.get("command_plan")
    if not isinstance(plan, dict):
        return "unavailable"
    fingerprint = str(plan.get("fingerprint", ""))
    suffix = f"; sha256 {fingerprint}" if fingerprint else ""
    return (
        f"{int(plan.get('measurement_count', 0))} measurement / "
        f"{int(plan.get('validation_count', 0))} validation{suffix}"
    )


def validate_command_plan(summary: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    expected_by_key = {
        "measurement_commands": list(NEXT_LOOP_MEASUREMENT_COMMANDS),
        "validation_commands": list(NEXT_LOOP_VALIDATION_COMMANDS),
    }
    for key, expected in expected_by_key.items():
        value = summary.get(key)
        if not isinstance(value, list):
            errors.append(f"{key} missing or not a list")
            continue
        if not value:
            errors.append(f"{key} must not be empty")
            continue
        if not all(isinstance(command, str) and command.strip() for command in value):
            errors.append(f"{key} must contain only non-empty strings")
            continue
        if value != expected:
            errors.append(f"{key} does not match the built-in command plan")
    expected_plan = command_plan_summary()["command_plan"]
    plan = summary.get("command_plan")
    if not isinstance(plan, dict):
        errors.append("command_plan missing or not an object")
    else:
        for key, expected in expected_plan.items():
            if plan.get(key) != expected:
                errors.append(f"command_plan.{key} expected {expected!r}, observed {plan.get(key)!r}")
    return errors


WORKLOG_REQUIRED_VALIDATION_MARKERS = (
    "python3 -m py_compile",
    "python3 tools/monthly_uplift_report.py --self-test",
    "python3 tools/monthly_uplift_report.py --check --handoff --limit 20",
    "python3 tools/monthly_uplift_report.py --check --publish-plan --limit 20",
    "python3 tools/monthly_uplift_report.py --check --goal-audit --limit 20",
    "python3 tools/monthly_uplift_report.py --check --debt-audit --limit 20",
    "python3 tools/monthly_uplift_report.py --check --worklog-template --limit 20",
    "python3 tools/monthly_uplift_report.py --check-worklog latest",
    "--expect-latest-heading",
    "python3 tools/monthly_uplift_report.py --check --limit 20 --output",
    "python3 tools/run_checks.py --skip-reports",
    "python3 tools/run_checks.py",
    "git diff --check",
)
CURRENT_NEXT_QUEUE_REQUIRED_MARKERS = (
    "Loop-control status:",
    "Local publish-unit split:",
    "needs-owner-review",
    "Regression gates for the next batch:",
    "python3 tools/monthly_uplift_report.py --check --handoff --limit 20",
    "python3 tools/monthly_uplift_report.py --check --publish-plan --limit 20",
    "python3 tools/monthly_uplift_report.py --check --goal-audit --limit 20",
    "python3 tools/monthly_uplift_report.py --check --debt-audit --limit 20",
    "python3 tools/monthly_uplift_report.py --check --worklog-template --limit 20",
    "python3 tools/monthly_uplift_report.py --check-worklog latest",
    "python3 tools/monthly_uplift_report.py --check --limit 20",
    "python3 tools/audit_repo.py --counts",
    "python3 tools/quality_scorecard.py",
    "python3 tools/source_map_audit.py",
    "python3 tools/root_entry_audit.py",
    "python3 tools/clone_audit.py --threshold",
    "python3 tools/run_checks.py --skip-reports",
    "python3 tools/run_checks.py",
    "git diff --check",
)

AGENT_A_KEYWORDS = (
    "aer-insights",
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
AGENT_B_KEYWORDS = (
    "cancer",
    "cell",
    "clinical",
    "jama",
    "lancet",
    "medicine",
    "medical",
    "nejm",
    "pnas",
)
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
AGENT_C_CATEGORY_KEYWORDS = (
    "agricultur",
    "conservation",
    "critical-inquiry",
    "engineering",
    "environment",
    "field-crops",
    "global-change",
    "humanities",
    "pmla",
    "technology",
)

DELTA_METRICS = (
    ("skills", "Inventory skills", ("counts", "skills"), 0),
    ("packs", "Inventory packs", ("counts", "packs"), 0),
    ("root_entries", "Root journal entries", ("counts", "root_entries"), 0),
    ("quality_mean", "Quality mean", ("quality", "mean"), 1),
    ("quality_min", "Quality min", ("quality", "min"), 1),
    ("quality_below_target", "Below score target", ("quality", "below_target"), 0),
    ("execution_bridge_wired", "Execution bridge wired", ("execution_bridge", "wired"), 0),
    ("execution_bridge_missing", "Execution bridge missing", ("execution_bridge", "missing"), 0),
    ("source_map_warnings", "Source-map warnings", ("source_maps", "warnings"), 0),
    ("source_map_max_unresolved", "Source-map max unresolved", ("source_maps", "max_unresolved"), 0),
    ("root_machine_only", "Root machine-only cards", ("root_entries", "machine_only"), 0),
    ("root_warnings", "Root-card warnings", ("root_entries", "warnings"), 0),
    ("external_link_urls", "External-link URLs", ("external_links", "url_count"), 0),
    ("external_link_cache_entries", "External-link cache rows", ("external_links", "cache_entry_count"), 0),
    ("external_link_current_cache_entries", "External-link current cache rows", ("external_links", "current_cache_entry_count"), 0),
    ("external_link_orphaned_cache_entries", "External-link orphaned cache rows", ("external_links", "orphaned_cache_entry_count"), 0),
    ("external_link_checked", "External-link checked cache rows", ("external_links", "checked_count"), 0),
    ("external_link_unchecked", "External-link unchecked URLs", ("external_links", "unchecked_count"), 0),
    ("external_link_actionable", "External-link actionable URLs", ("external_links", "actionable_count"), 0),
    ("external_link_inconclusive", "External-link inconclusive URLs", ("external_links", "inconclusive_count"), 0),
    ("clone_fail_hits", "Clone fail hits", ("clone_audit", "fail_hits"), 0),
    ("claims_rows", "Claims rows", ("claims", "row_count"), 0),
    ("claims_active_rows", "Claims active rows", ("claims", "active_row_count"), 0),
    ("claims_lines", "Claims boundary lines", ("claims", "line_count"), 0),
    ("unclaimed_score_candidates", "Unclaimed score candidates", ("loop_control", "unclaimed_score_candidates"), 0),
    ("unclaimed_source_map_candidates", "Unclaimed source-map candidates", ("loop_control", "unclaimed_source_map_candidates"), 0),
    ("unclaimed_execution_bridge_candidates", "Unclaimed execution-bridge candidates", ("loop_control", "unclaimed_execution_bridge_candidates"), 0),
    ("claim_sensitive_score_targets", "Claim-sensitive score targets", ("loop_control", "claim_sensitive_score_targets"), 0),
    ("claim_sensitive_source_map_targets", "Claim-sensitive source-map targets", ("loop_control", "claim_sensitive_source_map_targets"), 0),
    ("claim_sensitive_execution_bridge_targets", "Claim-sensitive execution-bridge targets", ("loop_control", "claim_sensitive_execution_bridge_targets"), 0),
    ("dirty_skipped_packs", "Dirty skipped packs", ("loop_control", "dirty_skipped_packs"), 0),
    ("worklog_loop_count", "Worklog loops", ("worklog", "loop_count"), 0),
    ("git_dirty_entries", "Git dirty entries", ("git", "dirty_count"), 0),
    ("git_dirty_pack_lanes", "Git dirty pack lanes", ("git", "dirty_pack_count"), 0),
    ("git_dirty_root_entries", "Git dirty root/tooling entries", ("git", "dirty_root_count"), 0),
    ("worktree_boundary_dirty_entries", "Worktree boundary dirty entries", ("worktree_boundary", "dirty_count"), 0),
    ("worktree_boundary_pack_lanes", "Worktree boundary pack lanes", ("worktree_boundary", "dirty_pack_count"), 0),
    ("worktree_boundary_root_entries", "Worktree boundary root/tooling entries", ("worktree_boundary", "dirty_root_count"), 0),
    ("schema_version", "Dashboard schema version", ("schema", "version"), 0),
    ("command_plan_measurement_count", "Command plan measurement commands", ("command_plan", "measurement_count"), 0),
    ("command_plan_validation_count", "Command plan validation commands", ("command_plan", "validation_count"), 0),
    ("next_batch_count", "Next-batch plan items", ("next_batch_plan", "count"), 0),
    ("content_policy_unclaimed_candidates", "Content-policy unclaimed candidates", ("content_edit_policy", "unclaimed_candidate_count"), 0),
    ("content_policy_claim_sensitive_targets", "Content-policy claim-sensitive targets", ("content_edit_policy", "claim_sensitive_target_count"), 0),
    ("content_policy_dirty_pack_lanes", "Content-policy dirty pack lanes", ("content_edit_policy", "dirty_pack_lane_count"), 0),
    ("execution_bridge_tail_missing", "Execution-bridge tail missing", ("execution_bridge_tail", "missing"), 0),
    (
        "execution_bridge_tail_unclaimed",
        "Execution-bridge tail unclaimed",
        ("execution_bridge_tail", "unclaimed_count"),
        0,
    ),
    (
        "execution_bridge_tail_owner_clearance",
        "Execution-bridge tail owner-clearance",
        ("execution_bridge_tail", "owner_clearance_count"),
        0,
    ),
    ("safe_content_queue_unclaimed_total", "Safe content queue unclaimed", ("safe_content_queue", "unclaimed_total"), 0),
    ("safe_content_queue_score", "Safe content queue score", ("safe_content_queue", "score_count"), 0),
    ("safe_content_queue_source_map", "Safe content queue source-map", ("safe_content_queue", "source_map_count"), 0),
    ("safe_content_queue_bridge", "Safe content queue bridge", ("safe_content_queue", "execution_bridge_count"), 0),
    ("safe_content_queue_score_ceiling", "Safe content queue score ceiling", ("safe_content_queue", "score_ceiling_count"), 0),
    ("safe_content_queue_dirty_skipped", "Safe content queue dirty skipped", ("safe_content_queue", "dirty_skipped_count"), 0),
    ("owner_clearance_queue_total", "Owner-clearance queue total", ("owner_clearance_queue", "total"), 0),
    ("remaining_debt_unclaimed_total", "Remaining-debt unclaimed total", ("remaining_debt", "unclaimed_total"), 0),
    ("remaining_debt_owner_clearance_total", "Remaining-debt owner-clearance total", ("remaining_debt", "owner_clearance_total"), 0),
    ("remaining_debt_dirty_pack_lanes", "Remaining-debt dirty pack lanes", ("remaining_debt", "dirty_pack_lane_count"), 0),
    ("publish_policy_root_paths", "Publish-policy root/tooling paths", ("publish_policy", "root_tooling_path_count"), 0),
    ("publish_policy_pack_lanes", "Publish-policy pack lanes", ("publish_policy", "pack_content_pack_count"), 0),
    ("goal_progress_worklog_loops", "Goal-progress worklog loops", ("goal_progress", "worklog_loop_count"), 0),
    ("goal_progress_execution_bridge_missing", "Goal-progress bridge missing", ("goal_progress", "execution_bridge_missing"), 0),
    ("completion_audit_requirements", "Completion-audit requirements", ("completion_audit", "requirement_count"), 0),
    ("completion_audit_blockers", "Completion-audit blockers", ("completion_audit", "blocker_count"), 0),
    ("handoff_manifest_completion_requirements", "Handoff completion-audit requirements", ("handoff_manifest", "completion_audit_requirement_count"), 0),
    ("handoff_manifest_completion_blockers", "Handoff completion-audit blockers", ("handoff_manifest", "completion_audit_blocker_count"), 0),
    ("handoff_manifest_root_paths", "Handoff root/tooling paths", ("handoff_manifest", "root_tooling_path_count"), 0),
    ("handoff_manifest_pack_lanes", "Handoff pack lanes", ("handoff_manifest", "pack_content_pack_count"), 0),
)
DELTA_TEXT_METRICS = (
    ("claims_present", "Claims boundary present", ("claims", "present")),
    ("claims_fingerprint", "Claims boundary fingerprint", ("claims", "fingerprint")),
    ("schema_contract", "Dashboard schema contract", ("schema", "contract")),
    ("external_link_status", "External-link advisory status", ("external_links", "status")),
    ("external_link_fingerprint", "External-link advisory fingerprint", ("external_links", "fingerprint")),
    (
        "schema_nested_contracts_fingerprint",
        "Dashboard nested-contracts fingerprint",
        ("schema", "nested_contracts_fingerprint"),
    ),
    (
        "worktree_boundary_fingerprint",
        "Worktree boundary fingerprint (worktree-sensitive)",
        ("worktree_boundary", "fingerprint"),
    ),
    ("command_plan_fingerprint", "Command plan fingerprint", ("command_plan", "fingerprint")),
    ("next_batch_fingerprint", "Next-batch plan fingerprint", ("next_batch_plan", "fingerprint")),
    ("content_policy_status", "Content-edit policy status", ("content_edit_policy", "status")),
    ("content_policy_fingerprint", "Content-edit policy fingerprint", ("content_edit_policy", "fingerprint")),
    (
        "content_policy_bridge_owner_clearance",
        "Content-policy bridge owner-clearance",
        ("content_edit_policy", "execution_bridge_owner_clearance_required"),
    ),
    ("execution_bridge_tail_status", "Execution-bridge tail status", ("execution_bridge_tail", "status")),
    ("execution_bridge_tail_policy", "Execution-bridge tail policy", ("execution_bridge_tail", "claim_sensitive_policy")),
    (
        "execution_bridge_tail_clearance_before_wiring",
        "Execution-bridge clearance-before-wiring",
        ("execution_bridge_tail", "owner_clearance_required_before_wiring"),
    ),
    ("execution_bridge_tail_fingerprint", "Execution-bridge tail fingerprint", ("execution_bridge_tail", "fingerprint")),
    ("safe_content_queue_status", "Safe content queue status", ("safe_content_queue", "status")),
    ("safe_content_queue_fingerprint", "Safe content queue fingerprint", ("safe_content_queue", "fingerprint")),
    ("owner_clearance_queue_fingerprint", "Owner-clearance queue fingerprint", ("owner_clearance_queue", "fingerprint")),
    ("remaining_debt_status", "Remaining-debt status", ("remaining_debt", "status")),
    ("remaining_debt_fingerprint", "Remaining-debt fingerprint", ("remaining_debt", "fingerprint")),
    ("publish_policy_status", "Publish policy status", ("publish_policy", "status")),
    (
        "publish_policy_fingerprint",
        "Publish policy fingerprint (worktree-sensitive)",
        ("publish_policy", "fingerprint"),
    ),
    ("goal_progress_status", "Goal-progress status", ("goal_progress", "status")),
    ("goal_progress_fingerprint", "Goal-progress fingerprint", ("goal_progress", "fingerprint")),
    ("completion_audit_status", "Completion-audit status", ("completion_audit", "completion_status")),
    ("completion_audit_fingerprint", "Completion-audit fingerprint", ("completion_audit", "fingerprint")),
    ("handoff_manifest_contract", "Handoff manifest contract", ("handoff_manifest", "contract")),
    ("handoff_manifest_completion_contract", "Handoff completion-audit contract", ("handoff_manifest", "completion_audit_contract")),
    (
        "handoff_manifest_fingerprint",
        "Handoff manifest fingerprint (worktree-sensitive)",
        ("handoff_manifest", "fingerprint"),
    ),
    ("skillopt_gate_plan_status", "SkillOpt gate-plan status", ("skillopt_gate_plan", "status")),
    ("skillopt_gate_plan_fingerprint", "SkillOpt gate-plan fingerprint", ("skillopt_gate_plan", "fingerprint")),
    ("current_next_queue_fingerprint", "Current-next-queue fingerprint", ("current_next_queue", "fingerprint")),
)
OWNER_CLEARANCE_KINDS = ("score-floor", "source-map", "execution-bridge")
OWNER_CLEARANCE_QUEUE_CONTRACT = "owner-clearance-queue-v2"
SKILLOPT_GATE_PLAN_CONTRACT = "monthly-uplift-skillopt-gate-plan-v1"
SKILLOPT_SNAPSHOT_COMMAND = "python3 tools/skillopt_gate.py snapshot --out /tmp/ajs-skillopt-baseline.json"
SKILLOPT_GATE_COMMAND = (
    "python3 tools/skillopt_gate.py gate --baseline /tmp/ajs-skillopt-baseline.json "
    "--out /tmp/ajs-skillopt-gate.json"
)
CURRENT_NEXT_QUEUE_CONTRACT = "current-next-queue-v7"
NEXT_BATCH_PLAN_CONTRACT = "monthly-uplift-next-batch-plan-v1"
EXTERNAL_LINKS_CONTRACT = "external-link-cache-summary-v2"
WORKLOG_LIVE_SUMMARY_LIMIT = 20


def worklog_live_summary_args(args: argparse.Namespace) -> argparse.Namespace:
    """Return the stable dashboard context used by the worklog live guard."""
    return argparse.Namespace(
        score_target=args.score_target,
        limit=WORKLOG_LIVE_SUMMARY_LIMIT,
        skip_clone=True,
        clone_threshold=args.clone_threshold,
        clone_fail_threshold=args.clone_fail_threshold,
        clone_top=args.clone_top,
        compare_json=None,
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


def external_links_summary() -> dict[str, Any]:
    data = json.loads(run([PYTHON, "tools/external_link_audit.py", "--cache-summary", "--json"]))
    if not isinstance(data, dict):
        raise ValueError("external_link_audit.py --cache-summary --json did not return an object")
    return {"external_links": data}


def external_links_fingerprint(advisory: dict[str, Any]) -> str:
    counts = advisory.get("counts", {}) if isinstance(advisory.get("counts"), dict) else {}
    payload = {
        "contract": str(advisory.get("contract", "")),
        "status": str(advisory.get("status", "")),
        "include_infra": bool(advisory.get("include_infra", False)),
        "cache_entry_count": int(advisory.get("cache_entry_count", 0)),
        "current_cache_entry_count": int(advisory.get("current_cache_entry_count", 0)),
        "orphaned_cache_entry_count": int(advisory.get("orphaned_cache_entry_count", 0)),
        "url_count": int(advisory.get("url_count", 0)),
        "checked_count": int(advisory.get("checked_count", 0)),
        "unchecked_count": int(advisory.get("unchecked_count", 0)),
        "actionable_count": int(advisory.get("actionable_count", 0)),
        "inconclusive_count": int(advisory.get("inconclusive_count", 0)),
        "counts": {str(key): int(value) for key, value in sorted(counts.items())},
    }
    return hashlib.sha256(json.dumps(payload, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()[:12]


def external_links_line(summary: dict[str, Any]) -> str:
    advisory = summary.get("external_links")
    if not isinstance(advisory, dict):
        return "unavailable"
    fingerprint = str(advisory.get("fingerprint", ""))
    suffix = f"; sha256 {fingerprint}" if fingerprint else ""
    cache = "cache present" if advisory.get("cache_present") else "cache missing"
    return (
        f"{advisory.get('contract', EXTERNAL_LINKS_CONTRACT)}; "
        f"status {advisory.get('status', 'unknown')}; "
        f"{int(advisory.get('checked_count', 0))}/{int(advisory.get('url_count', 0))} cached; "
        f"{int(advisory.get('actionable_count', 0))} actionable; "
        f"{int(advisory.get('inconclusive_count', 0))} inconclusive; {cache}{suffix}"
    )


def external_links_cache_line(summary: dict[str, Any]) -> str:
    advisory = summary.get("external_links")
    if not isinstance(advisory, dict):
        return "unavailable"
    fingerprint = str(advisory.get("fingerprint", ""))
    suffix = f"; sha256 {fingerprint}" if fingerprint else ""
    return (
        f"{int(advisory.get('current_cache_entry_count', 0))}/"
        f"{int(advisory.get('url_count', 0))} current URLs have cache rows; "
        f"{int(advisory.get('cache_entry_count', 0))} total cache rows; "
        f"{int(advisory.get('orphaned_cache_entry_count', 0))} orphaned{suffix}"
    )


def external_link_count(advisory: dict[str, Any], key: str) -> int:
    counts = advisory.get("counts", {}) if isinstance(advisory.get("counts"), dict) else {}
    try:
        return int(counts.get(key, 0))
    except (TypeError, ValueError):
        return 0


def external_links_breakdown_line(summary: dict[str, Any]) -> str:
    advisory = summary.get("external_links")
    if not isinstance(advisory, dict):
        return "unavailable"
    fingerprint = str(advisory.get("fingerprint", ""))
    suffix = f"; sha256 {fingerprint}" if fingerprint else ""
    return (
        f"DEAD {external_link_count(advisory, 'DEAD')} / "
        f"REDIRECT {external_link_count(advisory, 'REDIRECT')} actionable; "
        f"BLOCKED {external_link_count(advisory, 'BLOCKED')} / "
        f"UNREACHABLE {external_link_count(advisory, 'UNREACHABLE')} inconclusive; "
        f"UNCHECKED {external_link_count(advisory, 'UNCHECKED')}; "
        f"OK {external_link_count(advisory, 'OK')}{suffix}"
    )


def validate_external_links(summary: dict[str, Any]) -> list[str]:
    if "generated_at" not in summary and "external_links" not in summary:
        return []
    advisory = summary.get("external_links")
    if not isinstance(advisory, dict):
        return ["external_links missing or not an object"]
    errors: list[str] = []
    counts = advisory.get("counts")
    if not isinstance(counts, dict):
        return ["external_links.counts missing or not an object"]
    required_classes = ("OK", "DEAD", "REDIRECT", "BLOCKED", "UNREACHABLE", "UNCHECKED")
    normalized_counts: dict[str, int] = {}
    for cls in required_classes:
        try:
            normalized_counts[cls] = int(counts.get(cls, 0))
        except (TypeError, ValueError):
            errors.append(f"external_links.counts.{cls} must be an integer")
            normalized_counts[cls] = 0
    if advisory.get("contract") != EXTERNAL_LINKS_CONTRACT:
        errors.append(
            f"external_links.contract expected {EXTERNAL_LINKS_CONTRACT!r}, observed {advisory.get('contract')!r}"
        )
    url_count = int(advisory.get("url_count", 0))
    cache_entry_count = int(advisory.get("cache_entry_count", 0))
    current_cache_entry_count = int(advisory.get("current_cache_entry_count", 0))
    orphaned_cache_entry_count = int(advisory.get("orphaned_cache_entry_count", 0))
    checked_count = int(advisory.get("checked_count", 0))
    unchecked_count = int(advisory.get("unchecked_count", 0))
    actionable_count = int(advisory.get("actionable_count", 0))
    inconclusive_count = int(advisory.get("inconclusive_count", 0))
    if sum(normalized_counts.values()) != url_count:
        errors.append("external_links counts do not sum to url_count")
    if checked_count + unchecked_count != url_count:
        errors.append("external_links checked_count + unchecked_count does not equal url_count")
    if current_cache_entry_count > url_count:
        errors.append("external_links current_cache_entry_count exceeds url_count")
    if checked_count > current_cache_entry_count:
        errors.append("external_links checked_count exceeds current_cache_entry_count")
    if cache_entry_count != current_cache_entry_count + orphaned_cache_entry_count:
        errors.append("external_links cache_entry_count does not equal current_cache_entry_count + orphaned_cache_entry_count")
    if unchecked_count != normalized_counts["UNCHECKED"]:
        errors.append("external_links unchecked_count does not match counts.UNCHECKED")
    if actionable_count != normalized_counts["DEAD"] + normalized_counts["REDIRECT"]:
        errors.append("external_links actionable_count does not match DEAD+REDIRECT")
    if inconclusive_count != normalized_counts["BLOCKED"] + normalized_counts["UNREACHABLE"]:
        errors.append("external_links inconclusive_count does not match BLOCKED+UNREACHABLE")
    if not advisory.get("cache_present"):
        expected_status = "no-cache"
    elif actionable_count:
        expected_status = "actionable-review"
    elif inconclusive_count or unchecked_count:
        expected_status = "advisory-review"
    else:
        expected_status = "cached-ok"
    if advisory.get("status") != expected_status:
        errors.append(f"external_links.status expected {expected_status!r}, observed {advisory.get('status')!r}")
    expected_fingerprint = external_links_fingerprint(advisory)
    if advisory.get("fingerprint") != expected_fingerprint:
        errors.append(
            f"external_links.fingerprint expected {expected_fingerprint!r}, observed {advisory.get('fingerprint')!r}"
        )
    return errors


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


def execution_bridge_summary(rows: list[dict[str, Any]], limit: int) -> dict[str, Any]:
    empirical = [
        row
        for row in rows
        if row.get("pack_type") == "depth" and row.get("code_status") == "present"
    ]
    missing = sorted(
        [row for row in empirical if not row.get("exec_bridge")],
        key=lambda row: (float(row.get("score", 0)), str(row.get("pack", ""))),
    )
    wired = len(empirical) - len(missing)
    return {
        "empirical_depth_packs": len(empirical),
        "wired": wired,
        "missing": len(missing),
        "missing_packs": missing[:limit],
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


def score_ceiling_reason(row: dict[str, Any]) -> str:
    breakdown = row.get("_breakdown")
    if not isinstance(breakdown, dict):
        return ""
    max_values = {
        "depth": 35.0,
        "trigger": 20.0,
        "resources": 28.0,
        "runnable": 5.0,
        "structure": 6.0,
    }
    for key, max_value in max_values.items():
        try:
            value = float(breakdown.get(key, -1))
        except (TypeError, ValueError):
            return ""
        if value < max_value:
            return ""
    return "scorecard rubric ceiling reached; do not treat as score-floor debt"


def root_summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    warnings = [row for row in rows if row.get("warnings")]
    enriched = [row for row in rows if row.get("enriched")]
    return {
        "entry_count": len(rows),
        "enriched": len(enriched),
        "machine_only": len(rows) - len(enriched),
        "warnings": len(warnings),
    }


def nested_number(data: dict[str, Any], path: tuple[str, ...]) -> float | None:
    value: Any = data
    for key in path:
        if not isinstance(value, dict) or key not in value:
            return None
        value = value[key]
        if value is None:
            return None
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    return float(value)


def nested_value(data: dict[str, Any], path: tuple[str, ...]) -> Any:
    value: Any = data
    for key in path:
        if not isinstance(value, dict) or key not in value:
            return None
        value = value[key]
    return value


def rounded_number(value: float, precision: int) -> int | float:
    if precision == 0:
        return int(round(value))
    return round(value, precision)


def normalized_delta_text(value: Any) -> str:
    if value is None:
        return "missing"
    if isinstance(value, bool):
        return "true" if value else "false"
    text = str(value)
    return text if text else "missing"


def compare_delta(previous: dict[str, Any], current: dict[str, Any]) -> dict[str, Any]:
    metrics: dict[str, dict[str, Any]] = {}
    for key, label, path, precision in DELTA_METRICS:
        old = nested_number(previous, path)
        new = nested_number(current, path)
        if old is None or new is None:
            continue
        metrics[key] = {
            "label": label,
            "precision": precision,
            "previous": rounded_number(old, precision),
            "current": rounded_number(new, precision),
            "delta": rounded_number(new - old, precision),
        }

    text_metrics: dict[str, dict[str, Any]] = {}
    for key, label, path in DELTA_TEXT_METRICS:
        old_value = nested_value(previous, path)
        new_value = nested_value(current, path)
        if old_value is None and new_value is None:
            continue
        text_metrics[key] = {
            "label": label,
            "previous": normalized_delta_text(old_value),
            "current": normalized_delta_text(new_value),
            "changed": old_value != new_value,
        }

    return {
        "baseline_generated_at": str(previous.get("generated_at", "unknown")),
        "current_generated_at": str(current.get("generated_at", "unknown")),
        "previous_loop_status": str(previous.get("loop_control", {}).get("status", "unknown")),
        "current_loop_status": str(current.get("loop_control", {}).get("status", "unknown")),
        "metrics": metrics,
        "text": text_metrics,
    }


def load_compare_json(path: Path) -> dict[str, Any]:
    input_path = path if path.is_absolute() else ROOT / path
    try:
        data = json.loads(input_path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise ValueError(f"could not read compare JSON {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError(f"compare JSON {path} must contain an object")
    return data


def latest_worklog_section(text: str) -> tuple[str, str] | None:
    headings = list(WORKLOG_HEADING_RE.finditer(text))
    if not headings:
        return None
    latest = headings[-1]
    next_heading = re.search(r"\n(?:##|###) ", text[latest.end() :])
    end = latest.end() + next_heading.start() if next_heading else len(text)
    return latest.group(0), text[latest.start() : end]


def squash_spaces(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def current_next_queue_global_section(text: str) -> str | None:
    marker = "## Current Next Queue"
    start = text.find(marker)
    if start == -1:
        return None
    section = text[start:]
    next_heading = re.search(r"\n(?:##|###) ", section[len(marker) :])
    if next_heading:
        return section[: len(marker) + next_heading.start()]
    return section


def contract_family_errors(section: str, pattern: str, expected: str, label: str) -> list[str]:
    observed = sorted(set(re.findall(pattern, section)))
    return [f"Current Next Queue global section has stale {label} {value!r}; expected {expected!r}" for value in observed if value != expected]


def validate_current_next_queue_global_text(text: str, summary: dict[str, Any] | None = None) -> list[str]:
    section = current_next_queue_global_section(text)
    if section is None:
        return ["worklog missing '## Current Next Queue'"]
    errors: list[str] = []
    required_contracts = (
        CURRENT_NEXT_QUEUE_CONTRACT,
        DASHBOARD_SCHEMA_CONTRACT,
        OWNER_CLEARANCE_QUEUE_CONTRACT,
        COMPLETION_AUDIT_CONTRACT,
    )
    for contract in required_contracts:
        if contract not in section:
            errors.append(f"Current Next Queue global section missing contract {contract!r}")
    errors.extend(contract_family_errors(section, r"current-next-queue-v\d+", CURRENT_NEXT_QUEUE_CONTRACT, "queue contract"))
    errors.extend(contract_family_errors(section, r"monthly-uplift-dashboard-v\d+", DASHBOARD_SCHEMA_CONTRACT, "schema contract"))
    errors.extend(contract_family_errors(section, r"owner-clearance-queue-v\d+", OWNER_CLEARANCE_QUEUE_CONTRACT, "owner-clearance contract"))
    errors.extend(
        contract_family_errors(
            section,
            r"monthly-uplift-completion-audit-v\d+",
            COMPLETION_AUDIT_CONTRACT,
            "completion-audit contract",
        )
    )
    if isinstance(summary, dict):
        schema = summary.get("schema", {}) if isinstance(summary.get("schema"), dict) else {}
        nested_fingerprint = str(schema.get("nested_contracts_fingerprint", ""))
        if nested_fingerprint and nested_fingerprint not in section:
            errors.append(
                "Current Next Queue global section missing live nested-contracts fingerprint "
                f"{nested_fingerprint!r}"
            )
        for fragment in (
            f"owner-clearance target fingerprints `{owner_clearance_target_fingerprint_line(summary)}`",
            f"completion-audit owner target fingerprints `{completion_audit_owner_target_fingerprint_line(summary)}`",
        ):
            if fragment not in section:
                errors.append(f"Current Next Queue global section missing live fragment {fragment!r}")
    return errors


def extract_backtick_commands(line: str) -> list[str]:
    commands = re.findall(r"`([^`]*--expect-latest-heading[^`]*)`", line)
    if commands:
        return commands
    if "--expect-latest-heading" in line:
        return [line.strip().lstrip("- ").strip()]
    return []


def validate_latest_heading_commands(validation_block: str, heading: str) -> list[str]:
    errors: list[str] = []
    commands = [
        command
        for line in validation_block.splitlines()
        for command in extract_backtick_commands(line)
    ]
    if not commands:
        return ["latest loop validation missing strict latest-heading command"]
    for command in commands:
        try:
            parts = shlex.split(command)
        except ValueError as exc:
            errors.append(f"strict latest-heading command could not be parsed: {exc}")
            continue
        try:
            index = parts.index("--expect-latest-heading")
        except ValueError:
            errors.append("strict latest-heading command missing --expect-latest-heading")
            continue
        if index + 1 >= len(parts):
            errors.append("strict latest-heading command missing expected heading value")
            continue
        expected = parts[index + 1]
        if expected != heading:
            errors.append(
                f"strict latest-heading command expected {expected!r}, "
                f"but latest heading is {heading!r}"
            )
    return errors


def validate_worklog_text(text: str) -> list[str]:
    errors: list[str] = []
    if "Pending in this loop" in text:
        errors.append("worklog still contains 'Pending in this loop'")
    placeholder = WORKLOG_PLACEHOLDER_RE.search(text)
    if placeholder:
        errors.append(f"worklog still contains template placeholder {placeholder.group(0)!r}")

    section = latest_worklog_section(text)
    if section is None:
        errors.append("worklog has no dated loop heading like '### YYYY-MM-DD - ...'")
        return errors

    heading, latest = section
    for marker in WORKLOG_REQUIRED_MARKERS:
        if marker not in latest:
            errors.append(f"latest loop {heading!r} missing marker {marker!r}")

    if "- Validation:" in latest:
        validation_block = latest.split("- Validation:", 1)[1]
        for marker in WORKLOG_REQUIRED_VALIDATION_MARKERS:
            if marker not in validation_block:
                errors.append(f"latest loop {heading!r} validation missing command marker {marker!r}")
        errors.extend(validate_latest_heading_commands(validation_block, heading))
        planned_evidence = WORKLOG_PLANNED_EVIDENCE_RE.search(validation_block)
        if planned_evidence:
            errors.append(
                f"latest loop {heading!r} still contains planned validation text "
                f"{planned_evidence.group(0)!r}"
            )

    next_queue = current_next_queue_global_section(text)
    if next_queue is None:
        errors.append("worklog missing '## Current Next Queue'")
    else:
        normalized_next_queue = squash_spaces(next_queue)
        for marker in CURRENT_NEXT_QUEUE_REQUIRED_MARKERS:
            if marker not in next_queue:
                if marker not in normalized_next_queue:
                    errors.append(f"Current Next Queue missing marker {marker!r}")
        errors.extend(validate_current_next_queue_global_text(text))
    return errors


def skillopt_gate_plan_summary(summary: dict[str, Any]) -> dict[str, Any]:
    git = summary.get("git", {}) if isinstance(summary.get("git"), dict) else {}
    units = summary.get("publish_units", {}) if isinstance(summary.get("publish_units"), dict) else {}
    pack_unit = units.get("pack_content", {}) if isinstance(units.get("pack_content"), dict) else {}
    dirty_pack_paths = git.get("dirty_pack_paths", []) if isinstance(git.get("dirty_pack_paths"), list) else []
    dirty_skill_paths = [
        str(path)
        for path in dirty_pack_paths
        if str(path).endswith("/SKILL.md") and "/skills/" in str(path)
    ]
    dirty_pack_count = int(pack_unit.get("pack_count", 0) or 0)
    applicable_now = bool(dirty_skill_paths)
    if applicable_now:
        status = "dirty-skill-lanes-present"
        recommended_action = "preserve-existing-pack-lane-evidence"
        reason = (
            "dirty skill-body paths already exist in pack-content lanes; do not invent a "
            "pre-edit baseline after the fact, but require SkillOpt snapshot, gate, and final "
            "fast hard gate for new skill edits"
        )
    else:
        status = "ready-before-next-skill-edit"
        recommended_action = "take-baseline-before-bounded-skill-edit"
        reason = (
            "no dirty skill-body paths are currently visible; take the SkillOpt snapshot before "
            "the next skill edit, then run the SkillOpt gate and final fast hard gate before handoff"
        )
    plan = {
        "contract": SKILLOPT_GATE_PLAN_CONTRACT,
        "status": status,
        "applicable_now": applicable_now,
        "required_before_new_skill_edits": True,
        "dirty_skill_path_count": len(dirty_skill_paths),
        "dirty_skill_paths": dirty_skill_paths,
        "dirty_pack_lane_count": dirty_pack_count,
        "snapshot_command": SKILLOPT_SNAPSHOT_COMMAND,
        "gate_command": SKILLOPT_GATE_COMMAND,
        "final_hard_gate": "python3 tools/run_checks.py --skip-reports",
        "recommended_action": recommended_action,
        "reason": reason,
    }
    plan["fingerprint"] = hashlib.sha256(
        json.dumps(plan, ensure_ascii=False, sort_keys=True).encode("utf-8")
    ).hexdigest()[:12]
    return {"skillopt_gate_plan": plan}


def skillopt_gate_plan_line(summary: dict[str, Any]) -> str:
    plan = summary.get("skillopt_gate_plan")
    if not isinstance(plan, dict):
        plan = skillopt_gate_plan_summary(summary)["skillopt_gate_plan"]
    fingerprint = str(plan.get("fingerprint", ""))
    suffix = f"; sha256 {fingerprint}" if fingerprint else ""
    return (
        f"{plan.get('contract', SKILLOPT_GATE_PLAN_CONTRACT)}; status {plan.get('status', 'unknown')}; "
        f"{int(plan.get('dirty_skill_path_count', 0))} dirty skill paths / "
        f"{int(plan.get('dirty_pack_lane_count', 0))} dirty pack lanes; "
        f"action {plan.get('recommended_action', 'unknown')}; "
        f"final hard gate {plan.get('final_hard_gate', 'unknown')}{suffix}"
    )


def validate_skillopt_gate_plan(summary: dict[str, Any]) -> list[str]:
    if "generated_at" not in summary and "skillopt_gate_plan" not in summary:
        return []
    expected = skillopt_gate_plan_summary(summary)["skillopt_gate_plan"]
    plan = summary.get("skillopt_gate_plan")
    if not isinstance(plan, dict):
        return ["skillopt_gate_plan missing or not an object"]
    errors: list[str] = []
    for key, expected_value in expected.items():
        if plan.get(key) != expected_value:
            errors.append(f"skillopt_gate_plan.{key} expected {expected_value!r}, observed {plan.get(key)!r}")
    return errors


def current_next_queue_expected_fragments(summary: dict[str, Any]) -> list[str]:
    loop_control = summary.get("loop_control", {}) if isinstance(summary.get("loop_control"), dict) else {}
    skillopt_plan = summary.get("skillopt_gate_plan", {}) if isinstance(summary.get("skillopt_gate_plan"), dict) else {}
    schema_source = {
        **summary,
        "external_links": {"contract": EXTERNAL_LINKS_CONTRACT},
        "skillopt_gate_plan": {"contract": SKILLOPT_GATE_PLAN_CONTRACT},
        "current_next_queue": {"contract": CURRENT_NEXT_QUEUE_CONTRACT},
    }
    schema = schema_summary(schema_source)["schema"]
    command_plan = summary.get("command_plan", {}) if isinstance(summary.get("command_plan"), dict) else {}
    external_links = summary.get("external_links", {}) if isinstance(summary.get("external_links"), dict) else {}
    bridge_tail = summary.get("execution_bridge_tail", {}) if isinstance(summary.get("execution_bridge_tail"), dict) else {}
    safe_queue = summary.get("safe_content_queue", {}) if isinstance(summary.get("safe_content_queue"), dict) else {}
    content_policy = summary.get("content_edit_policy", {}) if isinstance(summary.get("content_edit_policy"), dict) else {}
    remaining_debt = summary.get("remaining_debt", {}) if isinstance(summary.get("remaining_debt"), dict) else {}
    publish_policy = summary.get("publish_policy", {}) if isinstance(summary.get("publish_policy"), dict) else {}
    next_batch_plan = summary.get("next_batch_plan", {}) if isinstance(summary.get("next_batch_plan"), dict) else {}
    goal_progress = summary.get("goal_progress", {}) if isinstance(summary.get("goal_progress"), dict) else {}
    completion_audit = summary.get("completion_audit", {}) if isinstance(summary.get("completion_audit"), dict) else {}
    handoff_manifest = summary.get("handoff_manifest", {}) if isinstance(summary.get("handoff_manifest"), dict) else {}
    clone = summary.get("clone_audit")
    include_clone_dependent = isinstance(clone, dict)
    clearance_queue = owner_clearance_queue_data(summary)
    fragments = [
        f"Current-next-queue contract: `{CURRENT_NEXT_QUEUE_CONTRACT}`",
        f"Loop-control status: `{loop_control.get('status', '')}`",
        f"`{loop_control.get('next_lane', '')}`",
        f"`{schema.get('contract', '')}`",
        "and `current_next_queue`",
        f"The current nested-contracts fingerprint is `{schema.get('nested_contracts_fingerprint', '')}`",
        f"`{external_links.get('contract', '')}`",
        f"external-link advisory status `{external_links.get('status', '')}`",
        f"external-link classes `{external_links_breakdown_line(summary)}`",
        f"external-link cache coverage `{external_links_cache_line(summary)}`",
        f"fingerprint `{external_links.get('fingerprint', '')}`",
        f"`{bridge_tail.get('contract', '')}`",
        f"execution-bridge tail policy `{bridge_tail.get('claim_sensitive_policy', '')}`",
        (
            "execution-bridge clearance before wiring "
            f"`{str(bool(bridge_tail.get('owner_clearance_required_before_wiring', False))).lower()}`"
        ),
        f"execution-bridge pack decision `{execution_bridge_tail_pack_line(summary)}`",
        f"fingerprint `{bridge_tail.get('fingerprint', '')}`",
        f"`{safe_queue.get('contract', '')}`",
        f"status `{safe_queue.get('status', '')}`",
        f"recommended action `{safe_queue.get('recommended_action', '')}`",
        f"fingerprint `{safe_queue.get('fingerprint', '')}`",
        f"`{content_policy.get('contract', '')}`",
        f"content-edit policy status `{content_policy.get('status', '')}`",
        f"fingerprint `{content_policy.get('fingerprint', '')}`",
        f"`{remaining_debt.get('contract', '')}`",
        f"remaining-debt status `{remaining_debt.get('status', '')}`",
        f"fingerprint `{remaining_debt.get('fingerprint', '')}`",
        f"owner-clearance queue `{owner_clearance_queue_line(summary)}`",
        f"owner-clearance target fingerprints `{owner_clearance_target_fingerprint_line(summary)}`",
        f"fingerprint `{clearance_queue.get('fingerprint', '')}`",
        f"`{publish_policy.get('contract', '')}`",
        f"publish policy status `{publish_policy.get('status', '')}`",
        f"`{next_batch_plan.get('contract', '')}`",
        f"next-batch count `{int(next_batch_plan.get('count', 0))}`",
        f"fingerprint `{next_batch_plan.get('fingerprint', '')}`",
        f"`{goal_progress.get('contract', '')}`",
        f"`{completion_audit.get('contract', '')}`",
        f"completion-audit owner target fingerprints `{completion_audit_owner_target_fingerprint_line(summary)}`",
        f"`{handoff_manifest.get('contract', '')}`",
        f"`{skillopt_plan.get('contract', '')}`",
        f"SkillOpt gate plan status `{skillopt_plan.get('status', '')}`",
        f"SkillOpt snapshot command `{skillopt_plan.get('snapshot_command', '')}`",
        f"SkillOpt gate command `{skillopt_plan.get('gate_command', '')}`",
        f"SkillOpt final hard gate `{skillopt_plan.get('final_hard_gate', '')}`",
        f"fingerprint `{skillopt_plan.get('fingerprint', '')}`",
        (
            f"plan is {int(command_plan.get('measurement_count', 0))} measurement commands / "
            f"{int(command_plan.get('validation_count', 0))} validation commands"
        ),
        "`python3 tools/quality_scorecard.py --top 15 --min-score 90`",
        f"fingerprint `{command_plan.get('fingerprint', '')}`",
    ]
    if include_clone_dependent:
        fragments.extend(
            [
                f"goal-progress status `{goal_progress.get('status', '')}`",
                f"fingerprint `{goal_progress.get('fingerprint', '')}`",
                f"completion-audit status `{completion_audit.get('completion_status', '')}`",
                f"fingerprint `{completion_audit.get('fingerprint', '')}`",
            ]
        )
    return [fragment for fragment in fragments if "``" not in fragment]


def current_next_queue_summary(summary: dict[str, Any]) -> dict[str, Any]:
    fragments = current_next_queue_expected_fragments(summary)
    queue = {
        "contract": CURRENT_NEXT_QUEUE_CONTRACT,
        "required_fragments": fragments,
        "fragment_count": len(fragments),
    }
    queue["fingerprint"] = hashlib.sha256(
        json.dumps(queue, ensure_ascii=False, sort_keys=True).encode("utf-8")
    ).hexdigest()[:12]
    return {"current_next_queue": queue}


def current_next_queue_line(summary: dict[str, Any]) -> str:
    queue = summary.get("current_next_queue")
    if not isinstance(queue, dict):
        queue = current_next_queue_summary(summary)["current_next_queue"]
    fingerprint = str(queue.get("fingerprint", ""))
    suffix = f"; sha256 {fingerprint}" if fingerprint else ""
    return (
        f"{queue.get('contract', CURRENT_NEXT_QUEUE_CONTRACT)}; "
        f"{int(queue.get('fragment_count', 0))} live fragments{suffix}"
    )


def validate_current_next_queue_text(text: str, summary: dict[str, Any]) -> list[str]:
    if "## Current Next Queue" not in text:
        return ["worklog missing '## Current Next Queue'"]
    next_queue = text.split("## Current Next Queue", 1)[1]
    normalized_next_queue = squash_spaces(next_queue)
    errors: list[str] = validate_current_next_queue_global_text(text, summary)
    for fragment in current_next_queue_expected_fragments(summary):
        if fragment not in next_queue and fragment not in normalized_next_queue:
            errors.append(f"Current Next Queue stale or missing live fragment {fragment!r}")
    return errors


def validate_current_next_queue(summary: dict[str, Any]) -> list[str]:
    if "generated_at" not in summary and "current_next_queue" not in summary:
        return []
    expected = current_next_queue_summary(summary)["current_next_queue"]
    queue = summary.get("current_next_queue")
    errors: list[str] = []
    if not isinstance(queue, dict):
        errors.append("current_next_queue missing or not an object")
    else:
        for key, expected_value in expected.items():
            if queue.get(key) != expected_value:
                errors.append(f"current_next_queue.{key} expected {expected_value!r}, observed {queue.get(key)!r}")

    try:
        path = latest_worklog_path()
        text = path.read_text(encoding="utf-8")
    except (OSError, ValueError) as exc:
        errors.append(f"current_next_queue worklog read failed: {exc}")
    else:
        actual_section = latest_worklog_section(text)
        actual_heading = actual_section[0] if actual_section else ""
        summary_worklog = summary.get("worklog", {}) if isinstance(summary.get("worklog"), dict) else {}
        if str(summary_worklog.get("latest_heading", "")) == actual_heading:
            errors.extend(validate_current_next_queue_text(text, summary))
    return errors


def latest_worklog_path() -> Path:
    candidates: list[tuple[str, Path]] = []
    for path in (ROOT / ".maintenance").glob("MONTHLY-UPLIFT-*.md"):
        match = WORKLOG_FILE_RE.match(path.name)
        if match:
            candidates.append((match.group(1), path))
    if not candidates:
        raise ValueError("no .maintenance/MONTHLY-UPLIFT-YYYY-MM-DD.md worklog files found")
    return sorted(candidates, key=lambda item: (item[0], item[1].name))[-1][1]


def resolve_worklog_path(path: Path) -> Path:
    if path.as_posix() in {"latest", "current"}:
        return latest_worklog_path()
    return path if path.is_absolute() else ROOT / path


def validate_expected_latest_heading(text: str, expected_latest_heading: str | None) -> list[str]:
    if not expected_latest_heading:
        return []
    expected = expected_latest_heading.strip()
    if not expected:
        return []
    section = latest_worklog_section(text)
    if section is None:
        return [f"latest loop heading missing; expected {expected!r}"]
    heading, _latest = section
    if heading != expected:
        return [f"latest loop heading {heading!r} does not match expected {expected!r}"]
    return []


def check_worklog(
    path: Path,
    live_summary: dict[str, Any] | None = None,
    expected_latest_heading: str | None = None,
) -> str:
    input_path = resolve_worklog_path(path)
    try:
        text = input_path.read_text(encoding="utf-8")
    except OSError as exc:
        raise ValueError(f"could not read worklog {path}: {exc}") from exc
    errors = validate_worklog_text(text)
    errors.extend(validate_expected_latest_heading(text, expected_latest_heading))
    if live_summary is not None:
        errors.extend(validate_current_next_queue_text(text, live_summary))
    if errors:
        raise ValueError("; ".join(errors))
    heading, _section = latest_worklog_section(text) or ("unknown", "")
    loop_count = len(list(WORKLOG_HEADING_RE.finditer(text)))
    rel_path = input_path.relative_to(ROOT).as_posix() if input_path.is_relative_to(ROOT) else str(input_path)
    return f"monthly_uplift_report worklog-check passed: {rel_path}; {loop_count} loop entries; latest {heading}.\n"


def worklog_summary() -> dict[str, Any]:
    try:
        path = latest_worklog_path()
        text = path.read_text(encoding="utf-8")
    except (OSError, ValueError) as exc:
        return {
            "status": "Review",
            "path": ".maintenance/MONTHLY-UPLIFT-*.md",
            "loop_count": 0,
            "latest_heading": "",
            "errors": [str(exc)],
        }

    errors = validate_worklog_text(text)
    section = latest_worklog_section(text)
    heading = section[0] if section else ""
    rel_path = path.relative_to(ROOT).as_posix() if path.is_relative_to(ROOT) else str(path)
    return {
        "status": "OK" if not errors else "Review",
        "path": rel_path,
        "loop_count": len(list(WORKLOG_HEADING_RE.finditer(text))),
        "latest_heading": heading,
        "errors": errors,
    }


def pack_from_path(path: str) -> str:
    return str(path).split("/", 1)[0]


def pack_base_name(pack: str) -> str:
    return pack.removesuffix("-Skills")


def read_claims_context() -> dict[str, Any]:
    if not CLAIMS_PATH.exists():
        return {
            "present": False,
            "path": ".maintenance/CLAIMS.md",
            "rows": {},
            "text": "",
            "line_count": 0,
            "row_count": 0,
            "active_row_count": 0,
            "fingerprint": "",
        }

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
    return {
        "present": True,
        "path": ".maintenance/CLAIMS.md",
        "rows": rows,
        "text": text,
        "line_count": len(text.splitlines()),
        "row_count": len(rows),
        "active_row_count": sum(active_claim_status(row["status"]) for row in rows.values()),
        "fingerprint": hashlib.sha256(text.encode("utf-8")).hexdigest()[:12],
    }


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
    if "agent b" in text_lower and any(keyword in base_lower for keyword in AGENT_B_KEYWORDS):
        return "Agent B natural-science/medicine lane covers this pack family"
    if "agent c" in text_lower and any(keyword in base_lower for keyword in AGENT_C_KEYWORDS):
        return "Agent C social-science/humanities lane is marked uncommitted or awaiting review"
    if "agent c" in text_lower and any(keyword in base_lower for keyword in AGENT_C_CATEGORY_KEYWORDS):
        return "Agent C category 3/7/9 lane covers humanities, engineering, agriculture, or environment packs"
    if active_claim_text_near_pack(base, str(claims.get("text", ""))):
        return "Claims text mentions this pack in an active, queued, uncommitted, or awaiting-review lane"
    return ""


def claims_summary(
    quality: dict[str, Any],
    execution_bridge: dict[str, Any],
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

    for row in execution_bridge["missing_packs"]:
        pack = str(row["pack"])
        reason = claim_reason_for_pack(pack, claims)
        if reason:
            sensitive_packs[pack] = reason
            current_targets.append({"kind": "execution-bridge", "pack": pack, "reason": reason})

    return {
        "path": claims["path"],
        "present": bool(claims.get("present")),
        "line_count": int(claims.get("line_count", 0)),
        "row_count": int(claims.get("row_count", 0)),
        "active_row_count": int(claims.get("active_row_count", 0)),
        "fingerprint": str(claims.get("fingerprint", "")),
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
    execution_bridge_rows: list[dict[str, Any]],
    claims: dict[str, Any],
    dirty_packs: set[str],
    limit: int,
) -> dict[str, list[dict[str, Any]]]:
    score_candidates: list[dict[str, Any]] = []
    score_ceiling: list[dict[str, Any]] = []
    for row in sorted(quality_rows, key=lambda item: (float(item["score"]), str(item["pack"]))):
        pack = str(row["pack"])
        if pack in dirty_packs:
            continue
        if claim_reason_for_pack(pack, claims):
            continue
        ceiling_reason = score_ceiling_reason(row)
        if ceiling_reason:
            score_ceiling.append(
                {
                    "score": float(row["score"]),
                    "pack": pack,
                    "weakest_skill": weakest_skill_path(row),
                    "reason": ceiling_reason,
                }
            )
            if len(score_ceiling) >= limit and len(score_candidates) >= limit:
                break
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
        pack = pack_from_path(path)
        if pack in dirty_packs:
            continue
        if claim_reason_for_pack(pack, claims):
            continue
        source_candidates.append({"unresolved_flags": unresolved, "path": path})
        if len(source_candidates) >= limit:
            break

    bridge_candidates: list[dict[str, Any]] = []
    sorted_bridge_rows = sorted(
        execution_bridge_rows,
        key=lambda item: (float(item.get("score", 0)), str(item.get("pack", ""))),
    )
    for row in sorted_bridge_rows:
        pack = str(row.get("pack", ""))
        if not pack:
            continue
        if pack in dirty_packs:
            continue
        if claim_reason_for_pack(pack, claims):
            continue
        bridge_candidates.append(
            {
                "pack": pack,
                "score": float(row.get("score", 0)),
                "current_bridge_links": int(row.get("exec_bridge_skills", 0)),
                "weakest_skill": weakest_skill_path(row),
            }
        )
        if len(bridge_candidates) >= limit:
            break

    return {
        "score_unclaimed": score_candidates,
        "score_ceiling": score_ceiling[:limit],
        "source_map_unclaimed": source_candidates,
        "execution_bridge_unclaimed": bridge_candidates,
        "dirty_skipped_packs": [{"pack": pack} for pack in sorted(dirty_packs)],
    }


def loop_control_summary(
    execution_bridge: dict[str, Any],
    claims_context: dict[str, Any],
    claims: dict[str, Any],
    candidate_pool_data: dict[str, list[dict[str, Any]]],
) -> dict[str, Any]:
    score_candidates = candidate_pool_data.get("score_unclaimed", [])
    source_candidates = candidate_pool_data.get("source_map_unclaimed", [])
    bridge_candidates = candidate_pool_data.get("execution_bridge_unclaimed", [])
    dirty_skipped = candidate_pool_data.get("dirty_skipped_packs", [])

    sensitive_counts = {"score-floor": 0, "source-map": 0, "execution-bridge": 0}
    for row in claims.get("sensitive_current_targets", []):
        kind = str(row.get("kind", ""))
        if kind in sensitive_counts:
            sensitive_counts[kind] += 1

    has_unclaimed_work = bool(score_candidates or source_candidates or bridge_candidates)
    has_sensitive_work = any(sensitive_counts.values())
    if has_unclaimed_work:
        status = "content-candidates"
        next_lane = "content"
        reason = "unclaimed score/source/bridge candidates are available after claim and dirty-pack filtering"
    elif has_sensitive_work:
        status = "owner-clearance-needed"
        next_lane = "tooling-or-owner-clearance"
        reason = "all visible content debt is claim-sensitive or already dirty; avoid content edits without owner clearance"
    else:
        status = "monitoring-tooling"
        next_lane = "tooling"
        reason = "no unclaimed or claim-sensitive content debt is visible in the current target window"

    return {
        "status": status,
        "next_lane": next_lane,
        "reason": reason,
        "unclaimed_score_candidates": len(score_candidates),
        "unclaimed_source_map_candidates": len(source_candidates),
        "unclaimed_execution_bridge_candidates": len(bridge_candidates),
        "claim_sensitive_score_targets": sensitive_counts["score-floor"],
        "claim_sensitive_source_map_targets": sensitive_counts["source-map"],
        "claim_sensitive_execution_bridge_targets": sensitive_counts["execution-bridge"],
        "dirty_skipped_packs": len(dirty_skipped),
    }


def expected_loop_control(summary: dict[str, Any]) -> dict[str, Any]:
    candidate_pool_data = summary.get("candidate_pool", {})
    claims = summary.get("claims", {})
    execution_bridge = summary.get("execution_bridge", {})

    score_candidates = candidate_pool_data.get("score_unclaimed", [])
    source_candidates = candidate_pool_data.get("source_map_unclaimed", [])
    bridge_candidates = candidate_pool_data.get("execution_bridge_unclaimed", [])
    dirty_skipped = candidate_pool_data.get("dirty_skipped_packs", [])

    sensitive_counts = {"score-floor": 0, "source-map": 0, "execution-bridge": 0}
    for row in claims.get("sensitive_current_targets", []):
        kind = str(row.get("kind", ""))
        if kind in sensitive_counts:
            sensitive_counts[kind] += 1

    has_unclaimed_work = bool(score_candidates or source_candidates or bridge_candidates)
    has_sensitive_work = any(sensitive_counts.values())
    if has_unclaimed_work:
        status = "content-candidates"
        next_lane = "content"
    elif has_sensitive_work:
        status = "owner-clearance-needed"
        next_lane = "tooling-or-owner-clearance"
    else:
        status = "monitoring-tooling"
        next_lane = "tooling"

    return {
        "status": status,
        "next_lane": next_lane,
        "unclaimed_score_candidates": len(score_candidates),
        "unclaimed_source_map_candidates": len(source_candidates),
        "unclaimed_execution_bridge_candidates": len(bridge_candidates),
        "claim_sensitive_score_targets": sensitive_counts["score-floor"],
        "claim_sensitive_source_map_targets": sensitive_counts["source-map"],
        "claim_sensitive_execution_bridge_targets": sensitive_counts["execution-bridge"],
        "dirty_skipped_packs": len(dirty_skipped),
    }


def validate_summary(summary: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if "generated_at" in summary:
        errors.extend(validate_schema_contract(summary))
    errors.extend(validate_worktree_boundary(summary))
    errors.extend(validate_external_links(summary))
    errors.extend(validate_command_plan(summary))
    errors.extend(validate_next_batch_plan(summary))
    errors.extend(validate_execution_bridge_tail(summary))
    errors.extend(validate_safe_content_queue(summary))
    errors.extend(validate_content_edit_policy(summary))
    errors.extend(validate_remaining_debt(summary))
    errors.extend(validate_publish_policy(summary))
    errors.extend(validate_goal_progress(summary))
    errors.extend(validate_completion_audit(summary))
    errors.extend(validate_handoff_manifest(summary))
    errors.extend(validate_skillopt_gate_plan(summary))
    errors.extend(validate_current_next_queue(summary))
    loop_control = summary.get("loop_control")
    if not isinstance(loop_control, dict):
        return ["missing loop_control summary"]

    for key, expected in expected_loop_control(summary).items():
        observed = loop_control.get(key)
        if observed != expected:
            errors.append(f"loop_control.{key} expected {expected!r}, observed {observed!r}")

    candidate_pool_data = summary.get("candidate_pool", {})
    dirty_packs = {
        str(row.get("pack", ""))
        for row in candidate_pool_data.get("dirty_skipped_packs", [])
    }
    sensitive_packs = set(summary.get("claims", {}).get("sensitive_packs", {}))

    claims = summary.get("claims")
    if not isinstance(claims, dict):
        errors.append("missing claims summary")
    else:
        if not claims.get("present"):
            errors.append("claims boundary: .maintenance/CLAIMS.md is missing")
        if int(claims.get("row_count", 0)) <= 0:
            errors.append("claims boundary: no parsed claim rows")
        if claims.get("present") and not str(claims.get("fingerprint", "")):
            errors.append("claims boundary: missing fingerprint")

    for row in candidate_pool_data.get("score_unclaimed", []):
        pack = str(row.get("pack", ""))
        if pack in dirty_packs:
            errors.append(f"score candidate {pack} is already dirty")
        if pack in sensitive_packs:
            errors.append(f"score candidate {pack} is claim-sensitive")

    for row in candidate_pool_data.get("source_map_unclaimed", []):
        path = str(row.get("path", ""))
        pack = pack_from_path(path)
        if pack in dirty_packs:
            errors.append(f"source-map candidate {path} is already dirty")
        if pack in sensitive_packs:
            errors.append(f"source-map candidate {path} is claim-sensitive")

    missing_bridge_packs = {
        str(row.get("pack", ""))
        for row in summary.get("execution_bridge", {}).get("missing_packs", [])
    }
    for row in candidate_pool_data.get("execution_bridge_unclaimed", []):
        pack = str(row.get("pack", ""))
        if pack in dirty_packs:
            errors.append(f"execution-bridge candidate {pack} is already dirty")
        if pack in sensitive_packs:
            errors.append(f"execution-bridge candidate {pack} is claim-sensitive")
        if pack not in missing_bridge_packs:
            errors.append(f"execution-bridge candidate {pack} is not in the missing bridge tail")

    worklog = summary.get("worklog")
    if not isinstance(worklog, dict):
        errors.append("missing worklog summary")
    elif worklog.get("status") != "OK":
        for error in worklog.get("errors", []) or ["worklog status is not OK"]:
            errors.append(f"worklog: {error}")

    queue = summary.get("owner_clearance_queue")
    if not isinstance(queue, dict):
        errors.append("missing owner_clearance_queue summary")
    else:
        expected_queue = owner_clearance_queue(summary)
        for key in ("contract", "total", "fingerprint"):
            if queue.get(key) != expected_queue.get(key):
                errors.append(
                    f"owner_clearance_queue.{key} expected {expected_queue.get(key)!r}, observed {queue.get(key)!r}"
                )
        expected_totals = claim_sensitive_group_totals(summary)
        for kind in OWNER_CLEARANCE_KINDS:
            expected_total = expected_totals.get(kind, 0)
            expected_row = expected_queue.get(kind)
            row = queue.get(kind)
            if expected_total == 0 and row is None:
                continue
            if not isinstance(row, dict):
                errors.append(f"owner_clearance_queue.{kind} missing")
                continue
            if not isinstance(expected_row, dict):
                errors.append(f"owner_clearance_queue.{kind} unexpected")
                continue
            displayed = row.get("displayed", [])
            if not isinstance(displayed, list):
                errors.append(f"owner_clearance_queue.{kind}.displayed must be a list")
                displayed = []
            targets = row.get("targets", [])
            if not isinstance(targets, list):
                errors.append(f"owner_clearance_queue.{kind}.targets must be a list")
                targets = []
            expected_displayed = expected_row.get("displayed", [])
            expected_targets = expected_row.get("targets", [])
            display_limit = int(row.get("display_limit", 0))
            expected_display_limit = int(expected_row.get("display_limit", 0))
            omitted = int(expected_row.get("omitted", 0))
            if row.get("total") != expected_total:
                errors.append(f"owner_clearance_queue.{kind}.total expected {expected_total}, observed {row.get('total')!r}")
            if display_limit != expected_display_limit:
                errors.append(
                    f"owner_clearance_queue.{kind}.display_limit expected {expected_display_limit}, observed {display_limit}"
                )
            if displayed != expected_displayed:
                errors.append(f"owner_clearance_queue.{kind}.displayed does not match claims boundary")
            if targets != expected_targets:
                errors.append(f"owner_clearance_queue.{kind}.targets does not match claims boundary")
            if row.get("target_fingerprint") != expected_row.get("target_fingerprint"):
                errors.append(
                    "owner_clearance_queue."
                    f"{kind}.target_fingerprint expected {expected_row.get('target_fingerprint')!r}, "
                    f"observed {row.get('target_fingerprint')!r}"
                )
            if row.get("total") != len(targets):
                errors.append(
                    f"owner_clearance_queue.{kind}.total {row.get('total')!r} does not match targets length {len(targets)}"
                )
            if row.get("omitted") != omitted:
                errors.append(f"owner_clearance_queue.{kind}.omitted expected {omitted}, observed {row.get('omitted')!r}")
            if bool(row.get("truncated")) != bool(omitted):
                errors.append(f"owner_clearance_queue.{kind}.truncated expected {bool(omitted)}, observed {row.get('truncated')!r}")
            if display_limit < len(displayed):
                errors.append(
                    f"owner_clearance_queue.{kind}.display_limit {display_limit} is smaller than displayed rows {len(displayed)}"
                )

    git = summary.get("git")
    if isinstance(git, dict):
        dirty_pack_names_value = git.get("dirty_pack_names", [])
        dirty_pack_paths_value = git.get("dirty_pack_paths", [])
        dirty_root_lines_value = git.get("dirty_root_lines", [])
        dirty_root_paths_value = git.get("dirty_root_paths", [])
        dirty_root_tracked_paths_value = git.get("dirty_root_tracked_paths", [])
        dirty_root_untracked_paths_value = git.get("dirty_root_untracked_paths", [])
        dirty_pack_names_list = dirty_pack_names_value if isinstance(dirty_pack_names_value, list) else []
        dirty_pack_paths_list = dirty_pack_paths_value if isinstance(dirty_pack_paths_value, list) else []
        dirty_root_lines_list = dirty_root_lines_value if isinstance(dirty_root_lines_value, list) else []
        dirty_root_paths_list = dirty_root_paths_value if isinstance(dirty_root_paths_value, list) else []
        dirty_root_tracked_paths_list = (
            dirty_root_tracked_paths_value if isinstance(dirty_root_tracked_paths_value, list) else []
        )
        dirty_root_untracked_paths_list = (
            dirty_root_untracked_paths_value if isinstance(dirty_root_untracked_paths_value, list) else []
        )
        if int(git.get("dirty_pack_count", len(dirty_pack_names_list))) != len(dirty_pack_names_list):
            errors.append("git.dirty_pack_count does not match dirty_pack_names")
        if int(git.get("dirty_pack_path_count", len(dirty_pack_paths_list))) != len(dirty_pack_paths_list):
            errors.append("git.dirty_pack_path_count does not match dirty_pack_paths")
        if int(git.get("dirty_root_count", len(dirty_root_lines_list))) != len(dirty_root_lines_list):
            errors.append("git.dirty_root_count does not match dirty_root_lines")
        if int(git.get("dirty_root_path_count", len(dirty_root_paths_list))) != len(dirty_root_paths_list):
            errors.append("git.dirty_root_path_count does not match dirty_root_paths")
        if int(git.get("dirty_root_tracked_path_count", len(dirty_root_tracked_paths_list))) != len(dirty_root_tracked_paths_list):
            errors.append("git.dirty_root_tracked_path_count does not match dirty_root_tracked_paths")
        if int(git.get("dirty_root_untracked_path_count", len(dirty_root_untracked_paths_list))) != len(dirty_root_untracked_paths_list):
            errors.append("git.dirty_root_untracked_path_count does not match dirty_root_untracked_paths")
        if unique_ordered([str(path) for path in dirty_root_tracked_paths_list + dirty_root_untracked_paths_list]) != [
            str(path) for path in dirty_root_paths_list
        ]:
            errors.append("git dirty root tracked/untracked paths do not reconcile to dirty_root_paths")
        expected_root_command = git_add_command([str(path) for path in dirty_root_paths_list])
        if str(git.get("dirty_root_pathspec_command", "")) != expected_root_command:
            errors.append("git.dirty_root_pathspec_command does not match dirty_root_paths")
        for path in dirty_pack_paths_list:
            if not pack_from_path(str(path)).endswith("-Skills"):
                errors.append(f"git.dirty_pack_paths contains non-pack path {path}")
        for path in dirty_root_paths_list:
            if pack_from_path(str(path)).endswith("-Skills"):
                errors.append(f"git.dirty_root_paths contains pack path {path}")
        for path in dirty_root_tracked_paths_list:
            if pack_from_path(str(path)).endswith("-Skills"):
                errors.append(f"git.dirty_root_tracked_paths contains pack path {path}")
        for path in dirty_root_untracked_paths_list:
            if pack_from_path(str(path)).endswith("-Skills"):
                errors.append(f"git.dirty_root_untracked_paths contains pack path {path}")

        units = summary.get("publish_units")
        if isinstance(units, dict):
            expected_units = publish_units_from_git(git)
            root_unit = units.get("root_tooling")
            pack_unit = units.get("pack_content")
            if not isinstance(root_unit, dict):
                errors.append("publish_units.root_tooling missing")
            else:
                expected_root = expected_units["root_tooling"]
                for key in (
                    "status",
                    "paths",
                    "path_count",
                    "tracked_paths",
                    "tracked_path_count",
                    "untracked_paths",
                    "untracked_path_count",
                    "staging_command",
                ):
                    if root_unit.get(key) != expected_root.get(key):
                        errors.append(f"publish_units.root_tooling.{key} does not match git dirty root paths")
            if not isinstance(pack_unit, dict):
                errors.append("publish_units.pack_content missing")
            else:
                expected_pack = expected_units["pack_content"]
                for key in ("status", "packs", "pack_count", "paths", "path_count"):
                    if pack_unit.get(key) != expected_pack.get(key):
                        errors.append(f"publish_units.pack_content.{key} does not match git dirty pack paths")

    return errors


def external_links_fixture() -> dict[str, Any]:
    advisory = {
        "contract": EXTERNAL_LINKS_CONTRACT,
        "status": "actionable-review",
        "include_infra": False,
        "cache_path": "tools/.cache/external_links.json",
        "cache_present": True,
        "cache_entry_count": 9,
        "current_cache_entry_count": 8,
        "orphaned_cache_entry_count": 1,
        "url_count": 10,
        "checked_count": 8,
        "unchecked_count": 2,
        "actionable_count": 1,
        "inconclusive_count": 2,
        "counts": {
            "OK": 5,
            "DEAD": 1,
            "REDIRECT": 0,
            "BLOCKED": 1,
            "UNREACHABLE": 1,
            "UNCHECKED": 2,
        },
    }
    advisory["fingerprint"] = external_links_fingerprint(advisory)
    return {"external_links": advisory}


def loop_control_fixture(
    *,
    score_candidates: list[dict[str, Any]] | None = None,
    source_candidates: list[dict[str, Any]] | None = None,
    bridge_candidates: list[dict[str, Any]] | None = None,
    dirty_skipped: list[dict[str, Any]] | None = None,
    sensitive_packs: dict[str, str] | None = None,
    sensitive_targets: list[dict[str, str]] | None = None,
    missing_bridge: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    summary: dict[str, Any] = {
        "candidate_pool": {
            "score_unclaimed": score_candidates or [],
            "source_map_unclaimed": source_candidates or [],
            "execution_bridge_unclaimed": bridge_candidates or [],
            "dirty_skipped_packs": dirty_skipped or [],
        },
        "claims": {
            "present": True,
            "path": ".maintenance/CLAIMS.md",
            "line_count": 3,
            "row_count": 1,
            "active_row_count": 1,
            "fingerprint": "fixture",
            "sensitive_packs": sensitive_packs or {},
            "sensitive_current_targets": sensitive_targets or [],
        },
        "execution_bridge": {
            "missing_packs": missing_bridge or [],
        },
        "worklog": {
            "status": "OK",
            "path": ".maintenance/MONTHLY-UPLIFT-2026-06-27.md",
            "loop_count": 35,
            "latest_heading": "### 2026-06-27 - Fixture Loop",
            "errors": [],
        },
        **external_links_fixture(),
        **command_plan_summary(),
    }
    summary["loop_control"] = {**expected_loop_control(summary), "reason": "fixture"}
    summary["owner_clearance_queue"] = owner_clearance_queue(summary)
    summary.update(execution_bridge_tail_summary(summary))
    summary.update(safe_content_queue_summary(summary))
    return summary


def handoff_fixture() -> dict[str, Any]:
    summary = loop_control_fixture(
        score_candidates=[
            {
                "pack": "Unclaimed-Pack",
                "score": 90.0,
                "weakest_skill": "Unclaimed-Pack/skills/fixture/SKILL.md",
            }
        ]
    )
    summary.update(
        {
            "generated_at": "2026-06-27T00:00:00-07:00",
            "counts": {"skills": 2902, "packs": 195, "root_entries": 200},
            "quality": {
                "pack_count": 195,
                "mean": 93.6,
                "min": 90.0,
                "below_target": 0,
                "worst": [
                    {
                        "score": 90.0,
                        "pack": "Fixture-Pack",
                        "weak_skills": [{"path": "Fixture-Pack/skills/fixture/SKILL.md"}],
                    }
                ],
            },
            "source_maps": {
                "map_count": 194,
                "warnings": 0,
                "max_unresolved": 14,
                "highest_unresolved": [
                    {
                        "unresolved_flags": 14,
                        "path": "Fixture-Pack/resources/official-source-map.md",
                    }
                ],
            },
            "root_entries": {"entry_count": 200, "enriched": 200, "machine_only": 0, "warnings": 0},
            "execution_bridge": {"empirical_depth_packs": 134, "wired": 131, "missing": 3, "missing_packs": []},
            "clone_audit": None,
            "git": {
                "branch": "## main...origin/main",
                "dirty_lines": [" M tools/monthly_uplift_report.py"],
                "dirty_count": 1,
                "dirty_pack_names": [],
                "dirty_pack_count": 0,
                "dirty_pack_paths": [],
                "dirty_pack_path_count": 0,
                "dirty_root_lines": [" M tools/monthly_uplift_report.py"],
                "dirty_root_count": 1,
                "dirty_root_paths": ["tools/monthly_uplift_report.py"],
                "dirty_root_path_count": 1,
                "dirty_root_tracked_paths": ["tools/monthly_uplift_report.py"],
                "dirty_root_tracked_path_count": 1,
                "dirty_root_untracked_paths": [],
                "dirty_root_untracked_path_count": 0,
                "dirty_root_pathspec_command": "git add -- tools/monthly_uplift_report.py",
            },
            "targets": {"score_floor": 90.0, "clone_fail_threshold": 0.90, "display_limit": 20},
            **schema_summary(),
        }
    )
    summary.update(worktree_boundary_summary(summary["git"]))
    summary["publish_units"] = publish_units_from_git(summary["git"])
    summary.update(execution_bridge_tail_summary(summary))
    summary.update(safe_content_queue_summary(summary))
    summary.update(content_edit_policy_summary(summary))
    summary.update(remaining_debt_summary(summary))
    summary.update(next_batch_plan_summary(summary))
    summary.update(publish_policy_summary(summary))
    summary.update(skillopt_gate_plan_summary(summary))
    summary.update(goal_progress_summary(summary))
    summary.update(completion_audit_summary(summary))
    summary.update(handoff_manifest_summary(summary))
    summary.update(current_next_queue_summary(summary))
    summary.update(schema_summary(summary))
    return summary


def self_test_errors() -> list[str]:
    errors: list[str] = []
    cases = [
        (
            "content-candidates",
            loop_control_fixture(score_candidates=[{"pack": "Unclaimed-Pack"}]),
            {"status": "content-candidates", "next_lane": "content", "unclaimed_score_candidates": 1},
        ),
        (
            "bridge-content-candidates",
            loop_control_fixture(
                bridge_candidates=[
                    {
                        "pack": "Bridge-Pack",
                        "score": 91.0,
                        "current_bridge_links": 0,
                        "weakest_skill": "Bridge-Pack/skills/fixture/SKILL.md",
                    }
                ],
                missing_bridge=[{"pack": "Bridge-Pack"}],
            ),
            {
                "status": "content-candidates",
                "next_lane": "content",
                "unclaimed_execution_bridge_candidates": 1,
            },
        ),
        (
            "owner-clearance-needed",
            loop_control_fixture(
                sensitive_packs={"Claimed-Pack": "claimed"},
                sensitive_targets=[
                    {"kind": "score-floor", "pack": "Claimed-Pack", "reason": "claimed"},
                    {"kind": "execution-bridge", "pack": "Claimed-Pack", "reason": "claimed"},
                ],
                missing_bridge=[{"pack": "Claimed-Pack"}],
            ),
            {
                "status": "owner-clearance-needed",
                "next_lane": "tooling-or-owner-clearance",
                "claim_sensitive_score_targets": 1,
                "claim_sensitive_execution_bridge_targets": 1,
                "unclaimed_execution_bridge_candidates": 0,
            },
        ),
        (
            "monitoring-tooling",
            loop_control_fixture(),
            {"status": "monitoring-tooling", "next_lane": "tooling"},
        ),
    ]

    for name, summary, expected in cases:
        observed_errors = validate_summary(summary)
        if observed_errors:
            errors.append(f"{name}: expected no validation errors, got {observed_errors}")
        loop_control = summary["loop_control"]
        for key, value in expected.items():
            if loop_control.get(key) != value:
                errors.append(f"{name}: loop_control.{key} expected {value!r}, observed {loop_control.get(key)!r}")

    stale_measurement_plan = handoff_fixture()
    stale_measurement_plan["measurement_commands"] = ["python3 tools/audit_repo.py --counts"]
    if not any("measurement_commands" in error for error in validate_summary(stale_measurement_plan)):
        errors.append("stale measurement command plan was not rejected")

    stale_validation_plan = handoff_fixture()
    stale_validation_plan["validation_commands"] = list(NEXT_LOOP_VALIDATION_COMMANDS[:-1])
    if not any("validation_commands" in error for error in validate_summary(stale_validation_plan)):
        errors.append("stale validation command plan was not rejected")

    stale_command_plan_metadata = handoff_fixture()
    stale_command_plan_metadata["command_plan"] = {
        **stale_command_plan_metadata["command_plan"],
        "fingerprint": "stale",
    }
    if not any("command_plan.fingerprint" in error for error in validate_summary(stale_command_plan_metadata)):
        errors.append("stale command-plan fingerprint was not rejected")

    missing_schema = handoff_fixture()
    missing_schema.pop("schema", None)
    if not any("schema" in error for error in validate_summary(missing_schema)):
        errors.append("missing dashboard schema was not rejected")

    stale_schema = handoff_fixture()
    stale_schema["schema"] = {**stale_schema["schema"], "version": 0}
    if not any("schema.version" in error for error in validate_summary(stale_schema)):
        errors.append("stale dashboard schema version was not rejected")

    stale_schema_nested_contract = handoff_fixture()
    stale_schema_nested_contract["schema"] = {
        **stale_schema_nested_contract["schema"],
        "nested_contracts": {
            **stale_schema_nested_contract["schema"]["nested_contracts"],
            "handoff_manifest": "stale",
        },
    }
    if not any("schema.nested_contracts" in error for error in validate_summary(stale_schema_nested_contract)):
        errors.append("stale dashboard nested-contract registry was not rejected")

    stale_schema_nested_fingerprint = handoff_fixture()
    stale_schema_nested_fingerprint["schema"] = {
        **stale_schema_nested_fingerprint["schema"],
        "nested_contracts_fingerprint": "stale",
    }
    if not any("schema.nested_contracts_fingerprint" in error for error in validate_summary(stale_schema_nested_fingerprint)):
        errors.append("stale dashboard nested-contract fingerprint was not rejected")

    stale_worktree_boundary = handoff_fixture()
    stale_worktree_boundary["worktree_boundary"] = {
        **stale_worktree_boundary["worktree_boundary"],
        "fingerprint": "stale",
    }
    if not any("worktree_boundary.fingerprint" in error for error in validate_summary(stale_worktree_boundary)):
        errors.append("stale worktree-boundary fingerprint was not rejected")

    stale_external_links = handoff_fixture()
    stale_external_links["external_links"] = {
        **stale_external_links["external_links"],
        "fingerprint": "stale",
    }
    if not any("external_links.fingerprint" in error for error in validate_summary(stale_external_links)):
        errors.append("stale external-links fingerprint was not rejected")

    stale_handoff_manifest = handoff_fixture()
    stale_handoff_manifest["handoff_manifest"] = {
        **stale_handoff_manifest["handoff_manifest"],
        "fingerprint": "stale",
    }
    if not any("handoff_manifest.fingerprint" in error for error in validate_summary(stale_handoff_manifest)):
        errors.append("stale handoff-manifest fingerprint was not rejected")

    stale_handoff_manifest_contract = handoff_fixture()
    stale_handoff_manifest_contract["handoff_manifest"] = {
        **stale_handoff_manifest_contract["handoff_manifest"],
        "contract": "stale",
    }
    if not any("handoff_manifest.contract" in error for error in validate_summary(stale_handoff_manifest_contract)):
        errors.append("stale handoff-manifest contract was not rejected")

    stale_handoff_manifest_completion = handoff_fixture()
    stale_handoff_manifest_completion["handoff_manifest"] = {
        **stale_handoff_manifest_completion["handoff_manifest"],
        "completion_audit_requirement_count": 99,
    }
    if not any("handoff_manifest.completion_audit_requirement_count" in error for error in validate_summary(stale_handoff_manifest_completion)):
        errors.append("stale handoff-manifest completion requirement count was not rejected")

    stale_current_next_queue = handoff_fixture()
    stale_current_next_queue["current_next_queue"] = {
        **stale_current_next_queue["current_next_queue"],
        "fingerprint": "stale",
    }
    if not any("current_next_queue.fingerprint" in error for error in validate_summary(stale_current_next_queue)):
        errors.append("stale current-next-queue fingerprint was not rejected")

    full_clone_current_next_queue = handoff_fixture()
    full_clone_current_next_queue["clone_audit"] = {
        "max_score": 0.0,
        "fail_hits": 0,
        "reported_pairs": 0,
    }
    full_clone_current_next_queue.update(goal_progress_summary(full_clone_current_next_queue))
    full_clone_current_next_queue.update(completion_audit_summary(full_clone_current_next_queue))
    full_clone_current_next_queue.update(handoff_manifest_summary(full_clone_current_next_queue))
    full_clone_current_next_queue.update(current_next_queue_summary(full_clone_current_next_queue))
    full_clone_fragments = current_next_queue_expected_fragments(full_clone_current_next_queue)
    skip_clone_fragments = current_next_queue_expected_fragments(handoff_fixture())
    full_clone_required_fragments = (
        f"goal-progress status `{full_clone_current_next_queue['goal_progress']['status']}`",
        f"fingerprint `{full_clone_current_next_queue['goal_progress']['fingerprint']}`",
        f"completion-audit status `{full_clone_current_next_queue['completion_audit']['completion_status']}`",
        f"fingerprint `{full_clone_current_next_queue['completion_audit']['fingerprint']}`",
    )
    for fragment in full_clone_required_fragments:
        if fragment not in full_clone_fragments:
            errors.append(f"full clone Current Next Queue fragments missing {fragment!r}")
        if fragment in skip_clone_fragments:
            errors.append(f"skip-clone Current Next Queue fragments unexpectedly required {fragment!r}")

    bridge_pack_queue = handoff_fixture()
    bridge_pack_fragments = current_next_queue_expected_fragments(bridge_pack_queue)
    bridge_pack_fragment = f"execution-bridge pack decision `{execution_bridge_tail_pack_line(bridge_pack_queue)}`"
    if bridge_pack_fragment not in bridge_pack_fragments:
        errors.append(f"Current Next Queue fragments missing bridge-pack decision fragment {bridge_pack_fragment!r}")
    missing_bridge_pack_text = "## Current Next Queue\n" + "\n".join(
        f"- {fragment}"
        for fragment in bridge_pack_fragments
        if fragment != bridge_pack_fragment
    )
    missing_bridge_pack_errors = validate_current_next_queue_text(
        missing_bridge_pack_text,
        bridge_pack_queue,
    )
    if not any(bridge_pack_fragment in error for error in missing_bridge_pack_errors):
        errors.append("missing bridge-pack decision fragment was not rejected")

    owner_queue_fragments = current_next_queue_expected_fragments(bridge_pack_queue)
    owner_queue_fragment = f"owner-clearance queue `{owner_clearance_queue_line(bridge_pack_queue)}`"
    if owner_queue_fragment not in owner_queue_fragments:
        errors.append(f"Current Next Queue fragments missing owner-clearance queue fragment {owner_queue_fragment!r}")
    missing_owner_queue_text = "## Current Next Queue\n" + "\n".join(
        f"- {fragment}"
        for fragment in owner_queue_fragments
        if fragment != owner_queue_fragment
    )
    missing_owner_queue_errors = validate_current_next_queue_text(
        missing_owner_queue_text,
        bridge_pack_queue,
    )
    if not any(owner_queue_fragment in error for error in missing_owner_queue_errors):
        errors.append("missing owner-clearance queue fragment was not rejected")

    owner_target_fragment = (
        f"owner-clearance target fingerprints `{owner_clearance_target_fingerprint_line(bridge_pack_queue)}`"
    )
    if owner_target_fragment not in owner_queue_fragments:
        errors.append(
            f"Current Next Queue fragments missing owner-clearance target fingerprint fragment {owner_target_fragment!r}"
        )
    missing_owner_target_text = "## Current Next Queue\n" + "\n".join(
        f"- {fragment}"
        for fragment in owner_queue_fragments
        if fragment != owner_target_fragment
    )
    missing_owner_target_errors = validate_current_next_queue_text(
        missing_owner_target_text,
        bridge_pack_queue,
    )
    if not any(owner_target_fragment in error for error in missing_owner_target_errors):
        errors.append("missing owner-clearance target fingerprint fragment was not rejected")

    completion_owner_target_fragment = (
        "completion-audit owner target fingerprints "
        f"`{completion_audit_owner_target_fingerprint_line(bridge_pack_queue)}`"
    )
    if completion_owner_target_fragment not in owner_queue_fragments:
        errors.append(
            "Current Next Queue fragments missing completion-audit owner target fingerprint "
            f"fragment {completion_owner_target_fragment!r}"
        )
    missing_completion_owner_target_text = "## Current Next Queue\n" + "\n".join(
        f"- {fragment}"
        for fragment in owner_queue_fragments
        if fragment != completion_owner_target_fragment
    )
    missing_completion_owner_target_errors = validate_current_next_queue_text(
        missing_completion_owner_target_text,
        bridge_pack_queue,
    )
    if not any(completion_owner_target_fragment in error for error in missing_completion_owner_target_errors):
        errors.append("missing completion-audit owner target fingerprint fragment was not rejected")

    external_class_fragments = current_next_queue_expected_fragments(bridge_pack_queue)
    external_class_fragment = f"external-link classes `{external_links_breakdown_line(bridge_pack_queue)}`"
    if external_class_fragment not in external_class_fragments:
        errors.append(f"Current Next Queue fragments missing external-link class fragment {external_class_fragment!r}")
    missing_external_class_text = "## Current Next Queue\n" + "\n".join(
        f"- {fragment}"
        for fragment in external_class_fragments
        if fragment != external_class_fragment
    )
    missing_external_class_errors = validate_current_next_queue_text(
        missing_external_class_text,
        bridge_pack_queue,
    )
    if not any(external_class_fragment in error for error in missing_external_class_errors):
        errors.append("missing external-link class fragment was not rejected")

    external_cache_fragments = current_next_queue_expected_fragments(bridge_pack_queue)
    external_cache_fragment = f"external-link cache coverage `{external_links_cache_line(bridge_pack_queue)}`"
    if external_cache_fragment not in external_cache_fragments:
        errors.append(f"Current Next Queue fragments missing external-link cache coverage fragment {external_cache_fragment!r}")
    missing_external_cache_text = "## Current Next Queue\n" + "\n".join(
        f"- {fragment}"
        for fragment in external_cache_fragments
        if fragment != external_cache_fragment
    )
    missing_external_cache_errors = validate_current_next_queue_text(
        missing_external_cache_text,
        bridge_pack_queue,
    )
    if not any(external_cache_fragment in error for error in missing_external_cache_errors):
        errors.append("missing external-link cache coverage fragment was not rejected")

    stable_queue_summary = handoff_fixture()
    stable_queue = current_next_queue_summary(stable_queue_summary)["current_next_queue"]
    volatile_queue_summary = json.loads(json.dumps(stable_queue_summary))
    volatile_queue_summary["worktree_boundary"] = {
        **volatile_queue_summary["worktree_boundary"],
        "dirty_count": 0,
        "dirty_root_count": 0,
        "dirty_root_path_count": 0,
        "root_staging_command": "",
        "fingerprint": "volatile-worktree",
    }
    volatile_queue_summary["publish_units"] = {
        **volatile_queue_summary["publish_units"],
        "root_tooling": {
            **volatile_queue_summary["publish_units"]["root_tooling"],
            "status": "empty",
            "path_count": 0,
            "paths": [],
            "staging_command": "",
        },
    }
    volatile_queue_summary["publish_policy"] = {
        **volatile_queue_summary["publish_policy"],
        "root_tooling_status": "empty",
        "root_tooling_path_count": 0,
        "root_tooling_staging_command": "",
        "path_scoped_staging_required": False,
        "fingerprint": "volatile-publish",
    }
    volatile_queue_summary["handoff_manifest"] = {
        **volatile_queue_summary["handoff_manifest"],
        "root_tooling_path_count": 0,
        "root_tooling_staging_command": "",
        "worktree_boundary_fingerprint": "volatile-worktree",
        "publish_policy_fingerprint": "volatile-publish",
        "fingerprint": "volatile-handoff",
    }
    volatile_queue = current_next_queue_summary(volatile_queue_summary)["current_next_queue"]
    if volatile_queue != stable_queue:
        errors.append("Current Next Queue v7 changed after volatile worktree/publish/handoff fields changed")
    for forbidden_fragment in (
        "root/tooling currently forms one ready unit with",
        "pack content currently has",
        f"fingerprint `{stable_queue_summary['publish_policy']['fingerprint']}`",
        f"fingerprint `{stable_queue_summary['handoff_manifest']['fingerprint']}`",
    ):
        if any(forbidden_fragment in fragment for fragment in stable_queue["required_fragments"]):
            errors.append(f"Current Next Queue v7 still includes volatile fragment {forbidden_fragment!r}")

    next_batch_queue = handoff_fixture()
    next_batch_fragments = current_next_queue_expected_fragments(next_batch_queue)
    next_batch_required_fragments = (
        f"`{next_batch_queue['next_batch_plan']['contract']}`",
        f"next-batch count `{next_batch_queue['next_batch_plan']['count']}`",
        f"fingerprint `{next_batch_queue['next_batch_plan']['fingerprint']}`",
    )
    for fragment in next_batch_required_fragments:
        if fragment not in next_batch_fragments:
            errors.append(f"Current Next Queue fragments missing next-batch fragment {fragment!r}")
    missing_next_batch_count_text = "## Current Next Queue\n" + "\n".join(
        f"- {fragment}"
        for fragment in next_batch_fragments
        if fragment != next_batch_required_fragments[1]
    )
    missing_next_batch_count_errors = validate_current_next_queue_text(missing_next_batch_count_text, next_batch_queue)
    if not any(next_batch_required_fragments[1] in error for error in missing_next_batch_count_errors):
        errors.append("missing next-batch count fragment was not rejected by Current Next Queue validation")

    command_plan_queue = handoff_fixture()
    command_plan_fragments = current_next_queue_expected_fragments(command_plan_queue)
    command_plan_required_fragments = (
        (
            f"plan is {command_plan_queue['command_plan']['measurement_count']} measurement commands / "
            f"{command_plan_queue['command_plan']['validation_count']} validation commands"
        ),
        "`python3 tools/quality_scorecard.py --top 15 --min-score 90`",
        f"fingerprint `{command_plan_queue['command_plan']['fingerprint']}`",
    )
    for fragment in command_plan_required_fragments:
        if fragment not in command_plan_fragments:
            errors.append(f"Current Next Queue fragments missing command-plan fragment {fragment!r}")
    missing_quality_floor_command_text = "## Current Next Queue\n" + "\n".join(
        f"- {fragment}"
        for fragment in command_plan_fragments
        if fragment != command_plan_required_fragments[1]
    )
    missing_quality_floor_errors = validate_current_next_queue_text(
        missing_quality_floor_command_text, command_plan_queue
    )
    if not any(command_plan_required_fragments[1] in error for error in missing_quality_floor_errors):
        errors.append("missing quality-floor command fragment was not rejected by Current Next Queue validation")

    stale_skillopt_plan = handoff_fixture()
    stale_skillopt_plan["skillopt_gate_plan"] = {
        **stale_skillopt_plan["skillopt_gate_plan"],
        "fingerprint": "stale",
    }
    if not any("skillopt_gate_plan.fingerprint" in error for error in validate_summary(stale_skillopt_plan)):
        errors.append("stale SkillOpt gate-plan fingerprint was not rejected")

    skillopt_queue = handoff_fixture()
    skillopt_fragments = current_next_queue_expected_fragments(skillopt_queue)
    skillopt_required_fragments = (
        f"SkillOpt snapshot command `{skillopt_queue['skillopt_gate_plan']['snapshot_command']}`",
        f"SkillOpt gate command `{skillopt_queue['skillopt_gate_plan']['gate_command']}`",
        f"SkillOpt final hard gate `{skillopt_queue['skillopt_gate_plan']['final_hard_gate']}`",
    )
    for fragment in skillopt_required_fragments:
        if fragment not in skillopt_fragments:
            errors.append(f"Current Next Queue fragments missing SkillOpt fragment {fragment!r}")
    missing_skillopt_final_gate_text = "## Current Next Queue\n" + "\n".join(
        f"- {fragment}"
        for fragment in skillopt_fragments
        if fragment != skillopt_required_fragments[2]
    )
    missing_skillopt_final_gate_errors = validate_current_next_queue_text(
        missing_skillopt_final_gate_text,
        skillopt_queue,
    )
    if not any(skillopt_required_fragments[2] in error for error in missing_skillopt_final_gate_errors):
        errors.append("missing SkillOpt final hard gate fragment was not rejected")

    worklog_args = worklog_live_summary_args(
        argparse.Namespace(
            score_target=88.0,
            limit=5,
            clone_threshold=0.72,
            clone_fail_threshold=0.91,
            clone_top=17,
        )
    )
    if worklog_args.limit != WORKLOG_LIVE_SUMMARY_LIMIT:
        errors.append("worklog live summary args did not force the canonical monthly display limit")
    if not worklog_args.skip_clone:
        errors.append("worklog live summary args did not skip clone audit")
    if worklog_args.score_target != 88.0:
        errors.append("worklog live summary args did not preserve score target")
    if worklog_args.clone_threshold != 0.72 or worklog_args.clone_fail_threshold != 0.91:
        errors.append("worklog live summary args did not preserve clone thresholds")

    stale_content_policy = handoff_fixture()
    stale_content_policy["content_edit_policy"] = {
        **stale_content_policy["content_edit_policy"],
        "fingerprint": "stale",
    }
    if not any("content_edit_policy.fingerprint" in error for error in validate_summary(stale_content_policy)):
        errors.append("stale content-edit policy fingerprint was not rejected")

    stale_bridge_tail = handoff_fixture()
    stale_bridge_tail["execution_bridge_tail"] = {
        **stale_bridge_tail["execution_bridge_tail"],
        "fingerprint": "stale",
    }
    if not any("execution_bridge_tail.fingerprint" in error for error in validate_summary(stale_bridge_tail)):
        errors.append("stale execution-bridge tail fingerprint was not rejected")

    stale_safe_queue = handoff_fixture()
    stale_safe_queue["safe_content_queue"] = {
        **stale_safe_queue["safe_content_queue"],
        "fingerprint": "stale",
    }
    if not any("safe_content_queue.fingerprint" in error for error in validate_summary(stale_safe_queue)):
        errors.append("stale safe content queue fingerprint was not rejected")

    stale_remaining_debt = handoff_fixture()
    stale_remaining_debt["remaining_debt"] = {
        **stale_remaining_debt["remaining_debt"],
        "fingerprint": "stale",
    }
    if not any("remaining_debt.fingerprint" in error for error in validate_summary(stale_remaining_debt)):
        errors.append("stale remaining-debt fingerprint was not rejected")

    stale_publish_policy = handoff_fixture()
    stale_publish_policy["publish_policy"] = {
        **stale_publish_policy["publish_policy"],
        "fingerprint": "stale",
    }
    if not any("publish_policy.fingerprint" in error for error in validate_summary(stale_publish_policy)):
        errors.append("stale publish-policy fingerprint was not rejected")

    stale_goal_progress = handoff_fixture()
    stale_goal_progress["goal_progress"] = {
        **stale_goal_progress["goal_progress"],
        "fingerprint": "stale",
    }
    if not any("goal_progress.fingerprint" in error for error in validate_summary(stale_goal_progress)):
        errors.append("stale goal-progress fingerprint was not rejected")

    stale_completion_audit = handoff_fixture()
    stale_completion_audit["completion_audit"] = {
        **stale_completion_audit["completion_audit"],
        "fingerprint": "stale",
    }
    if not any("completion_audit.fingerprint" in error for error in validate_summary(stale_completion_audit)):
        errors.append("stale completion-audit fingerprint was not rejected")

    valid_next_batch_plan = handoff_fixture()
    valid_next_batch_plan.update(remaining_debt_summary(valid_next_batch_plan))
    valid_next_batch_plan.update(next_batch_plan_summary(valid_next_batch_plan))
    valid_next_batch_plan.update(publish_policy_summary(valid_next_batch_plan))
    valid_next_batch_plan.update(skillopt_gate_plan_summary(valid_next_batch_plan))
    valid_next_batch_plan.update(goal_progress_summary(valid_next_batch_plan))
    valid_next_batch_plan.update(completion_audit_summary(valid_next_batch_plan))
    valid_next_batch_plan.update(handoff_manifest_summary(valid_next_batch_plan))
    valid_next_batch_plan.update(current_next_queue_summary(valid_next_batch_plan))
    valid_next_batch_plan.update(schema_summary(valid_next_batch_plan))
    next_batch_errors = validate_summary(valid_next_batch_plan)
    if next_batch_errors:
        errors.append(f"valid next-batch plan fixture failed: {next_batch_errors}")

    stale_next_batches = handoff_fixture()
    stale_next_batches.update(remaining_debt_summary(stale_next_batches))
    stale_next_batches.update(next_batch_plan_summary(stale_next_batches))
    stale_next_batches["next_batches"] = ["stale next batch"]
    if not any("next_batches" in error for error in validate_summary(stale_next_batches)):
        errors.append("stale next-batch list was not rejected")

    stale_next_batch_metadata = handoff_fixture()
    stale_next_batch_metadata.update(remaining_debt_summary(stale_next_batch_metadata))
    stale_next_batch_metadata.update(next_batch_plan_summary(stale_next_batch_metadata))
    stale_next_batch_metadata["next_batch_plan"] = {
        **stale_next_batch_metadata["next_batch_plan"],
        "fingerprint": "stale",
    }
    if not any("next_batch_plan.fingerprint" in error for error in validate_summary(stale_next_batch_metadata)):
        errors.append("stale next-batch fingerprint was not rejected")

    stale_next_batch_contract = handoff_fixture()
    stale_next_batch_contract.update(remaining_debt_summary(stale_next_batch_contract))
    stale_next_batch_contract.update(next_batch_plan_summary(stale_next_batch_contract))
    stale_next_batch_contract["next_batch_plan"] = {
        **stale_next_batch_contract["next_batch_plan"],
        "contract": "stale",
    }
    if not any("next_batch_plan.contract" in error for error in validate_summary(stale_next_batch_contract)):
        errors.append("stale next-batch contract was not rejected")

    dirty_score = loop_control_fixture(
        score_candidates=[{"pack": "Dirty-Pack"}],
        dirty_skipped=[{"pack": "Dirty-Pack"}],
    )
    if not any("already dirty" in error for error in validate_summary(dirty_score)):
        errors.append("dirty score candidate was not rejected")

    dirty_source = loop_control_fixture(
        source_candidates=[{"path": "Dirty-Pack/resources/official-source-map.md"}],
        dirty_skipped=[{"pack": "Dirty-Pack"}],
    )
    if not any("already dirty" in error for error in validate_summary(dirty_source)):
        errors.append("dirty source-map candidate was not rejected")

    sensitive_score = loop_control_fixture(
        score_candidates=[{"pack": "Sensitive-Pack"}],
        sensitive_packs={"Sensitive-Pack": "claimed"},
    )
    if not any("claim-sensitive" in error for error in validate_summary(sensitive_score)):
        errors.append("claim-sensitive score candidate was not rejected")

    sensitive_source = loop_control_fixture(
        source_candidates=[{"path": "Sensitive-Pack/resources/official-source-map.md"}],
        sensitive_packs={"Sensitive-Pack": "claimed"},
    )
    if not any("claim-sensitive" in error for error in validate_summary(sensitive_source)):
        errors.append("claim-sensitive source-map candidate was not rejected")

    dirty_bridge = loop_control_fixture(
        bridge_candidates=[{"pack": "Dirty-Pack"}],
        dirty_skipped=[{"pack": "Dirty-Pack"}],
        missing_bridge=[{"pack": "Dirty-Pack"}],
    )
    if not any("already dirty" in error for error in validate_summary(dirty_bridge)):
        errors.append("dirty execution-bridge candidate was not rejected")

    sensitive_bridge = loop_control_fixture(
        bridge_candidates=[{"pack": "Sensitive-Pack"}],
        sensitive_packs={"Sensitive-Pack": "claimed"},
        missing_bridge=[{"pack": "Sensitive-Pack"}],
    )
    if not any("claim-sensitive" in error for error in validate_summary(sensitive_bridge)):
        errors.append("claim-sensitive execution-bridge candidate was not rejected")

    stale_bridge = loop_control_fixture(
        bridge_candidates=[{"pack": "Stale-Pack"}],
        missing_bridge=[],
    )
    if not any("not in the missing bridge tail" in error for error in validate_summary(stale_bridge)):
        errors.append("stale execution-bridge candidate was not rejected")

    handoff_summary = handoff_fixture()
    rendered_handoff = handoff(handoff_summary)
    for expected_text in (
        "# Monthly Uplift Handoff",
        "Status: `content-candidates`",
        "Worklog: OK; 35 loops; latest ### 2026-06-27 - Fixture Loop",
        "Claims boundary: .maintenance/CLAIMS.md; 1 rows; 1 active; 3 lines; sha256 fixture",
        "Working tree: ## main...origin/main with 1 dirty entries (0 pack lanes, 1 root/tooling entries)",
        "Dashboard schema: monthly_uplift_report v25; monthly-uplift-dashboard-v25",
        "External-link classes: DEAD 1 / REDIRECT 0 actionable; BLOCKED 1 / UNREACHABLE 1 inconclusive; UNCHECKED 2; OK 5; sha256",
        "External-link cache: 8/10 current URLs have cache rows; 9 total cache rows; 1 orphaned; sha256",
        "Worktree boundary: 1 dirty / 0 pack lanes / 1 root-tooling entries; sha256",
        "Execution-bridge tail: monitoring; action inspect-claims-and-scorecard; scope review-tail; policy inspect-before-wiring; wiring-now false; clearance-before-wiring false; blocked inspect-claims-before-wiring; 131/134 wired; 3 missing; 0 unclaimed / 0 owner-clearance; sha256",
        "Execution-bridge packs: safe-to-wire none; blocked owner-clearance none",
        "Safe content queue: ready; action harden-score-floor; 1 unclaimed (score 1 / source 0 / bridge 0); 0 score-ceiling; 0 dirty skipped; sha256",
        "Content-edit policy: content-allowed; content allowed; next content; 1 unclaimed / 0 claim-sensitive; 0 dirty pack lanes; sha256",
        "Remaining debt: unclaimed-candidates; 1 unclaimed / 0 owner-clearance; 0 dirty pack lanes; bridge 3 missing; source max unresolved 14; sha256",
        "Owner-clearance queue: owner-clearance-queue-v2; 0 targets; score 0 / source 0 / bridge 0; sha256",
        "Owner-clearance target fingerprints: score none / source none / bridge none; queue sha256",
        "Publish policy: local-only-root-tooling; local-only; root 1 paths; packs 0 lanes empty; path-scoped staging required; sha256",
        "Goal progress: active-partial-clone-skipped; core OK; worklog 35 loops; clone skipped; bridge 131/134; next content; sha256",
        "Completion audit: not-complete; action none; 13 requirements; 11 OK / 0 triaged / 2 review; 3 blockers; sha256",
        "Handoff manifest: content-candidates -> content; root 1 paths; packs 0 lanes; completion 13 req / 3 blockers; sha256",
        "SkillOpt gate plan: monthly-uplift-skillopt-gate-plan-v1; status ready-before-next-skill-edit; 0 dirty skill paths / 0 dirty pack lanes; action take-baseline-before-bounded-skill-edit; final hard gate python3 tools/run_checks.py --skip-reports; sha256",
        f"Command plan: {command_plan_line(handoff_summary)}",
        "Next-batch plan:",
        "## Dirty Boundary",
        "Dirty pack lanes: none",
        "Root/tooling dirty entries: `M tools/monthly_uplift_report.py`",
        "Root/tooling paths: `tools/monthly_uplift_report.py`",
        "Root/tooling tracked paths: `tools/monthly_uplift_report.py`",
        "Root/tooling untracked paths: none",
        "Root/tooling staging preview: `git add -- tools/monthly_uplift_report.py`",
        "## Publish Units",
        "Root/tooling unit: ready; 1 paths (1 tracked, 0 untracked)",
        "Root/tooling command: `git add -- tools/monthly_uplift_report.py`",
        "Pack content units: empty; 0 pack lanes",
        "## Measurement Commands",
        "python3 tools/audit_repo.py --counts",
        "python3 tools/clone_audit.py --threshold 0.75 --fail-threshold 0.90 --top 20",
        "python3 tools/run_checks.py --skip-reports",
        "`python3 tools/run_checks.py`",
        "python3 tools/monthly_uplift_report.py --check-worklog latest",
        "python3 tools/monthly_uplift_report.py --check-worklog latest --limit 20 --expect-latest-heading",
    ):
        if expected_text not in rendered_handoff:
            errors.append(f"handoff output missing {expected_text!r}")

    bad_worklog = loop_control_fixture()
    bad_worklog["worklog"] = {
        "status": "Review",
        "path": ".maintenance/MONTHLY-UPLIFT-2026-06-27.md",
        "loop_count": 0,
        "latest_heading": "",
        "errors": ["fixture worklog failure"],
    }
    if not any("fixture worklog failure" in error for error in validate_summary(bad_worklog)):
        errors.append("worklog summary failure was not rejected")

    missing_claims = loop_control_fixture()
    missing_claims["claims"] = {
        "present": False,
        "path": ".maintenance/CLAIMS.md",
        "line_count": 0,
        "row_count": 0,
        "active_row_count": 0,
        "fingerprint": "",
        "sensitive_packs": {},
        "sensitive_current_targets": [],
    }
    missing_claims["owner_clearance_queue"] = owner_clearance_queue(missing_claims)
    missing_claim_errors = validate_summary(missing_claims)
    if not any("claims boundary" in error for error in missing_claim_errors):
        errors.append(f"missing claims boundary was not rejected: {missing_claim_errors}")

    broken_git_paths = handoff_fixture()
    broken_git_paths["git"] = {
        **broken_git_paths["git"],
        "dirty_root_paths": ["Dirty-Pack-Skills/skills/fixture/SKILL.md"],
        "dirty_root_path_count": 1,
        "dirty_root_tracked_paths": ["tools/monthly_uplift_report.py"],
        "dirty_root_tracked_path_count": 1,
        "dirty_root_untracked_paths": [],
        "dirty_root_untracked_path_count": 0,
        "dirty_root_pathspec_command": "git add -- tools/monthly_uplift_report.py",
    }
    if not any("dirty_root_paths contains pack path" in error for error in validate_summary(broken_git_paths)):
        errors.append("pack path in dirty_root_paths was not rejected")
    if not any("dirty_root_pathspec_command" in error for error in validate_summary(broken_git_paths)):
        errors.append("dirty_root_pathspec_command mismatch was not rejected")

    broken_publish_units = handoff_fixture()
    broken_publish_units["publish_units"] = publish_units_from_git(broken_publish_units["git"])
    broken_publish_units["publish_units"]["root_tooling"] = {
        **broken_publish_units["publish_units"]["root_tooling"],
        "path_count": 99,
    }
    if not any("publish_units.root_tooling.path_count" in error for error in validate_summary(broken_publish_units)):
        errors.append("broken publish-unit root path count was not rejected")

    rendered_markdown = markdown(handoff_fixture())
    for expected_text in (
        "| Worklog | OK; 35 loops; latest `### 2026-06-27 - Fixture Loop` |",
        "| Claims boundary | .maintenance/CLAIMS.md; 1 rows; 1 active; 3 lines; sha256 fixture |",
        "| Dashboard schema | monthly_uplift_report v25; monthly-uplift-dashboard-v25 |",
        "| External-link classes | DEAD 1 / REDIRECT 0 actionable; BLOCKED 1 / UNREACHABLE 1 inconclusive; UNCHECKED 2; OK 5; sha256",
        "| External-link cache | 8/10 current URLs have cache rows; 9 total cache rows; 1 orphaned; sha256",
        "| Worktree boundary | 1 dirty / 0 pack lanes / 1 root-tooling entries; sha256",
        "| Execution-bridge tail | monitoring; action inspect-claims-and-scorecard; scope review-tail; policy inspect-before-wiring; wiring-now false; clearance-before-wiring false; blocked inspect-claims-before-wiring; 131/134 wired; 3 missing; 0 unclaimed / 0 owner-clearance; sha256",
        "| Execution-bridge packs | safe-to-wire none; blocked owner-clearance none |",
        "| Safe content queue | ready; action harden-score-floor; 1 unclaimed (score 1 / source 0 / bridge 0); 0 score-ceiling; 0 dirty skipped; sha256",
        "| Content-edit policy | content-allowed; content allowed; next content; 1 unclaimed / 0 claim-sensitive; 0 dirty pack lanes; sha256",
        "| Remaining debt | unclaimed-candidates; 1 unclaimed / 0 owner-clearance; 0 dirty pack lanes; bridge 3 missing; source max unresolved 14; sha256",
        "| Owner-clearance queue | owner-clearance-queue-v2; 0 targets; score 0 / source 0 / bridge 0; sha256",
        "| Owner-clearance target fingerprints | score none / source none / bridge none; queue sha256",
        "| Publish policy | local-only-root-tooling; local-only; root 1 paths; packs 0 lanes empty; path-scoped staging required; sha256",
        "| Goal progress | active-partial-clone-skipped; core OK; worklog 35 loops; clone skipped; bridge 131/134; next content; sha256",
        "| Completion audit | not-complete; action none; 13 requirements; 11 OK / 0 triaged / 2 review; 3 blockers; sha256",
        "| Handoff manifest | content-candidates -> content; root 1 paths; packs 0 lanes; completion 13 req / 3 blockers; sha256",
        "| SkillOpt gate plan | monthly-uplift-skillopt-gate-plan-v1; status ready-before-next-skill-edit; 0 dirty skill paths / 0 dirty pack lanes; action take-baseline-before-bounded-skill-edit; final hard gate python3 tools/run_checks.py --skip-reports; sha256",
        "| Command plan | 7 measurement / 12 validation; sha256",
        "| Next-batch plan |",
        "| Worklog health | OK | OK; 35 loops; latest ### 2026-06-27 - Fixture Loop |",
        "| Claims boundary | OK | .maintenance/CLAIMS.md; 1 rows; 1 active; 3 lines; sha256 fixture |",
        "## Dirty Boundary Review",
        "Root/tooling dirty entries: `M tools/monthly_uplift_report.py`",
        "Root/tooling paths: `tools/monthly_uplift_report.py`",
        "Root/tooling tracked paths: `tools/monthly_uplift_report.py`",
        "Root/tooling untracked paths: none",
        "Root/tooling staging preview: `git add -- tools/monthly_uplift_report.py`",
        "## Publish Unit Review",
        "Root/tooling unit: ready; 1 paths (1 tracked, 0 untracked)",
        "Pack content units: empty; 0 pack lanes",
        "## Measurement Commands",
        "python3 tools/audit_repo.py --counts",
        "python3 tools/clone_audit.py --threshold 0.75 --fail-threshold 0.90 --top 20",
        "python3 tools/monthly_uplift_report.py --check-worklog latest --limit 20 --expect-latest-heading '### 2026-06-27 - Fixture Loop'",
    ):
        if expected_text not in rendered_markdown:
            errors.append(f"markdown output missing {expected_text!r}")

    rendered_publish_plan = publish_plan(handoff_fixture())
    for expected_text in (
        "# Local Publish Plan",
        "Status: `local-only-root-tooling`",
        "Publish requested: `false`",
        "Local-only recommended: `true`",
        "Allowed unit: `root_tooling`",
        "Blocked unit: `pack_content`",
        "Publish policy: local-only-root-tooling; local-only; root 1 paths; packs 0 lanes empty; path-scoped staging required; sha256",
        "Worktree boundary: 1 dirty / 0 pack lanes / 1 root-tooling entries; sha256",
        "## Allowed Root/Tooling Unit",
        "Root/tooling: ready; 1 paths",
        "Staging command: `git add -- tools/monthly_uplift_report.py`",
        "`tools/monthly_uplift_report.py`",
        "## Blocked Pack Content Unit",
        "Pack content: empty; 0 pack lanes",
        "Owner-clearance queue: owner-clearance-queue-v2; 0 targets; score 0 / source 0 / bridge 0; sha256",
        "Owner-clearance target fingerprints: score none / source none / bridge none; queue sha256",
        "## Required Pre-Publish Checks",
        "python3 tools/monthly_uplift_report.py --check-worklog latest --limit 20 --expect-latest-heading '### 2026-06-27 - Fixture Loop'",
        "No git commands are executed by this plan.",
    ):
        if expected_text not in rendered_publish_plan:
            errors.append(f"publish-plan output missing {expected_text!r}")

    rendered_debt_audit = debt_audit(handoff_fixture())
    for expected_text in (
        "# Remaining Debt Audit",
        "Status: `unclaimed-candidates`",
        "Execution-bridge tail: monitoring; action inspect-claims-and-scorecard; scope review-tail; policy inspect-before-wiring; wiring-now false; clearance-before-wiring false; blocked inspect-claims-before-wiring; 131/134 wired; 3 missing; 0 unclaimed / 0 owner-clearance; sha256",
        "Execution-bridge packs: safe-to-wire none; blocked owner-clearance none",
        "Content-edit policy: content-allowed; content allowed; next content; 1 unclaimed / 0 claim-sensitive; 0 dirty pack lanes; sha256",
        "Remaining debt: unclaimed-candidates; 1 unclaimed / 0 owner-clearance; 0 dirty pack lanes; bridge 3 missing; source max unresolved 14; sha256",
        "Owner-clearance queue: owner-clearance-queue-v2; 0 targets; score 0 / source 0 / bridge 0; sha256",
        "Owner-clearance target fingerprints: score none / source none / bridge none; queue sha256",
        "| Score floor | 1 | 0 | lowest 90.0; below target 0 |",
        "| Source-map | 0 | 0 | warnings 0; max unresolved 14 |",
        "| Execution bridge | 0 | 0 | 131/134 wired; 3 missing |",
        "## Ownership Boundary",
        "## Validation Commands",
        "python3 tools/monthly_uplift_report.py --check-worklog latest --limit 20 --expect-latest-heading '### 2026-06-27 - Fixture Loop'",
    ):
        if expected_text not in rendered_debt_audit:
            errors.append(f"debt-audit output missing {expected_text!r}")

    rendered_goal_audit = goal_audit(handoff_fixture())
    for expected_text in (
        "# Goal Completion Audit",
        "Completion status: `not-complete`",
        "Goal status action: none",
        "Completion audit: not-complete; action none; 13 requirements; 11 OK / 0 triaged / 2 review; 3 blockers; sha256",
        "Execution-bridge tail: monitoring; action inspect-claims-and-scorecard; scope review-tail; policy inspect-before-wiring; wiring-now false; clearance-before-wiring false; blocked inspect-claims-before-wiring; 131/134 wired; 3 missing; 0 unclaimed / 0 owner-clearance; sha256",
        "Execution-bridge packs: safe-to-wire none; blocked owner-clearance none",
        "Owner-clearance queue: owner-clearance-queue-v2; 0 targets; score 0 / source 0 / bridge 0; sha256",
        "Owner-clearance target fingerprints: score none / source none / bridge none; queue sha256",
        "Goal progress: active-partial-clone-skipped; core OK; worklog 35 loops; clone skipped; bridge 131/134; next content; sha256",
        "| Durable worklog | OK | 35 loops; latest ### 2026-06-27 - Fixture Loop |",
        "| SkillOpt gate discipline | OK | snapshot/gate/final hard gate recorded; plan ready-before-next-skill-edit; final hard gate python3 tools/run_checks.py --skip-reports; SkillOpt sha256",
        "| Remaining debt register | Review | 1 unclaimed; 0 owner-clearance; 0 dirty pack lanes; debt sha256",
        "| Owner-clearance queue | OK | 0 owner-clearance targets; targets score none / source none / bridge none; queue sha256",
        "| Clone threshold | Needs full gate | clone audit skipped |",
        "| Future candidates | OK |",
        "Full clone audit is required before a completion claim.",
        "## Validation Commands",
        "python3 tools/monthly_uplift_report.py --check-worklog latest --limit 20 --expect-latest-heading '### 2026-06-27 - Fixture Loop'",
        "No goal status is changed by this audit.",
    ):
        if expected_text not in rendered_goal_audit:
            errors.append(f"goal-audit output missing {expected_text!r}")

    dirty_handoff = handoff_fixture()
    dirty_handoff["candidate_pool"] = {
        **dirty_handoff.get("candidate_pool", {}),
        "dirty_skipped_packs": [{"pack": f"Dirty-Pack-{index}"} for index in range(10)],
    }
    dirty_handoff["loop_control"] = {**expected_loop_control(dirty_handoff), "reason": "fixture"}
    dirty_handoff.update(execution_bridge_tail_summary(dirty_handoff))
    dirty_handoff.update(safe_content_queue_summary(dirty_handoff))
    dirty_handoff.update(content_edit_policy_summary(dirty_handoff))
    dirty_handoff.update(remaining_debt_summary(dirty_handoff))
    dirty_handoff.update(next_batch_plan_summary(dirty_handoff))
    dirty_handoff.update(publish_policy_summary(dirty_handoff))
    dirty_handoff.update(skillopt_gate_plan_summary(dirty_handoff))
    dirty_handoff.update(goal_progress_summary(dirty_handoff))
    dirty_handoff.update(completion_audit_summary(dirty_handoff))
    dirty_handoff.update(handoff_manifest_summary(dirty_handoff))
    dirty_handoff.update(current_next_queue_summary(dirty_handoff))
    dirty_handoff.update(schema_summary(dirty_handoff))
    rendered_dirty_handoff = handoff(dirty_handoff)
    if "Dirty-Pack-7; +2 more" not in rendered_dirty_handoff:
        errors.append("handoff dirty-skipped truncation did not include remaining count")

    baseline = handoff_fixture()
    current = handoff_fixture()
    current["quality"] = {**current["quality"], "min": 91.0}
    current["execution_bridge"] = {**current["execution_bridge"], "wired": 132, "missing": 2}
    current["claims"] = {**current["claims"], "fingerprint": "fixture-next"}
    current["candidate_pool"] = {
        **current["candidate_pool"],
        "dirty_skipped_packs": [{"pack": f"Dirty-Pack-{index}"} for index in range(3)],
    }
    current["loop_control"] = {**expected_loop_control(current), "reason": "fixture"}
    current["worklog"] = {**current["worklog"], "loop_count": 36}
    current["git"] = {
        **current["git"],
        "dirty_lines": [
            " M Dirty-Pack-Skills/skills/fixture/SKILL.md",
            " M tools/monthly_uplift_report.py",
            "?? .maintenance/MONTHLY-UPLIFT-2026-06-27.md",
        ],
        "dirty_count": 3,
        "dirty_pack_names": ["Dirty-Pack-Skills"],
        "dirty_pack_count": 1,
        "dirty_pack_paths": ["Dirty-Pack-Skills/skills/fixture/SKILL.md"],
        "dirty_pack_path_count": 1,
        "dirty_root_lines": [
            " M tools/monthly_uplift_report.py",
            "?? .maintenance/MONTHLY-UPLIFT-2026-06-27.md",
        ],
        "dirty_root_count": 2,
        "dirty_root_paths": [
            "tools/monthly_uplift_report.py",
            ".maintenance/MONTHLY-UPLIFT-2026-06-27.md",
        ],
        "dirty_root_path_count": 2,
        "dirty_root_tracked_paths": ["tools/monthly_uplift_report.py"],
        "dirty_root_tracked_path_count": 1,
        "dirty_root_untracked_paths": [".maintenance/MONTHLY-UPLIFT-2026-06-27.md"],
        "dirty_root_untracked_path_count": 1,
        "dirty_root_pathspec_command": (
            "git add -- tools/monthly_uplift_report.py "
            ".maintenance/MONTHLY-UPLIFT-2026-06-27.md"
        ),
    }
    current.update(worktree_boundary_summary(current["git"]))
    current["publish_units"] = publish_units_from_git(current["git"])
    current.update(execution_bridge_tail_summary(current))
    current.update(safe_content_queue_summary(current))
    current.update(content_edit_policy_summary(current))
    current.update(remaining_debt_summary(current))
    current.update(next_batch_plan_summary(current))
    current.update(publish_policy_summary(current))
    current.update(skillopt_gate_plan_summary(current))
    current.update(goal_progress_summary(current))
    current.update(completion_audit_summary(current))
    current.update(handoff_manifest_summary(current))
    current.update(current_next_queue_summary(current))
    current.update(schema_summary(current))
    current["delta"] = compare_delta(baseline, current)
    rendered_delta = handoff(current)
    for expected_text in (
        "## Trajectory Delta",
        "Quality min: 90.0 -> 91.0 (+1.0)",
        "Execution bridge missing: 3 -> 2 (-1)",
        "Dirty skipped packs: 0 -> 3 (+3)",
        "Worklog loops: 35 -> 36 (+1)",
        "Git dirty entries: 1 -> 3 (+2)",
        "Git dirty pack lanes: 0 -> 1 (+1)",
        "Git dirty root/tooling entries: 1 -> 2 (+1)",
        "Command plan measurement commands: 7 -> 7 (0)",
        "Command plan validation commands: 12 -> 12 (0)",
        "Dirty pack lanes: Dirty-Pack-Skills",
        "Root/tooling dirty entries: `M tools/monthly_uplift_report.py`; `?? .maintenance/MONTHLY-UPLIFT-2026-06-27.md`",
        "Root/tooling paths: `tools/monthly_uplift_report.py`; `.maintenance/MONTHLY-UPLIFT-2026-06-27.md`",
        "Root/tooling tracked paths: `tools/monthly_uplift_report.py`",
        "Root/tooling untracked paths: `.maintenance/MONTHLY-UPLIFT-2026-06-27.md`",
        "Root/tooling staging preview: `git add -- tools/monthly_uplift_report.py .maintenance/MONTHLY-UPLIFT-2026-06-27.md`",
        "Claims boundary fingerprint: fixture -> fixture-next (changed)",
        "Worktree boundary fingerprint (worktree-sensitive):",
        "Publish policy fingerprint (worktree-sensitive):",
        "Handoff manifest fingerprint (worktree-sensitive):",
    ):
        if expected_text not in rendered_delta:
            errors.append(f"delta handoff output missing {expected_text!r}")
    rendered_delta_markdown = markdown(current)
    if "| Claims boundary fingerprint | fixture | fixture-next | changed |" not in rendered_delta_markdown:
        errors.append("delta markdown output missing claims fingerprint row")
    for expected_markdown in (
        "| Worktree boundary fingerprint (worktree-sensitive) |",
        "| Publish policy fingerprint (worktree-sensitive) |",
        "| Handoff manifest fingerprint (worktree-sensitive) |",
    ):
        if expected_markdown not in rendered_delta_markdown:
            errors.append(f"delta markdown output missing worktree-sensitive row {expected_markdown!r}")
    rendered_delta_worklog = worklog_template(current)
    if "Claims boundary fingerprint: fixture -> fixture-next (changed)." not in rendered_delta_worklog:
        errors.append("delta worklog-template output missing claims fingerprint line")
    for expected_worklog in (
        "Worktree boundary fingerprint (worktree-sensitive):",
        "Publish policy fingerprint (worktree-sensitive):",
        "Handoff manifest fingerprint (worktree-sensitive):",
    ):
        if expected_worklog not in rendered_delta_worklog:
            errors.append(f"delta worklog-template output missing worktree-sensitive line {expected_worklog!r}")

    clearance = handoff_fixture()
    clearance["claims"] = {
        "sensitive_packs": {"Claimed-Pack": "Agent A queued"},
        "sensitive_current_targets": [
            {"kind": "score-floor", "pack": "Claimed-Pack", "reason": "Agent A queued"},
            {"kind": "execution-bridge", "pack": "Claimed-Pack", "reason": "Agent A queued"},
        ],
    }
    clearance["execution_bridge"] = {
        **clearance["execution_bridge"],
        "missing_packs": [{"pack": "Claimed-Pack", "score": 90.0, "exec_bridge_skills": 0}],
    }
    clearance["loop_control"] = {**expected_loop_control(clearance), "reason": "fixture"}
    clearance["owner_clearance_queue"] = owner_clearance_queue(clearance)
    clearance.update(execution_bridge_tail_summary(clearance))
    clearance.update(safe_content_queue_summary(clearance))
    clearance.update(content_edit_policy_summary(clearance))
    clearance.update(remaining_debt_summary(clearance))
    clearance.update(next_batch_plan_summary(clearance))
    clearance.update(publish_policy_summary(clearance))
    clearance.update(skillopt_gate_plan_summary(clearance))
    clearance.update(goal_progress_summary(clearance))
    clearance.update(completion_audit_summary(clearance))
    clearance.update(handoff_manifest_summary(clearance))
    clearance.update(current_next_queue_summary(clearance))
    clearance.update(schema_summary(clearance))
    clearance_tail = clearance["execution_bridge_tail"]
    if clearance_tail.get("claim_sensitive_policy") != "clearance-before-wiring":
        errors.append("owner-clearance execution-bridge tail did not require clearance-before-wiring")
    if clearance_tail.get("wiring_allowed_now"):
        errors.append("owner-clearance execution-bridge tail incorrectly allowed wiring now")
    if not clearance_tail.get("owner_clearance_required_before_wiring"):
        errors.append("owner-clearance execution-bridge tail did not mark clearance required before wiring")
    if clearance_tail.get("blocked_owner_clearance_packs") != ["Claimed-Pack"]:
        errors.append("owner-clearance execution-bridge tail did not expose blocked pack list")
    rendered_clearance = handoff(clearance)
    for expected_text in (
        "## Owner Clearance Queue",
        "Execution-bridge tail: owner-clearance-required; action request-owner-clearance; scope owner-clearance-only; policy clearance-before-wiring; wiring-now false; clearance-before-wiring true; blocked request-owner-clearance-before-wiring; 131/134 wired; 3 missing; 0 unclaimed / 1 owner-clearance; sha256",
        "Execution-bridge packs: safe-to-wire none; blocked owner-clearance Claimed-Pack (Agent A queued)",
        "Owner-clearance queue: owner-clearance-queue-v2; 2 targets; score 1 (1 shown) / source 0 / bridge 1 (1 shown); sha256",
        f"Owner-clearance target fingerprints: {owner_clearance_target_fingerprint_line(clearance)}",
        "Score-floor targets: Claimed-Pack (Agent A queued)",
        "Execution-bridge targets: Claimed-Pack (Agent A queued)",
        "Execution-bridge candidates: none unclaimed; owner clearance required for Claimed-Pack (Agent A queued)",
    ):
        if expected_text not in rendered_clearance:
            errors.append(f"owner-clearance handoff output missing {expected_text!r}")
    rendered_clearance_markdown = markdown(clearance)
    if "| Execution-bridge packs | safe-to-wire none; blocked owner-clearance `Claimed-Pack` (Agent A queued) |" not in rendered_clearance_markdown:
        errors.append("owner-clearance markdown output missing bridge pack decision line")
    if "| Owner-clearance queue | owner-clearance-queue-v2; 2 targets; score 1 (1 shown) / source 0 / bridge 1 (1 shown); sha256" not in rendered_clearance_markdown:
        errors.append("owner-clearance markdown output missing queue compact line")
    if f"| Owner-clearance target fingerprints | {owner_clearance_target_fingerprint_line(clearance)} |" not in rendered_clearance_markdown:
        errors.append("owner-clearance markdown output missing target fingerprint line")
    if "get owner clearance before wiring: Claimed-Pack (Agent A queued)." not in rendered_clearance_markdown:
        errors.append("owner-clearance markdown output missing bridge clearance reason")
    rendered_clearance_goal_audit = goal_audit(clearance)
    if "Execution-bridge packs: safe-to-wire none; blocked owner-clearance Claimed-Pack (Agent A queued)" not in rendered_clearance_goal_audit:
        errors.append("owner-clearance goal audit missing bridge pack decision line")
    if "Owner-clearance queue: owner-clearance-queue-v2; 2 targets; score 1 (1 shown) / source 0 / bridge 1 (1 shown); sha256" not in rendered_clearance_goal_audit:
        errors.append("owner-clearance goal audit missing queue compact line")
    if f"Owner-clearance target fingerprints: {owner_clearance_target_fingerprint_line(clearance)}" not in rendered_clearance_goal_audit:
        errors.append("owner-clearance goal audit missing target fingerprint line")
    if "| Execution bridge and debt | Triaged | 131/134 wired; 1 bridge gap is owner-clearance gated; policy clearance-before-wiring; clearance required before wiring |" not in rendered_clearance_goal_audit:
        errors.append("owner-clearance goal audit did not triage the bridge tail")
    if "Execution bridge still has 1 owner-clearance-gated gap." not in rendered_clearance_goal_audit:
        errors.append("owner-clearance goal audit missing bridge-tail blocker")

    mixed_bridge = handoff_fixture()
    mixed_bridge["candidate_pool"] = {
        **mixed_bridge.get("candidate_pool", {}),
        "score_unclaimed": [],
        "source_map_unclaimed": [],
        "execution_bridge_unclaimed": [
            {
                "pack": "Open-Pack",
                "score": 91.0,
                "current_bridge_links": 0,
                "weakest_skill": "Open-Pack/skills/fixture/SKILL.md",
            }
        ],
        "dirty_skipped_packs": [],
    }
    mixed_bridge["claims"] = {
        **mixed_bridge["claims"],
        "sensitive_packs": {"Claimed-Pack": "Agent A queued"},
        "sensitive_current_targets": [
            {"kind": "execution-bridge", "pack": "Claimed-Pack", "reason": "Agent A queued"},
        ],
    }
    mixed_bridge["execution_bridge"] = {
        **mixed_bridge["execution_bridge"],
        "wired": 132,
        "missing": 2,
        "missing_packs": [
            {"pack": "Open-Pack", "score": 91.0, "exec_bridge_skills": 0},
            {"pack": "Claimed-Pack", "score": 92.0, "exec_bridge_skills": 0},
        ],
    }
    mixed_bridge["loop_control"] = {**expected_loop_control(mixed_bridge), "reason": "fixture"}
    mixed_bridge["owner_clearance_queue"] = owner_clearance_queue(mixed_bridge)
    mixed_bridge.update(execution_bridge_tail_summary(mixed_bridge))
    mixed_bridge.update(safe_content_queue_summary(mixed_bridge))
    mixed_bridge.update(content_edit_policy_summary(mixed_bridge))
    mixed_bridge.update(remaining_debt_summary(mixed_bridge))
    mixed_bridge.update(next_batch_plan_summary(mixed_bridge))
    mixed_bridge.update(publish_policy_summary(mixed_bridge))
    mixed_bridge.update(skillopt_gate_plan_summary(mixed_bridge))
    mixed_bridge.update(goal_progress_summary(mixed_bridge))
    mixed_bridge.update(completion_audit_summary(mixed_bridge))
    mixed_bridge.update(handoff_manifest_summary(mixed_bridge))
    mixed_bridge.update(current_next_queue_summary(mixed_bridge))
    mixed_bridge.update(schema_summary(mixed_bridge))
    mixed_errors = validate_summary(mixed_bridge)
    if mixed_errors:
        errors.append(f"mixed execution-bridge tail fixture failed validation: {mixed_errors}")
    mixed_tail = mixed_bridge["execution_bridge_tail"]
    if mixed_tail.get("recommendation_scope") != "unclaimed-only":
        errors.append("mixed execution-bridge tail did not scope recommendation to unclaimed-only")
    if mixed_tail.get("blocked_recommendation") != "leave-owner-clearance-rows-blocked":
        errors.append("mixed execution-bridge tail did not preserve owner-clearance blocking")
    if mixed_tail.get("claim_sensitive_policy") != "split-wire-unclaimed-request-clearance":
        errors.append("mixed execution-bridge tail did not expose split claim-sensitive policy")
    if not mixed_tail.get("wiring_allowed_now"):
        errors.append("mixed execution-bridge tail did not allow unclaimed wiring")
    if not mixed_tail.get("owner_clearance_required_before_wiring"):
        errors.append("mixed execution-bridge tail did not keep clearance-before-wiring for claimed rows")
    if mixed_tail.get("safe_to_wire_packs") != ["Open-Pack"]:
        errors.append("mixed execution-bridge tail did not expose safe-to-wire pack list")
    if mixed_tail.get("blocked_owner_clearance_packs") != ["Claimed-Pack"]:
        errors.append("mixed execution-bridge tail did not expose blocked owner-clearance pack list")
    if mixed_tail.get("owner_clearance_required"):
        errors.append("mixed execution-bridge tail should allow unclaimed work while flagging blocked rows")
    if not mixed_bridge["content_edit_policy"].get("execution_bridge_owner_clearance_required"):
        errors.append("mixed content-edit policy did not retain bridge owner-clearance status")
    rendered_mixed_handoff = handoff(mixed_bridge)
    for expected_text in (
        "Execution-bridge tail: unclaimed-candidates; action wire-unclaimed; scope unclaimed-only; policy split-wire-unclaimed-request-clearance; wiring-now true; clearance-before-wiring true; blocked leave-owner-clearance-rows-blocked; 132/134 wired; 2 missing; 1 unclaimed / 1 owner-clearance; sha256",
        "Execution-bridge packs: safe-to-wire Open-Pack; blocked owner-clearance Claimed-Pack (Agent A queued)",
        "Content-edit policy: content-allowed; content allowed; next content; 1 unclaimed / 1 claim-sensitive; 0 dirty pack lanes; bridge owner-clearance; sha256",
        "Execution-bridge targets: Claimed-Pack (Agent A queued)",
        "Execution-bridge candidates: Open-Pack",
    ):
        if expected_text not in rendered_mixed_handoff:
            errors.append(f"mixed bridge handoff output missing {expected_text!r}")
    rendered_mixed_goal_audit = goal_audit(mixed_bridge)
    if "Execution-bridge packs: safe-to-wire Open-Pack; blocked owner-clearance Claimed-Pack (Agent A queued)" not in rendered_mixed_goal_audit:
        errors.append("mixed bridge goal audit missing bridge pack decision line")
    if "| Execution bridge and debt | Triaged | 132/134 wired; 1 bridge gap is owner-clearance gated; 1 bridge gap remains actionable; policy split-wire-unclaimed-request-clearance; clearance required before wiring |" not in rendered_mixed_goal_audit:
        errors.append("mixed bridge goal audit did not separate blocked and actionable gaps")
    if "Execution bridge still has 1 owner-clearance-gated gap and 1 unclaimed gap." not in rendered_mixed_goal_audit:
        errors.append("mixed bridge goal audit missing split bridge-tail blocker")

    stale_clearance_fingerprint = json.loads(json.dumps(clearance))
    stale_clearance_fingerprint["owner_clearance_queue"] = {
        **stale_clearance_fingerprint["owner_clearance_queue"],
        "fingerprint": "stale",
    }
    if not any("owner_clearance_queue.fingerprint" in error for error in validate_summary(stale_clearance_fingerprint)):
        errors.append("stale owner-clearance queue fingerprint was not rejected")

    stale_clearance_display = json.loads(json.dumps(clearance))
    stale_clearance_display["owner_clearance_queue"]["score-floor"]["displayed"][0]["reason"] = "stale"
    if not any("owner_clearance_queue.score-floor.displayed" in error for error in validate_summary(stale_clearance_display)):
        errors.append("stale owner-clearance queue displayed rows were not rejected")

    clearance_overflow = handoff_fixture()
    clearance_overflow["claims"] = {
        "sensitive_packs": {f"Claimed-Pack-{index}": "Agent A queued" for index in range(7)},
        "sensitive_current_targets": [
            {"kind": "score-floor", "pack": f"Claimed-Pack-{index}", "reason": "Agent A queued"}
            for index in range(7)
        ],
    }
    clearance_overflow["loop_control"] = {**expected_loop_control(clearance_overflow), "reason": "fixture"}
    clearance_overflow["owner_clearance_queue"] = owner_clearance_queue(clearance_overflow)
    clearance_overflow.update(execution_bridge_tail_summary(clearance_overflow))
    clearance_overflow.update(safe_content_queue_summary(clearance_overflow))
    clearance_overflow.update(content_edit_policy_summary(clearance_overflow))
    clearance_overflow.update(remaining_debt_summary(clearance_overflow))
    clearance_overflow.update(next_batch_plan_summary(clearance_overflow))
    clearance_overflow.update(publish_policy_summary(clearance_overflow))
    clearance_overflow.update(skillopt_gate_plan_summary(clearance_overflow))
    clearance_overflow.update(goal_progress_summary(clearance_overflow))
    clearance_overflow.update(completion_audit_summary(clearance_overflow))
    clearance_overflow.update(handoff_manifest_summary(clearance_overflow))
    clearance_overflow.update(current_next_queue_summary(clearance_overflow))
    clearance_overflow.update(schema_summary(clearance_overflow))
    rendered_overflow_handoff = handoff(clearance_overflow)
    rendered_overflow_markdown = markdown(clearance_overflow)
    rendered_overflow_worklog = worklog_template(clearance_overflow)
    if "Claimed-Pack-4 (Agent A queued); +2 more" not in rendered_overflow_handoff:
        errors.append("owner-clearance handoff overflow did not include remaining count")
    if "`Claimed-Pack-4` (Agent A queued); +2 more" not in rendered_overflow_markdown:
        errors.append("owner-clearance markdown overflow did not include remaining count")
    if "Claimed-Pack-4 (Agent A queued); +2 more." not in rendered_overflow_worklog:
        errors.append("owner-clearance worklog overflow did not include remaining count")
    if "Owner-clearance queue: owner-clearance-queue-v2; 7 targets; score 7 (5 shown, +2 more) / source 0 / bridge 0; sha256" not in rendered_overflow_handoff:
        errors.append("owner-clearance handoff compact line did not include overflow counts")
    if f"Owner-clearance target fingerprints: {owner_clearance_target_fingerprint_line(clearance_overflow)}" not in rendered_overflow_handoff:
        errors.append("owner-clearance handoff target fingerprint line did not include hidden target hash")
    if "| Owner-clearance queue | owner-clearance-queue-v2; 7 targets; score 7 (5 shown, +2 more) / source 0 / bridge 0; sha256" not in rendered_overflow_markdown:
        errors.append("owner-clearance markdown compact line did not include overflow counts")
    if f"| Owner-clearance target fingerprints | {owner_clearance_target_fingerprint_line(clearance_overflow)} |" not in rendered_overflow_markdown:
        errors.append("owner-clearance markdown target fingerprint line did not include hidden target hash")
    if "Owner-clearance queue: owner-clearance-queue-v2; 7 targets; score 7 (5 shown, +2 more) / source 0 / bridge 0; sha256" not in rendered_overflow_worklog:
        errors.append("owner-clearance worklog compact line did not include overflow counts")
    if f"Owner-clearance target fingerprints: {owner_clearance_target_fingerprint_line(clearance_overflow)}." not in rendered_overflow_worklog:
        errors.append("owner-clearance worklog target fingerprint line did not include hidden target hash")

    stale_clearance_hidden_target = json.loads(json.dumps(clearance_overflow))
    stale_clearance_hidden_target["owner_clearance_queue"]["score-floor"]["targets"][6]["reason"] = "stale"
    if not any(
        "owner_clearance_queue.score-floor.targets" in error
        for error in validate_summary(stale_clearance_hidden_target)
    ):
        errors.append("stale hidden owner-clearance queue target was not rejected")

    broken_clearance_queue = handoff_fixture()
    broken_clearance_queue["claims"] = {
        "sensitive_packs": {"Claimed-Pack": "Agent A queued"},
        "sensitive_current_targets": [
            {"kind": "score-floor", "pack": "Claimed-Pack", "reason": "Agent A queued"},
        ],
    }
    broken_clearance_queue["loop_control"] = {**expected_loop_control(broken_clearance_queue), "reason": "fixture"}
    broken_clearance_queue["owner_clearance_queue"] = {
        "score-floor": {
            "total": 0,
            "display_limit": 5,
            "displayed": [{"pack": "Claimed-Pack", "reason": "Agent A queued"}],
            "omitted": 0,
            "truncated": False,
        }
    }
    if not any("owner_clearance_queue.score-floor.total" in error for error in validate_summary(broken_clearance_queue)):
        errors.append("broken owner-clearance queue total was not rejected")

    rendered_worklog = worklog_template(clearance)
    for expected_text in (
        "### 2026-06-27 - Monthly Uplift Loop",
        "- Live metrics:",
        "- Validation checklist:",
        "python3 tools/monthly_uplift_report.py --check --worklog-template --limit 20",
        "Owner clearance queue",
        "Root/tooling dirty entries: `M tools/monthly_uplift_report.py`",
        "Root/tooling paths: `tools/monthly_uplift_report.py`",
        "Root/tooling tracked paths: `tools/monthly_uplift_report.py`",
        "Root/tooling untracked paths: none",
        "Root/tooling staging preview: `git add -- tools/monthly_uplift_report.py`",
        "Publish units:",
        "Root/tooling unit: ready; 1 paths (1 tracked, 0 untracked)",
        "Pack content units: empty; 0 pack lanes",
        "Measurement checklist:",
        "python3 tools/audit_repo.py --counts",
        "python3 tools/clone_audit.py --threshold 0.75 --fail-threshold 0.90 --top 20",
        "python3 tools/monthly_uplift_report.py --check-worklog latest --limit 20 --expect-latest-heading '### 2026-06-27 - Monthly Uplift Loop'",
        "Worktree boundary: 1 dirty / 0 pack lanes / 1 root-tooling entries; sha256",
        "External-link classes: DEAD 1 / REDIRECT 0 actionable; BLOCKED 1 / UNREACHABLE 1 inconclusive; UNCHECKED 2; OK 5; sha256",
        "External-link cache: 8/10 current URLs have cache rows; 9 total cache rows; 1 orphaned; sha256",
        "Execution-bridge tail: owner-clearance-required; action request-owner-clearance; scope owner-clearance-only; policy clearance-before-wiring; wiring-now false; clearance-before-wiring true; blocked request-owner-clearance-before-wiring; 131/134 wired; 3 missing; 0 unclaimed / 1 owner-clearance; sha256",
        "Execution-bridge packs: safe-to-wire none; blocked owner-clearance Claimed-Pack (Agent A queued).",
        "Content-edit policy: content-allowed; content allowed; next content; 1 unclaimed / 2 claim-sensitive; 0 dirty pack lanes; bridge owner-clearance; sha256",
        "Remaining debt: unclaimed-candidates; 1 unclaimed / 2 owner-clearance; 0 dirty pack lanes; bridge 3 missing; source max unresolved 14; sha256",
        "Owner-clearance queue: owner-clearance-queue-v2; 2 targets; score 1 (1 shown) / source 0 / bridge 1 (1 shown); sha256",
        f"Owner-clearance target fingerprints: {owner_clearance_target_fingerprint_line(clearance)}.",
        "Goal progress: active-partial-clone-skipped; core OK; worklog 35 loops; clone skipped; bridge 131/134; next content; sha256",
        "Handoff manifest: content-candidates -> content; root 1 paths; packs 0 lanes; completion 13 req / 3 blockers; sha256",
        "Command plan: 7 measurement / 12 validation; sha256",
        "Next-batch plan:",
        "Execution-bridge owner-clearance tail: Claimed-Pack (Agent A queued).",
        "Current Next Queue fragments:",
        "Current-next-queue contract: `current-next-queue-v7`",
        f"completion-audit owner target fingerprints `{completion_audit_owner_target_fingerprint_line(clearance)}`",
    ):
        if expected_text not in rendered_worklog:
            errors.append(f"worklog template output missing {expected_text!r}")

    valid_worklog = """
### 2026-06-27 - Monthly Uplift Loop

- Scope: root tooling.
- Rationale: keep the loop evidence complete.
- Files: `tools/monthly_uplift_report.py`.
- Result: added a worklog checker.
- Validation:
  - `python3 -m py_compile tools/monthly_uplift_report.py tools/run_checks.py`
  - `python3 tools/monthly_uplift_report.py --self-test`
  - `python3 tools/monthly_uplift_report.py --check --handoff --limit 20`
  - `python3 tools/monthly_uplift_report.py --check --publish-plan --limit 20`
  - `python3 tools/monthly_uplift_report.py --check --goal-audit --limit 20`
  - `python3 tools/monthly_uplift_report.py --check --debt-audit --limit 20`
  - `python3 tools/monthly_uplift_report.py --check --worklog-template --limit 20 --output /tmp/ajs-monthly-worklog-template.md`
  - `python3 tools/monthly_uplift_report.py --check-worklog latest`
  - `python3 tools/monthly_uplift_report.py --check-worklog latest --limit 20 --expect-latest-heading '### 2026-06-27 - Monthly Uplift Loop'`
  - `python3 tools/monthly_uplift_report.py --check --limit 20 --output /tmp/ajs-monthly-report-final.md`
  - `python3 tools/run_checks.py --skip-reports`
  - `python3 tools/run_checks.py`
  - `git diff --check`

## Current Next Queue

- Current-next-queue contract: `current-next-queue-v7`.
- Dashboard contract: `monthly-uplift-dashboard-v25`.
- Owner-clearance contract: `owner-clearance-queue-v2`.
- Completion audit contract: `monthly-uplift-completion-audit-v6`.
- Loop-control status: `owner-clearance-needed`.
- Local publish-unit split: root/tooling currently forms one ready unit;
  pack content remains marked `needs-owner-review`.
- Regression gates for the next batch: `python3 tools/monthly_uplift_report.py --check --handoff --limit 20`,
  `python3 tools/monthly_uplift_report.py --check --publish-plan --limit 20`,
  `python3 tools/monthly_uplift_report.py --check --goal-audit --limit 20`,
  `python3 tools/monthly_uplift_report.py --check --debt-audit --limit 20`,
  `python3 tools/monthly_uplift_report.py --check --worklog-template --limit 20`,
  `python3 tools/monthly_uplift_report.py --check-worklog latest`,
  `python3 tools/monthly_uplift_report.py --check --limit 20`,
  `python3 tools/audit_repo.py --counts`, `python3 tools/quality_scorecard.py`,
  `python3 tools/source_map_audit.py`, `python3 tools/root_entry_audit.py`,
  `python3 tools/clone_audit.py --threshold 0.75 --fail-threshold 0.90 --top 20`,
  `python3 tools/run_checks.py --skip-reports`, `python3 tools/run_checks.py`,
  and `git diff --check`.
"""
    if validate_worklog_text(valid_worklog):
        errors.append(f"valid worklog fixture failed: {validate_worklog_text(valid_worklog)}")
    valid_heading = "### 2026-06-27 - Monthly Uplift Loop"
    if validate_expected_latest_heading(valid_worklog, valid_heading):
        errors.append("expected latest-heading fixture was rejected")
    stale_heading_errors = validate_expected_latest_heading(valid_worklog, "### 2026-06-27 - Older Loop")
    if not any("does not match expected" in error for error in stale_heading_errors):
        errors.append(f"stale latest-heading fixture was not rejected: {stale_heading_errors}")

    missing_command_worklog = valid_worklog.replace(
        "  - `python3 tools/monthly_uplift_report.py --check-worklog latest`\n",
        "",
    ).replace(
        "  - `python3 tools/monthly_uplift_report.py --check-worklog latest --limit 20 --expect-latest-heading '### 2026-06-27 - Monthly Uplift Loop'`\n",
        "",
    )
    missing_command_errors = validate_worklog_text(missing_command_worklog)
    if not any("validation missing command marker" in error for error in missing_command_errors):
        errors.append(f"missing-command worklog fixture was not rejected: {missing_command_errors}")

    stale_strict_heading_worklog = valid_worklog.replace(
        "--expect-latest-heading '### 2026-06-27 - Monthly Uplift Loop'",
        "--expect-latest-heading '### 2026-06-27 - Wrong Loop'",
    )
    stale_strict_heading_errors = validate_worklog_text(stale_strict_heading_worklog)
    if not any("strict latest-heading command expected" in error for error in stale_strict_heading_errors):
        errors.append(f"stale strict latest-heading command was not rejected: {stale_strict_heading_errors}")

    missing_next_queue_worklog = valid_worklog.replace(
        "  `python3 tools/monthly_uplift_report.py --check-worklog latest`,\n",
        "",
    )
    missing_next_queue_errors = validate_worklog_text(missing_next_queue_worklog)
    if not any("Current Next Queue missing marker" in error for error in missing_next_queue_errors):
        errors.append(f"missing-next-queue worklog fixture was not rejected: {missing_next_queue_errors}")

    missing_publish_unit_worklog = valid_worklog.replace(
        "- Local publish-unit split: root/tooling currently forms one ready unit;\n"
        "  pack content remains marked `needs-owner-review`.\n",
        "",
    )
    missing_publish_unit_errors = validate_worklog_text(missing_publish_unit_worklog)
    if not any("Local publish-unit split:" in error for error in missing_publish_unit_errors):
        errors.append(f"missing-publish-unit worklog fixture was not rejected: {missing_publish_unit_errors}")

    later_valid_loop = """
### 2026-06-28 - Later Loop

- Scope: root tooling.
- Rationale: keep latest loop validation markers complete.
- Files: `tools/monthly_uplift_report.py`.
- Result: added a later loop entry.
- Validation:
  - `python3 -m py_compile tools/monthly_uplift_report.py tools/run_checks.py`
  - `python3 tools/monthly_uplift_report.py --self-test`
  - `python3 tools/monthly_uplift_report.py --check --handoff --limit 20`
  - `python3 tools/monthly_uplift_report.py --check --publish-plan --limit 20`
  - `python3 tools/monthly_uplift_report.py --check --goal-audit --limit 20`
  - `python3 tools/monthly_uplift_report.py --check --debt-audit --limit 20`
  - `python3 tools/monthly_uplift_report.py --check --worklog-template --limit 20 --output /tmp/ajs-monthly-worklog-template.md`
  - `python3 tools/monthly_uplift_report.py --check-worklog latest`
  - `python3 tools/monthly_uplift_report.py --check --limit 20 --output /tmp/ajs-monthly-report-final.md`
  - `python3 tools/run_checks.py --skip-reports`
  - `python3 tools/run_checks.py`
  - `git diff --check`

- Current-next-queue contract: `current-next-queue-v7`.
"""
    stale_global_contract_worklog = valid_worklog.replace("current-next-queue-v7", "current-next-queue-v6", 1)
    stale_global_contract_errors = validate_worklog_text(stale_global_contract_worklog + later_valid_loop)
    if not any("stale queue contract" in error for error in stale_global_contract_errors):
        errors.append(
            "stale global Current Next Queue contract was masked by a later loop entry: "
            f"{stale_global_contract_errors}"
        )

    masked_global_target_text = "\n".join(
        [
            "## Current Next Queue",
            "",
            "- Current-next-queue contract: `current-next-queue-v7`.",
            "- Dashboard contract: `monthly-uplift-dashboard-v25`.",
            "- Owner-clearance contract: `owner-clearance-queue-v2`.",
            "- Completion audit contract: `monthly-uplift-completion-audit-v6`.",
            f"- The current nested-contracts fingerprint is `{clearance['schema']['nested_contracts_fingerprint']}`.",
            "",
            "### Later Loop",
            "",
            *[f"- {fragment}" for fragment in current_next_queue_expected_fragments(clearance)],
        ]
    )
    masked_global_target_errors = validate_current_next_queue_text(masked_global_target_text, clearance)
    if not any("global section missing live fragment" in error for error in masked_global_target_errors):
        errors.append(
            "missing global owner-target fingerprint was masked by later queue fragments: "
            f"{masked_global_target_errors}"
        )

    invalid_worklog = """
### 2026-06-27 - Monthly Uplift Loop

- Scope: [describe root-only/tooling/content lane and ownership boundary].
- Validation:
  - `python3 tools/run_checks.py --skip-reports`
"""
    if not validate_worklog_text(invalid_worklog):
        errors.append("invalid worklog fixture was not rejected")

    planned_worklog = """
### 2026-06-27 - Monthly Uplift Loop

- Scope: root tooling.
- Rationale: keep the loop evidence complete.
- Files: `tools/monthly_uplift_report.py`.
- Result: added a worklog checker.
- Validation:
  - `python3 -m py_compile tools/monthly_uplift_report.py tools/run_checks.py`
    -> scheduled for this loop.
  - `python3 tools/monthly_uplift_report.py --self-test`
  - `python3 tools/monthly_uplift_report.py --check --handoff --limit 20`
  - `python3 tools/monthly_uplift_report.py --check --publish-plan --limit 20`
  - `python3 tools/monthly_uplift_report.py --check --goal-audit --limit 20`
  - `python3 tools/monthly_uplift_report.py --check-worklog latest`
  - `python3 tools/monthly_uplift_report.py --check --limit 20 --output /tmp/ajs-monthly-report-final.md`
  - `python3 tools/run_checks.py --skip-reports`
  - `python3 tools/run_checks.py`
  - `git diff --check`

## Current Next Queue

- Loop-control status: `owner-clearance-needed`.
- Regression gates for the next batch: `python3 tools/monthly_uplift_report.py --check --handoff --limit 20`,
  `python3 tools/monthly_uplift_report.py --check --publish-plan --limit 20`,
  `python3 tools/monthly_uplift_report.py --check-worklog latest`,
  `python3 tools/monthly_uplift_report.py --check --limit 20`,
  `python3 tools/audit_repo.py --counts`, `python3 tools/quality_scorecard.py`,
  `python3 tools/source_map_audit.py`, `python3 tools/root_entry_audit.py`,
  `python3 tools/run_checks.py --skip-reports`, `python3 tools/run_checks.py`,
  and `git diff --check`.
"""
    planned_errors = validate_worklog_text(planned_worklog)
    if not any("planned validation text" in error for error in planned_errors):
        errors.append(f"planned-evidence worklog fixture was not rejected: {planned_errors}")

    pending_evidence_worklog = valid_worklog.replace(
        "  - `python3 tools/monthly_uplift_report.py --check-worklog latest`\n",
        "  - `python3 tools/monthly_uplift_report.py --check-worklog latest`\n"
        "    -> pending final run after this append.\n",
    )
    pending_evidence_errors = validate_worklog_text(pending_evidence_worklog)
    if not any("planned validation text" in error for error in pending_evidence_errors):
        errors.append(f"pending-evidence worklog fixture was not rejected: {pending_evidence_errors}")

    should_report_worklog = valid_worklog.replace(
        "  - `python3 tools/monthly_uplift_report.py --check-worklog latest`\n",
        "  - `python3 tools/monthly_uplift_report.py --check-worklog latest`\n"
        "    -> should report the latest loop after this append.\n",
    )
    should_report_errors = validate_worklog_text(should_report_worklog)
    if not any("planned validation text" in error for error in should_report_errors):
        errors.append(f"should-report worklog fixture was not rejected: {should_report_errors}")

    try:
        latest_path = latest_worklog_path()
        if not latest_path.name.startswith("MONTHLY-UPLIFT-"):
            errors.append(f"latest worklog path has unexpected name {latest_path.name!r}")
        if resolve_worklog_path(Path("latest")) != latest_path:
            errors.append("latest worklog alias did not resolve to latest worklog path")
        if resolve_worklog_path(Path("current")) != latest_path:
            errors.append("current worklog alias did not resolve to latest worklog path")
    except ValueError as exc:
        errors.append(f"latest worklog path lookup failed: {exc}")

    return errors


def status_paths(line: str) -> list[str]:
    path = line[3:].strip() if len(line) > 3 else line.strip()
    if " -> " in path:
        return [part.strip() for part in path.split(" -> ", 1)]
    return [path]


def unique_ordered(items: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        result.append(item)
    return result


def git_add_command(paths: list[str]) -> str:
    if not paths:
        return ""
    quoted = " ".join(shlex.quote(path) for path in paths)
    return f"git add -- {quoted}"


def is_untracked_status(line: str) -> bool:
    return line[:2] == "??"


def dirty_pack_names(lines: list[str]) -> set[str]:
    packs: set[str] = set()
    for line in lines:
        for path in status_paths(line):
            top = pack_from_path(path)
            if top.endswith("-Skills"):
                packs.add(top)
    return packs


def dirty_worktree_breakdown(lines: list[str]) -> dict[str, Any]:
    pack_names: set[str] = set()
    pack_paths: list[str] = []
    root_lines: list[str] = []
    root_paths: list[str] = []
    root_tracked_paths: list[str] = []
    root_untracked_paths: list[str] = []
    for line in lines:
        line_has_root_path = False
        for path in status_paths(line):
            top = pack_from_path(path)
            if top.endswith("-Skills"):
                pack_names.add(top)
                pack_paths.append(path)
            else:
                line_has_root_path = True
                root_paths.append(path)
                if is_untracked_status(line):
                    root_untracked_paths.append(path)
                else:
                    root_tracked_paths.append(path)
        if line_has_root_path:
            root_lines.append(line)
    pack_paths_unique = unique_ordered(pack_paths)
    root_paths_unique = unique_ordered(root_paths)
    root_tracked_paths_unique = unique_ordered(root_tracked_paths)
    root_untracked_paths_unique = unique_ordered(root_untracked_paths)
    return {
        "dirty_pack_names": sorted(pack_names),
        "dirty_pack_count": len(pack_names),
        "dirty_pack_paths": pack_paths_unique,
        "dirty_pack_path_count": len(pack_paths_unique),
        "dirty_root_lines": root_lines,
        "dirty_root_count": len(root_lines),
        "dirty_root_paths": root_paths_unique,
        "dirty_root_path_count": len(root_paths_unique),
        "dirty_root_tracked_paths": root_tracked_paths_unique,
        "dirty_root_tracked_path_count": len(root_tracked_paths_unique),
        "dirty_root_untracked_paths": root_untracked_paths_unique,
        "dirty_root_untracked_path_count": len(root_untracked_paths_unique),
        "dirty_root_pathspec_command": git_add_command(root_paths_unique),
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
    dirty_lines = lines[1:]
    return {
        "branch": lines[0] if lines else "",
        "dirty_lines": dirty_lines,
        "dirty_count": len(dirty_lines),
        **dirty_worktree_breakdown(dirty_lines),
    }


def worktree_boundary_summary(git: dict[str, Any]) -> dict[str, Any]:
    pack_names = [str(pack) for pack in git.get("dirty_pack_names", [])]
    root_paths = [str(path) for path in git.get("dirty_root_paths", [])]
    root_tracked_paths = [str(path) for path in git.get("dirty_root_tracked_paths", [])]
    root_untracked_paths = [str(path) for path in git.get("dirty_root_untracked_paths", [])]
    payload = {
        "branch": str(git.get("branch", "")),
        "dirty_lines": [str(line) for line in git.get("dirty_lines", [])],
        "dirty_pack_names": pack_names,
        "dirty_root_paths": root_paths,
        "dirty_root_tracked_paths": root_tracked_paths,
        "dirty_root_untracked_paths": root_untracked_paths,
        "dirty_root_pathspec_command": str(git.get("dirty_root_pathspec_command", "")),
    }
    return {
        "worktree_boundary": {
            "branch": payload["branch"],
            "dirty_count": int(git.get("dirty_count", len(payload["dirty_lines"]))),
            "dirty_pack_count": int(git.get("dirty_pack_count", len(pack_names))),
            "dirty_root_count": int(git.get("dirty_root_count", len(git.get("dirty_root_lines", [])))),
            "dirty_root_path_count": int(git.get("dirty_root_path_count", len(root_paths))),
            "dirty_root_tracked_path_count": int(git.get("dirty_root_tracked_path_count", len(root_tracked_paths))),
            "dirty_root_untracked_path_count": int(git.get("dirty_root_untracked_path_count", len(root_untracked_paths))),
            "root_staging_command": payload["dirty_root_pathspec_command"],
            "fingerprint": hashlib.sha256(
                json.dumps(payload, ensure_ascii=False, sort_keys=True).encode("utf-8")
            ).hexdigest()[:12],
        }
    }


def worktree_boundary_line(summary: dict[str, Any]) -> str:
    boundary = summary.get("worktree_boundary")
    if not isinstance(boundary, dict):
        git = summary.get("git", {})
        boundary = worktree_boundary_summary(git if isinstance(git, dict) else {})["worktree_boundary"]
    fingerprint = str(boundary.get("fingerprint", ""))
    suffix = f"; sha256 {fingerprint}" if fingerprint else ""
    return (
        f"{int(boundary.get('dirty_count', 0))} dirty / "
        f"{int(boundary.get('dirty_pack_count', 0))} pack lanes / "
        f"{int(boundary.get('dirty_root_count', 0))} root-tooling entries{suffix}"
    )


def validate_worktree_boundary(summary: dict[str, Any]) -> list[str]:
    if "generated_at" not in summary and "worktree_boundary" not in summary:
        return []
    errors: list[str] = []
    git = summary.get("git")
    if not isinstance(git, dict):
        return ["worktree_boundary requires git summary"]
    expected = worktree_boundary_summary(git)["worktree_boundary"]
    boundary = summary.get("worktree_boundary")
    if not isinstance(boundary, dict):
        return ["worktree_boundary missing or not an object"]
    for key, expected_value in expected.items():
        if boundary.get(key) != expected_value:
            errors.append(f"worktree_boundary.{key} expected {expected_value!r}, observed {boundary.get(key)!r}")
    return errors


def build_summary(args: argparse.Namespace) -> dict[str, Any]:
    counts = parse_counts(run([PYTHON, "tools/audit_repo.py", "--counts"]))
    quality_rows = json.loads(run([PYTHON, "tools/quality_scorecard.py", "--json"]))
    source_rows = json.loads(run([PYTHON, "tools/source_map_audit.py", "--json"]))
    root_rows = json.loads(run([PYTHON, "tools/root_entry_audit.py", "--json"]))
    quality = score_summary(quality_rows, args.score_target, args.limit)
    execution_bridge = execution_bridge_summary(quality_rows, args.limit)
    source_maps = source_summary(source_rows, args.limit)
    claims_context = read_claims_context()
    claims = claims_summary(quality, execution_bridge, source_maps, claims_context)
    git = git_status()
    candidate_pool_data = candidate_pool(
        quality_rows,
        source_rows,
        execution_bridge["missing_packs"],
        claims_context,
        dirty_pack_names(git["dirty_lines"]),
        args.limit,
    )
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

    summary = {
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "counts": counts,
        "quality": quality,
        "execution_bridge": execution_bridge,
        "source_maps": source_maps,
        "root_entries": root_summary(root_rows),
        **external_links_summary(),
        "clone_audit": clone,
        "claims": claims,
        "candidate_pool": candidate_pool_data,
        "loop_control": loop_control_summary(execution_bridge, claims_context, claims, candidate_pool_data),
        "worklog": worklog_summary(),
        "git": git,
        **worktree_boundary_summary(git),
        "publish_units": publish_units_from_git(git),
        **schema_summary(),
        **command_plan_summary(),
        "targets": {
            "score_floor": args.score_target,
            "clone_fail_threshold": args.clone_fail_threshold,
            "display_limit": args.limit,
        },
    }
    summary["owner_clearance_queue"] = owner_clearance_queue(summary)
    summary.update(execution_bridge_tail_summary(summary))
    summary.update(safe_content_queue_summary(summary))
    summary.update(content_edit_policy_summary(summary))
    summary.update(remaining_debt_summary(summary))
    summary.update(next_batch_plan_summary(summary))
    summary.update(publish_policy_summary(summary))
    summary.update(skillopt_gate_plan_summary(summary))
    summary.update(goal_progress_summary(summary))
    summary.update(completion_audit_summary(summary))
    summary.update(handoff_manifest_summary(summary))
    summary.update(current_next_queue_summary(summary))
    summary.update(schema_summary(summary))
    if args.compare_json:
        summary["delta"] = compare_delta(load_compare_json(args.compare_json), summary)
    return summary


def status_label(ok: bool, skipped: bool = False) -> str:
    if skipped:
        return "Skipped"
    return "OK" if ok else "Review"


def claims_source_line(claims: dict[str, Any]) -> str:
    path = claims.get("path", ".maintenance/CLAIMS.md")
    if not claims.get("present"):
        return f"{path}; missing"
    fingerprint = claims.get("fingerprint", "")
    suffix = f"; sha256 {fingerprint}" if fingerprint else ""
    return (
        f"{path}; {claims.get('row_count', 0)} rows; "
        f"{claims.get('active_row_count', 0)} active; {claims.get('line_count', 0)} lines{suffix}"
    )


def working_tree_line(git: dict[str, Any]) -> str:
    dirty_count = int(git.get("dirty_count", len(git.get("dirty_lines", []))))
    pack_count = int(git.get("dirty_pack_count", 0))
    root_count = int(git.get("dirty_root_count", 0))
    return (
        f"{git.get('branch', '')} with {dirty_count} dirty entries "
        f"({pack_count} pack lanes, {root_count} root/tooling entries)"
    )


def format_items_with_remainder(items: list[str], limit: int = 8, *, code: bool = False) -> str:
    if not items:
        return "none"
    rendered = [f"`{item}`" if code else item for item in items[:limit]]
    text = "; ".join(rendered)
    remaining = len(items) - limit
    if remaining > 0:
        return f"{text}; +{remaining} more"
    return text


def dirty_status_line(line: str) -> str:
    return line.strip()


def dirty_boundary_lines(git: dict[str, Any], *, pack_limit: int = 8, root_limit: int = 8) -> list[str]:
    pack_names = [str(pack) for pack in git.get("dirty_pack_names", [])]
    root_lines = [dirty_status_line(str(line)) for line in git.get("dirty_root_lines", [])]
    root_paths = [str(path) for path in git.get("dirty_root_paths", [])]
    tracked_paths = [str(path) for path in git.get("dirty_root_tracked_paths", [])]
    untracked_paths = [str(path) for path in git.get("dirty_root_untracked_paths", [])]
    root_command = str(git.get("dirty_root_pathspec_command", ""))
    return [
        "- Dirty pack lanes: " + format_items_with_remainder(pack_names, pack_limit),
        "- Root/tooling dirty entries: " + format_items_with_remainder(root_lines, root_limit, code=True),
        "- Root/tooling paths: " + format_items_with_remainder(root_paths, root_limit, code=True),
        "- Root/tooling tracked paths: " + format_items_with_remainder(tracked_paths, root_limit, code=True),
        "- Root/tooling untracked paths: " + format_items_with_remainder(untracked_paths, root_limit, code=True),
        "- Root/tooling staging preview: " + (f"`{root_command}`" if root_command else "none"),
    ]


def publish_units_from_git(git: dict[str, Any]) -> dict[str, Any]:
    root_paths = [str(path) for path in git.get("dirty_root_paths", [])]
    tracked_paths = [str(path) for path in git.get("dirty_root_tracked_paths", [])]
    untracked_paths = [str(path) for path in git.get("dirty_root_untracked_paths", [])]
    pack_names = [str(pack) for pack in git.get("dirty_pack_names", [])]
    pack_paths = [str(path) for path in git.get("dirty_pack_paths", [])]
    return {
        "root_tooling": {
            "status": "ready" if root_paths else "empty",
            "paths": root_paths,
            "path_count": len(root_paths),
            "tracked_paths": tracked_paths,
            "tracked_path_count": len(tracked_paths),
            "untracked_paths": untracked_paths,
            "untracked_path_count": len(untracked_paths),
            "staging_command": str(git.get("dirty_root_pathspec_command", "")),
            "note": "Path-scoped root/tooling unit; review before staging.",
        },
        "pack_content": {
            "status": "needs-owner-review" if pack_names else "empty",
            "packs": pack_names,
            "pack_count": len(pack_names),
            "paths": pack_paths,
            "path_count": len(pack_paths),
            "note": "Keep content pack lanes separate from root/tooling publishes unless explicitly cleared.",
        },
    }


def publish_units_data(summary: dict[str, Any]) -> dict[str, Any]:
    units = summary.get("publish_units")
    if isinstance(units, dict):
        return units
    git = summary.get("git", {})
    return publish_units_from_git(git if isinstance(git, dict) else {})


def publish_unit_lines(summary: dict[str, Any], *, limit: int = 8) -> list[str]:
    units = publish_units_data(summary)
    root = units.get("root_tooling", {}) if isinstance(units.get("root_tooling"), dict) else {}
    pack = units.get("pack_content", {}) if isinstance(units.get("pack_content"), dict) else {}
    root_paths = [str(path) for path in root.get("paths", [])]
    pack_names = [str(name) for name in pack.get("packs", [])]
    command = str(root.get("staging_command", ""))
    return [
        (
            f"- Root/tooling unit: {root.get('status', 'unknown')}; "
            f"{int(root.get('path_count', len(root_paths)))} paths "
            f"({int(root.get('tracked_path_count', 0))} tracked, "
            f"{int(root.get('untracked_path_count', 0))} untracked)"
        ),
        "- Root/tooling paths: " + format_items_with_remainder(root_paths, limit, code=True),
        "- Root/tooling command: " + (f"`{command}`" if command else "none"),
        (
            f"- Pack content units: {pack.get('status', 'unknown')}; "
            f"{int(pack.get('pack_count', len(pack_names)))} pack lanes"
        ),
        "- Pack content packs: " + format_items_with_remainder(pack_names, limit),
    ]


def readiness_rows(summary: dict[str, Any]) -> list[tuple[str, str, str]]:
    quality = summary["quality"]
    source_maps = summary["source_maps"]
    root_entries = summary["root_entries"]
    clone = summary["clone_audit"]
    worklog = summary["worklog"]
    claims = summary["claims"]
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
        (
            "Worklog health",
            status_label(worklog.get("status") == "OK"),
            f"{worklog.get('status', 'Review')}; {worklog.get('loop_count', 0)} loops; latest {worklog.get('latest_heading', '')}",
        ),
        (
            "Claims boundary",
            status_label(bool(claims.get("present")) and int(claims.get("row_count", 0)) > 0),
            claims_source_line(claims),
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
            status_label(int(git.get("dirty_count", len(git["dirty_lines"]))) == 0),
            working_tree_line(git),
        )
    )
    return rows


def format_delta_value(value: Any, precision: int = 0) -> str:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return str(value)
    if precision > 0:
        return f"{float(value):.{precision}f}"
    if isinstance(value, float) and not value.is_integer():
        return f"{value:.1f}"
    return str(int(value))


def format_signed_delta(value: Any, precision: int = 0) -> str:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return str(value)
    if value > 0:
        return f"+{format_delta_value(value, precision)}"
    return format_delta_value(value, precision)


def format_text_delta_status(row: dict[str, Any]) -> str:
    return "changed" if row.get("changed") else "unchanged"


def delta_rows(summary: dict[str, Any]) -> list[dict[str, Any]]:
    delta = summary.get("delta", {})
    metrics = delta.get("metrics", {}) if isinstance(delta, dict) else {}
    rows: list[dict[str, Any]] = []
    for key, _label, _path, _precision in DELTA_METRICS:
        metric = metrics.get(key)
        if isinstance(metric, dict):
            rows.append(metric)
    return rows


def delta_text_rows(summary: dict[str, Any]) -> list[dict[str, Any]]:
    delta = summary.get("delta", {})
    metrics = delta.get("text", {}) if isinstance(delta, dict) else {}
    rows: list[dict[str, Any]] = []
    for key, _label, _path in DELTA_TEXT_METRICS:
        metric = metrics.get(key)
        if isinstance(metric, dict):
            rows.append(metric)
    return rows


def pack_list(rows: list[dict[str, Any]], limit: int = 3) -> str:
    return ", ".join(str(row["pack"]) for row in rows[:limit])


def pack_list_with_remainder(rows: list[dict[str, Any]], limit: int = 3) -> str:
    rendered = pack_list(rows, limit)
    remaining = len(rows) - limit
    if remaining > 0:
        return f"{rendered}; +{remaining} more"
    return rendered


def pack_reason_list_with_remainder(rows: list[dict[str, Any]], limit: int = 3, *, code: bool = False) -> str:
    rendered: list[str] = []
    for row in rows[:limit]:
        pack = str(row.get("pack", ""))
        reason = str(row.get("reason", "")).replace("|", "/")
        pack_text = f"`{pack}`" if code else pack
        rendered.append(f"{pack_text} ({reason})" if reason else pack_text)
    remaining = len(rows) - limit
    text = "; ".join(rendered)
    if remaining > 0:
        return f"{text}; +{remaining} more"
    return text


def source_map_list(rows: list[dict[str, Any]], limit: int = 3) -> str:
    return ", ".join(f"`{row['path']}`" for row in rows[:limit])


def claim_pack_reason(summary: dict[str, Any], pack: str) -> str:
    return str(summary.get("claims", {}).get("sensitive_packs", {}).get(pack, ""))


def unclaimed_score_rows(summary: dict[str, Any]) -> list[dict[str, Any]]:
    return list(summary.get("candidate_pool", {}).get("score_unclaimed", []))


def score_ceiling_rows(summary: dict[str, Any]) -> list[dict[str, Any]]:
    return list(summary.get("candidate_pool", {}).get("score_ceiling", []))


def unclaimed_source_rows(summary: dict[str, Any]) -> list[dict[str, Any]]:
    return list(summary.get("candidate_pool", {}).get("source_map_unclaimed", []))


def unclaimed_bridge_rows(summary: dict[str, Any]) -> list[dict[str, Any]]:
    return list(summary.get("candidate_pool", {}).get("execution_bridge_unclaimed", []))


def execution_bridge_clearance_rows(summary: dict[str, Any]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    seen: set[str] = set()
    for row in summary.get("execution_bridge", {}).get("missing_packs", []):
        pack = str(row.get("pack", ""))
        if not pack or pack in seen:
            continue
        reason = claim_pack_reason(summary, pack)
        if not reason:
            continue
        seen.add(pack)
        rows.append({"pack": pack, "reason": reason})
    return rows


EXECUTION_BRIDGE_TAIL_CONTRACT = "monthly-uplift-execution-bridge-tail-v3"


def execution_bridge_tail_summary(summary: dict[str, Any]) -> dict[str, Any]:
    execution_bridge = summary.get("execution_bridge", {}) if isinstance(summary.get("execution_bridge"), dict) else {}
    loop_control = summary.get("loop_control", {}) if isinstance(summary.get("loop_control"), dict) else {}
    missing_rows = execution_bridge.get("missing_packs", [])
    if not isinstance(missing_rows, list):
        missing_rows = []
    unclaimed_rows = unclaimed_bridge_rows(summary)
    clearance_rows = execution_bridge_clearance_rows(summary)
    missing_total = int(execution_bridge.get("missing", len(missing_rows)))
    unclaimed_count = int(loop_control.get("unclaimed_execution_bridge_candidates", len(unclaimed_rows)))
    owner_clearance_count = len(clearance_rows)

    if missing_total == 0:
        status = "complete"
        recommended_action = "none"
        recommendation_scope = "complete"
        blocked_recommendation = "none"
        claim_sensitive_policy = "complete-no-wiring-needed"
        reason = "execution-bridge wiring is complete for all empirical depth packs"
    elif unclaimed_count > 0:
        status = "unclaimed-candidates"
        recommended_action = "wire-unclaimed"
        recommendation_scope = "unclaimed-only"
        blocked_recommendation = (
            "leave-owner-clearance-rows-blocked" if owner_clearance_count else "none"
        )
        if owner_clearance_count:
            claim_sensitive_policy = "split-wire-unclaimed-request-clearance"
            reason = (
                "wire only unclaimed execution-bridge rows; remaining bridge gaps need owner clearance"
            )
        else:
            claim_sensitive_policy = "wire-unclaimed"
            reason = "unclaimed execution-bridge candidates are safe after claim and dirty-pack filtering"
    elif owner_clearance_count > 0:
        status = "owner-clearance-required"
        recommended_action = "request-owner-clearance"
        recommendation_scope = "owner-clearance-only"
        blocked_recommendation = "request-owner-clearance-before-wiring"
        claim_sensitive_policy = "clearance-before-wiring"
        reason = "remaining execution-bridge gaps are claim-sensitive"
    else:
        status = "monitoring"
        recommended_action = "inspect-claims-and-scorecard"
        recommendation_scope = "review-tail"
        blocked_recommendation = "inspect-claims-before-wiring"
        claim_sensitive_policy = "inspect-before-wiring"
        reason = "execution-bridge gaps remain but no actionable unclaimed or owner-clearance rows are visible"

    safe_to_wire_packs = [
        str(row.get("pack", ""))
        for row in unclaimed_rows
        if isinstance(row, dict) and str(row.get("pack", ""))
    ]
    blocked_owner_clearance_packs = [row["pack"] for row in clearance_rows if row.get("pack")]

    tail: dict[str, Any] = {
        "contract": EXECUTION_BRIDGE_TAIL_CONTRACT,
        "status": status,
        "recommended_action": recommended_action,
        "recommendation_scope": recommendation_scope,
        "blocked_recommendation": blocked_recommendation,
        "claim_sensitive_policy": claim_sensitive_policy,
        "wiring_allowed_now": bool(unclaimed_count),
        "owner_clearance_required_before_wiring": bool(owner_clearance_count),
        "wired": int(execution_bridge.get("wired", 0)),
        "total": int(execution_bridge.get("empirical_depth_packs", 0)),
        "missing": missing_total,
        "unclaimed_count": unclaimed_count,
        "owner_clearance_count": owner_clearance_count,
        "owner_clearance_present": bool(owner_clearance_count),
        "owner_clearance_required": bool(owner_clearance_count and not unclaimed_count),
        "safe_to_wire_count": unclaimed_count,
        "blocked_owner_clearance_count": owner_clearance_count,
        "safe_to_wire_packs": safe_to_wire_packs,
        "blocked_owner_clearance_packs": blocked_owner_clearance_packs,
        "unclaimed": [
            {
                "pack": str(row.get("pack", "")),
                "score": float(row.get("score", 0.0)),
                "current_bridge_links": int(row.get("current_bridge_links", row.get("exec_bridge_skills", 0))),
            }
            for row in unclaimed_rows
            if isinstance(row, dict)
        ],
        "owner_clearance": clearance_rows,
        "reason": reason,
    }
    tail["fingerprint"] = hashlib.sha256(
        json.dumps(tail, ensure_ascii=False, sort_keys=True).encode("utf-8")
    ).hexdigest()[:12]
    return {"execution_bridge_tail": tail}


def execution_bridge_tail_line(summary: dict[str, Any]) -> str:
    tail = summary.get("execution_bridge_tail")
    if not isinstance(tail, dict):
        tail = execution_bridge_tail_summary(summary)["execution_bridge_tail"]
    fingerprint = str(tail.get("fingerprint", ""))
    suffix = f"; sha256 {fingerprint}" if fingerprint else ""
    blocked = str(tail.get("blocked_recommendation", "none"))
    blocked_part = f"; blocked {blocked}" if blocked and blocked != "none" else ""
    return (
        f"{tail.get('status', 'unknown')}; action {tail.get('recommended_action', 'unknown')}; "
        f"scope {tail.get('recommendation_scope', 'unknown')}; "
        f"policy {tail.get('claim_sensitive_policy', 'unknown')}; "
        f"wiring-now {str(bool(tail.get('wiring_allowed_now', False))).lower()}; "
        f"clearance-before-wiring {str(bool(tail.get('owner_clearance_required_before_wiring', False))).lower()}"
        f"{blocked_part}; "
        f"{int(tail.get('wired', 0))}/{int(tail.get('total', 0))} wired; "
        f"{int(tail.get('missing', 0))} missing; "
        f"{int(tail.get('unclaimed_count', 0))} unclaimed / "
        f"{int(tail.get('owner_clearance_count', 0))} owner-clearance{suffix}"
    )


def execution_bridge_tail_pack_line(summary: dict[str, Any], *, limit: int = 5, code: bool = False) -> str:
    tail = summary.get("execution_bridge_tail")
    if not isinstance(tail, dict):
        tail = execution_bridge_tail_summary(summary)["execution_bridge_tail"]
    safe_packs = [
        str(pack)
        for pack in tail.get("safe_to_wire_packs", [])
        if str(pack)
    ]
    blocked_rows: list[dict[str, Any]] = [
        row
        for row in tail.get("owner_clearance", [])
        if isinstance(row, dict) and str(row.get("pack", ""))
    ]
    if not blocked_rows:
        blocked_rows = [
            {"pack": str(pack), "reason": ""}
            for pack in tail.get("blocked_owner_clearance_packs", [])
            if str(pack)
        ]
    safe_text = format_items_with_remainder(safe_packs, limit, code=code)
    blocked_text = pack_reason_list_with_remainder(blocked_rows, limit, code=code) if blocked_rows else "none"
    return f"safe-to-wire {safe_text}; blocked owner-clearance {blocked_text}"


def validate_execution_bridge_tail(summary: dict[str, Any]) -> list[str]:
    if "generated_at" not in summary and "execution_bridge_tail" not in summary:
        return []
    expected = execution_bridge_tail_summary(summary)["execution_bridge_tail"]
    tail = summary.get("execution_bridge_tail")
    if not isinstance(tail, dict):
        return ["execution_bridge_tail missing or not an object"]
    errors: list[str] = []
    for key, expected_value in expected.items():
        if tail.get(key) != expected_value:
            errors.append(f"execution_bridge_tail.{key} expected {expected_value!r}, observed {tail.get(key)!r}")
    return errors


SAFE_CONTENT_QUEUE_CONTRACT = "monthly-uplift-safe-content-queue-v2"


def safe_content_queue_summary(summary: dict[str, Any]) -> dict[str, Any]:
    score_rows = unclaimed_score_rows(summary)
    ceiling_rows = score_ceiling_rows(summary)
    source_rows = unclaimed_source_rows(summary)
    bridge_rows = unclaimed_bridge_rows(summary)
    candidate_pool_data = summary.get("candidate_pool", {}) if isinstance(summary.get("candidate_pool"), dict) else {}
    dirty_rows = candidate_pool_data.get("dirty_skipped_packs", [])
    if not isinstance(dirty_rows, list):
        dirty_rows = []
    clearance_queue = owner_clearance_queue_data(summary)
    score_count = len(score_rows)
    ceiling_count = len(ceiling_rows)
    source_count = len(source_rows)
    bridge_count = len(bridge_rows)
    unclaimed_total = score_count + source_count + bridge_count
    dirty_skipped_count = len(dirty_rows)
    owner_clearance_total = int(clearance_queue.get("total", 0))

    if score_count:
        status = "ready"
        recommended_action = "harden-score-floor"
        reason = "unclaimed score candidates are available after claim and dirty-pack filtering"
    elif source_count:
        status = "ready"
        recommended_action = "repair-source-map"
        reason = "unclaimed source-map candidates are available after claim and dirty-pack filtering"
    elif bridge_count:
        status = "ready"
        recommended_action = "wire-execution-bridge"
        reason = "unclaimed execution-bridge candidates are available after claim and dirty-pack filtering"
    elif dirty_skipped_count:
        status = "dirty-in-progress"
        recommended_action = "finish-dirty-pack-lanes"
        reason = "candidate packs are already dirty in the shared worktree"
    elif owner_clearance_total:
        status = "owner-clearance-required"
        recommended_action = "request-owner-clearance"
        reason = "visible content debt is claim-sensitive"
    else:
        status = "monitoring"
        recommended_action = "monitor"
        reason = "no unclaimed content candidates are visible in the current target window"

    score_targets = [
        {
            "pack": str(row.get("pack", "")),
            "score": float(row.get("score", 0.0)),
            "weakest_skill": str(row.get("weakest_skill", "")),
        }
        for row in score_rows
        if isinstance(row, dict)
    ]
    source_targets = [
        {
            "pack": pack_from_path(str(row.get("path", ""))),
            "path": str(row.get("path", "")),
            "unresolved_flags": int(row.get("unresolved_flags", 0)),
        }
        for row in source_rows
        if isinstance(row, dict)
    ]
    bridge_targets = [
        {
            "pack": str(row.get("pack", "")),
            "score": float(row.get("score", 0.0)),
            "current_bridge_links": int(row.get("current_bridge_links", row.get("exec_bridge_skills", 0))),
            "weakest_skill": str(row.get("weakest_skill", "")),
        }
        for row in bridge_rows
        if isinstance(row, dict)
    ]
    queue: dict[str, Any] = {
        "contract": SAFE_CONTENT_QUEUE_CONTRACT,
        "status": status,
        "recommended_action": recommended_action,
        "unclaimed_total": unclaimed_total,
        "score_count": score_count,
        "source_map_count": source_count,
        "execution_bridge_count": bridge_count,
        "score_ceiling_count": ceiling_count,
        "dirty_skipped_count": dirty_skipped_count,
        "owner_clearance_total": owner_clearance_total,
        "score_targets": score_targets,
        "score_ceiling": [
            {
                "pack": str(row.get("pack", "")),
                "score": float(row.get("score", 0.0)),
                "weakest_skill": str(row.get("weakest_skill", "")),
                "reason": str(row.get("reason", "")),
            }
            for row in ceiling_rows
            if isinstance(row, dict)
        ],
        "source_map_targets": source_targets,
        "execution_bridge_targets": bridge_targets,
        "dirty_skipped": [
            {"pack": str(row.get("pack", ""))}
            for row in dirty_rows
            if isinstance(row, dict)
        ],
        "reason": reason,
    }
    queue["fingerprint"] = hashlib.sha256(
        json.dumps(queue, ensure_ascii=False, sort_keys=True).encode("utf-8")
    ).hexdigest()[:12]
    return {"safe_content_queue": queue}


def safe_content_queue_line(summary: dict[str, Any]) -> str:
    queue = summary.get("safe_content_queue")
    if not isinstance(queue, dict):
        queue = safe_content_queue_summary(summary)["safe_content_queue"]
    fingerprint = str(queue.get("fingerprint", ""))
    suffix = f"; sha256 {fingerprint}" if fingerprint else ""
    return (
        f"{queue.get('status', 'unknown')}; action {queue.get('recommended_action', 'unknown')}; "
        f"{int(queue.get('unclaimed_total', 0))} unclaimed "
        f"(score {int(queue.get('score_count', 0))} / source {int(queue.get('source_map_count', 0))} / "
        f"bridge {int(queue.get('execution_bridge_count', 0))}); "
        f"{int(queue.get('score_ceiling_count', 0))} score-ceiling; "
        f"{int(queue.get('dirty_skipped_count', 0))} dirty skipped{suffix}"
    )


def validate_safe_content_queue(summary: dict[str, Any]) -> list[str]:
    if "generated_at" not in summary and "safe_content_queue" not in summary:
        return []
    expected = safe_content_queue_summary(summary)["safe_content_queue"]
    queue = summary.get("safe_content_queue")
    if not isinstance(queue, dict):
        return ["safe_content_queue missing or not an object"]
    errors: list[str] = []
    for key, expected_value in expected.items():
        if queue.get(key) != expected_value:
            errors.append(f"safe_content_queue.{key} expected {expected_value!r}, observed {queue.get(key)!r}")
    return errors


def claim_sensitive_groups(summary: dict[str, Any], limit: int | None = 5) -> dict[str, list[dict[str, str]]]:
    groups: dict[str, list[dict[str, str]]] = {}
    seen: set[tuple[str, str]] = set()
    targets = summary.get("claims", {}).get("sensitive_current_targets", [])
    for target in targets:
        kind = str(target.get("kind", ""))
        pack = str(target.get("pack", ""))
        if not kind or not pack:
            continue
        key = (kind, pack)
        if key in seen:
            continue
        seen.add(key)
        rows = groups.setdefault(kind, [])
        if limit is None or len(rows) < limit:
            rows.append({"pack": pack, "reason": str(target.get("reason", ""))})
    return groups


def claim_sensitive_group_totals(summary: dict[str, Any]) -> dict[str, int]:
    totals: dict[str, int] = {}
    seen: set[tuple[str, str]] = set()
    targets = summary.get("claims", {}).get("sensitive_current_targets", [])
    for target in targets:
        kind = str(target.get("kind", ""))
        pack = str(target.get("pack", ""))
        if not kind or not pack:
            continue
        key = (kind, pack)
        if key in seen:
            continue
        seen.add(key)
        totals[kind] = totals.get(kind, 0) + 1
    return totals


def owner_clearance_target_fingerprint(rows: list[dict[str, str]]) -> str:
    normalized = [
        {"pack": str(row.get("pack", "")), "reason": str(row.get("reason", ""))}
        for row in rows
        if isinstance(row, dict)
    ]
    return hashlib.sha256(
        json.dumps(normalized, ensure_ascii=False, sort_keys=True).encode("utf-8")
    ).hexdigest()[:12]


def owner_clearance_queue_fingerprint(queue: dict[str, Any]) -> str:
    groups: dict[str, Any] = {}
    total = 0
    for kind in OWNER_CLEARANCE_KINDS:
        row = queue.get(kind)
        if not isinstance(row, dict):
            continue
        displayed = row.get("displayed", [])
        if not isinstance(displayed, list):
            displayed = []
        targets = row.get("targets", [])
        if not isinstance(targets, list):
            targets = []
        normalized_displayed = [
            {"pack": str(item.get("pack", "")), "reason": str(item.get("reason", ""))}
            for item in displayed
            if isinstance(item, dict)
        ]
        normalized_targets = [
            {"pack": str(item.get("pack", "")), "reason": str(item.get("reason", ""))}
            for item in targets
            if isinstance(item, dict)
        ]
        row_total = int(row.get("total", 0))
        total += row_total
        groups[kind] = {
            "total": row_total,
            "display_limit": int(row.get("display_limit", 0)),
            "displayed": normalized_displayed,
            "targets": normalized_targets,
            "target_fingerprint": str(row.get("target_fingerprint", "")),
            "omitted": int(row.get("omitted", 0)),
            "truncated": bool(row.get("truncated", False)),
        }
    payload = {"contract": OWNER_CLEARANCE_QUEUE_CONTRACT, "total": total, "groups": groups}
    return hashlib.sha256(json.dumps(payload, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()[:12]


def owner_clearance_queue(summary: dict[str, Any], limit: int = 5) -> dict[str, Any]:
    groups = claim_sensitive_groups(summary, limit=None)
    totals = {kind: len(rows) for kind, rows in groups.items()}
    queue: dict[str, Any] = {"contract": OWNER_CLEARANCE_QUEUE_CONTRACT}
    for kind in OWNER_CLEARANCE_KINDS:
        total = totals.get(kind, 0)
        target_rows = groups.get(kind, [])
        rows = target_rows[:limit]
        if not total and not rows:
            continue
        omitted = max(total - len(rows), 0)
        queue[kind] = {
            "total": total,
            "display_limit": limit,
            "displayed": rows,
            "targets": target_rows,
            "target_fingerprint": owner_clearance_target_fingerprint(target_rows),
            "omitted": omitted,
            "truncated": omitted > 0,
        }
    queue["total"] = sum(int(queue.get(kind, {}).get("total", 0)) for kind in OWNER_CLEARANCE_KINDS)
    queue["fingerprint"] = owner_clearance_queue_fingerprint(queue)
    return queue


def owner_clearance_queue_data(summary: dict[str, Any]) -> dict[str, Any]:
    queue = summary.get("owner_clearance_queue")
    if isinstance(queue, dict):
        return queue
    return owner_clearance_queue(summary)


def owner_clearance_kind_line(queue: dict[str, Any], kind: str, label: str) -> str:
    row = queue.get(kind)
    if not isinstance(row, dict):
        return f"{label} 0"
    total = int(row.get("total", 0))
    displayed = row.get("displayed", [])
    shown = len(displayed) if isinstance(displayed, list) else 0
    omitted = int(row.get("omitted", 0))
    if total == 0:
        return f"{label} 0"
    if omitted > 0:
        return f"{label} {total} ({shown} shown, +{omitted} more)"
    return f"{label} {total} ({shown} shown)"


def owner_clearance_queue_line(summary: dict[str, Any]) -> str:
    queue = owner_clearance_queue_data(summary)
    fingerprint = str(queue.get("fingerprint", ""))
    suffix = f"; sha256 {fingerprint}" if fingerprint else ""
    parts = [
        owner_clearance_kind_line(queue, "score-floor", "score"),
        owner_clearance_kind_line(queue, "source-map", "source"),
        owner_clearance_kind_line(queue, "execution-bridge", "bridge"),
    ]
    return (
        f"{queue.get('contract', OWNER_CLEARANCE_QUEUE_CONTRACT)}; "
        f"{int(queue.get('total', 0))} targets; "
        f"{' / '.join(parts)}{suffix}"
    )


def owner_clearance_target_fingerprint_line(summary: dict[str, Any]) -> str:
    queue = owner_clearance_queue_data(summary)
    parts: list[str] = []
    for kind, label in (
        ("score-floor", "score"),
        ("source-map", "source"),
        ("execution-bridge", "bridge"),
    ):
        row = queue.get(kind)
        fingerprint = str(row.get("target_fingerprint", "")) if isinstance(row, dict) else ""
        parts.append(f"{label} {fingerprint or 'none'}")
    queue_fingerprint = str(queue.get("fingerprint", ""))
    suffix = f"; queue sha256 {queue_fingerprint}" if queue_fingerprint else ""
    return f"{' / '.join(parts)}{suffix}"


def completion_audit_owner_target_fingerprint_line(summary: dict[str, Any]) -> str:
    audit = summary.get("completion_audit")
    if not isinstance(audit, dict):
        audit = completion_audit_summary(summary)["completion_audit"]
    parts = [
        f"score {str(audit.get('owner_clearance_score_target_fingerprint', '')) or 'none'}",
        f"source {str(audit.get('owner_clearance_source_target_fingerprint', '')) or 'none'}",
        f"bridge {str(audit.get('owner_clearance_bridge_target_fingerprint', '')) or 'none'}",
    ]
    queue_fingerprint = str(audit.get("owner_clearance_queue_fingerprint", ""))
    suffix = f"; queue sha256 {queue_fingerprint}" if queue_fingerprint else ""
    return f"{' / '.join(parts)}{suffix}"


def clearance_remainder_from_row(row: dict[str, Any]) -> str:
    omitted = int(row.get("omitted", 0))
    if omitted > 0:
        return f"; +{omitted} more"
    return ""


def list_fingerprint(items: list[str]) -> str:
    payload = json.dumps(items, ensure_ascii=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:12]


def next_batches(summary: dict[str, Any]) -> list[str]:
    quality = summary["quality"]
    execution_bridge = summary["execution_bridge"]
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

    if int(execution_bridge["missing"]) > 0:
        unclaimed_missing = unclaimed_bridge_rows(summary)
        claimed_missing = execution_bridge_clearance_rows(summary)
        if unclaimed_missing:
            batches.append(
                "Finish the unclaimed execution-bridge tail with lightweight links to "
                "`shared-resources/empirical-methods/execution-with-mcp.md`: "
                f"{pack_list(unclaimed_missing)}."
            )
        if claimed_missing:
            batches.append(
                "The remaining execution-bridge tail is claim-sensitive; get owner clearance before wiring: "
                f"{pack_reason_list_with_remainder(claimed_missing)}."
            )
    else:
        batches.append("Execution-bridge wiring is complete for all empirical depth packs.")

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


def next_batch_plan_summary(summary: dict[str, Any]) -> dict[str, Any]:
    batches = next_batches(summary)
    return {
        "next_batches": batches,
        "next_batch_plan": {
            "contract": NEXT_BATCH_PLAN_CONTRACT,
            "count": len(batches),
            "fingerprint": list_fingerprint(batches),
        },
    }


def summary_next_batches(summary: dict[str, Any]) -> list[str]:
    value = summary.get("next_batches")
    if isinstance(value, list) and value and all(isinstance(item, str) and item.strip() for item in value):
        return value
    return next_batches(summary)


def next_batch_plan_line(summary: dict[str, Any]) -> str:
    plan = summary.get("next_batch_plan")
    if not isinstance(plan, dict):
        plan = next_batch_plan_summary(summary)["next_batch_plan"]
    fingerprint = str(plan.get("fingerprint", ""))
    suffix = f"; sha256 {fingerprint}" if fingerprint else ""
    return f"{int(plan.get('count', 0))} items{suffix}"


def validate_next_batch_plan(summary: dict[str, Any]) -> list[str]:
    if "next_batches" not in summary and "next_batch_plan" not in summary:
        return []
    errors: list[str] = []
    expected = next_batch_plan_summary(summary)
    batches = summary.get("next_batches")
    if not isinstance(batches, list):
        errors.append("next_batches missing or not a list")
    elif not batches:
        errors.append("next_batches must not be empty")
    elif not all(isinstance(item, str) and item.strip() for item in batches):
        errors.append("next_batches must contain only non-empty strings")
    elif batches != expected["next_batches"]:
        errors.append("next_batches does not match the computed next-batch plan")

    plan = summary.get("next_batch_plan")
    if not isinstance(plan, dict):
        errors.append("next_batch_plan missing or not an object")
    else:
        for key, expected_value in expected["next_batch_plan"].items():
            if plan.get(key) != expected_value:
                errors.append(f"next_batch_plan.{key} expected {expected_value!r}, observed {plan.get(key)!r}")
    return errors


CONTENT_EDIT_POLICY_CONTRACT = "content-edit-policy-v2"


def content_edit_policy_summary(summary: dict[str, Any]) -> dict[str, Any]:
    loop_control = summary.get("loop_control", {}) if isinstance(summary.get("loop_control"), dict) else {}
    execution_bridge = summary.get("execution_bridge", {}) if isinstance(summary.get("execution_bridge"), dict) else {}
    bridge_tail = summary.get("execution_bridge_tail", {}) if isinstance(summary.get("execution_bridge_tail"), dict) else {}
    boundary = summary.get("worktree_boundary", {}) if isinstance(summary.get("worktree_boundary"), dict) else {}
    status = str(loop_control.get("status", ""))
    next_lane = str(loop_control.get("next_lane", ""))
    unclaimed_count = sum(
        int(loop_control.get(key, 0))
        for key in (
            "unclaimed_score_candidates",
            "unclaimed_source_map_candidates",
            "unclaimed_execution_bridge_candidates",
        )
    )
    claim_sensitive_count = sum(
        int(loop_control.get(key, 0))
        for key in (
            "claim_sensitive_score_targets",
            "claim_sensitive_source_map_targets",
            "claim_sensitive_execution_bridge_targets",
        )
    )
    dirty_pack_count = int(boundary.get("dirty_pack_count", 0))
    content_edits_allowed = next_lane == "content" and unclaimed_count > 0
    owner_clearance_required = status == "owner-clearance-needed" or (
        claim_sensitive_count > 0 and unclaimed_count == 0
    )
    if bridge_tail:
        execution_bridge_owner_clearance_required = bool(
            bridge_tail.get("owner_clearance_present", bridge_tail.get("owner_clearance_required", False))
        )
    else:
        execution_bridge_owner_clearance_required = (
            int(execution_bridge.get("missing", 0)) > 0
            and int(loop_control.get("claim_sensitive_execution_bridge_targets", 0)) > 0
            and int(loop_control.get("unclaimed_execution_bridge_candidates", 0)) == 0
        )
    tooling_only_recommended = not content_edits_allowed and next_lane in {"tooling", "tooling-or-owner-clearance"}
    if content_edits_allowed:
        policy_status = "content-allowed"
        reason = "unclaimed content candidates are available after claim and dirty-pack filtering"
    elif owner_clearance_required:
        policy_status = "owner-clearance-required"
        reason = "visible content debt is claim-sensitive or already dirty; keep work in tooling unless owner clearance is granted"
    else:
        policy_status = "tooling-monitoring"
        reason = "no unclaimed or claim-sensitive content debt is visible in the current target window"

    policy: dict[str, Any] = {
        "contract": CONTENT_EDIT_POLICY_CONTRACT,
        "status": policy_status,
        "next_lane": next_lane,
        "content_edits_allowed": content_edits_allowed,
        "owner_clearance_required": owner_clearance_required,
        "tooling_only_recommended": tooling_only_recommended,
        "execution_bridge_owner_clearance_required": execution_bridge_owner_clearance_required,
        "unclaimed_candidate_count": unclaimed_count,
        "claim_sensitive_target_count": claim_sensitive_count,
        "dirty_pack_lane_count": dirty_pack_count,
        "reason": reason,
    }
    policy["fingerprint"] = hashlib.sha256(
        json.dumps(policy, ensure_ascii=False, sort_keys=True).encode("utf-8")
    ).hexdigest()[:12]
    return {"content_edit_policy": policy}


def content_edit_policy_line(summary: dict[str, Any]) -> str:
    policy = summary.get("content_edit_policy")
    if not isinstance(policy, dict):
        policy = content_edit_policy_summary(summary)["content_edit_policy"]
    fingerprint = str(policy.get("fingerprint", ""))
    suffix = f"; sha256 {fingerprint}" if fingerprint else ""
    gate = "content allowed" if policy.get("content_edits_allowed") else "content blocked"
    bridge_gate = "; bridge owner-clearance" if policy.get("execution_bridge_owner_clearance_required") else ""
    return (
        f"{policy.get('status', 'unknown')}; {gate}; next {policy.get('next_lane', 'unknown')}; "
        f"{int(policy.get('unclaimed_candidate_count', 0))} unclaimed / "
        f"{int(policy.get('claim_sensitive_target_count', 0))} claim-sensitive; "
        f"{int(policy.get('dirty_pack_lane_count', 0))} dirty pack lanes{bridge_gate}{suffix}"
    )


def validate_content_edit_policy(summary: dict[str, Any]) -> list[str]:
    if "generated_at" not in summary and "content_edit_policy" not in summary:
        return []
    expected = content_edit_policy_summary(summary)["content_edit_policy"]
    policy = summary.get("content_edit_policy")
    if not isinstance(policy, dict):
        return ["content_edit_policy missing or not an object"]
    errors: list[str] = []
    for key, expected_value in expected.items():
        if policy.get(key) != expected_value:
            errors.append(f"content_edit_policy.{key} expected {expected_value!r}, observed {policy.get(key)!r}")
    return errors


REMAINING_DEBT_CONTRACT = "monthly-uplift-remaining-debt-v2"


def remaining_debt_summary(summary: dict[str, Any]) -> dict[str, Any]:
    loop_control = summary.get("loop_control", {}) if isinstance(summary.get("loop_control"), dict) else {}
    quality = summary.get("quality", {}) if isinstance(summary.get("quality"), dict) else {}
    source_maps = summary.get("source_maps", {}) if isinstance(summary.get("source_maps"), dict) else {}
    execution_bridge = summary.get("execution_bridge", {}) if isinstance(summary.get("execution_bridge"), dict) else {}
    boundary = summary.get("worktree_boundary", {}) if isinstance(summary.get("worktree_boundary"), dict) else {}
    owner_totals = claim_sensitive_group_totals(summary)
    clearance_queue = owner_clearance_queue(summary)

    unclaimed = {
        "score-floor": int(loop_control.get("unclaimed_score_candidates", 0)),
        "source-map": int(loop_control.get("unclaimed_source_map_candidates", 0)),
        "execution-bridge": int(loop_control.get("unclaimed_execution_bridge_candidates", 0)),
    }
    owner_clearance = {
        "score-floor": int(owner_totals.get("score-floor", 0)),
        "source-map": int(owner_totals.get("source-map", 0)),
        "execution-bridge": int(owner_totals.get("execution-bridge", 0)),
    }
    unclaimed_total = sum(unclaimed.values())
    owner_clearance_total = sum(owner_clearance.values())
    dirty_skipped_count = int(loop_control.get("dirty_skipped_packs", 0))
    dirty_pack_lane_count = int(boundary.get("dirty_pack_count", 0))

    if unclaimed_total:
        status = "unclaimed-candidates"
        reason = "unclaimed content debt remains available after claim and dirty-pack filtering"
    elif owner_clearance_total or dirty_skipped_count or dirty_pack_lane_count:
        status = "owner-clearance-or-dirty"
        reason = "remaining content debt is owner-clearance gated or already dirty; keep root/tooling work separated"
    else:
        status = "monitoring"
        reason = "no visible content debt remains in the current target window"

    debt: dict[str, Any] = {
        "contract": REMAINING_DEBT_CONTRACT,
        "status": status,
        "unclaimed_total": unclaimed_total,
        "owner_clearance_total": owner_clearance_total,
        "owner_clearance_queue_fingerprint": str(clearance_queue.get("fingerprint", "")),
        "dirty_skipped_pack_count": dirty_skipped_count,
        "dirty_pack_lane_count": dirty_pack_lane_count,
        "score_floor": {
            "unclaimed": unclaimed["score-floor"],
            "owner_clearance": owner_clearance["score-floor"],
            "lowest_score": float(quality.get("min", 0.0)),
            "below_target": int(quality.get("below_target", 0)),
        },
        "source_map": {
            "unclaimed": unclaimed["source-map"],
            "owner_clearance": owner_clearance["source-map"],
            "warnings": int(source_maps.get("warnings", 0)),
            "max_unresolved": int(source_maps.get("max_unresolved", 0)),
        },
        "execution_bridge": {
            "unclaimed": unclaimed["execution-bridge"],
            "owner_clearance": owner_clearance["execution-bridge"],
            "wired": int(execution_bridge.get("wired", 0)),
            "total": int(execution_bridge.get("empirical_depth_packs", 0)),
            "missing": int(execution_bridge.get("missing", 0)),
        },
        "reason": reason,
    }
    debt["fingerprint"] = hashlib.sha256(
        json.dumps(debt, ensure_ascii=False, sort_keys=True).encode("utf-8")
    ).hexdigest()[:12]
    return {"remaining_debt": debt}


def remaining_debt_line(summary: dict[str, Any]) -> str:
    debt = summary.get("remaining_debt")
    if not isinstance(debt, dict):
        debt = remaining_debt_summary(summary)["remaining_debt"]
    bridge = debt.get("execution_bridge", {}) if isinstance(debt.get("execution_bridge"), dict) else {}
    source = debt.get("source_map", {}) if isinstance(debt.get("source_map"), dict) else {}
    fingerprint = str(debt.get("fingerprint", ""))
    suffix = f"; sha256 {fingerprint}" if fingerprint else ""
    return (
        f"{debt.get('status', 'unknown')}; "
        f"{int(debt.get('unclaimed_total', 0))} unclaimed / "
        f"{int(debt.get('owner_clearance_total', 0))} owner-clearance; "
        f"{int(debt.get('dirty_pack_lane_count', 0))} dirty pack lanes; "
        f"bridge {int(bridge.get('missing', 0))} missing; "
        f"source max unresolved {int(source.get('max_unresolved', 0))}{suffix}"
    )


def validate_remaining_debt(summary: dict[str, Any]) -> list[str]:
    if "generated_at" not in summary and "remaining_debt" not in summary:
        return []
    expected = remaining_debt_summary(summary)["remaining_debt"]
    debt = summary.get("remaining_debt")
    if not isinstance(debt, dict):
        return ["remaining_debt missing or not an object"]
    errors: list[str] = []
    for key, expected_value in expected.items():
        if debt.get(key) != expected_value:
            errors.append(f"remaining_debt.{key} expected {expected_value!r}, observed {debt.get(key)!r}")
    return errors


PUBLISH_POLICY_CONTRACT = "local-publish-policy-v1"


def publish_policy_summary(summary: dict[str, Any]) -> dict[str, Any]:
    content_policy = summary.get("content_edit_policy")
    if not isinstance(content_policy, dict):
        content_policy = content_edit_policy_summary(summary)["content_edit_policy"]
    clearance_queue = owner_clearance_queue_data(summary)
    units = publish_units_data(summary)
    root_unit = units.get("root_tooling", {}) if isinstance(units.get("root_tooling"), dict) else {}
    pack_unit = units.get("pack_content", {}) if isinstance(units.get("pack_content"), dict) else {}
    root_path_count = int(root_unit.get("path_count", 0))
    pack_count = int(pack_unit.get("pack_count", 0))
    root_status = str(root_unit.get("status", ""))
    pack_status = str(pack_unit.get("status", ""))
    owner_clearance_required = bool(content_policy.get("owner_clearance_required"))
    pack_content_owner_review_required = pack_status == "needs-owner-review" or owner_clearance_required
    if pack_content_owner_review_required:
        status = "local-only-owner-review"
    elif root_path_count:
        status = "local-only-root-tooling"
    else:
        status = "local-only-clean"

    if root_path_count and pack_count:
        reason = (
            "No publish request is active; keep the root/tooling unit local, and keep pack-content "
            "lanes out of any path-scoped staging without owner clearance."
        )
    elif root_path_count:
        reason = "No publish request is active; keep the root/tooling unit local until an explicit publish request."
    elif pack_count:
        reason = "No publish request is active; pack-content lanes require owner review before staging."
    else:
        reason = "No publish request is active and no dirty publish units are visible."

    policy: dict[str, Any] = {
        "contract": PUBLISH_POLICY_CONTRACT,
        "status": status,
        "publish_requested": False,
        "local_only_recommended": True,
        "path_scoped_staging_required": bool(root_path_count or pack_count),
        "allowed_publish_unit": "root_tooling",
        "blocked_publish_unit": "pack_content",
        "root_tooling_status": root_status,
        "root_tooling_path_count": root_path_count,
        "root_tooling_staging_command": str(root_unit.get("staging_command", "")),
        "pack_content_status": pack_status,
        "pack_content_pack_count": pack_count,
        "content_edits_allowed": bool(content_policy.get("content_edits_allowed")),
        "owner_clearance_required": owner_clearance_required,
        "pack_content_owner_review_required": pack_content_owner_review_required,
        "reason": reason,
    }
    policy["fingerprint"] = hashlib.sha256(
        json.dumps(policy, ensure_ascii=False, sort_keys=True).encode("utf-8")
    ).hexdigest()[:12]
    return {"publish_policy": policy}


def publish_policy_line(summary: dict[str, Any]) -> str:
    policy = summary.get("publish_policy")
    if not isinstance(policy, dict):
        policy = publish_policy_summary(summary)["publish_policy"]
    fingerprint = str(policy.get("fingerprint", ""))
    suffix = f"; sha256 {fingerprint}" if fingerprint else ""
    local_mode = "local-only" if policy.get("local_only_recommended") else "publish requested"
    staging = "path-scoped staging required" if policy.get("path_scoped_staging_required") else "no staging needed"
    return (
        f"{policy.get('status', 'unknown')}; {local_mode}; "
        f"root {int(policy.get('root_tooling_path_count', 0))} paths; "
        f"packs {int(policy.get('pack_content_pack_count', 0))} lanes "
        f"{policy.get('pack_content_status', 'unknown')}; {staging}{suffix}"
    )


def validate_publish_policy(summary: dict[str, Any]) -> list[str]:
    if "generated_at" not in summary and "publish_policy" not in summary:
        return []
    expected = publish_policy_summary(summary)["publish_policy"]
    policy = summary.get("publish_policy")
    if not isinstance(policy, dict):
        return ["publish_policy missing or not an object"]
    errors: list[str] = []
    for key, expected_value in expected.items():
        if policy.get(key) != expected_value:
            errors.append(f"publish_policy.{key} expected {expected_value!r}, observed {policy.get(key)!r}")
    return errors


GOAL_PROGRESS_CONTRACT = "monthly-uplift-goal-progress-v3"


def goal_progress_summary(summary: dict[str, Any]) -> dict[str, Any]:
    targets = summary.get("targets", {}) if isinstance(summary.get("targets"), dict) else {}
    quality = summary.get("quality", {}) if isinstance(summary.get("quality"), dict) else {}
    source_maps = summary.get("source_maps", {}) if isinstance(summary.get("source_maps"), dict) else {}
    root_entries = summary.get("root_entries", {}) if isinstance(summary.get("root_entries"), dict) else {}
    execution_bridge = summary.get("execution_bridge", {}) if isinstance(summary.get("execution_bridge"), dict) else {}
    bridge_tail = summary.get("execution_bridge_tail", {}) if isinstance(summary.get("execution_bridge_tail"), dict) else {}
    clone = summary.get("clone_audit")
    worklog = summary.get("worklog", {}) if isinstance(summary.get("worklog"), dict) else {}
    loop_control = summary.get("loop_control", {}) if isinstance(summary.get("loop_control"), dict) else {}
    command_plan = summary.get("command_plan", {}) if isinstance(summary.get("command_plan"), dict) else {}
    next_batch_plan = summary.get("next_batch_plan", {}) if isinstance(summary.get("next_batch_plan"), dict) else {}
    content_policy = summary.get("content_edit_policy", {}) if isinstance(summary.get("content_edit_policy"), dict) else {}
    safe_queue = summary.get("safe_content_queue", {}) if isinstance(summary.get("safe_content_queue"), dict) else {}
    skillopt_plan = summary.get("skillopt_gate_plan")
    if not isinstance(skillopt_plan, dict):
        skillopt_plan = skillopt_gate_plan_summary(summary)["skillopt_gate_plan"]
    clearance_queue = owner_clearance_queue_data(summary)
    remaining_debt = summary.get("remaining_debt", {}) if isinstance(summary.get("remaining_debt"), dict) else {}
    publish_policy = summary.get("publish_policy", {}) if isinstance(summary.get("publish_policy"), dict) else {}
    boundary = summary.get("worktree_boundary", {}) if isinstance(summary.get("worktree_boundary"), dict) else {}

    score_floor = float(targets.get("score_floor", 90.0))
    quality_min = float(quality.get("min", 0.0))
    score_floor_ok = quality_min >= score_floor and int(quality.get("below_target", 0)) == 0
    source_maps_ok = int(source_maps.get("warnings", 0)) == 0
    root_cards_ok = (
        int(root_entries.get("warnings", 0)) == 0
        and int(root_entries.get("machine_only", 0)) == 0
        and int(root_entries.get("enriched", 0)) == int(root_entries.get("entry_count", root_entries.get("enriched", 0)))
    )
    if isinstance(clone, dict):
        clone_fail_hits = int(clone.get("fail_hits", 0))
        clone_status = "ok" if clone_fail_hits == 0 else "review"
    else:
        clone_fail_hits = 0
        clone_status = "skipped"
    worklog_ok = str(worklog.get("status", "")) == "OK"
    owner_clearance_required = bool(content_policy.get("owner_clearance_required", False))
    execution_bridge_owner_clearance_required = bool(
        bridge_tail.get(
            "owner_clearance_present",
            bridge_tail.get(
                "owner_clearance_required",
                content_policy.get("execution_bridge_owner_clearance_required", False),
            ),
        )
    )
    local_only_recommended = bool(publish_policy.get("local_only_recommended", False))
    core_invariants_ok = score_floor_ok and source_maps_ok and root_cards_ok
    future_candidates_recorded = int(next_batch_plan.get("count", 0)) > 0

    if not worklog_ok:
        status = "worklog-review"
        reason = "worklog gate is not OK; repair loop evidence before continuing"
    elif not core_invariants_ok:
        status = "metric-review"
        reason = "one or more core monthly uplift invariants needs review"
    elif clone_status == "review":
        status = "clone-review"
        reason = "clone audit reported fail-threshold hits"
    elif clone_status == "skipped":
        status = "active-partial-clone-skipped"
        reason = "core invariants hold in this snapshot; clone audit was skipped and remains required in full gates"
    elif owner_clearance_required:
        status = "active-owner-clearance-needed"
        reason = "core invariants hold; content work remains owner-clearance gated"
    else:
        status = "active-progressing"
        reason = "core invariants hold and the loop has validated progress evidence"

    progress: dict[str, Any] = {
        "contract": GOAL_PROGRESS_CONTRACT,
        "status": status,
        "worklog_status": str(worklog.get("status", "")),
        "worklog_loop_count": int(worklog.get("loop_count", 0)),
        "worklog_latest_heading": str(worklog.get("latest_heading", "")),
        "score_floor_ok": score_floor_ok,
        "score_floor_target": score_floor,
        "quality_min": quality_min,
        "source_maps_ok": source_maps_ok,
        "source_map_warnings": int(source_maps.get("warnings", 0)),
        "root_cards_ok": root_cards_ok,
        "root_entry_enriched": int(root_entries.get("enriched", 0)),
        "root_entry_machine_only": int(root_entries.get("machine_only", 0)),
        "root_entry_warnings": int(root_entries.get("warnings", 0)),
        "clone_audit_status": clone_status,
        "clone_fail_hits": clone_fail_hits,
        "execution_bridge_wired": int(execution_bridge.get("wired", 0)),
        "execution_bridge_total": int(execution_bridge.get("empirical_depth_packs", 0)),
        "execution_bridge_missing": int(execution_bridge.get("missing", 0)),
        "execution_bridge_tail_status": str(bridge_tail.get("status", "")),
        "execution_bridge_tail_policy": str(bridge_tail.get("claim_sensitive_policy", "")),
        "execution_bridge_wiring_allowed_now": bool(bridge_tail.get("wiring_allowed_now", False)),
        "execution_bridge_clearance_required_before_wiring": bool(
            bridge_tail.get("owner_clearance_required_before_wiring", False)
        ),
        "execution_bridge_tail_fingerprint": str(bridge_tail.get("fingerprint", "")),
        "command_plan_measurement_count": int(command_plan.get("measurement_count", 0)),
        "command_plan_validation_count": int(command_plan.get("validation_count", 0)),
        "next_batch_count": int(next_batch_plan.get("count", 0)),
        "safe_content_queue_status": str(safe_queue.get("status", "")),
        "safe_content_queue_fingerprint": str(safe_queue.get("fingerprint", "")),
        "safe_content_queue_unclaimed_total": int(safe_queue.get("unclaimed_total", 0)),
        "skillopt_gate_plan_status": str(skillopt_plan.get("status", "")),
        "skillopt_gate_plan_fingerprint": str(skillopt_plan.get("fingerprint", "")),
        "skillopt_gate_dirty_skill_path_count": int(skillopt_plan.get("dirty_skill_path_count", 0)),
        "skillopt_gate_dirty_pack_lane_count": int(skillopt_plan.get("dirty_pack_lane_count", 0)),
        "skillopt_gate_required_before_new_skill_edits": bool(
            skillopt_plan.get("required_before_new_skill_edits", False)
        ),
        "skillopt_gate_applicable_now": bool(skillopt_plan.get("applicable_now", False)),
        "future_candidates_recorded": future_candidates_recorded,
        "loop_next_lane": str(loop_control.get("next_lane", "")),
        "content_edits_allowed": bool(content_policy.get("content_edits_allowed", False)),
        "owner_clearance_required": owner_clearance_required,
        "execution_bridge_owner_clearance_required": execution_bridge_owner_clearance_required,
        "local_only_recommended": local_only_recommended,
        "dirty_pack_lane_count": int(boundary.get("dirty_pack_count", 0)),
        "reason": reason,
    }
    progress["fingerprint"] = hashlib.sha256(
        json.dumps(progress, ensure_ascii=False, sort_keys=True).encode("utf-8")
    ).hexdigest()[:12]
    return {"goal_progress": progress}


def goal_progress_line(summary: dict[str, Any]) -> str:
    progress = summary.get("goal_progress")
    if not isinstance(progress, dict):
        progress = goal_progress_summary(summary)["goal_progress"]
    fingerprint = str(progress.get("fingerprint", ""))
    suffix = f"; sha256 {fingerprint}" if fingerprint else ""
    core = "core OK" if progress.get("score_floor_ok") and progress.get("source_maps_ok") and progress.get("root_cards_ok") else "core review"
    return (
        f"{progress.get('status', 'unknown')}; {core}; "
        f"worklog {int(progress.get('worklog_loop_count', 0))} loops; "
        f"clone {progress.get('clone_audit_status', 'unknown')}; "
        f"bridge {int(progress.get('execution_bridge_wired', 0))}/"
        f"{int(progress.get('execution_bridge_total', 0))}; "
        f"next {progress.get('loop_next_lane', 'unknown')}{suffix}"
    )


def validate_goal_progress(summary: dict[str, Any]) -> list[str]:
    if "generated_at" not in summary and "goal_progress" not in summary:
        return []
    expected = goal_progress_summary(summary)["goal_progress"]
    progress = summary.get("goal_progress")
    if not isinstance(progress, dict):
        return ["goal_progress missing or not an object"]
    errors: list[str] = []
    for key, expected_value in expected.items():
        if progress.get(key) != expected_value:
            errors.append(f"goal_progress.{key} expected {expected_value!r}, observed {progress.get(key)!r}")
    return errors


COMPLETION_AUDIT_CONTRACT = "monthly-uplift-completion-audit-v6"


def completion_audit_remaining_debt_row(summary: dict[str, Any]) -> tuple[str, str, dict[str, Any]]:
    debt = remaining_debt_summary(summary)["remaining_debt"]
    unclaimed_total = int(debt.get("unclaimed_total", 0))
    owner_clearance_total = int(debt.get("owner_clearance_total", 0))
    dirty_pack_lane_count = int(debt.get("dirty_pack_lane_count", 0))
    fingerprint = str(debt.get("fingerprint", ""))
    if unclaimed_total:
        status = "Review"
    elif owner_clearance_total or dirty_pack_lane_count:
        status = "Triaged"
    else:
        status = "OK"
    evidence = (
        f"{unclaimed_total} unclaimed; {owner_clearance_total} owner-clearance; "
        f"{dirty_pack_lane_count} dirty pack lanes"
    )
    if fingerprint:
        evidence = f"{evidence}; debt sha256 {fingerprint}"
    return status, evidence, debt


def completion_audit_owner_clearance_row(summary: dict[str, Any]) -> tuple[str, str, dict[str, Any]]:
    queue = owner_clearance_queue_data(summary)
    total = int(queue.get("total", 0))
    fingerprint = str(queue.get("fingerprint", ""))
    status = "Triaged" if total else "OK"
    evidence = f"{total} owner-clearance targets"
    target_fingerprints = owner_clearance_target_fingerprint_line(summary)
    if target_fingerprints:
        evidence = f"{evidence}; targets {target_fingerprints}"
    elif fingerprint:
        evidence = f"{evidence}; queue sha256 {fingerprint}"
    return status, evidence, queue


def bridge_gap_phrase(count: int) -> str:
    return f"{count} bridge gap" + ("" if count == 1 else "s")


def completion_audit_requirement_rows(
    summary: dict[str, Any], progress: dict[str, Any] | None = None
) -> list[tuple[str, str, str]]:
    if progress is None:
        progress = summary.get("goal_progress") if isinstance(summary.get("goal_progress"), dict) else None
    if not isinstance(progress, dict):
        progress = goal_progress_summary(summary)["goal_progress"]

    worklog = summary.get("worklog", {}) if isinstance(summary.get("worklog"), dict) else {}
    loop_control = summary.get("loop_control", {}) if isinstance(summary.get("loop_control"), dict) else {}
    clone = summary.get("clone_audit")
    commands = summary.get("command_plan", {}) if isinstance(summary.get("command_plan"), dict) else {}
    targets = summary.get("targets", {}) if isinstance(summary.get("targets"), dict) else {}
    target = float(progress.get("score_floor_target", targets.get("score_floor", 90.0)))
    clone_status = str(progress.get("clone_audit_status", "unknown"))
    clone_audit_status = "OK" if clone_status == "ok" else "Needs full gate"
    clone_evidence = "clone audit skipped"
    if isinstance(clone, dict):
        clone_evidence = (
            f"{int(clone.get('fail_hits', 0))} hits >= "
            f"{float(targets.get('clone_fail_threshold', 0.90)):g}; "
            f"{int(clone.get('reported_pairs', 0))} reported pairs"
        )
    bridge_missing = int(progress.get("execution_bridge_missing", 0))
    bridge_owner_clearance_required = bool(progress.get("execution_bridge_owner_clearance_required", False))
    bridge_tail = summary.get("execution_bridge_tail", {}) if isinstance(summary.get("execution_bridge_tail"), dict) else {}
    bridge_owner_clearance_count = int(bridge_tail.get("owner_clearance_count", 0))
    bridge_unclaimed_count = int(bridge_tail.get("unclaimed_count", 0))
    debt_status = "Triaged" if bool(progress.get("owner_clearance_required")) or bridge_owner_clearance_required else "OK"
    if bridge_owner_clearance_count:
        if bridge_unclaimed_count:
            debt_evidence = (
                f"{bridge_gap_phrase(bridge_owner_clearance_count)} "
                f"{'is' if bridge_owner_clearance_count == 1 else 'are'} owner-clearance gated; "
                f"{bridge_gap_phrase(bridge_unclaimed_count)} "
                f"{'remains' if bridge_unclaimed_count == 1 else 'remain'} actionable"
            )
        else:
            debt_evidence = (
                f"{bridge_gap_phrase(bridge_owner_clearance_count)} "
                f"{'is' if bridge_owner_clearance_count == 1 else 'are'} owner-clearance gated"
            )
    elif bridge_missing and bool(progress.get("owner_clearance_required")):
        debt_evidence = f"{bridge_missing} bridge gaps remain owner-clearance gated"
    else:
        debt_evidence = f"{bridge_missing} bridge gaps visible"
    bridge_policy = str(
        bridge_tail.get("claim_sensitive_policy", progress.get("execution_bridge_tail_policy", ""))
    )
    clearance_before_wiring = bool(
        bridge_tail.get(
            "owner_clearance_required_before_wiring",
            progress.get("execution_bridge_clearance_required_before_wiring", False),
        )
    )
    if bridge_policy:
        debt_evidence = f"{debt_evidence}; policy {bridge_policy}"
    if clearance_before_wiring:
        debt_evidence = f"{debt_evidence}; clearance required before wiring"
    expected_measurement_count = len(NEXT_LOOP_MEASUREMENT_COMMANDS)
    expected_validation_count = len(NEXT_LOOP_VALIDATION_COMMANDS)
    debt_register_status, debt_register_evidence, _ = completion_audit_remaining_debt_row(summary)
    queue_status, queue_evidence, _ = completion_audit_owner_clearance_row(summary)
    skillopt_dirty_paths = int(progress.get("skillopt_gate_dirty_skill_path_count", 0))
    skillopt_dirty_pack_lanes = int(progress.get("skillopt_gate_dirty_pack_lane_count", 0))
    skillopt_status = str(progress.get("skillopt_gate_plan_status", "unknown"))
    skillopt_fingerprint = str(progress.get("skillopt_gate_plan_fingerprint", ""))
    skillopt_plan = summary.get("skillopt_gate_plan")
    if not isinstance(skillopt_plan, dict):
        skillopt_plan = skillopt_gate_plan_summary(summary)["skillopt_gate_plan"]
    skillopt_final_gate = str(skillopt_plan.get("final_hard_gate", "unknown"))
    if skillopt_dirty_paths:
        skillopt_gate_status = "Triaged"
        skillopt_evidence = (
            f"{skillopt_dirty_paths} dirty skill paths / {skillopt_dirty_pack_lanes} dirty pack lanes; "
            f"plan {skillopt_status}; preserve existing pack-lane evidence; "
            f"final hard gate {skillopt_final_gate}"
        )
    elif bool(progress.get("skillopt_gate_required_before_new_skill_edits", False)):
        skillopt_gate_status = "OK"
        skillopt_evidence = (
            f"snapshot/gate/final hard gate recorded; plan {skillopt_status}; "
            f"final hard gate {skillopt_final_gate}"
        )
    else:
        skillopt_gate_status = "Review"
        skillopt_evidence = f"plan {skillopt_status}"
    if skillopt_fingerprint:
        skillopt_evidence = f"{skillopt_evidence}; SkillOpt sha256 {skillopt_fingerprint}"

    return [
        (
            "Durable worklog",
            "OK" if str(worklog.get("status", "")) == "OK" else "Review",
            f"{int(worklog.get('loop_count', 0))} loops; latest {worklog.get('latest_heading', '')}",
        ),
        (
            "Live measurement plan",
            "OK" if int(commands.get("measurement_count", 0)) >= expected_measurement_count else "Review",
            f"{int(commands.get('measurement_count', 0))} measurement commands",
        ),
        (
            "Validation plan",
            "OK" if int(commands.get("validation_count", 0)) >= expected_validation_count else "Review",
            f"{int(commands.get('validation_count', 0))} validation commands",
        ),
        ("SkillOpt gate discipline", skillopt_gate_status, skillopt_evidence),
        (
            "Score floor",
            "OK" if progress.get("score_floor_ok") else "Review",
            f"min {float(progress.get('quality_min', 0.0)):.1f}; target {target:g}",
        ),
        (
            "Source-map warnings",
            "OK" if progress.get("source_maps_ok") else "Review",
            f"{int(progress.get('source_map_warnings', 0))} warnings",
        ),
        (
            "Root-card warnings",
            "OK" if progress.get("root_cards_ok") else "Review",
            (
                f"{int(progress.get('root_entry_enriched', 0))} enriched; "
                f"{int(progress.get('root_entry_machine_only', 0))} machine-only; "
                f"{int(progress.get('root_entry_warnings', 0))} warnings"
            ),
        ),
        ("Clone threshold", clone_audit_status, clone_evidence),
        ("Remaining debt register", debt_register_status, debt_register_evidence),
        ("Owner-clearance queue", queue_status, queue_evidence),
        (
            "Execution bridge and debt",
            debt_status,
            f"{int(progress.get('execution_bridge_wired', 0))}/{int(progress.get('execution_bridge_total', 0))} wired; {debt_evidence}",
        ),
        (
            "Future candidates",
            "OK" if progress.get("future_candidates_recorded") else "Review",
            f"{int(progress.get('next_batch_count', 0))} next-batch items",
        ),
        (
            "Ownership and publish boundary",
            "OK" if progress.get("local_only_recommended") else "Review",
            (
                f"next {loop_control.get('next_lane', 'unknown')}; "
                f"{int(progress.get('dirty_pack_lane_count', 0))} dirty pack lanes; local-only"
            ),
        ),
    ]


def completion_audit_blockers(progress: dict[str, Any], bridge_tail: dict[str, Any] | None = None) -> list[str]:
    blockers = ["Month-scale goal remains active; this audit does not mark it complete."]
    if str(progress.get("clone_audit_status", "unknown")) == "skipped":
        blockers.append("Full clone audit is required before a completion claim.")
    if bool(progress.get("owner_clearance_required")):
        blockers.append("Content debt remains owner-clearance gated.")
    bridge_missing = int(progress.get("execution_bridge_missing", 0))
    tail = bridge_tail if isinstance(bridge_tail, dict) else {}
    bridge_owner_clearance_count = int(tail.get("owner_clearance_count", 0))
    bridge_unclaimed_count = int(tail.get("unclaimed_count", 0))
    if bridge_owner_clearance_count:
        if bridge_unclaimed_count:
            blockers.append(
                f"Execution bridge still has {bridge_owner_clearance_count} owner-clearance-gated "
                f"{'gap' if bridge_owner_clearance_count == 1 else 'gaps'} and "
                f"{bridge_unclaimed_count} unclaimed {'gap' if bridge_unclaimed_count == 1 else 'gaps'}."
            )
        else:
            blockers.append(
                f"Execution bridge still has {bridge_owner_clearance_count} owner-clearance-gated "
                f"{'gap' if bridge_owner_clearance_count == 1 else 'gaps'}."
            )
    elif bridge_missing:
        blockers.append(f"Execution bridge still has {bridge_missing} visible gaps.")
    return blockers


def completion_audit_summary(summary: dict[str, Any]) -> dict[str, Any]:
    progress = summary.get("goal_progress")
    if not isinstance(progress, dict):
        progress = goal_progress_summary(summary)["goal_progress"]
    bridge_tail = summary.get("execution_bridge_tail", {}) if isinstance(summary.get("execution_bridge_tail"), dict) else {}
    safe_queue = summary.get("safe_content_queue", {}) if isinstance(summary.get("safe_content_queue"), dict) else {}
    skillopt_plan = summary.get("skillopt_gate_plan")
    if not isinstance(skillopt_plan, dict):
        skillopt_plan = skillopt_gate_plan_summary(summary)["skillopt_gate_plan"]
    _, _, remaining_debt = completion_audit_remaining_debt_row(summary)
    _, _, clearance_queue = completion_audit_owner_clearance_row(summary)
    rows = completion_audit_requirement_rows(summary, progress)
    blockers = completion_audit_blockers(progress, bridge_tail)
    ok_count = sum(1 for _, status, _ in rows if status == "OK")
    triaged_count = sum(1 for _, status, _ in rows if status == "Triaged")
    review_count = len(rows) - ok_count - triaged_count
    audit: dict[str, Any] = {
        "contract": COMPLETION_AUDIT_CONTRACT,
        "completion_status": "not-complete",
        "goal_status_action": "none",
        "reason": str(progress.get("reason", "")),
        "goal_progress_status": str(progress.get("status", "")),
        "goal_progress_fingerprint": str(progress.get("fingerprint", "")),
        "requirement_count": len(rows),
        "ok_count": ok_count,
        "triaged_count": triaged_count,
        "review_count": review_count,
        "blocker_count": len(blockers),
        "clone_gate_required": str(progress.get("clone_audit_status", "unknown")) == "skipped",
        "owner_clearance_required": bool(progress.get("owner_clearance_required", False)),
        "execution_bridge_owner_clearance_required": bool(
            bridge_tail.get(
                "owner_clearance_present",
                progress.get("execution_bridge_owner_clearance_required", False),
            )
        ),
        "execution_bridge_missing": int(progress.get("execution_bridge_missing", 0)),
        "execution_bridge_tail_status": str(bridge_tail.get("status", progress.get("execution_bridge_tail_status", ""))),
        "execution_bridge_tail_fingerprint": str(
            bridge_tail.get("fingerprint", progress.get("execution_bridge_tail_fingerprint", ""))
        ),
        "safe_content_queue_status": str(safe_queue.get("status", progress.get("safe_content_queue_status", ""))),
        "safe_content_queue_fingerprint": str(
            safe_queue.get("fingerprint", progress.get("safe_content_queue_fingerprint", ""))
        ),
        "safe_content_queue_unclaimed_total": int(
            safe_queue.get("unclaimed_total", progress.get("safe_content_queue_unclaimed_total", 0))
        ),
        "skillopt_gate_plan_status": str(skillopt_plan.get("status", progress.get("skillopt_gate_plan_status", ""))),
        "skillopt_gate_plan_fingerprint": str(
            skillopt_plan.get("fingerprint", progress.get("skillopt_gate_plan_fingerprint", ""))
        ),
        "skillopt_gate_dirty_skill_path_count": int(
            skillopt_plan.get("dirty_skill_path_count", progress.get("skillopt_gate_dirty_skill_path_count", 0))
        ),
        "skillopt_gate_dirty_pack_lane_count": int(
            skillopt_plan.get("dirty_pack_lane_count", progress.get("skillopt_gate_dirty_pack_lane_count", 0))
        ),
        "remaining_debt_status": str(remaining_debt.get("status", "")),
        "remaining_debt_fingerprint": str(remaining_debt.get("fingerprint", "")),
        "remaining_debt_unclaimed_total": int(remaining_debt.get("unclaimed_total", 0)),
        "remaining_debt_owner_clearance_total": int(remaining_debt.get("owner_clearance_total", 0)),
        "remaining_debt_dirty_pack_lane_count": int(remaining_debt.get("dirty_pack_lane_count", 0)),
        "owner_clearance_queue_total": int(clearance_queue.get("total", 0)),
        "owner_clearance_queue_fingerprint": str(clearance_queue.get("fingerprint", "")),
        "owner_clearance_score_target_fingerprint": str(
            clearance_queue.get("score-floor", {}).get("target_fingerprint", "")
            if isinstance(clearance_queue.get("score-floor"), dict)
            else ""
        ),
        "owner_clearance_source_target_fingerprint": str(
            clearance_queue.get("source-map", {}).get("target_fingerprint", "")
            if isinstance(clearance_queue.get("source-map"), dict)
            else ""
        ),
        "owner_clearance_bridge_target_fingerprint": str(
            clearance_queue.get("execution-bridge", {}).get("target_fingerprint", "")
            if isinstance(clearance_queue.get("execution-bridge"), dict)
            else ""
        ),
        "requirements": [
            {"requirement": requirement, "status": status, "evidence": evidence}
            for requirement, status, evidence in rows
        ],
        "blockers": blockers,
    }
    audit["fingerprint"] = hashlib.sha256(
        json.dumps(audit, ensure_ascii=False, sort_keys=True).encode("utf-8")
    ).hexdigest()[:12]
    return {"completion_audit": audit}


def completion_audit_line(summary: dict[str, Any]) -> str:
    audit = summary.get("completion_audit")
    if not isinstance(audit, dict):
        audit = completion_audit_summary(summary)["completion_audit"]
    fingerprint = str(audit.get("fingerprint", ""))
    suffix = f"; sha256 {fingerprint}" if fingerprint else ""
    return (
        f"{audit.get('completion_status', 'unknown')}; action {audit.get('goal_status_action', 'unknown')}; "
        f"{int(audit.get('requirement_count', 0))} requirements; "
        f"{int(audit.get('ok_count', 0))} OK / {int(audit.get('triaged_count', 0))} triaged / "
        f"{int(audit.get('review_count', 0))} review; "
        f"{int(audit.get('blocker_count', 0))} blockers{suffix}"
    )


def validate_completion_audit(summary: dict[str, Any]) -> list[str]:
    if "generated_at" not in summary and "completion_audit" not in summary:
        return []
    expected = completion_audit_summary(summary)["completion_audit"]
    audit = summary.get("completion_audit")
    if not isinstance(audit, dict):
        return ["completion_audit missing or not an object"]
    errors: list[str] = []
    for key, expected_value in expected.items():
        if audit.get(key) != expected_value:
            errors.append(f"completion_audit.{key} expected {expected_value!r}, observed {audit.get(key)!r}")
    return errors


HANDOFF_MANIFEST_CONTRACT = "monthly-uplift-handoff-v4"


def handoff_manifest_summary(summary: dict[str, Any]) -> dict[str, Any]:
    schema = summary.get("schema", {}) if isinstance(summary.get("schema"), dict) else {}
    claims = summary.get("claims", {}) if isinstance(summary.get("claims"), dict) else {}
    loop_control = summary.get("loop_control", {}) if isinstance(summary.get("loop_control"), dict) else {}
    worklog = summary.get("worklog", {}) if isinstance(summary.get("worklog"), dict) else {}
    boundary = summary.get("worktree_boundary", {}) if isinstance(summary.get("worktree_boundary"), dict) else {}
    external_links = summary.get("external_links", {}) if isinstance(summary.get("external_links"), dict) else {}
    command_plan = summary.get("command_plan", {}) if isinstance(summary.get("command_plan"), dict) else {}
    next_batch_plan = summary.get("next_batch_plan", {}) if isinstance(summary.get("next_batch_plan"), dict) else {}
    content_policy = summary.get("content_edit_policy", {}) if isinstance(summary.get("content_edit_policy"), dict) else {}
    bridge_tail = summary.get("execution_bridge_tail", {}) if isinstance(summary.get("execution_bridge_tail"), dict) else {}
    safe_queue = summary.get("safe_content_queue", {}) if isinstance(summary.get("safe_content_queue"), dict) else {}
    skillopt_plan = summary.get("skillopt_gate_plan")
    if not isinstance(skillopt_plan, dict):
        skillopt_plan = skillopt_gate_plan_summary(summary)["skillopt_gate_plan"]
    clearance_queue = owner_clearance_queue_data(summary)
    remaining_debt = summary.get("remaining_debt", {}) if isinstance(summary.get("remaining_debt"), dict) else {}
    publish_policy = summary.get("publish_policy", {}) if isinstance(summary.get("publish_policy"), dict) else {}
    goal_progress = summary.get("goal_progress", {}) if isinstance(summary.get("goal_progress"), dict) else {}
    completion_audit = summary.get("completion_audit", {}) if isinstance(summary.get("completion_audit"), dict) else {}
    units = publish_units_data(summary)
    root_unit = units.get("root_tooling", {}) if isinstance(units.get("root_tooling"), dict) else {}
    pack_unit = units.get("pack_content", {}) if isinstance(units.get("pack_content"), dict) else {}

    manifest: dict[str, Any] = {
        "contract": HANDOFF_MANIFEST_CONTRACT,
        "schema_contract": str(schema.get("contract", "")),
        "loop_status": str(loop_control.get("status", "")),
        "next_lane": str(loop_control.get("next_lane", "")),
        "claims_fingerprint": str(claims.get("fingerprint", "")),
        "claims_active_row_count": int(claims.get("active_row_count", 0)),
        "worklog_loop_count": int(worklog.get("loop_count", 0)),
        "worklog_latest_heading": str(worklog.get("latest_heading", "")),
        "worktree_boundary_fingerprint": str(boundary.get("fingerprint", "")),
        "external_link_status": str(external_links.get("status", "")),
        "external_link_actionable_count": int(external_links.get("actionable_count", 0)),
        "external_link_unchecked_count": int(external_links.get("unchecked_count", 0)),
        "external_link_cache_entry_count": int(external_links.get("cache_entry_count", 0)),
        "external_link_current_cache_entry_count": int(external_links.get("current_cache_entry_count", 0)),
        "external_link_orphaned_cache_entry_count": int(external_links.get("orphaned_cache_entry_count", 0)),
        "external_link_fingerprint": str(external_links.get("fingerprint", "")),
        "command_plan_fingerprint": str(command_plan.get("fingerprint", "")),
        "next_batch_plan_contract": str(next_batch_plan.get("contract", "")),
        "next_batch_plan_fingerprint": str(next_batch_plan.get("fingerprint", "")),
        "content_edit_policy_status": str(content_policy.get("status", "")),
        "content_edit_policy_fingerprint": str(content_policy.get("fingerprint", "")),
        "execution_bridge_tail_status": str(bridge_tail.get("status", "")),
        "execution_bridge_tail_policy": str(bridge_tail.get("claim_sensitive_policy", "")),
        "execution_bridge_wiring_allowed_now": bool(bridge_tail.get("wiring_allowed_now", False)),
        "execution_bridge_clearance_required_before_wiring": bool(
            bridge_tail.get("owner_clearance_required_before_wiring", False)
        ),
        "execution_bridge_tail_fingerprint": str(bridge_tail.get("fingerprint", "")),
        "safe_content_queue_status": str(safe_queue.get("status", "")),
        "safe_content_queue_fingerprint": str(safe_queue.get("fingerprint", "")),
        "safe_content_queue_unclaimed_total": int(safe_queue.get("unclaimed_total", 0)),
        "skillopt_gate_plan_status": str(skillopt_plan.get("status", "")),
        "skillopt_gate_plan_fingerprint": str(skillopt_plan.get("fingerprint", "")),
        "skillopt_gate_dirty_skill_path_count": int(skillopt_plan.get("dirty_skill_path_count", 0)),
        "skillopt_gate_dirty_pack_lane_count": int(skillopt_plan.get("dirty_pack_lane_count", 0)),
        "owner_clearance_queue_total": int(clearance_queue.get("total", 0)),
        "owner_clearance_queue_fingerprint": str(clearance_queue.get("fingerprint", "")),
        "owner_clearance_score_target_fingerprint": str(
            clearance_queue.get("score-floor", {}).get("target_fingerprint", "")
            if isinstance(clearance_queue.get("score-floor"), dict)
            else ""
        ),
        "owner_clearance_source_target_fingerprint": str(
            clearance_queue.get("source-map", {}).get("target_fingerprint", "")
            if isinstance(clearance_queue.get("source-map"), dict)
            else ""
        ),
        "owner_clearance_bridge_target_fingerprint": str(
            clearance_queue.get("execution-bridge", {}).get("target_fingerprint", "")
            if isinstance(clearance_queue.get("execution-bridge"), dict)
            else ""
        ),
        "remaining_debt_status": str(remaining_debt.get("status", "")),
        "remaining_debt_fingerprint": str(remaining_debt.get("fingerprint", "")),
        "publish_policy_status": str(publish_policy.get("status", "")),
        "publish_policy_fingerprint": str(publish_policy.get("fingerprint", "")),
        "goal_progress_status": str(goal_progress.get("status", "")),
        "goal_progress_fingerprint": str(goal_progress.get("fingerprint", "")),
        "execution_bridge_owner_clearance_required": bool(
            bridge_tail.get(
                "owner_clearance_present",
                goal_progress.get("execution_bridge_owner_clearance_required", False),
            )
        ),
        "completion_status": str(completion_audit.get("completion_status", "")),
        "completion_audit_contract": str(completion_audit.get("contract", "")),
        "completion_audit_requirement_count": int(completion_audit.get("requirement_count", 0)),
        "completion_audit_ok_count": int(completion_audit.get("ok_count", 0)),
        "completion_audit_triaged_count": int(completion_audit.get("triaged_count", 0)),
        "completion_audit_review_count": int(completion_audit.get("review_count", 0)),
        "completion_audit_blocker_count": int(completion_audit.get("blocker_count", 0)),
        "completion_audit_fingerprint": str(completion_audit.get("fingerprint", "")),
        "publish_requested": bool(publish_policy.get("publish_requested", False)),
        "local_only_recommended": bool(publish_policy.get("local_only_recommended", False)),
        "root_tooling_status": str(root_unit.get("status", "")),
        "root_tooling_path_count": int(root_unit.get("path_count", 0)),
        "root_tooling_staging_command": str(root_unit.get("staging_command", "")),
        "pack_content_status": str(pack_unit.get("status", "")),
        "pack_content_pack_count": int(pack_unit.get("pack_count", 0)),
    }
    manifest["fingerprint"] = hashlib.sha256(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True).encode("utf-8")
    ).hexdigest()[:12]
    return {"handoff_manifest": manifest}


def handoff_manifest_line(summary: dict[str, Any]) -> str:
    manifest = summary.get("handoff_manifest")
    if not isinstance(manifest, dict):
        manifest = handoff_manifest_summary(summary)["handoff_manifest"]
    fingerprint = str(manifest.get("fingerprint", ""))
    suffix = f"; sha256 {fingerprint}" if fingerprint else ""
    return (
        f"{manifest.get('loop_status', 'unknown')} -> {manifest.get('next_lane', 'unknown')}; "
        f"root {int(manifest.get('root_tooling_path_count', 0))} paths; "
        f"packs {int(manifest.get('pack_content_pack_count', 0))} lanes; "
        f"completion {int(manifest.get('completion_audit_requirement_count', 0))} req / "
        f"{int(manifest.get('completion_audit_blocker_count', 0))} blockers{suffix}"
    )


def validate_handoff_manifest(summary: dict[str, Any]) -> list[str]:
    if "generated_at" not in summary and "handoff_manifest" not in summary:
        return []
    expected = handoff_manifest_summary(summary)["handoff_manifest"]
    manifest = summary.get("handoff_manifest")
    if not isinstance(manifest, dict):
        return ["handoff_manifest missing or not an object"]
    errors: list[str] = []
    for key, expected_value in expected.items():
        if manifest.get(key) != expected_value:
            errors.append(f"handoff_manifest.{key} expected {expected_value!r}, observed {manifest.get(key)!r}")
    return errors


def markdown(summary: dict[str, Any]) -> str:
    counts = summary["counts"]
    quality = summary["quality"]
    execution_bridge = summary["execution_bridge"]
    source_maps = summary["source_maps"]
    root_entries = summary["root_entries"]
    clone = summary["clone_audit"]
    claims = summary["claims"]
    loop_control = summary["loop_control"]
    worklog = summary["worklog"]
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
        f"| Execution bridge | {execution_bridge['wired']} / {execution_bridge['empirical_depth_packs']} empirical depth packs wired; {execution_bridge['missing']} missing |",
        f"| Source maps | {source_maps['map_count']} maps, {source_maps['warnings']} warnings, max unresolved {source_maps['max_unresolved']} |",
        f"| Root entries | {root_entries['enriched']} enriched, {root_entries['machine_only']} machine-only, {root_entries['warnings']} warnings |",
        f"| External links | {external_links_line(summary)} |",
        f"| External-link classes | {external_links_breakdown_line(summary)} |",
        f"| External-link cache | {external_links_cache_line(summary)} |",
        f"| Worklog | {worklog['status']}; {worklog['loop_count']} loops; latest `{str(worklog['latest_heading']).replace('|', '/')}` |",
        f"| Claims boundary | {claims_source_line(claims)} |",
    ]
    if clone is None:
        lines.append("| Clone audit | skipped |")
    else:
        lines.append(
            f"| Clone audit | max reported {clone['max_score']:.3f}, fail hits {clone['fail_hits']}, reported pairs {clone['reported_pairs']} |"
        )
    lines.append(f"| Git status | {working_tree_line(git)} |")
    lines.append(f"| Dashboard schema | {schema_line(summary)} |")
    lines.append(f"| Worktree boundary | {worktree_boundary_line(summary)} |")
    lines.append(f"| Execution-bridge tail | {execution_bridge_tail_line(summary)} |")
    lines.append(f"| Execution-bridge packs | {execution_bridge_tail_pack_line(summary, code=True)} |")
    lines.append(f"| Safe content queue | {safe_content_queue_line(summary)} |")
    lines.append(f"| Content-edit policy | {content_edit_policy_line(summary)} |")
    lines.append(f"| Remaining debt | {remaining_debt_line(summary)} |")
    lines.append(f"| Owner-clearance queue | {owner_clearance_queue_line(summary)} |")
    lines.append(f"| Owner-clearance target fingerprints | {owner_clearance_target_fingerprint_line(summary)} |")
    lines.append(f"| Publish policy | {publish_policy_line(summary)} |")
    lines.append(f"| Goal progress | {goal_progress_line(summary)} |")
    lines.append(f"| Completion audit | {completion_audit_line(summary)} |")
    lines.append(f"| Handoff manifest | {handoff_manifest_line(summary)} |")
    lines.append(f"| SkillOpt gate plan | {skillopt_gate_plan_line(summary)} |")
    lines.append(f"| Current next queue | {current_next_queue_line(summary)} |")
    lines.append(f"| Command plan | {command_plan_line(summary)} |")
    lines.append(f"| Next-batch plan | {next_batch_plan_line(summary)} |")

    lines.extend(["", "## Goal-readiness Signals", "", "| Check | Status | Evidence |", "|---|---|---|"])
    for check, status, evidence in readiness_rows(summary):
        lines.append(f"| {check} | {status} | {evidence} |")

    delta = summary.get("delta")
    if isinstance(delta, dict):
        lines.extend(
            [
                "",
                "## Trajectory Delta",
                "",
                f"Compared with: {delta.get('baseline_generated_at', 'unknown')}",
                "",
                "| Metric | Previous | Current | Delta |",
                "|---|---:|---:|---:|",
            ]
        )
        for row in delta_rows(summary):
            precision = int(row.get("precision", 0))
            lines.append(
                "| {label} | {previous} | {current} | {delta} |".format(
                    label=row["label"],
                    previous=format_delta_value(row["previous"], precision),
                    current=format_delta_value(row["current"], precision),
                    delta=format_signed_delta(row["delta"], precision),
                )
            )
        text_rows = delta_text_rows(summary)
        if text_rows:
            lines.extend(["", "| Signal | Previous | Current | Status |", "|---|---|---|---|"])
            for row in text_rows:
                lines.append(
                    "| {label} | {previous} | {current} | {status} |".format(
                        label=str(row["label"]).replace("|", "/"),
                        previous=str(row["previous"]).replace("|", "/"),
                        current=str(row["current"]).replace("|", "/"),
                        status=format_text_delta_status(row),
                    )
                )

    lines.extend(
        [
            "",
            "## Loop-control Signals",
            "",
            "| Signal | Current |",
            "|---|---:|",
            f"| Status | {loop_control['status']} |",
            f"| Recommended next lane | {loop_control['next_lane']} |",
            f"| Unclaimed score candidates | {loop_control['unclaimed_score_candidates']} |",
            f"| Unclaimed source-map candidates | {loop_control['unclaimed_source_map_candidates']} |",
            f"| Unclaimed execution-bridge candidates | {loop_control['unclaimed_execution_bridge_candidates']} |",
            f"| Claim-sensitive score targets | {loop_control['claim_sensitive_score_targets']} |",
            f"| Claim-sensitive source-map targets | {loop_control['claim_sensitive_source_map_targets']} |",
            f"| Claim-sensitive execution-bridge targets | {loop_control['claim_sensitive_execution_bridge_targets']} |",
            f"| Dirty skipped packs | {loop_control['dirty_skipped_packs']} |",
            f"| Reason | {loop_control['reason']} |",
        ]
    )

    clearance_queue = owner_clearance_queue_data(summary)
    if clearance_queue:
        labels = {
            "score-floor": "Score-floor targets",
            "source-map": "Source-map targets",
            "execution-bridge": "Execution-bridge targets",
        }
        lines.extend(
            [
                "",
                "## Owner Clearance Queue",
                "",
                "These grouped targets are not safe edit candidates until the owning lane clears them.",
                "",
                "| Target type | Current queue |",
                "|---|---|",
            ]
        )
        for kind in OWNER_CLEARANCE_KINDS:
            queue_row = clearance_queue.get(kind, {})
            rows = queue_row.get("displayed", [])
            if not rows:
                continue
            rendered = "; ".join(
                f"`{row['pack']}` ({row['reason'].replace('|', '/')})" if row["reason"] else f"`{row['pack']}`"
                for row in rows
            )
            rendered += clearance_remainder_from_row(queue_row)
            lines.append(f"| {labels.get(kind, kind)} | {rendered} |")

    lines.extend(["", "## Lowest Scorecard Packs", "", "| Score | Pack | Weakest skill |", "|---:|---|---|"])
    for row in quality["worst"]:
        weakest = weakest_skill_path(row)
        lines.append(f"| {float(row['score']):.1f} | {row['pack']} | `{weakest}` |")

    lines.extend(["", "## Highest Source-map Unresolved Flags", "", "| Flags | Source map |", "|---:|---|"])
    for row in source_maps["highest_unresolved"]:
        lines.append(f"| {int(row['unresolved_flags'])} | `{row['path']}` |")

    lines.extend(["", "## Execution-Bridge Tail", "", "| Pack | Score | Current bridge links | Claim status |", "|---|---:|---:|---|"])
    if execution_bridge["missing_packs"]:
        for row in execution_bridge["missing_packs"]:
            reason = claim_pack_reason(summary, str(row["pack"]))
            claim_status = reason.replace("|", "/") if reason else "unclaimed"
            lines.append(
                f"| {row['pack']} | {float(row['score']):.1f} | {int(row.get('exec_bridge_skills', 0))} | {claim_status} |"
            )
    else:
        lines.append("| n/a | n/a | n/a | All empirical depth packs are wired. |")

    if claims["sensitive_current_targets"]:
        lines.extend(["", "## Claim-sensitive Current Targets", "", "| Target | Pack | Reason |", "|---|---|---|"])
        for target in claims["sensitive_current_targets"]:
            reason = str(target["reason"]).replace("|", "/")
            lines.append(f"| {target['kind']} | `{target['pack']}` | {reason} |")

    candidate_pool_data = summary.get("candidate_pool", {})
    score_candidates = candidate_pool_data.get("score_unclaimed", [])
    source_candidates = candidate_pool_data.get("source_map_unclaimed", [])
    bridge_candidates = candidate_pool_data.get("execution_bridge_unclaimed", [])
    bridge_clearance = execution_bridge_clearance_rows(summary)
    dirty_skipped = candidate_pool_data.get("dirty_skipped_packs", [])
    if score_candidates or source_candidates or bridge_candidates:
        lines.extend(
            [
                "",
                "## Unclaimed Candidate Pool",
                "",
                "These are selected from the full scorecard, source-map, and execution-bridge outputs, not just the displayed top rows; re-check claims before editing. Packs already dirty in the current worktree are skipped so the next queue does not point back to an in-progress batch.",
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
        if bridge_candidates:
            lines.extend(["", "| Pack | Score | Current bridge links | Weakest skill |", "|---|---:|---:|---|"])
            for row in bridge_candidates:
                lines.append(
                    f"| {row['pack']} | {float(row['score']):.1f} | "
                    f"{int(row['current_bridge_links'])} | `{row['weakest_skill']}` |"
                )
    if dirty_skipped:
        lines.extend(["", "## Dirty In-progress Packs Skipped", "", "| Pack |", "|---|"])
        for row in dirty_skipped:
            lines.append(f"| {row['pack']} |")

    if git["dirty_lines"]:
        lines.extend(["", "## Dirty Boundary Review", ""])
        lines.extend(dirty_boundary_lines(git))
        lines.extend(["", "## Publish Unit Review", ""])
        lines.extend(publish_unit_lines(summary))

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
    for batch in summary_next_batches(summary):
        lines.append(f"- {batch}")
    lines.extend(["", "## Measurement Commands", ""])
    for command in summary_measurement_commands(summary):
        lines.append(f"- `{command}`")

    lines.extend(["", "## Validation Commands", ""])
    for command in summary_validation_commands_with_latest_heading(summary):
        lines.append(f"- `{command}`")
    return "\n".join(lines) + "\n"


def handoff(summary: dict[str, Any]) -> str:
    counts = summary["counts"]
    quality = summary["quality"]
    execution_bridge = summary["execution_bridge"]
    source_maps = summary["source_maps"]
    root_entries = summary["root_entries"]
    clone = summary["clone_audit"]
    claims = summary["claims"]
    loop_control = summary["loop_control"]
    worklog = summary["worklog"]
    git = summary["git"]
    candidate_pool_data = summary.get("candidate_pool", {})
    dirty_skipped = candidate_pool_data.get("dirty_skipped_packs", [])
    score_candidates = candidate_pool_data.get("score_unclaimed", [])
    source_candidates = candidate_pool_data.get("source_map_unclaimed", [])
    bridge_candidates = candidate_pool_data.get("execution_bridge_unclaimed", [])
    bridge_clearance = execution_bridge_clearance_rows(summary)
    target = summary["targets"]["score_floor"]

    clone_line = "skipped"
    if clone is not None:
        clone_line = (
            f"max {clone['max_score']:.3f}, fail hits {clone['fail_hits']}, "
            f"reported pairs {clone['reported_pairs']}"
        )

    lines = [
        "# Monthly Uplift Handoff",
        "",
        f"Generated: {summary['generated_at']}",
        "",
        "## Loop Decision",
        "",
        f"- Status: `{loop_control['status']}`",
        f"- Next lane: `{loop_control['next_lane']}`",
        f"- Reason: {loop_control['reason']}",
        "",
        "## Current Metrics",
        "",
        f"- Inventory: {counts['skills']} skills / {counts['packs']} packs / {counts['root_entries']} root entries",
        f"- Quality: mean {quality['mean']}, min {quality['min']}, below {target:g}: {quality['below_target']}",
        f"- Execution bridge: {execution_bridge['wired']} / {execution_bridge['empirical_depth_packs']} wired; {execution_bridge['missing']} missing",
        f"- Source maps: {source_maps['map_count']} maps, {source_maps['warnings']} warnings, max unresolved {source_maps['max_unresolved']}",
        f"- Root entries: {root_entries['enriched']} enriched, {root_entries['machine_only']} machine-only, {root_entries['warnings']} warnings",
        f"- External links: {external_links_line(summary)}",
        f"- External-link classes: {external_links_breakdown_line(summary)}",
        f"- External-link cache: {external_links_cache_line(summary)}",
        f"- Worklog: {worklog['status']}; {worklog['loop_count']} loops; latest {worklog['latest_heading']}",
        f"- Claims boundary: {claims_source_line(claims)}",
        f"- Clone audit: {clone_line}",
        f"- Working tree: {working_tree_line(git)}",
        f"- Dashboard schema: {schema_line(summary)}",
        f"- Worktree boundary: {worktree_boundary_line(summary)}",
        f"- Execution-bridge tail: {execution_bridge_tail_line(summary)}",
        f"- Execution-bridge packs: {execution_bridge_tail_pack_line(summary)}",
        f"- Safe content queue: {safe_content_queue_line(summary)}",
        f"- Content-edit policy: {content_edit_policy_line(summary)}",
        f"- Remaining debt: {remaining_debt_line(summary)}",
        f"- Owner-clearance queue: {owner_clearance_queue_line(summary)}",
        f"- Owner-clearance target fingerprints: {owner_clearance_target_fingerprint_line(summary)}",
        f"- Publish policy: {publish_policy_line(summary)}",
        f"- Goal progress: {goal_progress_line(summary)}",
        f"- Completion audit: {completion_audit_line(summary)}",
        f"- Handoff manifest: {handoff_manifest_line(summary)}",
        f"- SkillOpt gate plan: {skillopt_gate_plan_line(summary)}",
        f"- Current next queue: {current_next_queue_line(summary)}",
        f"- Command plan: {command_plan_line(summary)}",
        f"- Next-batch plan: {next_batch_plan_line(summary)}",
    ]

    delta = summary.get("delta")
    if isinstance(delta, dict):
        lines.extend(
            [
                "",
                "## Trajectory Delta",
                "",
                f"- Compared with: {delta.get('baseline_generated_at', 'unknown')}",
                f"- Previous status: `{delta.get('previous_loop_status', 'unknown')}`",
                f"- Current status: `{delta.get('current_loop_status', 'unknown')}`",
            ]
        )
        for row in delta_rows(summary):
            precision = int(row.get("precision", 0))
            lines.append(
                "- {label}: {previous} -> {current} ({delta})".format(
                    label=row["label"],
                    previous=format_delta_value(row["previous"], precision),
                    current=format_delta_value(row["current"], precision),
                    delta=format_signed_delta(row["delta"], precision),
                )
            )
        for row in delta_text_rows(summary):
            lines.append(
                "- {label}: {previous} -> {current} ({status})".format(
                    label=row["label"],
                    previous=row["previous"],
                    current=row["current"],
                    status=format_text_delta_status(row),
                )
            )

    lines.extend(
        [
            "",
            "## Candidate Gate",
            "",
            f"- Unclaimed score candidates: {loop_control['unclaimed_score_candidates']}",
            f"- Unclaimed source-map candidates: {loop_control['unclaimed_source_map_candidates']}",
            f"- Unclaimed execution-bridge candidates: {loop_control['unclaimed_execution_bridge_candidates']}",
            f"- Claim-sensitive score targets: {loop_control['claim_sensitive_score_targets']}",
            f"- Claim-sensitive source-map targets: {loop_control['claim_sensitive_source_map_targets']}",
            f"- Claim-sensitive execution-bridge targets: {loop_control['claim_sensitive_execution_bridge_targets']}",
            f"- Dirty skipped packs: {loop_control['dirty_skipped_packs']}",
        ]
    )
    if git.get("dirty_lines"):
        lines.extend(["", "## Dirty Boundary", ""])
        lines.extend(dirty_boundary_lines(git))
        lines.extend(["", "## Publish Units", ""])
        lines.extend(publish_unit_lines(summary))

    clearance_queue = owner_clearance_queue_data(summary)
    if clearance_queue:
        labels = {
            "score-floor": "Score-floor targets",
            "source-map": "Source-map targets",
            "execution-bridge": "Execution-bridge targets",
        }
        lines.extend(
            [
                "",
                "## Owner Clearance Queue",
                "",
                "These are not safe edit candidates until the owning lane clears them.",
            ]
        )
        for kind in OWNER_CLEARANCE_KINDS:
            queue_row = clearance_queue.get(kind, {})
            rows = queue_row.get("displayed", [])
            if not rows:
                continue
            rendered = "; ".join(
                f"{row['pack']} ({row['reason']})" if row["reason"] else row["pack"]
                for row in rows
            )
            rendered += clearance_remainder_from_row(queue_row)
            lines.append(f"- {labels.get(kind, kind)}: {rendered}")

    lines.extend(["", "## Next Queue", ""])
    if score_candidates:
        lines.append("- Score candidates: " + pack_list(score_candidates, limit=5))
    else:
        lines.append("- Score candidates: none after claim and dirty-pack filtering")
    if source_candidates:
        lines.append("- Source-map candidates: " + source_map_list(source_candidates, limit=5))
    else:
        lines.append("- Source-map candidates: none after claim and dirty-pack filtering")
    if bridge_candidates:
        lines.append("- Execution-bridge candidates: " + pack_list(bridge_candidates, limit=5))
    elif bridge_clearance:
        lines.append(
            "- Execution-bridge candidates: none unclaimed; owner clearance required for "
            + pack_reason_list_with_remainder(bridge_clearance, limit=5)
        )
    else:
        lines.append("- Execution-bridge candidates: none unclaimed in the current target window")
    if dirty_skipped:
        lines.append("- Dirty skipped packs: " + pack_list_with_remainder(dirty_skipped, limit=8))
    lines.append("- Before content edits, re-read `.maintenance/CLAIMS.md` and use path-scoped staging.")

    lines.extend(["", "## Measurement Commands", ""])
    for command in summary_measurement_commands(summary):
        lines.append(f"- `{command}`")

    lines.extend(["", "## Validation Commands", ""])
    for command in summary_validation_commands_with_latest_heading(summary):
        lines.append(f"- `{command}`")
    return "\n".join(lines) + "\n"


def publish_plan(summary: dict[str, Any]) -> str:
    policy = summary.get("publish_policy")
    if not isinstance(policy, dict):
        policy = publish_policy_summary(summary)["publish_policy"]
    units = publish_units_data(summary)
    root_unit = units.get("root_tooling", {}) if isinstance(units.get("root_tooling"), dict) else {}
    pack_unit = units.get("pack_content", {}) if isinstance(units.get("pack_content"), dict) else {}
    root_paths = [str(path) for path in root_unit.get("paths", [])]
    pack_names = [str(name) for name in pack_unit.get("packs", [])]
    command = str(root_unit.get("staging_command", ""))

    lines = [
        "# Local Publish Plan",
        "",
        f"Generated: {summary['generated_at']}",
        "",
        "## Policy",
        "",
        f"- Status: `{policy.get('status', 'unknown')}`",
        f"- Publish requested: `{str(policy.get('publish_requested', False)).lower()}`",
        f"- Local-only recommended: `{str(policy.get('local_only_recommended', True)).lower()}`",
        f"- Allowed unit: `{policy.get('allowed_publish_unit', 'root_tooling')}`",
        f"- Blocked unit: `{policy.get('blocked_publish_unit', 'pack_content')}`",
        f"- Reason: {policy.get('reason', '')}",
        f"- Publish policy: {publish_policy_line(summary)}",
        f"- Worktree boundary: {worktree_boundary_line(summary)}",
        "",
        "## Allowed Root/Tooling Unit",
        "",
        (
            f"- Root/tooling: {root_unit.get('status', 'unknown')}; "
            f"{int(root_unit.get('path_count', len(root_paths)))} paths"
        ),
        "- Staging command: " + (f"`{command}`" if command else "none"),
    ]
    if root_paths:
        lines.append("- Paths:")
        lines.extend(f"  - `{path}`" for path in root_paths)
    else:
        lines.append("- Paths: none")

    lines.extend(
        [
            "",
            "## Blocked Pack Content Unit",
            "",
            (
                f"- Pack content: {pack_unit.get('status', 'unknown')}; "
                f"{int(pack_unit.get('pack_count', len(pack_names)))} pack lanes"
            ),
            f"- Owner-clearance queue: {owner_clearance_queue_line(summary)}",
            f"- Owner-clearance target fingerprints: {owner_clearance_target_fingerprint_line(summary)}",
        ]
    )
    if pack_names:
        lines.append("- Packs:")
        lines.extend(f"  - `{pack}`" for pack in pack_names)
    else:
        lines.append("- Packs: none")

    lines.extend(
        [
            "",
            "## Required Pre-Publish Checks",
            "",
            "- Re-read `.maintenance/CLAIMS.md`.",
            "- Re-run the dashboard and worklog gates.",
        ]
    )
    for command_text in summary_validation_commands_with_latest_heading(summary):
        lines.append(f"- `{command_text}`")
    lines.extend(
        [
            "",
            "No git commands are executed by this plan.",
        ]
    )
    return "\n".join(lines) + "\n"


def debt_audit(summary: dict[str, Any]) -> str:
    debt = summary.get("remaining_debt")
    if not isinstance(debt, dict):
        debt = remaining_debt_summary(summary)["remaining_debt"]
    loop_control = summary.get("loop_control", {}) if isinstance(summary.get("loop_control"), dict) else {}
    content_policy = summary.get("content_edit_policy")
    if not isinstance(content_policy, dict):
        content_policy = content_edit_policy_summary(summary)["content_edit_policy"]
    clearance_queue = owner_clearance_queue_data(summary)
    score = debt.get("score_floor", {}) if isinstance(debt.get("score_floor"), dict) else {}
    source = debt.get("source_map", {}) if isinstance(debt.get("source_map"), dict) else {}
    bridge = debt.get("execution_bridge", {}) if isinstance(debt.get("execution_bridge"), dict) else {}

    rows = [
        (
            "Score floor",
            int(score.get("unclaimed", 0)),
            int(score.get("owner_clearance", 0)),
            f"lowest {float(score.get('lowest_score', 0.0)):.1f}; below target {int(score.get('below_target', 0))}",
        ),
        (
            "Source-map",
            int(source.get("unclaimed", 0)),
            int(source.get("owner_clearance", 0)),
            f"warnings {int(source.get('warnings', 0))}; max unresolved {int(source.get('max_unresolved', 0))}",
        ),
        (
            "Execution bridge",
            int(bridge.get("unclaimed", 0)),
            int(bridge.get("owner_clearance", 0)),
            f"{int(bridge.get('wired', 0))}/{int(bridge.get('total', 0))} wired; {int(bridge.get('missing', 0))} missing",
        ),
    ]

    lines = [
        "# Remaining Debt Audit",
        "",
        f"Generated: {summary['generated_at']}",
        "",
        "## Decision",
        "",
        f"- Status: `{debt.get('status', 'unknown')}`",
        f"- Loop-control status: `{loop_control.get('status', 'unknown')}`",
        f"- Execution-bridge tail: {execution_bridge_tail_line(summary)}",
        f"- Execution-bridge packs: {execution_bridge_tail_pack_line(summary)}",
        f"- Safe content queue: {safe_content_queue_line(summary)}",
        f"- Content-edit policy: {content_edit_policy_line(summary)}",
        f"- Remaining debt: {remaining_debt_line(summary)}",
        f"- Owner-clearance queue: {owner_clearance_queue_line(summary)}",
        f"- Owner-clearance target fingerprints: {owner_clearance_target_fingerprint_line(summary)}",
        f"- Reason: {debt.get('reason', '')}",
        "",
        "## Debt Register",
        "",
        "| Lane | Unclaimed | Owner-clearance | Current signal |",
        "|---|---:|---:|---|",
    ]
    for lane, unclaimed, owner_clearance, signal in rows:
        lines.append(f"| {lane} | {unclaimed} | {owner_clearance} | {signal} |")

    lines.extend(
        [
            "",
            "## Ownership Boundary",
            "",
            f"- Dirty skipped packs: {int(debt.get('dirty_skipped_pack_count', 0))}",
            f"- Dirty pack lanes: {int(debt.get('dirty_pack_lane_count', 0))}",
            f"- Worktree boundary: {worktree_boundary_line(summary)}",
            f"- Publish policy: {publish_policy_line(summary)}",
        ]
    )

    clearance_queue = owner_clearance_queue_data(summary)
    if clearance_queue:
        labels = {
            "score-floor": "Score-floor targets",
            "source-map": "Source-map targets",
            "execution-bridge": "Execution-bridge targets",
        }
        lines.extend(["", "## Owner Clearance Queue", ""])
        for kind in OWNER_CLEARANCE_KINDS:
            queue_row = clearance_queue.get(kind, {})
            rows_value = queue_row.get("displayed", [])
            if not rows_value:
                continue
            rendered = "; ".join(
                f"{row['pack']} ({row['reason']})" if row["reason"] else row["pack"]
                for row in rows_value
            )
            rendered += clearance_remainder_from_row(queue_row)
            lines.append(f"- {labels.get(kind, kind)}: {rendered}")

    lines.extend(
        [
            "",
            "## Validation Commands",
            "",
        ]
    )
    for command_text in summary_validation_commands_with_latest_heading(summary):
        lines.append(f"- `{command_text}`")
    return "\n".join(lines) + "\n"


def goal_audit(summary: dict[str, Any]) -> str:
    progress = summary.get("goal_progress")
    if not isinstance(progress, dict):
        progress = goal_progress_summary(summary)["goal_progress"]
    audit = summary.get("completion_audit")
    if not isinstance(audit, dict):
        audit = completion_audit_summary(summary)["completion_audit"]
    rows = [
        (
            str(row.get("requirement", "")),
            str(row.get("status", "")),
            str(row.get("evidence", "")),
        )
        for row in audit.get("requirements", [])
        if isinstance(row, dict)
    ]
    blockers = [str(blocker) for blocker in audit.get("blockers", [])]

    lines = [
        "# Goal Completion Audit",
        "",
        f"Generated: {summary['generated_at']}",
        "",
        "## Decision",
        "",
        f"- Completion status: `{audit.get('completion_status', 'unknown')}`",
        f"- Goal status action: {audit.get('goal_status_action', 'unknown')}",
        f"- Completion audit: {completion_audit_line(summary)}",
        f"- Execution-bridge tail: {execution_bridge_tail_line(summary)}",
        f"- Execution-bridge packs: {execution_bridge_tail_pack_line(summary)}",
        f"- Safe content queue: {safe_content_queue_line(summary)}",
        f"- Owner-clearance queue: {owner_clearance_queue_line(summary)}",
        f"- Owner-clearance target fingerprints: {owner_clearance_target_fingerprint_line(summary)}",
        f"- Goal progress: {goal_progress_line(summary)}",
        f"- Reason: {audit.get('reason', progress.get('reason', ''))}",
        "",
        "## Requirement Evidence",
        "",
        "| Requirement | Status | Evidence |",
        "|---|---|---|",
    ]
    for requirement, status, evidence in rows:
        lines.append(f"| {requirement} | {status} | {evidence.replace('|', '/')} |")
    lines.extend(["", "## Blockers / Remaining Proof", ""])
    for blocker in blockers:
        lines.append(f"- {blocker}")
    lines.extend(["", "## Validation Commands", ""])
    for command_text in summary_validation_commands_with_latest_heading(summary):
        lines.append(f"- `{command_text}`")
    lines.extend(["", "No goal status is changed by this audit."])
    return "\n".join(lines) + "\n"


def worklog_template_heading(summary: dict[str, Any]) -> str:
    generated_date = str(summary["generated_at"]).split("T", 1)[0]
    return f"### {generated_date} - Monthly Uplift Loop"


def worklog_template(summary: dict[str, Any]) -> str:
    counts = summary["counts"]
    quality = summary["quality"]
    execution_bridge = summary["execution_bridge"]
    source_maps = summary["source_maps"]
    root_entries = summary["root_entries"]
    clone = summary["clone_audit"]
    claims = summary["claims"]
    loop_control = summary["loop_control"]
    git = summary["git"]
    target = summary["targets"]["score_floor"]
    bridge_clearance = execution_bridge_clearance_rows(summary)
    heading = worklog_template_heading(summary)
    clone_line = "skipped"
    if clone is not None:
        clone_line = (
            f"max {clone['max_score']:.3f}, fail hits {clone['fail_hits']}, "
            f"reported pairs {clone['reported_pairs']}"
        )

    lines = [
        heading,
        "",
        "- Scope: [describe root-only/tooling/content lane and ownership boundary].",
        "- Rationale: [describe why this bounded batch is the lowest-risk high-impact next step].",
        "- Files: [list paths changed in this loop].",
        "- Result: [summarize the delivered change and how it improves the month-long goal].",
        "- Live metrics:",
        f"  - Inventory: {counts['skills']} skills / {counts['packs']} packs / {counts['root_entries']} root entries.",
        f"  - Quality: mean {quality['mean']}, min {quality['min']}, below {target:g}: {quality['below_target']}.",
        f"  - Execution bridge: {execution_bridge['wired']} / {execution_bridge['empirical_depth_packs']} wired; {execution_bridge['missing']} missing.",
        f"  - Source maps: {source_maps['map_count']} maps, {source_maps['warnings']} warnings, max unresolved {source_maps['max_unresolved']}.",
        f"  - Root entries: {root_entries['enriched']} enriched, {root_entries['machine_only']} machine-only, {root_entries['warnings']} warnings.",
        f"  - External links: {external_links_line(summary)}.",
        f"  - External-link classes: {external_links_breakdown_line(summary)}.",
        f"  - External-link cache: {external_links_cache_line(summary)}.",
        f"  - Claims boundary: {claims_source_line(claims)}.",
        f"  - Clone audit: {clone_line}.",
        f"  - Working tree: {working_tree_line(git)}.",
        f"  - Dashboard schema: {schema_line(summary)}.",
        f"  - Worktree boundary: {worktree_boundary_line(summary)}.",
        f"  - Execution-bridge tail: {execution_bridge_tail_line(summary)}.",
        f"  - Execution-bridge packs: {execution_bridge_tail_pack_line(summary)}.",
        f"  - Safe content queue: {safe_content_queue_line(summary)}.",
        f"  - Content-edit policy: {content_edit_policy_line(summary)}.",
        f"  - Remaining debt: {remaining_debt_line(summary)}.",
        f"  - Owner-clearance queue: {owner_clearance_queue_line(summary)}.",
        f"  - Owner-clearance target fingerprints: {owner_clearance_target_fingerprint_line(summary)}.",
        f"  - Publish policy: {publish_policy_line(summary)}.",
        f"  - Goal progress: {goal_progress_line(summary)}.",
        f"  - Completion audit: {completion_audit_line(summary)}.",
        f"  - Handoff manifest: {handoff_manifest_line(summary)}.",
        f"  - SkillOpt gate plan: {skillopt_gate_plan_line(summary)}.",
        f"  - Current next queue: {current_next_queue_line(summary)}.",
        f"  - Command plan: {command_plan_line(summary)}.",
        f"  - Next-batch plan: {next_batch_plan_line(summary)}.",
    ]
    if git.get("dirty_lines"):
        lines.extend(f"  {line}" for line in dirty_boundary_lines(git))
        lines.append("  - Publish units:")
        lines.extend(f"    {line}" for line in publish_unit_lines(summary))
    lines.extend(
        [
        "- Loop-control:",
        f"  - Status: `{loop_control['status']}`.",
        f"  - Next lane: `{loop_control['next_lane']}`.",
        f"  - Reason: {loop_control['reason']}.",
        f"  - Unclaimed score/source/bridge candidates: {loop_control['unclaimed_score_candidates']} / {loop_control['unclaimed_source_map_candidates']} / {loop_control['unclaimed_execution_bridge_candidates']}.",
        f"  - Claim-sensitive score/source/bridge targets: {loop_control['claim_sensitive_score_targets']} / {loop_control['claim_sensitive_source_map_targets']} / {loop_control['claim_sensitive_execution_bridge_targets']}.",
        f"  - Dirty skipped packs: {loop_control['dirty_skipped_packs']}.",
        ]
    )
    if bridge_clearance:
        lines.append(
            "  - Execution-bridge owner-clearance tail: "
            f"{pack_reason_list_with_remainder(bridge_clearance, limit=5)}."
        )

    delta = summary.get("delta")
    if isinstance(delta, dict):
        lines.extend(
            [
                "- Trajectory delta:",
                f"  - Compared with: {delta.get('baseline_generated_at', 'unknown')}.",
                f"  - Previous/current status: `{delta.get('previous_loop_status', 'unknown')}` -> `{delta.get('current_loop_status', 'unknown')}`.",
            ]
        )
        for row in delta_rows(summary):
            precision = int(row.get("precision", 0))
            lines.append(
                "  - {label}: {previous} -> {current} ({delta}).".format(
                    label=row["label"],
                    previous=format_delta_value(row["previous"], precision),
                    current=format_delta_value(row["current"], precision),
                    delta=format_signed_delta(row["delta"], precision),
                )
            )
        for row in delta_text_rows(summary):
            lines.append(
                "  - {label}: {previous} -> {current} ({status}).".format(
                    label=row["label"],
                    previous=row["previous"],
                    current=row["current"],
                    status=format_text_delta_status(row),
                )
            )

    clearance_queue = owner_clearance_queue_data(summary)
    if clearance_queue:
        labels = {
            "score-floor": "Score-floor",
            "source-map": "Source-map",
            "execution-bridge": "Execution-bridge",
        }
        lines.append("- Owner clearance queue:")
        for kind in OWNER_CLEARANCE_KINDS:
            queue_row = clearance_queue.get(kind, {})
            rows = queue_row.get("displayed", [])
            if not rows:
                continue
            rendered = "; ".join(
                f"{row['pack']} ({row['reason']})" if row["reason"] else row["pack"]
                for row in rows
            )
            rendered += clearance_remainder_from_row(queue_row)
            lines.append(f"  - {labels.get(kind, kind)}: {rendered}.")

    current_queue = summary.get("current_next_queue")
    if not isinstance(current_queue, dict):
        current_queue = current_next_queue_summary(summary)["current_next_queue"]
    fragments = current_queue.get("required_fragments", [])
    if isinstance(fragments, list) and fragments:
        lines.append("- Current Next Queue fragments:")
        for fragment in fragments:
            lines.append(f"  - {fragment}")

    lines.extend(
        [
            "- Measurement checklist:",
        ]
    )
    for command in summary_measurement_commands(summary):
        lines.append(f"  - [ ] `{command}`")
    lines.extend(
        [
            "- Validation checklist:",
            "  - [ ] `python3 -m py_compile tools/monthly_uplift_report.py tools/run_checks.py`",
            "  - [ ] `python3 tools/monthly_uplift_report.py --self-test`",
            "  - [ ] `python3 tools/monthly_uplift_report.py --check --worklog-template --limit 20 --skip-clone --output /tmp/ajs-monthly-worklog-template.md`",
        ]
    )
    for command in summary_validation_commands(summary):
        lines.append(f"  - [ ] `{command}`")
    lines.append(f"  - [ ] `{strict_latest_heading_command(heading)}`")
    lines.append("- Next queue: [copy the safe next lane from handoff after validation].")
    return "\n".join(lines) + "\n"


def write_output(path: Path, content: str) -> None:
    output_path = path if path.is_absolute() else ROOT / path
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")


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
    render_group = parser.add_mutually_exclusive_group()
    render_group.add_argument("--json", action="store_true", help="emit the aggregate summary as JSON")
    render_group.add_argument(
        "--handoff",
        action="store_true",
        help="emit a compact Markdown handoff with loop status, next lane, candidates, and validation commands",
    )
    render_group.add_argument(
        "--worklog-template",
        action="store_true",
        help="emit a Markdown worklog entry template populated with live loop metrics and validation commands",
    )
    render_group.add_argument(
        "--publish-plan",
        action="store_true",
        help="emit a read-only local publish plan that separates root/tooling paths from blocked pack-content lanes",
    )
    render_group.add_argument(
        "--goal-audit",
        action="store_true",
        help="emit a read-only completion audit for the active month-long goal without changing goal status",
    )
    render_group.add_argument(
        "--debt-audit",
        action="store_true",
        help="emit a read-only remaining-debt audit that separates unclaimed, owner-clearance, and dirty-pack debt",
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="run dependency-free dashboard logic regression tests and exit",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="validate dashboard self-consistency before emitting the snapshot",
    )
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="validate dashboard self-consistency and print only the check result",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="write the same Markdown or JSON payload to PATH while still printing it to stdout",
    )
    parser.add_argument(
        "--compare-json",
        type=Path,
        help="compare the live summary against a previous JSON snapshot from this tool",
    )
    parser.add_argument(
        "--check-worklog",
        type=Path,
        help="validate that a monthly worklog has a complete latest loop entry and current next queue",
    )
    parser.add_argument(
        "--expect-latest-heading",
        help="when used with --check-worklog, require the newest dated loop heading to match this exact string",
    )
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
    if args.self_test:
        errors = self_test_errors()
        if errors:
            print("monthly_uplift_report self-test failed:", file=sys.stderr)
            for error in errors:
                print(f"- {error}", file=sys.stderr)
            return 1
        print("monthly_uplift_report self-test passed.")
        return 0

    if args.check_worklog:
        try:
            print(
                check_worklog(
                    args.check_worklog,
                    build_summary(worklog_live_summary_args(args)),
                    args.expect_latest_heading,
                ),
                end="",
            )
        except ValueError as exc:
            print(f"monthly_uplift_report worklog-check failed: {exc}", file=sys.stderr)
            return 1
        except (ToolError, json.JSONDecodeError) as exc:
            print(f"monthly_uplift_report worklog-check failed: {exc}", file=sys.stderr)
            if isinstance(exc, ToolError):
                if exc.stdout:
                    print(exc.stdout, file=sys.stderr)
                if exc.stderr:
                    print(exc.stderr, file=sys.stderr)
            return 1
        return 0

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

    if args.check or args.check_only:
        errors = validate_summary(summary)
        if errors:
            print("monthly_uplift_report self-check failed:", file=sys.stderr)
            for error in errors:
                print(f"- {error}", file=sys.stderr)
            return 1

    if args.check_only:
        rendered = "monthly_uplift_report self-check passed.\n"
        if args.output:
            write_output(args.output, rendered)
        print(rendered, end="")
        return 0

    if args.json:
        rendered = json.dumps(summary, ensure_ascii=False, indent=2) + "\n"
    elif args.handoff:
        rendered = handoff(summary)
    elif args.worklog_template:
        rendered = worklog_template(summary)
    elif args.publish_plan:
        rendered = publish_plan(summary)
    elif args.goal_audit:
        rendered = goal_audit(summary)
    elif args.debt_audit:
        rendered = debt_audit(summary)
    else:
        rendered = markdown(summary)
    if args.output:
        write_output(args.output, rendered)
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
