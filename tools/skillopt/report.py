#!/usr/bin/env python3
"""Summarize SkillOpt optimization ledgers and enforce the validation gate.

Each ledger (tools/skillopt/ledger/*.json) records the rollout scores, the
add/delete/replace edits proposed for one skill, and the gate decision for each.
This tool reports them and -- with --check -- enforces the one rule SkillOpt does
not bend: an APPLIED edit must have strictly beaten its baseline on the held-out
validation set. A rejected edit must never appear in applied_edits.

Usage:
  python3 tools/skillopt/report.py            # human-readable summary
  python3 tools/skillopt/report.py --json     # machine-readable
  python3 tools/skillopt/report.py --check    # exit 1 if any applied edit failed its gate
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

LEDGER_DIR = Path(__file__).resolve().parent / "ledger"


def load_ledgers() -> list[dict]:
    out = []
    for path in sorted(LEDGER_DIR.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        data["_file"] = path.name
        out.append(data)
    return out


def gate_violations(ledger: dict) -> list[str]:
    """Return integrity problems: an applied edit that did not win its gate."""
    problems = []
    applied = set(ledger.get("applied_edits", []))
    rejected = set(ledger.get("rejected_edit_buffer", []))
    for edit in ledger.get("edits", []):
        eid = edit.get("id", "?")
        status = edit.get("status", "")
        base = edit.get("baseline_score")
        cand = edit.get("candidate_score")
        if status == "APPLIED" or eid in applied:
            if eid in rejected:
                problems.append(f"{eid}: in BOTH applied_edits and rejected_edit_buffer")
            if base is not None and cand is not None and not (cand > base):
                problems.append(
                    f"{eid}: APPLIED but candidate {cand} did not strictly beat baseline {base}"
                )
            if edit.get("gate") not in (None, "ACCEPTED"):
                problems.append(f"{eid}: APPLIED but gate={edit.get('gate')!r} (expected ACCEPTED)")
        if status == "REJECTED" and eid in applied:
            problems.append(f"{eid}: REJECTED yet listed in applied_edits")
    return problems


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--check", action="store_true", help="exit 1 if any applied edit failed its gate")
    args = ap.parse_args()

    ledgers = load_ledgers()

    if args.json:
        print(json.dumps(ledgers, ensure_ascii=False, indent=2))
    else:
        if not ledgers:
            print("No SkillOpt ledgers yet under tools/skillopt/ledger/.")
            return 0
        print(f"SkillOpt ledgers -- {len(ledgers)} skill(s) optimized\n")
        for lg in ledgers:
            if not lg.get("runs") and lg.get("status") == "assessed-no-edit":
                print(f"• {lg['skill']}")
                print(f"    assessed — no high-value gated edit (skill unchanged)")
                note = lg.get("assessment", "")
                if note:
                    print(f"      {note[:160]}{'…' if len(note) > 160 else ''}")
                print()
                continue
            runs = {r["stage"]: r for r in lg.get("runs", [])}
            base = runs.get("baseline", {}).get("judge_total")
            cand = runs.get("candidate", {}).get("judge_total")
            delta = (cand - base) if (base is not None and cand is not None) else None
            n_app = len(lg.get("applied_edits", []))
            n_rej = len(lg.get("rejected_edit_buffer", []))
            static = lg.get("static_scorecard_before")
            print(f"• {lg['skill']}")
            print(
                f"    held-out behavioral score: {base} -> {cand}"
                + (f"  (delta {delta:+d})" if delta is not None else "")
                + (f"   | static scorecard (shape): {static} unchanged" if static is not None else "")
            )
            print(f"    edits: {n_app} accepted by gate, {n_rej} rejected (buffered)")
            for edit in lg.get("edits", []):
                mark = "✓ applied " if edit.get("status") == "APPLIED" else "✗ rejected"
                print(f"      [{mark}] {edit.get('id')}: {edit.get('gate_reason','')}")
            for tr in lg.get("transfers", []):
                print(f"      ↳ transfer → {Path(tr['target']).parent.name}: {tr['inherited_fact'][:70]}")
            print()

    # integrity gate
    all_problems = []
    for lg in ledgers:
        for p in gate_violations(lg):
            all_problems.append(f"{lg['_file']}: {p}")
    if all_problems:
        print("GATE INTEGRITY VIOLATIONS:", file=sys.stderr)
        for p in all_problems:
            print(f"  - {p}", file=sys.stderr)
        if args.check:
            return 1
    elif args.check:
        print("Gate integrity OK: every applied edit strictly beat its baseline.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
