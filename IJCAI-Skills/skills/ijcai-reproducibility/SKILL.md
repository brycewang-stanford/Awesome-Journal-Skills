---
name: ijcai-reproducibility
description: Use when strengthening IJCAI or IJCAI-ECAI reproducibility evidence for theory, algorithms, datasets, and computational experiments under the official convincing/credible/irreproducible reviewer rubric and optional reproducibility-section guidance.
---

# IJCAI Reproducibility

Use this before submission and again before camera-ready. Reopen the current reproducibility
page; IJCAI's rubric and checklist can change.

## Evidence map

- Target at least a credible reproducibility rating for every major result; aim for
  convincing when resources can be shared safely.
- For new algorithms, include a conceptual outline or pseudocode in the paper.
- For theory, state assumptions, formal claims, citations to tools, proof sketches, and
  proofs for novel claims.
- For datasets, cite existing sources, describe unavailable or proprietary datasets, and
  include or promise release of new datasets only when legally possible.
- For computational experiments, report final hyperparameters, search ranges, selection
  criteria, seeds or repeat strategy, software versions, compute infrastructure, and runtime.
- Add an optional "Reproducibility" section when it resolves likely reviewer doubts, but do
  not depend on supplementary material for central claims.

## Rubric mapping by contribution shape

IJCAI's rating moves from irreproducible to credible to convincing. Because the PC spans
symbolic, search, planning, KR, multi-agent, and learning work, the evidence that earns
"convincing" differs by contribution. Map each result to the right column before drafting.

| Contribution | Minimum for "credible" | What lifts it to "convincing" |
| --- | --- | --- |
| New algorithm (search/planning/CSP) | Pseudocode plus complexity claim in body | Runnable code, instance generator, seeds, version pins |
| Theoretical result | Assumptions and proof sketch in body | Full appendix proofs, citations to formal tools |
| Multi-agent / game-theoretic | Protocol, agent counts, payoffs | Released simulator, opponent policies, seeds |
| Dataset contribution | Source, licensing, collection described | Public release or controlled-access path, datasheet |
| Learning experiment | Hyperparameters and splits in body | Code, environment file, compute, repeat strategy |

## Worked vignette: a multi-agent coordination paper

A coordination-protocol paper claims faster convergence but reports no seeds and ships no
simulator. To reach "convincing": state the agent count sweep and payoff matrix in the body;
appendix the convergence proof sketch; release an anonymized simulator with fixed seeds and the
opponent policies; pin library versions. Without the simulator the result stays "credible" at
best, which an IJCAI reviewer may flag as a significance discount.

## Reviewer pushback and the venue-specific fix

- "Cannot tell if the proof holds." Put assumptions and a sketch in the body and full proofs in
  the Technical Appendix; do not bury the theorem statement.
- "No way to regenerate the instances." Ship a deterministic generator and seeds, not just
  result tables, since IJCAI search/planning reviewers re-run when skeptical.
- "Dataset is unavailable." Explain the legal barrier and give enough detail for in-principle
  reproduction; never imply a release you cannot deliver by camera-ready.
- "Reproducibility rests on the appendix." Pull the load-bearing protocol into the 7-page body
  because reviewers are not required to open the supplement.

## Output format

```text
[Result inventory] <claim -> evidence location>
[Rubric target] convincing / credible / currently weak
[Missing details] <algorithm/theory/data/compute/hyperparameters/seeds>
[Paper fixes] <must be in main PDF>
[Supplement fixes] <optional or supporting evidence>
```
