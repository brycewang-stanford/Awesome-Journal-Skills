---
name: games-and-economic-behavior
description: Use when targeting Games and Economic Behavior (GEB) or deciding whether a game-theory manuscript or its application fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Games and Economic Behavior (games-and-economic-behavior)

## Journal positioning

GEB is a leading journal for game theory and its applications, publishing strategic-behavior theory, mechanism and market design, and behavioral and computational game theory. It rewards papers with a genuine game-theoretic contribution — a new model, equilibrium result, mechanism, or analysis of strategic behavior — whether purely theoretical or applied. The readership spans economic theorists, computer scientists, and behavioral researchers who work on strategic interaction, so the strategic/game-theoretic core must be substantive.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Elsevier site and the editorial submission system.

## When to trigger

- The author names GEB as the target venue, or wants a home for a game-theory paper or its application.
- A theory paper's contribution is a strategic model, equilibrium result, or mechanism.
- A behavioral or computational paper needs re-framing so the game-theoretic contribution is foregrounded.
- The author needs GEB's desk-reject risks and a credible theory / mechanism-design alternative list.

## Scope & topic fit

- Game theory: equilibrium concepts, dynamic and repeated games, information and signaling, bargaining.
- Mechanism design and market design: auctions, matching, allocation, and implementation.
- Behavioral game theory: bounded rationality, learning, and experimental tests of strategic models.
- Computational and algorithmic game theory, and applications of game theory across economics and related fields.

## Method & evidence bar

- The game-theoretic contribution is the filter: clearly stated games, correct and complete equilibrium analysis, and results that generalize or illuminate strategic behavior.
- Mechanism/market-design papers need well-posed objectives and properties (incentive compatibility, efficiency, stability) proven, not asserted.
- Behavioral and experimental work must connect cleanly to a game-theoretic prediction and use appropriate design and inference.
- Computational contributions need correctness and a clear strategic/economic payoff, not just an algorithm.

## Structure & house style

- The introduction states the strategic setting, the model, the main result, and its significance early, and explains the game-theoretic contribution.
- Position against the relevant game-theory / mechanism-design literature; relate assumptions and results to prior work explicitly.
- Uses an unstructured abstract and JEL codes; an appendix carries proofs, derivations, and (for experiments) instructions and procedures.
- Propositions and exhibits should be self-contained; the central result (theorem, mechanism property, or treatment effect) should be clearly stated.

## Official-submission checklist

- Search the live site for "Games and Economic Behavior guide for authors / submission guidelines" and follow the current Elsevier version.
- Re-check formatting, abstract/JEL requirements, anonymization, and proof/appendix conventions on the submission system.
- Re-check the current data and code / replication policy for any experimental or computational components.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the game-theoretic contribution and why it generalizes or illuminates strategic behavior.
- [ ] The contribution is stated as a model / equilibrium result / mechanism property, not as statistical significance.
- [ ] The introduction positions the paper against the current game-theory / mechanism-design frontier.
- [ ] Proofs are complete and correct; mechanism properties or experimental tests are rigorous.
- [ ] Appendix, derivations, and any experimental/computational materials are ready for the official policy.

## Common desk-reject triggers

- A theory paper with incomplete proofs, fragile assumptions, or a non-general result.
- A mechanism-design paper that asserts rather than proves its properties.
- A behavioral/experimental paper with no clean game-theoretic prediction or weak design.
- A narrow application with no genuine strategic or game-theoretic contribution.

## Re-routing decision

- General-interest at the top → `american-economic-review`; broad microeconomic theory → `journal-of-economic-theory`.
- Technically rigorous theory/econometrics general venue → `international-economic-review`; broad general field → `european-economic-review`.
- Experiment-centered work where design is the core → `experimental-economics`; IO/regulation applications of game theory → `rand-journal-of-economics`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Games and Economic Behavior
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the game-theoretic contribution clear GEB's bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / JEL / proofs-appendix / experiment materials / data-code>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
