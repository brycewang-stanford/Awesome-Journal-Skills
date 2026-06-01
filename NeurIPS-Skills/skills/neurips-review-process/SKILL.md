---
name: neurips-review-process
description: Use when explaining or diagnosing the NeurIPS main-track review process, including OpenReview, reviewer and AC roles, contribution-type review, ethics flags, reciprocal reviewing, discussion, and LLM-review policy.
---

# NeurIPS Review Process

Use this skill to reason about what reviewers and ACs are likely to do with a submission. Do not use
it to infer acceptance odds from folklore; use it to identify decision-relevant weaknesses.

## Process model

- Reviews happen in OpenReview under double blind.
- Reviewers are asked to evaluate quality, clarity, significance, and the submission's declared
  contribution type.
- ACs coordinate reviewers, handle conflicts and quality issues, write or supervise meta-reviews,
  and make recommendations.
- Ethics concerns can be flagged and routed to ethics reviewers; severe cases can affect decisions.
- Authors who are also reviewers or ACs face reciprocal-reviewing obligations; gross negligence can
  create sanctions affecting their own submissions.

## Reviewer mental model

Reviewers are overloaded cross-area specialists. They need to see:

- what the contribution is;
- why it is new relative to close NeurIPS/ICML/ICLR/ACL/CVPR/KDD-style work;
- whether the evidence supports the exact claim;
- whether limitations, safety, data, and reproducibility are handled responsibly;
- whether the paper can be trusted as a scientific artifact.

## Diagnosis workflow

1. Map each likely review concern to quality, clarity, significance, ethics, reproducibility, or fit.
2. Predict which concerns the AC can use in a meta-review.
3. Decide whether the problem is fixable by clarification, extra analysis, better framing, or
   re-routing.
4. For author response, prioritize issues that change decision logic rather than issues that only
   improve tone.

## Output format

```text
[Likely review split] enthusiastic / borderline / skeptical
[AC-level issue] <one issue most likely to drive the meta-review>
[Ethics/reproducibility flags] <none or list>
[Response strategy] clarify / concede / add small result / reroute
```

