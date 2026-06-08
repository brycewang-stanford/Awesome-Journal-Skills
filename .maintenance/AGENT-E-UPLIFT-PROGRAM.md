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

## Repeatable Phase-4 pipeline (for remaining packs)
Proven on QJE/JPE/JFE. To lift any deep-but-resourceless EMPIRICAL pack to flagship parity, run one
QC'd subagent per pack with this brief (see git history of QJE for the exact output shape):
1. `cp -R shared-resources/empirical-methods/code <Pack>/resources/code`; prepend a one-line
   provenance HTML comment to the vendored `code/README.md`; change NO Stata/Python command.
2. `<Pack>/resources/README.md` — index; relative-link the two shared prose docs + the pack source-map.
3. `<Pack>/resources/worked-examples/01-introduction.md` — before→after intro in that venue's house
   style, derived ONLY from the pack's own skill files; FICTIONAL illustrative paper (no fabricated facts).
4. `<Pack>/resources/exemplars/library.md` — REAL papers in that venue, **web-verified** (title/authors/
   year/venue), header with access date; OMIT anything unverifiable; document omissions. 6 verified > 15 guessed.
Guardrails: touch only `<Pack>/resources/`; verify venue to avoid sibling-journal misattribution
(JFE≠JF≠RFS; JPE≠AER≠QJE≠EconJournal). After each batch: `python3 tools/run_checks.py --skip-reports
--skip-diff-check` (must stay green) and `python3 tools/quality_scorecard.py --json` to confirm the lift.
Next targets by scorecard (deep prose, no resources): REStud, AMJ, ASQ, J-Marketing, The-Accounting-Review,
J-Accounting-Research, J-Labor-Economics, J-Economic-Growth, J-Human-Resources, J-Financial-Intermediation,
J-Econometrics, J-Development-Economics, J-Public-Economics, RFS, J-Finance, AER-family, etc.
(Theory-only/humanities packs — AMR, Econometric-Theory, AHR, PMLA, Mind — get the checklist's inference/
"so what" sections but NOT the code kit.)

## Known remaining items (logged, not yet done)
- **Phase 2 — CS-conference near-clones**: `Computer-Science-Conference-Skills` has many 0.86–0.89 sibling
  pairs (e.g. ICCV↔ECCV, EACL↔NAACL, ICDM↔SDM). Below the 0.90 CI fail-threshold (they are breadth
  *profiles* of genuinely similar sibling venues), so CI-legal, but a quality smell. Differentiate the
  worst pairs with venue-specific facts (review model, page limits, area structure) when budget allows.
- **Phase 2 — weak descriptions**: scorecard `desc_journal_cue`/`desc_use_when` columns flag packs whose
  `description:` fields under-specify the trigger; tighten the lowest, logging each.

## Progress log
- 2026-06-07: **Phase 1** complete + verified (`audit_repo.py` → pass; clone audit max 0.887 < 0.90).
  Reconciled tripwires 1600→1930 / 95→122; added `--counts`; updated both README badges + methodology.
- 2026-06-07: **Phase 5a** — `tools/quality_scorecard.py` added (117 packs, mean 59.0/100). Confirmed the
  capability gap is *resources*: pre-program only 1 pack (ERJ) had code+worked+exemplars.
- 2026-06-07: **Phase 3** — built `shared-resources/empirical-methods/`: reviewer-objection-checklist.md,
  reporting-standards.md (cross-cutting prose), and a venue-neutral English `code/` kit adapted from ERJ's
  verified Stata/Python (683 lines, py_compile OK, zero command changes).
- 2026-06-07: **Phase 4 pilot** — QJE, JPE, JFE each given the full resource layer via QC'd subagents with
  web-verified exemplars. Scores 69.6 → **93.6** each; packs with full resource layer 1 → 4. Subagents
  correctly excluded misattributed papers (Dube-Lester-Reich→REStat, Carhart→JF, Becker-Allocation→EconJ).
