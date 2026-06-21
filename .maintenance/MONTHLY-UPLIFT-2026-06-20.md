# Codex Monthly Uplift Plan — 2026-06-20 to 2026-07-20

## Objective

Raise Awesome Journal Skills one clear quality tier over one month by improving
the current repository rather than inflating counts. This pass is count
disciplined: no new journals, packs, root cards, or submodules unless the user
explicitly opens a separate expansion lane.

## Baseline snapshot

Captured on 2026-06-20 from a clean `main...origin/main` checkout.

| Check | Current result |
|---|---:|
| `tools/audit_repo.py --counts` | 2809 skills / 183 packs / 200 root entries |
| `tools/quality_scorecard.py --top 40 --show-skills` | mean 93.3, min 89.2, below 86/88/90 = 0/0/2 |
| Low-tail packs below 90 | Journal of Public Administration Research and Theory, Comparative Political Studies |
| `tools/root_entry_audit.py` | 200 enriched cards, 0 warnings |
| `tools/source_map_audit.py` | 168 source maps, 0 warnings |
| Highest unresolved source maps | Journal of Labor Economics, Journal of Marketing, M&SOM, AEJ Applied Economics, Conservation Biology |
| `tools/clone_audit.py --threshold 0.75 --fail-threshold 0.90 --top 40` | no fail-threshold hits; top risks are Science/PNAS rebuttal and CS conference breadth pairs around 0.799 |

## Work worth doing

1. **Maintain the low-tail score floor.** Any first-party pack below 90 is
   visible quality debt. Fix it with venue-specific router guidance,
   diagnostic tables, source discipline, and decision rules, not generic prose.
2. **Close root-card provenance warnings.** Four enriched Chinese root cards
   still lack external URLs. Fix only with reliable public sources; otherwise
   keep the warning honest.
3. **Reduce unresolved source-map debt.** The source-map audit has no structural
   warnings, but a few packs still carry many `UNVERIFIED` / `待核实` markers.
   The month should turn reachable official facts into checked entries and
   leave blocked facts explicitly labeled.
4. **Triage high-similarity pairs.** CS conference breadth profiles and the
   Science/PNAS rebuttal pair should be either differentiated with concrete
   sibling-routing logic or documented as intentional shared scaffolding.
5. **Improve maintenance ergonomics.** Keep acceptance commands, score movement,
   and remaining risks visible so future agents do not rediscover the same
   baselines.

## Four-week execution plan

### Week 1 — Measurable cleanup

- Clear the four `root_entry_audit.py` URL warnings if reliable sources exist.
- Improve any packs below 90 with router-level decision tables, field-specific
  rejection risks, and official-source/use-case scaffolding.
- Re-run `quality_scorecard.py`, `root_entry_audit.py`, and
  `run_checks.py --skip-reports` after each small batch.

### Week 2 — Breadth-pack differentiation

- Use clone-audit output to identify the top CS conference near-clone clusters.
- Add sibling-selection or "do not route here" tables in shared resources
  where many profiles share a template.
- Differentiate only the highest-risk profile pairs first; keep broad template
  structure where it is useful and honest.

### Week 3 — Source-map reliability

- Take the top unresolved source maps in `source_map_audit.py`.
- Convert reachable official-source facts into checked rows with dates.
- Preserve `UNVERIFIED` / `待核实` for blocked, login-only, or unstable facts.
- Record any blocked-source pattern in the pack source map rather than guessing.

### Week 4 — Acceptance hardening

- Refresh score, clone, source-map, root-card, and external-link reports.
- Sync `CONTRIBUTING.md`, `tools/README.md`, and README snippets only if the
  commands or user-facing expectations have changed.
- Produce a final acceptance note with exact commands, score movement, and
  remaining advisory risks.

## Anti-cheat constraints

- Do not lower scorecard thresholds or clone-audit thresholds to make numbers
  look better.
- Do not delete checks, hide warnings, or reclassify weak packs as out of
  scope.
- Do not add low-quality packs or journals just to grow inventory counts.
- Do not invent current journal facts. Use official pages when reachable; mark
  blocked facts transparently.
- Do not touch submodules from this lane.

## Acceptance commands

```bash
python3 tools/audit_repo.py --counts
python3 tools/quality_scorecard.py --top 40 --show-skills
python3 tools/root_entry_audit.py
python3 tools/source_map_audit.py
python3 tools/clone_audit.py --threshold 0.75 --fail-threshold 0.90 --top 40
python3 tools/run_checks.py --skip-reports
git diff --check
git status --short --branch
```

## Work log

