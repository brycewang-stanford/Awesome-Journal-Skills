---
name: jom-data-analysis
description: Use when running and reporting the statistical analysis for a Journal of Operations Management (JOM) empirical manuscript — measurement validity for survey constructs, identification and endogeneity for archival operations data, manipulation checks for behavioral-OM experiments, and robustness. Executes and reports the analysis; it does not design the study (jom-methods) or frame the contribution (jom-contribution-framing).
---

# Data Analysis & Validity for Empirical OM (jom-data-analysis)

## When to trigger

- Operations data are collected and it is time to estimate and report
- You are unsure whether your estimator matches your design (survey constructs, archival panel, experiment, multilevel/nested plants)
- Reviewers (and the Empirical Research Methods Department) will probe measurement, common-method bias, or endogeneity
- A decision letter says "the analysis does not support the operational inference"

## Establish measurement before estimation (survey/behavioral)

For survey-based OM constructs, defend the measurement model first:

- **Reliability:** Cronbach's alpha and/or composite reliability for each multi-item operations scale.
- **CFA:** report fit (CFI, TLI, RMSEA, SRMR) and show the hypothesized factor structure beats plausible alternatives (one-factor, combined-factor).
- **Convergent & discriminant validity:** AVE per construct; AVE > inter-construct squared correlations (or HTMT). Report the correlation matrix with reliabilities on the diagonal.
- **Aggregation** (plant/team level): justify with ICC(1), ICC(2), r_wg(j) before aggregating respondents.
- **Qualitative/IBR:** establish trustworthiness — data structure (first-order → themes → dimensions), audit trail, representative evidence so the path from observation to construct is traceable.

## Choose the estimator that matches the design

| Operations data structure / claim                    | Estimator                                                  |
|------------------------------------------------------|-------------------------------------------------------------|
| Latent constructs, mediation, full survey model      | SEM (covariance-based) or PLS-SEM where prediction/formative |
| Nested data (respondents in plants/firms)            | Multilevel / HLM                                            |
| Archival operations panel with unit heterogeneity    | Fixed/random effects, high-dimensional FE; cluster-robust SE|
| Causal claim from secondary data                     | DiD/staggered DiD, IV/2SLS, matching, RD as the design fits |
| Count outcomes (recalls, defects, disruptions)       | Poisson / negative binomial                                 |
| Time-to-event (failure, project completion)          | Cox / parametric survival                                  |
| Manipulated operational decision                     | ANOVA/regression with manipulation & attention checks       |

Cluster standard errors to the sampling/operational structure (plant, firm, supply tie).

## Common-method bias (survey OM)

Report the *designed* separations from `jom-methods` first (temporal/source/respondent separation), then statistical evidence: a Harman single-factor test is necessary but weak — prefer a marker variable, an unmeasured latent method factor, or showing interaction effects survive. Multi-respondent dyadic data is the strongest procedural remedy.

## Endogeneity (archival OM)

Recalls, supplier ties, lean adoption, and disruptions are rarely exogenous. State the threat (selection, reverse causality, omitted operational confounds), the identification strategy, and its assumptions. Report first-stage strength for IV and parallel-trends/anticipation checks for DiD.

## Robustness

- Alternative specifications (controls in/out, alternative operational measures, subsamples by industry/regime).
- Sensitivity to identification assumptions.
- Attrition/missing-data handling (FIML/multiple imputation, not listwise by default).
- Reproducible secondary-data construction consistent with the Wiley Data Availability Statement.

## Anti-patterns

- OLS on nested plant data ignoring non-independence.
- Causal-steps mediation instead of bootstrapped indirect effects.
- Single-factor test as the sole CMB defense.
- Unaddressed endogeneity in archival operations regressions.
- p-values with no effect sizes or operational magnitude.

## Output format

```
【Measurement】alpha/CR, CFA fit, AVE/discriminant (survey) — pass/issues
【Estimator】SEM / HLM / panel-FE / DiD-IV / count / survival / experiment; SE clustering ...
【CMB / identification】designed separation + test; or endogeneity strategy + assumptions ...
【Mediation/Moderation】bootstrap CI / simple slopes reported? ...
【Robustness】...
【Next step】jom-contribution-framing
```
