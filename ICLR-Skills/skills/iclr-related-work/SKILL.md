---
name: iclr-related-work
description: Use when positioning an ICLR paper against prior work, concurrent OpenReview submissions, arXiv papers, benchmark lineages, and adjacent learning-representation claims.
---

# ICLR Related Work

Use this to make the novelty claim robust under ICLR review. ICLR reviewers often know recent
OpenReview, arXiv, and workshop work, so the related-work strategy must survive public comparison.

## Positioning checks

- Identify the closest prior method, theory result, dataset, benchmark, or analysis paper.
- Separate "uses a similar component" from "solves the same scientific problem."
- Track concurrent arXiv/OpenReview work and discuss it when a reasonable reviewer would expect it.
- Compare against strong open-source and widely used baselines, not only papers that are convenient.
- Explain differences in assumptions, data access, compute budget, evaluation metric, and failure
  mode.
- Avoid dismissive language; public discussion can amplify careless related-work claims.

## Novelty statement

Build the novelty claim as:

```text
Prior work can <capability under stated conditions>.
It does not <specific missing capability or explanation>.
This paper shows <new mechanism/result/evidence>, under <scope>.
The claim is supported by <theory/experiment/artifact>.
```

## Output format

```text
[Closest work] <paper/system/benchmark>
[Difference axis] problem / assumption / method / evidence / scale / theory / artifact
[Must-cite items] <recent OpenReview/arXiv/ICLR-adjacent work>
[Novelty risk] low / medium / high
[Revision text] <concise related-work paragraph or bullet>
```

