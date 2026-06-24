---
name: aeri-tables-figures
description: Use when building or trimming the exhibits of an American Economic Review: Insights (AER: Insights) short-format manuscript to the hard five-exhibit budget, one page each, no significance asterisks. Designs the minimum exhibit set; it does not run the analysis behind them.
---

# Tables & Figures — Five-Exhibit Budget (aeri-tables-figures)

## When to trigger

- The draft has more than five figures-plus-tables
- An exhibit spills past one page, or carries significance asterisks/boldface
- Each exhibit costs 200 words of your text budget and you must choose
- The central result is buried in a dense multi-panel table

## The AER: Insights exhibit constraints (检索于 2026-06；以官网为准)

- **Maximum five exhibits** (figures or tables combined). Manuscripts over the limit are **returned unreviewed**.
- **Each exhibit is limited to one page.**
- **Each exhibit subtracts 200 words** from the main-text allowance (7,000 with zero exhibits → 6,000 with five). So every exhibit must out-earn 200 words of prose.
- **AEA house style:** report standard errors / confidence sets; **no asterisks or boldface to denote significance** (an AEA-wide convention). Notes state the estimator, sample, clustering, and units.

## Budgeting the five slots

Choose the exhibit set that, together, tells the single-insight story. A common allocation for an empirical short paper:

| Slot | Typical content |
|------|-----------------|
| 1 | The **headline result** — the one figure or table a reader remembers (event-study, RD plot, treatment-effect estimate) |
| 2 | The **central identification diagnostic** (pre-trend leads, density, first-stage, balance) |
| 3 | A **mechanism or key heterogeneity** exhibit, if it is part of the single insight |
| 4–5 | Held in reserve — a robustness summary or a descriptive table only if load-bearing |

If two exhibits can merge into one well-designed multi-panel page, merge them and reclaim a slot (and 200 words). Everything else goes to the Supplemental Appendix.

## Design rules

- **The headline exhibit must be self-reading** — a reader who sees only it should grasp the insight.
- **Figures over tables** where a figure communicates the magnitude faster (AER: Insights papers lean visual).
- **One page each, legible at print size**; no microscopic multi-panel grids spilling over.
- **Notes carry the inference** since there are no asterisks: report point estimates with SEs / 95% confidence sets in the cell or note.
- **Units and signs explicit**; the magnitude, not just the sign, is the point.

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
## Checklist

- [ ] **≤5 exhibits total**; each **≤1 page**
- [ ] Word budget reconciled: 7,000 − 200×(#exhibits) ≥ main-text length
- [ ] Exhibit 1 is the **self-reading headline**; exhibit 2 the identification diagnostic
- [ ] **No significance asterisks/boldface**; SEs / confidence sets shown
- [ ] Notes state estimator, sample, clustering, units
- [ ] Non-essential exhibits moved to the Supplemental Appendix
- [ ] Mergeable exhibits combined to reclaim a slot where sensible

## Anti-patterns

- A sixth exhibit (auto-return) or an exhibit that runs to two pages
- Significance asterisks or boldface for significance
- A dense table where a single figure would land the magnitude
- Spending an exhibit slot (and 200 words) on a descriptive table that prose covers
- A headline exhibit that needs the text to be intelligible

## Output format

```
【Exhibit count】__ / 5 (each ≤1 page?)
【Word reconciliation】7000 − 200×__ = __ words available; draft = __ words
【Exhibit 1 (headline)】<self-reading result>
【Exhibit 2 (identification)】<diagnostic>
【Exhibits 3–5】<mechanism / robustness / descriptive — only if load-bearing>
【No-asterisk check】SEs / CIs in notes? [Y/N]
【To the appendix】<exhibits demoted>
【Next step】aeri-writing-style
```
