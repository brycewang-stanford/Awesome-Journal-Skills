---
name: restat-submission
description: Use when running the final pre-submission preflight for The Review of Economics and Statistics (REStat) via Editorial Express — format rules, abstract limit, online-appendix cap, article categories, submission fee, the proprietary-data fee hold, and house style. Final checks; it does not draft content.
---

# Submission Preflight (restat-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit on Editorial Express
- Unsure which files, fees, and declarations the REStat submission expects
- Confirming format (PDF, 12pt, double-spaced) and house style are REStat-compliant
- Deciding Article vs Short Paper, and whether proprietary data affects the fee timing

## Process facts (refreshed 2026-06-20; live-check volatile items on MIT Press)

- REStat is published by **MIT Press**, edited at the **Harvard Kennedy School**; submission is via **Editorial Express** (`editorialexpress.com/.../e-submit...?dbase=restat`). Editors as of 2026: Will Dobbie (Harvard) and Raymond Fisman (Boston U), co-chairs.
- **Submission fee:** nonrefundable **US$125** per new submission, paid online by credit card at submission. **Proprietary-data papers: do NOT pay the fee until the editorial office confirms** the data comply with the Data and Code Availability Policy.
- **Article categories:** full-length **Articles**, **Notes**, and (since Dec 2019) **Short Papers** — Short Papers strictly **≤6000 words and ≤5 exhibits**; live-check category text before upload.
- **Format:** one **PDF**; **12-point font**; **double-spaced throughout** (including abstract, acknowledgments, footnotes, references); **online appendix ≤20 pages**, but the **manuscript must be self-contained**.
- **Abstract ≤100 words**, in JEL-suitable form; JEL codes / keywords on the title page.
- **Data & code:** empirical papers fall under the Data and Code Availability Policy (deposit to the **REStat Harvard Dataverse** before publication); indicate proprietary data at submission (`restat-replication-package`).

## Preflight checklist

### Format & style
- [ ] One **PDF**; font **12-point**; **double-spaced throughout** (abstract, acknowledgments, footnotes, references included)
- [ ] **Abstract ≤100 words**, JEL-suitable; JEL codes + keywords on the title page
- [ ] **Online appendix ≤20 pages**; main manuscript **self-contained**
- [ ] Standard economics house style: SEs in parentheses; stars permitted but never instead of SEs; self-contained exhibit notes
- [ ] Tables/figures legible; the headline result readable from one main exhibit

### Category & files
- [ ] Article vs **Note** vs **Short Paper** chosen; if Short Paper, **≤6000 words and ≤5 exhibits**
- [ ] Cover letter prepared (state the contribution and venue fit)
- [ ] Online appendix file ready (≤20 pp)

### Fees & data policy
- [ ] Submission fee (**US$125**, nonrefundable) ready by credit card
- [ ] **Proprietary data:** fee **held** until the editorial office confirms policy compliance; access instructions documented
- [ ] Replication plan in place for the REStat Harvard Dataverse (`restat-replication-package`)

### Declarations
- [ ] Original, unpublished work, not under review elsewhere; no duplicate submission
- [ ] Funding / conflict-of-interest disclosures prepared; AI not listed as an author

## Anti-patterns

- Paying the **US$125 fee on a proprietary-data paper before** compliance is confirmed
- Abstract over 100 words, or single-spaced manuscript (REStat wants double-spacing throughout)
- Online appendix doing work the self-contained main paper must do, or exceeding 20 pages
- Submitting a Short Paper over 6000 words / 5 exhibits
- Stars with no standard errors; exhibits with non-self-contained notes
- Planning the Harvard Dataverse deposit only after acceptance

## Output format

```
【Format】PDF / 12pt / double-spaced throughout? [Y/N]
【Abstract】≤100 words + JEL/keywords? [Y/N]
【Category】Article / Note / Short Paper (≤6000w, ≤5 exhibits if Short)? [Y/N]
【Appendix】online appendix ≤20pp; main self-contained? [Y/N]
【Fee】US$125 ready; proprietary-data fee HELD until compliance? [Y/N]
【Data policy】Harvard Dataverse plan + proprietary flagged? [Y/N]
【Declarations】originality / disclosures / no AI author? [Y/N]
【Next step】submit via Editorial Express → await editor-managed review
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — 8-section pre-submission self-check
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official REStat / MIT Press URLs behind every fact
