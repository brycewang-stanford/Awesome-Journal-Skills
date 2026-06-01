---
name: icml-submission
description: Use when auditing an ICML main-track submission for OpenReview, LaTeX formatting, 8-page body, anonymity, supplementary material, impact statement, dual submission, concurrent ICML submissions, reciprocal reviewing, and LLM/prompt-injection policy compliance.
---

# ICML Submission

Use this for a final ICML submission audit. ICML rules are annual; reopen the current CFP, Author
Instructions, OpenReview group, style files, example paper, FAQ, and LLM-review policy before giving
submission-ready advice.

## Submission checks

- Confirm the target is main-track research paper, not position paper, workshop, tutorial, expo, or
  Journal-to-Conference. Position papers use a separate call and OpenReview site.
- Verify OpenReview account readiness for all authors before the relevant deadline. ICML 2026
  freezes the author list after the abstract deadline.
- Check that the PDF uses the current ICML LaTeX style. ICML 2026 provides no support for non-LaTeX
  typesetting.
- Enforce the current main-body limit. The 2026 submission body limit is 8 pages, followed by
  references and appendices in the same PDF.
- Check the PDF file-size limit and all required OpenReview fields.
- Confirm double-blind compliance in the paper, appendices, supplementary manuscripts, code/data
  ZIPs, anonymous repositories, filenames, metadata, acknowledgments, grant numbers, and links.
- Include the impact statement in the required place for main-track papers.

## ICML-specific desk-reject risks

- Main body over the page limit.
- Non-anonymized paper, appendix, code, data, repository, or supplementary manuscript.
- Missing or late abstract/full-paper submission.
- Dual submission to another archival venue at the full-paper deadline.
- Prompt injection or review-manipulation text.
- Template modifications that create unfair space.
- Reciprocal reviewer or LLM-review policy violations tied to the paper.

## Concurrent ICML submissions

Treat related submissions by overlapping author sets as prior work. If a reasonable reviewer would
expect the related paper in the related-work section, cite it anonymously, explain the difference,
and include the anonymized PDF in supplementary material.

## Output format

```text
[Submission readiness] Ready / Needs fixes / Not ready
[Track] Main / position / workshop / other
[Blocking ICML checks] <OpenReview/LaTeX/page limit/anonymity/supplement/impact/dual-submission>
[Concurrent-submission risk] none / cite anonymously / reroute or withdraw
[Highest desk-reject risk] <one issue>
[Fix list] <ordered fixes before submission>
```

