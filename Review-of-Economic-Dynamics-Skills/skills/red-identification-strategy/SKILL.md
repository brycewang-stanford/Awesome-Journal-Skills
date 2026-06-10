---
name: red-identification-strategy
description: Use when making the inferential backbone of a Review of Economic Dynamics (RED) manuscript credible, adapting to the paper type. For theoretical/computational papers it covers model assumptions, regularity conditions, and what disciplines the parameters; for empirical dynamic papers it covers causal design. RED's scope spans all three, so this skill branches accordingly.
---

# Identification & Model Logic for RED (red-identification-strategy)

## When to trigger

- Establishing why the paper's central claim is credible, before robustness
- Unsure whether RED expects a causal-design argument or a model-assumptions argument
- A computational paper where "identification" means parameter discipline, not instruments

## Branch by paper type (RED takes all three)

### Theoretical / computational dynamic models
The credibility question is about **assumptions, existence, and discipline**, not instruments:

- State the **model assumptions** and **regularity conditions** explicitly (preferences, technology,
  stationarity, boundedness, transversality); flag where existence/uniqueness of equilibrium is proved
  or assumed.
- Make **proof exposition** clean: state results as propositions, separate assumptions from claims,
  and put long proofs in an appendix while keeping the intuition in the body.
- Show **parameter discipline** — which parameters are calibrated to data targets, which are estimated,
  and which are free; justify each so results are not an artifact of free parameters.
- Discuss **generality**: what survives relaxing key assumptions, and where the result is knife-edge.

### Methodological / computational-method papers
- State the method's **regularity conditions** and where they bind; characterize **accuracy** and
  **convergence** of the numerical solution; report **asymptotics** where the method estimates parameters.
- Provide **Monte Carlo / numerical experiments** that show the method works under known data-generating processes.

### Empirical dynamic papers
- Make the **causal/identification design** explicit (the source of variation, the exclusion logic,
  the dynamic structure being estimated — e.g., VAR identification, local projections, structural estimation).
- Tie the empirical object back to **what it disciplines in the dynamic model**.

## Checklist

- [ ] The right branch is chosen for the paper type
- [ ] Assumptions/conditions (theory) or identifying variation (empirics) are explicit and defended
- [ ] Parameter discipline is documented; results are not driven by undisciplined free parameters
- [ ] Generality / accuracy / robustness of the core claim is characterized

## Anti-patterns

- Importing reduced-form "identification" language into a calibrated model where it does not apply
- Hiding free parameters or equilibrium-existence gaps
- Asserting generality without showing what relaxing the assumptions does

## Parameter-discipline table

For quantitative papers, create a table with one row per key parameter:

| Parameter | Value | Source/target | Free or disciplined? | Sensitivity shown? |
|---|---|---|---|---|

Any parameter that is free and influential needs a sensitivity check or a narrower claim.

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — solvers and estimation toolkits
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — scope sources
