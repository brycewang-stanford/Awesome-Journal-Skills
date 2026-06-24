---
name: jfi-identification-strategy
description: Use when auditing the core analytical engine of a Journal of Financial Intermediation (JFI) paper — for empirics, the causal design that separates credit supply from demand in banking data; for theory, the assumptions, equilibrium discipline, and proof exposition. It pressure-tests the design; it does not run the analysis.
---

# Identification Strategy (jfi-identification-strategy)

## When to trigger

- Setting up or defending the empirical design of a banking/intermediation paper
- Setting up or defending the assumptions and propositions of a theory paper

## Empirical track (applied banking / credit)

JFI referees are unforgiving on identification in bank data. Build a credible **causal design** and defend
it:

- **Source of variation:** a regulatory change, supervisory shock, branching deregulation, a discontinuity
  in capital/eligibility rules, or a plausibly exogenous credit-supply shifter.
- **Modern estimators:** staggered DID with heterogeneity-robust estimators (Callaway–Sant'Anna,
  Sun–Abraham, de Chaisemartin–D'Haultfœuille), IV with weak-IV-robust inference, or RDD with the
  rdrobust toolkit.
- **Bank-data-specific threats:** bank selection into treatment, borrower–firm sorting, balance-sheet
  timing and mechanical reverse causality, and the **lending-channel separation** of credit supply from
  demand (firm×time fixed effects in matched lender–borrower panels).
- **Inference:** cluster at the level of treatment assignment (often bank or market); wild-cluster
  bootstrap when clusters are few.

## Theory track (intermediation models)

When the contribution is a **model**, identification means **analytical discipline**:

- State **assumptions** transparently and motivate each economically (what friction it encodes).
- Make **results** precise as propositions/lemmas; keep **proof exposition** readable — sketch the
  mechanism in the text, full proofs in an appendix.
- Argue **generality**: which results survive relaxed assumptions, and where the boundary lies.
- A **numerical example** (see jfi-data-analysis) can illustrate the mechanism without claiming empirical
  estimation.

## The within-firm benchmark, and when it is not enough

The Khwaja–Mian within-firm estimator is this community's default answer to demand confounds: with
multi-bank firms, firm×time fixed effects difference out borrower demand and isolate the credit-supply
channel. A JFI referee then pushes **past** the default:

- Multi-bank firms are larger and less bank-dependent — show what the design's external margin
  (single-relationship firms) does, or bound how far the within-firm estimate travels.
- "Equal demand across a firm's lenders" is itself an assumption: a firm may cut demand for one bank's
  specialized product. Address with loan-purpose controls or product-level fixed effects.
- Firm-level **real outcomes** cannot carry firm×time FE; aggregate the bank shock to the firm with
  pre-period exposure shares, and defend share exogeneity as in shift-share designs.

## Design selection for common intermediation shocks

| Variation exploited | Default design | Venue-specific threat to pre-empt |
|---|---|---|
| Staggered regulation/deregulation across states or countries | Heterogeneity-robust staggered DID | Banks lobby for timing — show treatment is not predicted by pre-trend bank health |
| Capital- or size-threshold rule | RDD with density test | Banks bunch by managing the ratio; McCrary check is mandatory |
| Funding or deposit shock with differential exposure | Exposure (shift-share) design | Exposure shares correlate with local demand — balance on borrower observables |
| Run or crisis window | High-frequency event design | Mechanical balance-sheet timing; reverse causality from borrower distress |

## Worked contrast: one estimate, two readings (illustrative)

A 1pp funding shock reduces bank-level lending by 2.8pp (bank panel, OLS). At JFI that is not yet a
result: the same number is consistent with shocked banks happening to serve shocked borrowers. The
within-firm version at 1.6pp (firm×time FE) is the publishable object — and the 1.2pp gap becomes
evidence on borrower–bank sorting worth its own paragraph, not a nuisance to hide. JFI referees read the
movement of the coefficient across fixed-effect columns as a diagnostic in itself; design the
identification section so that movement is interpreted, not merely displayed.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the identification claim, don't only argue it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JFI is banking and financial intermediation — typically corporate / bank causal designs built around regulation and shocks.

1. `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result` to list
   the checks the design still owes.
2. **Staggered DiD:** `callaway_santanna` / `sun_abraham` + `bacon_decomposition` +
   `honest_did_from_result` (the pre-trend test is low-power, Roth 2022).
3. **IV:** `effective_f_test` + an `anderson_rubin_ci` (valid under weak instruments),
   not a 2SLS t-stat alone.
4. **RDD:** `rdrobust` (bias-corrected) + `rddensity` / `mccrary_test` for manipulation.
5. **OVB:** `oster_delta` / `sensemakr` — how strong a confounder would have to be.

Report the economic magnitude; route the full battery to the appendix; keep every
number reproducible. A run end-to-end (synthetic data, real returns) is in the
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md). If StatsPAI/Stata are not connected, adapt the
vendored `resources/code/` skeleton and flag any unverified number.
## Anti-patterns

- OLS-plus-controls dressed up as identification on a bank panel
- Conflating credit supply and demand without firm×time absorption
- A theory whose key result silently depends on an unstated assumption
- Clustering at the wrong level, or ignoring few-cluster inference

## Output format

```
【Track】empirical / theory
【Design or assumptions】<the variation, or the key assumptions>
【Top threat / boundary】<the main objection + answer>
【Inference / generality】<clustering, or which results survive>
【Next skill】jfi-data-analysis
```
