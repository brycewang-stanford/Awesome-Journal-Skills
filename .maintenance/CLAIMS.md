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
| AAAI-Skills | Codex | done | fourth category-8 conference depth pack: 12 official-source-backed skills |
| IJCAI-Skills | Codex | done | fifth category-8 conference depth pack: 12 official-source-backed skills |
| AISTATS-Skills | Codex | done | sixth category-8 conference depth pack: 12 official-source-backed skills |
| Management-Science-Skills | Codex | done | completed W2 plugin shell into 12 official-source-backed skills |
| Operations-Research-Skills | Codex | done | completed W2 plugin shell into 12 official-source-backed skills |
| Manufacturing-and-Service-Operations-Management-Skills | Codex | done | completed W2 plugin shell into 12 official-source-backed skills |
| Production-and-Operations-Management-Skills | Codex | done | completed partial W2 scaffold into 12 official-source-backed skills |
| Journal-of-Operations-Management-Skills | Codex | done | completed W2 plugin shell into 12 official-source-backed skills |
| Journal-of-Marketing-Skills | Codex | done | completed W2 plugin shell into 12 official-source-backed skills |
| Journal-of-Marketing-Research-Skills | Codex | done | completed W2 plugin shell into 12 official-source-backed skills |
| Marketing-Science-Skills | Codex | done | completed W2 plugin shell into 12 official-source-backed skills |
| Journal-of-Consumer-Research-Skills | Codex | done | completed W2 plugin shell into 12 official-source-backed skills |
| MIS-Quarterly-Skills | Codex | done | completed W2 plugin shell into 12 official-source-backed skills |
| Information-Systems-Research-Skills | Codex | done | completed W2 plugin shell into 12 official-source-backed skills |
| The-Accounting-Review-Skills | Codex | done | completed W2 plugin shell into 12 official-source-backed skills |
| Journal-of-Accounting-Research-Skills | Codex | done | completed W2 plugin shell into 12 official-source-backed skills |
| Journal-of-Accounting-and-Economics-Skills | Codex | done | completed W2 plugin shell into 12 official-source-backed skills |
| Contemporary-Accounting-Research-Skills | Codex | done | completed W2 plugin shell into 12 official-source-backed skills |
| Organization-Science-Skills | Codex | done | completed W2 plugin shell into 12 official-source-backed skills |
| Journal-of-International-Business-Studies-Skills | Codex | done | completed W2 plugin shell into 12 official-source-backed skills |
| Journal-of-Business-Venturing-Skills | Codex | done | completed W2 plugin shell into 12 official-source-backed skills |
| The-Econometrics-Journal-Skills | Codex | done | completed concurrent plugin shell into 12 official-source-backed skills |
| Econometric-Theory-Skills | Codex | done | completed concurrent plugin shell into 12 official-source-backed skills |
| Journal-of-Econometrics-Skills | Codex | done | completed concurrent plugin shell into 12 official-source-backed skills |
| Quantitative-Economics-Skills | Codex | done | completed concurrent plugin shell into 12 official-source-backed skills |
| Review-of-Economic-Dynamics-Skills | Codex | done | completed concurrent plugin shell into 12 official-source-backed skills |
| Review-of-Finance-Skills | Codex | done | completed concurrent plugin shell into 12 official-source-backed skills |
| Journal-of-Applied-Econometrics-Skills | Codex | done | completed concurrent plugin shell into 12 official-source-backed skills |
| Journal-of-Business-and-Economic-Statistics-Skills | Codex | done | completed concurrent plugin shell into 12 official-source-backed skills |
| Journal-of-Financial-Intermediation-Skills | Codex | done | completed concurrent plugin shell into 12 official-source-backed skills |
| Journal-of-Financial-and-Quantitative-Analysis-Skills | Codex | done | completed concurrent plugin shell into 12 official-source-backed skills |
| Journal-of-Corporate-Finance-Skills | Codex | done | completed concurrent plugin shell into 12 official-source-backed skills |
| Journal-of-Banking-and-Finance-Skills | Codex | done | completed concurrent plugin shell into 12 official-source-backed skills |
| Mathematical-Finance-Skills | Codex | done | completed concurrent plugin shell into 12 official-source-backed skills |
| Games-and-Economic-Behavior-Skills | Codex | done | completed concurrent plugin shell into 12 official-source-backed skills |
| Journal-of-Economic-Growth-Skills | Codex | done | completed concurrent plugin shell into 12 official-source-backed skills |
| Journal-of-Economic-Theory-Skills | Codex | done | completed concurrent plugin shell into 12 official-source-backed skills |
| Journal-of-Human-Resources-Skills | Codex | done | completed concurrent plugin shell into 12 official-source-backed skills |

## Lane — 全学科扩张规划 (10×100 = 1000 packs)
- **Owner**: planning agent + Codex support · Status: Wave 0 done; Wave 1 inventory split done
- Files: `.maintenance/EXPANSION-PLAN.md`, `.maintenance/JOURNAL-MASTER-LIST.md`,
  `.maintenance/ASSET-INVENTORY.md`, `.maintenance/ROOT-CARD-CATEGORY-MAP.md`,
  `.maintenance/BREADTH-ENTRY-CATEGORY-MAP.md`, `.maintenance/CATEGORY-8-BUILD-QUEUE.md`
  (planning/inventory docs only)
- 验收节点: ≈2026-06-30 (reminder scheduled)
- Next: continue category 8 Wave 25-A depth-pack production from `.maintenance/CATEGORY-8-BUILD-QUEUE.md`
  with UAI / COLT / MLSys / KDD; `JOURNAL-MASTER-LIST.md` reserves `[A-depth]` for complete
  reusable depth assets and keeps breadth-only seeds in the map files
