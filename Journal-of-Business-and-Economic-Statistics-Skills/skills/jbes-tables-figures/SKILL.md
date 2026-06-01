---
name: jbes-tables-figures
description: Use when designing the simulation tables and figures for a Journal of Business & Economic Statistics (JBES) methods paper so size, power, coverage, and the empirical results are legible to both statisticians and applied economists. Improves exhibits; it does not change results.
---

# Tables & Figures (jbes-tables-figures)

## When to trigger

- Simulation tables are dense and a reader cannot read off whether the method controls size
- Size, power, coverage, bias, and RMSE are scattered instead of side-by-side
- Figures lack confidence bands, or compare against no baseline
- Exhibit notes do not state the DGP, sample size, replications, or nominal level

## What JBES exhibits must communicate

A JBES paper is judged by method experts who read the tables as the evidence. Exhibits carry two distinct jobs: the **Monte Carlo exhibits** that establish the method's statistical properties, and the **empirical exhibits** that establish relevance on real data. Both must be readable by a statistician *and* an applied economist, since the journal bridges the two communities.

## Monte Carlo exhibits

- Put **size and power side-by-side** across DGPs and sample sizes; mark the nominal level so over/under-rejection is obvious.
- For interval methods, report **coverage and average length** together; for point estimators, **bias and RMSE** together.
- Always show the **incumbent baseline** in the same table under identical DGPs.
- Figures: size-power curves, coverage-vs-n plots, empirical-vs-nominal QQ plots, sampling distributions with the asymptotic reference overlaid.

## Empirical exhibits

- Report estimates with appropriate (HAC/cluster/dependence-robust) standard errors.
- Show the substantive payoff: what the new method changes relative to the standard approach.

## Self-contained notes (every exhibit)

State the DGP or data source, sample size(s), number of Monte Carlo replications, nominal level, the estimator/test, the inference method, and units. A reader should not need the body to interpret the table.

## Checklist

- [ ] Size and power readable side-by-side, with nominal level marked
- [ ] Coverage shown with average length; bias shown with RMSE
- [ ] Incumbent baseline in the same exhibit under identical DGPs
- [ ] Figures have confidence bands / reference distributions
- [ ] Every note states DGP/data, n, replications, level, method, units
- [ ] Vector output (PDF/EPS); no chartjunk; legible in print
- [ ] Numbers match the manuscript text and the code output

## Anti-patterns

- A wall of numbers where size control cannot be read off at a glance
- Reporting power without size (or coverage without length)
- Omitting the baseline, so "improvement" is unquantified in the exhibit
- Notes that force the reader back into the body to decode the table
- Figures with no uncertainty and no reference distribution

## Output format

```
【Exhibit】Monte Carlo / empirical
【Size+power】side-by-side with level marked? [Y/N]
【Coverage/length or bias/RMSE】paired? [Y/N]
【Baseline】incumbent in same exhibit? [Y/N]
【Notes】DGP/data, n, reps, level, method, units present? [Y/N]
【Next step】jbes-writing-style
```
