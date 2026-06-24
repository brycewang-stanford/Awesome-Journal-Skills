---
name: jm-tables-figures
description: Use when building the tables and figures for a Journal of Marketing (JM) manuscript — exact-statistic result tables, interaction/mechanism plots, and managerial-takeaway exhibits in AMA house style, all counting against the 50-page limit. Finalizes exhibits; it does not run the analysis (jm-data-analysis) or polish the prose (jm-writing-style).
---

# Tables & Figures, AMA Style (jm-tables-figures)

## When to trigger

- Results are settled and exhibits need to be built or cleaned up
- Tables show stars only, with no exact p-values, standard errors, or effect sizes
- A figure could carry the managerial takeaway better than a paragraph
- You are over the 50-page limit and exhibits are part of the budget

## JM reporting carries into the exhibits

JM's statistical-transparency mandate is not just a text rule — it governs every table. Result tables must show **actual p-values** (not "p < .05" or stars alone), **standard errors**, and **effect sizes / magnitudes**. A reader should be able to judge the *substantive* importance of an effect from the table, because JM evaluates managerial relevance, not significance counts. Prefer reporting coefficients with SEs and exact p-values, and add a column or note giving the effect in interpretable units (elasticity, lift, WTP, welfare) wherever feasible.

## Mind the 50-page budget

JM enforces a **50-page maximum** that is **inclusive of** title, abstract, keywords, text, footnotes, references, tables, figures, and print appendices; only **web appendices** are excluded. Every table and figure therefore spends pages. Design exhibits to earn their space: consolidate redundant tables, move secondary results to a web appendix, and ensure each remaining exhibit answers a question a reviewer or manager actually asks.

## What each exhibit type should do

- **Descriptives / correlation table**: sample composition and construct relationships at a glance; reliabilities on the diagonal where multi-item scales are used.
- **Main results table(s)**: coefficients, SEs, exact p-values, effect sizes; clearly labeled models/specifications; the identification design legible from the table.
- **Interaction / mechanism figure**: simple-slopes or marginal-effects plot for moderation; a mediation diagram with indirect-effect estimates and CIs for process.
- **Managerial-takeaway exhibit**: a figure that converts the result into a decision-relevant quantity (e.g., predicted sales/CLV across a manipulated lever) — this is where JM's dual mandate shows in the exhibits.
- **Study-design / conceptual figure**: a clean model or multi-study roadmap when it aids comprehension.

## AMA house-style essentials

- Author-date conventions in notes; consistent decimal places; defined abbreviations.
- 12-point font; tables and figures may be single-spaced; 1-inch margins; **no** page numbers, line numbers, headers, or footers in the file.
- Each exhibit **self-contained**: a title, complete notes (N, estimator, SE type, significance reporting), and units, readable without the text.
- Number consistently and reference every exhibit in the text in order.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-appendix drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JM is empirical marketing — field experiments, panel/CRM data, and quasi-experiments; randomization inference for experiments, DiD / IV for observational claims.

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the effect size in
  interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Tables report exact p-values, SEs, and effect sizes (no stars-only)
- [ ] At least one exhibit conveys the managerial magnitude in real units
- [ ] Interaction plotted; mediation shown with indirect effects + CIs
- [ ] Each exhibit self-contained (title, full notes, N, estimator, units)
- [ ] Redundant tables consolidated; secondary results moved to web appendix
- [ ] Total exhibits fit within the 50-page inclusive budget
- [ ] AMA formatting: 12-pt, no page/line numbers/headers/footers

## Anti-patterns

- **Stars-only tables** with no exact p-values, SEs, or magnitudes.
- **Significance without managerial meaning** — no units a decision maker reads.
- **Exhibit bloat** that pushes the manuscript over 50 pages.
- **Non-self-contained exhibits** that require the text to interpret.
- **Inconsistent numbering / undefined abbreviations.**

## Output format

```
【Tables】exact p / SE / effect size present? specifications labeled?
【Managerial exhibit】magnitude in real units shown? where ...
【Interaction/mediation】simple slopes / indirect-effect plot present?
【Self-containment】titles + full notes + units complete?
【Page budget】exhibits fit 50-page inclusive limit? web appendix used?
【AMA format】12-pt, no page/line numbers/headers/footers: ok?
【Next step】jm-writing-style
```
