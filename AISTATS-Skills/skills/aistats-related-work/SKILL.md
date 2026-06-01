---
name: aistats-related-work
description: Use when positioning an AISTATS submission against AI, machine-learning, statistics, and uncertainty literature, including arXiv preprints, workshop versions, concurrent submissions, prior conference versions, and PMLR archival status.
---

# AISTATS Related Work

Use this to audit novelty and eligibility. Reopen the current CFP for dual-submission,
anonymity, and prior-publication rules before advising authors.

## Positioning checks

- Separate statistical novelty from engineering improvement: new estimator, bound,
  inference procedure, optimization analysis, uncertainty method, or empirical insight.
- Compare to both ML conference work and statistics literature; AISTATS reviewers often
  expect both communities to be represented.
- Treat PMLR, journal, and formal conference proceedings as archival unless current rules say
  otherwise.
- Cite arXiv and workshop versions in a way that preserves double-blind review. Do not point
  reviewers to identity-revealing pages.
- Explain overlap with any concurrent or prior version, and do not submit duplicate archival
  work.
- Use related work to sharpen what is new: assumption weakening, finite-sample behavior,
  computational efficiency, uncertainty calibration, robustness, or empirical regime.

## Output format

```text
[Eligibility] clear / needs declaration / risky
[Closest literatures] <ML/statistics/application>
[Nearest 3 works] <work -> distinction>
[Archival-overlap risk] <none/issues>
[Novelty sentence] <AISTATS-ready contribution contrast>
```
