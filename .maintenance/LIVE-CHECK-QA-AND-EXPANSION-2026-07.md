# Live-Check QA + Expansion Campaign (2026-07, one-month paced)

Follow-on to the 183-pack live-check rollout. Three workstreams the user approved:

## Item 1 — Independent QA audit (highest value, zero-conflict)
Orchestrator-level INDEPENDENT re-verification of a stratified sample of already-committed
packs, to catch any "confident-but-wrong" subagent assertion (the ST-Tavory failure class).
Method: each audit subagent reads the source-map's stated current editor + APC, then
INDEPENDENTLY web-verifies, and compares. MATCH → confirm (no edit). MISMATCH → investigate,
fix the source map if it's wrong/stale, log the correction. Never fabricate.
- Flagship 5 already independently re-verified 2026-06-23 (Econometrica, J Finance, Mgmt Sci,
  APSR, J Marketing) — all 5/5 correct.
- This round: stratified ~32-pack sample across disciplines.

## Item 2 — Extend live-check to packs/entries lacking the source-map layer
- 10 top sci/med `-Skills` packs have NO source map: Cell, Lancet, NEJM, Science, PNAS,
  Physical-Review-Letters, JACS, JAMA, Cancer-Cell, Annals-of-Mathematics.
- 200 root journal-entry cards (AJS-ROOT-JOURNAL-ENTRY) — the root-card enrichment lane.
- **Ownership gate:** several of these are Codex "reserved-area" / actively-edited lanes
  (PNAS-Nexus is uncommitted right now). MUST confirm non-conflict before touching; otherwise
  document + recommend coordination rather than edit.

## Item 3 — Routine cadence for the July transition surge
Tighten coverage around the ~July 1 handovers (PMLA, JHR, Journal of Management) and Sept 1
(JFQA). Preferred mechanism: targeted ONE-TIME runs (auto-expiring) at the transition dates,
rather than a blanket every-2-days bump (precise + no revert needed).

## Progress log

### Item 1 — QA audit (DONE so far: 64 packs / 2 waves)
- Wave 1 (32 packs): 29 verified-correct, 3 fixed — AMJ removed non-existent US$3,500 APC
  (fabrication-class), TAR fee $270/$645→$285/$680 (stale), REStud fee 200/120→250/150 (2026-06-01).
  Commit 7e1f498e.
- Wave 2 (32 packs): 29 verified-correct, 3 fixed — JAMS APC $3,860→£3,090/$4,990/€3,990;
  JET ($3,130) & GEB ($2,860) Elsevier APCs softened to honest hedges (no longer independently
  confirmable). Commit 97bcf790.
- **Pattern: editor assertions ~100% correct; APC/fee figures are the weak spot (5 of 6 fixes).**
- Flagship-5 spot-check (2026-06-23): 5/5 correct.

### Item 2 — ownership findings + revised target
- **Root cards (209 AJS-ROOT-JOURNAL-ENTRY):** thin routing stubs that intentionally contain NO
  SKILL.md and point to a canonical skill inside a bundle; they are the parallel Codex agent's
  "root-card enrichment lane" (actively editing breadth bundles / PNAS-Nexus right now).
  **Verdict: owned by the parallel lane — NOT touched. Recommend coordination.**
- **Revised safe target: 10 flagship sci/med packs lacking a source-map layer** (Cell, Lancet,
  NEJM, Science, PNAS, Physical-Review-Letters, JACS, JAMA, Cancer-Cell, Annals-of-Mathematics).
  No active edits (clean tree). Adding a source map = additive new file, zero conflict. (These were
  prior "reserved-area" scorecard packs — flagged for breadth-lane review.)

### Item 3 — July/Sept transition coverage (DONE)
Instead of a blanket every-2-days bump (would need a manual revert), created two targeted
AUTO-EXPIRING one-time cloud runs:
- trig_01HuhBSQzrhNTEiBJyzTQMyS — 2026-07-02 16:00 UTC — applies the July-1 handovers
  (PMLA→Potkay, JHR→Lovenheim, Journal of Management successor) + checks the still-TBD successors.
- trig_01TwzUqoEP3D6qmx11whJFfV — 2026-09-02 16:00 UTC — applies the Sept-1 JFQA handover
  (Pennacchi→Giannetti) + re-checks remaining TBD successors.
Weekly routine "Journal live-check re-verify (all 183 packs)" (trig_01HQj8Vk…) stays as the
steady-state watch.

## CAMPAIGN COMPLETE (2026-06-23)
- Item 1: 64 packs independently QA-audited across 2 waves → 58 verified-correct, 6 fixed
  (5 of 6 were APC/fee figures incl. one fabricated AMJ APC; editor assertions held up).
- Item 2: root cards confirmed parallel-agent-owned (deferred, recommend coordination);
  10 flagship sci/med packs given a verified source-map layer they previously lacked.
- Item 3: two auto-expiring one-time runs scheduled for the July & Sept handover dates.
- Gates: run_checks green; source_map_audit 194 maps / 0 warnings.
