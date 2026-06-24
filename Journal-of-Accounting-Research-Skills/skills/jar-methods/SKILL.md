---
name: jar-methods
description: Use when the research design and identification strategy are the bottleneck for a Journal of Accounting Research (JAR) manuscript — choosing the setting, source of identifying variation, and sample to support a causal accounting claim. Designs the study; it does not run the estimation, clustering, or robustness (jar-data-analysis).
---

# Research Design & Identification (jar-methods)

## When to trigger

- The design is a panel regression with no source of identifying variation
- The claim is causal but the variation is observational/endogenous
- A referee says "this is correlation, not causation" or "the channel is unidentified"
- You must choose between an archival, experimental, analytical, or field design

## JAR's dominant design: empirical-archival capital markets

JAR's defining methodology is **large-sample empirical-archival capital-markets** research (financial-statement and market-data econometrics in the **Ball-Brown** lineage). The journal also publishes **experimental**, **analytical/modeling**, and **field-study** work, and the **Registered Reports** track is well suited to higher-outcome-risk designs that require new data collection. The bar across all of them is **credible identification**: a referee must believe the estimate reflects the economic effect you claim, not an omitted variable, reverse causality, or selection.

## Find identifying variation (the core archival problem)

| Theoretical claim | Identification that earns it |
|-------------------|------------------------------|
| Effect of a rule/standard | Staggered or sharp adoption as a natural experiment (modern DiD) |
| Effect at a threshold | Regression discontinuity (e.g., index inclusion, size cutoffs) |
| Effect of an endogenous firm choice | IV/2SLS with a defensible instrument, or a shock to the choice |
| Information content of a disclosure | Short-window event study around the release |
| Causal mechanism under control | Experiment (lab/online/field), often paired with archival evidence |

- **Anticipate the threats by name**: omitted correlated variables, reverse causality, selection into treatment, and measurement error. State which one is the binding concern and how the design neutralizes it.
- **Parallel trends / pre-trends** for DiD; **bandwidth and manipulation tests** for RD; **instrument relevance and exclusion** for IV — plan the diagnostics now, not in the rebuttal.
- **Construct measurement**: define accounting constructs (earnings quality, disclosure, audit quality, comparability) with measures used in prior JAR work, and plan validation.

## Sample and reproducibility from the start

Specify the sample frame, screens, and data vintages (Compustat/CRSP/I/B/E/S/Audit Analytics/EDGAR). Because JAR **requires** posted data and code, design the pipeline to be top-to-bottom reproducible from raw extracts, recording exclusion rules and access dates.

## Execution bridge (StatsPAI / Stata MCP)

For the **empirical / causal lane**, estimate and audit rather than only specify. Full
map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JAR is archival/empirical accounting; foreground identification around disclosure and regulation shocks, with modern DiD where adoption is staggered.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result` to
  enumerate the checks the design owes.
- **Panel / staggered DiD:** `callaway_santanna` / `sun_abraham` + `bacon_decomposition`
  + `honest_did_from_result`. **IV:** `effective_f_test` + `anderson_rubin_ci`. **RDD:**
  `rdrobust` + `mccrary_test`.
- **Experiments:** randomization-based inference and `romano_wolf` for the many-outcome
  family-wise correction reviewers expect.

Match the toolchain to the **reviewer pool**, and report the effect size the venue
wants. A run end-to-end (synthetic data, real returns) is in the
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] A specific source of identifying variation is named (shock/threshold/instrument/manipulation)
- [ ] The binding endogeneity threat is identified and the design addresses it
- [ ] Diagnostics planned (pre-trends / bandwidth / first-stage / manipulation checks)
- [ ] Accounting constructs measured with validated, prior-literature measures
- [ ] Sample frame, screens, and data vintages specified; pipeline reproducible
- [ ] If high-risk/new-data: Registered Reports (Stage 1 protocol) considered

## Anti-patterns

- **Kitchen-sink OLS** with controls standing in for identification.
- **Endogenous regressor** treated as exogenous with no strategy.
- **Weak/implausible instruments** failing relevance or exclusion.
- **Staggered DiD with two-way FE** ignoring heterogeneous-treatment-timing bias (use modern estimators).
- **Event windows fished** for significance; ad hoc bandwidths in RD.

## Output format

```
【Design】archival-NE / RD / IV / event-study / experiment / analytical / field
【Identifying variation】shock / threshold / instrument / manipulation
【Binding threat】OVB / reverse causality / selection / measurement — addressed by ...
【Diagnostics planned】pre-trends / bandwidth / first-stage / balance ...
【Constructs & measures】definitions + validation
【Sample & reproducibility】frame, screens, vintages; data/code pipeline
【Next step】jar-data-analysis
```

## Resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official JAR/Chicago Booth/Wiley URLs (accessed 2026-06-01)
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — archival data sources and identification tooling (reghdfe / csdid / rdrobust / ivreghdfe)
