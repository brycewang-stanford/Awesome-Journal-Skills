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

## Desk-reject triage table

ICLR enforcement is strict and the consequences are public: even a withdrawn submission leaves a
visible OpenReview trace. Triage the highest-probability rejections first.

| Risk | Quick test | Fix before deadline |
| --- | --- | --- |
| De-anonymization | Grep PDF and ZIP for names, remotes, buckets | Strip metadata, neutralize links |
| Over-limit main text | Count pages against the current rule | Move material after references |
| Author-list change | Check the freeze window in the CFP | Finalize authors before the cutoff |
| Dual submission | Confirm no archival overlap | Withdraw or rescope the other venue |
| LLM disclosure | Confirm the form field is truthful | Disclose; remove hallucinated citations |

## Worked vignette

A team submits an LLM fine-tuning paper whose anonymized repo link points to a GitHub org naming the
lab, with a caption thanking a named cluster. Both leak identity. The fix: replace the link with an
anonymized supplement ZIP, remove the acknowledgment until camera-ready, re-grep the PDF for the
cluster name, and confirm all authors completed OpenReview profiles before the freeze.

## Reviewer-pushback patterns

- "Looks like a workshop paper." Reframe for the main track or route elsewhere.
- "Possible dual submission." Document why the other version is non-archival under current policy.

## Output format

```text
[ICLR readiness] Ready / Needs fixes / Not ready
[OpenReview state] profiles / abstract / paper / supplement / reviewer nomination
[Blocking risks] <anonymity/page-limit/dual-submission/LLM/reciprocal-reviewing>
[Fix order] <highest-impact fixes before deadline>
[Current-cycle pages to reopen] <CFP, Author Guide, OpenReview group, template, LLM policy>
```

