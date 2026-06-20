---
name: jegeo-theory-model
description: Use when the model or conceptual frame is the bottleneck for a Journal of Economic Geography (JEG) manuscript — NEG / quantitative-spatial models OR conceptual frameworks from human geography. Makes the mechanism legible to both communities; it does not invent results.
---

# Theory and Model Craft (jegeo-theory-model)

## When to trigger

- The empirics are strong but there is no mechanism — just a gravity structure or a set of correlations with space as a fixed effect
- A formal NEG/quantitative-spatial model is in place but a geographer reviewer cannot see what economic-geography *story* it tells
- A conceptual paper (evolutionary/institutional/relational) has rich theory but an economist reviewer cannot see a testable or generalizable claim
- The model's spatial assumptions (mobility, trade costs, externality range, spatial scale) are buried or undefended

## Two modes of theorizing — choose deliberately

JEG accepts both **formal models** and **conceptual frameworks**, but each must be made legible to the other community. Decide which mode you are in, then do the work that makes the other side trust it.

### Mode A: Formal model (NEG / quantitative-spatial)

The lineage runs from core-periphery NEG (Krugman; Fujita-Krugman-Venables) to the estimable quantitative-spatial models (Redding-Rossi-Hansberg, Allen-Arkolakis, Donaldson-Hornbeck). A JEG formal model must:

- **Carry an economic-geography mechanism a geographer can name** — agglomeration force vs. dispersion force, why firms/people locate where they do, what makes the equilibrium spatial. A black-box gravity equation with no told mechanism reads as econometrics, not economic geography.
- **State spatial assumptions explicitly:** factor mobility, trade/commuting costs, the *range* over which externalities operate, and the spatial scale of the equilibrium. These are modeling choices with geographic content, not technicalities.
- **Discipline the counterfactual:** be clear which spatial linkages drive the general-equilibrium result, and resist welfare claims the spatial structure cannot bear.
- **Map model objects to data** so the identification skill has something to bite on.

### Mode B: Conceptual framework (evolutionary / institutional / relational)

The lineage includes evolutionary economic geography (relatedness, branching, path dependence, regional resilience — Boschma, Frenken), institutional and relational approaches, and GPN/GVC theory (Coe, Yeung). A JEG conceptual contribution must:

- **Produce a generalizable claim, not a description** — propositions, a typology, or a mechanism that travels beyond the motivating case.
- **Be falsifiable or at least testable in principle**, so an economist sees a claim, not only a narrative.
- **Define its constructs operationally enough** that someone could measure or observe them (what *is* relatedness, lock-in, embeddedness, in this paper).

## The bridge move (what wins at JEG)

| If you are a... | The trust-building move the other community needs |
|------------------|---------------------------------------------------|
| formal modeler | name the agglomeration/dispersion mechanism in plain prose; tie a coefficient to a geographic story |
| conceptual theorist | extract one testable proposition and operationalize one construct |
| empiricist with no model | install a minimal mechanism that organizes the regressions (why this sign, this scale) |

## Checklist

- [ ] Mode chosen (formal vs. conceptual) and the mechanism stated in plain prose
- [ ] Formal: agglomeration/dispersion forces named; spatial assumptions (mobility, costs, externality range, scale) explicit
- [ ] Formal: counterfactual disciplined; which spatial linkages drive it is stated
- [ ] Conceptual: a generalizable, testable-in-principle claim, not a description
- [ ] Conceptual: key constructs operationally defined
- [ ] Model objects map to data (or constructs map to observables)
- [ ] A reader from the *other* community can restate the mechanism in one sentence

## Anti-patterns

- A gravity/quantitative-spatial structure presented with no economic-geography mechanism (econometrics in disguise)
- A welfare counterfactual whose spatial linkages are never made transparent
- A conceptual framework that only redescribes the case and yields no claim that travels
- Constructs (relatedness, embeddedness, lock-in) invoked but never defined or operationalized
- Treating the model as decoration bolted onto a finished empirical section
- Spatial scale and externality range chosen implicitly, then never justified

## Worked vignette (illustrative)

A paper estimates a quantitative-spatial model of remote-work adoption reshaping city systems. The math is clean but a geographer referee says it has no mechanism — agglomeration just falls out of the parameters. The fix is not more equations: it is one paragraph naming the force (face-to-face knowledge externalities weaken as remote work rises, so the dispersion force gains relative to the agglomeration force) and tying the key elasticity to that story. Now both communities read the same mechanism, and the counterfactual reallocation of activity across the urban hierarchy is interpretable rather than mechanical.

## Referee pushback mapped to the model/frame fix

- *"This is just gravity — where is the economic geography?"* → Add the prose mechanism (which agglomeration/dispersion force, why firms move) and tie a key coefficient to it.
- *"The welfare counterfactual is a black box."* → Make transparent which spatial linkages and parameters drive it; show sensitivity to the most contestable one.
- *"Your framework only describes this case."* → Extract a proposition that travels and state the conditions under which it should hold elsewhere.
- *"What exactly is 'embeddedness' here?"* → Operationalize the construct: how would you observe or measure it, in this paper.
- *"The model is decoration."* → Show the model organizing the empirics — predicting a sign, a scale, or a heterogeneity the regressions then test.

## Spatial scale and externality range are theoretical choices

A recurring JEG-specific failure is treating the spatial scale of the equilibrium and the *range* over which an externality operates as data-handling details. They are theoretical commitments: a knowledge spillover that matters within 25km implies a different model — and a different unit of analysis — than one operating at the regional scale. State these ranges as part of the theory, justify them, and make sure the empirical scale matches the theorized range. A model whose externality is "local" but whose data are national is internally inconsistent, and both communities will notice.

## Output format

```text
【Journal】Journal of Economic Geography
【Skill】jegeo-theory-model
【Mode】formal (NEG/quantitative-spatial) / conceptual (EEG/institutional/GPN)
【Mechanism in plain prose】one sentence both communities can restate
【Spatial assumptions / constructs】mobility, costs, externality range, scale | or defined constructs
【Counterfactual / generalizable claim】what it supports, what it does not
【Model→data (or construct→observable)】mapping
【Next skill】jegeo-robustness
```
