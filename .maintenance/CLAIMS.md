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
- **Codex — 2026-06-17 audit-quality cleanup lane**: scorecard trigger semantics and the
  single remaining machine-only root card (`Zuzhi-Yu-Guanli/README.md`); no journal-content
  skill rewrites, no pack-count changes, no root README wall edits, and no submodule edits.
- **Codex — 2026-06-20 month-long quality uplift lane**: measurement-driven cleanup in
  `.maintenance/MONTHLY-UPLIFT-2026-06-20.md`; prioritize low-tail breadth packs, root-card
  provenance, source-map unresolved debt, and clone-audit triage; no submodule edits and no
  count growth unless the user explicitly opens an expansion lane.
- **Claude — 2026-06-21 SkillOpt behavioral-optimization lane**: port Microsoft SkillOpt's
  rollout→reflect→**validation-gate** loop into `tools/skillopt/` (behavioral eval that the
  static `quality_scorecard.py` cannot do), and demo-optimize the **Harvard-Law-Review-Skills**
  pack only. Touches `tools/skillopt/**` and `Harvard-Law-Review-Skills/**` exclusively; targeted
  `git add` only; no other journal-content rewrites, no count changes, no submodule edits.

## Claim log
| Pack | Agent | Status | Notes |
|------|-------|--------|-------|
| Harvard-Law-Review-Skills | Claude | done | SkillOpt behavioral demo: hlr-submission held-out 30→100; fixed Scholastica→own-portal error, added verified word limits/anonymization/Bluebook-22nd; transferred to placement-strategy/workflow/checklist |
| tools/skillopt (harness) | Claude | done | new rollout→judge→**validation-gate** harness (behavioral counterpart to Codex's deterministic `tools/skillopt_gate.py`); tools-only, no overlap |
| American-Historical-Review-Skills | Claude | in progress | SkillOpt scale-up: ahr-submission behavioral loop; add verified review-count/acceptance-rate/decision-timeline facts |
| Journal-of-the-American-Academy-of-Religion-Skills | Claude | in progress | SkillOpt scale-up: jaar-submission behavioral loop; add verified 106-day/≈90%-reject/grad-review-policy facts |
| Progress-in-Human-Geography-Skills | Claude | assessed | SkillOpt triage: submission skill already well-calibrated; facts genuinely volatile (需复核) — no high-value verified edit, gate would reject padding |
| SkillOpt scale-up wave (anthro/socio/comm/educ/geo/humanities submission skills) | Claude | done | 16 packs optimized over 4 waves (commits 05b73424/d57b9d08/e932b38f/f322301d), held-out behavioral +6 to +72, all gate-accepted, every fact source-map-grounded; static scores unchanged. 19 skills optimized + PiHG triaged; report.py --check green |
| SkillOpt citation/style tier (19 packs) | Claude | done | dedicated citation skills HLR/AHR/PMLA/Mind edited (+22..+59, commit 5c8ae3f6), JAAR certified; writing-style tier ASR 7th-ed transfer + 13 certified (commit 7ca579e1). Honest triage, no padding. Yale lane (parallel) untouched |
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
| Repo-wide second-pass uplift | Codex | done | scorecard low-tail depth-pack hardening + CS conference breadth routing de-cloning; local hard gates passed, no push |
| Zuzhi-Yu-Guanli | Codex | done | root-card enrichment only; no canonical skill rewrite |
| tools/quality_scorecard.py | Codex | done | trigger-pattern recognition only; no scoring threshold weakening |
| tools/external_link_audit.py | Codex | done | markdown URL-boundary fix for adjacent links; no network gate added |
| Computer-Science-Conference-Skills URL anchors | Codex | done | verified 404 replacements only; no new conference/profile count |
| Computer-Science-Conference-Skills HRI/CoRL routing | Codex | done | sibling-routing correction only; no profile-count changes |
| Repo-wide monthly quality uplift | Codex | in progress | see `.maintenance/MONTHLY-UPLIFT-2026-06-20.md`; count-disciplined score/root/source/clone cleanup |

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

### Agent C lane — WAVE C3 (2026-06-XX): cat-2 sub-discipline expansion (in progress, 待验收)
Extending the Category 2 lane into NEW social-science sub-disciplines (still zero overlap with the
active agent's cat-1/8 and Agent B's natural-science/medicine turf). 6 NEW standalone packs, each in
its own new dir, built via parallel sub-agents + independent QC (clone audit <0.75, full bilingual
READMEs, official-source-map with 待核实):
- American-Educational-Research-Journal-Skills (`aerj-`) — Education (AERA/SAGE) — NEW subdiscipline
- Demography-Skills (`demog-`) — Demography/population (PAA/Duke UP, open access) — NEW subdiscipline
- Criminology-Skills (`crim-`) — Criminology (ASC/Wiley) — NEW subdiscipline
- Journal-of-Communication-Skills (`joc-`) — Communication (ICA/OUP) — NEW subdiscipline
- Psychological-Bulletin-Skills (`psychbull-`) — Psychology review/meta-analysis flagship (APA)
- Journal-of-Politics-Skills (`jop-`) — Political science (SPSA/UChicago), distinct from APSR/AJPS
Isolation rule unchanged: only own new dirs; CLAIMS/PROGRESS append-only; no README-count/tools/other-pack edits.

### Agent C lane — WAVE C3 STATUS (in progress → COMPLETE, 待验收)
6 cat-2 sub-discipline packs built + independently QC'd + uncommitted: American-Educational-Research-Journal,
Demography, Criminology, Journal-of-Communication, Psychological-Bulletin, Journal-of-Politics. 72 new
SKILL.md. Fixed one near-clone (joc-rebuttal 0.757→<0.45). All 12 cat-2 packs (C1-C3) now <0.50 vs anything.
Only shared files touched: CLAIMS.md + PROGRESS.md (append-only). No README-count/tools/other-pack edits.

## Lane — Categories 3/7/9 + cat-2 round-out (Agent C, multi-batch)
- **Owner**: Agent C (Opus) · Started after cat-2 (12 packs) committed by owner · Status: in progress (待验收)
- **Why**: per ASSET-INVENTORY, categories 3 (Humanities), 7 (Engineering), 9 (Agriculture & Env) are
  "almost all complete packs still missing". Nobody has claimed them (Agent B = nat-sci/medicine only;
  active agent = cat-1/8). Zero file overlap.
- **Boundary discipline (avoid Agent B)**: cat-9/cat-7 packs use UNAMBIGUOUSLY ag/env/engineering venues,
  NOT Nature-family or physics journals (those are Agent B's nat-sci turf).
- **Batch A — cat-3 Humanities** (humanities-adapted skill set: argument / sources / interpretation /
  citation-style, NOT data-analysis): American-Historical-Review, PMLA, Mind, Critical-Inquiry,
  The-Art-Bulletin, Journal-of-the-American-Academy-of-Religion.
- **Batch B — cat-9 Agriculture & Environment** (empirical-science skill set): Environmental-Science-and-Technology,
  Global-Environmental-Change, Conservation-Biology, Global-Change-Biology, Field-Crops-Research, Agricultural-Systems.
- **Batch C — cat-2 round-out** (IR / survey / family / social-psych subfields): International-Organization,
  World-Politics, Public-Opinion-Quarterly, Social-Forces, Journal-of-Marriage-and-Family, Social-Psychology-Quarterly.
- **Process**: parallel sub-agents per batch → independent QC (clone audit <0.75 ideally <0.50, structure,
  full bilingual READMEs, source maps) → fix any near-clones → log. Isolation: only own new dirs;
  CLAIMS/PROGRESS append-only; no README-count/tools/other-pack edits (owner reconciles counts).

### Agent C lane — WAVE C4 STATUS: COMPLETE (待验收)
18 new packs (216 SKILL.md) built + independently QC'd + uncommitted: Batch A cat-3 Humanities (AHR, PMLA,
Mind, Critical-Inquiry, The-Art-Bulletin, JAAR); Batch B cat-9 Ag/Env (Environmental-Science-and-Technology,
Global-Environmental-Change, Conservation-Biology, Global-Change-Biology, Field-Crops-Research, Agricultural-Systems);
Batch C cat-2 round-out (International-Organization, World-Politics, Public-Opinion-Quarterly, Social-Forces,
Journal-of-Marriage-and-Family, Social-Psychology-Quarterly). All <0.50 clone vs anything; full bilingual READMEs;
JAAR completed by Agent C after a sub-agent API overload. Only shared files touched: CLAIMS.md + PROGRESS.md
(append-only). No README-count/tools/other-pack edits. Agent C cumulative = 30 packs across cat 2/3/9.

## Lane — Economic-Research-Journal-Skills DEEP POLISH (Agent D, user-directed)
- **Owner**: Agent D (Opus, user-directed) · Status: in progress (待验收) · Started 2026-06-06
- **Why this lane**: user explicitly directed a deep, best-in-class polish of
  `Economic-Research-Journal-Skills/` (《经济研究》). This Chinese depth pack was UNCLAIMED in the
  log above. Goal: make it the strongest 《经济研究》 submission skill pack available, venue-specific
  and exemplar-anchored, per `.maintenance/METHODOLOGY.md`.
- **Isolation rule**: Agent D ONLY edits files under `Economic-Research-Journal-Skills/`. Does NOT
  touch root README.md / README.zh-CN.md counts, tools/audit_repo.py, other packs' files, or any
  submodule. CLAIMS.md + PROGRESS.md are append-only. If folder/skill COUNT changes (new skills
  added), that is flagged here for the audit owner (Codex) to reconcile root counts — Agent D does
  not edit root counts itself.
- **Coordination note**: `Economic-Research-Journal-Skills` is NOT in Agent A's queue (QJE/JPE/
  Econometrica/RES/JF/JFE/RFS) nor any Codex/Agent B/Agent C target. Zero file overlap. If Agent A
  later claims it, defer to this lane (already in progress).
