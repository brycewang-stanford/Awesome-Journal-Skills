---
name: jar-tables-figures
description: Use when finalizing the descriptive, results, and identification exhibits for a Journal of Accounting Research (JAR) manuscript — the summary-statistics table, correlation matrix, main regression tables, and identification plots that an empirical-archival accounting paper lives or dies on. Builds the exhibits; it does not run the estimation (jar-data-analysis) or polish prose (jar-writing-style).
---

# Tables & Figures (jar-tables-figures)

## When to trigger

- Tables are cluttered, inconsistent, or not self-explanatory
- A referee cannot tell the sample, units, or SE clustering from the table notes
- You need the standard JAR exhibit set assembled in house style
- Identification needs a figure (pre-trends, RD plot) to be believed

## The standard JAR exhibit set

An empirical-archival JAR paper is read through its tables. Build, in order:

1. **Sample construction table** — from the raw population to the final N, line by line, with each screen and the observations lost. Referees expect to trace the sample.
2. **Descriptive statistics** — N, mean, SD, and key percentiles for every variable; state winsorization (e.g., 1/99%).
3. **Correlation matrix** — Pearson (and often Spearman) among the main variables; flag significance.
4. **Main results** — the central regression(s): coefficients with t-/z-stats or standard errors beneath, the **SE clustering stated in the note**, fixed effects indicated, and N and R² (or pseudo-R²) reported.
5. **Identification & robustness** — first-stage (IV), DiD dynamics, RD estimates, falsification/placebo, alternative measures, and cross-sectional (channel) partitions.

## House-style discipline

JAR uses a custom author-date house style; match the **typographic conventions of recent JAR articles** rather than importing a reference manager's defaults. For exhibits specifically:

- **Self-contained**: a title, the sample/period, the units, and the dependent variable are clear from the table and its note alone.
- **Inference visible**: report what is beneath the coefficients (t-stats / SEs) and **state the clustering** in the note; mark significance consistently.
- **Variable definitions**: every variable defined (often an appendix variable-definitions table) with its data source (Compustat/CRSP/I/B/E/S/Audit Analytics/EDGAR).
- **Numbers consistent**: Ns, coefficients, and signs match the text; decimal places consistent.

## Figures that earn their place

Use figures where they do identification work a table cannot: **DiD event-study plots** (coefficients by period with confidence bands, showing flat pre-trends), **RD plots** (binned means around the cutoff), and time series of the treatment/setting. Avoid decorative charts; every figure should support the causal claim.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-appendix drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JAR is archival/empirical accounting; foreground identification around disclosure and regulation shocks, with modern DiD where adoption is staggered.

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the effect size in
  interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Sample-construction table traces raw population → final N
- [ ] Descriptives with winsorization stated; correlation matrix included
- [ ] Main table reports coefficients, inference statistics, FE, N, R²
- [ ] **SE clustering stated in every regression-table note**
- [ ] Variable-definitions table with data sources included
- [ ] Identification figure (pre-trends / RD) present where the claim is causal
- [ ] All numbers reconcile with the text; formatting matches recent JAR articles

## Anti-patterns

- **Mystery samples**: a final N with no construction table.
- **Naked coefficients**: no SEs/t-stats and no clustering note.
- **Reference-manager defaults** instead of JAR house style.
- **Decorative figures** that do no identification work.
- **Undefined variables** or sources scattered through the text.

## Output format

```
【Exhibit set】sample / descriptives / correlations / main / robustness present?
【Inference shown】t-stats or SEs + clustering stated in notes?
【Variable definitions】table with sources included?
【Identification figure】pre-trends / RD plot present where causal?
【Consistency】Ns and coefficients reconcile with text?
【House style】matches recent JAR articles?
【Next step】jar-writing-style
```

## Resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official JAR/Chicago Booth/Wiley URLs (accessed 2026-06-01)
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — exhibit-export tooling (estout / outreg2 / modelsummary) and data sources
