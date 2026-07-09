---
name: recsys-artifact-evaluation
description: Use when packaging ACM RecSys code, datasets, splits, trained models, propensity logs, and seeds as an anonymous in-paper repository during review or a public archive after acceptance, even though RecSys has no separate artifact badge — covering what recommender reviewers open first and how to make a top-N ranking table regenerable end to end.
---

# RecSys Artifact Evaluation

Use this for evidence packaging around RecSys. The venue does not run a separate artifact-badge
process; instead the Call for Contributions expects a link to an **anonymous repository** inside
the paper, and reproducibility-minded reviewers judge the paper partly by whether that repository
makes the ranking claims regenerable.

## Artifact plan

- Decide what a reviewer needs to trust the claim: the exact dataset version, the split script,
  baseline configurations, tuning grids, trained-model checkpoints, exposure/propensity logs for
  off-policy claims, seeds, and the evaluation code.
- Keep decision-critical evidence in the paper or appendix; optional run files live in the
  repository, because RecSys reviewers are not obliged to open it.
- Anonymize repository history, commit authors, cluster paths, license headers, and any platform
  or organization names.
- Include a one-minute reproduction map: environment, dependencies, dataset download or
  identifier, commands, expected ranking numbers, runtime, seeds, and known nondeterminism.
- For proprietary interaction data, give enough provenance and preprocessing detail for credible
  reproduction on a public dataset without violating data-use terms.
- After acceptance, swap the anonymous mirror for a public, licensed, citable archive.

## What RecSys evidence reviewers open first

| Claim type | First artifact inspected | Common failure caught |
|---|---|---|
| Top-N ranking gain | Split script + baseline configs | Random split leaking the future; baselines under-tuned |
| Off-policy / counterfactual result | Logged propensities + estimator code | Propensities missing, so the IPS/DR estimate cannot be recomputed |
| Sequential/session model | Data ordering + leave-one-last split | Test interactions seen during training |
| Reported metric values | The scorer and its cutoff | Sampled metrics presented as full-ranking numbers |

Because RecSys reviewers can and do re-run a small offline pipeline, make the headline ranking
table regenerable with one command before polishing anything else.

## Worked vignette: packaging an off-policy study

A hypothetical submission proposes an exposure-corrected ranker validated offline and in a
semi-synthetic simulator.

- Ship the logging policy's **propensities** alongside the interactions, not just the clicks, so
  the inverse-propensity estimate can be recomputed.
- Provide the simulator as one parameterized script so a reviewer can vary exposure strength and
  reward, rather than trusting a single frozen curve.
- Emit every ranking and reward table directly from logged results so the PDF numbers and the
  repository numbers cannot drift apart.
- State which regime the simulator satisfies the positivity assumption in and where it breaks it,
  since that mapping is what reproducibility-minded reviewers grade.

## Calibration anchors

```text
repo/
  README.md            # one-minute orientation: env, data id, one command per table
  environment.yml      # pinned versions of the recommender framework and deps
  data/PREP.md         # dataset version, split protocol (temporal), checksums
  configs/             # per-model + per-baseline configs with tuning grids
  run_tables.sh        # regenerates Table 1..N from seeds
```

- Assume only the README and one entry script get opened; design for that.
- Repository size limits and accepted hosting change by cycle; verify against the current
  submission instructions rather than a past year.

## Output format

```text
[Artifact role] anonymous in-paper repo / camera-ready public archive
[Contents] <data/splits/configs/checkpoints/propensities/seeds>
[Anonymity risks] <paths / commit authors / platform names / URLs>
[Reproduction level] turnkey / scripted / descriptive / weak
[Fixes before upload] <ordered list>
```
