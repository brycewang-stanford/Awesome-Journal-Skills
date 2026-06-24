---
name: jibs-data-analysis
description: Use when running and reporting the empirical analysis for a Journal of International Business Studies (JIBS) manuscript — cross-national measurement equivalence, common-method-variance checks, the right multilevel/dynamic-panel estimator, endogeneity and dynamic-endogeneity identification, and robustness aligned to the JIBS methods-editorial canon. Executes and reports; it does not design the study (jibs-methods) or frame the contribution (jibs-contribution-framing).
---

# Data Analysis & Cross-National Validity (jibs-data-analysis)

## When to trigger

- Cross-country or multilevel data are collected and it is time to estimate and report
- You are unsure your estimator matches nesting (individuals in firms in countries) or a process design
- Reviewers will probe measurement equivalence, CMV, or (dynamic) endogeneity
- A reviewer cites a JIBS "From the Editors" methods editorial against your analysis

## Establish cross-national measurement equivalence first

At JIBS, because constructs travel across countries and cultures, **measurement equivalence is a first-order review concern**, not an afterthought. Before testing hypotheses:

- **Reliability & CFA.** Report reliability (alpha/composite reliability) and a confirmatory factor analysis with fit (CFI, TLI, RMSEA, SRMR).
- **Measurement invariance.** Run multi-group CFA and report **configural → metric → scalar** invariance across countries; if scalar fails, report partial invariance or the alignment method and discuss what cross-country comparisons remain defensible.
- **Construct & discriminant validity.** AVE per construct; AVE > inter-construct squared correlations (or HTMT). Report the correlation matrix with reliabilities on the diagonal.
- **Aggregation (multilevel).** Justify any aggregation to the country/firm level with ICC(1), ICC(2), and r_wg(j).
- **Qualitative designs.** Where the design is case-based, "validity" becomes trustworthiness — a transparent data structure, an audit trail, and representative cross-case quotations.

## Match the estimator to the cross-country/multilevel design

| Data structure / claim                              | Estimator                                                    |
|-----------------------------------------------------|--------------------------------------------------------------|
| Individuals/firms nested in countries               | Multilevel / HLM (random intercepts/slopes); country-level Xs |
| Latent constructs across groups, mediation          | Multi-group / multilevel SEM                                 |
| Internationalization as a path-dependent process    | Dynamic panel (system/diff GMM), firm FE, lagged DVs         |
| Cross-border entry-mode / location choice           | Logit/probit/multinomial; conditional/mixed logit            |
| Cross-country count/limited DV                       | Poisson/negative binomial; Tobit/Heckman as fits            |

Cluster standard errors to the country (or country-year) structure.

## Common-method variance (CMV) — an active JIBS gatekeeper

JIBS routinely asks survey/same-respondent papers that appear to suffer from CMV to run validity checks and resubmit. A Harman single-factor test alone is **not** sufficient. Report the *designed* separations first (from jibs-methods), then statistical evidence: a marker-variable approach, an unmeasured latent method factor (CFA), or showing interaction/cross-level effects survive (these are hard to inflate by CMV). Cite the JIBS "From the Editors" CMV editorial.

## Endogeneity and "dynamic endogeneity"

For internationalization-as-process designs, address **dynamic endogeneity** explicitly: past strategy, performance, and unobserved firm heterogeneity co-evolve. Execute the identification planned at design (instruments and first-stage strength, dynamic-panel GMM with instrument-count and Hansen/AR(2) diagnostics, DiD/natural experiment, or selection models) and discuss the assumptions. Reviewers anchor this to the JIBS endogeneity/dynamic-endogeneity editorials.

## Reporting & robustness

- **Mediation:** bias-corrected bootstrap CIs (e.g., 5,000 resamples); conditional indirect effects for moderated mediation.
- **Moderation/cross-level interactions:** report the coefficient *and* plot simple slopes; report incremental variance.
- **Effect sizes:** report magnitudes, not only p-values (a JIBS p-value editorial cautions against p-value worship).
- **Robustness:** alternative country samples (drop influential countries), alternative distance measures, alternative specifications; sensitivity to endogeneity assumptions.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JIBS is international business — cross-country panels with confounded institutions; emphasize fixed effects, clustering, and endogeneity of location / entry choices.

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
## Output format

```
【Measurement】reliability/CFA fit; invariance configural/metric/scalar (or partial/alignment) ...
【Estimator】multilevel / multilevel-SEM / dynamic-panel GMM / choice model; SE clustered by country ...
【CMV evidence】designed separation + marker/latent-method test (beyond Harman) ...
【Endogeneity / dynamic endogeneity】strategy executed; diagnostics; assumptions ...
【Mediation/Moderation】bootstrap CIs / simple slopes / incremental variance ...
【Robustness】country-drop, alt distance, alt specs ...
【FTE editorial alignment】 ...
【Next step】jibs-contribution-framing
```

## Anti-patterns

- Pooling countries without testing measurement invariance.
- Single-factor (Harman) test as the sole CMV defense.
- OLS on country-nested data, ignoring non-independence.
- Internationalization-process regressions with no dynamic-endogeneity treatment.
- Reporting p-values with no effect sizes or practical magnitude.
- Treating cultural/institutional distance as a black-box covariate.
