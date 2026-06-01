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

## Output format

```
【Lane】analytical / empirical
【Method class】... (why it fits the operations decision)
【Identification / solution】strategy ...
【Numerical / robustness plan】...
【SE clustering / instance design】...
【Next step】msom-data-analysis
```
