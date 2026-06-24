---
name: smj-methods
description: Use when designing the research method for a Strategic Management Journal (SMJ) manuscript — sample, unit of analysis, measures, and the identification strategy. Designs the study; estimation and endogeneity execution live in smj-data-analysis.
---

# Research Design & Methods (smj-methods)

## When to trigger

- Sample, time window, and unit of analysis are not yet pinned down
- Measures (especially of performance and of the strategic choice) are not validated
- You have not yet chosen an identification design for a causal claim
- You are deciding between quantitative panel work, a natural experiment, qualitative theory-building, or formal modeling

## Design families SMJ publishes

| Family                         | Best for                                                     |
|--------------------------------|--------------------------------------------------------------|
| Panel econometrics (firm/BU)   | Performance consequences of strategic choices over time      |
| Natural experiment / DID       | An exogenous shock to strategy or environment                |
| IV / two-stage                 | An endogenous strategic choice with a credible instrument    |
| Matching + DID                 | Selection on observables into a strategic action             |
| Selection (Heckman)            | Outcome observed only after a self-selected strategic step   |
| Qualitative / inductive        | Building new strategy theory where constructs are immature   |
| Formal / analytical modeling   | Deriving and testing equilibrium strategic behavior          |

The hallmark SMJ empirical paper uses **panel data with fixed effects** and then deploys one or more identification tools to address endogeneity. Choose the design *from the threat*, not from convenience.

> SMJ's empirical standard is codified in its own editorial — Bettis, Gambardella, Helfat & Mitchell (2014), "Quantitative empirical analysis in strategic management," *SMJ* 35(7): 949–953 — which asks authors to acknowledge endogeneity and make a good-faith effort to address it, and disapproves of **data snooping and p-hacking**. SMJ also accepts that perfect causal inference is sometimes impossible; correlations that rule out alternative mechanisms can still be valuable if framed honestly.

## Sample & unit of analysis

- State the population, sampling frame, time window, and the exact unit (firm-year, BU-year, alliance, deal). Mismatched units (theory at the firm level, data at the deal level) draw fire.
- Justify the panel length: enough pre-periods to test parallel trends if using DID; enough within-firm variation if using FE.
- Report and justify all sample-construction filters (survivorship, missing data, industry exclusions). SMJ reviewers probe sample-selection artifacts.

## Measurement (the quiet rejection reason)

- **Performance DV:** pick the construct deliberately — accounting (ROA), market (Tobin's q, abnormal returns), or operational. Justify why it matches the theory; report sensitivity to alternatives.
- **Strategic-choice IV:** validate that the measure captures the construct (e.g., diversification, alliance scope) and not something correlated. Cite the source of any established measure.
- **Controls:** include theoretically motivated controls (firm size, age, slack, industry, prior performance) but avoid "bad controls" — outcomes of the treatment that absorb the effect.
- Pre-register, or at minimum pre-specify, the primary specification to avoid the appearance of specification search (SMJ disapproves of data snooping / p-hacking).

## Identification design (decide before estimating)

State the **identifying threat** explicitly, then the design that defeats it:

- **Selection into the strategic choice** (firms that ally/acquire/diversify differ): matching, IV, selection model, or a shock that assigns the choice.
- **Reverse causality** (performance drives the choice): lagged structure plus a design that breaks simultaneity (shock/IV); lags alone are not enough.
- **Unobserved heterogeneity** (a firm trait drives both): firm fixed effects, plus discussion of time-varying confounds FE cannot absorb.
- **Omitted environmental confounds:** industry-year fixed effects, region controls.

Name the design here; `smj-data-analysis` executes and stress-tests it.

## Execution bridge (StatsPAI / Stata MCP)

For the **empirical / causal lane**, estimate and audit rather than only specify. Full
map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). SMJ is strategy — firm-level panels where strategic choices are endogenous; foreground IV / DiD identification and the endogeneity-of-strategy objection.

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

- [ ] Population, frame, time window, and unit of analysis are explicit and matched to theory
- [ ] Every sample filter is reported and justified (survivorship / missingness addressed)
- [ ] Performance DV is justified; alternative operationalizations identified for robustness
- [ ] Strategic-choice measure is validated and sourced
- [ ] Controls are theory-driven; no post-treatment / "bad" controls
- [ ] The identifying threat is named and a design is chosen to address it
- [ ] For DID: pre-periods support a parallel-trends test; for IV: a candidate instrument with a relevance + exclusion story

## Anti-patterns

- Choosing OLS-with-controls and hoping reviewers ignore endogeneity (they will not)
- Unit-of-analysis mismatch between theory and data
- Undisclosed sample filters that could drive the result
- A performance measure chosen because it "works," not because it fits the theory
- Controlling for a variable that is itself an outcome of the treatment
- Picking the design before identifying the threat it is supposed to solve

## Output format

```
【Design family】panel FE | DID/natural experiment | IV | matching+DID | Heckman | qualitative | formal
【Sample】population / frame / window / unit
【Filters】[list + justification]
【DV (performance)】construct + measure + alternatives
【Focal X (strategic choice)】measure + source + validity note
【Identifying threat】selection | reverse causality | unobserved heterogeneity | omitted confound
【Chosen identification design】...
【Next step】smj-data-analysis
```

## Templates & resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — strategy data sources and Stata/R/Python packages for FE, IV, DiD, matching, RDD
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — SMJ endogeneity policy and the Bettis et al. (2014) methods editorial
