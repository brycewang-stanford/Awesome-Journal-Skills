---
name: devpsych-data-analysis
description: Use when analyzing and reporting results for a Developmental Psychology (APA) manuscript. The journal expects analyses that model developmental change correctly — growth-curve/multilevel/SEM, mediation/moderation, measurement invariance — with effect sizes and confidence intervals, JARS-compliant disclosure, and a clear confirmatory/exploratory split. Guides analysis norms; it does not fabricate results.
---

# Data Analysis (devpsych-data-analysis)

Developmental Psychology holds analyses to a developmental and a credibility standard at once: the model
must actually capture **change** (not just a cross-sectional snapshot), and reporting must meet **JARS** —
**effect sizes with confidence intervals**, full disclosure, and a clean **confirmatory vs. exploratory**
split. The most common fatal error is interpreting trajectories without first establishing that the
construct is measured the same way across ages.

## When to trigger

- Fitting growth-curve / multilevel / SEM models, or mediation/moderation of developmental effects
- A reviewer asked for measurement invariance, effect sizes, intervals, or attrition handling
- Reconciling preregistered developmental hypotheses with exploratory trajectory findings
- Preparing analysis scripts and a data dictionary for deposit

## Reporting norms Developmental Psychology expects

1. **Model change correctly.** Use the method the claim requires: **latent growth / multilevel models**
   for trajectories, **SEM** for latent constructs, **cross-lagged / RI-CLPM** for reciprocal effects,
   **mediation/moderation** for mechanism and moderated change. State time coding and centering.
2. **Establish measurement invariance first.** Test **configural → metric → scalar** across ages/waves
   *before* interpreting mean change; report partial invariance honestly if full scalar fails.
3. **Effect sizes + uncertainty.** Report a standardized or unstandardized effect size **and confidence
   intervals** for major results — slope estimates, interactions, indirect effects — not just stars.
4. **Handle missing data and attrition principledly.** Use **FIML or multiple imputation**; report the
   attrition analysis (completers vs. dropouts) and the missingness assumption.
5. **JARS disclosure.** Report how sample size was determined, all exclusions and reasons, all conditions
   and measures; keep confirmatory and exploratory analyses clearly separated.
6. **Reproducibility.** Provide analysis scripts and a data dictionary; the numbers should regenerate in
   a fresh session (see `devpsych-open-science-and-transparency`).

## Worked micro-example (illustrative numbers)

A preregistered three-wave latent-growth study (ages 4, 6, 8; N = 300, 18% attrition) of effortful
control, testing maternal scaffolding as a driver of the growth slope.

```
Invariance (reported first):
  configural fit good; metric and scalar invariance hold across waves
  (ΔCFI < .01) → mean change is interpretable.
Confirmatory (preregistered):
  Latent slope > 0: b = 0.42/year, 95% CI [0.31, 0.53] (within-person growth).
  Scaffolding × time: b = 0.18, 95% CI [0.07, 0.29] (steeper growth with
  higher wave-1 scaffolding).
  Missing data: FIML; MAR; completers and dropouts did not differ on baseline
  covariates (attrition analysis in supplement).
Exploratory (labeled):
  RI-CLPM suggests child→parent effects in later waves; reported as
  exploratory and flagged for confirmation in a future sample.
```

Why this passes scrutiny: invariance is reported *before* the growth claim; every developmental parameter
carries an effect size and a CI; missingness is modeled, not deleted; the reciprocal-effects finding is
honestly demoted to exploratory.

## Analysis-stage reviewer pushback and the venue fix

| Reviewer pushback | What it signals here | Developmental Psychology fix |
|-------------------|----------------------|------------------------------|
| "Is the construct the same at each age?" | invariance not tested | report configural→metric→scalar before interpreting change |
| "You deleted dropouts" | attrition bias | refit with FIML/MI; add the completers-vs-dropouts analysis |
| "ANOVA on age groups for a change claim" | wrong model for the claim | fit a growth/multilevel model on within-person data |
| "Stars, no effect size" | pre-reform reporting | report slope/interaction effect sizes with CIs |
| "Is this confirmatory?" | HARKing concern | point to preregistration; relabel post hoc trajectories exploratory |

## Calibration anchors

- A clean latent-growth slope with a tight CI, on an invariant measure, beats an age-group ANOVA with
  stars — the venue's currency is credible *change*, not a snapshot contrast.
- Prefer estimation language ("effortful control grew 0.42/year, 95% CI [...]") to "significant effect of
  age." Bare p-value sentences read as thin here.
- When attrition is non-trivial, state the missingness assumption and show the trajectory is robust to a
  reasonable alternative (e.g., pattern-mixture sensitivity), rather than implying complete data.

## Anti-patterns

- Interpreting mean change without establishing measurement invariance
- Listwise deletion or ignoring differential attrition
- Using age-group ANOVA to support a within-person change claim
- p-values and stars with no effect sizes or confidence intervals
- HARKing exploratory trajectory shapes into confirmatory hypotheses

## Output format

```
【Model】growth / multilevel / SEM / cross-lagged / mediation-moderation — matches the change claim?
【Invariance】configural→metric→scalar tested before interpreting change? [Y/N]
【Main result】effect size + confidence interval + meaning
【Missing data】FIML/MI + attrition analysis reported? [Y/N]
【Confirmatory vs exploratory】clearly separated (JARS)? [Y/N]
【Reproducible】scripts + data dictionary + fresh-session check? [Y/N]
【Next】devpsych-tables-figures
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — `lavaan`, Mplus, `lme4`/`nlme`, `semTools` invariance, `mice`, effect-size tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — JARS statistical and disclosure requirements
