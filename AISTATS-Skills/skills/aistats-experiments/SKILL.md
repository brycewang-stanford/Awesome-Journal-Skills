---
name: aistats-experiments
description: Use when designing or auditing AISTATS experiments, simulations, baselines, statistical tests, uncertainty estimates, ablations, random seeds, hyperparameters, compute, dataset handling, and claim-to-evidence fit, with emphasis on experiments that validate theorems rather than chase leaderboards.
---

# AISTATS Experiments

Use this before submission when the empirical or simulation story is not yet locked.

## Experiment audit

- Map each empirical claim to a table, figure, simulation, ablation, or robustness check.
- Include baselines that represent both ML practice and relevant statistical methods.
- Separate synthetic simulations that validate assumptions from real-data experiments that
  show practical relevance.
- Report uncertainty for stochastic results: repeated runs, standard errors, confidence
  intervals, paired tests, or bootstrap intervals when appropriate.
- Report dataset splits, preprocessing, metrics, hyperparameter search ranges, final chosen
  settings, selection criteria, random seeds, hardware, software versions, and runtime.
- Add ablations for the mechanism, not just cosmetic variants.
- Audit for leakage, selection bias, multiple-comparison issues, and mismatch between
  theoretical assumptions and empirical setup.

## What experiments are for at this venue

- AISTATS experiments exist to validate theory, not to win leaderboards. One focused
  simulation confirming a predicted rate outweighs five extra benchmark datasets.
- The strongest design triad: a synthetic study where assumptions hold exactly, a study where
  they are deliberately violated, and a real-data study showing practical behavior.
- Reviewers, frequently statisticians, check whether the empirical regime — sample size,
  dimension, noise level — matches the asymptotic regime of the theorems. A bound proven as
  n grows but tested only at n = 500 invites the question of relevance.

## Theory-validation design table

| Theoretical claim | Matching experiment | Reject pattern avoided |
|---|---|---|
| Convergence rate in n | Log-log error versus n with fitted slope | "Rates asserted but never plotted" |
| Confidence-interval coverage | Empirical coverage across many replications | "Nominal 95 percent never verified" |
| Regret bound | Cumulative regret versus horizon, with the bound curve overlaid | "Bound and trajectory never compared" |
| Robustness to misspecification | Violation-severity sweep | "Guarantees hold under assumptions the experiments quietly break" |

## Vignette: a kernel conditional independence test

Suppose the paper proves finite-sample type-I error control under a boundedness assumption.
The matching plan: simulate under the null at several sample sizes to verify size, sweep
dependence strength for power curves, then inject heavy-tailed noise that breaks boundedness
to map degradation — every panel tied to a numbered theorem or remark.

## Statistical reporting floor

- Replication counts and seeds for every stochastic figure; captions must say whether bars
  are standard errors, confidence intervals, or quantiles.
- Report the compute actually consumed rather than vague feasibility language.

## Output format

```text
[Experiment readiness] strong / adequate / weak
[Claim -> evidence map] <claim: table/figure/simulation>
[Missing statistical evidence] <uncertainty/test/seed/baseline>
[Reproducibility gaps] <hyperparameters/compute/data/code>
[Decision-critical next run] <one experiment or simulation>
```
