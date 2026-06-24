---
name: jleo-tables-figures
description: Use when designing tables and figures for a Journal of Law, Economics, and Organization (JLEO) manuscript — making exhibits carry the institutional/organizational comparison cleanly for an OUP economics audience. Improves the exhibits; it does not run the analysis (jleo-robustness) or write the prose (jleo-writing-style).
---

# Tables & Figures (jleo-tables-figures)

## When to trigger

- The main table has fifteen columns and a reader cannot find the institutional comparison that is the point
- A reduced-form effect is reported but the governance/institutional contrast it implies is not visible in any exhibit
- An event study or comparative-static prediction would be far more persuasive as a figure than a table
- Notes are not self-contained: a reader cannot tell the sample, the estimator, the clustering, or what the coefficient means
- A formal model's comparative statics are stated in prose but never shown graphically

## Designing exhibits for the institutional argument

JLEO is an economics journal published by OUP; the exhibit conventions are standard top-economics, but the *content* must foreground the institutional or organizational comparison. The reader should be able to read the institutional claim off the exhibit without the text.

1. **One main table answers the headline question.** The coefficient that *is* the institutional effect (the governance-form contrast, the reform effect, the assignment effect) belongs in the first one or two columns, with the build-up to the preferred specification readable left to right. Move the kitchen sink to the appendix.
2. **Show the comparison, not just the coefficient.** If the claim is "hierarchy beats market above a specificity threshold," a figure with the outcome by specificity, split by governance form, makes the institutional logic visible in a way a regression table cannot.
3. **Event studies and comparative statics belong in figures.** Reform effects: plot leads and lags with CIs so the parallel-trends evidence is visible. Theory predictions: overlay the model's comparative static on the data.
4. **Self-contained notes.** Every exhibit states sample, unit of observation, estimator, the institutional treatment, fixed effects, the clustering level, and what one unit of the coefficient means *institutionally* (e.g., "a one-SD rise in asset specificity").
5. **Report uncertainty honestly.** Standard errors / confidence intervals on every estimate; for few-cluster institutional settings, report the bootstrap-based interval, not just the naive SE. Significance stars are acceptable house practice at JLEO, but SEs must be present and the institutional magnitude must be interpretable.

## Quick diagnostic

| Symptom | Fix |
|---------|-----|
| Reader cannot find the institutional effect in the table | Promote it to columns 1–2; demote controls |
| The governance comparison is implicit in a coefficient | Add a figure showing the outcome by governance form |
| Parallel trends asserted in text only | Event-study figure with leads/lags and CIs |
| Note does not give clustering / estimator / sample | Rewrite the note to be self-contained |
| Magnitude is a bare coefficient | State the institutional interpretation of one unit |

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JLEO is law-and-economics/organizations; institutional designs with endogeneity — foreground identification.

- **Tables:** `etable` (multi-model) or `did_summary_to_latex` straight from the `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] The headline institutional effect is in the first one or two columns of the main table
- [ ] At least one exhibit shows the governance/institutional *comparison*, not just a coefficient
- [ ] Reform/event designs have an event-study figure with leads, lags, and CIs
- [ ] Every note is self-contained (sample, unit, estimator, FE, clustering, treatment definition)
- [ ] Each coefficient's institutional magnitude is interpretable (a one-SD or discrete-form change)
- [ ] SEs/CIs present on every estimate; few-cluster intervals use the bootstrap

## Anti-patterns

- A 14-column main table where the institutional comparison is buried in the middle
- Figures that are decorative (raw scatter with no institutional split) rather than argumentative
- Notes that omit the clustering level or the estimator, leaving inference unverifiable
- Reporting a coefficient with no statement of what it means for the governance/institution
- Parallel-trends or comparative-static claims that exist only in prose, never in an exhibit

## Worked vignette (illustrative)

A make-or-buy paper's Table 3 has ten columns sweeping controls; the governance contrast (integrated vs. arm's-length dispute rates) is implicit in a single interaction coefficient in column 7. The JLEO fix: promote the integrated-vs-market contrast to a two-panel Table 1 (Panel A baseline, Panel B with the specificity interaction, SEs in parentheses, the dependent-variable mean shown), and add Figure 1 plotting dispute rates against asset specificity, split by governance form — so the reader *sees* the crossing point where hierarchy starts to dominate the market. The sweep moves to the appendix. The institutional comparison is now legible without the text, and the figure carries the transaction-cost logic the table only implies.

## Output format

```text
【Headline exhibit】the table/figure that carries the institutional claim
【Institutional effect placement】in columns ___ (should be 1-2)
【Comparison shown】figure of outcome by governance form / institution? [Y/N]
【Event study / comparative static figure】present with CIs? [Y/N/NA]
【Notes self-contained】sample + estimator + FE + clustering + treatment def? [Y/N]
【Magnitude interpretable】one-unit institutional meaning stated? [Y/N]
【Next skill】jleo-writing-style
```
