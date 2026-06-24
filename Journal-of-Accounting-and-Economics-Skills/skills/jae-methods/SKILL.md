---
name: jae-methods
description: Use when designing the empirical (or analytical) approach for a Journal of Accounting and Economics (JAE) manuscript — choosing an identification strategy (natural experiments, DiD, IV, RD) for large-sample archival capital-markets/contracting/disclosure data, or structuring an economic model, so the design can credibly support the economic prediction.
---

# Research Design & Identification for JAE (jae-methods)

## When to trigger

- You have a prediction but no credible way to rule out endogeneity or reverse causality
- A reviewer will ask "is this causal or just correlation?"
- You must choose between an archival quasi-experiment and an analytical model
- Your treatment (a disclosure, a standard, a contract feature) is plausibly chosen, not random

## JAE's dominant methodology

JAE's workhorse is **large-sample empirical archival research grounded in economics** — observational capital-markets and contracting data analyzed with econometric, identification-focused designs — alongside **analytical economic modeling**. The journal favors economic analyses of accounting problems (capital-markets information content, contracting, disclosure, agency/monitoring) in the Watts-Zimmerman positive-accounting tradition. It does **not** publish normative prescriptions, behavioral lab experiments, or design-science artifacts; design accordingly.

## Design for identification

Because accounting choices and disclosures are endogenous, a bare panel regression rarely survives review. Match the design to the prediction:

| Setting / claim                                   | Identification strategy                                  |
|---------------------------------------------------|---------------------------------------------------------|
| A regulation/standard changes for some firms      | Difference-in-differences around the shock; staggered DiD |
| A continuous threshold (covenant, index, size cut)| Regression discontinuity                                |
| Endogenous regressor, valid instrument available  | IV / 2SLS; defend exclusion restriction explicitly      |
| Self-selection into disclosure/treatment          | Heckman selection; propensity-score matching            |
| Information event (earnings, 8-K, disclosure)      | Short-window event study (CARs), market-reaction design |
| Pure mechanism / equilibrium claim                | Analytical model with assumptions, propositions, proofs |

State the **identifying assumption** in words (parallel trends, exclusion restriction, continuity at the cutoff) and show how the design satisfies it. A natural experiment from a regulatory shock (SOX, Reg FD, IFRS/ASU adoption, an enforcement change) is the most persuasive JAE design when available.

## Sample and measurement design

- **Population and sample waterfall**: define the population, the merges (Compustat-CRSP-I/B/E/S-Execucomp-DealScan-Audit Analytics via WRDS), and every exclusion, with counts.
- **Construct measurement**: justify proxies (discretionary accruals, accrual quality, conditional conservatism, bid-ask spread for information asymmetry) and pre-register the expected sign.
- **Control set**: include the economic determinants the theory implies; avoid "bad controls" that absorb the mechanism.

## Analytical-model design

If the contribution is the model: state primitives and the information structure, solve for equilibrium, present comparative statics as testable propositions, and put proofs in an appendix. Keep assumptions economically interpretable.

## Execution bridge (StatsPAI / Stata MCP)

For the **empirical / causal lane**, estimate and audit rather than only specify. Full
map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JAE is empirical accounting with an economics lens; treat identification and weak-IV-robust inference as the binding constraints.

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

- [ ] Identification strategy named and matched to the prediction
- [ ] Identifying assumption stated in words and defended
- [ ] A shock / instrument / discontinuity is exploited where feasible
- [ ] Sample-construction waterfall with counts is specified
- [ ] Proxies justified; control set avoids bad controls
- [ ] Analytical models state assumptions, equilibrium, and comparative statics

## Anti-patterns

- **"Kitchen-sink" panel OLS** presented as if causal.
- **Instruments with no credible exclusion restriction.**
- **Ignoring self-selection** into disclosure/treatment.
- **Bad controls** that mechanically absorb the effect of interest.
- **A normative or lab-experiment design** that JAE does not publish.

## Output format

```
【Design】DiD / RD / IV / matching / event study / analytical model
【Identifying assumption】parallel trends / exclusion / continuity ...
【Shock or instrument】...
【Sample waterfall】population → merges → exclusions → final N
【Key proxies & expected signs】...
【Threats to identification】... and how addressed
【Next step】jae-data-analysis
```
