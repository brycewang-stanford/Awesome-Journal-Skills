---
name: aaai-related-work
description: Use when positioning an AAAI paper's novelty against archival work, contemporaneous arXiv or workshop papers, and AAAI/IJCAI/NeurIPS/ICML/ICLR neighbors across the broad AI scope, while staying inside AAAI's dual-submission and AI-as-source policy constraints and writing a related-work section legible to non-specialist reviewers.
---

# AAAI Related Work

Use this to make the novelty claim robust under AAAI's broad AI review. The related-work section
must help reviewers distinguish the paper from both archival work and contemporaneous non-archival
work.

## Positioning checks

- Identify the closest archival AI papers and current arXiv/workshop work.
- Separate method novelty, task novelty, evaluation novelty, and system integration novelty.
- Cite contemporaneous non-archival work carefully when it affects priority or reviewer
  expectations.
- Do not submit substantially similar work to multiple archival venues at the same time.
- Explain how the paper differs from AAAI/IJCAI/NeurIPS/ICML/ICLR neighbors in assumptions,
  evidence, scope, and contribution.
- Avoid using AI systems as citable scientific sources under AAAI policy.

## Novelty paragraph

Use this structure:

```text
Closest prior work solves <problem> under <assumptions>.
It does not address <specific missing setting/mechanism/evidence>.
This paper contributes <new item> and verifies it through <evidence>.
The claim is limited to <scope>.
```

## Positioning across AAAI's breadth

AAAI spans search, planning, knowledge representation, constraint satisfaction, multi-agent systems,
learning, NLP, vision, and robotics, so the closest prior work may live in a subfield your reviewer
does not. Make the contrast explicit for a non-specialist instead of assuming shared background.

| Neighbor venue | Reviewer expectation | Differentiation to spell out |
| --- | --- | --- |
| IJCAI | broad-AI overlap | what your result adds beyond their framing |
| NeurIPS/ICML | ML method or theory depth | why AAAI breadth, not just a benchmark gain |
| ICLR | representation-learning lens | non-learning mechanism or guarantee you contribute |
| AAAI prior years | incremental-track suspicion | the new assumption, evidence, or scope |

## Reviewer-pushback patterns

- "This looks concurrent with arXiv paper Y." Fix: cite Y, state it is non-archival and contemporaneous,
  and name the specific setting or evidence you add; do not bury or ignore it.
- "Isn't this the same as your workshop paper?" Fix: clarify the archival delta and confirm no
  substantially similar work is under review elsewhere, satisfying the dual-submission rule.
- "Citation looks AI-generated." Fix: verify every reference against a real source; AAAI policy bars
  AI systems as citable scientific sources and hallucinated citations are a credibility risk.

## Worked vignette

A reasoning-over-knowledge-graphs paper sits near both a KR archival line and a recent NeurIPS
embedding paper. Using the axes: against KR work the difference is *evidence* (learned vs. hand-built
rules); against the NeurIPS neighbor it is *scope* (logical soundness, not just link prediction). One
contemporaneous arXiv preprint is cited as non-archival with a one-line delta, and the dual-submission
box is checked clean.

## Output format

```text
[Closest work] <paper/system/benchmark>
[Difference axis] problem / method / theory / data / evaluation / system / impact
[Must-cite items] <archival and contemporaneous work>
[Multiple-submission risk] none / clarify / withdraw / reroute
[Revision text] <AAAI-ready related-work paragraph>
```

