---
name: jeea-tables-figures
description: Use when building or revising tables and figures for a Journal of the European Economic Association (JEEA) manuscript so exhibits read clean for a general-interest audience and respect JEEA house norms. Shapes exhibits; it does not change the underlying estimates.
---

# Tables & Figures (jeea-tables-figures)

## When to trigger

- Tables are dense, over-decorated, or still carry significance asterisks
- A figure is the better vehicle for the headline result but you are leading with a table
- Notes are missing the sample, units, inference, or estimator
- Exhibits are dumped at the end rather than supporting the argument

## The JEEA exhibits bar

JEEA is **general interest**, so exhibits must be legible to an economist outside the subfield: the **headline result should be readable from one table or one figure** with its note alone. JEEA follows the standard modern-economics presentation discipline — **report standard errors / confidence sets, not significance asterisks or boldface for significance** — and the final accepted version is copyedited to OUP house style, so do not over-format the submission. Lead with the exhibit that carries the claim; everything else supports it.

## Table craft

- **Three-line tables** (`booktabs`): top/mid/bottom rules only; no vertical rules, no shading for emphasis.
- **No significance stars.** Report point estimate and **standard error (or confidence set)** beneath it; never `***`/`**`/`*` or boldface to denote significance.
- **Self-contained notes:** sample and period, unit of observation, dependent variable and units, estimator, inference (clustering level), and the number of observations/clusters.
- **One claim per table.** The main table should let a reader recover the headline magnitude and its uncertainty without the text.
- **Structural fit tables:** show targeted vs. untargeted moments (data vs. model) so identification is visible.

## Figure craft

- **Event-study plots** with confidence bands and a visible pre-period (flat leads = the parallel-trends evidence).
- **Model-fit overlays** (data vs. simulated moments) and **counterfactual curves with uncertainty bands** for structural work.
- **Vector output** (`.eps`/`.pdf`) preferred for final files; raster at ≥300 dpi; readable axis labels and units; colorblind-safe palettes; no chartjunk.
- Prefer a figure over a table when the **shape** of the result (dynamics, heterogeneity, distribution) is the point.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JEEA is a general-interest European economics flagship; credible identification across applied fields.

- **Tables:** `etable` (multi-model) or `did_summary_to_latex` straight from the `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] No significance asterisks or boldface-for-significance anywhere
- [ ] Standard errors / confidence sets reported beneath estimates
- [ ] Each table/figure note is self-contained (sample, units, estimator, inference, N)
- [ ] Headline result recoverable from one exhibit + its note
- [ ] Event-study / fit / counterfactual figures carry uncertainty bands
- [ ] Three-line tables; vector figures at publication quality
- [ ] Exhibits support the argument in-text, not dumped at the end

## Exhibits by paper type

- **Applied micro / development:** lead with the event-study figure (dynamics + parallel-trends evidence) or a single main-effect table; relegate the specification grid to the online appendix.
- **Theory:** a figure of the key comparative static or a numerical example can make an abstract proposition concrete; do not over-tabulate.
- **Structural / quantitative:** a model-fit table (targeted vs. untargeted moments) plus a counterfactual figure with uncertainty bands; a parameter-estimate table with standard errors.
- **Macro / finance:** impulse-response or factor figures with confidence bands; avoid factor-zoo tables no generalist can parse.

## Worked vignette (illustrative)

A draft reports the main result in a 9-column regression table with three rows of asterisks and bolded coefficients. A general-interest referee cannot find the headline number. The JEEA-grade fix: move seven columns to the online appendix, keep the two that carry the claim, replace asterisks with the point estimate and its standard error in parentheses, and add a self-contained note (sample, period, unit, dependent variable in levels, clustering at the state level, N and number of clusters). The headline magnitude is now readable from the table alone — and the event-study figure, promoted to the main text, shows the dynamics the table cannot.

## Anti-patterns

- Significance stars or bolded "significant" coefficients (against JEEA house norms)
- A table no one can read without hunting through three paragraphs of text
- Notes missing the clustering level, units, or sample definition
- Leading with a regression table when an event-study figure tells the story better
- Over-formatting to mimic the typeset journal style the copyeditor will apply anyway
- Counterfactual or fit figures with no uncertainty representation
- A factor-zoo or specification-grid table dumped in the main text with no headline exhibit

## Output format

```
【Headline exhibit】[table N / figure N] — recoverable from its note? [Y/N]
【Significance display】SEs/CIs only, no asterisks? [Y/N]
【Notes complete】sample/units/estimator/inference/N? [Y/N]
【Figures】event-study / fit / counterfactual with bands? [Y/N]
【Next step】jeea-writing-style
```
