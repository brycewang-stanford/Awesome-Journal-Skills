---
name: jfqa-data-analysis
description: Use when running and documenting the empirical analysis for a Journal of Financial and Quantitative Analysis (JFQA) paper — finance data construction (CRSP/Compustat/TAQ/IBES), winsorizing, fixed effects, clustered and Newey-West standard errors, robustness, and heterogeneity — so results survive double-anonymous JFQA review and reproduce from the archived code. For theory papers, lighten this and document numerical examples instead.
---

# JFQA Data Analysis (jfqa-data-analysis)

Use this skill to execute and document the estimation for a **JFQA** empirical finance paper so it is both credible and reproducible from the code you will archive (see jfqa-replication-and-data-policy).

## Data construction (finance-specific)

- Build from standard sources (CRSP, Compustat, CRSP/Compustat Merged, TAQ, IBES, TRACE, OptionMetrics) and document every filter (share codes, exchanges, financials/utilities exclusions, delisting returns).
- **Winsorize or trim** outliers and disclose the cutoffs; finance variables (ratios, returns) have heavy tails.
- Report the sample period, the number of firms and observations, and the unit of analysis.

## Estimation & inference

- Use fixed effects appropriate to the question; justify the **clustering** dimension (firm, time, or two-way) — finance referees will ask.
- For asset-pricing tests, use **Fama-MacBeth** with Newey-West or the appropriate correction; for panels, cluster-robust SEs.
- Report **economic magnitudes** (e.g., effect of a one-SD change, basis points, alpha per month), not just significance stars.

## Robustness & heterogeneity

- Alternative samples, alternative variable definitions, alternative fixed effects and clustering.
- Subsample/heterogeneity cuts motivated by the mechanism, not fishing.
- Placebo or falsification tests where the design allows.

## Reproducibility discipline

- One master script regenerating every table/figure from raw (or pseudo) data.
- Pin software/package versions; set and report seeds for any bootstrap/simulation.
- Keep the pipeline archive-ready as you go — JFQA may run **random external code verification**.

## Theory papers

If the paper is theoretical, lighten this skill: replace empirical estimation with **reproducible numerical examples / calibrations** that illustrate the propositions, and document the computation so a reader can rerun it.

## Standard-error decision grid (the first thing a JFQA referee checks)

| Setting | Inference JFQA referees expect | Also show |
|---|---|---|
| Firm panel, persistent outcome | two-way cluster (firm and year), or firm cluster with year FE | robustness to the other clustering choice |
| Fama-MacBeth on monthly returns | Newey-West with the lag count stated and justified | plain FMB SEs for comparison |
| Staggered policy adoption | cluster at the level of treatment assignment (e.g., state) | event-study leads/lags |
| Few clusters (roughly < 50) | wild cluster bootstrap p-values | the cluster count itself |
| Overlapping long-horizon returns | Newey-West/Hodrick lags matched to the horizon | non-overlapping subsample check |
| Generated regressors (betas, fitted values) | bootstrap or an errors-in-variables correction | the uncorrected SEs flagged as such |

An unjustified clustering choice is among the most common JFQA referee complaints; pre-empt it in the table notes, not just the text.

## Worked pass: a corporate-finance panel (numbers illustrative)

Hypothetical study of cash holdings and supplier concentration. Sample: Compustat 1990-2023, financials (SIC 6000-6999) and utilities (4900-4999) dropped, ratios winsorized at the 1st/99th percentiles. With firm and year fixed effects and two-way clustering, the standardized coefficient is 0.021 (t = 3.4): a one-SD rise in concentration moves cash/assets by 2.1 pp, about 12% of the 17.5 pp sample mean. The JFQA-grade write-up reports the 12%-of-mean line next to the t-stat, names the clustering in the note, and adds a falsification on firms with nationally diversified suppliers where the mechanism predicts nothing.

## Filter log the referee will try to reconstruct

- CRSP: share codes 10/11; the exchange universe stated; delisting returns merged and the treatment of missing delisting returns disclosed.
- Compustat: accounting data lagged so it was publicly available at the return date; duplicate gvkey-period rows resolved.
- Linking: CCM link table with valid link-date ranges — never name matching.
- Any price or size screens (e.g., penny-stock exclusions) disclosed and shown not to drive the result.
- Each filter's observation loss tracked so the sample-construction table sums from raw pulls to the final N.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JFQA is empirical finance (asset pricing + corporate) — the DiD / IV / RDD chain for corporate causal claims, the factor-zoo haircut for cross-sectional pricing.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER, accounts for
  cross-test correlation) or `benjamini_hochberg` — report the adjusted threshold.
- **OVB sensitivity:** `oster_delta` / `sensemakr` — the confounder strength that would
  overturn the headline.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists the missing checks and the
  exact `suggest_function` for each — no guessing the battery.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Keep the decisive checks in the body and the exhaustive (now actually-run) battery in
the appendix. See the executed chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Output format

```
【Sample】sources, filters, period, N firms/obs
【Estimator】FE / FMB / DID / IV + clustering justified
【Magnitudes】economic effect sizes reported
【Robustness】samples / definitions / placebos
【Next step】jfqa-tables-figures
```