| Date | Batch | Status | Evidence |
|---|---|---|---|
| 2026-06-20 | Baseline and monthly plan | done | Baseline commands above |
| 2026-06-20 | Root-card provenance closure | done | `python3 tools/root_entry_audit.py` -> 200 enriched, 0 machine-only, 0 warnings |
| 2026-06-20 | Low-tail breadth resource entry points | done | `python3 tools/quality_scorecard.py --min-score 90 --top 8` -> min 90.0, below 86/88/90 = 0/0/0 |
| 2026-06-20 | Clone-audit triage batch | done | `python3 tools/clone_audit.py --threshold 0.75 --fail-threshold 0.90 --top 40` -> no fail-threshold hits; Science/PNAS pair no longer appears >=0.75 |
| 2026-06-20 | JoE source-map policy refresh | done | `python3 tools/source_map_audit.py` -> 0 warnings; JoE removed from highest unresolved source-map list after official 2026-06-20 portal/fee/review/data refresh |
| 2026-06-20 | JBF source-map policy refresh | done | `python3 tools/source_map_audit.py` -> 0 warnings; JBF removed from highest unresolved source-map list after official 2026-06-20 fee/review/editor/data/style refresh |
| 2026-06-20 | JET source-map policy refresh | done | `python3 tools/source_map_audit.py` -> 0 warnings; JET removed from highest unresolved source-map list after official 2026-06-20 editor/review/data/style refresh |
| 2026-06-20 | EJ source-map policy refresh | done | `python3 tools/source_map_audit.py` -> 0 warnings; EJ removed from highest unresolved source-map list after official 2026-06-20 submission-fee/editor/review/data refresh |
| 2026-06-20 | JFI source-map policy refresh | done | `python3 tools/source_map_audit.py` -> 0 warnings; JFI removed from highest unresolved source-map list after official 2026-06-20 fee/editor/review/data refresh |
| 2026-06-20 | GEC source-map policy refresh | done | `python3 tools/source_map_audit.py` -> 0 warnings; GEC removed from highest unresolved source-map list after official 2026-06-20 article-type/review/editor/APC/data refresh |
| 2026-06-20 | JBES source-map policy refresh | done | `python3 tools/source_map_audit.py` -> 0 warnings; JBES removed from highest unresolved source-map list after official 2026-06-20 scope/editor/ASA-data-policy refresh plus live-T&F preflight boundaries |
| 2026-06-20 | JDE source-map policy refresh | done | `python3 tools/source_map_audit.py` -> 0 warnings; JDE removed from highest unresolved source-map list after official 2026-06-20 fee/editor/review/short-paper/data refresh |
| 2026-06-20 | JOP source-map policy refresh | done | `python3 tools/source_map_audit.py Journal-of-Politics-Skills` -> unresolved_flags 0 after 2026-06-20 SPSA/editor/Dataverse/API refresh plus UChicago author-rule snippet provenance |
| 2026-06-20 | REStat source-map policy refresh | done | `python3 tools/source_map_audit.py Review-of-Economics-and-Statistics-Skills` -> unresolved_flags 0 after 2026-06-20 MIT/Editorial Express/Harvard Dataverse refresh |
| 2026-06-20 | AgSy source-map policy refresh | done | `python3 tools/source_map_audit.py Agricultural-Systems-Skills --all` -> unresolved_flags 0 after 2026-06-20 ScienceDirect/Elsevier article-type/review/APC/data-policy refresh |
| 2026-06-20 | JEEA source-map policy refresh | done | `python3 tools/source_map_audit.py Journal-of-the-European-Economic-Association-Skills --all` -> unresolved_flags 0 after 2026-06-20 EEA/OUP membership/fee/editorial/review/DCAS refresh |
| 2026-06-20 | Mathematical Finance source-map policy refresh | done | `python3 tools/source_map_audit.py Mathematical-Finance-Skills --all` -> unresolved_flags 0 after 2026-06-20 Wiley/BFS/data-policy/editor-metadata refresh |
| 2026-06-20 | Critical Inquiry source-map policy refresh | done | `python3 tools/source_map_audit.py Critical-Inquiry-Skills --all` -> unresolved_flags 0 after 2026-06-20 CI submissions/overview/editors/OA refresh |
| 2026-06-20 | JBV source-map policy refresh | done | `python3 tools/source_map_audit.py Journal-of-Business-Venturing-Skills --all` -> unresolved_flags 0 after 2026-06-20 ScienceDirect guide/editorial-board/OA/data-policy refresh and Co-EIC update |
| 2026-06-20 | QE source-map policy refresh | done | `python3 tools/source_map_audit.py Quantitative-Economics-Skills --all` -> unresolved_flags 0 after 2026-06-20 ES submission/editorial/replication plus Wiley metadata refresh |
| 2026-06-20 | JAE source-map policy refresh | done | `python3 tools/source_map_audit.py Journal-of-Accounting-and-Economics-Skills --all` -> unresolved_flags 0 after 2026-06-20 ScienceDirect/archived-guide/Wharton/EAA/Elsevier-policy refresh |
| 2026-06-20 | JMF source-map policy refresh | done | `python3 tools/source_map_audit.py Journal-of-Marriage-and-Family-Skills --all` -> unresolved_flags 0 after 2026-06-20 NCFR/Wiley submission/style/review/data-policy refresh |
| 2026-06-20 | JPubE source-map policy refresh | done | `python3 tools/source_map_audit.py Journal-of-Public-Economics-Skills --all` -> unresolved_flags 0 after 2026-06-20 ScienceDirect/Elsevier guide/editorial-board/Option-C data-policy refresh |
| 2026-06-20 | SPQ source-map policy refresh | done | `python3 tools/source_map_audit.py Social-Psychology-Quarterly-Skills --all` -> unresolved_flags 0 after 2026-06-20 SAGE author-instructions/home/editorial-board/data-policy refresh |
| 2026-06-20 | AJS source-map policy refresh | done | `python3 tools/source_map_audit.py American-Journal-of-Sociology-Skills --all` -> unresolved_flags 0 after 2026-06-20 UChicago Press/Editorial Manager source-route refresh and live-check boundary cleanup |
| 2026-06-20 | GCB source-map policy refresh | done | `python3 tools/source_map_audit.py Global-Change-Biology-Skills --all` -> unresolved_flags 0 after 2026-06-20 Wiley author-guideline/checklist/editorial-board/data-policy refresh |
| 2026-06-20 | JFR source-map policy refresh | done | `python3 tools/source_map_audit.py Journal-of-Financial-Research-Skills --all` -> unresolved_flags 0 after 2026-06-20 jryj/pbocri official journal-intro/submission/review-process refresh |
| 2026-06-20 | JIE source-map policy refresh | done | `python3 tools/source_map_audit.py Journal-of-International-Economics-Skills --all` -> unresolved_flags 0 after 2026-06-20 ScienceDirect Guide/editorial-board, Mendeley Data, and Elsevier submission-fee refresh |
| 2026-06-20 | Management Science source-map policy refresh | done | `python3 tools/source_map_audit.py Management-Science-Skills --all` -> unresolved_flags 0 after 2026-06-20 INFORMS PubsOnline submission-guidelines/editorial-board/code-data/fee refresh |
| 2026-06-20 | AERJ source-map policy refresh | done | `python3 tools/source_map_audit.py American-Educational-Research-Journal-Skills --all` -> unresolved_flags 0 after 2026-06-20 SAGE author-instructions/AERA home/editors/operations/standards refresh and integrated-journal correction |
| 2026-06-20 | Criminology source-map policy refresh | done | `python3 tools/source_map_audit.py Criminology-Skills --all` -> unresolved_flags 0 after 2026-06-20 ASC/Wiley/ACT/APC/data-policy/preprint review refresh |
| 2026-06-20 | ISR source-map policy refresh | done | `python3 tools/source_map_audit.py Information-Systems-Research-Skills --all` -> unresolved_flags 0 after 2026-06-20 INFORMS submission-guidelines/editorial-board/editorial-statement/Open-Option refresh |
| 2026-06-20 | JIBS source-map policy refresh | done | `python3 tools/source_map_audit.py Journal-of-International-Business-Studies-Skills --all` -> unresolved_flags 0 after 2026-06-20 Springer/AIB journal-home/editorial-board/submission-guidelines/OA-DART refresh |
| 2026-06-20 | RED source-map policy refresh | done | `python3 tools/source_map_audit.py Review-of-Economic-Dynamics-Skills --all` -> unresolved_flags 0 after 2026-06-20 SED/ScienceDirect Guide/editorial-board/data-code/APC refresh |
| 2026-06-20 | JPAM source-map policy refresh | done | `python3 tools/source_map_audit.py Journal-of-Policy-Analysis-and-Management-Skills --all` -> unresolved_flags 0 after 2026-06-20 APPAM/Wiley Research Exchange/fee/article-type/data-repository refresh |
| 2026-06-20 | American Anthropologist source-map policy refresh | done | `python3 tools/source_map_audit.py American-Anthropologist-Skills --all` -> unresolved_flags 0 after 2026-06-20 AA/AAA/Wiley ACT/Research Exchange/ethics/APC refresh |
| 2026-06-20 | New Media & Society source-map policy refresh | done | `python3 tools/source_map_audit.py New-Media-and-Society-Skills --all` -> unresolved_flags 0 after 2026-06-20 SAGE author-instructions/home/editorial-board/ethics/data-policy refresh |
| 2026-06-20 | AER Insights source-map policy refresh | done | `python3 tools/source_map_audit.py AER-Insights-Skills --all` -> unresolved_flags 0 after 2026-06-20 AEA submission/editorial-policy/editors/style/data-code/JEL refresh plus single-blind correction |
| 2026-06-20 | AJPS source-map policy refresh | done | `python3 tools/source_map_audit.py American-Journal-of-Political-Science-Skills --all` -> unresolved_flags 0 after 2026-06-20 AJPS/MPSA manuscript-prep/editorial-board/Dataverse/AI/SI-25/CCSS refresh |
| 2026-06-20 | Low-tail depth score floor | done | `python3 tools/quality_scorecard.py --min-score 90 --top 8 --show-skills` -> min 90.0, below 86/88/90 = 0/0/0 after JPART/CPS venue-specific diagnostic expansions |
| 2026-06-20 | JOLE source-map policy refresh | done | `python3 tools/source_map_audit.py Journal-of-Labor-Economics-Skills --all` -> unresolved_flags 0 after 2026-06-20 UChicago/SOLE/Editorial Manager source refresh and portal live-check boundary cleanup |
| 2026-06-20 | JM source-map policy refresh | done | `python3 tools/source_map_audit.py Journal-of-Marketing-Skills --all` -> unresolved_flags 0 after 2026-06-20 AMA/SAGE author-instructions/editorial-leadership/transparency/fee refresh |
| 2026-06-20 | M&SOM source-map policy refresh | done | `python3 tools/source_map_audit.py Manufacturing-and-Service-Operations-Management-Skills --all` -> unresolved_flags 0 after 2026-06-20 INFORMS submission-guidelines/editorial-board/AI-policy/practice-track/Open-Option refresh plus structured-abstract correction |
| 2026-06-20 | AEJ Applied source-map policy refresh | done | `python3 tools/source_map_audit.py AEJ-Applied-Economics-Skills --all` -> unresolved_flags 0 after 2026-06-20 AEA journal/editorial-policy/submission/style/data-code/disclosure refresh plus single-blind and Raymond Fisman corrections |
| 2026-06-20 | Conservation Biology source-map policy refresh | done | `python3 tools/source_map_audit.py Conservation-Biology-Skills --all` -> unresolved_flags 0 after 2026-06-20 SCB/Wiley scope/style/double-anonymous/ACT/data-sharing refresh plus DAS-vs-deposit correction |
| 2026-06-20 | Field Crops Research source-map policy refresh | done | `python3 tools/source_map_audit.py Field-Crops-Research-Skills --all` -> unresolved_flags 0 after 2026-06-20 ScienceDirect/Elsevier scope/article-types/review/APC/Option-C data-policy refresh |
| 2026-06-20 | Organization Science source-map policy refresh | done | `python3 tools/source_map_audit.py Organization-Science-Skills --all` -> unresolved_flags 0 after 2026-06-20 INFORMS submission/editorial-board/editorial-statement/transparency/checklist/Open-Option refresh plus 2025 data-policy correction |
| 2026-06-20 | User-facing maintenance docs | done | `CONTRIBUTING.md`, `tools/README.md`, `README.md`, and `README.en.md` now point maintainers to the count-disciplined monthly quality program and acceptance commands |
| 2026-06-20 | Post-batch acceptance gates | done | `run_checks.py --skip-reports` passed; counts remain 2809 / 183 / 200; scorecard min 90.0; root/source-map warnings 0; clone audit has no 0.90 fail-threshold hits |
| 2026-06-20 | AEJ: Economic Policy single-blind correction | done | Corrected a factual error: AEJ: Economic Policy is **single-blind** (verified on `aeaweb.org/journals/pol/editorial-policy`), not double-blind. Dropped anonymization requirements across 13 files; injected verified facts (Editor C. Kirabo Jackson; fee 200/100/0 member, 300/200/0 nonmember; USD 15/page pub fee; 100-word abstract). `source_map_audit.py AEJ-Economic-Policy-Skills --all` -> unresolved_flags 11 -> 5, 0 warnings |
| 2026-06-20 | The Accounting Review sitting Senior Editor | done | June 2026 transition now live: Mohan Venkatachalam (Duke, Fuqua) confirmed as sitting Senior Editor on the AAA masthead (2026-06-20), succeeding Kathryn Kadous. Updated source map (+masthead source #7), workflow, and review-process skills. `source_map_audit.py The-Accounting-Review-Skills --all` -> 0 warnings (12 flags retained — fee/403-PDF/full-roster genuinely volatile) |
| 2026-06-20 | Lane-A verification note | n/a | Global `run_checks.py`/`audit_repo.py` cannot be cleanly run while a separate active expansion lane has uncommitted social-science depth packs on disk (untracked); Lane-A correctness was verified per-pack with scoped `source_map_audit.py` and per-pack broken-link checks instead |
| 2026-06-20 | World Politics publisher correction | done | Factual fix: publisher changed from Cambridge UP (through Vol. 74/2022) to **Johns Hopkins UP** (Vol. 75/2023+) per Cambridge Core; triple-blind, <=12,500w, Dataverse verified. `source_map_audit.py World-Politics-Skills --all` -> flags 12 -> 7, 0 warnings |
| 2026-06-20 | JCF fabricated-editor correction | done | Factual fix: prior source map + both READMEs named a fabricated EiC roster (Lyandres/Lehar/Parlour); corrected to Co-EiCs **Hankins (Kentucky) + Almeida (Illinois)**, independently corroborated. flags 11 -> 13 (honest live-roster/blocked-page flags) |
| 2026-06-20 | RJE editor + fee correction | done | Factual fix: EiC "Craig A. Bond" -> "Craig Bond" (rje.org directly read); removed a false-confidence "$100" submission fee (Wiley 402, snippets conflict $100/$200) from 5 spots and flagged honestly. flags 10 -> 10 |
| 2026-06-20 | MISQ / JOM / JME source-map refresh | done | EICs confirmed/corrected (MISQ Sue Brown; JOM Bendoly+Oliva; JME co-EiCs Aruoba+Swanson); blocked-domain facts flagged honestly. MISQ flags 11 -> 21 (Cloudflare-blocked domain, added honest caveats), JOM 11 -> 9, JME 11 -> 12. 0 warnings each |
| 2026-06-20 | GEB / JMR / Operations Research source-map refresh | done | GTS/SAGE/INFORMS facts verified; JMR 10 -> 6, OR 10 -> 7, GEB 10 -> 11 (honest AI-heading flag). Editors: GEB Moulin; JMR Hamilton (+incoming Thomadsen 2026-29); OPRE Amy Ward. 0 warnings each |
| 2026-06-20 | Concurrency note | n/a | A second agent ran in parallel this session: a large Phase-2 expansion (psych/socio/anthro/law/geography review packs, repo grew toward 2987 skills / 200 packs) plus its own "economics and marketing source maps" refresh (incl. JEG). One `index.lock` collision occurred; Lane-A commits were scoped per-pack with lock-retry. Push deferred until the expansion lane commits its EXPECTED_* tripwire + root-README reconciliation (audit_repo currently fails at HEAD on counts only) |
| 2026-06-21 | High-debt source-map closure | done | Cleared every `source_map_audit.py --json` entry with unresolved_flags >= 7 by rewriting the highest-risk official source maps into verified-fact plus bounded live-check form; `python3 tools/source_map_audit.py` -> 183 maps, 0 warnings, highest unresolved now 6 |
| 2026-06-21 | README REAP-only check | done | `rg -ni "sccei|stanford center.*china|china.*economy.*institutions|economy.*institutions|center on china" README.md README.en.md` returned no matches; REAP links remain intact |
| 2026-06-21 | JEP low-tail code capability kit | done | Added `Journal-of-Educational-Psychology-Skills/resources/code/` R skeletons for cluster diagnostics, multilevel/growth models, mediation, and JARS tables; `quality_scorecard.py --top 10 --show-skills` -> min 90.0, below 86/88/90 = 0/0/0; `source_map_audit.py Journal-of-Educational-Psychology-Skills --all` -> 0 warnings; local `Rscript` unavailable |
| 2026-06-21 | README full-discipline coverage map | done | Expanded the bilingual README tagline and Coverage at a Glance from a compressed 5-block summary into the full discipline map: multidisciplinary/cross-field, economics/management, social sciences, humanities, math/physical, life sciences, medicine/health, engineering/technology, CS/AI, agriculture/environment/earth, and sport science; stale `five blocks` wording removed |
| 2026-06-21 | Non-breadth clone-risk differentiation | done | Added venue-specific revision/analysis ledgers to AREcon, ARSoc, American Anthropologist, and Current Anthropology high-similarity skill pairs; `clone_audit.py --threshold 0.75 --fail-threshold 0.90 --top 30` now reports only Computer-Science-Conference-Skills breadth-profile pairs above 0.75 |
| 2026-06-21 | Current Anthropology source-map debt cleanup | done | Reworked CA official-source map around directly readable Wenner-Gren pages plus UChicago official URL/snippet anchors, removed the non-official Wikipedia dependency, and preserved live-browser re-check boundaries for UChicago policy facts; `source_map_audit.py Current-Anthropology-Skills --all` -> unresolved_flags 6 -> 0, 0 warnings |
| 2026-06-21 | Annual Review of Sociology source-map debt cleanup | done | Reworked ARSoc official-source map around Annual Reviews official URL/snippet anchors, removed Wikipedia/secondary-JCR dependence, kept live-browser checks for editor roster, delivery specs, S2O, and impact metrics; `source_map_audit.py Annual-Review-of-Sociology-Skills --all` -> unresolved_flags 6 -> 0, 0 warnings |
| 2026-06-21 | Low-tail 90-floor: no-code declarations | done | Second lane (this session): 5 review/theory/law packs scored 84.0 because their resources README explained "no code" with phrasing the scorecard's backtick-stripped `NO_CODE_MARKERS` could not match. Rephrased HLR, Progress-in-Human-Geography, ARSoc, Annual-Review-of-Psychology, Perspectives-on-Psychological-Science to "does not vendor a `code/` kit" → all 5 now 94.0 (`code_status: not_applicable`). Committed 64218536 |
| 2026-06-21 | Low-tail 90-floor: empirical-psych code kits | done | Authored real, venue-specific **R** code kits (README + 5 scripts each) for Cognitive-Psychology (crossed (G)LMM, formal model comparison + parameter/model recovery, SDT + EZ-diffusion, hierarchical-Bayes brms + LOO) and Journal-of-Applied-Psychology (CFA + measurement invariance, ICC/r_wg aggregation, multilevel mediation with MC/bootstrap CI, artifact-corrected psychometric meta). Both 84.0 → 94.0. Committed f41eaddc, f10b4a60 |
| 2026-06-21 | Code kits verified end-to-end (R 4.5.2) | done | Corrects the earlier "Rscript unavailable" note — `Rscript` **is** present (R 4.5.2). Installed lavaan/semTools/lmerTest/emmeans/effectsize/mice/brms+rstan/loo and ran every script in both new kits to completion (brms model converged Rhat≈1.00, all Pareto-k good; CFA CFI=1.00; invariance χ²-diff n.s.). Also read-only re-ran the concurrent lane's JEP kit — solid. Committed 902a06ab |
| 2026-06-21 | Two-lane convergence + floor restored | done | Two parallel agents independently took the low-tail floor task and avoided collision by skipping each other's packs (this lane: 5 no-code + Cognitive + JAP; other lane: JEP kit + README discipline map + clone differentiation). Combined result: `quality_scorecard.py` -> mean 93.3, **min 90.0, below 86/88/90 = 0/0/0**; `audit_repo.py` passes 2883/193/200 (the original push blocker — tripwire/count mismatch — is resolved) |
| 2026-06-21 | Monthly uplift dashboard automation | done | Added `tools/monthly_uplift_report.py` plus `tools/README.md` documentation so the month-long lane has one read-only Markdown/JSON health snapshot. Live report: 2883 skills / 193 packs / 200 root entries; scorecard mean 93.3, min 90.0, below 90 = 0; source-map/root warnings = 0/0; clone max reported 0.788 with 0 fail-threshold hits. |
| 2026-06-21 | CS breadth sibling-routing differentiation | done | Added asymmetric routing guidance to the STOC/FOCS, PLDI/POPL, and NDSS/USENIX Security profiles. `clone_audit.py --bundle Computer-Science-Conference-Skills --threshold 0.75 --fail-threshold 0.90 --top 40` now drops those three previously top-risk sibling pairs from the >=0.75 report; max reported pair moved from 0.788 to 0.785 with 0 fail-threshold hits. |
| 2026-06-21 | Monthly report untracked-file visibility | done | Tightened `tools/monthly_uplift_report.py` to call `git status --short --branch --untracked-files=all`, so the health snapshot cannot miss new untracked scripts under a local `status.showUntrackedFiles` setting. `python3 tools/monthly_uplift_report.py --skip-clone` now shows `tools/monthly_uplift_report.py` as untracked while it remains unpublished. |
| 2026-06-21 | CS breadth clone-risk second pass | done | Added venue-specific routing detail for CHIL/CPAIOR, VRST/ESEM, KDD/ICAPS, BMVC/3DV, and CHI/DIS. `clone_audit.py --bundle Computer-Science-Conference-Skills --threshold 0.75 --fail-threshold 0.90 --top 40` moved the max reported breadth-pair score from 0.785 to 0.779 with 0 fail-threshold hits. |
| 2026-06-21 | CS breadth clone-risk third pass | done | Added routing boundaries for AISTATS/UAI, MobiCom/MobiSys, and RecSys/SOSP. `clone_audit.py --bundle Computer-Science-Conference-Skills --threshold 0.75 --fail-threshold 0.90 --top 40` moved the max reported breadth-pair score from 0.779 to 0.777 with 0 fail-threshold hits. |
| 2026-06-21 | CS breadth clone-risk fourth/fifth pass | done | Added venue-specific routing boundaries for SIGMETRICS/HotNets, WiSec/HPDC, CoLLAs/AutoML, MLSys/AAMAS, SIGGRAPH/SIGGRAPH Asia, MODELS/WSDM, CASE/RO-MAN, SIGDIAL/FAST, Eurographics/Pacific Graphics, ICMR/ISBI, PPoPP/FAST, INLG/*SEM, CCS/IEEE S&P, and NSDI/OSDI. `clone_audit.py --bundle Computer-Science-Conference-Skills --threshold 0.75 --fail-threshold 0.90 --top 40` moved the max reported breadth-pair score from 0.777 to 0.771 with 0 fail-threshold hits; `quality_scorecard.py --top 5 --show-skills` kept min score at 90.0. |
| 2026-06-21 | CS breadth clone-risk sixth pass | done | Added routing boundaries for TEI/UbiComp/SIGACCESS, ICDE/ICPR/K-CAP/ISWC, I3D/IEEE VR, ASE/RE, KR/RAID, HCOMP/ISS, IUI/MobileHCI, and HPCA/ISCA/ASPLOS/SC. `clone_audit.py --bundle Computer-Science-Conference-Skills --threshold 0.75 --fail-threshold 0.90 --top 40` moved the max reported breadth-pair score from 0.771 to 0.766 with 0 fail-threshold hits; `quality_scorecard.py --top 5 --show-skills` kept min score at 90.0. |
| 2026-06-21 | CS breadth clone-risk seventh pass | done | Added routing boundaries for ISER/ISRR, ACSAC/ESORICS/PETS/FC, EuroVis/AVI/IEEE VIS, CoNEXT/SIGCOMM, ISSTA/SANER/ICSME, AsiaCCS/FC, ICDM/SDM, ECCV/ICCV, ICLR/ICML, CHIIR/ECML PKDD/CSCW, AAAI/IJCAI, and ICRA/IROS. `clone_audit.py --bundle Computer-Science-Conference-Skills --threshold 0.75 --fail-threshold 0.90 --top 40` moved the max reported breadth-pair score from 0.766 to 0.763 with 0 fail-threshold hits; `quality_scorecard.py --top 5 --show-skills` kept min score at 90.0. |
| 2026-06-21 | CS breadth clone-risk eighth pass | done | Added the final routing boundaries for ACCV/WACV, ICFP/CAV, SIGMOD/VLDB, LICS/MSR, Humanoids/RoboCup/DARS, OOPSLA/LREC-COLING, SLT/INTERSPEECH/TREC, SCA/COLING, CP/SAT, AIES/FAccT, EuroSys/INFOCOM, and CoNLL/EMNLP. `clone_audit.py --bundle Computer-Science-Conference-Skills --threshold 0.75 --fail-threshold 0.90 --top 40` now reports **no pairs at or above 0.750**; `quality_scorecard.py --top 5 --show-skills` kept min score at 90.0. |
| 2026-06-21 | Global clone-risk 0.75 clearance | done | Added discipline-specific editor-strategy boundaries to the remaining AREcon/ARSoc role pair after the CS breadth cleanup. `clone_audit.py --threshold 0.75 --fail-threshold 0.90 --top 30` now reports **no pairs at or above 0.750** across 2883 first-party skills / 344 comparison groups; `quality_scorecard.py --top 5 --show-skills` kept min score at 90.0. |
| 2026-06-21 | Monthly report readiness triage | done | Upgraded `tools/monthly_uplift_report.py` from a static snapshot into a live readiness dashboard: it now reports OK/Review status for score floor, source-map warnings, root-card warnings, clone fail threshold, and dirty working tree review, then generates next-batch suggestions from current metrics. `python3 -m py_compile tools/monthly_uplift_report.py` passed; `python3 tools/monthly_uplift_report.py --json --skip-clone` parsed cleanly; full report now recognizes clone audit as a regression gate because reported pairs are 0. |
| 2026-06-21 | JMR source-map reliability refresh | done | Re-verified JMR against the live SAGE MRJ author-instructions page, AMA submission/editorial/transparency pages, AMA masthead/transition page, and the official SAGE 2026 Choice price-list workbook. Updated the official source map plus the JMR submission/review-process skills to resolve optional OA APC and routing-chart caveats honestly. `python3 tools/source_map_audit.py Journal-of-Marketing-Research-Skills --all` -> unresolved_flags 6 -> 0, 0 warnings. |
| 2026-06-21 | AMR source-map reliability refresh | done | Re-verified AMR against the live AOM journal page, author resources, editorial-team page, style-guide PDF, and AOM AI policy. Updated the official source map plus AMR submission/workflow/writing-style resources to replace stale APA-edition/portal/abstract/AI caveats with verified AOM Style Guide, ScholarOne, no-fee, editor-team, 200-word abstract, and AI-disclosure facts while keeping manuscript length and acceptance-rate boundaries honest. `python3 tools/source_map_audit.py Academy-of-Management-Review-Skills --all` -> unresolved_flags 5 -> 0, 0 warnings. |
| 2026-06-21 | Monthly report claims-aware triage | done | `tools/monthly_uplift_report.py` now reads `.maintenance/CLAIMS.md`, labels claim-sensitive score-floor and source-map candidates, and avoids recommending them as next unclaimed batches. `python3 -m py_compile tools/monthly_uplift_report.py` passed; `python3 tools/monthly_uplift_report.py --json --skip-clone` parsed cleanly; live report marks all current bottom-band and top source-map candidates as claim-sensitive, so the next safe batch should be tooling or owner-cleared content work. |
| 2026-06-21 | Monthly report expanded candidate view | done | Added `--limit N` to `tools/monthly_uplift_report.py` so maintainers can expand the low-score/source-map/clone candidate tables without changing audit thresholds. The claims scan now also checks nearby `.maintenance/CLAIMS.md` prose, which correctly marks `PMLA-Skills` as awaiting-review lane work when using `--limit 12`. `python3 -m py_compile tools/monthly_uplift_report.py` passed; `python3 tools/monthly_uplift_report.py --skip-clone --limit 12` passed; invalid `--limit 0` exits with an argument error. |
| 2026-06-21 | Monthly report full-pool candidate triage | done | `tools/monthly_uplift_report.py` now builds an `Unclaimed Candidate Pool` from the full `quality_scorecard.py --json` and `source_map_audit.py --json` outputs, not just the displayed top rows. It filters active/queued/awaiting-review claims before suggesting score or source-map follow-ups; `--limit` controls both visible tables and pool size. `python3 -m py_compile tools/monthly_uplift_report.py` passed; `python3 tools/monthly_uplift_report.py --json --skip-clone --limit 8` parsed cleanly and no longer suggests claim-sensitive ASQ or Progress-in-Human-Geography rows. |
| 2026-06-21 | Source-map verification (WebSearch lane) — flags 6/5 tier | done | Re-verified the highest-debt source maps against official pages and reduced them: Econometrica 6→5 (single-anonymous + title-page affiliations; added 2024–25 Editors' Report + verified 9mo/15mo timing), Econometric Theory 6→3 (ScholarOne mc.manuscriptcentral.com/econ-theory from 2026-01-28; cover-letter optional; no fee on official pages), Review of Financial Studies 6→2 (official SFS stats: acceptance 7.27%, first-decision median 30d/mean 34d, 18-month resubmission; flagged likely fee rise ~$400/$460), Perspectives on Psychological Science 6→4 (APA 7th; Open-Practice badges discontinued 2024-01-01 → mandatory transparency statement), Sociological Theory 6→5 (editor Iddo Tavory, NYU; 2027 transition), AEJ:EP 5→4 (Feb 2009 launch), AMJ 5→4 (no membership gate). Each `source_map_audit.py <pack> --all` → 0 warnings. Commits c9ba14f8/aba51ed7/042cd66b/be13f217/7e07c342/408a572a. |
| 2026-06-21 | Source-map verification (WebSearch lane) — flags=4 econ/finance | done | Verified editors/fees/portals and narrowed template maps to 3 flags each: JMCB ($150/$200 fee; OA APC $3,990), IER (editor Dirk Krueger; $150 fee), JUE (Baum-Snow+Behrens), JRU (W. Kip Viscusi), World Development (Arun Agrawal; OA APC $4,750), Research Policy (SPRU distributed team), JHE (multi-editor board), JEEM (von Haefen+Lange), plus JEBO/JIMF/Economic Policy/IMF-ER; Wave A: WBER (Edmonds+Pavcnik), JLE (**$100 fee from 2026-05-01**), JLEO (Andrea Prat), Journal of Economic Geography (5 EICs), **Experimental Economics (publisher moved Springer→Cambridge, 2025)**, INFORMS-JoC (Smith term ended 2025). Commits 1e3fe45c/bceee1f6/3ad64ac6/732f0e03/0844ab34. |
| 2026-06-21 | Source-map verification (WebSearch lane) — flags=4 mgmt/marketing | done | JAIS (Monideepa Tarafdar; AIS Green OA), JMIS (Vladimir Zwass), Organization Studies (Meyer+Quattrone), Journal of Management Studies (General Editors Fortwengel/Post/Potočnik), JAMS (Charles+Stephanie Noble), RAS ($500 submission fee), Journal of Management (Devers through 2026-06), HRM (Wiley co-EiC team), Financial Management (Goldstein/Kahle/Thomas), ETP (Johan Wiklund), JCP (Wooten→Bagchi 2027), AoM Annals (Cronin+George, proposal-first), Annual Review of Economics (Aghion/Rey/Besley), JFM (Lehmann/Seppi/Subrahmanyam), SMJ (current Co-Editors + Research Exchange + 54-day median). Commits c6fb0064/196c6f07/9416ac4a/4e669b8c. |
| 2026-06-21 | Source-map residual assessment (WebSearch lane) | done | Net effect: `source_map_audit.py` flags≥4 reduced 51→18, 0 warnings, flags=6 now 1. The remaining 18 are honest-by-design and intentionally left flagged: 6 Chinese packs (JWE, Sociological-Studies, JMSC, China-Industrial-Economics, China-Rural-Economy, CEQ) whose residual 待核实 are CNKI/官网《投稿须知》 formatting details (中图分类号/JEL/引用体例) plus a 403-blocked official site — US-only WebSearch cannot verify these, so forcing them would risk fabrication; and 12 English packs at an honest floor where residual flags are legend/section-header boilerplate, publisher 403 pages, or facts the publisher does not publish (e.g., JFE acceptance rate, review-journal current editors). Per the anti-cheat rules these stay flagged. `run_checks.py --skip-reports` → all hard checks passed; `audit_repo.py` → 2883/193/200. |
