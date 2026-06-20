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
| Highest unresolved source maps | American Anthropologist, New Media & Society, AER Insights, AJPS, Journal of Labor Economics |
| `tools/clone_audit.py --threshold 0.75 --fail-threshold 0.90 --top 40` | no fail-threshold hits; top risks are Science/PNAS rebuttal and CS conference breadth pairs around 0.799 |

## Work worth doing

1. **Raise the low-tail breadth floor.** The five breadth packs at 86.0 are
   the main visible quality debt. They need better router guidance, selection
   patterns, source-map discipline, and domain-specific decision tables, not
   generic prose.
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
- Improve the five breadth packs below 90 with router-level decision tables,
  field-specific rejection risks, and official-source/use-case scaffolding.
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
| 2026-06-20 | User-facing maintenance docs | done | `CONTRIBUTING.md`, `tools/README.md`, `README.md`, and `README.en.md` now point maintainers to the count-disciplined monthly quality program and acceptance commands |
| 2026-06-20 | Post-batch acceptance gates | done | `run_checks.py --skip-reports` passed; counts remain 2809 / 183 / 200; scorecard min 89.2; root/source-map warnings 0; clone audit has no 0.90 fail-threshold hits |
