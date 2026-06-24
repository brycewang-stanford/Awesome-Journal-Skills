---
name: tar-tables-figures
description: Use when building or cleaning the exhibits for a The Accounting Review (TAR) manuscript — descriptive, correlation, and regression tables, event-study and discontinuity figures, experimental cell means, and analytical-model exhibits in Chicago house style and within the page budget. Finalizes exhibits; it does not run the analysis (tar-data-analysis) or polish prose (tar-writing-style).
---

# Tables & Figures (tar-tables-figures)

## When to trigger

- Tables are cluttered, inconsistent, or not self-explanatory without the text
- You need the standard archival table set (descriptives, correlations, main regression)
- You are presenting a DiD/event study or RDD and need the right figure
- The exhibit count is pushing the 55-page initial limit
- A reviewer says "I cannot read the table" or "what is the economic magnitude?"

## TAR exhibit conventions

TAR follows **The Chicago Manual of Style (16th ed.)** for citations and references and the AAA
Manuscript Preparation Guide for layout (12-pt Times New Roman, double-spaced, 1-inch margins,
serially numbered pages). Remember the **55-page initial limit includes tables, figures, and
appendices** — so every exhibit must earn its space; move secondary results to an online appendix.
Each table must be **self-contained**: a reader should understand it without the text.

## The standard archival table set

1. **Sample selection** — a stepwise screen from the raw database population to the final N, so the
   sample is reproducible (this also supports the data-authenticity requirement).
2. **Descriptive statistics** — N, mean, median, SD, and key percentiles for all variables; note
   winsorization. Define every variable in a clearly labeled variable-definitions appendix.
3. **Correlation matrix** — Pearson (and often Spearman) correlations; flag significance.
4. **Main regression** — coefficients with standard errors (or t-stats) below, fixed effects and
   clustering noted in the table, R-squared/N reported. State the dependent variable in the title.
5. **Cross-sectional / robustness tables** — partitions and alternative specifications.

Report **economic magnitude** in or alongside the table, not just significance stars; state which
standard-error and clustering choice produced the reported inference.

## Figures by design

- **Event study / DiD**: plot event-time coefficients with confidence intervals to show pre-trends
  and dynamics — often the single most persuasive exhibit for identification.
- **RDD**: binned scatter with the fitted discontinuity at the threshold.
- **Experiment**: cell means with error bars for the manipulated factors; show the interaction.
- **Analytical model**: a figure of the comparative static (how the equilibrium quantity moves in a
  parameter), and a clearly labeled timeline of the information structure.

## House-style hygiene

- Consistent decimal places; aligned columns; explicit units.
- Significance convention stated once (e.g., ***/**/* with the tail) and used everywhere.
- Variable names in tables match the text and the definitions appendix exactly.
- Notes beneath each table define abbreviations, sample, period, and SE/clustering.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-appendix drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). TAR is archival accounting — DiD around regulation / standard changes, IV, and earnings-based designs; the corporate-causal chain fits directly.

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the effect size in
  interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Sample-selection table makes the N reproducible
- [ ] Descriptives, correlations, and main regression follow the standard archival set
- [ ] Fixed effects, clustering, N, and fit statistics reported in every regression table
- [ ] Economic magnitude shown, not only significance stars
- [ ] DiD/RDD/experiment/model figures match the design
- [ ] Variable names consistent across tables, text, and the definitions appendix
- [ ] Exhibit set fits the 55-page budget; secondary results moved online

## Anti-patterns

- **Stars-only tables** with no economic magnitude or SE/clustering note.
- **Orphan exhibits** that cannot be read without hunting through the text.
- **Inconsistent variable names** between tables and the definitions appendix.
- **A DiD with no event-time figure** to show pre-trends.
- **Page-budget blowout** from leaving every robustness table in the main body.

## Output format

```
【Table set】sample-selection / descriptives / correlations / main / robustness — complete? yes/no
【Regression tables】FE, clustering, N, fit reported? magnitude shown? yes/no
【Key figure】event-study / RDD / cell-means / comparative-static — matches design? yes/no
【Variable definitions】appendix present and consistent? yes/no
【Page budget】within 55 pages incl. exhibits? overflow → online appendix
【Next step】tar-writing-style
```
