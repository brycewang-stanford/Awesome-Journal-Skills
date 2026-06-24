---
name: jebo-tables-figures
description: Use when a Journal of Economic Behavior & Organization (JEBO) manuscript's exhibits must make a behavioral comparison legible — treatment bar charts, by-round dynamics, distribution plots, regression tables. Builds exhibits that show the mechanism; it does not run the analysis or write the prose.
---

# Tables & Figures (jebo-tables-figures)

## When to trigger

- Treatment differences are buried in a wall-of-coefficients regression table
- A reader cannot see the behavioral effect without reading the surrounding paragraph
- Experimental dynamics (learning over rounds, by-period contributions) are not visualized
- The figure shows means but hides the *distribution* the behavioral story depends on
- You are unsure whether significance markers belong in a JEBO exhibit

## What a JEBO exhibit must do

The reader should see the **behavioral comparison** — treatment vs. control, by group or over time — before reading a word of text. JEBO's experimental core makes a few exhibit types load-bearing:

- **Treatment-comparison plot.** Bar/dot plot of the outcome by treatment with confidence intervals; the headline contrast is the visual focus, not a footnote.
- **Dynamics plot.** For repeated games / multi-round experiments, plot the outcome by period and treatment so learning, decay, or convergence is visible (the round-by-round graph is a JEBO signature).
- **Distribution plot.** Where the mechanism is about heterogeneity (e.g., types, bimodality of contributions), show the full distribution (CDF, histogram, or beeswarm), not just the mean — a difference in means can hide a difference in shape.
- **Regression table.** Used to *support* the figure, with the design-relevant comparison up top, clustered SEs, and pre-registered/primary specification flagged.

## Exhibit decisions by what the result is about

| The behavioral claim is about… | Lead exhibit | Common mistake |
|--------------------------------|--------------|----------------|
| A level difference across treatments | bar/dot plot with CIs | a 6-column table where the contrast is row 4 |
| Change over repeated interaction | by-period line plot per treatment | reporting only the pooled average |
| Heterogeneity / types | distribution / CDF / beeswarm | a single mean hiding bimodality |
| A predicted ordering of arms | ordered plot matching the model's prediction | unordered table that obscures the ranking |
| A structural/behavioral estimate | parameter plot with CIs + fit overlay | a table of parameters with no fit visualization |

## House-style and Elsevier mechanics

- **Confidence intervals over bare asterisks.** Show SEs/CIs; let the reader judge. (Elsevier permits significance stars, but a behavioral comparison is far more persuasive shown as overlapping/non-overlapping intervals; reserve any asterisks for support tables, never as the sole evidence.)
- Self-contained captions: a referee should understand the exhibit without the body text — define treatment, unit, sample, error-bar meaning, and n.
- Figures legible in **grayscale** (Elsevier print) — use patterns/markers, not color alone.
- Report **n per cell** and the unit of observation (subject vs. subject-period vs. session); cluster the inference accordingly.
- Number tables/figures and place near first mention; high-resolution vector figures per Elsevier artwork specs (检索于 2026-06；以官网为准).

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JEBO spans behavioral/experimental and applied micro; randomization inference for experiments, DiD/IV for observational claims.

- **Tables:** `etable` (multi-model) or `did_summary_to_latex` straight from the `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] The headline behavioral comparison is visible in the lead figure before any prose
- [ ] Repeated-interaction results have a by-period plot per treatment
- [ ] Heterogeneity claims show the distribution, not only the mean
- [ ] Confidence intervals shown; significance stars are not the only evidence
- [ ] Captions are self-contained (treatment, unit, n, error-bar definition)
- [ ] Figures readable in grayscale; n-per-cell and clustering level reported
- [ ] Exhibit ordering matches the model's predicted ordering where one exists

## Anti-patterns

- The main treatment effect appearing only as a coefficient in a dense table
- A bar of means concealing a bimodal contribution distribution
- Asterisks doing all the persuasive work with no CIs
- Color-only figures that collapse in grayscale print
- Captions that require the body text to interpret
- Reporting subject-period n as if it were independent subjects (wrong clustering)

## Output format

```text
【Lead exhibit】treatment-comparison / by-period dynamics / distribution / parameter plot
【What it shows at a glance】<the behavioral contrast>
【Inference shown】CIs / SEs (asterisks support-only)
【Unit + n per cell】<subject / subject-period / session>; clustering:
【Grayscale-safe + self-contained caption】[Y/N]
【Next step】jebo-writing-style
```
