---
name: jmcb-submission
description: Use when running the final pre-submission preflight for a Journal of Money, Credit and Banking (JMCB) manuscript via Editorial Express — the page limit, the submission fee, the title-page/format rules, the data-exemption request, and house citation style. Final checks; it does not draft content.
---

# Submission Preflight (jmcb-submission)

## When to trigger

- "Submitting tomorrow" — last check before uploading to Editorial Express
- Unsure which files, fee, and declarations the JMCB submission expects
- Confirming the manuscript meets the ~40-page recommendation and format rules
- Deciding how to handle restricted bank/central-bank data (data exemption)

## Process facts (检索于 2026-06；以官网为准 — re-confirm on the OSU/Wiley pages)

- **Owner/publisher:** the journal is owned by the **Ohio State University Department of Economics** and published by **Wiley-Blackwell**; it appears ~7 issues/year. Online content is on Wiley Online Library (ISSN 1538-4616).
- **Submission portal:** submissions go through **Editorial Express** (editorialexpress.com/jmcb), *not* Wiley's ScholarOne or Editorial Manager — a common point of confusion for authors used to other Wiley journals.
- **Submission fee:** **US$150 for subscribers / US$200 for non-subscribers** (待核实；以官网为准), paid at submission. If an editor declines **without consulting referees**, the fee is refunded **minus US$50** for administrative costs. **No fee for resubmissions** of invited revisions.
- **Length:** the journal **strongly recommends manuscripts not exceed ~40 pages** with 1.5 line spacing, where the count **includes references, tables, and figures but excludes the online appendix**; excessively long submissions may be summarily rejected.
- **Data/replication:** consistent with JMCB's archive heritage, expect a data/code expectation; if data are restricted, **request a data exemption at submission** and document the access path.
- **Citation style:** author-year in text; reference list alphabetical by author then chronological.
- **Editors (verified 2026-06-22):** the editorial group includes Sanjay Chugh and Pok-sang Lam (OSU), Robert DeYoung (Kansas), and Kenneth D. West (Wisconsin–Madison); other listings add Luc Laeven (ECB) and Jing Cynthia Wu (Illinois). Re-verify the current desks on the Wiley/OSU board before tailoring a cover letter.

## Preflight checklist

### Format & length
- [ ] Manuscript within the **~40-page recommendation** (incl. references, tables, figures; excl. online appendix), 1.5 spacing
- [ ] **PDF** for the manuscript and the cover letter; mathematics survives PDF conversion intact
- [ ] **Title page** with author names, titles, and affiliations (confirm whether an anonymized version is also needed — blinding policy 待核实)
- [ ] Tables and figures self-contained (units, shock size, horizon on IRFs; FE/clustering/N on tables)
- [ ] **Author-year citations**; reference list alphabetical then chronological
- [ ] Online appendix prepared separately; main text self-contained

### Portal, fee & files (Editorial Express)
- [ ] Submitting via **Editorial Express** (not ScholarOne/Editorial Manager)
- [ ] Submission **fee** ready (subscriber vs. non-subscriber rate); aware of the minus-US$50 desk-reject refund and the resubmission waiver
- [ ] Cover letter (PDF) stating fit, the policy contribution, and the JMCB vs. sibling-journal rationale
- [ ] Online appendix and any non-restricted replication materials attached

### Data & declarations
- [ ] Replication/data plan decided; **data-exemption request** prepared if bank/central-bank data are restricted, with the access path documented
- [ ] Confirmed the paper is not under review elsewhere; conflict/funding disclosures ready
- [ ] AI not listed as an author

## Two fees, two stages — do not conflate them

A frequent author error is confusing the **submission fee** with the **Open Access APC**. They occur at different stages and serve different purposes:

| | Submission fee | Open Access APC |
|---|---|---|
| When | At submission, before review | Only if accepted *and* you choose OA |
| Amount (待核实) | US$150 subscriber / US$200 non-subscriber | ≈US$3,990 / £2,690 / €3,330 |
| Refundable | Minus US$50 if desk-rejected without referees; waived for resubmissions | n/a |
| Required? | Yes, to enter review | No — only for the OA option; default publication has no APC |

Budget for the submission fee now; the APC is a later, optional decision.

## The cover letter does real work here

Because JMCB sits among close siblings, the cover letter should pre-empt the "wrong journal" reflex: state in two or three sentences why the paper is a JMCB contribution (the monetary/credit/banking mechanism and the policy payoff), not a JME, AEJ:Macro, or JBF paper. Name the contribution and the policy lever; do not merely summarize the abstract. If the data are restricted, note the data-exemption request in the letter so the editor is not surprised.

## Anti-patterns

- Submitting through the wrong system (ScholarOne/Editorial Manager) because it is a Wiley journal — JMCB uses **Editorial Express**
- Blowing past ~40 pages by forgetting that references, tables, and figures count toward it
- Treating the **Open Access APC** (≈US$3,990, 待核实) as if it were the submission-time fee — they are different charges
- Restricted-data results with no data-exemption request and no access path
- A cover letter that does not say why this is a JMCB paper rather than a JME/JBF paper

## Last-mile traps specific to JMCB

- **Page count surprise.** Authors counting only body text discover at upload that references and exhibits push them past ~40 pages. Verify the *full* count, with the online appendix split out, before you start the submission.
- **Math that breaks in PDF.** The guidelines warn that mathematics must survive PDF conversion; check that no equation renders as a missing glyph in the final file.
- **Title page completeness.** Names, titles, and affiliations are expected on the title page; confirm whether a separate anonymized file is also required (blinding policy 待核实).
- **Cover letter as PDF.** Both the manuscript and the cover letter are submitted as PDFs through Editorial Express.

## Output format

```text
【Length】≤ ~40pp incl. refs/tables/figures, excl. online appendix? [Y/N]
【Format】PDF; title page with affiliations; author-year cites? [Y/N]
【Exhibits】IRFs labeled (shock/units/horizon); tables show FE/clustering/N? [Y/N]
【Portal + fee】Editorial Express; correct fee tier ready? [Y/N]
【Data】replication plan / data-exemption + access path if restricted? [Y/N]
【Cover letter】states JMCB fit + policy contribution vs. siblings? [Y/N]
【Next step】submit via Editorial Express → jmcb-referee-strategy for what to expect
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — submission self-check
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — lightweight manuscript scaffold
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official URLs and volatile facts
