---
name: aistats-artifact-evaluation
description: Use when packaging AISTATS code, data, proofs, simulation scripts, notebooks, random seeds, and logs as anonymous supplementary evidence or public post-acceptance artifacts, even when there is no separate artifact badge. Covers what statistically minded AISTATS reviewers inspect first and how to make Monte Carlo studies turnkey.
---

# AISTATS Artifact Evaluation

Use this for evidence packaging around AISTATS. The venue centers on artificial intelligence,
statistics, and machine learning, so artifacts should make statistical and computational
claims inspectable.

## Artifact plan

- Decide what evidence reviewers need: proof details, derivations, simulation scripts,
  benchmark code, datasets, preprocessing, hyperparameter sweeps, random seeds, logs, or
  qualitative examples.
- Keep decision-critical evidence in the main paper or appendix; optional run files can live
  in supplementary material.
- Anonymize repository history, paths, notebook metadata, license headers, organization
  names, cluster paths, grants, and commit authors.
- Include a minimal reproduction map: environment, dependencies, hardware, commands, expected
  outputs, runtime, seeds, and known nondeterminism.
- For restricted data, give enough provenance and processing detail for credible
  reproduction without violating data-use terms.
- After acceptance, replace anonymous archives with public, licensed, citable artifacts when
  feasible.

## What AISTATS evidence reviewers open first

| Claim type | First artifact inspected | Common failure caught |
|---|---|---|
| Convergence rate or regret bound | Proof appendix and constants | Condition used in the proof but missing from the theorem statement |
| Monte Carlo simulation | Seeded simulation script | Plots cannot be regenerated because seeds and replication counts are absent |
| Benchmark comparison | Training and evaluation configs | Baseline tuning budget undocumented |
| Bayesian or MCMC method | Sampler diagnostics and chain logs | No convergence statistics or trace evidence anywhere |

Because AISTATS reviewers are often statisticians, they will rerun a small simulation far
more readily than they will retrain a deep model, so make synthetic studies turnkey before
polishing anything else.

## Worked vignette: packaging a Monte Carlo study

A hypothetical submission proposes a doubly robust treatment-effect estimator with a root-n
normality guarantee, validated on synthetic causal data plus two real benchmarks.

- Ship the data-generating process as one parameterized script rather than constants buried
  in notebooks, so reviewers can vary n, dimension, and confounding strength.
- Record the replication count and the exact seed sequence used for every coverage and bias
  table; AISTATS-style claims about interval coverage are meaningless without them.
- Emit tables directly from logged results so the PDF numbers and artifact numbers cannot
  drift apart.
- State explicitly where the simulated regime satisfies the theorem assumptions and where it
  deliberately violates them, since that mapping is what statistical reviewers grade.

## Calibration anchors

- Supplementary inspection at AISTATS is at reviewer discretion; assume only the README and
  one entry script get opened, and design accordingly.
- Upload size limits and accepted formats vary by cycle; verify against the current
  OpenReview submission form rather than past years.

## Output format

```text
[Artifact role] anonymous supplement / camera-ready release / public archive
[Contents] <code/data/proofs/logs/notebooks>
[Anonymity risks] <paths/metadata/licenses/URLs>
[Reproduction level] turnkey / scripted / descriptive / weak
[Fixes before upload] <ordered list>
```
