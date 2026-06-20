---
name: jeem-theory-model
description: Use when a Journal of Environmental Economics and Management (JEEM) manuscript needs a resource/pollution-control or dynamic-resource model that earns its place — generating a testable comparative static or a policy-relevant welfare expression, not decorating an empirical result. Sharpens the model; it does not invent evidence or citations.
---

# Theory and Model Craft (jeem-theory-model)

## When to trigger

- A pollution/abatement or resource-extraction model is in the paper but a referee asks "what does the model buy us?"
- The empirical work needs a conceptual frame that maps estimates to a **welfare or optimal-policy** statement
- A dynamic-resource problem (fishery, forest, groundwater, exhaustible stock) needs its Euler/Hotelling logic made explicit
- The model's comparative statics are stated but never confronted with data or used to derive the efficient instrument

## What a model must earn at JEEM

JEEM is empirical-leaning, so a model is rarely the whole paper; it must **do work**. A model earns its place if it (a) produces a sign or magnitude prediction the empirics then test, (b) delivers the **welfare or optimal-instrument** expression that turns reduced-form estimates into a policy number, or (c) reveals a mechanism — leakage, avoidance, dynamic adjustment — that changes the interpretation. A model that only restates intuition or that cannot be confronted with the data should be cut to an appendix or removed.

## When the paper needs no formal model

Not every JEEM paper needs a model section, and forcing one weakens the paper. A cleanly identified reduced-form estimate — a regulation's effect on emissions, a capitalization of an amenity — can stand on a compact conceptual framework that states the externality, the welfare object, and the assumptions linking the estimate to welfare, without a full optimization. The test is whether a formal model would *add* a tested prediction, a welfare expression, or a mechanism insight. If it would only restate the framework in equations, a clear conceptual paragraph plus the welfare-mapping assumptions (handed to `jeem-identification`) serves better. Reserve formal modeling for where it earns its keep.

## The canonical JEEM modeling toolkit

| Problem | Core structure | What it must deliver |
|---------|----------------|----------------------|
| Pollution / abatement | marginal damage = marginal abatement cost; Pigouvian tax vs. permits | the efficient tax/cap; the price-vs-quantity (Weitzman) ranking under uncertainty |
| Exhaustible resource | Hotelling: shadow price grows at the discount rate | optimal extraction path; effect of a tax/backstop on the path |
| Renewable resource | bioeconomic (Gordon–Schaefer); open-access vs. optimal stock | rent dissipation; the efficient harvest/quota |
| Spatial-dynamic resource | stock externality across space/time (groundwater, fisheries) | the wedge between private and social use; instrument design |
| Regulation under uncertainty | asymmetric information, monitoring/enforcement | second-best instrument; the value of information/monitoring |

## How to make the model load-bearing

1. **State the externality or stock dynamics first** — the environmental structure (marginal damage function, growth function, decay) is what distinguishes a JEEM model from a generic optimization.
2. **Derive one comparative static you will test** — e.g., "a stricter cap raises the permit price proportionally to the abatement-cost slope," then estimate that slope.
3. **Get to the welfare/instrument expression** — JEEM wants the efficient tax, the optimal quota, or the welfare loss, written in terms of objects the data identify.
4. **Be explicit about second-best** — real environmental policy is second-best (pre-existing distortions, incomplete coverage, monitoring costs); a first-best result that ignores leakage or enforcement will draw fire.
5. **Match the model's parameters to the empirical estimands** so the calibration/estimation in `jeem-identification` and `jeem-robustness` actually feeds it.

## Price-vs-quantity and the role of uncertainty

A distinctively environmental theory contribution lives in the Weitzman prices-vs-quantities tradition: when marginal damages and marginal abatement costs are uncertain, the choice between a tax and a cap turns on the relative slopes. If a paper proposes a regulatory instrument, the model should say *why that instrument* — steep marginal damages favor quantity instruments (caps), flat marginal damages favor price instruments (taxes). Stating this comparison, and tying the slopes to objects the empirics estimate, is the kind of theory move JEEM rewards over a generic optimization restatement.

## Calibration discipline

When the model is calibrated rather than estimated, JEEM referees expect the calibration to be disciplined and transparent: parameters tied to the paper's own data or to clearly cited field estimates (not borrowed wholesale from an unrelated macro paper), sensitivity of the headline welfare number to the key parameters reported, and the social cost of carbon or discount rate — when they drive results — varied across the range used in the literature rather than fixed at one convenient value. A counterfactual welfare number that hinges on an undefended discount rate or an off-the-shelf damage elasticity will draw fire.

## Connecting the model to the policy instrument

The payoff of a JEEM model is usually an instrument: the efficient Pigouvian tax, the optimal cap, the right quota, the second-best subsidy. State that instrument as the model's headline output, written in terms the empirics can fill in, so the reader sees the path from estimate to policy. A model that derives an efficient tax equal to the marginal external cost, then has the empirical section identify that marginal cost, closes the loop — the paper delivers a number a regulator could legislate. A model that stops at "welfare is higher under regulation" without naming the instrument leaves the contribution abstract.

## Checklist

- [ ] The environmental structure (damage function / stock dynamics / externality) is explicit, not generic optimization
- [ ] The model yields at least one comparative static the empirics test, or the welfare/instrument expression the empirics fill in
- [ ] Dynamic problems state the Euler/Hotelling/bioeconomic condition and the steady state
- [ ] Welfare is written in terms of estimable objects (marginal damage, abatement-cost slope, stock value)
- [ ] Second-best realities (leakage, partial coverage, monitoring/enforcement) acknowledged where relevant
- [ ] Anything the model cannot confront with data is in the appendix, not padding the main text

## Anti-patterns

- A model whose only output is "intuition we already had" — decoration, not contribution
- First-best Pigouvian results in a setting that is plainly second-best (pre-existing taxes, leakage)
- A dynamic-resource model with no steady state, transition, or testable path implication
- Comparative statics derived but never tested, while the empirics ignore the model
- Calibrating to off-the-shelf parameters with no link to the paper's own identification
- Importing a macro/IO model wholesale with the environmental externality bolted on

## Worked vignette (illustrative)

A groundwater paper documents over-extraction and proposes a pump tax. Without a model, the tax level is arbitrary. The JEEM move: write the spatial-dynamic stock externality, derive that the efficient tax equals the present value of the marginal user cost (the stock's shadow price), and show this maps to an estimable hydrological-economic gradient. The empirical section then identifies that gradient, and the model converts it into a defensible tax schedule — the model is now load-bearing.

## Where the model lives in the paper

Decide the model's footprint honestly. If it generates the central testable prediction or the welfare expression, it belongs in the main text, stated compactly with the key result highlighted. If it is scaffolding that justifies a specification but is not itself the contribution, compress it to a proposition or two and move derivations to an appendix. JEEM referees reward a model that is exactly as large as it needs to be: a five-page derivation that ends in a result the empirics never use will be asked to shrink, while a one-line "assume a Pigouvian setting" that hides a load-bearing assumption will be asked to expand. Match the model's prominence to the work it does.

## Output format

```text
【Journal】Journal of Environmental Economics and Management
【Skill】jeem-theory-model
【Verdict】pass / trim-to-appendix / cut
【Environmental structure】damage function / stock dynamics / externality form
【What the model buys】tested comparative static OR welfare/instrument expression
【Estimable link】which model parameter the empirics identify
【Second-best caveats】leakage / coverage / enforcement noted? [Y/N]
【Source status】verified URL / 待核实 / not asserted
【Next skill】jeem-robustness
```
