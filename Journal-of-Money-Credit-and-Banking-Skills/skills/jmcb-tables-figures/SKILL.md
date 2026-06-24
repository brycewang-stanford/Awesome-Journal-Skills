---
name: jmcb-tables-figures
description: Use when exhibits — IRF plots, coefficient/event-study figures, balance-sheet and regression tables — are the bottleneck for a Journal of Money, Credit and Banking (JMCB) manuscript. Makes each exhibit answer the question on its own; it does not re-run the analysis or write the prose.
---

# Tables and Figures (jmcb-tables-figures)

## When to trigger

- An IRF figure has bands but no statement of what shock, what units, or what horizon
- A regression table reports six columns and the reader cannot tell which is the headline
- A bank balance-sheet or summary table is a data dump with no economic grouping
- Significance is shown with asterisks alone, with no economic magnitude in view
- The paper is at the 40-page limit and exhibits are competing for space with text

## The JMCB exhibit bar

JMCB is a quantitative monetary/banking journal, so its signature exhibits are **impulse-response functions, local-projection coefficient plots, and event-study figures**, alongside the standard regression and balance-sheet tables. The bar is that each exhibit is **self-contained and economically legible**: a reader skimming should grasp the shock, the units, the horizon, the magnitude, and the uncertainty without hunting through the text. Because the journal recommends ≤40 pages including tables and figures, exhibit economy is also a length discipline — every panel must earn its place.

## Exhibit craft

### Impulse responses and local projections
- **Label the shock and its size** ("response to a 25bp contractionary surprise") and the **units of the response** (pp, %, bps) directly on the figure.
- Show **confidence bands** and state the method in the note (bootstrap/HAR/lag-robust). For local projections, show enough horizon to see the peak and the return.
- Put the **economic magnitude in the caption**, not only the plot — "lending falls 1.8% at the 4-quarter peak."

### Regression and panel tables
- **Headline column first or visually flagged**; do not make the reader guess which specification is the result.
- Report the **economic magnitude** (a one-SD or one-policy-unit effect) next to the coefficient — a deposit beta or a pass-through in interpretable units, not a bare coefficient.
- State **fixed effects, clustering, and N** in every table; for micro-banking, make the firm×time absorption visible so demand-netting is obvious.
- Significance via asterisks is acceptable in JMCB house style, but **never let asterisks substitute for magnitude** — the economic size must be readable.

### Balance-sheet / summary tables
- Group rows by economic meaning (funding, lending, capital, liquidity), not source order.
- Show the cross-section that matters for the mechanism (e.g., by capital quartile) rather than one pooled column.

## The exhibit hierarchy a referee reads first

Referees skim exhibits before prose. Order them so the argument is legible from the figures and tables alone:

1. **A descriptive/summary table or motivating figure** — establishes the sample and the variation (e.g., the cross-section of bank capital, the time series of the shock).
2. **The headline exhibit** — the IRF, the main coefficient table, or the counterfactual that *is* the contribution. It should be unmistakable.
3. **The mechanism exhibit** — the heterogeneity cut or channel decomposition that shows *why* (e.g., response by capital quartile).
4. **The key robustness exhibit(s)** — the one or two that defuse the most damaging objection, with magnitudes beside the baseline.

If a referee can reconstruct the paper's claim from this sequence without the text, the exhibits are doing their job.

## Notes, units, and reproducibility cues

Table and figure notes are not decoration at JMCB — given the journal's replication heritage, they are where a careful referee checks that the exhibit means what the text claims. Each note should state the sample period and frequency, the estimator, the inference method (clustering dimensions, bootstrap, HAR), and the units of the reported effect. For IRFs, state the shock normalization explicitly (a 25bp or one-SD surprise). Ambiguous units or missing inference details invite the referee to assume the worst.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JMCB is monetary/banking — macro time series + bank panels; local projections for the macro lane, DiD/IV for the bank lane.

- **Tables:** `etable` (multi-model) or `did_summary_to_latex` straight from the `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Every IRF/LP figure states the shock, its size, the response units, and the horizon
- [ ] Confidence bands shown; inference method named in the note
- [ ] Headline specification is unmistakable in each table
- [ ] Economic magnitude (one-SD / one-policy-unit) reported alongside coefficients
- [ ] Fixed effects, clustering, and N in every regression table
- [ ] Summary/balance-sheet tables grouped by economic meaning and by the relevant cross-section
- [ ] Exhibits fit the 40-page discipline; overflow pushed to the online appendix with a pointer

## Anti-patterns

- An IRF with unlabeled axes or no stated shock size — the reader cannot recover the magnitude
- A regression table where the headline column is buried among controls and placebos
- Asterisks reported with no economic magnitude, so significance stands in for size
- A balance-sheet table dumped in source order with no economic grouping
- Plotting only the pooled response when the mechanism is heterogeneous (hiding the cross-section)
- Letting low-value exhibits occupy main-text pages while load-bearing ones get cut for length

## Figures vs. tables: choose by what the reader must see

A dynamic response (an IRF or event study) almost always belongs in a **figure** — the shape and the timing are the point, and a table of horizon coefficients hides both. A cross-sectional comparison or a precise magnitude with its standard error belongs in a **table**. JMCB papers often over-table dynamics and under-figure them; converting a 12-row horizon table into a banded IRF plot both clarifies the result and saves space against the 40-page recommendation. Reserve tables for where the exact number, not the pattern, is what a reader needs.

## Worked vignette (illustrative)

A draft shows a local-projection figure of lending after a monetary shock with bare y-axis "coefficient" and no shock size. The JMCB fix: relabel to "% response of bank lending to a 100bp contractionary surprise," extend the horizon to 12 quarters to show the −1.8% peak at quarter 4 and the return to zero by quarter 10, add 90% bootstrap bands, and state the magnitude in the caption. A second figure splits by capital quartile so the heterogeneity the paper argues is visible at a glance. Two clean figures replace four cluttered tables, freeing pages under the 40-page cap.

## Output format

```text
【Journal】Journal of Money, Credit and Banking
【Skill】jmcb-tables-figures
【Exhibit type】IRF/LP figure / regression table / balance-sheet table / event study
【Self-contained?】shock + units + horizon + magnitude readable without the text? [Y/N]
【Headline clarity】which column/panel is the result; is it flagged?
【Magnitude shown】economic size alongside coefficients/bands? [Y/N]
【Specs visible】fixed effects + clustering + N present? [Y/N]
【Length fit】exhibits within the 40-page core; overflow mapped to appendix
【Next skill】jmcb-internet-appendix
```
