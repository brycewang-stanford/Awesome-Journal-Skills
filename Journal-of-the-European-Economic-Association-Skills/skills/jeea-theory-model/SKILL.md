---
name: jeea-theory-model
description: Use when a Journal of the European Economic Association (JEEA) manuscript contains a theoretical or structural model whose assumptions, generality, or results need sharpening to the journal's general-interest bar. Disciplines the model and makes its results legible; it does not run empirics or polish prose.
---

# Theory & Model Craft (jeea-theory-model)

## When to trigger

- A model's assumptions are convenient but their role in the result is opaque
- A referee says the main proposition is "a special case" or "not general enough"
- The model is technically correct but the economic intuition is buried
- A structural model needs its mapping to data and counterfactuals made disciplined

## The JEEA theory bar

JEEA publishes **micro and macro theory** alongside empirics at a **general-interest** standard, so a model must earn its place by delivering a **result a broad economist finds illuminating**, not by technical machinery alone. The bar is: assumptions are **disciplined and motivated**, the headline result is **sharp and general enough that it is not an artifact of a convenient functional form**, the **economic intuition is stated in words**, and (for structural work) the model **maps to data and delivers a counterfactual** the reduced form cannot. Theory at JEEA is judged less like a pure-theory field journal (generality for its own sake) and more like a general-interest outlet (a memorable, robust economic lesson).

## Model discipline moves

- **Motivate every assumption.** For each assumption, state what it buys and what it would cost to relax. Flag the one or two assumptions that truly drive the result.
- **State the result in words first.** A reader should grasp the proposition before the proof; the math confirms the intuition, it does not replace it.
- **Generality vs. tractability.** Show the result is not a knife-edge: relax functional forms, parameter ranges, or timing where feasible; if the result needs a special case, say so and justify it.
- **Comparative statics with sign and interpretation.** Each comparative static should have an economic story, not just a derivative sign.
- **Proof hygiene.** Main-text proofs for the headline result kept legible; long or auxiliary proofs to the appendix; lemmas labeled by what they do.
- **Structural mapping (if applicable).** Tie primitives to data features (route to `jeea-identification` Branch A), report fit, and argue counterfactual validity.

## Checklist

- [ ] Headline result stated in plain economic language before any proof
- [ ] The 1–2 driving assumptions named; relaxation discussed
- [ ] Result shown not to hinge on a convenient functional form (or the special case is justified)
- [ ] Comparative statics carry economic interpretation, not just signs
- [ ] Proofs organized: headline in main text, auxiliary in appendix/online appendix
- [ ] Structural: primitives mapped to data; counterfactual validity argued
- [ ] A general-interest reader can extract the lesson without the algebra

## Theory vs. structural: two JEEA modes

JEEA publishes both **analytic theory** (the result is a proposition) and **structural/quantitative work** (the result is a number the model delivers). The discipline differs:

- **Analytic theory:** the payoff is a general, robust proposition with a clear mechanism. Generality and minimal assumptions are the currency; an empirical illustration, if any, supports the result rather than carrying it.
- **Structural / quantitative:** the payoff is a magnitude and a counterfactual. Here identification of parameters (route to `jeea-identification` Branch A) and fit to data discipline the model, and the counterfactual must be one a reduced form cannot deliver.

Know which mode you are in: a structural paper judged as pure theory (or vice versa) reads as mismatched to a co-editor.

## Anti-patterns

- A proposition that holds only under a convenient functional form, presented as general
- Assumptions chosen for tractability with no statement of what they cost
- A wall of algebra with the economic intuition never stated in words
- Comparative statics reported as derivative signs with no interpretation
- A structural model with no counterfactual — machinery without payoff
- Treating JEEA as a pure-theory journal that rewards generality without a general-interest lesson
- A model so elaborate the general-interest lesson disappears into special cases

## Worked vignette (illustrative)

A bargaining model yields an efficient outcome only under a specific surplus-sharing rule. A weak draft presents this as a general efficiency theorem. A JEEA-grade revision states the intuition first ("efficiency obtains because the sharing rule aligns marginal incentives"), names the sharing rule as the driving assumption, shows the result degrades smoothly as the rule deviates (illustrative: efficiency loss rises to about 12% at a 30% deviation), and draws the general lesson about when decentralized bargaining is efficient. The model now teaches something that travels.

## Output format

```
【Headline result (in words)】[...]
【Driving assumptions】[the 1–2 that matter] + relaxation
【Generality】[robust / justified special case]
【Comparative statics】[sign + economic story]
【Structural mapping】[primitives→data; counterfactual] (if applicable)
【Next step】jeea-identification or jeea-robustness
```
