---
name: jmis-submission
description: Use when running the final pre-submission preflight for a Journal of Management Information Systems (JMIS) manuscript — the email-to-EIC intake, full anonymization for double-blind review, the ≤50-page and 150-word-abstract limits, the numbered bracketed reference style, and the cover-letter/attachment package. Final checks; it does not draft content.
---

# Submission Preflight (jmis-submission)

## When to trigger

- "Submitting tomorrow" — last check before emailing the manuscript to the EIC
- Unsure exactly what files, anonymization, and formatting JMIS expects
- Confirming the paper is double-blind-ready and inside the page/abstract limits
- The team assumed a ScholarOne/T&F portal and needs the actual intake route

## Process facts (source map refreshed 2026-06; re-confirm on jmis-web.org / tandfonline)

- JMIS is the Taylor & Francis (Routledge) quarterly founded in 1984 and edited by **Vladimir Zwass** (Fairleigh Dickinson University); Online ISSN 1557-928X.
- **Intake is by email, not a portal.** Manuscripts are submitted to the EIC at **jmis@fdu.edu** with the subject line **"JMIS Submission"**, as MS Word or PDF attachments. There is no ScholarOne/T&F submission system at the intake stage. (检索于 2026-06；以官网为准.)
- **Review is double-anonymized.** The manuscript file must be **fully anonymized** so authors are not identifiable anywhere in the work; self-references may remain in the reference list (written so they do not reveal authorship).
- **Length:** the complete manuscript should **not exceed 50 pages**; text in **12-point, double-spaced, left-justified**, pages numbered.
- **Abstract:** **up to 150 words**, with **no citations**; include a set of **keywords/phrases**.
- **References:** numbered in brackets (e.g., **[9]**) with an **alphabetized reference list** — an IEEE-like numbered style, not author-date.
- **Attachments:** a cover letter (author affiliations, contact info, brief biographies) sent separately from the anonymized paper; **online appendixes** may be submitted separately; **survey instruments** must be provided as separate anonymized attachments if not in the paper.
- No submission fee is stated in the author guidelines. **待核实** if a fee or APC appears at acceptance.

## Preflight checklist

### Anonymization (double-blind)
- [ ] No author names, affiliations, emails, acknowledgments, or funding IDs in the manuscript file
- [ ] Self-citations phrased so they do not reveal authorship; identifying file metadata stripped
- [ ] Survey instruments / appendixes anonymized as separate attachments

### Format & length
- [ ] Complete manuscript **≤50 pages**; **12pt, double-spaced, left-justified**; pages numbered
- [ ] **Abstract ≤150 words, no citations**; keywords/phrases included
- [ ] References in **numbered bracketed [n]** style with an **alphabetized list**; formats correct for periodicals/books/chapters/proceedings
- [ ] Core claims established in the body; appendixes carry support only
- [ ] Tables/figures legible (grayscale-safe), with self-contained notes

### Files & intake
- [ ] Anonymized manuscript (MS Word or PDF)
- [ ] Separate cover letter (affiliations, contact, brief bios)
- [ ] Separate online appendix / survey-instrument attachments as needed
- [ ] Email to **jmis@fdu.edu**, subject **"JMIS Submission"**
- [ ] Confirmed the paper is not under review elsewhere

## Anti-patterns

- Submitting through a Taylor & Francis / ScholarOne portal — JMIS intake is the EIC's email
- An identifiable manuscript (names, affiliations, funding) sent into a double-blind process
- A manuscript over 50 pages, or an abstract over 150 words / with citations
- Author-date references when JMIS requires numbered brackets
- Bundling the cover letter into the anonymized file, or omitting survey-instrument attachments

## Output format

```text
【Anonymization】fully blind, metadata stripped, self-cites safe? [Y/N]
【Format】≤50pp / 12pt double-spaced / pages numbered? [Y/N]
【Abstract】≤150 words, no citations, keywords present? [Y/N]
【References】numbered [n] + alphabetized list? [Y/N]
【Files】anonymized MS + separate cover letter + appendix/instruments? [Y/N]
【Intake】email to jmis@fdu.edu, subject "JMIS Submission"? [Y/N]
【Next step】jmis-review-process for what to expect
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — submission self-check
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — lightweight manuscript scaffold
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official URLs and volatile facts
