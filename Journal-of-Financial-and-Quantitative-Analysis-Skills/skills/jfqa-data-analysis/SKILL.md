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

## Output format

```
【Sample】sources, filters, period, N firms/obs
【Estimator】FE / FMB / DID / IV + clustering justified
【Magnitudes】economic effect sizes reported
【Robustness】samples / definitions / placebos
【Next step】jfqa-tables-figures
```
