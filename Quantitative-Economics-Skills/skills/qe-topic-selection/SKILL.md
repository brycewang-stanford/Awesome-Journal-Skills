---
name: qe-topic-selection
description: Use early, when judging whether a project fits Quantitative Economics (QE) — a substantive economic question answered with serious quantitative methods (empirical, structural/computational, experimental, or simulation), sister to Econometrica and Theoretical Economics. Tests fit and sharpens the question; it does not design the estimation.
---

# Topic Selection (qe-topic-selection)

## When to trigger

- You have data, a model, or an experiment but are unsure QE is the right home
- The project feels like "pure theory" or "pure method" and you suspect a sibling journal fits better
- The economic question behind the quantitative exercise is not yet sharp
- You are choosing between QE, Econometrica, and a top field journal

## The QE fit bar

QE is the Econometric Society's **general-interest, empirically and quantitatively oriented** journal. Its comparative advantage among the ES trio is explicit: **Econometrica** leans theoretical/methodological, **Theoretical Economics** is pure theory, and **QE** publishes papers that **develop or apply quantitative methods to substantive economic questions** — empirical, computational/structural, experimental, and simulation-based — with a strong premium on **documented data and reproducible code**. The fit test is two-pronged:

1. **Is there a first-order economic question?** A quantitative exercise with no economic payoff (an estimator with no application, a simulation with no question) drifts toward Econometrica or a methods outlet.
2. **Does answering it require serious quantitative work?** A purely descriptive note without methodological or computational content under-fits QE's quantitative identity.

The sweet spot is a paper where the **method and the answer reinforce each other**: a structural model that delivers a counterfactual a reduced-form design cannot; an empirical design that pins down a parameter the literature has only assumed; an experiment whose data discipline a quantitative model; a simulation that resolves a measurement puzzle.

## Paper archetypes that fit QE

- **Structural / computational:** estimate a model, then run a policy counterfactual or welfare calculation.
- **Applied micro / finance with quantitative ambition:** a credible causal design whose magnitudes feed an economic quantity of interest.
- **Experimental:** lab / lab-in-the-field / online experiments whose data identify a parameter or test a quantitative theory (note QE's Jan 2026 pre-registration and instructions rules).
- **Simulation-based / measurement:** new data or methods that quantify something previously unmeasured, with reproducible code.

## Checklist

- [ ] The substantive economic question is stated in one sentence a non-specialist cares about
- [ ] The quantitative method is necessary to answer it (not decoration, not the whole point)
- [ ] The contribution is general-interest, not confined to one narrow subfield
- [ ] Data and code can be documented and made non-exclusive (ES policy) — no fatal access barrier
- [ ] QE beats the sibling alternatives: not pure theory (TE), not method-first (Econometrica)
- [ ] If experimental/own-data: a recognized pre-registration is feasible (effective Jan 2026)

## Anti-patterns

- A new estimator with a toy application — likely Econometrica, not QE
- A pure theorem with no quantification — Theoretical Economics
- A descriptive note with no quantitative or methodological content
- A question so narrow that only one subfield would cite the answer
- Data so locked down that the ES reproducibility regime cannot be satisfied

## Output format

```
【Question】one sentence, general-interest?
【Quantitative method】structural / empirical / experimental / simulation
【Why the method is necessary】...
【Sibling check】not pure theory (TE), not method-first (Econometrica)? [Y/N]
【Reproducibility feasible】data/code can be documented + non-exclusive? [Y/N]
【Next step】qe-literature-positioning
```
