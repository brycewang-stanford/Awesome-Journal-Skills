---
name: revacc-tables-figures
description: Use when the exhibits are the bottleneck for a Review of Accounting Studies (RAST) manuscript — building self-contained accounting panel tables, event-study and equilibrium figures, and a descriptive-statistics block that survives referee scrutiny. Builds the exhibits; it does not run the analysis (revacc-data-analysis) or polish the surrounding prose (revacc-writing-style).
---

# Tables & Figures (revacc-tables-figures)

## When to trigger

- Tables are dense, inconsistent, or not self-explanatory without the text
- Your descriptive-statistics table is missing or does not let a referee sanity-check the sample
- A DiD or event study has no dynamic/event-time figure
- An analytical paper has propositions but no figure illustrating the comparative statics
- Significance is shown only with asterisks, or coefficients lack the economic-magnitude read

## The standard RAST exhibit set

Accounting empirical papers at RAST converge on a recognizable sequence; build it in order.

1. **Variable definitions** — every variable defined with its data source (Compustat item, CRSP field, I/B/E/S measure) so the sample is reconstructable.
2. **Descriptive statistics** — N, mean, median, SD, key percentiles for all variables; this is the table referees use to catch a broken sample (implausible accruals, miswinsorized ratios).
3. **Correlations** — Pearson/Spearman where it informs multicollinearity or the main association.
4. **Main result** — the focal estimating equation with fixed effects and clustering noted in the table notes; report **economic magnitude**, not only significance.
5. **Identification diagnostics** — pre-trends/dynamic effects (DiD), first stage (IV), bandwidth/density (RD).
6. **Robustness and cross-section** — alternative proxies, subsamples, channel partitions.

For **analytical** papers, the exhibit set is figures: an equilibrium/comparative-static plot that makes the proposition legible, and a stylized numerical example.

## Make every exhibit self-contained

A RAST table must be readable without the body text. The title states what is estimated; the notes give the **sample, period, unit of observation, fixed effects, clustering, winsorization, and what significance markers mean**. A referee should reconstruct the specification from the table alone. Report coefficients with standard errors (or t-stats) consistently, and translate the headline coefficient into an economic magnitude ("a one-SD increase in disclosure quality lowers the bid-ask spread by X%").

## Figures that earn their place

- **Event-time / dynamic-effect plot** for any DiD — the single most persuasive identification exhibit; show the flat pre-trend and the post-treatment path with confidence bands.
- **Event-study CAR plot** for information-content/value-relevance claims, with the window and benchmark stated.
- **Comparative-static figure** for analytical papers — plot the equilibrium object against the key primitive so the accounting reading is visible.
- Avoid chartjunk and dual axes; one figure, one message.

## House-style discipline

Follow the journal's formatting (待核实; 检索于 2026-06；以官网为准): consistent decimal places, a stated significance convention, numbered tables/figures referenced in order, and an abstract within the journal's limit (~150–250 words, 待核实). Keep exhibits anonymized for double-blind review (no author-identifying file names or acknowledgements embedded).

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-appendix drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). RAST is empirical accounting; emphasize identification of disclosure / governance effects and the multiple-testing haircut for mined associations.

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the effect size in
  interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Variable-definitions table with data sources present
- [ ] Descriptive-statistics table lets a referee sanity-check the sample
- [ ] Main table reports economic magnitude, not just significance
- [ ] Table notes give sample, period, unit, FE, clustering, winsorization, significance convention
- [ ] DiD has a dynamic/event-time figure; IV/RD diagnostics shown
- [ ] Analytical comparative statics illustrated in a figure
- [ ] Every exhibit is self-contained and anonymized for double-blind review

## Anti-patterns

- **Asterisks-only inference** with no standard errors and no economic magnitude.
- **Table dependent on the text** — notes too thin to reconstruct the specification.
- **No descriptive-statistics table**, hiding a broken or implausible sample.
- **A DiD with no event-time plot**, leaving pre-trends unshown.
- **Chartjunk / dual axes** that obscure the one message a figure should carry.
- **Identifying file names or acknowledgements** breaking anonymization.

## Output format

```text
【Exhibit set】var-defs / descriptives / correlations / main / diagnostics / robustness
【Main table】FE + clustering in notes; economic magnitude reported? yes/no
【Identification figure】DiD event-time / IV first stage / RD plot
【Analytical figure】comparative static illustrated? yes/no
【Self-contained?】each exhibit readable alone; anonymized for double-blind
【House style】decimals/significance convention/abstract limit (待核实)
【Next skill】revacc-writing-style
```
