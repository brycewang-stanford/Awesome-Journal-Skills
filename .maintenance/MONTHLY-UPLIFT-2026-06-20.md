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
