---
name: jleo-identification
description: Use when the identification argument is the bottleneck for an empirical Journal of Law, Economics, and Organization (JLEO) manuscript — institutional/organizational causal designs (reforms, institutional variation, court/committee/case assignment, governance-form choice). Stress-tests the design to JLEO's institutional bar; it does not build the theory model (jleo-theory-model).
---

# Identification Strategy (jleo-identification)

## When to trigger

- The causal claim rests on OLS + controls, or TWFE on staggered institutional reforms
- The unit chooses its own governance form (make-or-buy, integration, contract type) and the estimate confounds selection with effect
- The "treatment" is a court/committee/judge/case assignment whose as-good-as-random status is asserted but not shown
- A referee asks "what is the source of variation that identifies this institutional effect?"
- The design borrows institutional variation across countries/states/firms without ruling out the obvious confounds

## The JLEO identification bar

JLEO empirics live or die on whether the **institutional or organizational variation** that does the identifying is credible — because the object of interest is usually itself chosen by the agents (firms pick governance forms; legislatures pick rules; litigants select into courts). The credible-identification standards are the same as any top empirical economics journal, but the *threats* are institution-specific: endogenous boundaries, endogenous reform timing, selection into contract form, and strategic case selection. Name the variation, defend it, and never let the institutional story substitute for the design.

## Design branches and their institution-specific threats

### Reforms / institutional change (DID, event study)
- With staggered adoption move beyond TWFE: Callaway–Sant'Anna, Sun–Abraham, de Chaisemartin–D'Haultfœuille; show clean event-study leads; report a Goodman–Bacon decomposition.
- The first-order JLEO threat is **endogenous reform timing**: institutions reform when conditions change. Defend timing exogeneity (or instrument it), and test for anticipation.

### Governance-form / make-or-buy choice (the classic TCE empirics)
- The boundary of the firm is *chosen*. A raw comparison of integrated vs. arm's-length transactions confounds the governance effect with the selection that produced it.
- Use within-transaction variation, an IV for the governance choice, a selection model with a defensible exclusion, or matching on asset-specificity/uncertainty proxies — and say which, and why it breaks the selection.

### Court / committee / judge / case assignment
- The cleanest JLEO-style natural experiment: random or rotation-based assignment of cases to judges/panels, or bills to committees.
- Show the assignment mechanism is actually as-good-as-random (balance on case characteristics); address case settlement/selection that re-introduces endogeneity downstream.

### Cross-institutional variation (states, countries, firms)
- Defend the variation against the obvious omitted institutional confounds; prefer within-jurisdiction-over-time variation or a sharp discontinuity to a cross-section of institutions.

### IV / RDD where applicable
- IV: strong first stage; weak-IV-robust inference (Anderson–Rubin) if weak; defend exclusion in the institutional context. RDD: density test (McCrary / Cattaneo–Jansson–Ma), bandwidth robustness, covariate smoothness, bias-corrected CIs.
- Cluster inference at the level of the institutional treatment; address few-cluster problems (wild-cluster bootstrap).

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JLEO is law-and-economics/organizations; institutional designs with endogeneity — foreground identification.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference + `romano_wolf` for many-outcome control.
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the magnitude in interpretable units; route the full battery to the appendix. A
run end-to-end (synthetic data, real returns) is in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] The identifying variation is named in one sentence and tied to the institutional setting
- [ ] Selection into the governance form / institution is explicitly addressed, not assumed away
- [ ] Reform timing exogeneity or assignment-as-random is defended and tested (anticipation, balance)
- [ ] Staggered designs use a modern estimator; event-study leads shown flat
- [ ] Inference clustered at the institutional treatment level; few-cluster issues handled
- [ ] The causal claim never exceeds what the institutional variation supports

## Anti-patterns

- Comparing integrated vs. non-integrated transactions as if governance form were randomly assigned
- TWFE on staggered institutional reforms with no heterogeneity-bias discussion
- Asserting judge/case/committee assignment is random without showing balance
- Cross-country institutional regressions with controls standing in for identification
- An "institutional story" doing the work the research design should do

## Worked vignette (illustrative)

A paper estimates the effect of vertical integration on hold-up costs using firm transaction data. The naive comparison is biased: firms integrate precisely the transactions most prone to hold-up. A JLEO-credible move uses a shock to asset specificity (e.g., a technology change raising relationship-specific investment for a subset of input categories) as the source of variation, with an event study around the shock and a placebo on unaffected categories. Suppose integrated-transaction disputes fall 18% (s.e. 6, illustrative) post-shock for treated categories only — that pattern, not the cross-section, identifies the governance effect.

## Output format

```text
【Design】reform-DID / governance-choice / case-assignment / cross-institution / IV / RDD
【Identifying variation】one sentence, tied to the institution
【Selection/endogeneity threat + fix】[...]
【Diagnostics】event-study leads / balance / first-stage / density / placebo
【Inference】clustering level; few-cluster handling
【What it does NOT identify】[...]
【Next skill】jleo-theory-model
```
