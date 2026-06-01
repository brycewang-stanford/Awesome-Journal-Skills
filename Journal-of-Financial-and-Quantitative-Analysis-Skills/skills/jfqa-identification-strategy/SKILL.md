---
name: jfqa-identification-strategy
description: Build a credible identification / research design for a Journal of Financial and Quantitative Analysis (JFQA) empirical finance paper — portfolio sorts and Fama-MacBeth, panel fixed effects, staggered DID on regulatory shocks, IV / natural experiments, RDD at thresholds, and event studies — with the inference finance referees demand. For theoretical submissions, pivot to assumptions, results, and proof exposition.
---

# JFQA Identification Strategy (jfqa-identification-strategy)

Use this skill to make the research design defensible for **JFQA**, an empirical and quantitative finance journal. JFQA referees press hard on whether a correlation is causal (or, in asset pricing, whether a premium is robust and not data-mined).

## Empirical finance designs (the common case)

Pick the design that matches the question and defend it:

- **Cross-section of returns** — portfolio sorts and **Fama-MacBeth** regressions; Newey-West / clustered SEs; control for standard factors; report economic magnitudes (return per one-SD change), not only t-stats; guard against data snooping (out-of-sample, multiple-testing awareness).
- **Corporate finance panels** — **firm and time fixed effects**, two-way clustering; show the variation that identifies the coefficient.
- **Policy / regulatory shocks** — **staggered DID** with a modern estimator (Callaway-Sant'Anna, de Chaisemartin-D'Haultfœuille), event-study leads/lags, and parallel-trends evidence; avoid naive TWFE on staggered timing.
- **Natural experiments / IV** — instrument relevance (first-stage F), exclusion logic backed by an economic story, weak-IV-robust CIs.
- **Thresholds / index reconstitution** — **RDD** with manipulation/density tests and bandwidth robustness.
- **Announcements** — **event study** with CARs/BHARs, a defensible market model, and attention to calendar clustering.

## What referees demand

- The right standard errors (clustering dimension justified, two-way where needed).
- Economic significance reported alongside statistical significance.
- Endogeneity confronted explicitly, not waved away with "controls."

## Theoretical submissions

JFQA also publishes theory. If your paper is a model, pivot this skill to: stating **assumptions** transparently, deriving **results/propositions**, clean **proof exposition**, and **testable implications** a finance reader can take to data. Keep generality matched to the question.

## Output format

```
【Design】sorts/FMB / panel FE / staggered DID / IV / RDD / event study / theory
【Identifying variation】what makes it credible
【Inference】clustering / weak-IV / multiple-testing handling
【Economic magnitude】effect size in finance units
【Next step】jfqa-data-analysis
```
