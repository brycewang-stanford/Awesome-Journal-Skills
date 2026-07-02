---
name: apsr-theory-building
description: Use when building the theoretical argument of an American Political Science Review (APSR) manuscript into a discipline-level contribution — whether the work is formal/game-theoretic, empirical with explicit mechanisms, interpretive, or normative. APSR rewards a clear, portable argument over a bare finding. Structures the argument; it does not run analyses.
---

# Theory & Argument Building (apsr-theory-building)

At APSR a result is not a contribution until it is attached to an **argument the discipline can use
elsewhere.** This skill turns findings into theory: explicit mechanisms, scope conditions, and
observable implications, in the idiom appropriate to your kind of work.

## When to trigger

- The empirics are strong but the "so what / why" is thin
- A reviewer said the paper is "atheoretical," "ad hoc," or "just a finding"
- You need to state mechanisms, assumptions, and scope conditions explicitly
- Formal modeling: deciding what to model, what to assume, and what the model buys you

## Build the argument (by mode of work)

### Empirical paper with a theory
1. **Concept** — define the key constructs precisely; distinguish from neighbors.
2. **Mechanism** — the causal story: who does what, why, under what incentives/constraints.
3. **Observable implications** — what we should see if the mechanism operates (and what we should
   *not* see). These become the tests in `apsr-research-design`.
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

## The "portability" test (APSR-specific)

Ask: *Could a scholar in another subfield import this mechanism/concept to their own problem?* If yes,
you have a discipline-level contribution. If the argument only works for your exact case, tighten it
into a general logic or reframe (back to `apsr-topic-selection`).

## The contribution paragraph, anatomized

APSR papers earn the flagship slot with one of a few recognizable contribution shapes. Decide which
yours is and say so in the paragraph that closes the introduction:

1. **A new concept** — a distinction the field lacked, defined against its nearest neighbors, with
   criteria for recognizing instances. The test: can two coders apply it to new cases and agree?
2. **A new mechanism** — a causal pathway that existing accounts skip, with the actors, incentives,
   and observable traces spelled out.
3. **A unification** — two literatures that talk past each other shown to be special cases of one
   logic. Name both literatures and state what the shared logic predicts that neither did alone.
4. **A revision** — received wisdom shown wrong or bounded. State the received claim fairly, the
   condition under which it fails, and what replaces it there.

### Before → after: from finding to argument

- *Before:* "We find that decentralization reduces clientelism in our sample."
  *After:* "Decentralization reduces clientelism only where local media can price broker services —
  a scope condition that explains why prior studies split, and that any theory tying institutional
  reform to accountability must now carry."

## Decoding the "atheoretical" referee report

When an APSR reviewer writes "atheoretical," "ad hoc," or "under-theorized," it usually means one of
three repairable gaps — diagnose before rewriting everything:

- **Mechanism gap** — the paper shows *that*, never *why*. Repair: add the actor-level story and one
  test that would fail if the story were wrong.
- **Stakes gap** — the theory exists but stays inside the case. Repair: run the portability test
  above and rewrite the contribution paragraph around who else can use the logic.
- **Derivation gap** — hypotheses appear from nowhere. Repair: show each hypothesis falling out of
  the mechanism, and flag any that are exploratory rather than derived (preregistration makes this
  distinction legible — see `apsr-transparency-and-data-policy`).

## Anti-patterns

- "Hypothesizing after results are known" (HARKing) — state theory before tests; preregister where possible
- A model with opaque assumptions chosen to produce the desired result
- Mechanisms named but never made observable
- Universal claims with no scope conditions
- Burying the argument under the empirics — the contribution paragraph must state it plainly

## Output format

```
【Core claim】one sentence
【Mechanism】the causal/logical story
【Assumptions】(formal) the load-bearing ones
【Observable implications】testable consequences → research-design
【Scope conditions】where it holds / fails
【Portability】who else can use this argument
【Next】apsr-research-design
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — formal-modeling and analysis tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — APSR scope and contribution expectations
