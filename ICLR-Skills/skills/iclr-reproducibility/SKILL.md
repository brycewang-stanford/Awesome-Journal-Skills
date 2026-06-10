---
name: iclr-reproducibility
description: Use when strengthening reproducibility for ICLR papers, including seeds, variance, compute, datasets, implementation details, ethics statements, and reviewer-verifiable evidence. Use when writing the ICLR reproducibility statement, when a reviewer says a result is not verifiable, or when mapping each representation-learning claim to a seed, split, and command so anyone reading the permanent OpenReview record can check it.
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

## The reproducibility statement as a contract

ICLR has long pushed reproducibility statements and code release as community norms. Treat the
statement as a public contract: it sits beside the paper permanently, so reviewers and later readers
will hold you to it. Map every claim to something checkable.

| Claim element | What the statement should pin | Reviewer doubt it removes |
| --- | --- | --- |
| Headline number | Seed set, split, exact command | "Did they tune on test?" |
| Architecture detail | Config file in the supplement | "Hidden trick not in the text" |
| Compute cost | Hardware and FLOPs, train vs inference | "Only works at huge scale" |
| Data pipeline | Preprocessing script and license | "Leakage between splits" |

## Worked vignette

A representation-learning paper reports an embedding that improves retrieval. The reproducibility
statement maps the headline metric to `eval_retrieval.py --seed {0..4} --split test`, names the
frozen-encoder protocol, links the anonymized config, and reports per-seed variance. When a reviewer
asks whether the gain survives a different split, the authors point to the appendix table already
covering it. The verifiable mapping turns a potential "fragile" grade into "adequate" without new runs.

## Reviewer-pushback patterns

- "Cannot verify without your private data." Provide a synthetic or public-subset substitute path.
- "No variance reported." Add seed spread; ICLR reviewers distrust single-run peaks.
- "Appendix is a dump." Add an appendix map so verification does not require reading every page.

## Output format

```text
[Reproducibility grade] strong / adequate / fragile / not reviewable
[Claim-to-evidence map] <claim -> table/figure/appendix/artifact>
[Missing controls] <seeds, baselines, ablations, leakage checks>
[Compute disclosure] complete / incomplete
[Priority fixes] <smallest changes that improve review confidence>
```

