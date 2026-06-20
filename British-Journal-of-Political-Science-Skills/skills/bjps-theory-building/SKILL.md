---
name: bjps-theory-building
description: Use when building the theoretical argument of a British Journal of Political Science (BJPS) manuscript into a contribution of general interest — whether the work is formal/game-theoretic, empirical with explicit mechanisms, interpretive, or normative. BJPS rewards a clear, portable argument over a bare finding. Structures the argument; it does not run analyses.
---

# Theory & Argument Building (bjps-theory-building)

At BJPS a result is not a contribution until it is attached to an **argument the field can use
elsewhere** — across countries, cases, and subfields. This skill turns findings into theory: explicit
mechanisms, scope conditions, and observable implications, in the idiom appropriate to your kind of
work.

## When to trigger

- The empirics are strong but the "so what / why" is thin
- A reviewer said the paper is "atheoretical," "ad hoc," or "just a finding"
- You need to state mechanisms, assumptions, and scope conditions explicitly
- Formal modeling: deciding what to model, what to assume, and what the model buys you

## Build the argument (by mode of work)

### Empirical paper with a theory
1. **Concept** — define the key constructs precisely; distinguish from neighbours.
2. **Mechanism** — the causal story: who does what, why, under what incentives/constraints.
3. **Observable implications** — what we should see if the mechanism operates (and what we should
   *not* see). These become the tests in `bjps-research-design`.
4. **Scope conditions** — where the argument holds and where it does not. Portability ≠ universality.

### Formal / game-theoretic paper
- State the **substantive puzzle** the model addresses before the setup.
- Keep assumptions **transparent and motivated**; flag which results are robust to which assumptions.
- Translate equilibrium predictions into **comparative statics** a reader can test or recognize.
- Say what the model **buys**: a non-obvious prediction, a resolution of a puzzle, a unifying logic.

### Interpretive / normative paper
- Make the **conceptual or normative stakes** explicit and connect them to political life.
- Build the argument through **reasons and texts**, not hypotheses; engage the strongest counter-view.
- Show what the argument lets the field **see or justify** that it could not before.

## The "portability" test (BJPS-specific)

Ask: *Could a scholar studying a different country, or working in another subfield, import this
mechanism/concept to their own problem?* If yes, you have a contribution of general interest. If the
argument only works for your exact case, tighten it into a general logic or reframe (back to
`bjps-topic-selection`). BJPS's international, cross-subfield readership is the audience for the
argument's portability.

## Anti-patterns

- "Hypothesizing after results are known" (HARKing) — state theory before tests; preregister where possible
- A model with opaque assumptions chosen to produce the desired result
- Mechanisms named but never made observable
- A single-case generalization with no scope conditions, or a universal claim with none
- Burying the argument under the empirics — the contribution paragraph must state it plainly

## Output format

```
【Core claim】one sentence
【Mechanism】the causal/logical story
【Assumptions】(formal) the load-bearing ones
【Observable implications】testable consequences → research-design
【Scope conditions】where it holds / fails (and across which cases)
【Portability】who else (which country/subfield) can use this argument
【Next】bjps-research-design
```

## Referee-pushback patterns and the BJPS-specific repair

- *"This is a finding, not a contribution."* → Attach the result to a mechanism with scope conditions and
  state the portable claim a scholar elsewhere could import.
- *"The argument only works for this one country."* → Generalize the logic: name the institutional or
  behavioural feature the case instantiates, and what other cases share it.
- *"The model's assumptions are doing the work."* → Flag which results survive which assumptions and
  motivate each; show the model buys a non-obvious comparative static.
- *"Mechanism is asserted, not observable."* → Translate it into observable implications (and a
  disconfirming pattern) that `bjps-research-design` can test.

## Calibration anchors (hedged)

- BJPS rewards a **portable** argument: the test is whether a comparativist studying a different country,
  or a scholar in another subfield, could carry the mechanism to their own problem.
- Methodological pluralism extends to theory-building: formal, empirical-mechanistic, interpretive, and
  normative arguments are all welcome, each judged in its own idiom — do not dress one as another.

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — formal-modeling and analysis tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — BJPS scope and contribution expectations
