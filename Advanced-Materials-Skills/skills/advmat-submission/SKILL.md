---
name: advmat-submission
description: Use when running the final pre-submission preflight for an Advanced Materials manuscript — article type, format, files, Supporting Information, TOC graphic, ORCID, and metadata for the Wiley submission system. Verifies submission readiness; does not write content.
---

# Advanced Materials Submission Preflight (advmat-submission)

## When to trigger

- "Submitting tonight" — the last check before the upload button
- You are unsure which files the Wiley submission system expects
- You need to confirm the manuscript fits its article-type format
- You want a single gate before handing off to peer review

## Pre-submission checklist

### Article type and format

- [ ] Correct article type selected (Communication vs. Research Article) and content matches (see `advmat-length-management`)
- [ ] Within the typeset page budget for that type (display items counted with text)
- [ ] Prepared in the Wiley Advanced Materials template / accepted format
- [ ] Communication: opening paragraph written to serve as the abstract; Research Article: short abstract (~200 words) + 3–7 keywords
- [ ] SI units, consistent significant figures, all abbreviations and formulae defined

### Files

- [ ] Main manuscript (with Experimental Section) + figures
- [ ] All figure files at Wiley's required resolution/format (vector for line art; high-DPI raster for micrographs)
- [ ] **Supporting Information** as a separate file, clearly labeled (see `advmat-supplementary`)
- [ ] **Table-of-Contents (TOC) graphic + blurb** prepared to spec
- [ ] Cover letter (see `advmat-cover-letter`)
- [ ] Bibliography in current Wiley Advanced Materials reference style

### Metadata and identifiers

- [ ] Title, abstract, author list entered consistently with the manuscript
- [ ] **ORCID** provided for authors as required (corresponding author at minimum)
- [ ] Affiliations and corresponding-author contact correct
- [ ] Funding recorded per Wiley instructions
- [ ] Data-availability statement and any required declarations present

### Authors and integrity

- [ ] All authors meet authorship criteria and approved submission
- [ ] Author contributions (CRediT) recorded if required
- [ ] Originality / not-under-consideration-elsewhere confirmed
- [ ] Prior preprint (ChemRxiv / arXiv) disclosed
- [ ] Competing-interest statement provided
- [ ] Ethics / biosafety statements included if biomaterials or animal/human-derived samples are involved

### Referees

- [ ] Suggested referees entered (see `advmat-referee-strategy`)
- [ ] Opposed referees entered with a brief, professional rationale

### Self-consistency

- [ ] Every "see Supporting Information" / "Figure Sx" pointer resolves
- [ ] Figure/scheme/table numbering continuous and matching in-text callouts
- [ ] SI items use the S-prefix and are each cited from the main text
- [ ] The main text stands alone without the SI (cross-check `advmat-supplementary`)

## Submission-system notes

- Submit through Wiley's online submission system for Advanced Materials (verify the current portal — Wiley has been migrating journals to the Research Exchange / "ReX" platform); confirm account and ORCID requirements on the author page.
- Color figures are free in Adv. Mater. (online and print) — but still budget figures against the page limit.
- Keep the SI as a distinct upload, not appended to the main manuscript PDF.
- Open access is optional: the OnlineOpen APC is high (on the order of ~US$6,000+ — confirm the live figure) and may be covered by a Wiley transformative/DEAL agreement for eligible institutions.
- If transferred from another Wiley journal, check that the transfer carried the correct files and that the article type is right for Adv. Mater.

## Night-before dry run

1. **Clean typeset.** Build the manuscript in the Wiley template from scratch to catch the real page count and any broken references.
2. **Page-budget check.** Confirm it fits the article-type format with a margin (see `advmat-length-management`).
3. **Pointer audit.** Confirm every "Supporting Information" and "Figure Sx" callout resolves, and no S-item is uncited.
4. **Asset check.** TOC graphic + blurb ready; figures at required resolution; SI a separate file.
5. **Metadata dry-fill.** Draft the portal fields (title, abstract, keywords, ORCID, funders, declarations) in a text file so the live session is transcription, not composition.
6. **Freeze.** No content edits after the dry run; any change reopens the page-budget and pointer audits.

## Desk-return triggers to eliminate

| Trigger                                       | Why editors bounce it                 |
|-----------------------------------------------|---------------------------------------|
| Wrong article type for the content            | Routed off the intended track         |
| Missing / off-spec TOC graphic                | Incomplete submission                 |
| SI appended inside the main PDF               | Breaks separate-SI production         |
| No benchmarking / incremental framing         | Reads as specialist → desk reject     |
| Missing ORCID / declarations                  | Held in editorial screening           |

## Anti-patterns

- Discovering an overrun only when typeset at production
- Uploading the SI glued onto the main manuscript PDF
- Wrong article type (Communication vs. Research Article) for the content
- Broken "see SI" cross-references after last-minute trimming
- Forgetting the TOC graphic, ORCID, or a required declaration
- Not disclosing a prior preprint

## Output format

```
【Article type】Communication / Research Article — matches content?  yes / fix
【Format】Wiley template; within page budget?  yes / fix
【Files】manuscript / figures / SI / TOC graphic / cover letter / bib — all present?
【Metadata】ORCID + keywords + declarations?  yes / fix
【Integrity】originality, preprint disclosure, competing interests, ethics
【Referees】suggested + opposed entered?  yes / fix
【Stands alone】yes / fix
【Next】await reports → advmat-revision; plan referees → advmat-referee-strategy
```

## Attached resources

- [`templates/checklist.md`](templates/checklist.md) — full pre-submission self-check across article type / format / files / metadata / authors / referees / self-consistency
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — Adv. Mater. skeleton (title, abstract/opening, body, Experimental Section, figure/TOC budgeting, SI outline)
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — characterization-analysis software, the DFT/simulation stack, figure tools, and data repositories

> Portal (Research Exchange/ReX vs. legacy), file specs, TOC-graphic format, APC, and required statements are volatile — verify all on the official Wiley Advanced Materials author page before submitting.
