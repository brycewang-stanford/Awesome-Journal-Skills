---
name: aistats-experiments
description: Use when designing or auditing AISTATS experiments, simulations, baselines, statistical tests, uncertainty estimates, ablations, random seeds, hyperparameters, compute, dataset handling, and claim-to-evidence fit.
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

## Output format

```text
[Experiment readiness] strong / adequate / weak
[Claim -> evidence map] <claim: table/figure/simulation>
[Missing statistical evidence] <uncertainty/test/seed/baseline>
[Reproducibility gaps] <hyperparameters/compute/data/code>
[Decision-critical next run] <one experiment or simulation>
```
