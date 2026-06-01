---
name: icml-artifact-evaluation
description: Use when packaging ICML code, data, anonymous repositories, supplementary code/data ZIPs, reproducibility artifacts, and public release material under ICML rules.
---

# ICML Artifact Evaluation

ICML does not let artifacts sit outside the paper's scientific argument. Reproducibility and code
availability are explicitly considered in decision-making, and accepted submissions may publish the
original supplementary material on OpenReview.

## Review-stage package

- Decide whether the artifact is code, data, model weights, simulator, benchmark, proof script,
  notebook, or supplementary manuscript.
- Anonymize authors, repository ownership, filenames, commit history, logs, model cards, dataset
  cards, licenses, and personal paths.
- If using an anonymous repository, put it on a branch that will not change after the submission
  deadline.
- Put critical evaluation material in the paper body, not only in supplement. Reviewers decide
  whether to consult appendices or supplementary material.
- Provide minimal commands, environment details, expected runtime, hardware assumptions, and result
  mapping.

## Public-release package

- Because accepted original supplementary material may become public, review-stage artifacts should
  not contain private, illegal, or unreleasable content.
- For camera-ready, final supplementary material is not uploaded separately; code/data should move
  to a public repository or archive and be linked in the paper/OpenReview code URL field.
- Add clear licenses and persistent identifiers when possible.

## Output format

```text
[Artifact role] code / data / model / benchmark / proof / none
[Review package] sufficient / incomplete / unsafe
[Anonymity risks] <metadata, repo, filenames, links>
[Decision relevance] <why reviewers need it>
[Public release plan] <repo/archive/license/code URL>
```

