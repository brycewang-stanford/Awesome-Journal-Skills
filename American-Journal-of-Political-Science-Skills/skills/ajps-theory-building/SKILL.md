---
name: ajps-theory-building
description: Use when building the theoretical argument of an American Journal of Political Science (AJPS) manuscript — whether empirical with explicit mechanisms, formal/game-theoretic, or measurement-driven. AJPS rewards testable theory tightly linked to the empirical strategy, with hypotheses stated before the results. Structures the argument; it does not run analyses.
---

# Theory & Argument Building (ajps-theory-building)

At AJPS the theory exists to **generate testable expectations** that the design and data then
adjudicate. The journal's empirical bar means a model or argument earns its place only if it yields
**observable, falsifiable implications** that the analysis can confront. This skill turns an idea into
hypotheses, mechanisms, and scope conditions in the idiom your work demands.

## When to trigger

- The empirics are strong but the "why" / mechanism is thin
- A reviewer said the paper is "atheoretical," "ad hoc," or "a model with no test"
- You need to state mechanisms, assumptions, and scope conditions explicitly
- Formal modeling: deciding what to model, what to assume, and what the model buys

## Build the argument (by mode of work)

### Empirical paper with a theory
1. **Concept** — define key constructs precisely; distinguish from neighbors and from how they will be
   measured (hand off to `ajps-data-analysis` for validation).
2. **Mechanism** — the causal story: who acts, why, under what incentives/constraints.
3. **Hypotheses** — state the **directional, testable** expectations *before* the results, and what
   pattern would **disconfirm** them. These become the tests in `ajps-research-design`.
4. **Scope conditions** — where the argument holds and where it does not.

### Formal / game-theoretic paper
- State the **substantive puzzle** the model addresses before the setup.
- Keep assumptions **transparent and motivated**; flag which results depend on which assumptions.
- Translate equilibrium predictions into **comparative statics** a reader can test or recognize.
- Make the empirical test follow from the model, and distinguish predictions **unique** to your model
  from those shared with rivals.

### Measurement / methodology paper (Research Note territory)
- Define the quantity the new measure/method recovers and the bias in existing approaches.
- State the conditions under which it outperforms incumbents, with a validation plan.

## The "testability" gate (AJPS-specific)

Before proceeding, write the sentence: *"If the theory is right, we should observe ___; if a rival is
right, we should observe ___ instead."* If you cannot fill both blanks with something the data can
distinguish, the theory is not yet ready for an AJPS empirical confrontation.

## Anti-patterns

- HARKing — fitting hypotheses to results after the fact; state theory before tests, preregister where possible
- A model whose assumptions are reverse-engineered to deliver the desired prediction
- Mechanisms named but never made observable or testable
- Universal claims with no scope conditions
- Burying the argument under the empirics — the contribution must be stated plainly up front

## Output format

```
【Core claim】one sentence
【Mechanism】the causal/logical story
【Hypotheses】directional, stated before results
【Assumptions】(formal) the load-bearing ones
【Disconfirming pattern】what would falsify it
【Scope conditions】where it holds / fails
【Next】ajps-research-design
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — formal-modeling and analysis tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — AJPS scope and contribution expectations
