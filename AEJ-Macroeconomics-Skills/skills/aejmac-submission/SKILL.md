---
name: aejmac-submission
description: Use when running the final pre-submission preflight for the American Economic Journal: Macroeconomics (AEJ: Macro) via the AEA ScholarOne system — author-anonymized manuscript and title page, membership-scaled fee, JEL codes, PDF and length rules, ≤100-word abstract, disclosure statements, and data/code readiness. Final checks; it does not draft content.
---

# Submission Preflight (aejmac-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit on the AEA system
- Unsure which files, fees, and statements the AEA submission expects
- Confirming the format rules (PDF, length, abstract, JEL) are AEJ: Macro-compliant
- Confirming disclosure statements and data/code readiness are in order

## Process facts (re-verified 2026-11-24 on the official AEA pages; re-confirm before submitting)

- AEJ: Macro is one of the AEA's four *American Economic Journals* (founded 2009; quarterly). Print ISSN 1945-7707 / Online ISSN 1945-7715. Submission is through **ScholarOne Manuscripts** as a **PDF** (under 10 MB when reasonably possible). Editor (re-verified 2026-11-24): **Ayşegül Şahin** (Princeton); coeditors Bianchi (Johns Hopkins), Kalemli-Özcan (Brown), Quadrini (USC) — re-verify the masthead on the AEA editors page before submission.
- **Submission fee (membership- and income-scaled; 检索于 2026-11-24；以官网为准):** AEA members US$200 (high-income country) / US$100 (middle-income) / US$0 (low-income); nonmembers US$300 / US$200 / US$0. Paid by credit card at submission. Papers **rejected without review receive a 50% refund**.
- **Publication fee:** US$15 per typeset page, assessed at page proofs (applies to papers first submitted on or after Feb 1, 2024; 检索于 2026-11-24；以官网为准).
- **Author-anonymized submission (changed fall 2026):** the AEA has launched a three-year randomized controlled trial of author-anonymized ("double-blind") reviewing across the AER, AER: Insights and the four AEJs, and the submission guidelines now require **anonymized manuscripts** for every submission: title and abstract at the top of the first page; author names, affiliations, contact information and the acknowledgement footnote in a separate PDF labelled "title page"; self-citations by name, never "my/our previous work"; no identifying locations, IRB approvals, or personal-website links; no RCT-registration entry in the reference list; supplementary appendix and response letters anonymized. The editorial-policy page still describes single-blind review (the control arm), so plan for either.
- **Other rules:** JEL codes customary (not stated as a rule on the current AEJ pages). AI cannot be listed as an author, and any AI use in preparing the manuscript, including drafting or editing text, must be briefly described during submission. A cover letter is not required — use it (preferably the form field) only for coeditor conflicts or data-access limitations.
- **Data & code:** governed by the AEA Data and Code Availability Policy; the **AEA Data Editor** runs a pre-publication reproducibility check; deposit at the AEA Data and Code Repository on openICPSR (see `aejmac-replication-package`). Field experiments register in the AEA RCT Registry.

## Preflight checklist

### Format & length
- [ ] One **anonymized PDF**: title + abstract on page 1; no names, affiliations, or acknowledgement footnote; self-citations by name; no identifying sites, IRB approvals, or personal links
- [ ] Separate **"title page" PDF**: title, authors, affiliations, contact information, acknowledgement footnote
- [ ] **Abstract ≤100 words**
- [ ] **JEL codes** and keywords included (customary)
- [ ] Within length guidance: ~40 pages (11pt, 1.5 spacing) / ~45 pages (12pt, 1.5 spacing), **including** figures, tables, references, and appendices (检索于 2026-11-24；以官网为准)
- [ ] Tables report standard errors in parentheses with **no significance asterisks** (AEA style guide)
- [ ] Figures/tables legible after AEA two-column typesetting; IRFs have stated confidence bands
- [ ] Online appendix prepared for material beyond the page limit

### Files & fees for the AEA system
- [ ] Anonymized manuscript PDF, title-page PDF, and anonymized supplemental appendix if any
- [ ] Fee tier determined (member/nonmember × income tier); card ready
- [ ] Replication package staged for the post-acceptance Data Editor check (incl. simulation/calibration code)
- [ ] Field experiment: AEA RCT ID entered in the submission form (registration cited on the title page, not in the anonymized reference list)

### Declarations
- [ ] **Separate disclosure statement from each coauthor** (AEA policy; US$10,000 interested-party threshold; all funding sources, in-kind support, positions)
- [ ] Confirmed the paper is original and not under review elsewhere
- [ ] AI not listed as an author; any AI use described in the submission form

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue aej-macroeconomics-skills   # from a clone of the AJS repository
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

- Abstract over 100 words (a hard AEJ: Macro constraint, tighter than most journals)
- Missing JEL codes (customary, even though the current pages do not state them as a rule)
- Forgetting a per-coauthor disclosure statement (each coauthor, separately)
- Overrunning the ~40-page guidance instead of moving material to the online appendix
- Treating the $15/page proof fee as a submission-time charge
- Leaving author names, affiliations, the acknowledgement footnote, or "our previous work" in the manuscript PDF now that submissions must be anonymized
- Using significance stars in tables (the AEA style guide says not to)

## Output format

```
【Format】anonymized PDF + separate title page; JEL + keywords? [Y/N]
【Abstract】≤100 words? [Y/N] (current: __)
【Length】within ~40pp guidance (incl. appendices) or appendix split planned? [Y/N]
【Fee】member/nonmember × income tier determined; card ready? [Y/N]
【Disclosure】separate statement per coauthor; $10k threshold checked? [Y/N]
【Data/code】replication package staged for the AEA Data Editor? [Y/N]
【Next step】submit via ScholarOne → aejmac-referee-strategy for what to expect
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — 8-section pre-submission self-check
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official AEA URLs behind every fact
