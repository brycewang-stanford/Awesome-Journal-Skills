---
name: icml-review-process
description: Use when explaining or diagnosing the ICML review process, including OpenReview, reciprocal reviewing, reviewer/AC behavior, review dimensions, author response, one-round discussion, LLM-review policy, ethics flags, and public review records.
---

# ICML Review Process

Use this to reason about how ICML reviewers and ACs will process a submission. The point is not to
forecast acceptance by score folklore; it is to identify the decision issue and response strategy.

## Process features

- ICML uses OpenReview with double-blind review.
- ICML 2026 aims for about three reviews per paper, though the number can vary.
- Reviewers consider soundness, originality, significance, clarity, and whether rebuttal resolved
  their main concerns.
- Authors get a response period and then one additional reviewer-author discussion round.
- Reviewers and ACs may discuss privately; ACs synthesize conflicts and unresolved concerns.
- Reviews and author-reviewer discussion for accepted papers are made public.
- ICML 2026 uses a Policy A / Policy B framework for reviewer LLM use, with authors indicating
  whether their paper requires Policy A review.
- Reciprocal reviewing links author behavior to reviewer obligations and policy compliance.

## Diagnosis workflow

1. Categorize each likely criticism by soundness, originality, significance, clarity, ethics,
   reproducibility, or policy.
2. Identify which criticism an AC can quote in a meta-review.
3. Separate fixable clarity issues from missing evidence.
4. Prepare response text that helps reviewers update their final justification.
5. Check whether LLM-review policy, prompt injection, reciprocal reviewing, or ethics concerns could
   become procedural rejection risks.

## Score-dimension to AC-leverage map

ICML ACs synthesize conflicts into a meta-review, so the useful question is which dimension an AC can
defend a decision on.

| Dimension | What a reviewer cites | What an AC can act on |
| --- | --- | --- |
| Soundness | Broken proof, untuned baseline, leakage | Strong reject anchor; hard to rebut without new evidence |
| Originality | Overlap with prior or concurrent work | Reject anchor unless delta is reframed |
| Significance | Narrow gain, no mechanism | Borderline; rebuttal can reframe scope |
| Clarity | Buried contribution, dense columns | Often fixable; weakest reject basis alone |

## Worked vignette: reading a split panel

The optimizer paper draws one champion citing the convergence theorem, one skeptic citing an
untuned Adam baseline, and one borderline reviewer citing clarity. The AC-quotable issue is the
baseline soundness concern, not clarity, so the response strategy concentrates the single discussion
round on the tuned-baseline table. Because accepted reviews and discussion become public, the authors
keep the tone measured. If the paper also flagged Policy A LLM-review handling, confirm that choice is
consistent so it does not surface as a procedural risk. Verify the per-paper review count and policy
labels against the current cycle rather than assuming the prior year's setup.

## Output format

```text
[Likely review pattern] supportive / split / skeptical
[AC decision issue] <one issue>
[Procedural risks] <LLM policy / reciprocal reviewer / ethics / anonymity / none>
[Response posture] clarify / add small result / concede / reroute
[Public-record concern] <what will be visible if accepted>
```

