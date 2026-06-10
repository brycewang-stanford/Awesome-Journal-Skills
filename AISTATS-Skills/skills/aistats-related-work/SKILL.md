---
name: aistats-related-work
description: Use when positioning an AISTATS submission against AI, machine-learning, statistics, and uncertainty literature, including arXiv preprints, workshop versions, concurrent submissions, prior conference versions, PMLR archival status, and the two-community citation coverage that AISTATS reviewers expect.
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

## Two-community coverage table

| Literature lane | Typical sources | What AISTATS reviewers check |
|---|---|---|
| ML conferences | NeurIPS, ICML, ICLR, UAI, COLT, prior AISTATS volumes in PMLR | Whether the nearest ML method is compared or explicitly distinguished |
| Statistics journals | Annals of Statistics, JMLR, JASA, Biometrika, EJS | Whether classical estimators and known rates are acknowledged |
| Applied statistical fields | Econometrics, biostatistics, epidemiology | Whether identification and inference assumptions follow standard usage |

A bibliography citing only ML venues tells a statistician reviewer that known statistical
results may be getting rediscovered — a recognizable AISTATS reject pattern that no amount
of benchmark strength repairs.

## Positioning vignette

Imagine the paper proposes a variance-reduced off-policy evaluation estimator with an
asymptotic normality result. Its nearest neighbors: a NeurIPS estimator with no inference
guarantee, a JASA semiparametric efficiency bound, and a prior AISTATS paper with a slower
rate. The novelty sentence should name all three contrasts — inference where the ML line had
none, computational tractability where the statistics line stayed abstract, and a sharper
rate than the direct predecessor.

## Concurrent-work judgment calls

- Independently concurrent arXiv work: cite neutrally, state the technical difference, and
  avoid priority claims that reviewers cannot verify.
- Your own workshop version: typically non-archival and citable, but verify against the
  current CFP wording and keep the citation phrased so double-blind review survives.
- When in doubt about archival status of a venue, declare the overlap in the submission form
  rather than gambling on a chair's interpretation.

## Output format

```text
[Eligibility] clear / needs declaration / risky
[Closest literatures] <ML/statistics/application>
[Nearest 3 works] <work -> distinction>
[Archival-overlap risk] <none/issues>
[Novelty sentence] <AISTATS-ready contribution contrast>
```
