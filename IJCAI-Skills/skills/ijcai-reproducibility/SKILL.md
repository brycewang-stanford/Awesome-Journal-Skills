---
name: ijcai-reproducibility
description: Use when strengthening IJCAI or IJCAI-ECAI reproducibility evidence for theory, algorithms, datasets, and computational experiments under the official convincing/credible/irreproducible reviewer rubric and optional reproducibility-section guidance.
---

# IJCAI Reproducibility

Use this before submission and again before camera-ready. Reopen the current reproducibility
page; IJCAI's rubric and checklist can change.

## Evidence map

- Target at least a credible reproducibility rating for every major result; aim for
  convincing when resources can be shared safely.
- For new algorithms, include a conceptual outline or pseudocode in the paper.
- For theory, state assumptions, formal claims, citations to tools, proof sketches, and
  proofs for novel claims.
- For datasets, cite existing sources, describe unavailable or proprietary datasets, and
  include or promise release of new datasets only when legally possible.
- For computational experiments, report final hyperparameters, search ranges, selection
  criteria, seeds or repeat strategy, software versions, compute infrastructure, and runtime.
- Add an optional "Reproducibility" section when it resolves likely reviewer doubts, but do
  not depend on supplementary material for central claims.

## Output format

```text
[Result inventory] <claim -> evidence location>
[Rubric target] convincing / credible / currently weak
[Missing details] <algorithm/theory/data/compute/hyperparameters/seeds>
[Paper fixes] <must be in main PDF>
[Supplement fixes] <optional or supporting evidence>
```
