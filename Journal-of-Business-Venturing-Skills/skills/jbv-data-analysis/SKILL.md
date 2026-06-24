---
name: jbv-data-analysis
description: Use when running and reporting the analysis for a Journal of Business Venturing (JBV) manuscript — choosing estimators that fit entrepreneurial data (survival/event-history, selection models, panels, experiments, qualitative trustworthiness), handling attrition and endogenous founding, and reporting robustness. Executes and reports the analysis; it does not design the study (jbv-methods) or frame the contribution (jbv-contribution-framing).
---

# Data Analysis & Validity (jbv-data-analysis)

## When to trigger

- Data are collected and it is time to estimate and report
- You are unsure the estimator matches an entrepreneurial-data structure (venture survival, founding choice, nested funding events)
- Reviewers will probe survivorship, selection into founding, or endogeneity
- A handling editor says "the analysis does not support the inference about entrepreneurship"

## Match the estimator to the entrepreneurial data structure

JBV is methodologically pluralistic, so the right tool depends on the claim. Common patterns in new-venture data:

| Data structure / claim                                  | Estimator                                                       |
|---------------------------------------------------------|------------------------------------------------------------------|
| Time-to-exit / IPO / failure                            | Survival / event-history (Cox, parametric AFT, competing risks)  |
| Choice to found / endogenous selection                  | Heckman / Roy selection; control function                        |
| Venture panel with unit heterogeneity                   | Fixed/random effects; cluster-robust SE (`reghdfe`, `fixest`)    |
| Policy / ecosystem / financing shock                    | DiD / event study / staggered-adoption estimators                |
| Counts (patents, funding rounds, ventures)              | Poisson / negative binomial; zero-inflated as fits               |
| Binary outcomes (funded, survived)                      | Logit / probit; rare-events corrections where outcomes are rare  |
| Manipulated entrepreneurial judgment                    | ANOVA/regression with manipulation & attention checks            |
| Inductive process / theory-building                     | Gioia data structure, audit trail, representative quotations     |

Cluster standard errors to the sampling/nesting structure (e.g., by cohort, region, accelerator, or industry).

## Handle entrepreneurship-specific threats

- **Survivorship**: report how failed/exited ventures are retained or how their absence is bounded; an analysis on survivors only must say so and qualify the inference.
- **Selection into founding**: model the founding decision or use a design-based identification; do not interpret survivor associations as antecedents of venture creation.
- **Attrition** in nascent panels (PSED/KFS-style): document attrition, test for differential attrition, and use FIML/multiple imputation rather than listwise deletion by default.
- **Endogeneity** of resources/financing/strategy: IV/2SLS, DiD, matching, or control functions, with the identifying assumption stated and probed.

## Robustness expected by JBV reviewers

- Alternative specifications (controls in/out, alternative venture measures, subsamples by stage/region).
- Sensitivity to selection and survivorship assumptions (bounds, alternative frames).
- Rule out the leading alternative explanation for the entrepreneurial finding empirically.
- For experiments: report manipulation/attention checks, effect sizes, and pre-registration if any.

## Reporting

- Report effect sizes and practical magnitude for the entrepreneurial phenomenon, not just p-values.
- For mediation, report indirect effects with bootstrap CIs; for moderation, plot simple slopes.
- For qualitative work, make the path from raw founder data to constructs traceable.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JBV studies founders and ventures where selection / survivorship threatens every claim; lead with identification and selection-correction tooling.

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

- [ ] Estimator matches the structure (survival/selection/panel/experiment/qual)
- [ ] Survivorship and selection into founding addressed, not assumed away
- [ ] Attrition documented; principled missing-data handling
- [ ] Endogeneity strategy executed and identifying assumption discussed
- [ ] SEs clustered to the entrepreneurial sampling structure
- [ ] Robustness + leading-alternative-explanation tests reported
- [ ] Effect sizes and practical magnitude interpreted

## Referee-pushback patterns and the JBV-specific fix

| Reviewer pushback                                         | JBV-specific fix                                                                    |
|-----------------------------------------------------------|-------------------------------------------------------------------------------------|
| "Your sample is survivors; failures are invisible."       | Re-draw the frame from registry/nascent data; bound the survivor bias.              |
| "Founder choices are endogenous."                         | Model founding selection or use a shock; report how the estimate moves.             |
| "A general-management effect on a startup panel."         | Test a moderation that only makes sense for ventures (uncertainty, liability of newness).|

## Worked micro-example (illustrative numbers)

A hypothetical JBV study asks whether prior startup failure raises the *hazard* of a founder's next venture securing Series A. Data: an illustrative panel of second-time founders from a registry frame retaining failed first ventures (so it is not survivor-only).

- **Estimator**: a Cox model for time-to-Series-A, clustered by accelerator cohort. (Illustrative) HR = 1.34, 95% CI [1.08, 1.66].
- **Survivorship guard**: a funded-only frame inflates the HR to ≈ 1.71 — a bias illustration only.
- **Selection guard**: a first-stage probit for "founds again" yields an inverse Mills ratio that moves the HR to 1.28 — still positive, so the inference holds.
- **Effect size**: HR 1.28 implies reaching Series A ~4–5 months sooner at the median, tied to learning-from-failure theory rather than a bare star.

## Calibration anchors (hedged)

- The bar is **identification in service of an entrepreneurship mechanism**; a flawless instrument with no venture-theory payoff still risks a "theory-thin" reject.
- Reviewers weight **process and micro-foundations**: show the entrepreneurial actor's decision in the data, not a reduced-form association alone.
- Robustness norms are pluralistic. Treat any "required" battery as guidance and **confirm against the journal's current author guidelines**.

## Anti-patterns

- **OLS on time-to-event** data instead of survival models.
- **Survivor-only inference** read as antecedents of venture creation.
- **Ignoring founding self-selection** in observational venture data.
- **p-values with no effect size** or practical entrepreneurial meaning.

## Output format

```
【Estimator】survival / selection / panel-FE / DiD / experiment / qual ...
【Survivorship & selection】how handled ...
【Attrition / missing data】...
【Endogeneity】strategy + identifying assumption ...
【Robustness】alt specs, bounds, alternative explanation ...
【Effect sizes】magnitude for the phenomenon ...
【Open issues for reviewers】...
【Next step】jbv-contribution-framing
```
