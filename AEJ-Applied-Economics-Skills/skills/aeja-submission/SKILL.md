---
name: aeja-submission
description: Use when running the final pre-submission preflight for an American Economic Journal: Applied Economics (AEJ: Applied) manuscript via the AEA online submission system — double-blind anonymization, JEL codes, the member submission fee, format, disclosures, and the AEA data-policy readiness. Final checks; it does not draft content.
---

# Submission Preflight (aeja-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit on the AEA system
- Unsure which files, fees, and declarations the AEA submission expects
- Confirming double-blind anonymization and JEL codes are in order
- Confirming the paper is data-policy-ready should it advance

## Process facts (检索于 2026-06；以官网为准 — re-confirm on aeaweb.org)

- AEJ: Applied is one of the four **American Economic Journals**, published by the **American Economic Association (AEA)**, quarterly; submission is through the **AEA online submission system**.
- **Double-blind review:** the manuscript must be **anonymized** — remove author names, affiliations, acknowledgments, and identifying self-citations from the submitted file.
- **Submission fee:** a **modest fee for AEA members, with a higher nonmember surcharge**, paid at submission (amount is **volatile — re-confirm**). Some hardship/low-income waivers may apply.
- **JEL codes required**; keywords and an abstract per AEA norms; a separate (non-anonymized) title page with author details is typically supplied alongside the blinded manuscript.
- **Editor:** Benjamin Olken (MIT); coeditors incl. Boustan, Cabral, Hull, Jaravel, Ryan; **Data Editor:** Lars Vilhuber (Cornell) (检索于 2026-06；以官网为准).
- **Data & code:** the AEA **Data and Code Availability Policy** applies; you need not deposit at submission, but the paper must be **buildable into an openICPSR package** that the Data Editor will verify **before publication** (`aeja-replication-package`).
- One paper under review at a time per AEA rules; AI cannot be listed as an author.

## Preflight checklist

### Anonymization & front matter
- [ ] Manuscript fully **anonymized** (no names, affiliations, acknowledgments, identifying self-citations) for double-blind review
- [ ] Separate non-anonymized **title page** with authors, affiliations, contact, acknowledgments prepared
- [ ] **JEL codes** assigned; keywords + abstract within AEA norms

### Format & exhibits
- [ ] Standard AEA manuscript format (readable font, reasonable margins/spacing); pages numbered
- [ ] Tables and figures legible; **standard errors reported** (stars permitted but SEs are required); exhibit notes self-contained
- [ ] Online appendix prepared for supplementary material (kept separate from the main paper)
- [ ] References complete and consistent (AEA author-date house style)

### Files, fee & policy readiness
- [ ] Blinded main PDF + title page + online appendix uploaded as required by the system
- [ ] **Submission fee** ready (member vs nonmember confirmed; waiver if eligible)
- [ ] Replication package buildable into an openICPSR deposit; Data Availability Statement drafted
- [ ] Experimental/own-data: instructions/instruments ready; pre-registration cited

### Declarations
- [ ] Disclosure statement (funding, interested-party relationships) per AEA policy
- [ ] Confirmed not under review elsewhere; AI not listed as an author

## Anti-patterns

- Submitting a manuscript that is **not anonymized** (breaks double-blind; common desk issue)
- Forgetting **JEL codes** or submitting without the separate title page
- Treating the data/code package as irrelevant at submission, then scrambling at the pre-publication check
- Omitting standard errors from exhibits, or notes that are not self-contained
- Assuming the fee amount from memory instead of re-confirming on aeaweb.org

## Output format

```
【Anonymization】manuscript blinded + title page separate? [Y/N]
【Front matter】JEL codes + keywords + abstract within norms? [Y/N]
【Exhibits】SEs reported, notes self-contained, online appendix separate? [Y/N]
【Fee】member/nonmember confirmed, ready (or waiver)? [Y/N]
【Data-policy readiness】openICPSR-buildable + DAS drafted? [Y/N]
【Declarations】disclosure done; not under review elsewhere; no AI author? [Y/N]
【Next step】submit via AEA system → aeja-rebuttal after the decision
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — 8-section pre-submission self-check
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official AEA/AEJ: Applied URLs behind every fact
