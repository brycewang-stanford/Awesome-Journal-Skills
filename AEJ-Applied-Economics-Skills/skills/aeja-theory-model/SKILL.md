---
name: aeja-theory-model
description: Use when an American Economic Journal: Applied Economics (AEJ: Applied) manuscript needs a model to interpret, discipline, or structure its empirical estimates — not to lead the paper. Calibrates how much theory belongs in an empirical-first journal and where it goes; it does not design the identification (aeja-identification) or build a standalone structural estimation.
---

# Theory & Model for Interpretation (aeja-theory-model)

## When to trigger

- A referee asks "what is the mechanism / what model rationalizes this?"
- The reduced-form estimate is credible but its economic meaning is ambiguous
- You want a welfare statement, an elasticity, or a counterfactual the raw estimate cannot deliver
- You are tempted to lead the paper with a full structural model and need to right-size it for AEJ: Applied

## The AEJ: Applied theory dial

AEJ: Applied is **empirical-first**. Theory earns its place only when it **interprets the estimate, sharpens the estimand, or unlocks a magnitude the design cannot deliver alone** — never as the headline. Pick the lightest tool that does the job and keep the empirical estimate the star.

| Theory's job | Right amount of model | Where it goes |
|--------------|-----------------------|---------------|
| Name the mechanism | a few equations / a conceptual framework | short section before results |
| Map a reduced-form coefficient to a structural parameter | a sufficient-statistic / envelope argument | inline derivation + appendix |
| Deliver a welfare or counterfactual number | a calibrated or partially-structural model | a dedicated section, clearly bounded |
| Discipline heterogeneity / sign predictions | a simple model generating testable comparative statics | framework section, tested in results |

### Sufficient-statistic style (often the AEJ: Applied sweet spot)
Where possible, express the welfare/policy object as a function of **estimable elasticities** (a Harberger/Chetty-style sufficient statistic) rather than estimating a full structural model. This keeps the credibility in the reduced-form design while delivering an economic magnitude. State the assumptions under which the sufficient statistic is valid and what it omits.

### When a fuller model is warranted
If the question genuinely requires out-of-sample counterfactuals or unobservable primitives, a small structural model is acceptable — but tie each parameter to a data feature, validate against an untargeted moment, and never let the model's assumptions silently replace the identification the design provided.

## Checklist

- [ ] Theory's job named (mechanism / mapping / welfare / comparative statics)
- [ ] Lightest adequate tool chosen; model does not upstage the empirical estimate
- [ ] If a sufficient statistic: the estimable elasticities and validity assumptions stated
- [ ] If structural: each parameter tied to a data feature; an untargeted-moment validation shown
- [ ] Comparative statics / sign predictions made *before* they are tested
- [ ] Welfare/counterfactual numbers carry their own uncertainty and stated scope

## Anti-patterns

- Leading an empirical AEJ: Applied paper with a full structural model (reads as a different journal)
- A "model" section that is decorative — adds notation but no testable prediction or magnitude
- Letting model assumptions quietly substitute for the identification the design was supposed to provide
- A welfare number with no uncertainty and no statement of what the model omits
- Comparative statics derived after seeing the results (HARKing the theory)

## Worked vignette (illustrative)

A clean RD shows a tuition subsidy raises enrollment by 4.2pp (s.e. 1.1). The number is credible but the policy question is the welfare gain. Instead of building a full college-choice model, the paper uses a sufficient-statistic argument: the marginal value of public funds depends on the enrollment elasticity (estimated) and the fiscal externality of an extra graduate (calibrated from administrative tax data). This yields an MVPF of ~1.3 (illustrative) with a stated range, while the credibility still rests on the RD — the AEJ: Applied ideal.

## Referee pushback mapped to the theory fix

- *"What is the mechanism behind this reduced-form effect?"* → Add a short framework with a sign prediction
  you then test, or a channel-distinguishing test in the data — not more notation.
- *"This number is not policy-relevant without a welfare interpretation."* → Express the welfare object as a
  sufficient statistic of estimable elasticities; state the assumptions that make it valid.
- *"Your structural model just assumes the result."* → Tie each parameter to a data feature and validate
  against an untargeted moment; keep the credibility anchored in the reduced-form design.

## Output format

```
【Theory's job】mechanism / reduced-to-structural mapping / welfare / comparative statics
【Tool chosen】framework / sufficient statistic / small structural model
【Key relation】estimand = f(estimable elasticities / parameters): ___
【Validity assumptions + what it omits】[...]
【Magnitude delivered】[number + uncertainty + scope], or "none — interpretation only"
【Next step】aeja-robustness
```
