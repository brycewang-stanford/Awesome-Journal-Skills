---
name: jfm-tables-figures
description: Use when microstructure exhibits — spreads, depth, price-impact, order-flow, and event-study plots — are the bottleneck for a Journal of Financial Markets (JFM) manuscript. Sharpens the exhibits; it does not invent evidence or citations.
---

# Tables and Figures (jfm-tables-figures)

## When to trigger

- The main table reports many liquidity coefficients but the reader cannot see the headline result
- A market-structure event has no event-study figure showing the spread/depth path around the date
- Units are ambiguous (basis points vs. cents vs. percent; per-share vs. per-dollar) across exhibits
- Intraday or cross-sectional patterns are described in prose where a figure would carry them
- Summary statistics for the liquidity measures and the sample are missing or buried

## What a JFM exhibit set must carry

Microstructure papers live or die on whether the trading-process pattern is **visible**. The exhibit set should let a referee verify the mechanism without re-reading the text.

| Exhibit | What it must show | Common JFM failure |
|---------|-------------------|---------------------|
| Summary stats / sample | distribution of spreads, depth, impact, volume; N stocks × days | reporting only means, hiding skew/outliers |
| Headline regression | the one coefficient that is the contribution, isolated | the result drowned in a 12-column table |
| Event study (if a shock) | spread/depth path with pre-event leads + CIs around the date | no leads shown, so pre-trends invisible |
| Cross-section / heterogeneity | effect strongest where mechanism predicts | only the pooled average |
| Intraday / dynamics | U-shaped pattern, impulse-response of impact | described in prose, not plotted |

## Craft rules JFM referees reward

1. **State units and horizon on every liquidity exhibit.** "Effective spread (bps)", "5-min permanent impact", "depth at touch (shares)". Inconsistent units between tables is an immediate credibility hit.
2. **Make the headline coefficient unmissable.** One column or one panel is the contribution; the rest is support. Bold the takeaway in the caption, not with significance stars on every cell.
3. **Report standard errors and the clustering** in the table notes — say it is two-way stock×time / Newey-West, not just "robust SE."
4. **Event studies need leads.** Show the periods *before* the market-structure change so pre-trends are visible; without them the design is unfalsifiable on the page.
5. **Self-contained notes.** Each table/figure note states sample, period, measure construction, and inference — a referee should not have to hunt.
6. **Plot what is intrinsically dynamic** (intraday U-shape, impulse responses, order-book replenishment) rather than tabulating it.

## Worked exhibit set (illustrative)

For a tick-size-change paper, a clean four-exhibit core: **Table 1** summary stats (quoted/effective spread in bps, depth in shares, daily volume, N stocks × days, with percentiles not just means); **Figure 1** event study — effective spread plotted from t−10 to t+10 days with confidence bands, leads visibly flat, the level shift at t=0 obvious; **Table 2** the DiD with the single treatment coefficient in column 1 isolated, columns 2-4 adding controls, notes stating two-way stock×day clustering; **Figure 2** heterogeneity — the spread effect by adverse-selection quintile, rising monotonically, showing the mechanism. A reader can verify the mechanism from the exhibits alone. Anything beyond this goes to the Internet Appendix.

## Summary statistics that pre-empt questions

The summary-statistics table is the first thing a referee reads, and a good one answers questions before they arise. For a microstructure paper, report not just means but the **distribution** (percentiles, SD) of each liquidity measure, the cross-sectional spread across stocks, and the sample dimensions (N stocks, N days, N trades). Show the liquidity measures' pairwise correlations so the reader sees whether your alternative constructs actually agree. Flag the skew that liquidity variables always exhibit — an unreported fat tail invites the "is this driven by a few illiquid names?" objection that a percentile table would have closed.

## Reading the exhibit like a referee

A microstructure referee scans, in order: Are the units sensible (a 200-bps "effective spread" on a liquid large cap is a red flag)? Do the event-study leads look flat, or is there a pre-trend the authors did not mention? Does the magnitude make economic sense relative to the average spread? Is the clustering in the notes, and does it match the panel structure? Build the exhibits to pass this scan — surprising-but-unexplained numbers and missing leads are what trigger the first skeptical comment.

## Captions and notes do real work

In microstructure papers the table/figure notes carry as much information as the cells. A complete note states: the sample (universe, period, N), the exact construction of each measure (effective spread formula, impact horizon, sign rule), the estimator and the **standard-error / clustering scheme**, and the units. A reader should be able to understand an exhibit without leaving it for the text. Vague notes ("robust standard errors in parentheses") invite the clustering objection; precise notes ("standard errors two-way clustered by stock and trading day") close it on the page. Treat the note as part of the result, not boilerplate.

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

- [ ] Every liquidity/impact exhibit states units and (for impact) the horizon
- [ ] The headline coefficient is visually isolated, not buried in a wide table
- [ ] Table notes name the SE/clustering scheme explicitly
- [ ] Any market-structure event has an event-study figure with pre-event leads and CIs
- [ ] Summary stats show distributions (not only means) for the liquidity measures
- [ ] Heterogeneity exhibit shows the effect is largest where the mechanism predicts
- [ ] Each exhibit note is self-contained (sample, period, construction, inference)

## Magnitude over stars

JFM exhibits should make the *economic* size of the effect unmissable, not just its statistical significance. With microstructure sample sizes, almost everything is significant at the 1% level, so a wall of three-star coefficients conveys little. Anchor every headline number against a benchmark a reader can judge: an effect of 3 bps means more when the table also shows the mean effective spread is 8 bps. State the implied magnitude in the caption ("a 38% reduction in the average effective spread"), and pair coefficients with the sample mean of the dependent variable. Significance markers are fine as a secondary signal, but the economic interpretation is what a microstructure referee weighs — a tiny, precisely estimated effect is not a contribution.

## Anti-patterns

- Inconsistent units (bps in one table, cents in the next) across the paper
- A 10-column regression table where the contribution is invisible
- An event study with no pre-event leads, so pre-trends cannot be judged
- Significance stars as the only signal of magnitude; no economic-size statement
- Describing the intraday pattern in a paragraph instead of plotting it
- Table notes that omit the clustering scheme

## Figures earn their place in microstructure papers

Some objects are intrinsically visual and lose their force in a table. Plot, do not tabulate: the **intraday U-shape** of spreads/depth/volume; the **event-study path** of a liquidity measure around a market-structure change (with leads and bands); the **price-impact / impulse-response function** showing how a trade's effect decays into permanent and temporary parts; **order-book replenishment** after a large trade; and **heterogeneity gradients** across an adverse-selection or size dimension. A well-built figure lets a referee confirm the dynamics in seconds; the same content in a 30-cell table is unreadable. Reserve tables for point estimates and their inference, figures for shapes and dynamics.

## Output format

```text
【Journal】Journal of Financial Markets (JFM)
【Skill】jfm-tables-figures
【Headline exhibit】is the contribution coefficient visually isolated? [Y/N]
【Units & horizon】stated on every liquidity/impact exhibit? [Y/N]
【Event study】leads + CIs around the shock shown? [Y/N / NA]
【Inference in notes】clustering scheme stated? [Y/N]
【Heterogeneity】mechanism-predicted pattern shown? [Y/N]
【Source status】verified URL / 待核实 / not asserted
【Next skill】jfm-internet-appendix
```
