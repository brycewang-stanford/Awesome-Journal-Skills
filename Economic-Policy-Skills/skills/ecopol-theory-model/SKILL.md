---
name: ecopol-theory-model
description: Use when building or tightening the conceptual frame or quantitative model that disciplines an Economic Policy (EP) manuscript's policy logic. Keeps the model minimal-but-honest and legible to a policy audience; it does not invent evidence or citations.
---

# Theory and Model Craft (ecopol-theory-model)

## When to trigger

- The empirical results need a model to map estimates into a welfare or policy-cost statement
- A quantitative/structural model runs the counterfactual policy but its mechanism is opaque to a non-specialist
- The model is more elaborate than the policy question requires (a discussant will ask "why all this machinery?")
- The counterfactual policy scenario is computed but the policymaker cannot see *which assumption* drives the headline number
- Reviewers/discussants want the welfare interpretation, not just reduced-form effects

## EP's model standard: minimal, transparent, policy-bearing

EP is not a theory journal. A model earns its place only if it does policy work: it converts estimates into **welfare, fiscal cost, or distributional** statements; it disciplines a **counterfactual policy**; or it clarifies a **mechanism** that the reduced form cannot. The house style is accessible, so the model in the main text should be the **smallest model that carries the policy conclusion**, with derivations and extensions in the technical appendix. Two tests every EP model must pass:

1. **The transparency test.** Can a policymaker see which assumption produces the headline number, and how the number moves if that assumption changes? If the model is a black box, the policy discussant will not trust the recommendation.
2. **The necessity test.** Remove the model — does the policy claim survive? If yes, the model is decoration; cut it to the appendix. If no, the model *is* the contribution and must be defended.

## Decision table: how much model does this paper need?

| The paper's job | Model role | Where it lives |
|-----------------|-----------|----------------|
| Estimate a causal policy effect, no welfare claim | none / a one-equation framing | main text, a paragraph |
| Turn effects into welfare or fiscal cost | a small sufficient-statistic / accounting model | main text, few equations; derivation in appendix |
| Simulate a not-yet-enacted reform | a calibrated/estimated structural model | mechanism in main text, full model in appendix |
| Explain a surprising mechanism | a stylized model isolating the channel | main text, deliberately minimal |

## Craft moves

- **Lead with the mechanism in words**, then formalize. The policy reader should grasp the channel before seeing a single equation.
- **Expose the key elasticity / sufficient statistic.** EP readers want to know "the answer depends mostly on parameter θ, which we estimate / take from the literature as X." Make θ visible and its source explicit.
- **Show the counterfactual's sensitivity** to the one or two assumptions that matter, in the main text — this is what a policymaker actually needs.
- **Calibration discipline:** every calibrated parameter gets a source and a sensitivity range; "standard values" without citation invites a discussant takedown.
- **Welfare framing:** state whose welfare, under what social objective, and what is omitted (distributional incidence, GE feedback, political constraints).

## Checklist

- [ ] The model passes the necessity test — without it the policy claim would not hold
- [ ] The mechanism is stated in plain words before formalization
- [ ] The key elasticity / sufficient statistic is named, sourced, and its value justified
- [ ] Counterfactual policy sensitivity to the one or two driving assumptions is shown in the main text
- [ ] Every calibrated parameter has a source and a sensitivity range
- [ ] Welfare/cost claims state whose welfare, the objective, and what is omitted
- [ ] Heavy derivations are in the technical appendix, not crowding the main text

## Anti-patterns

- A general-equilibrium apparatus where a one-line sufficient-statistic argument would do — over-modeling for a policy audience
- A black-box structural model whose headline number the reader cannot trace to an assumption
- "Standard calibration" with no citations and no sensitivity range
- A welfare statement that hides the distributional incidence a policymaker most cares about
- Model derivations dominating the main text and burying the policy message

## Output format

```text
【Journal】Economic Policy (EP)
【Skill】ecopol-theory-model
【Model role】framing / welfare-accounting / structural-counterfactual / mechanism
【Necessity test】does the policy claim need the model? Y/N
【Key parameter】θ = <value> (source) ; headline sensitivity to θ
【Welfare framing】whose welfare / objective / what is omitted
【Main-text vs appendix】what stays / what moves to appendix
【Next skill】ecopol-robustness
```
