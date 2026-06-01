---
name: aaai-related-work
description: Use when positioning an AAAI paper against archival work, arXiv or workshop contemporaneous papers, AAAI/IJCAI/NeurIPS/ICML/ICLR neighbors, and multiple-submission policy constraints.
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

## Output format

```text
[Closest work] <paper/system/benchmark>
[Difference axis] problem / method / theory / data / evaluation / system / impact
[Must-cite items] <archival and contemporaneous work>
[Multiple-submission risk] none / clarify / withdraw / reroute
[Revision text] <AAAI-ready related-work paragraph>
```

