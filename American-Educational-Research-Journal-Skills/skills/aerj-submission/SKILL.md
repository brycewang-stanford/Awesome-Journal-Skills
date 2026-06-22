---
name: aerj-submission
description: Use when running the final pre-submission preflight for the American Educational Research Journal (AERJ) via ScholarOne Manuscripts — masked preparation, length and abstract limits, APA 7th-edition formatting, ORCID, and a separate title page. Final checks; it does not draft content.
---

# Submission Preflight (aerj-submission)

The last check before pressing submit on **ScholarOne Manuscript Central**. AERJ is **masked**, so the
single most common avoidable failure is an under-anonymized manuscript or identifying metadata. Verify
volatile specifics on the official page before relying on them.

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure which files/metadata ScholarOne expects
- Confirming length/abstract limits, masking, and APA compliance

## Process facts (verified 2026-06-20; re-check live page before upload)

- **Owner / publisher:** American Educational Research Association (AERA) / SAGE. AERJ is the
  **flagship journal of AERA**.
- **One integrated journal — do NOT choose a section.** AERJ was *formerly* divided into **Social and
  Institutional Analysis** and **Teaching, Learning, and Human Development** sections, but the
  integrated AERJ began receiving new manuscripts on **July 1, 2015** and publishing on
  **January 1, 2016**. Submit to the single integrated journal; do not pick between the former sections.
- **Portal:** **ScholarOne Manuscripts** at **https://mc.manuscriptcentral.com/aerj**.
- **Review model:** **double-anonymous / masked** — names only on the **separate title page file**.
- **Length:** manuscript **maximum 50 pages**, double-spaced, 12-pt, 1" margins, **inclusive** of tables,
  figures, notes, and references; 8.5" x 11" paper.
- **Abstract:** **100–120 words**.
- **Style:** manuscripts follow **APA 7th edition**; AERJ uses the **SAGE Harvard reference style** on
  its submission-guidelines page for the reference list (verify against the live guidelines).
- **ORCID:** required for the corresponding author.
- **Fee:** the SAGE guidelines state there is **no fee to publish or submit**; gold OA via **SAGE Choice** is available for a fee.
- **Decision timeline / acceptance rate / AERA-membership-to-submit:** not stated in the pack source map
  — treat as **待核实/需复核** and confirm on the live SAGE author-instructions and AERA journal pages.

## Preflight checklist

### Fit & length
- [ ] Dominant education-research lens named for **integrated** AERJ fit (one journal; do **not** pick a former section)
- [ ] Manuscript within the 50-page maximum, including tables/figures/notes/references
- [ ] Abstract **100–120 words**, stating purpose + method + finding + significance

### Masking (anonymous review)
- [ ] No author names/affiliations/acknowledgments in the manuscript file
- [ ] No identifying citations, references, or footnotes ("as we showed in…" neutralized)
- [ ] Identifying **file metadata stripped** (document properties, comments)
- [ ] Separate **title page file** with all author/affiliation/contact details
- [ ] Anonymized preregistration / OSF link if referenced

### Format & metadata
- [ ] **APA 7th edition** formatting; reference list per the **SAGE Harvard reference style** on the guidelines page (verify live)
- [ ] Double-spaced, 12-pt, 1" margins
- [ ] Corresponding-author **ORCID** ready
- [ ] Figures/tables self-contained, accessible, anonymized (see `aerj-tables-figures`)

### Compliance & materials
- [ ] IRB / human-subjects / consent compliance per AERA ethics
- [ ] Reporting meets the AERA standard for the method (see `aerj-transparency-and-data-policy`)
- [ ] Data/code availability or access plan documented

## Anti-patterns

- Leaving author identifiers in the text, acknowledgments, or file metadata (breaks masking)
- Abstract outside 100–120 words; manuscript over the page limit
- Letting the manuscript read as a specialty-journal paper with no field-wide AERJ fit
- Mixing citation styles instead of clean APA 7th
- Budgeting for a submission fee that is not charged (verify)

## Desk-reject triggers at upload (AERJ-specific)

ScholarOne screening and the editors catch avoidable failures before review. This table maps
the most common pre-submission errors to their consequence so you can clear each one.

| Failure at upload | What it breaks | Avoidable fix |
|-------------------|----------------|---------------|
| Author name in text/metadata | Masked review | Strip identifiers; move them to the title-page file |
| No clear AERJ fit | Editor/reviewer match | Name the dominant education lens and field-wide significance |
| Abstract over the limit | Format compliance | Trim to the stated word range; verify the figure |
| Over-length manuscript | Inclusive page count | Cut to the page limit counting tables/figures/refs |
| Mixed citation styles | APA-7 compliance | Run a single clean author-date pass |

## Worked preflight vignette (illustrative)

A team is uploading a **mixed-methods evaluation of a community-schools initiative** to AERJ. The
preflight catches three things: an acknowledgments line thanking a named foundation
(breaks masking), an abstract of **134** words (illustrative, over a 100–120 target), and a figure
note citing "our prior district study" (a self-citation tell). Fixing all three before submission —
moving funder thanks to the title page, trimming the abstract to **118** words, neutralizing the
self-reference — converts a likely desk return into a clean send-out. Confirm the exact length and
abstract limits against the journal's current submission guidelines.

## Referee/editor pushback the preflight pre-empts

- *"This is not anonymized."* → Strip text, self-citation, and file-metadata identifiers before upload.
- *"The paper reads too narrow for AERJ."* → State the dominant education lens and field-wide stake in the cover letter.
- *"Reporting materials missing."* → Have the AERA-standard reporting and data-availability plan ready
  at submission, not after acceptance.

## Output format

```
【AERJ fit】dominant lens + field-wide stake stated? [Y/N]
【Masked】text + self-refs + file metadata clean + separate title page? [Y/N]
【Abstract】word count (100–120)
【Length】within limit incl. tables/figures/refs? [Y/N]
【APA 7th + ORCID】[Y/N]
【Reporting + data plan】ready? [Y/N]
【Next】await decision → aerj-rebuttal on R&R
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — APA reference managers, anonymization, repro tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official AERJ submission facts
