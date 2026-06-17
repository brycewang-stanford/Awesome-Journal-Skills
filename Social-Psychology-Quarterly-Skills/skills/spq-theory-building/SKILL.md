---
name: spq-theory-building
description: Use when building the theoretical argument of a Social Psychology Quarterly (SPQ) manuscript into a contribution to sociological social psychology — whether the work is in the symbolic-interaction, social-structure-and-personality, group-processes, identity, or affect tradition. SPQ rewards an explicit social-psychological mechanism linking structure to the individual, not a bare finding. Structures the argument; it does not run analyses.
---

# Theory & Argument Building (spq-theory-building)

At SPQ a result is not a contribution until it is attached to a **social-psychological mechanism** that
connects social structure or process to the individual — the self, identity, emotion, cognition, or
interaction. This skill turns findings into theory in the idiom of your tradition: explicit mechanisms,
scope conditions, and observable implications.

## When to trigger

- The empirics are strong but the "so what / why" is thin or purely descriptive
- A reviewer said the paper is "atheoretical," "ad hoc," or "not really social-psychological"
- You need to state the mechanism linking structure and the individual explicitly
- You are formalizing within a program (expectation states, affect control, identity verification)

## Build the argument (by tradition)

### Social structure and personality / group processes (mechanism-driven)
1. **Concept** — define the social-psychological constructs precisely (status, identity salience,
   mastery, sentiment, legitimacy); distinguish from neighbors.
2. **Mechanism** — the social process: how structural position or interaction produces the individual
   outcome (e.g., status → expectations → influence; structural strain → mastery → distress).
3. **Observable implications** — what we should see if the mechanism operates (and what we should *not*
   see). These become the tests in `spq-research-design`.
4. **Scope conditions** — the settings, populations, and structural contexts where the argument holds.

### Symbolic-interaction / interpretive
- Make the **conceptual stakes** explicit: what about the self, meaning, or the interaction order does
  this illuminate?
- Build the argument through **observed interaction and accounts**, not hypothesis tests, but still state
  the analytic claim and what evidence would challenge it.
- Show what the argument lets the field **see** about identity work, framing, or emotion management.

### Formal programs (expectation states, affect control, identity control)
- State the **substantive puzzle** before the formal setup; keep assumptions transparent and motivated.
- Derive predictions (comparative statics, equilibrium sentiments/expectations) a reader can test.
- Say what the model **buys**: a non-obvious prediction or a resolution of a puzzle in the program.

## The "structure–individual" test (SPQ-specific)

Ask: *Does the argument explain how something social (structure, position, interaction) connects to
something individual (self, emotion, cognition, behavior)?* If it only explains an individual process
with no social anchor, it drifts toward psychology; if only macro patterns with no individual mechanism,
toward macro sociology. Tighten until the link is the contribution (or reframe via `spq-topic-selection`).

## Mechanism ladder

Write the core argument as a ladder, not a topic list:

| Step | Question | Manuscript evidence |
| --- | --- | --- |
| Social condition | What position, interaction, institution, or group process starts the chain? | Setting, measure, field episode, or formal assumption |
| Perception / meaning | How is the condition interpreted by actors? | Accounts, measures, manipulation, or model parameter |
| Self / emotion / cognition | What individual-level social-psychological process changes? | Construct definition and observable indicator |
| Behavior / interaction | What consequence follows, and for whom? | Test, qualitative pattern, or derived prediction |
| Boundary | Where should the mechanism weaken or reverse? | Scope condition, null case, or contrast |

Use the ladder to decide what belongs in the theory section. A paragraph that cannot be placed on the ladder is probably background, not argument. A ladder with no boundary step will read as overgeneralized.

## Anti-patterns

- A finding with no named mechanism ("X correlates with Y")
- "Hypothesizing after results are known" (HARKing) — state theory before tests; preregister where it fits
- An individual-cognition mechanism with no social structure or interaction in it
- A macro claim with no individual-level social-psychological process
- Universal claims with no scope conditions
- Theory sections that list literatures but never state the mechanism sequence

## Output format

```
【Core claim】one sentence
【Tradition】symbolic interaction / SSP / group processes / identity / affect
【Mechanism】how structure/interaction connects to the individual
【Mechanism ladder】condition → meaning → individual process → behavior → boundary
【Observable implications】testable consequences → research-design
【Scope conditions】settings / populations where it holds
【Structure–individual link explicit?】[Y/N]
【Next】spq-research-design
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — formal-modeling and measurement tooling (affect control, SEM)
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — SPQ scope and contribution expectations
