# Weekly Uplift Loop - 2026-06-27

## Goal

Raise Awesome Journal Skills from broad coverage to durable best-in-class
quality by running a count-preserving measurement loop for one week: measure,
choose the highest-leverage unclaimed gap, make a bounded edit, gate it, and
record the next target.

## Starting Baseline

Captured on 2026-06-27 in `/Users/brycewang/Awesome-Journal-Skills`.

- Inventory: 2902 canonical skills, 195 first-party packs, 200 root journal
  entries.
- Working tree: 9 existing dirty entries in `gallery/xiaohongshu-ajs/**`,
  `tools/README.md`, and `tools/render_posters.mjs`; this loop does not own
  those paths.
- Quality scorecard before the first slice: mean 93.3, min 38.1, below 90 = 1.
- Source maps: 194 maps, 0 warnings, max unresolved flags = 14.
- Root cards: 200 enriched, 0 machine-only, 0 warnings.
- Clone audit: 2902 skills across 350 comparison groups, no pairs at or above
  0.750.
- Execution bridge coverage: 131/134 empirical depth packs wired.

## Urgent Gaps

1. **Score-floor break:** `Research-Toolkit-Skills` scored 38.1 because the
   scorecard treated a cross-journal toolkit as a single-venue depth pack and
   penalized it for missing journal cues and pack-local resources.
2. **Source-map debt:** `PNAS-Nexus-Skills/resources/official-source-map.md`
   has 14 unresolved flags; the next unclaimed source-map target after that is
   `World-Development-Skills/resources/official-source-map.md` at 3 flags.
3. **Bridge tail:** empirical execution wiring is almost complete but still
   leaves 3 empirical depth packs without the shared StatsPAI/Stata MCP bridge.
4. **Parallel-lane risk:** `.maintenance/CLAIMS.md` still marks active or
   queued content lanes; root/tooling edits are safer than unowned pack rewrites.

## Weekly Loop

Repeat daily or after each accepted batch:

```bash
python3 tools/audit_repo.py --counts
python3 tools/monthly_uplift_report.py --limit 16
python3 tools/skillopt_gate.py snapshot --out /tmp/ajs-weekly-baseline.json
# bounded edit: one tool, one pack, or one source-map family
python3 tools/skillopt_gate.py gate --baseline /tmp/ajs-weekly-baseline.json
python3 tools/run_checks.py --skip-reports
git diff --check
```

Use the full clone audit before a content batch:

```bash
python3 tools/clone_audit.py --threshold 0.75 --fail-threshold 0.90 --top 30
```

## Anti-Cheat Rules

- Do not change expected counts unless an expansion lane is explicitly opened.
- Do not lower score thresholds or hide weak packs; if a pack is misclassified,
  encode the new type with measurable criteria.
- Do not fabricate volatile journal facts to reduce unresolved flags.
- Do not edit claim-sensitive pack directories without owner clearance.
- Do not stage with `git add -A`; use explicit path staging if publishing later.

## First Slice

- Add an explicit toolkit scoring type for `Research-Toolkit-Skills` so the
  scorecard evaluates compact cross-journal routers against shared-resource
  coverage instead of venue-specific depth-pack cues.
- Add `Research-Toolkit-Skills/resources/README.md` to document why code and
  live source maps stay in shared resources and selected journal packs.

## First-Slice Validation

Completed on 2026-06-27.

- `python3 tools/quality_scorecard.py --top 12 --show-skills`: mean 93.6,
  min 90.0, below 90 = 0; `Research-Toolkit-Skills` now reports as a toolkit
  pack at 91.4 instead of a misclassified depth-pack outlier at 38.1.
- `python3 tools/monthly_uplift_report.py --limit 16`: clone max reported
  0.000, clone fail hits 0, score floor OK, source-map warnings 0, root-card
  warnings 0; only the three owned files from this slice remain dirty.
- `python3 tools/skillopt_gate.py gate --baseline /tmp/ajs-weekly-20260627-baseline.json --skip-clone`:
  PASS; inventory counts fixed at 2902 / 195 / 200 and the embedded hard checks
  passed.
- Embedded hard checks from the gate: `python3 tools/run_checks.py --skip-reports`,
  `python3 tools/audit_repo.py`, `python3 tools/clone_audit.py --threshold 0.75 --fail-threshold 0.90 --top 20`,
  and `git diff --check`.

## Next Candidates

1. Keep the score floor above 90 by sampling the current unclaimed bottom band
   before any expansion work: Research Toolkit, Agriculture/Environment,
   Engineering/Technology, and other breadth packs.
2. Resolve or honestly triage the 14 unresolved flags in PNAS Nexus using only
   reachable official sources.
3. Identify the 3 empirical depth packs missing execution-bridge wiring and add
   lightweight links to `shared-resources/empirical-methods/execution-with-mcp.md`.
4. If content lanes remain claim-sensitive, continue with tooling/reporting
   improvements instead of pack rewrites.
