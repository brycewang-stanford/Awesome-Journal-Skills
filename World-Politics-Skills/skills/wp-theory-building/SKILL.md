---
name: wp-theory-building
description: Use when building the theoretical argument of a World Politics manuscript so it travels across cases. World Politics rewards arguments that significantly advance theoretical debates in comparative politics and international relations, with explicit mechanisms and scope conditions that generalize beyond one case. Structures the argument; it does not run analyses.
---

# Theory & Argument Building (wp-theory-building)

At World Politics a finding is not a contribution until it is attached to **theory the field can carry
to other cases.** The journal asks articles to "significantly advance theoretical debates" — so this
skill turns case evidence into a portable argument: explicit mechanisms, scope conditions, and
observable implications that hold across comparative or IR settings.

## When to trigger

- The empirics are strong but the "so what / why it travels" is thin
- A reviewer said the paper is "atheoretical," "ad hoc," or "just a single-case story"
- You need to state mechanisms, assumptions, and scope conditions explicitly
- Formal modeling: deciding what to model for a comparative/IR puzzle

## Build the argument (by mode of work)

### Empirical paper with a theory
1. **Concept** — define the key constructs precisely (regime type, institution, alliance, identity);
   distinguish from neighbors and travel-test the concept across cases (avoid concept stretching).
2. **Mechanism** — the causal story: who does what, under what incentives/constraints, in what
   institutional or international setting.
3. **Observable implications** — what we should see if the mechanism operates across cases (and what we
   should *not* see). These become the tests in `wp-research-design`.
4. **Scope conditions** — where the argument holds and where it does not. Portability ≠ universality;
   say which regimes, regions, or periods it covers.

### Formal / game-theoretic paper
- State the **substantive comparative/IR puzzle** the model addresses before the setup.
- Keep assumptions **transparent and motivated**; flag which results are robust to which assumptions.
- Translate equilibrium predictions into **comparative statics** a reader can test across cases.
- Say what the model **buys**: a non-obvious prediction or a unifying logic for a cross-case pattern.

## The "travels" test (World Politics–specific)

Ask: *Could a scholar studying a different country, region, or international setting import this
mechanism and expect it to bite?* If yes, you have a comparative/IR contribution. If the argument only
works for your exact case, generalize the logic or reframe (back to `wp-topic-selection`). Concept
stretching is the opposite failure — a concept so broad it no longer travels meaningfully.

## Anti-patterns

- "Hypothesizing after results are known" (HARKing) — state theory before tests
- A model with opaque assumptions chosen to produce the desired result
- Mechanisms named but never made observable across cases
- Universal claims with no scope conditions, or concept stretching to force generality
- Burying the argument under the empirics — the contribution must be stated plainly

## Referee-pushback patterns and the venue-specific fix

World Politics rewards arguments that advance theoretical debates, so the sharpest objections are
about generativity and portability.

| Referee objection | The fix this skill drives |
|-------------------|----------------------------|
| "Empirical but not theoretically generative" | Attach the finding to a mechanism the field can carry to other cases; state a non-obvious prediction |
| "Scope conditions unstated" | Name where it holds and where it fails; portability is not universality |

## Worked micro-example (illustrative)

A hypothetical finding — "aid cut, then the incumbent fell" — becomes portable:

```text
Concept:   external-rent dependence (distinct from total revenue)
Mechanism: rents fund the coalition; a cut shrinks side-payments → elite defection
Scope:     holds where rents are fungible and the coalition is narrow
```

The single case is now a case *of* coalition-funding dynamics, which lets the argument travel.
(Confirm contribution expectations against current guidelines.)

## Operating pass for World Politics

Run this as a concrete capability pass. First lock the political mechanism, case scope, evidence warrant, and comparative or international implication; then test whether the manuscript addresses comparative and international politics reviewers who expect a big political question, credible evidence, and theory that travels beyond one case.

- **Primary move:** Return a claim-evidence-risk ledger; every recommendation must point to a manuscript location or missing artifact.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against International Organization for IR institutions/political economy, Journal of Politics for wider political science, Comparative Political Studies for comparative breadth; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Core claim】one sentence
【Mechanism】the causal/logical story and its setting
【Assumptions】(formal) the load-bearing ones
【Observable implications】testable consequences → research-design
【Scope conditions】which cases / regimes / periods it covers
【Travels?】who else (which cases) can use this argument
【Next】wp-research-design
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — formal-modeling and comparative-method tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — scope and contribution expectations
