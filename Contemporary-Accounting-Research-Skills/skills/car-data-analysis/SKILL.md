---
name: car-data-analysis
description: Use when running and reporting the analysis for a Contemporary Accounting Research (CAR) manuscript — the right estimator for archival/capital-markets, experimental, or analytical-calibration work, robustness, and CAR's Data Integrity & Code Sharing Policy (code archiving, variable definitions, data availability statement). Executes and reports; it does not design the study (car-methods).
---

# Data Analysis & Reproducibility (car-data-analysis)

## When to trigger

- Data are collected and it is time to estimate and report
- You are unsure the estimator matches the design (panel, experiment, limited DV)
- Reviewers will probe identification, robustness, or measurement choices
- You must prepare the code, variable definitions, and data availability statement CAR requires

## Choose the estimator that matches the design

| Data / claim                                     | Estimator                                                          |
|--------------------------------------------------|--------------------------------------------------------------------|
| Firm-year panel, archival effect                 | OLS/panel with firm & year fixed effects; SE clustered by firm     |
| Causal archival claim                            | Difference-in-differences, IV/2SLS, RD, entropy balancing/matching |
| Randomized experiment                            | ANOVA/ANCOVA, planned contrasts; report cell means and effect sizes|
| Process/mechanism (experiment)                   | Mediation with bootstrap CIs; moderated mediation as theorized     |
| Binary/count/censored outcome                    | Logit/probit, Poisson/NB, Tobit as fits                            |
| Analytical predictions                           | Calibration/simulation or an archival test of the model's implications |

Cluster standard errors to match the data structure (firm and/or time); for experiments, respect the randomization unit. Justify winsorizing/truncating and document the cutoffs.

## Robustness CAR reviewers expect

- Alternative specifications (controls in/out, alternative measures, subsamples).
- Sensitivity of identification (alternative instruments, parallel-trends evidence, placebo tests, bounding).
- Address competing explanations empirically; report how outliers and missing data were handled (and why).

## Data Integrity & Code Sharing Policy (CAR-specific, plan from the start)

CAR's policy (effective May 1, 2020) governs all empirical submissions — archival, experimental, field, surveys, simulations:

- **At submission (in Editorial Manager):** (1) describe how the data were acquired/produced and their sources, and attach the full instrument for surveys/experiments; (2) for proprietary organizational data, agree to provide a credible verification means on editor request and disclose any NDA restrictions; (3) disclose which authors had data access and ran the analyses.
- **Before acceptance:** (4) a **data availability statement** with a repository link, with the data **cited in the reference list**; (5) assurance — consistent with NSF guidelines — that data and code are retained by at least one author for **at least six years**.
- **Final version:** archive the **code** that builds the final dataset in a public repository, documenting **variable definitions**, observation-omission criteria (e.g., outliers), and modifications (winsorizing, truncating). Proprietary code may be withheld only if you instead explain how others can reproduce the final dataset. Exception requests accompany the initial submission and are approved by the EIC only in exceptional circumstances.
- A **title-page data availability statement** is required whenever the paper uses data.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). CAR is archival/empirical accounting; the DiD / IV / RDD chain serves its causal designs around reporting and regulation.

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

- [ ] Estimator matches the design; SEs clustered to the structure / randomization respected
- [ ] Identification tests reported (parallel trends, placebos, alternative instruments) for causal archival claims
- [ ] Mediation via bootstrap CIs; effect sizes and cell means reported for experiments
- [ ] Winsorizing/truncating, outlier and missing-data handling documented with cutoffs
- [ ] Robustness and competing-explanation tests reported
- [ ] Code archived; variable definitions, omission rules, and modifications documented
- [ ] Data availability statement (with repository link, data cited) and 6-year retention assurance prepared

## Anti-patterns

- **Unclustered SEs** on panel data; ignoring the randomization unit in experiments.
- **Causal language** on an associational archival design with no identification tests.
- **Undocumented winsorizing/sample screens** that the code repository cannot reproduce.
- **Leaving code-sharing to the end** — it shapes how you build variables from day one.

## Output format

```
【Estimator】panel-FE / DiD-IV-RD / ANOVA-experiment / calibration; SE clustering ...
【Identification/robustness】tests reported ...
【Experiment】effect sizes, mediation (bootstrap CI) ...
【Screens】winsorizing/truncating, outliers, missing data — documented?
【Code & data policy】repo, variable defs, data availability statement, 6-yr retention ...
【Next step】car-contribution-framing
```
