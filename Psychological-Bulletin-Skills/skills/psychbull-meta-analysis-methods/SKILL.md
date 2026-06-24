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

## Execution bridge (StatsPAI / Stata MCP)

Meta-analysis itself is largely **outside** this causal-inference toolchain — use
dedicated tools (e.g. metafor) for pooled effects and meta-regression. Full map (for
primary-study reanalysis): [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Psychological Bulletin is a meta-analytic review venue.

- **Moderator / meta-regression tests:** apply the multiple-testing haircut
  (`romano_wolf` / `benjamini_hochberg`) — many moderators inflate false positives.
- **Reanalyzing a primary dataset:** the design→fit→audit chain applies
  (`detect_design` → `recommend` → fit → `audit_result`).
- **Exhibits:** `etable` / `plot_from_result` for any reanalysis tables/figures.

Be explicit about what is meta-analytic (dedicated tools) vs primary reanalysis
(this chain). [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Anti-patterns

- A fixed-effect model imposed on an obviously heterogeneous literature
- Treating multiple effects per study as independent (understated SEs)
- Reporting only the pooled point estimate and CI, with no I²/τ²/prediction interval
- Mixing incomparable effect-size metrics without conversion
- Letting reported numbers diverge from the analysis script (the database is deposited and checkable)

## Model-choice expectations at the review flagship

Psychological Bulletin, the APA's flagship review journal, expects state-of-the-art meta-analytic
modeling — the model is where methods reviewers concentrate. The decision table they apply:

| Methodological choice | Defensible at this venue | Major-revision / reject trigger |
|-----------------------|--------------------------|----------------------------------|
| Model | Random-effects (or mixed) by default, justified | Fixed-effect imposed on a heterogeneous literature |
| Dependency | RVE or three-level model for clustered effects | Multiple effects per study treated as independent |
| Heterogeneity reporting | Q, I², τ², *and* a prediction interval | Only the pooled point estimate and its CI |
| τ² estimator | Named (REML) and reported | Default estimator, unstated |
| Metric comparability | Disparate metrics converted and documented | g and r mixed without conversion |

## Worked vignette — fitting the pooled model

*Illustrative numbers only — not real data.* The self-affirmation synthesis codes 51 effects from
k = 42 studies (9 studies contribute 2–4 effects each). Under this skill's rules:

- **Effect size**: Hedges' g with small-sample correction; 6 effects originally reported as r or t are
  converted to g and the conversions are documented.
- **Model**: a random-effects estimate is implausible to treat as a single true effect across varied
  populations, so REML random-effects is the base; clustered effects are handled with RVE
  (`robumeta`/`clubSandwich`) so the nine multi-effect studies do not understate the SEs.
- **Pooled result**: g = 0.34, 95% CI [0.24, 0.44].
- **Heterogeneity**: Q(41) significant, I² = 68%, τ² = 0.041 (τ = 0.20), and a 95% prediction interval
  of roughly [−0.10, 0.78] — far wider than the CI, which is the honest signal that true effects vary
  and motivates the moderator analysis rather than a single-number headline.

## Referee pushback → venue-specific fix

- *"You report a CI but no prediction interval."* → Add the PI; with I² = 68% the CI alone misleads
  about the spread of true effects across settings.
- *"Multiple effects per study were treated as independent."* → Refit with RVE or a three-level model and
  report how the SEs and τ² change.
- *"A fixed-effect model is indefensible here."* → Switch to random-effects, justify in text, and name
  the τ² estimator.

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
