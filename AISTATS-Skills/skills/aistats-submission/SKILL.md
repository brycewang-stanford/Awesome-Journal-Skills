---
name: aistats-submission
description: Use when auditing an AISTATS submission for OpenReview readiness, abstract/full-paper deadlines, the 8-page submission body, double-blind anonymity, supplementary material, reproducibility checklist, dual-submission policy, reviewer volunteer requirements, desk-reject triggers, and final-week submission sequencing.
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

## Desk-reject and triage table

| Trigger | Severity at AISTATS | Repair window |
|---|---|---|
| Overlength main text | Desk reject | None after the deadline |
| Style-file tampering | Desk reject or chair flag | None |
| Identity leak in PDF or supplement | Desk reject | None |
| Checklist contradicting the paper | Review-stage damage | Only before the deadline |
| Theorem assumptions absent from the body | Review-stage damage | Fixable in the writing pass |

## Final-week sequence for a theory-plus-experiments paper

1. Freeze theorem statements and renumber assumptions; reviewers cross-reference labels.
2. Regenerate every figure from seeded scripts so supplement and PDF cannot diverge.
3. Fill the checklist against what the paper actually contains, not what is planned.
4. Strip PDF metadata, notebook authorship fields, and repository owner strings.
5. Confirm the OpenReview abstract matches the PDF abstract word for word.

## Format anchors

- AISTATS uses a two-column PMLR-style layout; display equations and algorithm blocks that
  fit a one-column draft routinely overflow, so compress math early rather than on deadline
  night.
- The page counts cited above describe the 2026 cycle; treat every number as provisional and
  recheck the current Call for Papers before relying on it.

## Output format

```text
[AISTATS readiness] Ready / Needs fixes / Not ready
[Blocking checks] <OpenReview/page/anonymity/supplement/reproducibility/dual-submission>
[Statistical-evidence risk] <one issue>
[Desk-reject risk] <one issue>
[Fix order] <ordered fixes before submission>
```