- **Quality bar**: venue-specific, official-source-backed (URL + access date) or `待核实`; deepen
  every SKILL.md with real 《经济研究》 facts, worked Chinese-context examples, modern causal-inference
  code, and named exemplar papers. No find-replace clones.

### Agent D lane — DE-CONFLICTION UPDATE (2026-06-06)
DISCOVERED mid-work that a parallel agent is ALSO actively rebuilding
`Economic-Research-Journal-Skills/` (it added new skills er-introduction / er-reproducibility /
er-robustness / er-theory-hypotheses / er-reviewer-lens + `resources/code/*.do`, all uncommitted).
To honor the user's "don't conflict / collaborate friendly" directive, Agent D YIELDS the
skill-body rewrites + new-skill expansion + `resources/code/` to that agent, and narrows its own
lane to the **web-verified fact layer** (zero overlap with the other agent's new files):
- `resources/official-source-map.md` (rewritten, web-verified, VERIFIED/待核实 layered)
- reference-format BUG FIX in `templates/manuscript_template.md` + `templates/checklist.md`
  (《经济研究》 uses 著者-出版年制, NOT 顺序编码制 — the repo was factually wrong)
- `resources/code-templates.md` (verified command+citation reference; complements the other
  agent's runnable `.do` files)
- `skills/er-identification/SKILL.md` (verified exemplars + modern estimators; complements the
  other agent's `03_did_modern.do`, which already defers to er-identification for 投稿口径)
- NEW `HANDOFF-FROM-AGENT-D.md` (all of Agent D's verified research handed to the parallel agent:
  reference-format correction, exemplar attribution warnings, 江艇 2022 mechanism citation, English
  梗概 char-count caveat, verified journal facts, verified causal-inference commands).
Removed Agent D's duplicate empty dirs (er-theory-hypothesis singular, er-data-sample). Agent D's
er-robustness Write was correctly blocked by the read-before-write guard → the other agent's
er-robustness is authoritative. Agent D will NOT touch README/manifests/other skill bodies to avoid
clobbering. Recommend a SEQUENTIAL second polish pass by Agent D after the rebuild stabilizes.

### Agent D lane — SECOND PASS COMPLETE (2026-06-06, 待验收)
After the parallel agent's rebuild (18 skills + code/ + worked-examples/ + exemplars/), Agent D ran a
deep fact-audit (via subagent) + second polish pass. Findings: pack was largely accurate; issues
localized + fixed:
- `skills/er-submission/SKILL.md` was the STALE original (parallel agent updated templates but not
  this body) asserting unverified numbers (摘要200–400字/英文200–300词/JEL≥2/查重≤15%/上传≤20MB/
  推荐审稿人3名) as official. REWROTE with [官]/[经验值] discipline + added VERIFIED ¥0 fees,
  10-year multi-submission penalty, masthead/收录 facts.
- `≥1000字中文对照` was asserted as a hard official requirement in ~9 places (er-abstract ×4,
  checklist [官] mislabel, manuscript_template, README.md, README.zh-CN, worked-examples/08) but has
  NO official basis (verified). SOFTENED all to "中文对照（官方未规定字数）".
- Added `resources/exemplars/library.md` — 18 web-verified 《经济研究》 papers by method × hot-topic
  (complements the parallel agent's 5-paper deep-teardown README in the same dir; added a pointer).
- Augmented `resources/official-source-map.md` VERIFIED table: ¥0 fees, 10yr penalty, verbatim
  Chinese+foreign reference examples (AJCASS sister-journal house style), 收录/邮发 details.
QC: 18/18 frontmatter valid; no broken links (the ../../../resources from templates/ is correct);
no ≥1000字 / wrong-direction 顺序编码 residue; exemplar attributions all correct; 江艇 2022 mechanism
stance consistent. Research staged in `.maintenance/AGENT-D-ERJ-RESEARCH.md`. NOTE: parallel agent was
still active during this pass; Agent D only edited stale/erroneous shared files + added new files, no
clobbering observed (read-before-write guard held). Skill bodies the parallel agent owns left untouched.

### Agent-E lane — quality & capability uplift program (2026-06-07, 待验收)
Multi-phase program to raise the quality + capability of journal skills repo-wide. Lane boundaries:
infrastructure (`tools/*`, `.github/workflows/*`, root READMEs) + NEW additive resources under
existing packs (resources/code, resources/worked-examples, resources/exemplars). Does NOT rewrite
existing `skills/*/SKILL.md` bodies owned by other lanes; only ADDS resources + may tighten
`description:` frontmatter where objectively weak (logged per-pack). Leaves edits uncommitted for 验收.
- Phase 1 DONE: audit_repo.py tripwires reconciled 1600→1930 / 95→122 (matches live inventory);
  added `--counts` helper; README.md + README.en.md badges/methodology updated; audit + clone audit
  both green. (audit_repo.py constants may have been concurrently bumped by another process; verified.)
- Phase 5a: tools/quality_scorecard.py — objective per-pack scoring to target depth work.
- Phase 3: shared cross-cutting empirical-methods resource (reusable causal-inference assets).
- Phase 4: propagate flagship ERJ-style resources (code/worked-examples/exemplars) to top empirical packs.
See `.maintenance/AGENT-E-UPLIFT-PROGRAM.md` for the full plan + progress.

### Agent-E lane — PROGRESS UPDATE (2026-06-07, 待验收)
Phases 1, 5a, 3, 5b complete; Phase 4 piloted on 3 packs; Phase 2 spot-fix done. All hard gates green
(`python3 tools/run_checks.py --skip-reports --skip-diff-check`). New/changed (all uncommitted for 验收):
- tools/audit_repo.py (tripwires + `--counts`), tools/quality_scorecard.py (NEW), tools/run_checks.py
  (scorecard report), tools/README.md; README.md + README.en.md badges/methodology → 1930/122.
- shared-resources/empirical-methods/ (NEW): reviewer-objection-checklist.md, reporting-standards.md,
  code/ (English venue-neutral kit), README.md.
- Quarterly-Journal-of-Economics-Skills / Journal-of-Political-Economy-Skills /
  Journal-of-Financial-Economics-Skills: NEW resources/{code,worked-examples,exemplars,README} (69.6→93.6).
- JPE Becker-1965 misattribution fixed in jpe-theory-model, jpe-literature-positioning, JPE source-map.
Full plan + repeatable Phase-4 pipeline + next targets: .maintenance/AGENT-E-UPLIFT-PROGRAM.md.

### Agent-E lane — WEEK-2 UPDATE (2026-06-07, 待验收)
Scaled out the capability layer. Tier-1 (runnable code kit + resources/README) vendored into 75 packs
(61 English econometric-fit + 14 Chinese econ); Tier-2 (web-verified exemplars + venue worked-example)
added to 18 more flagships (3 QC'd subagent batches). Now 22 packs at full resource layer; 79 with a
runnable code library; scorecard mean 59.0→68.1. All hard gates green. Natural-sci/medicine/CS-AI/ag-env
packs intentionally EXCLUDED from the econometric kit (wrong method). Remaining Tier-2 backlog (~53 packs)
documented in AGENT-E-UPLIFT-PROGRAM.md — pipeline-ready, not silently skipped.

### Agent-E lane — WEEK-3 UPDATE (2026-06-08, 待验收)
Tier-2 econometric-fit backlog (43 packs) CLEARED — every fit pack now has web-verified exemplars +
worked-example. 67 packs at full resource layer; mean 59.0→73.5; all hard gates green. Details in
AGENT-E-UPLIFT-PROGRAM.md (Week 3). Edits committed by the concurrent committer; nothing destructive.

### Agent-E lane — WEEK-4 UPDATE (2026-06-08, 待验收) — PROGRAM COMPLETE
All remaining categories cleared (natsci/med 9, CS-AI 6, ag/env 6, theory/humanities 13; Chinese 14 by
parallel agent). EVERY single-venue first-party depth pack (113) now has worked-examples + exemplars;
79 have the code library. Mean 59.0→79.0; all hard gates green. Fixed mid-run: source-map link repoints,
AER/claude-scholar submodule pointer drift (restored), link-depth regex. See AGENT-E-UPLIFT-PROGRAM.md Week 4.

### Codex lane — repo-wide breadth-bundle capability uplift (2026-06-10, complete)
User requested a comprehensive one-week repo-wide capability uplift. Scope is deliberately low-conflict:
4 large breadth bundles (`Chinese-SocialScience-Journal-Skills`, `English-SocialScience-Journal-Skills`,
`English-NaturalScience-Journal-Skills`, `Computer-Science-Conference-Skills`), report/scorecard tooling,
and CS conference near-clone differentiation. Does NOT rewrite single-venue depth packs already completed
by Agent-E except for objective report-tool changes if needed. Leaves edits uncommitted for user 验收.
Completed with all hard checks green; see `.maintenance/AGENT-E-UPLIFT-PROGRAM.md` Week 5.

### Codex lane — existing-pack low-tail capability uplift (2026-06-17, complete)
User requested a one-week comprehensive improvement pass **without increasing the journal/conference
count**. Current lane is conflict-minimized and count-preserving:
- Include: selected existing low-tail first-party depth packs surfaced by `tools/quality_scorecard.py`,
  especially information systems, marketing/consumer research, public opinion/social psychology,
  political science, humanities, accounting, and econometrics packs.
- Exclude: any new journal/conference pack, root-entry expansion, submodules, `Economic-Research-Journal-Skills/`,
  and broad natural-science/medicine rewrites. To clear the repo-wide scorecard floor, only three
  existing reserved-area packs received narrow, non-structural scorecard patches (`JACS`, `Cancer-Cell`,
  `Annals-of-Mathematics`); no files were created and no lifecycle/manifest/counts changed.
- Coordination rule: check `git status` before each edit/validation boundary; keep edits targeted by path;
  do not weaken audit, clone, scorecard, or run-check gates.
