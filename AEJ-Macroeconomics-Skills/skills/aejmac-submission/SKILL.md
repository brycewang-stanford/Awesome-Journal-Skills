---
name: aejmac-submission
description: Use when running the final pre-submission preflight for the American Economic Journal: Macroeconomics (AEJ: Macro) via the AEA submission system — membership-scaled fee, JEL codes, PDF and length rules, ≤100-word abstract, disclosure statements, and data/code readiness. Final checks; it does not draft content.
---

# Submission Preflight (aejmac-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit on the AEA system
- Unsure which files, fees, and statements the AEA submission expects
- Confirming the format rules (PDF, length, abstract, JEL) are AEJ: Macro-compliant
- Confirming disclosure statements and data/code readiness are in order

## Process facts (verified 2026-06; editor + fees re-verified 2026-06-22; re-confirm on the official AEA pages)

- AEJ: Macro is one of the AEA's four *American Economic Journals* (founded 2009; quarterly). Print ISSN 1945-7707 / Online ISSN 1945-7715. Submission is through the **AEA submission system** as **PDF**. Editor (re-verified 2026-06-22): **Ayşegül Şahin** (Princeton); coeditors Bianchi (Johns Hopkins), Kalemli-Özcan (Brown), Quadrini (USC) — re-verify the masthead on the AEA editors page before submission.
- **Submission fee (membership- and income-scaled; 检索于 2026-06-22；以官网为准):** AEA members US$200 (high-income country) / US$100 (middle-income) / US$0 (low-income); nonmembers US$300 / US$200 / US$0. Paid by credit card at submission. Papers **rejected without review receive a 50% refund**.
- **Publication fee:** US$15 per typeset page, assessed at page proofs (applies to papers submitted after Feb 1, 2024; 检索于 2026-06-22；以官网为准).
- **Review:** **single-blind** (author known to referee). JEL codes required. AI cannot be listed as an author.
- **Data & code:** governed by the AEA Data and Code Availability Policy; the **AEA Data Editor** runs a pre-publication reproducibility check; deposit at the AEA Data and Code Repository on openICPSR (see `aejmac-replication-package`). Field experiments register in the AEA RCT Registry.

## Preflight checklist

### Format & length
- [ ] One **PDF**; first page has title, byline, and complete affiliations
- [ ] **Abstract ≤100 words**
- [ ] **JEL codes** and keywords included
- [ ] Within length guidance: ~40 pages (11pt, 1.5 spacing) / ~45 pages (12pt, 1.5 spacing), **including** figures, tables, references, and appendices (检索于 2026-06；以官网为准)
- [ ] Figures/tables legible after AEA two-column typesetting; IRFs have stated confidence bands
- [ ] Online appendix prepared for material beyond the page limit

### Files & fees for the AEA system
- [ ] Main manuscript PDF; online appendix file if any
- [ ] Fee tier determined (member/nonmember × income tier); card ready
- [ ] Replication package staged for the post-acceptance Data Editor check (incl. simulation/calibration code)
- [ ] Field-experiment registration link ready, if applicable

### Declarations
- [ ] **Separate disclosure statement from each coauthor** (AEA policy; US$10,000 interested-party threshold; all funding sources, in-kind support, positions)
- [ ] Confirmed the paper is original and not under review elsewhere
- [ ] AI not listed as an author

## Anti-patterns

- Abstract over 100 words (a hard AEJ: Macro constraint, tighter than most journals)
- Missing JEL codes
- Forgetting a per-coauthor disclosure statement (each coauthor, separately)
- Overrunning the ~40-page guidance instead of moving material to the online appendix
- Treating the $15/page proof fee as a submission-time charge
- Assuming double-blind anonymization (AEJ: Macro is single-blind)

## Output format

```
【Format】PDF; title page; JEL + keywords? [Y/N]
【Abstract】≤100 words? [Y/N] (current: __)
【Length】within ~40pp guidance (incl. appendices) or appendix split planned? [Y/N]
【Fee】member/nonmember × income tier determined; card ready? [Y/N]
【Disclosure】separate statement per coauthor; $10k threshold checked? [Y/N]
【Data/code】replication package staged for the AEA Data Editor? [Y/N]
【Next step】submit via the AEA system → aejmac-referee-strategy for what to expect
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — 8-section pre-submission self-check
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official AEA URLs behind every fact
