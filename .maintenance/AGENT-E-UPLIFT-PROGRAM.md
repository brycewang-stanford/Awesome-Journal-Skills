# Agent-E — Quality & Capability Uplift Program

Goal (user brief, 2026-06-07): comprehensively improve the repo over an extended autonomous
effort, **especially the quality and capability of the journal skills**. User selected ALL
four directions: depth (clone flagship resources), breadth (quality audit + fixes), capability
(new cross-cutting skills), and infrastructure (modernize the maintenance system).

## Diagnosis (baseline)
- 117 first-party curated packs + 5 imported submodule packs = 122 pack roots; 1930 SKILL.md
  (1824 first-party). 200 root journal-entry navigation folders.
- SKILL.md content is generally good (journal-aware, anti-patterns, output formats) and both CI
  gates (audit_repo.py, clone_audit.py) pass after Phase 1.
- **Capability gap**: exactly ONE pack (Economic-Research-Journal-Skills, the flagship) carries
  the high-leverage runnable resources — `resources/code/{stata,python}`, 12 `worked-examples/`,
  and an `exemplars/library.md`. Every other pack has only `external_tools.md` +
  `official-source-map.md`. The flagship's SKILL.md files are also ~2x deeper (~110 vs ~60 lines).
- **Infra drift**: audit tripwires were stale (1600/95 vs live 1930/122) → CI red. Fixed in Phase 1.
- **Latent near-clones**: the `Computer-Science-Conference-Skills` breadth bundle has many
  0.87–0.89 sibling pairs (below the 0.90 fail-threshold, so CI-legal, but a quality smell).

## Quality bar (rubric the program optimizes toward)
A high-capability journal pack should let an agent *act*, not just *advise*:
1. **Trigger precision** — `description:` is specific enough to auto-activate at the right moment.
2. **Venue-specific facts** — fees, word limits, blinding, data policy, house citation style,
   sourced (`[官]` verified vs `[经验值]` heuristic) with an `official-source-map.md`.
3. **Runnable assets** (empirical packs) — a code library the agent can adapt, not just prose.
4. **Worked examples** — before/after passages showing the craft, not just rules.
5. **Exemplar library** — real published papers in *that venue* by method × topic.
6. **Anti-patterns + output format** — every skill ends with a reusable output contract.

## Phases
- [x] **Phase 1 — infra fix**: reconcile audit tripwires + README badges; add `--counts`. CI green.
- [ ] **Phase 5a — measurement**: `tools/quality_scorecard.py` ranks every first-party pack on
      objective dimensions (skill depth, resources present, description specificity, manifest health).
      Output drives where Phase 4 depth work goes. Wired into CI as a non-failing report.
- [ ] **Phase 2 — breadth fixes**: act on scorecard + clone audit — differentiate the worst
      CS-conference near-clones; tighten objectively weak `description:` fields.
- [ ] **Phase 3 — capability**: a shared, repo-level empirical-methods resource (reusable
      causal-inference code + a reviewer-objection checklist) that empirical packs reference, so
      every quantitative pack inherits the flagship's method rigor without per-pack duplication.
- [ ] **Phase 4 — depth**: give the top empirical-econ packs the flagship treatment
      (resources/code + worked-examples + exemplars), built by QC'd parallel subagents, clone-checked.

## Constraints / coordination
- Additive-only on pack content (new resources/); no rewrite of other lanes' SKILL.md bodies.
- Every new pack resource clone-checked < 0.50 vs siblings before it lands.
- Edits left uncommitted for user 验收 (repo convention). Verifiable commands logged below.

## Progress log
- 2026-06-07: Phase 1 complete + verified (`python3 tools/audit_repo.py` → pass;
  `python3 tools/clone_audit.py --threshold 0.80 --fail-threshold 0.90 --top 10` → max 0.887 < 0.90).
