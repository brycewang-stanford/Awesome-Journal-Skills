---
name: aistats-reproducibility
description: Use when strengthening AISTATS reproducibility evidence, including the official checklist, statistical assumptions, proofs, datasets, hyperparameters, random seeds, compute, uncertainty estimates, baselines, and code/data release statements.
---

# AISTATS Reproducibility

Use this before submission and again before camera-ready. Reopen the current CFP and
OpenReview forms to confirm whether a reproducibility checklist is required.

## Evidence map

- Map each theorem, algorithmic claim, simulation claim, and empirical claim to a verifiable
  location in the paper, appendix, supplement, or artifact package.
- For theory, state assumptions, proof dependencies, convergence conditions, constants, and
  failure modes clearly enough for statistical readers.
- For experiments, report datasets, splits, preprocessing, evaluation metrics, baselines,
  hyperparameter ranges, final selected settings, seeds, repeated runs, compute, and runtime.
- For small performance differences, add uncertainty estimates: standard errors, confidence
  intervals, paired tests, bootstrap intervals, or repeated trials as appropriate.
- Explain missing code/data honestly and describe how a reader could reproduce the analysis
  in principle.
- Keep the checklist consistent with the manuscript; contradictions between checklist and
  paper are review-risk multipliers.

## Output format

```text
[Claim inventory] <claim -> evidence location>
[Checklist status] complete / inconsistent / missing
[Statistical reproducibility gaps] <assumptions/seeds/uncertainty/hyperparameters/compute>
[Paper fixes] <must appear in main PDF>
[Supplement fixes] <appendix or artifact additions>
```
