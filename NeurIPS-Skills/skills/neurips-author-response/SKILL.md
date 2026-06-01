---
name: neurips-author-response
description: Use when drafting or triaging NeurIPS OpenReview author responses, rebuttals, and discussion-period replies under the current year's response mechanics and double-blind constraints.
---

# NeurIPS Author Response

Use this skill after reviews are released. The goal is to clarify, correct misunderstandings, and
move reviewers and ACs toward a technically accurate decision without implying a revised paper has
replaced the submitted version.

## 2026 response mechanics to re-check

The 2026 handbook describes a three-phase response/discussion process: initial author response,
author-reviewer-AC discussion, then reviewer/AC discussion. It also states that authors respond
through OpenReview rebuttal buttons, with a per-review 10,000-character limit, no file uploads, no
identity-revealing content, and no links except an anonymized code link to the AC in an Official
Comment when reviewers ask for code. Reopen the current handbook before using these limits.

## Response triage

- Start from decision leverage, not reviewer score. Identify the few objections that ACs can use to
  justify rejection: correctness, missing baseline, unclear novelty, weak significance, anonymity,
  ethics, or reproducibility.
- Separate misunderstandings from real gaps. Correct the former directly; acknowledge the latter and
  explain what existing evidence in the original submission supports.
- Do not promise a new paper. New results can clarify, but the original submission remains the basis
  for the recommendation.
- Keep every response anonymous and link-free unless the current official policy gives an explicit
  exception.

## Drafting pattern

1. Thank reviewers briefly, then state the central clarification.
2. Answer the highest-leverage technical objection first.
3. Point to exact sections, equations, figures, appendix items, or checklist answers.
4. If adding a small result, state that it supports an existing claim and can be incorporated if
   accepted.
5. Close with the concrete change that would appear in camera-ready, not a broad promise.

## Pitfalls

- Arguing with tone instead of evidence.
- Spending space on low-confidence praise or score complaints.
- Uploading files, posting links, or identifying authors.
- Treating the response as a full revision.
- Ignoring the meta-review, AC questions, or reviewer-author professional obligations.

## Output format

```text
[Response priority] <reviewer/AC issue to address first>
[Decision leverage] High / Medium / Low
[Draft response] <anonymous OpenReview-ready text>
[Evidence cited] <paper section / appendix / checklist item>
[Do not say] <phrases or promises to avoid>
```

