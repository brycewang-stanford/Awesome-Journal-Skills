# ACCEPTANCE-2026-11: pre-submission polishing week (v1.2.0)

**Date:** 2026-11-23 · **Branch:** `presubmission-v1.2` · **Basis:** the one-week plan
"make AJS the best tool for paper pre-submission polishing, no new journals".
**How verified:** every number below is local output from `tools/run_checks.py`,
`tools/preflight.py`, a clean `claude plugin install` into an isolated config directory,
and the benchmark in `showcase/presubmission-benchmark/`.

## 0. Verdict

All seven plan days were delivered; the release itself (push and tag) is owner-run.
`run_checks.py` passes every hard gate. Inventory is unchanged: **4,166 skills / 300 packs
/ 744 venues**, so no new journals and no new skills. Conformance is 300/300.

## 1. Plan vs. delivered

| Day | Plan | Delivered | Evidence |
|---|---|---|---|
| Mon | Green CI; install test; benchmark fixtures | **CI:** the weekly run had been red since 2026-10-12 because the tripwire read a date-decaying score. It now reads `static_score`. **Install:** confirmed shared links were dead for installed users. **Fixtures:** 6 synthetic manuscripts × 12 planted defects | `tools/quality_scorecard.py`, `QUALITY-LANE-2026-09.md` (2026-11-23 revision), `tools/tests/fixtures/manuscripts/` |
| Tue | Preflight engine | `tools/preflight.py` (stdlib only; reads .tex/.md/.docx/.pdf/.txt; 20 check IDs), with 21 unit tests | `tools/tests/test_preflight.py` |
| Wed | Rules for 40 venues + freshness | **46 packs** re-verified against official pages, each with a rules block (585 rules total), plus `venue_rules.py --check`. The 11 due conferences: 8 now current, and the 3 with no published next call (COLM, EMNLP, UAI) correctly stay due. 9 dead links + IMC repaired | `venue-rules.json`, `CYCLE-CURRENCY.md` (86 current · 3 due · 0 stale), `DEAD-LINKS.md` rows |
| Thu | Pipeline + referee depth | `rt-submission-readiness` stages 0–5; `rt-simulated-referee` writes on real review forms with a verifier; `review-forms.md`, `prose-polish.md`, `cover-letter-and-disclosures.md`; preflight pointer in all 290 `*-submission` skills | toolkit skills, `shared-resources/submission-readiness/` |
| Fri | Benchmark + fix loop | **Preflight:** 45/47 mechanical, 0 false alarms on clean controls. **Panel:** 23/24 substantive kept as major, 24/24 raised. Every miss is published | `showcase/presubmission-benchmark/RESULTS.md` |
| Sat | Packaging + first screen | `vendor_shared.py`: 2,047 vendored copies with CI check; preflight ships inside the toolkit. Clean re-install: **0 broken links** (toolkit 113, JF 69). Both READMEs lead with pre-submission. Weekly live-check activated | `.github/workflows/live-check.yml` |
| Sun | Showcase + release | Real preprint (arXiv:2611.21070, CC BY 4.0) run end to end. Five preflight defects found and fixed, including a silent false green on the AEA exhibit cap. CHANGELOG 1.2.0; version set on 300 packs | `showcase/presubmission-real-preprint/`, `CHANGELOG.md` |

## 2. Facts corrected during re-verification (selection)

- Editors-in-chief: 《经济研究》, 《中国工业经济》, 《世界经济》; AER: Insights; AMJ (two stale skills); JMR masthead.
- Review mode:
  - AER: Insights and AEJ: Applied now require anonymized submissions (the AEA RCT);
  - QJE, REStud and Econometrica are not double-blind, contrary to what the packs said.
- Limits:
  - QJE abstract is 250 words;
  - The Lancet: 3,500 words (4,500 for RCTs) and CONSORT 2025;
  - *Science* has merged Reports into Research Articles (3,000 words / 5 items);
  - Marketing Science aims for 40 pages;
  - AMJ is ~40 pages including everything.
- 《世界经济》's limits had been copied from a different journal's page.
- Portals: JPE uses Editorial Manager, SMJ uses Wiley Research Exchange, and JF's checklist named the wrong system.
- AEJ: Applied forbids significance stars; the pack had said they were allowed.

## 3. What is open (carried forward)

- **Publisher sites that block automation:** INFORMS (Management Science, Marketing
  Science), SAGE (ASQ, JM, JMR) and nejm.org / science.org / cell.com refuse automated
  reads. Their blocks hold only what could be read the same day. The weekly live-check
  runs on a GitHub runner and may reach them.
- **Unresolved facts:** by `source_map_audit.py`'s marker count, Strategic Management
  Journal now carries the most (22), then Journal-on-Communications (19) and PNAS Nexus
  (18; the re-check resolved several facts but also logged new live-check items).
- **DAC template:** the archived DAC FAQ says IEEE template while the map says ACM. This
  was found by the dead-link pass and is unverified.
- **Benchmark v2:** fix the "clean" fixture errors the panel found (ACL Yoruba coverage,
  ERJ SE of a difference, JF anticipation window), add real papers with known revisions,
  and run the multi-agent panel configuration.
- **Preflight known limit:** a wrong headline number that coincides with a real number
  elsewhere is invisible to context-free traceability. It is documented, and the panel
  covers it.

## 4. Constraints honoured

- No auto-committing, self-measuring apparatus; no behavioural eval in CI. The panel
  benchmark is hand-run and its outputs are committed (QUALITY-LANE constraints).
- The backlog score is not a target. Only the date-independent tripwire changed.
- No push and no tag were made by the agent; release actions are owner-run.

## 5. Addendum (2026-11-24): second tranche

Done after the owner said "continue". It is on the same branch and not pushed.

- **Rules coverage:** 46 → **94 venues** (48 more packs re-verified; 585 → 1239 rules in
  `venue-rules.json`). Notable corrections are listed in CHANGELOG 1.2.0.
- **Preflight:**
  - `--compare` re-run diff;
  - `references_max` enforcement;
  - Word heading styles resolved through `styles.xml`;
  - two-column PDF detection;
  - eight further PDF-reader fixes.
- **Cross-format benchmark:** source, PDF and Word all reach 45/47 caught with zero
  clean-control false alarms. Before the fixes, the first PDF run had 165 false alarms,
  mostly from one Chinese PDF.
- **Fixture v2:** fixes the clean-fixture errors the panel found (ACL coverage, ERJ
  standard error, JF sample and reference period).
- **Multi-agent panel:** caught the inline panel's one miss (ACL S4), and raised six
  defensible major concerns on the v2 clean JF paper. The protocol now records the
  trade-off.
- **DAC:** moved to 2027. The IEEE/ACM template question is settled: IEEE for 2027.
- **Still open:**
  - Publisher sites that block automation (INFORMS, SAGE, ScienceDirect, cell.com,
    nejm.org, science.org) were read through archives or search rendering. Each map says
    so; the weekly live-check on a GitHub runner should re-read them.
  - Several APC figures are left null where the sources disagree.
