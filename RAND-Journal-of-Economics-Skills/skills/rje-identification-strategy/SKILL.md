---
name: rje-identification-strategy
description: Use when the identification or estimation strategy is the bottleneck for a RAND Journal of Economics (RJE) industrial-organization manuscript — structural demand/supply, entry and dynamic games, auctions, or reduced-form designs off mergers and regulation. Stress-tests the design to the IO-flagship bar before tables are drafted.
---

# Identification Strategy (rje-identification-strategy)

## When to trigger

- Your structural model's identification (instruments, functional form, moments) is unargued
- A merger/regulation evaluation rests on TWFE over staggered timing with no modern estimator
- An IV's first stage or exclusion restriction is weak in an IO setting
- You are unsure your design clears the RJE industrial-organization bar

## The RJE identification bar

RJE is the **flagship industrial-organization journal**, so identification is judged by IO norms: the **economic model and the source of identifying variation must be explicit**, and counterfactuals must be disciplined by the model and the data. Both **structural** and **reduced-form** work is welcomed — there is no preference for one, but each carries field-specific obligations.

## Branch A: Structural demand (BLP-style)

- **Price endogeneity** is the central threat. Instrument price with cost shifters, rival/own product characteristics (BLP instruments), or Gandhi–Houde differentiation instruments; argue their validity in market terms.
- Add **micro-moments** (consumer-level data) where available to pin down substitution and heterogeneity.
- State functional-form assumptions (random-coefficients distribution) and show key elasticities are reasonable, not artifacts.

## Branch B: Supply, conduct & markups

- Be explicit about the **conduct assumption** (Nash-Bertrand, Cournot, collusion) and, where possible, **test conduct** rather than assume it.
- Identify marginal cost from the supply-side FOCs; show pass-through and markups are economically sensible.

## Branch C: Entry / dynamic games

- For static entry, address **multiplicity of equilibria** (bounds, equilibrium selection).
- For dynamic models, justify the **CCP / two-step (Hotz–Miller)** approach or full-solution estimation, and state the state space and discount factor handling.

## Branch D: Auctions

- Map the **observed bids to the value distribution** through the equilibrium first-order conditions; state the information paradigm (private vs common values).

## Branch E: Reduced-form (mergers / regulation)

- Name the **policy or merger shock** giving exogenous variation; defend it institutionally.
- Staggered timing? Move beyond **TWFE** — use Callaway–Sant'Anna, Sun–Abraham, or de Chaisemartin–D'Haultfœuille, with an event-study plot and a Goodman-Bacon check.
- For IV: strong first stage, weak-IV-robust inference, and an exclusion restriction argued from market institutions.

## Checklist

- [ ] Economic model / identifying variation stated in one sentence
- [ ] Price endogeneity (structural) or treatment exogeneity (reduced-form) defended
- [ ] Instruments named and their validity argued in market terms
- [ ] Conduct / equilibrium-selection assumptions made explicit
- [ ] Modern estimator used where TWFE would be biased
- [ ] Counterfactual assumptions bounded and stated
- [ ] Claims never exceed what the model + data support

## Anti-patterns

- A demand system with price treated as exogenous, or weak/unargued price instruments
- Assuming Nash-Bertrand conduct when the data could test it
- TWFE on staggered merger/regulation timing with no heterogeneity-robust estimator
- Selling an in-sample fit as a credible far-out-of-sample counterfactual

## Output format

```
【Approach】structural demand / conduct / entry-dynamics / auctions / reduced-form
【Identifying variation】one sentence
【Key assumptions】[instruments, conduct, equilibrium selection, exclusion]
【Diagnostics done】[elasticities, first-stage F, pre-trends, conduct test]
【Diagnostics missing】[...]
【Next step】rje-data-analysis
```
