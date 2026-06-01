---
name: aistats-artifact-evaluation
description: Use when packaging AISTATS code, data, proofs, simulation scripts, notebooks, random seeds, and logs as anonymous supplementary evidence or public post-acceptance artifacts, even when there is no separate artifact badge.
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

## Output format

```text
[Artifact role] anonymous supplement / camera-ready release / public archive
[Contents] <code/data/proofs/logs/notebooks>
[Anonymity risks] <paths/metadata/licenses/URLs>
[Reproduction level] turnkey / scripted / descriptive / weak
[Fixes before upload] <ordered list>
```
