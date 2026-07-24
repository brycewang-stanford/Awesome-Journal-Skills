# .maintenance INDEX

Navigation aid for this directory. `.maintenance/` holds the repo's internal
planning, coordination, and audit-history documents — none of it ships in the
installable packs. This index is a **static snapshot (2026-07-24)**, not a
self-updating board: it exists so a new maintainer can tell live docs from
archived logs at a glance. When you retire or add a file, adjust the line here
in the same commit. Nothing here is deleted or moved by adding this index.

Before editing any pack, the two files that actually gate work are
**`CLAIMS.md`** (claim your lane first) and the current-month **`ROADMAP-*`**.

## Active — steers current & next work

| File | What it is |
|------|-----------|
| `ROADMAP-2026-08.md` | Current-month plan (window 2026-07-08 → 08-08): quality-saturation finish, measured expansion, fact-debt paydown, governance de-burden. |
| `ACCEPTANCE-2026-08.md` | Current-month acceptance report (numbers re-verified against the working tree). |
| `QUALITY-LANE-2026-09.md` | Forward quality-traction plan after the static scorecard saturated. Records the deliberate decisions: scorecard is a regression floor, **not** a ranking target; no rebuilding auto-committing eval apparatus. Read before touching `tools/quality_scorecard.py`. |
| `CLAIMS.md` | Active multi-agent claims board. Claim a lane here before editing; commit with targeted `git add <path>`. |
| `RELEASE-NOTES-v1.1.0.md` | Bilingual draft release notes awaiting an owner-run tag. |

## Reference & playbooks — undated, reusable

| File | What it is |
|------|-----------|
| `METHODOLOGY.md` | Depth-pack polishing quality bar. |
| `SUBAGENT-DEPTH-PACK-BRIEF.md` | Build brief for a generic 12-skill journal depth pack. |
| `SUBAGENT-SS-DEPTH-BRIEF.md` | Build brief for a new social-science depth pack. |
| `SUBAGENT-DEEPEN-BRIEF.md` | Brief for rewriting a templated pack up to flagship prose. |
| `JOURNAL-MASTER-LIST.md` | Master journal-selection table (10 discipline categories). |
| `CATEGORY-8-BUILD-QUEUE.md` | CS/AI (category-8) build queue — at terminal quota 100/100; kept as the coverage record. |
| `BREADTH-ENTRY-CATEGORY-MAP.md` | Breadth-bundle entry → discipline-category map. |
| `ROOT-CARD-CATEGORY-MAP.md` | Root journal-card → discipline-category map. |
| `ASSET-INVENTORY.md` | Inventory of pack assets (covers, resources). |
| `EXPANSION-PLAN.md` | All-discipline expansion blueprint (10×100 target). |
| `EXPANSION-PLAN-2026-06-PLUS100.md` | +100-journal expansion plan targeting the thinnest disciplines. |
| `EXEMPLAR-SLOT-TODO.md` | TODO registry for Chinese-journal exemplar method slots. |
| `LIVE-CHECK-URLS.txt` | URL list consumed by the live-check tooling. |
| `live-check.workflow.yml` | Live-check workflow snippet. |

## Historical archive — dated / completed logs

Kept for provenance; not a to-do list. Superseded plans and finished campaigns.

| File | What it is |
|------|-----------|
| `ROADMAP-2026-07.md` | Prior-month roadmap (superseded by 2026-08). |
| `ACCEPTANCE-2026-07.md` | Prior-month acceptance report. |
| `CLAIMS-ARCHIVE-2026-06.md` | Archived claims board (2026-06). |
| `PROGRESS.md` | Agent-A depth-pack polishing log (historical waves). |
| `ROUND2-RESULTS.md` | Round-2 de-clone + cover-module results. |
| `CLONE-TRIAGE-2026-06-20.md` | Dated clone-triage pass. |
| `DECLONE-PLAN.md` | Completed de-clone plan for the Chinese social-science bundle. |
| `COMPARISON-2026-07.md` | Competitive comparison vs peer academic-skills repos. |
| `CONTENT-VERIFICATION.md` | Social-science content-verification lane log. |
| `COVER-REPLACEMENT-TRACKER.md` | Journal-cover replacement tracker. |
| `EXECUTION-BRIDGE-ROLLOUT-2026-06.md` | Execution-bridge (StatsPAI/Stata MCP) rollout log. |
| `FLAGSHIP-DEPTH-UPLIFT-2026-06.md` | Flagship depth-pack uplift log. |
| `LIVE-CHECK-QA-AND-EXPANSION-2026-07.md` | Live-check QA + expansion campaign log. |
| `LIVE-CHECK-ROLLOUT-2026-07.md` | Live-check rollout log (remaining lanes). |
| `LIVE-CHECK-VERIFICATION-2026-06.md` | Live-check verification campaign (humanities & social science). |
| `PHASE5-RESOURCE-LAYER-PLAN.md` | Phase-5 resource-layer buildout plan. |
| `STUB-CARDS-LANE.md` | Stub landing-card enrichment lane (root entries now 200/200 enriched). |
| `AGENT-D-ERJ-RESEARCH.md` | Research staging notes for the Economic-Research depth pack. |
