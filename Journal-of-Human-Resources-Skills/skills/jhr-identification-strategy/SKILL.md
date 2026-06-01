---
name: jhr-identification-strategy
description: Use when stress-testing causal identification for a Journal of Human Resources empirical-micro manuscript, including RCT, DID, RDD, IV, event studies, decompositions, policy shocks, and reconciliation with prior estimates.
---

# Identification Strategy (jhr-identification-strategy)

## When to trigger

- The paper makes a causal claim
- Referees could say selection, omitted variables, or policy timing drives the result
- You need a reconciliation and sensitivity plan before submission

## Design checks

- **RCT**: attrition, balance, compliance, spillovers, pre-analysis plan, multiple
  testing, cluster level.
- **DID / event study**: timing, controls, pre-trends, treatment heterogeneity,
  anticipation, modern estimators where needed.
- **RDD**: manipulation, bandwidth, polynomial order, covariate continuity,
  donut/alternative bandwidths.
- **IV**: first stage, exclusion, monotonicity, weak-IV inference, LATE population.
- **Decomposition/descriptive**: what is descriptive, what is causal, and what
  policy lesson follows.

## JHR-specific layer

- Re-estimate or benchmark against close prior work when results differ.
- Report sensitivity tests that explain which sample/specification choices matter.
- Keep the public-policy interpretation tied to identified variation.

## Output format

```text
[Claim] causal / descriptive / decomposition
[Design] RCT / DID / RDD / IV / event study / other
[Main threat] ...
[Design defense] ...
[Reconciliation needed] ...
[Next step] jhr-data-analysis
```
