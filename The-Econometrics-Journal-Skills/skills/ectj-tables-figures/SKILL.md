---
name: ectj-tables-figures
description: Use when compressing EctJ tables, figures, Monte Carlo displays, empirical-application exhibits, theorem summaries, and appendix references under a roughly 20-page printed-paper constraint.
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

## Output format

```text
[Exhibit diagnosis] keep / compress / move / delete
[Main-text role] <theory, simulation, or application>
[Reader takeaway] <one sentence>
[Compression action] <merge panels, move appendix, simplify notes>
[Missing note detail] <sample, metric, seed, units, or method>
```
