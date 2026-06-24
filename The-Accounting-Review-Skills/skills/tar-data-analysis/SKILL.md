---
name: tar-data-analysis
description: Use when running and reporting the estimation for a The Accounting Review (TAR) manuscript — the estimator, fixed effects, standard-error clustering, robustness, and the data-authenticity / code-access documentation TAR requires. Executes and reports the analysis; it does not design identification (tar-methods) or frame the contribution (tar-contribution-framing).
---

# Estimation, Robustness & Data Authenticity (tar-data-analysis)

## When to trigger

- The sample is built and it is time to estimate and report
- You are unsure whether your standard errors, fixed effects, or estimator match the design
- Reviewers will probe robustness, alternative measures, or sample-selection screens
- You must assemble the data-authenticity / code-access package TAR requires
- A reviewer says "the result is not robust" or "I cannot tell how the sample was built"

## Estimator and inference (large-sample archival core)

- **Match the estimator to the design** set in `tar-methods`: OLS with high-dimensional fixed
  effects (firm, year, industry-year) for panel associations; DiD / staggered-DiD with a modern
  estimator for adoption shocks; 2SLS for endogenous regressors; RDD for threshold settings; logit/
  probit/Poisson/Tobit for limited or count outcomes (e.g., restatement, going-concern, fraud).
- **Cluster standard errors** at the level of treatment assignment / correlation (firm, or two-way
  firm-and-year); for few clusters use the wild-cluster bootstrap.
- **Report fixed effects explicitly** and show how the coefficient moves as you add them — a result
  that survives tighter fixed effects is more credible than one that does not.
- For **accounting-specific measures** (discretionary accruals, real earnings management, abnormal
  audit fees, effective/cash tax rates, disclosure tone), state the construction model and screen,
  and show the result is not an artifact of the proxy.

## Robustness reviewers expect

- Alternative measures of the focal accounting construct (e.g., a second accruals model; cash vs.
  GAAP ETR; alternative disclosure proxy).
- Alternative samples and screens (drop financials/utilities; winsorize vs. truncate; subperiods).
- Sensitivity of the identifying assumption (pre-trends, placebo dates, alternative instruments,
  bandwidth choices for RDD).
- Falsification / placebo tests where the effect should be absent.
- Economic magnitude, not just significance — interpret the coefficient in accounting terms.

## Data-authenticity & code access (a TAR-specific requirement)

TAR requires authors to enable confirmation of data authenticity, with differentiated rules:

- **Publicly available databases** (Compustat, CRSP, I/B/E/S, Audit Analytics): provide a precise
  description of the data **and** access to the **computer code** used to process it.
- **Data abstracted from public sources** (hand-collected from filings, PCAOB reports): provide the
  **abstraction methodology** plus code access.
- **Privately collected data** (proprietary field data, experiments): provide enough detail for
  reader confidence; **corroborating third parties** are acceptable.

Code/data sufficiency is part of the submission and acceptance requirements (待核实 whether a named
public repository deposit is mandated at acceptance). Build clean, commented scripts from raw
extract to every table now — not after the R&R.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). TAR is archival accounting — DiD around regulation / standard changes, IV, and earnings-based designs; the corporate-causal chain fits directly.

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

- [ ] Estimator matches the design; FEs reported; SEs clustered at the right level
- [ ] Coefficient stability shown across FE/control sets
- [ ] Focal accounting measure validated with an alternative construction
- [ ] Pre-trends/placebo/falsification tests reported where the design needs them
- [ ] Economic magnitude interpreted, not just p-values
- [ ] Data-authenticity package assembled per data type (description + processing code / methodology)
- [ ] Sample-construction screens documented and reproducible from raw data

## Anti-patterns

- **Uncluttered p-values, no magnitude** — significance without economic interpretation.
- **Single proxy** for a contested construct (e.g., one accruals model) presented as definitive.
- **TWFE on staggered adoption** ignoring heterogeneous-treatment-effect bias.
- **Robustness theater**: many tables that never vary the thing a skeptic doubts.
- **Unreproducible sample**: screens and merges that no one can rebuild from the raw data.
- **No processing code** ready, in violation of the data-authenticity policy.

## Output format

```
【Estimator】OLS-HDFE / staggered-DiD / 2SLS / RDD / logit-Poisson ...
【Fixed effects & clustering】... ; SE level ...
【Focal measure】construction + alternative proxy: pass/issues
【Robustness】alt measures / samples / placebo / pre-trends ...
【Economic magnitude】coefficient means ... in accounting terms
【Data authenticity】public-db / abstracted / private — code & description ready? yes/no
【Open issues for reviewers】...
【Next step】tar-contribution-framing
```
