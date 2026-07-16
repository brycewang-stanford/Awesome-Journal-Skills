---
name: lang-submission
description: Use when running the final pre-submission preflight for Language (LSA) via the Cambridge University Press ScholarOne portal — double-anonymous anonymization, the section and word-limit rules (General Research Article ≤18,000 words; Review Article ≤5,000), the abstract, Leipzig glossing, IPA, the Language Style Sheet, figure alt text, and open-access status. Final checks; it does not draft content.
---

# Submission Preflight (lang-submission)

The last check before you press submit on **Cambridge University Press ScholarOne** — the portal for
*Language* since **January 2026**, when the journal moved to CUP and became **fully open access from
Volume 102**. *Language* is **double-anonymous**, so the most common avoidable failures are an
under-anonymized manuscript and self-citations that unmask the author. Also verify the **section and
word limits**, the **Language Style Sheet** citations, and the **Leipzig glossing / IPA** before upload.
Verify all volatile items on the live CUP/LSA author pages immediately before submission.

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure which section, files, or metadata ScholarOne expects
- Confirming anonymization, word count, abstract, glossing, style, and alt text are all handled

## Process facts (verify volatile items on the official page)

- **Publisher / portal:** **Cambridge University Press**; submit via **ScholarOne** (since Jan 2026).
  An **Overleaf template** is available; ScholarOne accepts LaTeX and Word workflows — confirm current
  accepted formats.
- **Access:** **fully open access from Volume 102 (2026)**; check the current APC / waiver and any
  read-and-publish agreement on the CUP page.
- **Review model:** **double-anonymous** — remove author names, affiliations, acknowledgments, and
  identifying self-references; every effort must prevent authors and reviewers from identifying each
  other.
- **Editors:** Shelome Gooden and Michael Putnam (verify the current masthead before naming an editor
  in any submission-facing document; editorship rotates).
- **Sections & limits:**
  - **General Research Article** — up to **18,000 words** *inclusive of notes, charts, tables, and
    appendices but excluding references*; submissions **over 12,000 words** are assessed for
    appropriateness and may face more stringent review.
  - **Research Report** — a smaller, targeted contribution (shorter; confirm the current cap).
  - **Review Article** — up to **5,000 words** (excluding references).
  - **Discussion Notes**, **Reviews/Book Notices**, and the four **online-only sections** (Perspectives,
    Phonological Analysis, Language and Public Policy, Teaching Linguistics).
- **Abstract:** required; short (target ~150 words — confirm the current limit on the author page).
- **House style:** the **Language Style Sheet** / **Unified Style Sheet for Linguistics** (author-date);
  not APA or Chicago.
- **Examples:** numbered; **Leipzig interlinear glossing**; **IPA** in a Unicode font.
- **Figures:** provide **alt text / descriptive captions**; vector where possible.
- **Data:** include a data-availability statement; share analysis data/code where ethical (see
  `lang-data-and-transparency`).

## Preflight checklist

### Section & length
- [ ] Correct section selected (General Research Article / Research Report / Review Article / other)
- [ ] Within the section's word limit; General Research Article word count computed on the inclusive rule
- [ ] Over 12,000 words only if the length is genuinely earned

### Anonymity (double-anonymous)
- [ ] No author names, affiliations, or acknowledgments in the manuscript
- [ ] Self-citations worded to avoid unmasking ("Author 2020", neutral phrasing)
- [ ] Identifying **file metadata stripped**; a separate title page if the portal requires it

### Content & format
- [ ] Abstract present, within the current word target, states question + data + finding
- [ ] Language Style Sheet citations and reference list (NOT APA/Chicago)
- [ ] Numbered examples, aligned Leipzig glosses, abbreviations listed, correct IPA
- [ ] Figure alt text / descriptive captions
- [ ] Data-availability statement accurate (no over-stated mandate)
- [ ] Not under review elsewhere (concurrent submission violates publishing ethics)

## Avoidable-failure triage (what bounces a submission, and the fix)

| Failure at submission | Fix before upload |
|-----------------------|-------------------|
| Author identity leaks (names, acknowledgments, metadata, unmasking self-cites) | anonymize text + strip metadata + neutralize self-references |
| Over the word limit / unearned length past 12,000 | cut to the section cap; earn every page |
| APA/Chicago references | convert to the Language/Unified Style Sheet |
| Misaligned glosses / faked IPA | fix Leipzig alignment; use a Unicode IPA font |
| Descriptive data dump, no theoretical stakes | frame the general claim (route to `lang-theory-building`) |

## Calibration (Language-specific posture, hedged)

Reflects *Language*'s house and culture, not universal rules; confirm on the live pages. The most
common avoidable failure is an under-anonymized file under double-anonymous review; the second is a word
count that misreads the **inclusive** General Research Article rule (notes and tables count; references
do not). Illustrative: a 12,800-word General Research Article catches three triage issues at preflight —
an acknowledgments footnote naming a grant and a collaborator, references still in APA from a prior
subfield-journal attempt, and two figures with no alt text — and after fixes the file is anonymous,
Style-Sheet-conformant, and within a defensible length.

## Anti-patterns

- Leaving author identifiers in the text, acknowledgments, or file metadata (breaks double-anonymous)
- Miscomputing the inclusive word limit or pushing past 12,000 without earning it
- APA/Chicago references instead of the Language/Unified Style Sheet
- Submitting a descriptive data dump with no theoretical claim (a desk return)
- Submitting while the paper is under review at another journal

## Output format

```
【Section】General Research Article / Research Report / Review Article / other
【Length】within cap on the inclusive rule; earned past 12,000? [Y/N]
【Anonymized】text + self-cites + metadata clean? [Y/N]
【Abstract】present, within limit, states question/data/finding? [Y/N]
【House style】Language/Unified Style Sheet (NOT APA/Chicago)? [Y/N]
【Glossing/IPA/alt text】examples, transcription, figures conform? [Y/N]
【Data statement】accurate, not over-stated? [Y/N]
【Next】lang-review-process → lang-rebuttal on R&R
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — printable preflight checklist
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — Language-conformant manuscript skeleton
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — CUP/LSA submission, style, and open-access sources
