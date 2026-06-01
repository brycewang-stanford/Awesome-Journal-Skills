---
name: iclr-submission
description: Use when auditing an ICLR main-conference submission for OpenReview readiness, double-blind anonymity, page limits, reciprocal reviewing, LLM-use disclosure, dual-submission policy, supplementary material, and desk-reject risk.
---

# ICLR Submission

Use this for an ICLR main-conference submission audit. Reopen the current CFP, Author Guide,
OpenReview submission form, template, Code of Ethics, Code of Conduct, and LLM policy before giving
deadline-ready advice.

## Submission audit

- Confirm the target is the ICLR main conference, not a workshop, Tiny Paper, blog, affinity event,
  or later publication track.
- Check that all authors have complete OpenReview profiles and that the author list follows the
  current freeze/change windows.
- Verify that the abstract is substantive and non-duplicative before the abstract deadline; do not
  rely on a placeholder.
- Confirm use of the current ICLR LaTeX template and current page-limit rules. In 2026, submissions
  used 9 pages of main text, references outside the limit, and appendices after references.
- Inspect anonymity in the PDF, appendices, supplementary ZIP, code, data, demos, links, repository
  metadata, comments, acknowledgments, and file names.
- Confirm reciprocal-reviewing compliance for the author team unless the current cycle grants an
  explicit exemption.
- Complete any LLM-use disclosure truthfully. Hidden prompt injection, hallucinated citations, or
  undisclosed LLM-written scientific content can become ethics issues.

## Desk-reject and integrity risks

- Late or missing abstract/full paper.
- New author added after the author-list deadline.
- Template manipulation, over-limit main text, or missing required fields.
- Non-anonymous public links, repository ownership, analytics, demo login, or organization slug.
- Dual submission to another archival venue that violates current ICLR policy.
- Unclear LLM disclosure or review-manipulation text.
- Reciprocal-reviewing noncompliance.

## Output format

```text
[ICLR readiness] Ready / Needs fixes / Not ready
[OpenReview state] profiles / abstract / paper / supplement / reviewer nomination
[Blocking risks] <anonymity/page-limit/dual-submission/LLM/reciprocal-reviewing>
[Fix order] <highest-impact fixes before deadline>
[Current-cycle pages to reopen] <CFP, Author Guide, OpenReview group, template, LLM policy>
```

