# Maintenance Claims Board (multi-agent coordination)

> Two agents are polishing journal skill packs in parallel **in this same working tree**.
> Claim a pack here before editing it, and **check `git status` + this file before starting any pack.**
> Edits are left **uncommitted** for the user's final 验收 (review); do not push. If you do commit,
> use targeted `git add <Pack-Dir>` (never `git add -A`) so the other agent's work is preserved.

## Confirmed problem
Many depth packs are find-replace clones of one master template. Verified: QJE's
`qje-causal-identification` is byte-identical to JPE's `jpe-causal-identification` after
name-normalization (both 286 words, empty diff). The econ/finance flagship packs give generic
top-5 advice with no venue-specific facts. (The natural-science packs are more differentiated —
Science does NOT contain Cell Press "STAR Methods"; earlier claim retracted.)

## Lanes (discipline split)
- **Agent B — Natural Science & Medicine**: Cell, Science, PNAS, NEJM, Lancet, JAMA, Cancer-Cell,
  Physical-Review-Letters, Journal-of-the-American-Chemical-Society, Annals-of-Mathematics.
  (Detected active on Cell-Skills via uncommitted plugin.json version bump.)
- **Agent A (me) — Social Science**: English econ/finance/management flagships + Chinese depth packs.
- **Codex — Repository audit lane**: root README counts, marketplace metadata consistency,
  `tools/audit_repo.py`, and CI audit workflow. No journal-content rewrites and no submodule edits.

## Claim log
| Pack | Agent | Status | Notes |
|------|-------|--------|-------|
| Quarterly-Journal-of-Economics-Skills | A | in progress | golden template; deep venue research |
| Journal-of-Political-Economy-Skills | A | queued | |
| Econometrica-Skills | A | queued | |
| Review-of-Economic-Studies-Skills | A | queued | |
| Journal-of-Finance-Skills | A | queued | |
| Journal-of-Financial-Economics-Skills | A | queued | |
| Review-of-Financial-Studies-Skills | A | queued | |

## Out of scope (git submodules — do NOT edit)
AER-skills, nature-skills, nature-paper-skills, claude-scholar, codex-claude-academic-skills
