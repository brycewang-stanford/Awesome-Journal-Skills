---
name: jar-data-analysis
description: Use when running and reporting the empirical-archival analysis for a Journal of Accounting Research (JAR) manuscript — standard-error clustering, endogeneity execution, construct measurement, and the robustness battery referees expect, plus the reproducible data-and-code package JAR requires. Executes and reports; it does not choose the identification strategy (jar-methods) or frame the contribution (jar-contribution-framing).
---

# Data Analysis & Robustness (jar-data-analysis)

## When to trigger

- Data are built and it is time to estimate and report
- You are unsure how to cluster standard errors for your panel
- Referees will probe endogeneity, measurement, or the channel
- You must assemble the reproducible **data-and-code package** JAR posts

## Get the standard errors right (a JAR signature check)

Empirical-accounting referees scrutinize inference. Default to **clustering by firm**, and consider **two-way clustering by firm and year** (Petersen) when both cross-sectional and time-series dependence are present. With **few clusters**, use the **wild-cluster bootstrap** rather than asymptotic cluster-robust SEs. Match the clustering to the source of correlated shocks implied by your design, and report the choice explicitly.

## Execute the identification, don't just assert it

- **DiD**: report pre-trends and use heterogeneity-robust estimators for staggered timing (Callaway-Sant'Anna / Sun-Abraham), not naive two-way FE.
- **RD**: report the optimal bandwidth, robust bias-corrected estimates, a manipulation (density) test, and covariate balance at the cutoff.
- **IV/2SLS**: report the first stage and instrument strength (e.g., F-statistic), and defend the exclusion restriction in words.
- **Event studies**: report abnormal returns with a defensible benchmark model and window, and confront confounding events.

## Measure accounting constructs credibly

Use measures with precedent in prior JAR/JAE work (discretionary accruals, earnings persistence/smoothness, disclosure indices, comparability, audit-quality proxies, bid-ask spread / PIN for information asymmetry). Show the proxy behaves sensibly (validation, correlations with established measures) and test sensitivity to alternative proxies — proxy fragility is a common rejection reason.

## The robustness battery referees expect

- Alternative specifications: controls in/out, alternative fixed effects, alternative measures of the key construct.
- Subsamples and falsification/placebo tests (e.g., effect absent where theory says it should be).
- Sensitivity of identification assumptions (alternative instruments, donut RD, bounds).
- Cross-sectional partitions that confirm the **predicted channel** (the conditional predictions from jar-theory-development).
- Sample-construction and winsorization choices documented and varied.

## Reproducibility is a deliverable, not a courtesy

JAR's **data-and-code sharing policy requires and hosts** the materials. Keep top-to-bottom runnable scripts that regenerate every table and figure from raw extracts; document screens, vintages, and access dates; respect the terms of use (academic-research-only, acknowledgement of the JAR publication and code authors, authors retain copyright). On a **Registered Report**, the executed analysis must match the pre-approved Stage 1 protocol.

## Checklist

- [ ] SE clustering matches the design (firm / firm-and-year; wild bootstrap if few clusters)
- [ ] Identification executed with diagnostics (pre-trends / bandwidth / first-stage / balance)
- [ ] Modern DiD estimators used for staggered treatment timing
- [ ] Key construct validated; results robust to alternative proxies
- [ ] Robustness, falsification/placebo, and channel partitions reported
- [ ] Winsorization/sample screens documented and varied
- [ ] Reproducible data-and-code package assembled per JAR policy

## Anti-patterns

- **White/robust SEs on panel data** ignoring within-firm correlation.
- **Naive two-way-FE DiD** with staggered adoption.
- **One proxy, no validation** for a contested accounting construct.
- **Significance fishing** across windows, bandwidths, or specifications.
- **"Code available on request"** — JAR requires the package to be posted.

## Output format

```
【Estimator & SEs】model; clustering (firm / firm×year / wild bootstrap)
【Identification executed】diagnostics reported (pre-trends/bandwidth/first-stage)
【Construct measurement】proxy + validation + alt-proxy robustness
【Robustness/falsification】[...]
【Channel partitions】conditional predictions confirmed? [...]
【Reproducibility】data/code package status per JAR policy
【Open issues for referees】[...]
【Next step】jar-contribution-framing
```

## Resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official JAR/Chicago Booth/Wiley URLs (accessed 2026-06-01)
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — econometric packages (reghdfe / fixest / csdid / rdrobust / boottest) and data sources
