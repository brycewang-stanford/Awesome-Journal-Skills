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

## Public-policy validity check

For every causal claim, write the policy interpretation in LATE/ATT/descriptive terms:

- **Who** is affected: treated population, complier group, cohort, locality, or institution.
- **What margin** changes: enrollment, employment, wages, health, fertility, retirement, or another JHR outcome.
- **Which policy lever** is credible: eligibility rule, treatment intensity, price, access, mandate, or program design.
- **What does not travel**: populations, periods, institutions, or equilibrium responses outside the design.

If the policy sentence needs a broader population than the estimand supports, narrow the claim before
submission.

## Output format

```text
[Claim] causal / descriptive / decomposition
[Design] RCT / DID / RDD / IV / event study / other
[Main threat] ...
[Design defense] ...
[Reconciliation needed] ...
[Next step] jhr-data-analysis
```
