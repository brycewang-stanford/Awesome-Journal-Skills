---
name: aistats-reproducibility
description: Use when strengthening AISTATS reproducibility evidence, including the official reproducibility checklist, statistical assumptions, proofs, datasets, hyperparameters, random seeds, compute, uncertainty estimates, baselines, code/data release statements, and checklist-to-claim consistency audits.
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

## Checklist-to-claim audit table

| Checklist item | Pure-theory answer | Theory-plus-experiments answer |
|---|---|---|
| Code availability | NA only if there is literally no computation | Anonymous archive, or an honest stated reason |
| Assumptions stated | Every theorem lists its conditions inline | Plus a note on which experiments satisfy them |
| Error bars | NA for deterministic results | Required for every stochastic figure and table |
| Compute resources | NA | Hardware, runtime, and total number of runs |

Marking NA on an item the paper actually triggers is a recognizable AISTATS red flag,
because reviewers cross-check checklist answers against the PDF and read contradictions as
carelessness about the rest of the paper.

## Vignette: a rates-plus-simulation paper

Consider a submission proving posterior contraction rates for a Bayesian nonparametric model,
validated by MCMC simulation. Its reproducibility spine: prior hyperparameters and their
selection rule, chain length, burn-in, convergence diagnostics, replication seeds, and a
statement of which contraction-theorem conditions the simulated model satisfies — plus one
honest sentence about the condition it does not.

## Degrees of reproducibility

- Turnkey: one command regenerates each figure from logged seeds.
- Scripted: scripts exist but require documented manual steps or external data access.
- Descriptive: prose detailed enough that a competent reader could rebuild the pipeline.

For AISTATS, simulations should be turnkey because statistician reviewers actually rerun
them; large real-data pipelines may stay scripted with deviations documented. Stating the
achieved level honestly beats overpromising turnkey behavior that fails on a clean machine.

## Output format

```text
[Claim inventory] <claim -> evidence location>
[Checklist status] complete / inconsistent / missing
[Statistical reproducibility gaps] <assumptions/seeds/uncertainty/hyperparameters/compute>
[Paper fixes] <must appear in main PDF>
[Supplement fixes] <appendix or artifact additions>
```
