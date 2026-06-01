---
name: jape-identification-strategy
description: Use when designing or defending the empirical identification of a Journal of Applied Econometrics (JAE) manuscript — a credible strategy applied to real data, with assumptions stated, tested, and reproducible. Covers time-series, panel, IV, and quasi-experimental designs typical of applied econometrics, tying every claim to depositable evidence.
---

# Identification Strategy for JAE (jape-identification-strategy)

## When to trigger

- Choosing or defending the empirical design for a JAE paper
- A referee questions whether the estimand is identified on your real data
- Mapping each identifying assumption to a test you can deposit in the archive

## JAE is applied: identification on real data

JAE publishes **applications on real data**, so identification is a *credible empirical strategy*, not a theorem. The bar: a clearly stated **estimand**, **explicit identifying assumptions**, and **diagnostics that test them**, all reproducible from deposited code/data. Separate the econometric object from the substantive claim, and justify causal language with the *design*, not estimator branding.

## Common designs and load-bearing assumptions

- **Time-series / macro-econometrics** (common at JAE): unit-root and cointegration handling; lag selection; shock identification (recursive, sign, external instruments); HAC inference. Show robustness to lag length and identification scheme.
- **Panel / dynamic panel**: strict vs. sequential exogeneity; GMM instrument validity (Hansen/Sargan, AR(2)); avoid instrument proliferation.
- **IV / GMM**: relevance (first-stage / effective F) and exogeneity; weak-IV-robust inference; over-identification tests.
- **Quasi-experimental (DID, event study, RDD)**: parallel trends / continuity; modern estimators under staggered timing or heterogeneity; placebo and pre-trend tests.
- **Forecasting / structural**: define the loss function, information set, and stability assumptions.

## Reproducibility is part of identification

Every check must be **regeneratable** from the programs you will deposit in the **JAE Data Archive**. With confidential data, the readme must describe the source and extraction well enough for others to apply for access and re-run it. A diagnostic you cannot reproduce is not a defense.

## Output format

```
【Estimand】one sentence
【Design】time-series / panel / IV-GMM / quasi-experiment / forecasting
【Assumptions】each has a test? [Y/N]
【Inference】matched to design? [Y/N]
【Reproducible】every diagnostic regeneratable? [Y/N]
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — estimators and inference packages
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — Data Archive reproducibility sources
