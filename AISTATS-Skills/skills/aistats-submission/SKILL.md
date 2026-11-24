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
- Verify OpenReview profiles, conflicts, subject areas, title, abstract, and author list
  before the abstract deadline. In AISTATS 2027 the author list froze at the abstract
  deadline (no additions or removals, even at camera-ready), every submission had to
  nominate one author as a reciprocal reviewer, and no author could appear on more than 12
  submissions (3 for authors without an accepted ICLR/ICML/NeurIPS/AISTATS paper).
- Apply the current style file without spacing, margin, font, or bibliography hacks.
  AISTATS 2027 allows 8 pages of main text at submission (9 at camera-ready), excluding
  references, the AI Use Statement, the reproducibility checklist, and appendices;
  over-length main text is desk-rejected.
- Include the AI Use Statement. AISTATS 2027 desk-rejects any submission without an "AI Use
  Statement" section placed before the references; if no generative AI was used, say so.
- Submit supplementary material with the full paper. AISTATS 2027 has no separate
  supplement deadline (2026 had one a week later): append it to the PDF or upload one PDF
  or ZIP by the full-paper deadline, anonymized.
- Complete the reproducibility checklist after the references. In AISTATS 2027 omitting it
  does not trigger desk rejection, but it is then requested during the author response
  and required for the camera-ready.
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
| Missing AI Use Statement (AISTATS 2027) | Desk reject | None after the deadline |
| Author over the submission quota | Random desk reject of excess papers | Before the full-paper deadline |
| No reciprocal-reviewer nomination | Desk reject possible | Before the full-paper deadline |
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
- The page counts and rules cited above describe the AISTATS 2027 cycle (checked
  2026-11-23); treat every number as provisional and recheck the current Call for Papers
  before relying on it.
- Citations may be author–year or numeric at submission if used consistently; the
  camera-ready must use author–year (AISTATS 2027).

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue aistats-skills   # from a clone of the AJS repository
```

It reports, with a location for each finding:

- this venue's machine-readable limits, review mode and required statements, when the venue has a
  rules block (`--list-venues`);
- citations ↔ references;
- table and figure numbering, cross-references and standard-error notes;
- abstract numbers traced to the tables;
- placeholders and tracked changes.

With the Research Toolkit pack installed, `rt-submission-readiness` runs the same check as stage 0
of the full pre-submission pipeline (scorecard → referee panel → polish → cover letter). Anything
it lists as *not checked* still needs the manual items below.

## Output format

```text
[AISTATS readiness] Ready / Needs fixes / Not ready
[Blocking checks] <OpenReview/page/anonymity/supplement/reproducibility/dual-submission>
[Statistical-evidence risk] <one issue>
[Desk-reject risk] <one issue>
[Fix order] <ordered fixes before submission>
```
