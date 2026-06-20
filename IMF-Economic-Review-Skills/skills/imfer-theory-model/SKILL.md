---
name: imfer-theory-model
description: Use when an IMF Economic Review (IMFER) manuscript needs an open-economy model to discipline, interpret, or generate counterfactuals for its evidence — whether a full international-finance model leads the paper or a light framework supports an empirical estimate. Right-sizes the theory to IMFER's policy-relevant bar; it does not design identification (imfer-identification) or run robustness (imfer-robustness).
---

# Theory and Model Craft (imfer-theory-model)

## When to trigger

- A referee asks "what open-economy mechanism rationalizes this cross-country fact?"
- A reduced-form spillover or capital-flow estimate is credible but its welfare meaning is unclear
- You need a counterfactual a regression cannot deliver (an alternative exchange-rate regime, a CFM rule, a debt-restructuring path)
- A structural open-economy / DSGE model leads the paper and you must show it is disciplined by data, not assumption
- You are tempted to bolt a generic NK-SOE model onto an empirical paper and need to right-size it
- A welfare or optimal-policy number is the headline and you must defend its calibration and invariance

## Why theory placement matters at IMFER

IMFER sits between the model-heavy international-finance tradition and the empirical-policy tradition, and the editor will route a paper to referees from whichever side it leads with. That makes the *placement decision* consequential: a strong reduced-form paper that opens with two pages of model derivation invites a theory referee who will judge the model on its own terms; a model-led paper with a thin empirical section invites an empirical referee who will find the discipline lacking. Decide early which tradition the paper belongs to, signal it in the structure, and make the other component genuinely earn its space rather than apologize for it.

## The IMFER theory dial

IMFER publishes **both** model-led international-finance papers and empirical papers with a supporting framework. The dial is set by what the policy question needs: theory earns its place when it **names a transmission channel, maps a reduced-form coefficient to a structural object, or delivers a counterfactual / welfare number a policymaker can use**. Because IMFER counterfactuals are read as policy advice, the model's credibility and its policy-invariance matter as much as its elegance. Generic notation that re-labels the empirical result, with no testable prediction or magnitude, is the classic mis-fit.

| Theory's job | Right amount of model | Where it goes |
|--------------|-----------------------|---------------|
| Name the open-economy mechanism (UIP deviation, financial accelerator across borders) | a few equations / conceptual frame | short section before results |
| Map a reduced-form coefficient to a structural parameter | a sufficient-statistic / log-linearized relation | inline derivation + appendix |
| Deliver a welfare or counterfactual number (regime, CFM, intervention) | a calibrated open-economy model | a dedicated, clearly bounded section |
| Generate cross-country sign/heterogeneity predictions | a simple model with comparative statics | framework section, tested in results |
| Lead the paper (model-first) | a full international-finance / SOE-DSGE model | the body, with data discipline |

### When the model leads
A model-first IMFER paper must still earn policy relevance: tie each parameter to a **data moment or external estimate** (an impulse response, a comovement, an external-finance premium), validate against an **untargeted moment**, and report the policy counterfactual with its uncertainty. State the assumptions under which the counterfactual is policy-invariant — a referee who suspects the Lucas critique bites will not trust the welfare number.

### When the model supports
For an empirical-first paper, pick the lightest tool: a sufficient-statistic expression in estimable elasticities often delivers the welfare object while keeping the credibility in the design. State what the sufficient statistic omits.

### The open-economy building blocks referees expect
When a model is the lead, IMFER referees look for the canonical international-finance ingredients to be present and motivated, not decorative: a **UIP/risk-premium block** if exchange rates matter; a **collateral or borrowing constraint** if you study sudden stops or financial crises; a **traded/non-traded split** for real-exchange-rate dynamics; a **foreign demand / terms-of-trade** channel for spillovers; and **incomplete markets** if the welfare result hinges on risk-sharing failures. Each should map to a moment you target and a counterfactual the policy question needs — a model that includes a block doing no work invites the "decorative" critique.

### Calibration vs. estimation — be explicit
IMFER referees distinguish sharply between *calibrated* and *estimated* parameters, and want each labeled. State which parameters are set from external sources (and cite them), which are estimated internally (and from what moment), and which are free. A model that quietly calibrates the parameter doing the welfare work — then reports a precise optimal-policy number — invites the charge that the result is assumed. Where the headline magnitude is sensitive to a calibrated value, show the welfare object across a defensible range of that value rather than a single point.

## Checklist

- [ ] Theory's job named (mechanism / mapping / welfare / comparative statics / lead)
- [ ] Lightest adequate tool chosen; model does not upstage a credible empirical estimate unless model-first
- [ ] Open-economy structure (international margin) is explicit, not a closed-economy model with a trade footnote
- [ ] Model-first: each parameter tied to a data moment / external estimate; untargeted-moment validation shown
- [ ] Calibrated vs. estimated vs. free parameters labeled; external calibrations cited
- [ ] Counterfactual/welfare numbers carry uncertainty and a stated policy-invariance argument
- [ ] Comparative statics / sign predictions stated *before* they are tested
- [ ] Policy counterfactual is the object a policymaker would actually weigh

## Anti-patterns

- A generic closed-economy NK model with a token "open economy" extension and no international mechanism
- A decorative "model" section that adds notation but no testable prediction or magnitude
- A policy counterfactual with no uncertainty and no policy-invariance defense (Lucas critique ignored)
- Letting model assumptions silently replace the identification the empirical design provided
- Comparative statics derived after seeing the results (HARKing the theory)
- A welfare number reported to three decimals as if calibration uncertainty did not exist
- Calibrating the parameter that drives the welfare result without showing sensitivity to it
- Including a canonical block (UIP, collateral constraint) that does no work in the result
- Failing to label which parameters are calibrated, estimated, or free

## Worked vignette (illustrative)

A panel shows a US monetary tightening cuts emerging-market capital inflows by 0.8% of GDP (s.e. 0.2). The number is credible but the policy question is the welfare cost and whether a CFM helps. Rather than a bespoke model, the paper writes a small open-economy model with a collateral constraint: the marginal welfare gain from a CFM depends on the estimated inflow elasticity and the calibrated pecuniary externality. This yields an optimal macroprudential tax of ~2% (illustrative) with a stated range, while the empirical credibility still rests on the high-frequency US-shock design — the IMFER ideal of theory disciplined by, and serving, the evidence.

## Referee pushback mapped to the theory fix

- *"What open-economy mechanism produces this cross-country fact?"* → Add a short framework with a sign or heterogeneity prediction you then test (e.g., the effect should be larger where FX exposure is higher), not more notation.
- *"This number is not policy-relevant without a welfare interpretation."* → Express the welfare object as a sufficient statistic of estimable elasticities, or via a lightly calibrated SOE model; state the validity assumptions.
- *"Your structural model just assumes the result."* → Tie each parameter to a data moment / external estimate and validate against an untargeted moment; keep credibility anchored in the design.
- *"The counterfactual ignores the Lucas critique."* → State why the estimated parameters are invariant to the policy you simulate, or bound the counterfactual to the regime where they are.

## Output format

```text
【Journal】IMF Economic Review
【Skill】imfer-theory-model
【Theory's job】mechanism / mapping / welfare / comparative statics / model-lead
【Tool chosen】framework / sufficient statistic / calibrated SOE model / full DSGE
【Open-economy mechanism】___
【Key relation】policy object = f(estimable / structural parameters): ___
【Counterfactual + uncertainty + policy-invariance】___
【Next skill】imfer-robustness
```
