---
name: wber-theory-model
description: Use when a development model is needed to interpret an empirical result or to run a policy counterfactual for a The World Bank Economic Review (WBER) manuscript, or when deciding whether a formal model is needed at all. Disciplines the model-to-data link and the counterfactual; it does not run estimation or write prose.
---

# Theory and Model Craft (wber-theory-model)

## When to trigger

- A reduced-form result needs a model to interpret a mechanism or run a counterfactual
- A referee asks "what is the model that rationalizes this?" or "what does welfare do?"
- You want to extrapolate beyond the estimated policy to an un-tried policy (requires structure)
- The paper has a heavy model but it is decorative — it does not discipline the empirics or the counterfactual
- You are unsure whether WBER expects a formal model here at all

## Does WBER even want a model here?

WBER publishes both **theoretical and empirical** development research, but most accepted papers are empirical, and **a formal model is a means, not a merit badge**. Add a model only when it earns its place:

- **To interpret** — convert a reduced-form coefficient into a structural parameter (an elasticity, a friction) policymakers can reason about.
- **To extrapolate** — answer a counterfactual the data alone cannot (an un-tried transfer size, a national roll-out, a price change).
- **To aggregate** — move from a partial-equilibrium treatment effect to a general-equilibrium or welfare statement.

If none of these apply, a clean reduced-form evaluation with a clearly stated conceptual framework is the better WBER paper. A decorative model that the empirics ignore is a liability — it invites referee attacks for no payoff.

## Disciplining a development model

- **Tie every parameter to data.** Name what in the developing-country data identifies each parameter (a moment, an elasticity, an experimental treatment effect). "We calibrate to the literature" is weak; "the experimental LATE pins the take-up elasticity" is strong.
- **Match the friction to the setting.** Development models live or die on the right friction: credit/insurance constraints, missing markets, information asymmetries, enforcement/state-capacity limits, search frictions in informal labor markets. Use the one the data support, not a textbook default.
- **Validate out of sample.** Show the model reproduces a moment it was not fit to — ideally a treatment effect from the very experiment/reform that motivates the paper.
- **Make the counterfactual honest.** State which parameters you assume are policy-invariant (Lucas critique) and why; bound the GE channels you cannot fully model.

## Reduced-form ↔ structure handoff

| You have... | Add a model only if... | Otherwise |
|-------------|------------------------|-----------|
| A clean RCT/quasi-experimental effect | You need to extrapolate to an un-tried policy or aggregate to welfare | Report the effect + a conceptual framework; skip the model |
| A structural estimate | You can tie parameters to data and validate untargeted moments | Reconsider — calibration-in-disguise will be flagged |
| A policy counterfactual claim | The model is identified from credible variation | Do not run the counterfactual on calibrated guesses |

## Referee pushback mapped to the model fix

- *"What rationalizes this reduced-form pattern?"* → Add the *minimal* model that generates it; do not over-build. Show the model's comparative static matches the sign and rough magnitude you estimate.
- *"Your parameters are calibration in disguise."* → Tie each parameter to a data moment and report which moment moves which parameter; validate on an untargeted moment.
- *"The counterfactual assumes invariance you never defend."* → State explicitly which behavioral parameters you treat as policy-invariant and argue why the Lucas critique does not bite here.
- *"This is a rich-world model bolted onto a poor-country setting."* → Replace the frictionless core with the binding development friction (credit, insurance, information, enforcement) the data reveal.
- *"The model adds nothing the regressions don't."* → Either give it a job (a counterfactual the data cannot answer) or cut it to a conceptual framework.

## Checklist

- [ ] The model's job is named: interpret, extrapolate, or aggregate (not decoration)
- [ ] Each parameter is tied to identifying variation in the developing-country data
- [ ] The friction matches the setting (credit/insurance/information/enforcement/search)
- [ ] An untargeted moment or out-of-sample treatment effect validates the model
- [ ] Counterfactual states policy-invariance assumptions and bounds GE channels
- [ ] Model assumptions are kept separate from policy interpretation in the text
- [ ] If no model is warranted, a clear conceptual framework replaces it

## Theory-to-policy translation

Whatever its form, the model or framework must end in something a development policymaker can use. A structural elasticity should be reported as "a 10% subsidy raises adoption by X%"; a welfare statement should net out fiscal cost; a counterfactual should name the un-tried policy and its predicted effect with a stated uncertainty range. WBER's value-add over a pure-methods outlet is exactly this last step — the model exists to make a development decision tractable, not to demonstrate technique. If you cannot translate the model's output into a policy magnitude, reconsider whether the model is doing real work.

## Anti-patterns

- A decorative model the empirical section never uses or tests
- Calibrating to "the literature" and running a welfare counterfactual on unvalidated parameters
- A first-world frictionless model imposed on a setting defined by missing markets
- Running an un-tried-policy counterfactual without arguing policy-invariance
- Treating a model as a substitute for credible identification rather than a complement
- Reporting model output in abstract parameter units a policymaker cannot use
- Escalating to a full structural model when a conceptual framework would do the job

## Worked vignette (illustrative)

A paper estimates a sharp RD effect of a fertilizer subsidy on yields but the policy question is "what subsidy *level* maximizes welfare net of fiscal cost?" — which the single threshold cannot answer. The WBER-appropriate move: write a small household model with a credit constraint, pin the adoption elasticity to the RD jump and the constraint to observed liquidity heterogeneity, validate by reproducing the (untargeted) take-up gradient across wealth, then trace welfare across subsidy levels. The model earns its place because it answers a counterfactual the RD cannot, and it is disciplined by the same variation that identifies the reduced-form effect.

## When a conceptual framework beats a formal model

For many WBER empirical papers, the right "theory" is a tight conceptual framework, not a solved model: a clear statement of the agents, the binding constraint, and the predicted sign of the policy's effect. A framework earns its place when it (a) motivates the empirical specification, (b) makes the mechanism falsifiable, and (c) tells the reader what *would not* happen if the mechanism were absent. It avoids the trap of a formal model that the data ignore. Use a framework when you need to organize intuition and discipline interpretation; escalate to a formal model only when you must extrapolate or aggregate.

## Output format

```text
【Model's job】interpret / extrapolate / aggregate / NONE (framework only)
【Parameters ↔ data】each parameter tied to identifying variation
【Friction】credit / insurance / information / enforcement / search
【Validation】untargeted moment or out-of-sample treatment effect
【Counterfactual】policy-invariance assumptions + GE bounds
【Next step】wber-robustness
```
