---
name: jfqa-tables-figures
description: Use when building the tables and figures for a Journal of Financial and Quantitative Analysis (JFQA) paper — summary statistics, main regressions, robustness, and finance-standard exhibits with self-contained notes that state sample, clustering, winsorizing, and economic magnitudes. Use to make exhibits readable under double-anonymous review and consistent with JFQA formatting.
---

# JFQA Tables & Figures (jfqa-tables-figures)

Use this skill to design exhibits for a **JFQA** manuscript so a reviewer can read each one standalone and so the file complies with the journal's prescriptive formatting.

## Standard finance exhibit set

- **Table 1 — Summary statistics**: variable definitions, N, means, SDs, key percentiles; note winsorizing/trimming.
- **Correlation matrix** where relevant.
- **Main results table**: the core regressions/sorts, with coefficients, SEs, the clustering dimension, fixed effects listed, and N.
- **Robustness tables**: alternative samples, definitions, FE/clustering.
- **Heterogeneity / mechanism tables**.
- **Figures**: event-study coefficient plots, portfolio-sort patterns, RDD discontinuity plots, time-series of the key series.

## Self-contained notes (required discipline)

Each table/figure note must state: sample and period, unit of observation, what is winsorized, the SE/clustering choice, fixed effects, and how to read the magnitude. A reviewer should not need the text to interpret the exhibit.

## Presentation standards

- Report **economic magnitudes**, not only significance stars; finance referees want effect sizes (bps, monthly alpha, elasticities).
- Number tables/figures and call them out in order.
- Keep figures clean (vector output, legible at print resolution, no chartjunk).

## Formatting compliance

JFQA submissions use **8.5 × 11 paper, 1-inch margins, 12-pt Times New Roman, double-spaced** (body and appendices), in a single **text-searchable PDF**. Ensure embedded exhibits stay legible at these settings and that the PDF remains searchable (no image-only tables).

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-appendix drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md).

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id` — one variable definition, one set of numbers, body and appendix in sync.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering (from the result's diagnostics) and
  states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Anti-patterns

- Tables that require the text to interpret.
- Significance stars with no economic magnitude.
- Undisclosed winsorizing or an unstated clustering choice.
- Image-only exhibits that break the text-searchable-PDF requirement.

## A model JFQA table note, dissected (numbers illustrative)

> Table 3 reports value-weighted monthly returns of decile portfolios sorted on the signal using NYSE breakpoints, July 1973 to December 2023. The sample is CRSP common stocks (share codes 10/11); accounting variables are winsorized at the 1st/99th percentiles and lagged six months. The 10-1 spread is 0.42% per month (t = 2.9, Newey-West with 6 lags), about 5.2% annualized. Alphas are from the five-factor model plus momentum.

Why each clause earns its place: sample and period (replicability), breakpoints and weighting (the two choices that most often flip sort results), winsorizing and lags (data hygiene a JFQA referee will probe), spread with both monthly and annualized magnitude (economic significance), inference method with the lag count (no hidden SE choices), and the benchmark model (so "alpha" is defined). Write every note to this standard and the exhibit survives being read in isolation.

## Result-to-exhibit decision table

| Result type | Exhibit JFQA referees expect |
|---|---|
| Cross-sectional return premium | decile-sort table with 10-1 row, then a Fama-MacBeth table |
| Policy/regulation effect | event-study coefficient figure with CIs, then a group-time ATT table |
| Threshold design | binned scatter at the cutoff plus a bandwidth-robustness table |
| Mechanism claim | split-sample or interaction table keyed to where the channel should bind |
| Headline magnitude | a one-SD / %-of-mean row built into the main table, not buried in text |

## Calibration anchors from the published page

- Recent JFQA empirical papers commonly carry on the order of eight to twelve main-text exhibits, with additional robustness in an Internet Appendix — treat this as a soft anchor from reading recent issues, not a quota, and calibrate within your subfield.
- Internet Appendix exhibits are numbered separately (IA.1, IA.2, ...); the main text must stand alone without them.
- Every exhibit is cited in order of first mention; an orphan exhibit signals padding to a screener already wary of over-long papers.

## Figure craft for quantitative referees

- Coefficient and event-study plots carry confidence intervals and a marked reference period; a point-estimate-only figure invites the inference question all over again.
- Axis labels use finance units (bps, %, $bn), and the scale is chosen so the economic magnitude — not just the shape — is readable.
- Figures must survive grayscale printing and the 8.5 × 11 double-spaced layout without shrinking below legibility.

## Output format

```
【Exhibit list】Table 1...N, Figure 1...M with one-line purpose each
【Notes】each states sample / clustering / winsor / magnitude
【Formatting】fits 8.5x11 / 1-in / 12-pt TNR, PDF searchable
【Next step】jfqa-writing-style
```
