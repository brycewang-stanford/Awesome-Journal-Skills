---
name: msom-methods
description: Use when matching the method and identification to the operations problem for a Manufacturing & Service Operations Management (M&SOM) manuscript — selecting the analytical model class and solution approach, or the empirical identification strategy. Designs the study; msom-data-analysis executes and reports it.
---

# Methods & Identification (msom-methods)

## When to trigger

- You must choose a solution approach for an analytical model, or an identification strategy for an empirical study
- A reviewer questions whether the method can actually deliver the claimed operational insight
- You are unsure whether to pursue closed-form structure, computation, or estimation
- The operations decision and the method have drifted apart

## Match the method to the operations decision

M&SOM accepts the method that the **operations problem** demands and routes it to the right department. The method must be able to deliver insight about an **operational decision** — that is the gate, in either lane.

### Analytical lane (dominant tradition)

| Operational structure / claim                          | Approach                                                        |
|--------------------------------------------------------|----------------------------------------------------------------|
| Single-period stocking/pricing under uncertainty        | Newsvendor / convex stochastic optimization                    |
| Sequential operational decisions over time              | Dynamic programming / MDP; approximate DP when intractable     |
| Congestion, staffing, delay in service systems          | Queueing; heavy-traffic / diffusion approximation              |
| Decisions under distributional ambiguity                | Robust / distributionally robust optimization                  |
| Strategic interaction (suppliers, platforms, customers) | Game theory / mechanism design; equilibrium analysis           |
| Multi-stage planning under uncertainty                  | Stochastic programming (SAA, SDDP), chance constraints         |

Pair structural results with a **numerical study** that quantifies magnitudes, tests assumptions' bite, and surfaces managerial guidance the proofs alone cannot.

### Empirical lane

Identify the operational effect credibly: natural experiments and **difference-in-differences**, regression discontinuity, instrumental variables, structural estimation of an operational model, or field experiments with operating partners. Address endogenous operational decisions (capacity, inventory, staffing are chosen, not random) and selection. Match clustering of standard errors to the operational unit (store, facility, server, route).

## Operations centrality is still the gate

A flawless econometric or optimization exercise that does not improve or explain an operational decision is off-fit. Keep the decision in view at every methodological choice.

## Execution bridge (StatsPAI / Stata MCP)

For the **empirical / causal lane**, estimate and audit rather than only specify. Full
map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). M&SOM mixes analytical and empirical OM; the chain below serves the empirical-OM lane, while analytical / queueing / optimization work is outside it.

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

- [ ] Method class justified by the operational decision, not by familiarity
- [ ] Analytical: solution approach stated; numerical study planned to complement proofs
- [ ] Empirical: identification strategy stated; endogenous operational choices addressed
- [ ] Robustness / sensitivity plan defined (parameters, instruments, specifications)
- [ ] SE clustering / instance design matches the operational structure

## Anti-patterns

- Forcing closed form on a problem that needs computation (or vice versa).
- Empirical design that ignores that capacity/inventory/staffing are endogenous.
- A method showcase with no operational decision improved.
- Proofs with no numerical study to quantify or stress assumptions.


## Methods pass for Manufacturing & Service Operations Management

Run this as a concrete capability pass. First lock the process bottleneck, decision policy, queue/inventory/service mechanism, and implementation constraint; then test whether the manuscript addresses operations reviewers who look for service/manufacturing process insight, implementable policies, and operational performance evidence.

- **Primary move:** Name the estimand or objective, assumptions, diagnostics, robustness checks, and failure modes before accepting the method as venue-ready.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against Management Science for broader OR/MS reach, Production and Operations Management for wider OM readership, Operations Research for method-first theory; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Worked micro-example (illustrative)

Vignette: a queueing-control model for an appointment-based outpatient clinic deciding how many same-day slots to reserve against no-show risk. The decision is the reserve count; the mechanism is idle capacity versus overflow. An MDP with a threshold reservation policy fits because the *form* of the rule is the insight. On illustrative calibrated no-show rates of 12–28%, the numerical study would show that reserving slots near the expected no-show count keeps overtime cost within an illustrative 4% of the full-information benchmark (numbers illustrative). The method is chosen because the decision demands a sequential threshold rule — not because dynamic programming is available.

## Referee-pushback patterns and the venue fix

- *"The model is tractable but its assumptions are detached from operations."* → Tie each binding assumption to an observable feature of the operating system and show in the numerical study what relaxing it costs.
- *"Empirical identification is weak."* → State the source of exogenous variation explicitly, defend exclusion/parallel-trends, and treat the operational decision as endogenous rather than a control.
- *"Why this method and not a simpler one?"* → Show the simpler method cannot recover the policy structure or the identified operational effect the contribution rests on.

## Output format

```
【Lane】analytical / empirical
【Method class】... (why it fits the operations decision)
【Identification / solution】strategy ...
【Numerical / robustness plan】...
【SE clustering / instance design】...
【Next step】msom-data-analysis
```