- 不触碰任何现有 pack 内容；建包按分波滚动，每波过 `tools/run_checks.py` + clone 审计。

## Lane — Workflow Wave W1 · 大类1 经济学领域刊深度包 (parallel workflow)
- **Owner**: planning agent (Opus, parallel Workflow) · Status: content-complete + verified (uncommitted, 待验收)
- W1 result: 6/6 packs built, 12 skills each (72 SKILL.md). Cross-pack clone audit < 0.75
  (no sibling cloning); frontmatter valid; manifests declare 12; source-maps carry URL+date.
  Volatile facts honestly flagged 待核实 where official Elsevier/UChicago/Wiley pages returned
  HTTP 403/402. Human spot-check (jde vs rje identification-strategy) confirms deep venue-specificity.
- Reconciled after AISTATS, 17 concurrent econometrics/finance/theory/applied-micro shell completions, and W2 shell
  completion: `tools/audit_repo.py` now expects the actual combined count (1564 skills / 92 packs /
  200 root cards), and root README badges/tables include the 6 W1 packs, 17 additional
  econometrics/finance/theory/applied-micro packs, 18 W2 management/OM/marketing/accounting/IS packs, and 6 CS/AI
  conference depth packs.
  Root navigation cards remain the existing breadth-card entries unless the owner asks for separate
  depth-pack retargeting.
- Building 6 NEW standalone depth packs (clean gaps, no overlap with Codex CS lane):
  Journal-of-Development-Economics, Journal-of-Public-Economics, Journal-of-Labor-Economics,
  Journal-of-International-Economics, RAND-Journal-of-Economics, Journal-of-Monetary-Economics.
- Each agent ONLY creates files under its own `<Journal>-Skills/` dir; does NOT touch root
  README, root cards, marketplace, or any shared/existing file (those registered later by owner).
- Quality bar: venue-specific, official-source-backed (URL+date) or `待核实`; no find-replace clones.

## Lane — Workflow Wave W2 · 大类1 管理学侧深度包 (parallel workflow, aggressive)
- **Owner**: planning agent (Opus, parallel Workflow) · Status: 18/18 shells completed + registered
- 18 NEW standalone depth packs (clean gaps, no overlap with Codex CS lane / existing depth packs):
  Management-Science, Operations-Research, Manufacturing-and-Service-Operations-Management,
  Production-and-Operations-Management, Journal-of-Operations-Management, Journal-of-Marketing,
  Journal-of-Marketing-Research, Marketing-Science, Journal-of-Consumer-Research, MIS-Quarterly,
  Information-Systems-Research, The-Accounting-Review, Journal-of-Accounting-Research,
  Journal-of-Accounting-and-Economics, Contemporary-Accounting-Research, Organization-Science,
  Journal-of-International-Business-Studies, Journal-of-Business-Venturing.
- Same isolation rule as W1: each agent only writes its own `<Journal>-Skills/` dir; no shared files.
- Same quality bar: venue-specific, official-source-backed (URL+date) or `待核实`; no clones.

## Out of scope (git submodules — do NOT edit)
AER-skills, nature-skills, nature-paper-skills, claude-scholar, codex-claude-academic-skills

## Lane — Category 2 · English Social Sciences depth packs (Agent C)
- **Owner**: Agent C (Opus) · Status: in progress (uncommitted, 待验收) · Started 2026-06-01
- **Why this lane**: category 2 (English social sciences) is an explicit gap in
  `.maintenance/ASSET-INVENTORY.md` ("English social-science depth packs missing"). It is disjoint
  from the active agent's category-1 (econ/mgmt) + category-8 (CS/AI) lanes and from Agent B's
  natural-science/medicine turf, so there is **zero file overlap**.
- **Targets** (each a brand-new standalone `<Journal>-Skills/` depth pack; political science /
  sociology / psychology flagships):
  American-Political-Science-Review, American-Journal-of-Political-Science, American-Sociological-Review,
  American-Journal-of-Sociology, Psychological-Science, Journal-of-Personality-and-Social-Psychology.
- **Isolation rule (same as W1/W2)**: Agent C ONLY creates files under its own new
  `<Journal>-Skills/` directories. It does NOT edit root README.md / README.zh-CN.md, root cards,
  tools/audit_repo.py counts, the marketplace.json of other packs, or any existing shared file.
  Count/README registration is left to the audit owner (Codex) to reconcile, like W1/W2 packs now.
- **Quality bar**: venue-specific, official-source-backed (URL + access date) or `待核实`; 12-skill
  lifecycle tuned per discipline. No find-replace clones — cross-pack clone audit must stay < 0.75.
- **Coordination note**: these journal names are NOT among the active agent's queued packs. If the
  active agent claims any category-2 name later, Agent C yields it.

### Agent C lane — STATUS UPDATE (2026-06-01): COMPLETE
All 6 targeted cat-2 packs built + verified + uncommitted (待验收): American-Political-Science-Review,
American-Sociological-Review, Psychological-Science (built directly) + American-Journal-of-Political-Science,
American-Journal-of-Sociology, Journal-of-Personality-and-Social-Psychology (built via parallel sub-agents).
72 new SKILL.md. Clone audit: none ≥0.50 vs anything repo-wide. Only shared files touched: CLAIMS.md +
PROGRESS.md (append-only). Did NOT touch README counts / tools / other packs — left for owner reconciliation.
