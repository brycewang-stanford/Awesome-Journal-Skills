---
name: jm-data-analysis
description: Use when running and reporting the statistical analysis for a Journal of Marketing (JM) manuscript — the right estimator for a big-tent design, JM's exact p-value / standard-error / effect-size reporting mandate, identification and robustness, and the JM Dataverse replication packet. Executes and reports the analysis; it does not design the study (jm-methods) or frame the contribution (jm-contribution-framing).
---

# Data Analysis & Reporting (jm-data-analysis)

## When to trigger

- Data are collected and it is time to estimate and report
- You are unsure your estimator matches a big-tent design (experiment, panel, choice, qualitative)
- A reviewer will probe identification, robustness, or whether the effect is *managerially* meaningful
- You reached conditional acceptance and must assemble the JM Dataverse replication packet

## JM's hard reporting mandate (non-negotiable)

JM's submission rules bake in statistical transparency. Empirical papers **must report**:

- **Actual p-values** — not thresholds such as "p < .05" or stars-only tables.
- **Standard errors** for estimates.
- **Effect sizes** — the *magnitude* of the effect, because JM judges substantive and managerial importance, not mere significance.

Report these throughout the main text and tables. A results section that shows significance without magnitude fails JM's substantive bar: an effect that is "significant" but trivially small rarely changes a managerial decision.

## Choose the estimator that matches the design

| Design / claim                                    | Estimator                                                   |
|---------------------------------------------------|-------------------------------------------------------------|
| Randomized experiment (lab/online)                | ANOVA / regression with manipulation & attention checks     |
| Field experiment with a firm/platform             | Regression on randomized treatment; cluster-robust SE       |
| Process / mechanism                               | Mediation (bootstrapped indirect effects); moderation-of-process |
| Preferences / trade-offs                          | Choice models (logit/mixed logit), conjoint, hierarchical Bayes |
| Observational panel / market data                 | FE / high-dimensional FE; DiD / event study; synthetic control; IV/2SLS |
| Customer-base dynamics                            | CLV / hazard / count models on longitudinal data            |
| Limited / count dependent variable                | Logit/probit, Poisson/negative binomial, Tobit as fits      |
| Qualitative                                       | Transparent coding: codes → themes → constructs, audit trail |

Cluster standard errors to the design's randomization/sampling structure.

## Identification, mechanism, and robustness

- **Identification (secondary data)**: state the source of exogenous variation; defend parallel trends (DiD), instrument relevance/exclusion (IV), or the donor pool (synthetic control). Address endogeneity head-on.
- **Mediation**: report indirect effects with bias-corrected bootstrap CIs (e.g., 5,000 resamples); report conditional indirect effects for moderated mediation.
- **Moderation**: report the interaction coefficient *and* plot simple slopes; report incremental variance.
- **Robustness**: alternative specifications, measures, and subsamples; rule out alternative explanations empirically; report exclusions and missing-data handling explicitly.

## Effect size in managerial units

Translate effects into terms a decision maker reads: elasticities, lift in sales/conversion/CLV, willingness-to-pay in currency, welfare changes. This is how JM's dual mandate shows up in the results section.

## JM Dataverse replication packet (at conditional acceptance)

JM's Research Transparency Policy applies to conditionally accepted revisions of manuscripts submitted on/after 2023-01-01. At conditional acceptance, deposit to **JM's Dataverse**: raw data files, analysis programs/scripts, and any details sufficient to **replicate all reported analyses**; for qualitative work, interview guides, coding procedures, and annotated examples. The packet is accessible to the **processing Editor**, not reviewers. A **Data Availability Statement** is required on the title page of the final manuscript. **Preregistration is encouraged** — supply anonymized links and attest you faithfully represented the preregistration. (JM does not specify a dedicated Data-Editor verification step the way JMR does — 待核实.)

## Checklist

- [ ] **Actual p-values, standard errors, and effect sizes reported throughout**
- [ ] Estimator matches the design; SEs clustered appropriately
- [ ] Identification strategy stated and defended (secondary data)
- [ ] Mediation via bootstrap CIs; moderation via simple slopes + incremental variance
- [ ] Effect sizes translated into managerial units (lift, elasticity, WTP, welfare)
- [ ] Robustness, alternative explanations, exclusions, and missing data reported
- [ ] Replication packet prepared for JM Dataverse; Data Availability Statement drafted
- [ ] Preregistration links + attestation ready (if applicable)

## Anti-patterns

- **Significance without magnitude** — stars-only tables; "p < .05" with no effect size.
- **Estimator/design mismatch** — e.g., OLS ignoring panel structure or clustering.
- **Unaddressed endogeneity** in observational data.
- **Baron-Kenny causal-steps only** instead of bootstrapped indirect effects.
- **Retrofitted replication** — code that does not regenerate the reported tables.

## Output format

```
【Estimator】experiment / field / choice / panel-DiD / qualitative; SE clustering ...
【Exact statistics】p-values + SEs + effect sizes reported? yes/no
【Identification】strategy + defense (DiD/IV/synthetic control) ...
【Mediation/Moderation】bootstrap CI / simple slopes reported? ...
【Managerial magnitude】lift / elasticity / WTP / welfare ...
【Robustness】[...]
【JM Dataverse packet】data + code (+ qualitative materials) ready? Data Availability Statement?
【Next step】jm-contribution-framing
```
