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

## Closest-work decision tree

For each likely "this is just X" comparison, classify the relationship before writing prose.

| Relationship to prior work | Related-work action | Evidence needed |
| --- | --- | --- |
| Same problem, same method family | Treat as a direct baseline, not a citation footnote | head-to-head result, ablation, or theory delta |
| Same component, different objective | Explain the objective and representation change | loss/objective statement plus experiment tied to the claimed change |
| Same benchmark, different question | Explain what the benchmark now tests | metric interpretation, split/regime difference, or stress test |
| Same claim, weaker evidence | Be precise and generous; do not imply priority without proof | dated citation plus the stronger evidence axis |
| Concurrent OpenReview/arXiv work | Cite and scope it without overclaiming precedence | date, venue/status, and one-sentence distinction |

If the paper cannot name the closest work and the difference axis, mark novelty risk **high** and
route to `iclr-experiments` before polishing prose.

## Novelty statement

Build the novelty claim as:

```text
Prior work can <capability under stated conditions>.
It does not <specific missing capability or explanation>.
This paper shows <new mechanism/result/evidence>, under <scope>.
The claim is supported by <theory/experiment/artifact>.
```

Add a claim ledger underneath the paragraph:

| Claim in paper | Closest work | Difference axis | Required support | Status |
| --- | --- | --- | --- | --- |
| new capability | paper/system X | problem / assumption / method / evidence / scale / theory / artifact | experiment, proof, artifact, or dataset card | ready / weak / missing |

Any row marked **weak** or **missing** must either be softened in the abstract/introduction or backed
by a new result. Do not leave the strongest novelty claim supported only by wording.

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

## Public-thread response contract

When a reviewer or community comment challenges novelty, respond in a way that improves the permanent
OpenReview record:

1. Acknowledge the cited work in its own terms.
2. State the exact overlap without minimizing it.
3. Name one difference axis and point to the supporting experiment, theorem, or artifact.
4. Commit a manuscript change: citation, paragraph rewrite, added baseline, or softened claim.
5. Avoid priority arguments unless dates and versions are documented.

Escalate from prose to experiments when the difference axis is empirical. If the response would say
"we believe our method is different" without a supporting result, novelty risk stays **high**.

## Pre-submission audit

- Every strong novelty phrase in the abstract/introduction has a row in the claim ledger.
- Every closest-work row has a baseline, ablation, proof, or artifact pointer.
- Concurrent work is cited when a reasonable ICLR reviewer would know it.
- Related work does not rely on "first", "novel", or "significant" unless the support is explicit.
- The paper can survive a public "this is just X" comment without changing the core claim.

## Output format

```text
[Closest work] <paper/system/benchmark>
[Difference axis] problem / assumption / method / evidence / scale / theory / artifact
[Claim ledger] <claim -> closest work -> support status>
[Must-cite items] <recent OpenReview/arXiv/ICLR-adjacent work>
[Novelty risk] low / medium / high
[Public response] acknowledgement + overlap + difference + manuscript change
[Revision text] <concise related-work paragraph or bullet>
```
