---
name: jpam-research-design
description: Use when defending the causal identification of a Journal of Policy Analysis and Management (JPAM) manuscript — RCTs, difference-in-differences / event study, regression discontinuity / kink, instrumental variables, and synthetic control for policy and program evaluation. Strengthens the design and its assumptions; it does not write estimation code.
---

# Research Design & Identification (jpam-research-design)

Credible identification is JPAM's **core bar**. The journal evaluates the effects of real policies and
programs, so the design must connect the theory of change (`jpam-theory-building`) to evidence a
policymaker can trust. State the **estimand**, the **assumptions** that license a causal reading, and
**how each is defended** — then rule out the single strongest rival explanation. Selection-on-
observables alone rarely clears the bar.

## When to trigger

- Specifying or defending identification for a policy evaluation
- A reviewer questioned causal claims, parallel trends, the instrument, the discontinuity, or confounding
- Choosing among RCT / DiD / RD / IV / synthetic control for a given policy variation
- Preparing a pre-analysis plan for a prospective program evaluation

## Design menu (match to the policy variation)

- **RCT / field experiment.** The gold standard where feasible. Report randomization unit, balance,
  power/MDE, take-up, attrition, and ITT vs. TOT/LATE. Pre-register primary outcomes and subgroups.
- **Difference-in-differences / event study.** For staggered policy adoption use **heterogeneity-robust
  estimators** (Callaway–Sant'Anna, Sun–Abraham, de Chaisemartin–D'Haultfœuille, BJS imputation) — not
  naive TWFE. Show pre-trends as an event study; test, don't assert, parallel trends.
- **Regression discontinuity / kink.** For eligibility thresholds and benefit formulas. Report
  bandwidth selection, local-polynomial robustness, density/manipulation tests (McCrary/rddensity),
  covariate continuity, and the local nature of the estimand.
- **Instrumental variables.** For policy-induced variation. Defend the exclusion restriction
  *substantively*, report first-stage strength (effective F / weak-IV-robust inference), and interpret
  the LATE — whose behavior the instrument shifts.
- **Synthetic control.** For a single treated unit (a state/country policy). Report donor pool, pre-
  period fit, placebo/permutation inference, and leave-one-out robustness.

## Inference & policy-evaluation standards

- Cluster at the level of treatment assignment; with few clusters use wild-cluster bootstrap.
- Adjust for multiple outcomes/subgroups (and say which test is primary).
- Distinguish **ITT vs. treatment-on-the-treated**; report take-up for any offer-based program.
- Specify the **estimand and target population** — JPAM cares which population the policy decision is about.

## The adjudication test (JPAM-specific)

For the **single strongest rival explanation** (selection, anticipation, concurrent policy, mean
reversion), write one sentence: *"If the rival were driving the result, the data would look like ___;
instead they look like ___."* If you cannot, the design does not yet identify the policy effect.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JPAM is policy analysis — program evaluation is the core; DiD/IV/RDD and the policy-relevant magnitude are decisive.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference + `romano_wolf` for many-outcome control.
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the magnitude in interpretable units; route the full battery to the appendix. A
run end-to-end (synthetic data, real returns) is in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Estimand and target population stated explicitly
- [ ] Identifying assumption named and **defended**, not asserted
- [ ] Modern, heterogeneity-robust estimator for staggered DiD; pre-trends shown
- [ ] RD: bandwidth, density, and covariate-continuity tests reported
- [ ] IV: substantive exclusion argument + first-stage strength + LATE interpretation
- [ ] Clustering at the assignment level; multiple-testing handled
- [ ] Strongest rival explicitly ruled out (adjudication sentence)

## Anti-patterns

- Naive TWFE on staggered policy adoption; clustering at the wrong level
- "Causal effect of the policy" language on a selection-on-observables design
- Asserting parallel trends without an event-study pre-trend test
- A weak or substantively implausible instrument waved through on a high F alone
- Ignoring take-up/attrition so ITT and TOT are conflated
- Over-claiming a local RD/LATE estimate as the average policy effect for the whole population

## Calibration anchors (hedged)

- Credible identification is JPAM's price of entry; a real exogenous source of variation typically beats
  a richer set of controls on the same selection problem.
- The estimand JPAM cares about is the one the policy decision is about — be explicit when an RD/LATE is
  *local* and the decision concerns a broader population, and discuss external validity rather than
  papering over it.
- For staggered policy rollouts, default to a heterogeneity-robust estimator and show the underlying
  TWFE bias (e.g., a Goodman-Bacon decomposition) if a reviewer expects it.

## Worked micro-example (illustrative)

A state raises a benefit eligibility threshold; the team uses an **RD at the income cutoff**. The design
write-up states the estimand (effect at the threshold), defends continuity (covariates smooth across the
cutoff, no manipulation by a density test), reports bandwidth and local-polynomial robustness, and
**adjudicates the strongest rival**: *"If families were sorting just under the cutoff to qualify, the
running-variable density would spike there; it does not."* It then flags that the estimate is **local**
and discusses how it might differ away from the threshold. (Illustrative.)

## Output format

```
【Design】RCT / DiD-event-study / RD-kink / IV / synthetic control
【Estimand + population】what is identified, for whom
【Key assumption(s)】and how each is defended
【Rival ruled out】the adjudication sentence
【Inference】clustering, multiple-testing, weak-IV plan
【Next】jpam-data-analysis
```

## Supplementary resources

- [`../../resources/code/`](../../resources/code/) — runnable DiD / IV / RD / DML skeletons (Stata + Python)
- [`../../../shared-resources/empirical-methods/reviewer-objection-checklist.md`](../../../shared-resources/empirical-methods/reviewer-objection-checklist.md) — objections by identification strategy, each with a preemption
