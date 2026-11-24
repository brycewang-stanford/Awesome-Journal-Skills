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

## Process facts (refreshed 2026-06-20; re-verified 2026-11-23; live-check volatile items on MIT Press)

- REStat is published by **MIT Press**, edited at the **Harvard Kennedy School**; submission is via **Editorial Express** (`editorialexpress.com/.../e-submit...?dbase=restat`). Co-chairs as of 2026-11-23: **Will Dobbie (Harvard) and Tavneet Suri (MIT)** (Raymond Fisman is no longer listed). Editor assignment follows the paper's **JEL codes**; you may request a specific editor.
- **Review:** single-blind — MIT Press's peer-review taxonomy for REStat lists identity transparency as **"Single anonymized"**; no manuscript anonymization is needed.
- **Submission fee:** nonrefundable **US$125** per new submission, paid online by credit card at submission. **Waived** when one author holds a current-year individual subscription to REStat, or when a majority of the authors primarily work in low-income or lower-middle-income economies (World Bank). **Proprietary-data papers: do NOT pay the fee until the editorial office confirms** the data comply with the Data and Code Availability Policy.
- **Article categories:** full-length **Articles**, **Notes**, and (since Dec 2019) **Short Papers** — Short Papers strictly **≤6000 words and ≤5 exhibits** (each exhibit below five buys up to 200 extra words, so a zero-exhibit Short Paper may run to 7,000 words); the word count comes from the AEA word-count tool (main text + footnotes only) and is entered and uploaded (Word Count PDF, Step 5) at submission; over-length Short Papers are returned unreviewed and must be resubmitted as new, with a new fee. Short Papers may carry an online appendix of **no more than 20 pages**. Live-check category text before upload.
- **Format:** one **PDF**; **12-point font**; **double-spaced throughout** (including abstract, acknowledgments, footnotes, references); **page limit: 45 pages or less at acceptance** (double-spaced, 12-point, one-inch margins; text, tables, figures, references and everything intended for print) — not required at submission but encouraged; **online appendices have no size restriction** for regular papers (the ≤20-page cap applies to Short Papers), but the **manuscript must be self-contained**.
- **AI disclosure (required):** all authors must disclose whether generative AI was used in any aspect of the paper, naming the tool(s), model(s) and version(s) and every purpose (writing, coding the analysis, assembling data, formalizing the model, ...); submitting extensive prompts is encouraged.
- **Abstract ≤100 words**, in JEL-suitable form; JEL codes / keywords on the title page.
- **Data & code:** empirical papers fall under the Data and Code Availability Policy (deposit to the **REStat Harvard Dataverse** before publication); indicate proprietary data at submission (`restat-replication-package`).

## Preflight checklist

### Format & style
- [ ] One **PDF**; font **12-point**; **double-spaced throughout** (abstract, acknowledgments, footnotes, references included)
- [ ] **Abstract ≤100 words**, JEL-suitable; JEL codes + keywords on the title page
- [ ] Main paper aimed at **≤45 pages** (required at acceptance); online appendix unrestricted for regular papers (**≤20 pages for a Short Paper**); main manuscript **self-contained**
- [ ] Standard economics house style: SEs in parentheses; stars permitted but never instead of SEs; self-contained exhibit notes
- [ ] Tables/figures legible; the headline result readable from one main exhibit

### Category & files
- [ ] Article vs **Note** vs **Short Paper** chosen; if Short Paper, **≤6000 words and ≤5 exhibits** (+200 words per unused exhibit), AEA word-count PDF ready for Step 5
- [ ] Cover letter prepared (state the contribution and venue fit)
- [ ] Online appendix file ready (≤20 pp if a Short Paper)

### Fees & data policy
- [ ] Submission fee (**US$125**, nonrefundable) ready by credit card
- [ ] **Proprietary data:** fee **held** until the editorial office confirms policy compliance; access instructions documented
- [ ] Replication plan in place for the REStat Harvard Dataverse (`restat-replication-package`)

### Declarations
- [ ] Original, unpublished work, not under review elsewhere; no duplicate submission
- [ ] Funding / conflict-of-interest disclosures prepared; AI not listed as an author
- [ ] **Generative-AI disclosure** prepared for every author: whether AI was used, tool/model/version, and all purposes

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue restat-skills   # from a clone of the AJS repository
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

## Anti-patterns

- Paying the **US$125 fee on a proprietary-data paper before** compliance is confirmed
- Abstract over 100 words, or single-spaced manuscript (REStat wants double-spacing throughout)
- Online appendix doing work the self-contained main paper must do, or (Short Papers) exceeding 20 pages
- Omitting the generative-AI disclosure, or describing AI use without the model/version and purposes
- Submitting a Short Paper over 6000 words / 5 exhibits
- Stars with no standard errors; exhibits with non-self-contained notes
- Planning the Harvard Dataverse deposit only after acceptance

## Output format

```
【Format】PDF / 12pt / double-spaced throughout? [Y/N]
【Abstract】≤100 words + JEL/keywords? [Y/N]
【Category】Article / Note / Short Paper (≤6000w, ≤5 exhibits if Short)? [Y/N]
【Appendix】main ≤45pp target; online appendix (≤20pp if Short); main self-contained? [Y/N]
【Fee】US$125 ready; proprietary-data fee HELD until compliance? [Y/N]
【Data policy】Harvard Dataverse plan + proprietary flagged? [Y/N]
【Declarations】originality / disclosures / generative-AI disclosure / no AI author? [Y/N]
【Next step】submit via Editorial Express → await editor-managed review
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — 8-section pre-submission self-check
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official REStat / MIT Press URLs behind every fact
