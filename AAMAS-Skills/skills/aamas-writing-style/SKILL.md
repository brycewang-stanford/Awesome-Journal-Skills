---
name: aamas-writing-style
description: Use when revising an AAMAS paper so the interaction contribution leads the first page, the solution concept or incentive property is named, the game and agents are legible, claims are paired with proofs or multiagent experiments, the argument fits eight two-column pages plus references, and the wording stays double-blind.
---

# AAMAS Writing Style

Use this when revising the main paper. AAMAS papers need a compact statement of why an
*interaction* result matters and enough detail for a game theorist and an empiricist to both
validate it.

## Revision rules

- Put the interaction contribution on the first page: the multiagent problem, why single-agent
  or centralized fixes fail, the mechanism or learning rule, the strategic property, and the
  evidence.
- Name the solution concept or incentive property (Nash, correlated, coarse-correlated,
  no-regret, dominant-strategy truthful, Pareto); an unnamed "equilibrium" is a review flag.
- Make the game legible: agents, actions, information structure, and payoffs stated once and
  clearly.
- Pair every major claim with a proof sketch, a self-play or population experiment, or a
  deployment result.
- Use the 8-page body for the core argument and push long proofs, extra opponents, and extended
  ablations to the appendix (references are unlimited, so cite generously).
- Keep double-blind wording in self-citations, prior-system references, acknowledgements, and
  artifact descriptions.

## Interaction-first discipline

- State early why the result is genuinely multiagent - what breaks if the other agents are
  frozen into a static environment. If nothing breaks, the AAMAS framing does not hold.
- Give each theorem a body-level proof sketch; the appendix proof supports the sketch but never
  replaces it.
- Keep the game's information structure visible; who knows what and when is where multiagent
  proofs live or die.
- Separate a *proved* strategic property from an *observed* one; mixing "is truthful" and
  "appears cooperative" in one paragraph is a credibility leak here.

## Sentence-level rewrites

| Draft pattern | AAMAS-safe rewrite |
|---|---|
| "Our agents outperform the baselines..." | "reduce social cost by X (SE Y) over Z seeds against held-out opponents" |
| "The agents reach equilibrium..." | "converge to a coarse-correlated equilibrium (Def. 2) under Assumptions 1-3" |
| "The mechanism is fair and efficient..." | "is dominant-strategy truthful (Thm. 1) with efficiency loss bounded by ... (Thm. 2)" |
| "In a multiagent setting..." | Name the game, the number of agents, and the information structure |

## Vignette: compressing into eight two-column pages

A draft with two theorems, a mechanism, six figures, and a sprawling related-work section: keep
both theorem statements with one sketch each, the mechanism definition, and the two
decision-critical figures (truthfulness-under-learning and the efficiency gap); compress related
work into precise contrasts; move secondary lemmas and four figures to the appendix with forward
references. The test of a good cut: a reviewer reconstructs the whole interaction argument
without opening the supplement.

## Output format

```text
[Writing diagnosis] clear / interaction-buried / concept-unnamed / overloaded
[First-page fix] <new interaction framing>
[Claim discipline] <claim -> proof / experiment / limitation>
[Compression cuts] <move / delete / merge>
[Anonymity edits] <phrases to rewrite>
```
