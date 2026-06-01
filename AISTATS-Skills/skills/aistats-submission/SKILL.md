---
name: aistats-submission
description: Use when auditing an AISTATS submission for OpenReview readiness, abstract/full-paper deadlines, 8-page submission body, double-blind anonymity, supplementary material, reproducibility checklist, dual-submission policy, reviewer volunteer requirements, and reviewer-discussion policy.
---

# AISTATS Submission

Use this for an AISTATS paper submission audit. Reopen the current Call for Papers,
OpenReview group, style files, FAQ, and proceedings instructions before giving
deadline-ready advice.

## Submission audit

- Confirm the target is the main AISTATS conference, not a workshop or tutorial.
- Verify OpenReview profiles, conflicts, subject areas, title, abstract, author list, and
  reviewer-volunteer obligations before the abstract and full-paper deadlines.
- Apply the current style file without spacing, margin, font, or bibliography hacks.
  AISTATS 2026 used 8 pages of main text for submission, excluding references and
  appendices.
- Submit supplementary material by the current supplement deadline. In 2026 this was a
  separate deadline after the main paper deadline, and supplementary uploads were optional
  but had to remain anonymous.
- Include or complete the reproducibility checklist if the current cycle requires it.
- Enforce double-blind anonymity in paper text, appendix, supplement, code/data, file names,
  metadata, repository links, acknowledgements, grants, and self-citations.
- Check concurrent-submission rules and prior-publication status. Do not put the same work
  under review at another archival venue when AISTATS forbids it.

## Blocking risks

- Late abstract or full-paper upload.
- Overlength main text or modified style.
- Non-anonymized supplement, metadata, repository, or appendix.
- Missing reproducibility checklist or required OpenReview fields.
- Dual submission to another archival venue.
- Unclear statistical evidence, weak baselines, or missing uncertainty analysis.

## Output format

```text
[AISTATS readiness] Ready / Needs fixes / Not ready
[Blocking checks] <OpenReview/page/anonymity/supplement/reproducibility/dual-submission>
[Statistical-evidence risk] <one issue>
[Desk-reject risk] <one issue>
[Fix order] <ordered fixes before submission>
```
