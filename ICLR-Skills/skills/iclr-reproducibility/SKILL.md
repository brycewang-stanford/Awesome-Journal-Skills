---
name: iclr-reproducibility
description: Use when strengthening reproducibility for ICLR papers, including seeds, variance, compute, datasets, implementation details, ethics statements, and reviewer-verifiable evidence.
---

# ICLR Reproducibility

Use this when the paper's main claims depend on experiments, simulations, data processing, human
subjects, or benchmark comparisons. ICLR reviewers are asked to evaluate rigor and reproducibility,
not just headline scores.

## Reproducibility audit

- Map each central claim to a table, figure, proof, appendix item, or artifact command.
- Record seeds, variance, confidence intervals, test splits, preprocessing, early stopping,
  hyperparameter search, model selection, and compute budget.
- Distinguish training compute from inference compute and report hardware details that affect
  comparability.
- Add negative results and failure cases when they explain boundary conditions.
- Check whether ethics or reproducibility statements are relevant under the current Author Guide.
- Make the appendix useful but not required for basic verification; reviewers may not inspect every
  appendix page.

## Common ICLR weak points

- Single-seed wins on unstable benchmarks.
- Missing comparison to strong open-source baselines or recent OpenReview/arXiv work.
- Ambiguous data leakage, test-set tuning, or prompt selection.
- Scaling claims without enough model sizes, tasks, or compute reporting.
- Ablations that remove multiple mechanisms at once.
- Private data or closed APIs with no substitute verification path.

## Output format

```text
[Reproducibility grade] strong / adequate / fragile / not reviewable
[Claim-to-evidence map] <claim -> table/figure/appendix/artifact>
[Missing controls] <seeds, baselines, ablations, leakage checks>
[Compute disclosure] complete / incomplete
[Priority fixes] <smallest changes that improve review confidence>
```

