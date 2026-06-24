---
name: ectj-tables-figures
description: Use when compressing The Econometrics Journal (EctJ) tables, figures, Monte Carlo displays, empirical-application exhibits, theorem summaries, and appendix references under a roughly 20-page printed-paper constraint.
---

# EctJ Tables And Figures

Use this when exhibits are doing too little work or consuming too much space.

## Exhibit rules

- Every main-text exhibit must support the leading case, the empirical application, or a
  decisive simulation diagnostic.
- Use compact simulation panels rather than long grids of redundant parameter settings.
- Put implementation details and expanded robustness tables in the online supplement, while
  keeping proof-critical or application-critical results in the printed paper or printed
  appendix.
- Use self-contained notes: sample, estimator, tuning, uncertainty, and units should be
  legible without hunting through the appendix.
- Prefer figures for estimator behavior, coverage, bias, RMSE, or power curves when patterns
  matter more than exact cells.

## Exhibit budget

Assign every main-text exhibit to exactly one job:

- **Theorem consequence**: makes a limiting result or approximation behavior visible.
- **Monte Carlo stress test**: shows size, power, bias, RMSE, coverage, or computation under the most
  revealing boundary cases.
- **Applied-value proof**: shows the empirical conclusion, decision, or interval that changes relative to
  incumbents.
- **Diagnostic safeguard**: documents tuning, convergence, weak identification, or failure regions.

Delete or move exhibits whose only job is "more robustness." EctJ rewards a compact leading case; a long
grid that does not change interpretation weakens the paper.

## Main-text compression rule

Limit the main paper to one exhibit per claim:

- one theorem-consequence or estimator-behavior display;
- one simulation table/figure that isolates the boundary case;
- one empirical-application exhibit that proves use value;
- one appendix pointer for full grids.

If two exhibits make the same reader update, merge them or move the weaker one to the supplement.

## Monte Carlo display conventions referees check first

- Size tables report the nominal level explicitly and show null rejection rates across all sample
  sizes; an entry like 0.063 only reads as distortion when 0.05 sits in the header.
- Coverage tables pair coverage with median interval length; coverage alone hides the trivial
  wide-interval fix.
- Power is a figure, not a table: curves against the incumbent under drifting alternatives, with
  the size-adjusted variant in the supplement if size distortion exists.
- Every simulation exhibit names replications, sample sizes, and the DGP label in its note; the
  RES one-page main-text norm for simulation summaries makes self-contained notes mandatory
  because design details live elsewhere.
- Bias and RMSE share one panel with the strongest competitor, not a simplified strawman.

## Worked compression pass

Illustrative vignette: a draft carries nine simulation exhibits — size at three sample sizes,
power at three alternatives, and three tuning grids. The EctJ-shaped result is three exhibits:

1. One size-and-coverage table at n in {250, 1000} with the nominal 5% level in the header,
   covering the calibrated DGP and the boundary DGP.
2. One power figure overlaying the new test and the incumbent at the calibrated design.
3. One application exhibit showing the decision that changes (illustrative: the incumbent rejects
   correct specification for 14 of 60 industries, the new test for 4).

The six tuning and secondary-grid panels move to the online appendix with one forward reference.
Reader updates lost: none. Printed pages recovered: roughly two — often the difference between
conforming and not.

## Theorem-adjacent exhibits

- A schematic figure of the identification argument or estimator pipeline can replace half a page
  of prose, but only when the geometry, ordering, or data flow is genuinely hard to verbalize.
- Numerical illustrations of a limiting approximation (illustrative: the density of the
  standardized statistic at n=250 against its normal limit) earn main-text space when they
  preempt the finite-sample objection EctJ referees raise against unpaired asymptotics.
- An assumption-by-scenario validity table (which conditions hold in which application class)
  works well in the printed appendix as a scope map for the leading case.
- Whatever the exhibit, the printed-page bill is the binding constraint: each candidate must beat
  the paragraph it replaces.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). The Econometrics Journal is a methods venue — estimator validity + simulation; pair estimates with diagnostics.

- **Tables:** `etable` (multi-model) or `did_summary_to_latex` straight from the `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Output format

```text
[Exhibit diagnosis] keep / compress / move / delete
[Main-text role] <theory, simulation, or application>
[Reader takeaway] <one sentence>
[Compression action] <merge panels, move appendix, simplify notes>
[Missing note detail] <sample, metric, seed, units, or method>
```
