---
name: jpe-theory-model
description: Use when a Journal of Political Economy (JPE) manuscript needs an explicit economic model or mechanism — either a theory paper's model, or the framework that gives a reduced-form empirical result its economic meaning. Builds and disciplines the economic argument; it does not run estimation (see jpe-identification).
---

# Theory & Mechanism Model (jpe-theory-model)

## When to trigger

- A reduced-form result has no model or stated mechanism behind it ("what is the economics?")
- A structural/theory paper's model exists but its assumptions or comparative statics are not disciplined
- The empirical specification is not derived from, or connected to, any economic framework
- A referee will ask which economic force drives the result and you cannot point to one

## Why this is the JPE hallmark

JPE's identity is tight theoretical framing — the Chicago price-theory tradition that produced Becker's "Crime and Punishment: An Economic Approach" (JPE 1968) and the Black–Scholes option-pricing model (JPE 1973). Even empirical papers are read as tests of economic reasoning: **"What does theory predict, and does the evidence bear it out?"** The model need not be elaborate; a one- or two-equation framework that delivers a sharp, testable comparative static is often stronger than a baroque one. Internal consistency of the economic argument is scrutinized harder here than almost anywhere. If the contribution is a deep, self-contained macro model, weigh **JPE Macroeconomics** (companion journal, lead editor Greg Kaplan); a sharp theory or market-design result may suit **JPE Microeconomics** (lead editor John List) instead of the flagship.

Two modes:

- **Theory-led paper:** the model is the contribution; empirics (if any) illustrate or test it.
- **Empirics-led paper:** a compact model or explicit mechanism organizes the empirics, generates the prediction being tested, and gives the estimate its interpretation.

## Building / disciplining the model

### Minimal-model discipline (for empirics-led papers)
- Write the smallest model whose comparative static *is* the empirical prediction. Tie one model object to one estimated coefficient.
- State agents, their objective, the constraint, and what they optimize over. Price-theoretic logic — substitution, scarcity, incentives, market clearing — should be visible.
- Derive the sign/shape prediction the data will test, and say what evidence would *refute* it.
- Check the partial-equilibrium result against general equilibrium: does the effect survive when prices/quantities adjust elsewhere? If not, say so and bound it.

### Full-model rigor (for theory-led / structural papers)
- Assumptions: each one earns its place; flag which are substantive vs. technical convenience.
- Existence/uniqueness of equilibrium where relevant; comparative statics stated as propositions.
- Welfare analysis: who gains, who loses, and the efficiency benchmark.
- Map structural parameters to identifying variation before estimation (hand off to `jpe-identification`).
- Robustness of qualitative conclusions to the key assumptions; counterfactuals.

## Consistency checks a Chicago referee runs

- Do agents in the model behave optimally given prices and incentives?
- Does the market clear, and does the result survive equilibrium adjustment?
- Are there unmodeled selection or entry/exit margins that would overturn the conclusion?
- Is the comparative static the paper tests actually a *prediction* of the model, or assumed?
- Does the welfare claim follow from the model, or is it asserted?

## Checklist

- [ ] An explicit model or written-down mechanism exists
- [ ] One testable comparative static is derived and mapped to an estimated object
- [ ] Optimization, incentives, and market clearing are visible in the logic
- [ ] General-equilibrium / selection feedback considered (or bounded if assumed away)
- [ ] Assumptions labeled substantive vs. technical
- [ ] Welfare / efficiency implications follow from the model, not asserted
- [ ] The model is the *smallest* one that delivers the result (no gratuitous generality)

## Anti-patterns

- An empirical result with no model and no mechanism — "we find an effect" with no economic story
- A model whose comparative statics are never connected to the data
- Partial-equilibrium conclusions that ignore obvious GE feedback a referee will raise
- A needlessly elaborate model that obscures rather than sharpens the economic point
- A black-box quantitative model with no "what identifies what" mapping — a frequent JPE referee complaint
- Assumptions chosen for tractability that secretly drive the headline result
- Welfare statements that do not follow from the stated objective function

## Output format

```
【Mode】theory-led / empirics-led
【Core mechanism】the economic force in one sentence
【Model primitives】agents / objective / constraint
【Testable prediction】comparative static + the estimated object it maps to
【GE / selection check】survives equilibrium adjustment? [y/n + note]
【Welfare】who gains/loses; efficiency benchmark
【Next】jpe-identification (to test it) or jpe-robustness
```
