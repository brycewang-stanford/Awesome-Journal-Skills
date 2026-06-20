---
name: eer-theory-model
description: Use when a European Economic Review (EER) manuscript needs a theoretical model built or tightened — a pure-theory result, a quantitative/structural macro model, or a conceptual frame disciplining an empirical paper. Sharpens the model's contribution, assumptions, and link to data; it does not run the empirical identification or robustness.
---

# Theory & Model Craft (eer-theory-model)

## When to trigger

- The paper is pure theory and the result needs to be sharp and general
- A macro/quantitative model needs discipline (calibration/estimation, mapping to data)
- An empirical paper needs a model to organize the mechanism and interpret estimates
- Reviewers ask "what is the model adding?" or "why these assumptions?"

## The EER theory bar

EER publishes **theory and empirical work across all fields**, so a model is judged on whether it yields a **general, interpretable result a non-specialist can grasp** — not machinery for its own sake. For pure theory: the proposition must be **clean, general, and economically meaningful**, with assumptions that are minimal and defended. For quantitative/structural work: the model must be **disciplined by data** (calibration targets or estimation) and used to deliver a **counterfactual or quantity** a reduced-form design cannot. For theory-disciplining-empirics: the model must **organize the mechanism** and tell the reader what the estimates mean.

## Branch paths

### Branch A: Pure / micro theory
- **State the main result first** (proposition), then the assumptions it needs — minimal and economically motivated.
- Argue **generality**: does the result depend on a knife-edge assumption? Show robustness of the *theoretical* result to weakening key assumptions.
- Provide **intuition** for every formal result — a generalist reader must see *why* it holds.
- Keep proofs of key results in the main paper or a clearly-organized appendix.

### Branch B: Quantitative / structural model
- **Discipline by data:** state calibration targets or the estimation objective (MLE/GMM/MSM/SMM); report sources for every parameter.
- **Identification of parameters:** tie each estimated parameter to the data feature/moment that pins it (hand off the empirical side to `eer-identification` where relevant).
- **Fit:** report fit to targeted moments and validate against **untargeted** moments.
- **Counterfactual:** argue the parameters are policy-invariant enough for the experiment you run (Lucas critique); carry uncertainty into the counterfactual.

### Branch C: Theory disciplining an empirical paper
- The model exists to **interpret** estimates: derive the sign/comparative static the empirics test.
- Map model objects to estimable parameters; state what the empirical coefficient *is* in the model.
- Avoid a decorative model that the empirics do not actually test.

## Checklist

- [ ] Branch chosen; the model's job stated in one sentence
- [ ] Pure theory: main proposition stated first; assumptions minimal + defended; intuition given
- [ ] Generality argued (result not a knife-edge artifact)
- [ ] Quantitative: calibration/estimation discipline; parameter sources; targeted + untargeted fit
- [ ] Counterfactual rests on a defended policy-invariance argument; uncertainty carried
- [ ] Theory-for-empirics: model delivers the testable comparative static the data examine
- [ ] A non-specialist can state what the model adds in one sentence

## Anti-patterns

- A model whose only role is decoration — the empirics never test its predictions
- A proposition that holds only under a knife-edge assumption presented as general
- Quantitative results with no untargeted-moment validation ("it fits what we asked it to")
- A counterfactual that assumes policy-invariant parameters without arguing for it
- Formal results with no intuition — opaque to the general-interest EER reader
- Burying the main theoretical result behind pages of setup

## Worked vignette (illustrative)

A growth paper builds an endogenous-growth model. A weak version states equilibrium equations and calibrates with no transitional analysis. An EER version states the main proposition first (the growth rate is globally stable under condition C), gives the economic intuition (a self-correcting innovation incentive), shows the result survives weakening C, and then quantifies the transition speed (illustrative half-life ~7 years) with sensitivity to the key elasticity. A generalist sees the lesson: why this class of models does not hinge on knife-edge scale effects.

## Output format

```
【Model role】pure theory / quantitative-structural / theory-for-empirics
【Main result】proposition or headline quantity, stated first
【Assumptions】minimal set + why each is economically reasonable
【Discipline】generality argument (theory) OR calibration/estimation + fit (quant)
【Counterfactual / testable implication】+ uncertainty / policy-invariance
【What it does NOT establish】[...]
【Next step】eer-identification (if empirics test it) or eer-robustness
```
