---
name: aamas-related-work
description: Use when positioning an AAMAS submission against multiagent, game-theory, and reinforcement-learning literature spread across AAMAS, AAAI, IJCAI, NeurIPS, ICML, EC, and JAAMAS, including arXiv and workshop versions, concurrent submissions, prior conference versions, and the cross-community citation coverage AAMAS reviewers expect.
---

# AAMAS Related Work

Use this to audit novelty and eligibility. Reopen the current CFP for dual-submission,
anonymity, and prior-publication rules before advising authors; much of the nearest multiagent
work lives at *other* venues, which shapes both positioning and eligibility.

## Positioning checks

- Separate the interaction novelty from engineering improvement: a new solution concept,
  mechanism, learning-dynamics result, coordination protocol, negotiation strategy, or empirical
  multiagent finding.
- Compare across communities: AAMAS itself, the AI conferences (AAAI, IJCAI), the ML conferences
  (NeurIPS, ICML), and economics-and-computation venues (EC), plus the JAAMAS journal. Many
  landmark multiagent papers are *not* at AAMAS, so a bibliography that only cites AAMAS is as
  suspicious as one that ignores it.
- Treat conference proceedings and journals as archival unless the current rules say otherwise.
- Cite arXiv and workshop versions without breaking double-blind; do not point reviewers to an
  identity-revealing page.
- Explain overlap with any concurrent or prior version, and do not submit duplicate archival
  work.

## Cross-community coverage table

| Literature lane | Typical sources | What AAMAS reviewers check |
|---|---|---|
| Agents / multiagent core | AAMAS, JAAMAS, IJCAI, AAAI agent tracks | Whether the nearest multiagent method is compared or explicitly distinguished |
| Multiagent RL | NeurIPS, ICML, ICLR, prior AAMAS | Whether MADDPG/QMIX/COMA-style cousins are cited even though they are not AAMAS papers |
| Game theory / mechanism design | EC, GEB, algorithmic game-theory venues | Whether the solution concept and known impossibility results are acknowledged |
| Social choice / negotiation | AAMAS, AAAI, COMSOC, ADT | Whether standard axioms and strategyproofness usage are followed |

A bibliography citing only deep-MARL benchmarks tells a game-theory reviewer that known
equilibrium or mechanism results may be getting rediscovered - a recognizable AAMAS reject
pattern no amount of benchmark strength repairs. The mirror failure - only citing classical game
theory while ignoring the deep-MARL wave - loses the empirical reviewer.

## Positioning vignette

Imagine the paper proposes a communication protocol that improves cooperation in a mixed-motive
game. Its nearest neighbors: a NeurIPS MARL paper with emergent communication but no incentive
analysis, an EC paper with a cheap-talk equilibrium but no learning, and a prior AAMAS paper on
the same game with a weaker coordination result. The novelty sentence should name all three:
incentives where the MARL line had none, learning where the game-theory line stayed static, and
stronger coordination than the direct AAMAS predecessor.

## Concurrent-work judgment calls

- Independently concurrent arXiv work: cite neutrally, state the technical difference, and avoid
  priority claims reviewers cannot verify.
- Your own workshop version: usually non-archival and citable, but verify against the current
  CFP and phrase the citation so double-blind survives.
- When unsure about a venue's archival status, declare the overlap in the submission form rather
  than gambling on a chair's reading.

## Output format

```text
[Eligibility] clear / needs declaration / risky
[Closest literatures] <agents / MARL / game-theory / social-choice>
[Nearest 3 works] <work -> distinction>
[Archival-overlap risk] <none / issues>
[Novelty sentence] <AAMAS-ready interaction contrast>
```
