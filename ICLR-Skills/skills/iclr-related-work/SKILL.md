---
name: iclr-related-work
description: Use when positioning an ICLR paper against prior work, concurrent OpenReview submissions, arXiv papers, benchmark lineages, and adjacent learning-representation claims. Use when a reviewer cites a paper you missed, when a public comment disputes your novelty, or when separating "shares a component with" from "solves the same representation-learning problem" so the claim survives permanent public scrutiny.
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

## Surviving the public comparison

ICLR reviewers and even community members can post a "this is just X" comment that stays online next
to your paper forever. The defense is a precise difference axis, decided before submission.

| "Just like X" objection | Robust ICLR response | Fragile response |
| --- | --- | --- |
| Same architecture | Different objective and what it changes representationally | "Ours is bigger" |
| Same benchmark | Different question the benchmark now answers | Higher number only |
| Concurrent arXiv preprint | Dated, scoped distinction, cited generously | Ignoring it and hoping |
| Reuses a known loss | The new analysis or regime where it behaves differently | Renaming the loss |

## Worked vignette

A submission proposes a masked-prediction objective for time-series transformers. A reviewer links a
recent arXiv paper with a similar mask. Rather than dispute priority, the authors add a paragraph:
the prior work masks contiguous spans for forecasting, while this paper masks frequency components
and shows the representation transfers across sampling rates, supported by a transfer ablation. The
difference axis is "what is masked and which invariance it buys," not "we got there first."

## Reviewer-pushback patterns

- "You missed paper Y." Add it, state the axis of difference in one sentence, never dismiss it.
- "Dismissive of prior work." Public threads amplify rudeness; describe prior work in its own terms.
- "Cherry-picked baselines." Compare against the widely used open-source system, not the convenient one.

## Output format

```text
[Closest work] <paper/system/benchmark>
[Difference axis] problem / assumption / method / evidence / scale / theory / artifact
[Must-cite items] <recent OpenReview/arXiv/ICLR-adjacent work>
[Novelty risk] low / medium / high
[Revision text] <concise related-work paragraph or bullet>
```

