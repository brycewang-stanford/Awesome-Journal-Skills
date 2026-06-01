---
name: ijcai-experiments
description: Use when designing or auditing IJCAI or IJCAI-ECAI experiments, baselines, ablations, statistical evidence, hyperparameter reporting, compute descriptions, dataset handling, ethics risks, and reproducibility evidence for AI papers.
---

# IJCAI Experiments

Use this before submission when the experimental story is not yet locked. IJCAI reviewers
can score novelty, correctness, clarity, significance, impact, presentation, ethics, and
reproducibility.

## Experiment audit

- Map each major claim to a table, figure, theorem, ablation, proof, or qualitative analysis.
- Include strong, current, and properly tuned baselines; explain any missing baseline before
  reviewers ask.
- Report dataset splits, preprocessing, metrics, search ranges, final hyperparameters,
  selection criteria, random seeds or repeats, and compute infrastructure.
- Add ablations for the core mechanism, not just peripheral architecture choices.
- Use uncertainty estimates, paired tests, confidence intervals, or repeated runs when small
  differences could change the conclusion.
- For sensitive data or human-facing systems, document privacy, consent, copyright, safety,
  fairness, misuse, and deployment limits.
- Keep enough details in the main paper for credible reproduction even if reviewers ignore
  the supplementary material.

## Output format

```text
[Experiment readiness] strong / adequate / weak
[Claim -> evidence map] <claim: section/table/figure>
[Missing baseline or ablation] <item>
[Reproducibility gaps] <hyperparameters/seeds/compute/data/code>
[Decision-critical next run] <one experiment>
```
