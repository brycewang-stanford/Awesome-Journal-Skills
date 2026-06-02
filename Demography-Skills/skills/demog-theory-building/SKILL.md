---
name: demog-theory-building
description: Use when building the argument of a Demography (PAA / Duke University Press) manuscript into a population-science contribution — whether the work is formal/mathematical demography, an explanatory account of fertility/mortality/migration, or a measurement/decomposition advance. Demography rewards a clear mechanism or a sharpened estimate over a bare correlation. Structures the argument; it does not run analyses.
---

# Theory & Argument Building (demog-theory-building)

At Demography a result is not a contribution until it is attached to a **claim population science can
use** — a mechanism that explains a demographic process, a sharper estimate that revises the record,
or a formal result that unifies or clarifies. This skill turns findings into argument: explicit
mechanisms, scope conditions, and observable implications, in the idiom appropriate to your kind of
work.

## When to trigger

- The empirics are strong but the "so what / why" is thin
- A reviewer said the paper is "descriptive," "atheoretical," or "just a correlation"
- You need to state mechanisms, identifying assumptions, or scope conditions explicitly
- Formal demography: deciding what to model and what the model buys you

## Build the argument (by mode of work)

### Explanatory population study
1. **Concept & measure** — define the demographic construct (e.g., parity progression, lifespan
   inequality, net migration) precisely; distinguish it from neighbors and from its measure.
2. **Mechanism** — the population story: which behaviors, exposures, or compositional shifts move the
   rate, for whom, and why (incentives, constraints, selection, cohort experience).
3. **Observable implications** — what we should see if the mechanism operates (age pattern, cohort
   signature, subgroup contrast) and what we should *not* see. These become the tests in
   `demog-research-design`.
4. **Scope conditions** — which populations, periods, and regimes the argument covers.

### Formal / mathematical demography
- State the **substantive population puzzle** the model addresses before the setup.
- Keep assumptions (stability, stationarity, Markov transitions, independence) **transparent and
  motivated**; flag which results depend on which assumptions.
- Translate results into **interpretable demographic quantities** (e.g., contributions to life
  expectancy, sensitivities/elasticities, equilibrium structure) a reader can recognize.
- Say what the model **buys**: a non-obvious decomposition, a unifying identity, a corrected intuition.

### Measurement / decomposition contribution
- Make explicit **what the new measure or decomposition separates** that prior work conflated (e.g.,
  tempo vs. quantum, composition vs. rate, age vs. cohort).
- Show the substantive payoff: the trend now attributes to a different component than was assumed.

## The "portability" test (Demography-specific)

Ask: *Could a demographer studying a different component or population import this mechanism, measure,
or decomposition?* If yes, you have a population-science contribution. If it only works for your exact
case, generalize the logic or reframe (back to `demog-topic-selection`).

## Anti-patterns

- "Hypothesizing after results are known" — state the argument before the tests
- A formal model with opaque assumptions chosen to produce the desired identity
- Mechanisms named but never made observable in age/cohort/subgroup patterns
- Treating a regression coefficient as a mechanism with no demographic story
- Universal claims with no scope conditions on population, period, or regime

## Output format

```
【Core claim】one sentence
【Mechanism / identity】the population story or formal result
【Assumptions】(formal) the load-bearing ones
【Observable implications】testable demographic signatures -> research-design
【Scope conditions】which populations / periods it covers
【Portability】who else in population science can use this
【Next】demog-research-design
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — formal-demography and decomposition tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — Demography scope and contribution expectations
