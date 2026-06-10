---
name: jhr-data-analysis
description: Use when building or auditing Journal of Human Resources empirical data, sample construction, causal estimates, robustness, comparative estimation, online appendix material, and reproducible analysis.
---

# Data Analysis (jhr-data-analysis)

## When to trigger

- You are preparing the empirical pipeline for a JHR paper
- Sample construction, reconciliation, or robustness is still unsettled
- The paper needs a replication-ready workflow before acceptance

## Applied-micro analysis checklist

- Define unit, population, period, treatment, comparison group, and outcome.
- Show sample attrition and merge rules.
- Report baseline balance or pre-treatment comparability when relevant.
- Estimate main effects with the right clustering and fixed effects.
- Add reconciliation estimates against the closest prior published work.
- Add robustness for sample windows, functional form, controls, treatment
  definitions, and outlier handling.

## JHR-specific constraints

- Keep main tables inside the page limit; move overflow to Online Appendix.
- Prepare a data-archive plan from the start, especially for restricted data.
- For RCTs, track pre-analysis plan registration and deviations.

## Comparative-estimate workflow

Build one reconciliation table before submission:

| Column | Purpose |
|---|---|
| Prior published estimate | Reproduce or quote the closest estimate with sample/design notes |
| Prior specification on your data | Shows whether the difference is data or specification |
| Your preferred specification | Shows the incremental design or measurement change |
| Sensitivity bridge | Changes one assumption at a time: sample, controls, weights, clustering, outcome |

This table can live in the Online Appendix, but the introduction should summarize the lesson in one
sentence. Without it, a JHR referee can ask for reconciliation late in the process.

## Output format

```text
[Sample] unit + population + period
[Design] ...
[Main estimates] ...
[Reconciliation tests] ...
[Archive-readiness gaps] ...
[Next step] jhr-contribution-framing
```