- 2026-06-07: **Phase 2 (spot-fix)** — corrected a real factual defect the pilot surfaced: Becker's
  "A Theory of the Allocation of Time" was misattributed to JPE in 3 places (jpe-theory-model,
  jpe-literature-positioning, JPE source-map). Web-verified it is *The Economic Journal* 75(299):493–517,
  1965; substituted genuinely JPE-published price-theory classics (Stigler 1961, Crime & Punishment 1968).
- 2026-06-07: **Phase 5b** — wired the scorecard into `tools/run_checks.py` as a non-failing report;
  documented both new tools + the `--counts` workflow in `tools/README.md`.
- Final gate (week 1): `python3 tools/run_checks.py --skip-reports --skip-diff-check` → all hard checks pass.

### Week 2 (2026-06-07 cont.) — scale-out
- **Tier-1 bulk vendoring** (mechanical, by script, zero hallucination): vendored the runnable code kit +
  generated a `resources/README.md` index into **all 61 English econometric-fit packs** + the **Chinese
  ERJ kit into 14 Chinese econ packs** (75 total). Scope was deliberately bounded — natural-science/
  medicine (RCT/lab/clinical), CS-AI (ML), and biophysical ag/env packs were EXCLUDED because the
  DID/IV/RDD/DML kit does not fit their methods. Result: packs with a runnable code library **1 → 79**;
  mean score **59.0 → 66.0**. Fixed a vendored-link issue (Chinese `code/README.md` `../code-templates.md`
  → shared hub) so the markdown link-checker stays green.
- **Tier-2 venue layers** (QC'd subagents, web-verified, 3 batches of 6): added a fictional venue-style
  worked-example + a **web-verified** exemplar library to 18 more flagship packs — REStud, Econometrica,
  RFS, SMJ, AMJ, TAR · JAR, Management-Science, APSR, ASR, J-Marketing, JOLE · J-Finance, ASQ, JCR,
  Demography, JDE, JMR. Every subagent excluded misattributed papers (documented sibling-journal traps,
  e.g. FF1993→JFE, Carhart→JF, Hannan-Freeman→AJS, most dev-RCTs→QJE/AER/AEJ). Full-layer packs **4 → 22**;
  mean **66.0 → 68.1**; 20 packs now ≥85.
- Fixed one wrong link-depth (Econometrica exemplars used `../../` where `exemplars/` needs `../../../`).
- All hard gates green after each batch.

### Remaining Tier-2 backlog (pipeline-ready, not yet done — honest no-silent-truncation note)
~53 econometric-fit packs have Tier-1 (code + cross-cutting checklist/standards) but not yet the
venue-specific Tier-2 (worked-example + verified exemplars). They are a real capability uplift already;
Tier-2 is incremental polish. Next by value: J-Public-Economics, J-International-Economics, J-Monetary-
Economics, J-Econometrics, J-Accounting-and-Economics, Contemporary-Accounting-Research, Quantitative-
Economics, RAND-JE, Review-of-Economic-Dynamics, Review-of-Finance, J-Corporate-Finance, JFQA, J-Banking-
Finance, J-Applied-Econometrics, J-Financial-Intermediation, J-Economic-Growth, J-Human-Resources,
Marketing-Science, MISQ, ISR, Org-Science, JIBS, J-Business-Venturing, Operations-Research, POM, JOM,
M&SOM, AJPS, J-Politics, World-Politics, IO, POQ, AJS, Social-Forces, Criminology, JMF, SPQ, JPSP,
Psych-Science, Psych-Bulletin, AERJ, J-Communication, International-Organization. Run the proven Tier-2
brief (one QC'd subagent per pack, web-verified exemplars, `../../../` hub-link depth in exemplars/ &
worked-examples/). Theory-only/humanities packs (AMR, Econometric-Theory, J-Economic-Theory, Math-Finance,
GEB, AHR, PMLA, Mind, Critical-Inquiry, Art-Bulletin, JAAR, Annals-of-Math) get checklist reference only.
Natural-science/medicine/CS-AI/ag-env packs are out of scope for the econometric kit by design.
