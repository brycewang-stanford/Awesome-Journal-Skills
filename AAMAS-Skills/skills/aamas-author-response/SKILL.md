---
name: aamas-author-response
description: Use when drafting an AAMAS rebuttal to preliminary OpenReview reviews, covering the double-blind constraint, the no-new-results and no-revised-paper norms, how to answer game-theory, MARL, and systems reviewers at once, and how to give the area chair a clean acceptance rationale within a short response window.
---

# AAMAS Author Response

Use this after AAMAS preliminary reviews are released. Reopen the current OpenReview
instructions and the rebuttal-window rules before drafting; response mechanics are
cycle-specific and AAMAS reviews and decisions become public afterward.

## Triage

- Answer only what can move the decision: correctness of the game model or proofs, the reality
  of the interaction claim, baseline/opponent fairness, reproducibility, and scope.
- Use evidence already in the submission: sections, appendices, the supplement, theorem
  statements, learning curves, and opponent-set definitions. AAMAS rebuttals do not add new
  results and typically do not upload a revised paper.
- Keep the reply anonymous: no institution, no named system, no private URLs or repository
  owners.
- Correct outright factual errors first, then address requests for missing comparisons,
  ablations, equilibrium analysis, or seeds.

## Drafting pattern

1. State the decision-critical correction or concession in the first line.
2. Point to the exact submitted evidence (section, figure, appendix, or theorem number).
3. Explain the strategic or empirical consequence for the reviewer's concern.
4. Promise a camera-ready wording fix only if it adds no unsupported new claim.

## Multi-reviewer pushback patterns

AAMAS pools game theorists, MARL researchers, and systems-minded reviewers on one paper, so a
single rebuttal often answers three different lenses at once.

| Pushback | What it signals | AAMAS-ready fix |
|---|---|---|
| "This is really a single-agent method" | The interaction claim did not land | Point to where the result depends on other agents co-adapting; cite the ablation that freezes them |
| "Which equilibrium do you converge to?" | A game theorist read the solution concept | Name it (Nash / correlated / coarse / no-regret) and cite the proof or convergence plot |
| "Baselines are self-play only" | Opponent set looks weak | Anchor to the held-out opponents or population in the appendix, or concede a camera-ready addition |
| "Seeds and variance are missing" | An empirical reviewer checked rigor | Reference the seeded runs and standard errors; do not promise new experiments as fact |

## Response micro-example

Reviewer objection: the cooperation result may be an artifact of a single random seed. Reply
skeleton:

1. Note that Figure 3 already aggregates 30 seeds with standard errors.
2. Quote the exact aggregate so the reviewer need not re-open the PDF.
3. Point to Appendix C for the per-seed spread and the opponent set used.
4. Offer one camera-ready sentence stating the seed count in the caption.

## Discussion-window calibration

- One decision-critical point per reviewer beats an exhaustive reply; the area chair reads for
  whether the central interaction or correctness objection was actually resolved.
- Never paste a fresh proof or a new game variant into the response box; sketch the argument
  and anchor it in submitted material.
- Reply early - AAMAS rebuttal windows are short and reviewers who engage once rarely return.
- Remember the reviews and your response may become public with the paper; write as if they
  will.

## Output format

```text
[Priority issue] <reviewer concern>
[Decision dimension] correctness / interaction-reality / significance / reproducibility / scope
[Draft response] <AAMAS-ready anonymous text>
[Evidence anchor] <section/appendix/figure/theorem>
[Forbidden content removed] <identity leaks, new results, revised-paper promises>
```
