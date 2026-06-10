---
name: aaai-submission
description: Use when auditing an AAAI main technical track submission for OpenReview readiness, double-blind anonymity, page limits, reproducibility checklist, supplementary material, author limits, multiple-submission policy, and AAAI AI-use policy compliance.
---

# AAAI Submission

Use this for an AAAI main technical track submission audit. Reopen the current conference page,
Author Kit, CFP, submission instructions, review process page, supplementary-material page, and
author policies before giving deadline-ready advice.

## Submission audit

- Confirm the target track: Main Track, AI for Social Impact, AI Alignment, or another AAAI program.
  Track-specific rules can differ.
- Verify OpenReview account/profile readiness, conflicts, author list, subject areas, and submission
  metadata before the abstract and paper deadlines.
- Check the current AAAI author kit. AAAI-26 submissions used AAAI two-column camera-ready style,
  US Letter PDF, and 7 pages of technical content plus pages solely for references and the
  reproducibility checklist.
- Confirm double-blind compliance in the PDF, file names, references to prior work, supplement,
  code/data, and metadata. Omit acknowledgments in the review version.
- Include the reproducibility checklist after references when current instructions require it.
- Enforce the author submission limit and author-change rules. AAAI-26 limited each author to 10
  combined technical-track submissions and did not allow authors to be added after submission.
- Check multiple-submission compliance. An AAAI submission under review cannot simultaneously be
  under review at another archival venue.
- Apply the current AAAI AI-use policy: editing/polishing author-written text may be allowed, but
  LLM-generated manuscript text, AI authorship, and AI-generated citations are policy risks.

## Blocking risks

- Over-limit technical content or malformed PDF.
- Missing reproducibility checklist.
- Identity leakage in paper, supplement, links, code, data, or prior-work citations.
- Author added after the allowed window.
- Concurrent archival submission.
- Web pointers to mutable supplementary material.
- Policy-violating LLM-generated text, hallucinated references, or plagiarism.

## Summary-reject screen

AAAI's large reviewer pool and high volume mean a desk-level or Phase-1 cut is the most likely way to
lose, so screen for the mechanical failures first.

| Check | Fast-fail trigger | Where it bites |
| --- | --- | --- |
| Page limit | technical content over the cap | desk return |
| Anonymity | author name in PDF, code, or metadata | policy reject |
| Checklist | missing or contradictory | Phase-1 distrust |
| Dual submission | concurrent archival venue | ethics reject |

## Worked vignette

A robotics-learning team has 7 strong technical pages but left an acknowledgments line and a GitHub
URL with their lab name in the supplement. The audit flags anonymity as the highest summary-reject
risk: the fix order is strip the acknowledgment, replace the link with an anonymous archive, scrub
ZIP metadata, then re-export and re-run the anonymity sweep before the paper deadline.

## Output format

```text
[AAAI readiness] Ready / Needs fixes / Not ready
[Track] Main / AI for Social Impact / AI Alignment / other
[Blocking checks] <page/anonymity/checklist/supplement/author-limit/dual-submission/AI-policy>
[Highest summary-reject risk] <one issue>
[Fix order] <ordered fixes before submission>
```

