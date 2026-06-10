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

## Diagnostic-to-archive map by design

For each design, JAE referees expect a named diagnostic *and* the script that produces it in the eventual deposit:

| Design | Load-bearing diagnostic | Archive artifact |
| --- | --- | --- |
| VAR / shock identification | Robustness across identification schemes; lag-order sensitivity | `var_ident.do` + exported IRF CSVs |
| Dynamic panel GMM | Hansen J, AR(2), instrument count vs. N | `gmm_diag.do` + instrument-matrix log |
| IV / 2SLS | Effective first-stage F; Anderson–Rubin CI; overid test | `iv_firststage.R` + AR-interval table |
| Staggered DID / event study | Pre-trend test; heterogeneity-robust estimator comparison | `did_pretrends.R` + event-study CSV |
| RDD | Density (manipulation) test; bandwidth sensitivity curve | `rd_density.R` + bandwidth grid output |
| Forecasting | Out-of-sample loss comparison; stability over subsamples | `oos_eval.R` + rolling-window results |

A blank archive-artifact cell means the defense exists only as prose — at this journal that counts as no defense.

## Worked example: an external-instrument pass-through IV (illustrative)

Estimand: the 12-month price response to a 1% exchange-rate movement. Instrument: foreign monetary-policy surprises. First pass: effective F ≈ 8 — below comfort. The JAE-grade response is not to bury it: report the 2SLS estimate 0.31 (s.e. 0.09) *next to* an Anderson–Rubin 95% interval [0.07, 0.61], show OLS (0.18, s.e. 0.04) for the endogeneity direction, and add a stronger-instrument subsample where F ≈ 19 and the AR interval tightens. Every column maps to one script in the deposit; the readme names which table each program rebuilds.

## Where JAE referees push back on identification

- "Parallel trends asserted, not shown" → add the pre-trend event study and a heterogeneity-robust estimator; archive both.
- "Instrument count grows with T" → collapse the GMM instrument matrix, re-report Hansen J, and state the count in the table.
- "Identification scheme drives the IRFs" → show recursive vs. sign vs. external-instrument results side by side in the appendix.
- "This diagnostic is not in the package" → treat as a code bug: add the script, rerun, update the exhibit.

## Identification appendix block

```text
Estimand: [population object, one sentence]
Assumption A1: [statement] → Test: [diagnostic] → Script: [file] → Result: [pass/fail + number]
Assumption A2: ...
Confidential-data note: [access path readers can follow, if applicable]
```

## Output format

```
【Estimand】one sentence
【Design】time-series / panel / IV-GMM / quasi-experiment / forecasting
【Assumptions】each has a test? [Y/N]
【Inference】matched to design? [Y/N]
【Reproducible】every diagnostic regeneratable? [Y/N]
【Map】each assumption → test → script → exhibit complete? [Y/N]
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — estimators and inference packages
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — Data Archive reproducibility sources
