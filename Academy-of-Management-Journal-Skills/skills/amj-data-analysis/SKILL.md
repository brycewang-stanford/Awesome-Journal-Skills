---
name: amj-data-analysis
description: Use when running and reporting the statistical analysis for an Academy of Management Journal (AMJ) manuscript — measurement validity, common-method bias, the right estimator (HLM, SEM, panel, experiments), endogeneity, and robustness. Executes and reports the analysis; it does not design the study (amj-methods) or frame the contribution (amj-contribution-framing).
---

# Data Analysis & Validity (amj-data-analysis)

## When to trigger

- Data are collected and it is time to estimate and report
- You are unsure whether your estimator matches your design (nested data, latent constructs, panel)
- Reviewers will probe measurement validity, common-method bias, or endogeneity
- Interaction/mediation effects need correct testing and reporting
- A reviewer says "the analysis does not support the inference" or "validity is not established"

## Establish measurement before estimation

AMJ reviewers expect the measurement model to be defended first:

- **Reliability**: Cronbach's alpha and/or composite reliability for each multi-item scale.
- **Confirmatory factor analysis (CFA)**: report fit (e.g., CFI, TLI, RMSEA, SRMR) and show the hypothesized factor structure fits better than plausible alternatives (one-factor, combined-factor models).
- **Convergent & discriminant validity**: AVE per construct; AVE > inter-construct squared correlations (or HTMT). Report the correlation matrix with reliabilities on the diagonal.
- **Aggregation** (multilevel): justify with ICC(1), ICC(2), and r_wg(j) before aggregating to a higher level.
- **Qualitative analysis**: where the design is qualitative, "validity" becomes trustworthiness — present a Gioia-style data structure (first-order codes → second-order themes → aggregate dimensions), an audit trail, and representative quotations so the path from raw data to constructs is traceable.

## Choose the estimator that matches the design

| Data structure / claim                       | Estimator                                                   |
|-----------------------------------------------|-------------------------------------------------------------|
| Latent constructs, mediation, full model      | Structural equation modeling (SEM)                          |
| Nested data (indiv. in teams/firms)           | Multilevel / hierarchical linear modeling (HLM)             |
| Panel with unit heterogeneity                 | Fixed/random effects; cluster-robust SE                     |
| Manipulated cause                             | ANOVA/regression with manipulation & attention checks       |
| Endogenous archival regressor                 | 2SLS/IV, DiD, Heckman, propensity matching (per design)     |
| Count/limited dependent variable              | Poisson/negative binomial, logit/probit, Tobit as fits      |

Match clustering of standard errors to the sampling/nesting structure.

## Common-method bias (CMB)

Report the *designed* separations from `amj-methods` first; then provide statistical evidence: a Harman single-factor test is necessary but weak — prefer a marker-variable approach, an unmeasured latent method factor (CFA), or showing interaction effects survive (interactions are hard to inflate by CMB). The Podsakoff et al. framework is the expected reference for both procedural and statistical remedies.

## Reporting mediation, moderation, and effect sizes

- **Mediation**: report indirect effects with bias-corrected bootstrap confidence intervals (e.g., 5,000 resamples); report the conditional indirect effect for moderated mediation.
- **Moderation**: report the interaction coefficient *and* plot simple slopes with significance regions; report incremental variance from the interaction.
- **Effect sizes**: report standardized coefficients/effect sizes and discuss practical magnitude, not just p-values.

## Robustness

- Alternative specifications (controls in/out; alternative measures; subsamples).
- Sensitivity to endogeneity assumptions (e.g., alternative instruments, bounds).
- Address alternative explanations empirically where possible.
- Report attrition/missing-data handling (FIML/multiple imputation, not listwise by default).

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). AMJ is empirical management — panel, multilevel, DiD, IV, and field/lab experiments; the chain below serves that lane, while grounded-theory / qualitative work uses its own standards.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or
  `benjamini_hochberg` — report the adjusted threshold.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`;
  multilevel data → cluster at the right level.
- **Re-fit off one handle:** `audit_result(result_id)` lists the missing checks and the
  exact `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Keep the decisive checks in the body and the exhaustive battery in the appendix. See the
executed chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Reliabilities, CFA fit, AVE, and discriminant validity reported
- [ ] Correlation table with reliabilities on the diagonal included
- [ ] Estimator matches design (SEM/HLM/panel/experiment), SEs clustered appropriately
- [ ] CMB addressed beyond a single-factor test
- [ ] Mediation via bootstrap CIs; moderation via simple slopes + incremental variance
- [ ] Endogeneity strategy executed and its assumptions discussed (archival)
- [ ] Robustness checks and alternative-explanation tests reported
- [ ] Missing-data and aggregation decisions documented

## Anti-patterns

- **OLS on nested data** ignoring non-independence (use HLM).
- **Baron-Kenny causal-steps only** for mediation instead of bootstrapped indirect effects.
- **p-hacking / selective controls**: results that appear only with a particular control set.
- **Single-factor test as the sole CMB defense.**
- **Significant squared term = "curvilinear"** with no turning-point or theoretical check.
- **Reporting p-values with no effect sizes** or practical interpretation.

## Output format

```
【Measurement】alpha/CR, CFA fit (CFI/TLI/RMSEA/SRMR), AVE/discriminant: pass/issues
【Estimator】SEM / HLM / panel-FE / experiment / IV-DiD; SE clustering ...
【CMB evidence】designed separation + statistical test ...
【Mediation/Moderation】bootstrap CI / simple slopes reported? ...
【Endogeneity】strategy executed; assumptions discussed ...
【Robustness】[...]
【Open issues for reviewers】[...]
【Next step】amj-contribution-framing
```
