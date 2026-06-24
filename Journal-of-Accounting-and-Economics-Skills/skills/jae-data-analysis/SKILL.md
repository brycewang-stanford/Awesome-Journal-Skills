---
name: jae-data-analysis
description: Use when running and reporting the empirical analysis for a Journal of Accounting and Economics (JAE) manuscript — building the archival sample, choosing fixed effects and clustered standard errors, executing the identification design, and demonstrating robustness for large-sample capital-markets/contracting/disclosure data. Executes and reports the analysis; it does not design the study (jae-methods) or frame the contribution (jae-contribution-framing).
---

# Data Analysis & Inference for JAE (jae-data-analysis)

## When to trigger

- The sample is built and it is time to estimate and report
- You are unsure how to specify fixed effects or cluster standard errors
- Reviewers will probe endogeneity, correlated omitted variables, or sample selection
- A reviewer says "the standard errors are understated" or "this is not identified"

## Build and document the archival sample first

JAE reviewers expect a transparent **sample-construction waterfall**: starting population (e.g., Compustat firm-years), each merge (CRSP, I/B/E/S, Execucomp, DealScan, Audit Analytics via WRDS), each exclusion (financials/utilities, missing data, penny stocks), and the final N at every step. Report descriptive statistics and a correlation table. **Winsorize** continuous variables (commonly at 1%/99%) and say so.

## Specify the estimator to match the panel and the design

| Data structure / claim                       | Estimator / specification                                   |
|-----------------------------------------------|-------------------------------------------------------------|
| Firm panel with unobserved heterogeneity      | Firm and year fixed effects (e.g., `reghdfe`)               |
| Inference with within-firm correlation        | Standard errors clustered by firm; often **two-way** (firm & year) |
| Regulatory shock / treatment                  | Difference-in-differences; report pre-trends                |
| Endogenous regressor                          | 2SLS/IV with first-stage diagnostics (F-stat, exclusion)    |
| Self-selection                                | Heckman (report inverse Mills) or PSM (report balance)      |
| Information event                             | Short-window CARs; cross-sectional regression of returns    |
| Binary/limited outcome                        | Logit/probit/Tobit as the outcome dictates                  |

Match the **clustering** to where correlation lives in the data; a single firm-clustered SE may understate inference when shocks are common across firms in a year — two-way clustering is the JAE norm for many panels.

## Execute the identification, not just the regression

- **DiD**: plot/test parallel pre-trends; report the dynamic (event-time) coefficients, not only the average treatment effect.
- **IV**: report the first stage, the instrument's strength, and defend the exclusion restriction in words.
- **Matching/Heckman**: report covariate balance or the selection equation; show results are not an artifact of the procedure.
- **Cross-sectional partitions**: the theory's mechanism test — show the effect concentrates where the friction (information asymmetry, weak governance, tight covenants) is severe.

## Robustness (expected, not optional)

- Alternative proxies for the key construct (e.g., different discretionary-accruals or conservatism measures).
- Alternative specifications (controls in/out, alternative fixed effects, subsamples).
- Placebo/falsification tests and, for DiD, a non-event window.
- Sensitivity to correlated omitted variables (e.g., bounding / coefficient-stability arguments).
- Address economically plausible alternative explanations empirically.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JAE is empirical accounting with an economics lens; treat identification and weak-IV-robust inference as the binding constraints.

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

- [ ] Sample waterfall with N at each step; winsorization stated
- [ ] Descriptives and correlation table reported
- [ ] Fixed effects and **clustered (often two-way)** SEs match the design
- [ ] Identification executed (pre-trends / first stage / balance), not assumed
- [ ] Cross-sectional partition supports the economic mechanism
- [ ] Robustness: alternative proxies, specifications, placebos, sensitivity
- [ ] Economic magnitude (not only significance) reported

## Anti-patterns

- **Pooled OLS with no fixed effects or clustering** on a firm panel.
- **One-way clustering** when shocks are common across firms within a year.
- **Reporting an IV with no first stage** or no exclusion-restriction defense.
- **DiD with no pre-trend evidence.**
- **Significance with no economic magnitude** ("statistically significant" but trivially small).
- **Selective controls** that make the result appear.

## Output format

```
【Sample】population → merges → exclusions → final N; winsorized at ...
【Specification】FE (firm/year); SE clustering (firm / two-way)
【Identification executed】pre-trends / first-stage F / balance ...
【Main result】coefficient, t-stat, economic magnitude
【Mechanism (cross-section)】effect concentrated where friction severe
【Robustness】alt proxies / specs / placebo / sensitivity
【Open issues for reviewers】...
【Next step】jae-contribution-framing
```
