---
name: icml-review-process
description: Use when explaining or diagnosing the ICML review process, including OpenReview, reciprocal reviewing, reviewer/AC behavior, review dimensions, author response, one-round discussion, LLM-review policy, ethics flags, and public review records.
---

# ICML Review Process

Use this to reason about how ICML reviewers and ACs will process a submission. The point is not to
forecast acceptance by score folklore; it is to identify the decision issue and response strategy.

## Process features

- ICML uses OpenReview with double-blind review.
- ICML 2027 adds a two-stage process: the area chair decides whether a paper proceeds to full
  review, a senior area chair must confirm any first-stage rejection, and first-stage rejections
  arrive by February 23, 2027. Papers in doubt go to full review, so the first page and abstract
  have to make the contribution legible to one AC.
- Authors pick one of seven contribution types (General, Theory, Application-driven, Concept and
  Feasibility, Negative Results, Datasets/Evaluations/Benchmarks, Position Papers); reviewers judge
  the paper against that type's standard, not one they prefer.
- Main-track reviewers score soundness, presentation, significance, and originality (1-4), plus an
  overall recommendation (1-6) and confidence, and must consider whether the discussion resolved
  their main concerns. The per-paper review count is not stated for 2027.
- Authors get three discussion rounds (rebuttal, reviewer follow-up, author follow-up), each capped
  at 5,000 characters.
- Reviewers and ACs may discuss privately; ACs synthesize conflicts and unresolved concerns.
- Reviews and author-reviewer discussion for accepted papers are made public.
- ICML 2027 applies Policy B (privacy-compliant LLM assistance only, no LLM-written judgment) to all
  reviewing; the 2026 author-selected Policy A option is not offered.
- Reciprocal reviewing links author behavior to reviewer obligations and policy compliance: a
  reciprocal reviewer's missing or very low-quality reviews can get the submission desk-rejected.

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
baseline soundness concern, not clarity, so the response strategy puts the tuned-baseline table in the
first 5,000-character rebuttal and saves the follow-up rounds for the skeptic's reply. Because accepted
reviews and discussion become public, the authors keep the tone measured. Verify the per-paper review
count, round limits, and LLM-review policy against the current cycle rather than assuming the prior
year's setup.

## Output format

```text
[Likely review pattern] supportive / split / skeptical
[AC decision issue] <one issue>
[Procedural risks] <LLM policy / reciprocal reviewer / ethics / anonymity / none>
[Response posture] clarify / add small result / concede / reroute
[Public-record concern] <what will be visible if accepted>
```

