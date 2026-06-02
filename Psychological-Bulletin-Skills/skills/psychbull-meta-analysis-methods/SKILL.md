---
name: psychbull-meta-analysis-methods
description: Use when computing effect sizes and fitting the meta-analytic model for a Psychological Bulletin manuscript — effect-size metrics, random-effects vs. fixed-effect choice, dependent effect sizes (RVE / multilevel), and heterogeneity (Q, I², τ², prediction interval). Guides the core synthesis; moderators and bias diagnostics live in psychbull-moderators-and-bias.
---

# Meta-Analysis Methods (psychbull-meta-analysis-methods)

This is the quantitative core of a Psychological Bulletin meta-analysis: turning coded study
statistics into **effect sizes**, pooling them under a defensible **model**, and characterizing
**heterogeneity** honestly. Psychological Bulletin expects **MARS**-compliant methods. This skill
covers estimation; moderators and publication-bias diagnostics live in `psychbull-moderators-and-bias`.

## When to trigger

- Computing effect sizes from coded statistics
- Choosing fixed-effect vs. random-effects (vs. multilevel) models
- Handling **multiple effect sizes per study** (dependency)
- Quantifying and interpreting **heterogeneity**

## Effect sizes

- Pick a metric that matches the designs and is comparable across studies: **standardized mean
  difference (Hedges' g, small-sample corrected)**, **correlation r → Fisher's z**, **log odds
  ratio / risk ratio**. Convert disparate metrics to a common scale and document conversions.
- Compute with a transparent tool (e.g., `metafor::escalc`); record the formula and the inputs used.
- Track the **direction/sign** so effects align with the substantive hypothesis.

## Model choice

1. **Random-effects (or mixed-effects) by default.** Psychological literatures vary across
   populations, measures, and procedures, so a common true effect is implausible; estimate τ² and a
   summary effect with a **random-effects** model. Justify any fixed-effect use explicitly.
2. **Dependent effect sizes** (multiple per study/sample) violate independence. Use **robust variance
   estimation (RVE)** (`robumeta`/`clubSandwich`) or a **multilevel/three-level** model
   (`metafor::rma.mv`); do not naively treat all effects as independent.
3. **Weighting** by inverse variance; report the estimator for τ² (e.g., REML).

## Heterogeneity

- Report **Q** (test), **I²** (proportion of variance from heterogeneity), and **τ²/τ** (absolute
  between-study SD), plus a **prediction interval** for the range of true effects.
- Interpret heterogeneity substantively — it motivates the **moderator** analysis, it is not a nuisance
  to hide. High heterogeneity with a tiny CI on the mean can mislead without the prediction interval.

## Anti-patterns

- A fixed-effect model imposed on an obviously heterogeneous literature
- Treating multiple effects per study as independent (understated SEs)
- Reporting only the pooled point estimate and CI, with no I²/τ²/prediction interval
- Mixing incomparable effect-size metrics without conversion
- Letting reported numbers diverge from the analysis script (the database is deposited and checkable)

## Output format

```
【Effect-size metric】g / z(r) / logOR + conversions noted
【Model】random-effects / multilevel / RVE (+ τ² estimator)
【Dependency】handled via RVE / multilevel? [Y/N]
【Pooled effect】estimate + 95% CI
【Heterogeneity】Q, I², τ², prediction interval
【Next】psychbull-moderators-and-bias
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — `metafor`, `robumeta`/`clubSandwich`, Stata `meta`, CMA
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — MARS reporting of model, effect sizes, heterogeneity
