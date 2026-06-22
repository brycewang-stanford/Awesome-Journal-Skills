---
name: ajs-submission
description: Use when running the final pre-submission preflight for the American Journal of Sociology (AJS) via Editorial Manager — the $30 submission fee (waived for sole-author grad students), the separate cover page for double-blind review, the ~150-word abstract, mandatory figure alt text, AJS house style, and the originality statement. Final checks; it does not draft content.
---

# Submission Preflight (ajs-submission)

The last check before pressing submit on **Editorial Manager** (`editorialmanager.com/ucp-ajs`). AJS
is **double-blind**, so the most common avoidable failures are an under-anonymized manuscript and a
cover page left inside the manuscript file. Also unique to AJS: a **$30 submission fee** and **AJS's
own house style** (not the ASA Style Guide). Verify volatile items on the live pages before submission.

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure which files/metadata Editorial Manager expects
- Confirming the fee, anonymization, abstract, alt text, and house style are all handled

## Process facts (verify volatile items on the official page)

- **Owner / publisher:** University of Chicago (Dept. of Sociology) / **University of Chicago Press**
  (NOT SAGE/ASA).
- **Portal:** **Editorial Manager** (`editorialmanager.com/ucp-ajs`); accepts **Word, PDF, or LaTeX**.
- **Review model:** **double-blind** — anonymize the manuscript; submit the **cover page as a separate
  file** so personal information is not in the manuscript. Reviewer and author identities are not
  disclosed to the other side, and **AJS avoids sending papers to people in the submitting author's
  network**.
- **Desk-reject / "preject" filter:** before peer review, AJS **prejects** some papers — those **not in
  dialogue with current sociology**, **opinion pieces**, or **current-event interpretations without
  original sociological research**. Make the manuscript's dialogue with current sociology explicit.
- **Editorship structure:** the article side has **three levels of editorship**; the editorial board is
  the **faculty of the University of Chicago Department of Sociology**; first-submission reviewer
  assignment is handled by a **Manuscript Assignment Board of Assistant Editors supervised by
  graduate-student Associate Editors** who study the blinded manuscript to set substantive area/method.
- **Submission fee:** **$30** per new submission; **waived for graduate students submitting as sole
  authors** (proof of status may be requested). Confirm the current amount and waiver workflow on the
  official page.
- **Abstract:** **~150 words** (as close to 150 as possible); must state the question/puzzle, identify
  the data, and indicate findings. **No abstract → not sent to reviewers.**
- **Length:** **no fixed word cap**; be concise (referees may need more time over ~18,000 words).
  Live-check current guidance before upload.
- **Style:** **AJS's own author-date house style** (name + year; "et al." for 3+); **NOT the ASA Style
  Guide**. Notes start at "1"; acknowledgment note on the cover sheet with an asterisk; footnotes or
  endnotes both fine.
- **Figures:** **alt text required for every figure** at submission, with the captions.
- **Format:** serif typeface ≥11 pt (preferably 12), double-spaced, ≥1-inch margins.

## Preflight checklist

### Fee & files
- [ ] $30 submission fee ready (or sole-author grad-student waiver + proof of status)
- [ ] Manuscript file (Word/PDF/LaTeX) **with no cover page inside it**
- [ ] **Separate cover page** file (names, affiliations, acknowledgments)

### Anonymity (double-blind)
- [ ] No author names, affiliations, or acknowledgments in the manuscript
- [ ] Self-references worded to avoid specific attribution
- [ ] Identifying **file metadata stripped** (document properties, comments)

### Content & format
- [ ] Abstract present, ~150 words, states question + data + findings
- [ ] AJS house-style citations/notes/references (NOT ASA Style Guide)
- [ ] Serif ≥11 pt, double-spaced, ≥1-in margins
- [ ] Post-text sections in order: notes, references, tables, figures, appendices
- [ ] Alt text for every figure, with captions
- [ ] Originality statement prepared if the paper overlaps prior work
- [ ] Not under review elsewhere (concurrent submission violates Press ethics)

## Avoidable-failure triage (what bounces a submission, and the fix)

Recurring pre-review failures specific to AJS's portal and double-blind model. Confirm volatile specifics against the journal's current submission guidelines.

| Failure at submission | Fix before upload |
|-----------------------|-------------------|
| Cover page or identifying metadata left in the file | separate cover page; strip document properties and tracked comments |
| Formatted to ASA Style Guide | convert to AJS author-date house style |
| No abstract | add ~150 words: question + data + findings |
| Fee unpaid / wrong waiver assumption | pay $30, or claim sole-author grad waiver only if eligible |
| Prejected pre-review (opinion piece, current-event take, or no dialogue with current sociology) | frame original sociological research in explicit dialogue with current literature |

## Calibration (AJS-specific posture, hedged)

Reflects AJS's house and culture, not universal rules; confirm wording against the journal's current submission guidelines. The most common avoidable style failure is mis-applying the ASA Style Guide — AJS uses its own author-date system. Length is tolerated, not rewarded: no fixed word cap, but referees may need more time over an illustrative ~18,000 words. The $30 fee is waived only for graduate students submitting as sole authors; a coauthored paper does not qualify. Illustrative: a sole-author candidate's 17,500-word article catches three triage issues — an acknowledgments footnote naming the committee, references in ASA style from a prior ASR attempt, and two figures lacking alt text — and after fixes the waiver applies and the submission clears pre-review checks.

## Anti-patterns

- Leaving the cover page / author identifiers inside the manuscript file (breaks double-blind)
- Formatting to the **ASA Style Guide** instead of AJS house style
- Forgetting the **$30 fee** (or wrongly assuming the grad-student waiver applies to coauthored papers)
- Submitting with no abstract (it will not be sent to reviewers) or missing figure alt text
- Submitting while the paper is under review at another journal

## Output format

```
【Fee】$30 paid or sole-author grad waiver (+proof)? [Y/N]
【Files】manuscript clean of cover page + separate cover page file? [Y/N]
【Anonymized】text + self-refs + file metadata clean? [Y/N]
【Abstract】~150 words, states question/data/findings? [Y/N]
【House style】AJS author-date (NOT ASA Style Guide)? [Y/N]
【Alt text】every figure? [Y/N]
【Originality / ethics】statement if needed + not under review elsewhere? [Y/N]
【Next】await decision → ajs-rebuttal on R&R
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reference managers, anonymization, portal summary
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — AJS fee, abstract, house style, alt-text, and ethics policy
