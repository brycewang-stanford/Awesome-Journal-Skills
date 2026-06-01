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
- **Codex — Chinese depth-pack source-map lane**: add missing
  `resources/official-source-map.md` files for the seven Chinese depth packs listed in
  `.maintenance/CONTENT-VERIFICATION.md`; source-map/resource metadata only, no
  `skills/*/SKILL.md` rewrites and no submodule edits.
- **Codex — AMR consistency lane**: propagate already verified AMR fee / EIC facts into the two
  leftover AMR files noted in `.maintenance/CONTENT-VERIFICATION.md`; no broad AMR rewrite.
- **Codex — CS/AI conference expansion lane**: add a new AI-first computer-science conference
  breadth pack to satisfy the 1000-skill target; no edits to existing journal-content skill bodies
  and no submodule edits.
- **Codex — Category 8 Wave 25-A depth-pack lane**: build complete CS/AI conference depth packs
  from `.maintenance/CATEGORY-8-BUILD-QUEUE.md`, starting with NeurIPS; no submodule edits.

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
| China-Industrial-Economics-Skills | Codex | done | source-map only; no skill rewrites |
| China-Rural-Economy-Skills | Codex | done | source-map only; no skill rewrites |
| Chinese-Public-Administration-Skills | Codex | done | source-map only; no skill rewrites |
| Journal-of-Management-World-Skills | Codex | done | source-map only; no skill rewrites |
| Journal-of-Finance-and-Economics-Skills | Codex | done | source-map only; no skill rewrites |
| Journal-of-Quantitative-and-Technological-Economics-Skills | Codex | done | source-map only; no skill rewrites |
| Accounting-Research-Skills | Codex | done | source-map only; no skill rewrites |
| Academy-of-Management-Review-Skills | Codex | done | fee/EIC consistency only |
| Computer-Science-Conference-Skills | Codex | done | new AI-first conference breadth pack: 155 profiles + router |
| NeurIPS-Skills | Codex | done | first category-8 conference depth pack: 12 official-source-backed skills |
| ICML-Skills | Codex | done | second category-8 conference depth pack: 12 official-source-backed skills |
| ICLR-Skills | Codex | done | third category-8 conference depth pack: 12 official-source-backed skills |

## Lane — 全学科扩张规划 (10×100 = 1000 packs)
- **Owner**: planning agent + Codex support · Status: Wave 0 done; Wave 1 inventory split done
- Files: `.maintenance/EXPANSION-PLAN.md`, `.maintenance/JOURNAL-MASTER-LIST.md`,
  `.maintenance/ASSET-INVENTORY.md`, `.maintenance/ROOT-CARD-CATEGORY-MAP.md`,
  `.maintenance/BREADTH-ENTRY-CATEGORY-MAP.md`, `.maintenance/CATEGORY-8-BUILD-QUEUE.md`
  (planning/inventory docs only)
- 验收节点: ≈2026-06-30 (reminder scheduled)
- Next: continue category 8 Wave 25-A depth-pack production from `.maintenance/CATEGORY-8-BUILD-QUEUE.md`
  with AAAI / IJCAI / AISTATS / UAI; `JOURNAL-MASTER-LIST.md` reserves `[A-depth]` for complete
  reusable depth assets and keeps breadth-only seeds in the map files
- 不触碰任何现有 pack 内容；建包按分波滚动，每波过 `tools/run_checks.py` + clone 审计。

## Lane — Workflow Wave W1 · 大类1 经济学领域刊深度包 (parallel workflow)
- **Owner**: planning agent (Opus, parallel Workflow) · Status: in progress
- Building 6 NEW standalone depth packs (clean gaps, no overlap with Codex CS lane):
  Journal-of-Development-Economics, Journal-of-Public-Economics, Journal-of-Labor-Economics,
  Journal-of-International-Economics, RAND-Journal-of-Economics, Journal-of-Monetary-Economics.
- Each agent ONLY creates files under its own `<Journal>-Skills/` dir; does NOT touch root
  README, root cards, marketplace, or any shared/existing file (those registered later by owner).
- Quality bar: venue-specific, official-source-backed (URL+date) or `待核实`; no find-replace clones.

## Out of scope (git submodules — do NOT edit)
AER-skills, nature-skills, nature-paper-skills, claude-scholar, codex-claude-academic-skills
