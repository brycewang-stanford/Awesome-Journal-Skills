---
name: jcf-data-analysis
description: Use when building and running the empirical analysis for a Journal of Corporate Finance (JCF) paper — assembling WRDS-era firm panels (Compustat/CRSP/SDC/DealScan), constructing variables, estimating with fixed effects and clustered errors, and layering robustness. It guides the empirical build; pair it with jcf-identification-strategy for the design itself.
---

# Data Analysis (jcf-data-analysis)

## When to trigger

- Assembling the firm-level panel and constructing corporate-finance variables
- Choosing estimators, fixed effects, and clustering
- Planning the robustness battery a JCF referee will expect

## Data build (empirical corporate finance)

- Core sources: **Compustat** (fundamentals, leverage, payout), **CRSP** (returns/event windows), **CCM** (linked), **SDC/Refinitiv** (M&A, IPO/SEO, repurchases), **DealScan** (loans/covenants), **BoardEx/ISS/Execucomp** (governance, pay). Respect WRDS/vendor licenses — never redistribute raw vendor data.
- Document **sample construction** (filters, financials/utilities exclusions, fiscal-year alignment), **winsorizing** (e.g., 1/99), and every variable's formula.

## Estimation conventions

- **High-dimensional fixed effects** (`reghdfe` / `fixest`): firm, year, and often industry×year.
- **Cluster** standard errors at the firm level (and/or two-way firm-and-year) consistent with the variation.
- For staggered-adoption DID, use **modern estimators** (see jcf-identification-strategy), not plain TWFE.
- Report economic magnitudes, not just significance — JCF readers want the size of the effect on a corporate-finance outcome.

## Robustness the referee expects

- [ ] Alternative variable definitions and subsamples (size, period, industry)
- [ ] Alternative fixed-effects / clustering structures
- [ ] Endogeneity probes consistent with the design (placebo, falsification, alt. instrument)
- [ ] Sensitivity to outliers / winsorizing thresholds
- [ ] A short, honest discussion of remaining limitations

## Reproducibility (ties to data policy)

- One master script (`run_all`) regenerating every table/figure from the build.
- Pin software/package versions; set seeds for bootstrap/simulation.
- Prepare the **Elsevier Option C** data-availability statement and code/variable-construction archive now, not at acceptance (see jcf-replication-and-data-policy).

## Anti-patterns

- Kitchen-sink controls with no design and no magnitudes.
- Hidden sample-selection steps that change the result.
- Significance-only reporting with no economic interpretation.

## Output

```
【Panel】sources + filters + winsor: documented? [Y/N]
【Spec】FE = <…>; cluster = <…>; estimator = <…>
【Robustness】<list run / planned>
```
