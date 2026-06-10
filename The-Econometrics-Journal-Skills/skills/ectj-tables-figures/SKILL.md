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

## Output format

```text
[Exhibit diagnosis] keep / compress / move / delete
[Main-text role] <theory, simulation, or application>
[Reader takeaway] <one sentence>
[Compression action] <merge panels, move appendix, simplify notes>
[Missing note detail] <sample, metric, seed, units, or method>
```
