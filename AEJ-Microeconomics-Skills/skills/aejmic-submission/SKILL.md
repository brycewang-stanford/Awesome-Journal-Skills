---
name: aejmic-submission
description: Use when running the final pre-submission preflight for the American Economic Journal: Microeconomics (AEJ: Micro) via the AEA ScholarOne system — the author-anonymized manuscript and title page, the 100-word abstract, JEL classification, the submission fee, format, and the AEA Data and Code Availability Policy. Final checks; it does not draft content.
---

# Submission Preflight (aejmic-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit on the AEA system
- Unsure which files, codes, and fees the AEA submission expects
- Confirming the abstract, format, and data/code requirements are met
- Verifying the data/code availability requirements before submission

## Process facts (re-verified 2026-11-24 on the official AEA pages；以官网为准)

- AEJ: Micro is one of the AEA's four field journals (founded 2009 — 待核实, quarterly); submission is through **ScholarOne Manuscripts** as a PDF (under 10 MB when reasonably possible). Editor (re-verified 2026-11-24): **Navin Kartik** (Yale, since Fall 2025); coeditors Ali, Bonatti, Rozen, Xu — re-verify the masthead before submission.
- **Author-anonymized submission (changed fall 2026):** the AEA has launched a three-year randomized controlled trial of author-anonymized ("double-blind") reviewing across the AER, AER: Insights and the four AEJs, and the submission guidelines now require **anonymized manuscripts** for every submission: title and abstract at the top of the first page; author names, affiliations, contact information and the acknowledgement footnote in a separate PDF labelled "title page"; self-citations by name, never "my/our previous work"; no identifying locations, IRB approvals, or personal-website links; no RCT-registration entry in the reference list; supplementary appendix and response letters anonymized. The editorial-policy page still describes single-blind review (the control arm), so plan for either.
- **Abstract:** **100 words or fewer** (required). JEL classification customary per AEA practice (not stated as a rule on the current AEJ pages); keywords expected.
- **Length:** strongly recommended **not to exceed 45 pages**, including figures, tables, references, and in-paper appendices, at a minimum of **12-point font, 1.5 spacing, 1-inch margins** (references may be single spaced); all pages numbered. Average article: 36–37 typeset pages.
- **Cover letter:** not required — use it (preferably the form field) only for coeditor conflicts or data-access limitations. Any AI use in preparing the manuscript must be briefly described during submission.
- **Submission fee:** AEA members **$200** (high-income) / **$100** (middle-income) / **$0** (low-income); nonmembers **$300 / $200 / $0**; scaled by membership and country income classification. Papers rejected without review are refunded **50%**. (Amounts **volatile** — confirm on the AEA submissions page.)
- **Publication fee:** **$15 per typeset page** assessed at page proofs (papers first submitted on or after Feb 1, 2024) — distinct from the submission fee.
- **Data & code:** the **AEA Data and Code Availability Policy** (administered by the **AEA Data Editor**, Lars Vilhuber) applies to papers with **empirical work, simulations, or experimental work**; deposit to the **AEA Data and Code Repository (openICPSR)**; verified before acceptance. Pure-theory papers still deposit numerical/simulation code.
- **House style:** AEA style; proofs in appendix where long; numerical examples to illustrate; report **standard errors in parentheses (the style guide says not to use significance asterisks)** for empirical/experimental work; tables at most 9 columns.
- **What to expect after submit:** a co-editor screens for fit and may **desk-reject** without referees; otherwise expert referees verify the proofs. Choose JEL codes that route the paper to a co-editor in the right subfield (see `aejmic-referee-strategy`).

## Preflight checklist

### Front matter & format
- [ ] **Abstract ≤100 words** (hard limit)
- [ ] **JEL codes** and keywords present (customary)
- [ ] Within the 45-page recommendation (≥12-point, 1.5 spacing, 1-inch margins, pages numbered), incl. references and in-paper appendices
- [ ] Numbered propositions/theorems; proofs self-contained (main text or appendix)
- [ ] Figures/tables legible; **no significance asterisks** for inference — report SEs / coverage sets
- [ ] AEA/LaTeX formatting per the current author guidelines
- [ ] Manuscript PDF **anonymized**: title + abstract on page 1; no names, affiliations, or acknowledgement footnote; self-citations by name, never "our previous work"
- [ ] Separate **"title page" PDF**: authors, affiliations, contact information, acknowledgement footnote (funding, thanks)

### Files, fees & data
- [ ] Anonymized manuscript PDF + title-page PDF + anonymized supplemental appendix if any
- [ ] Submission fee ready (member $200/$100/$0 by income; nonmember higher) — confirm current amount
- [ ] Aware of the $15/typeset-page publication fee at proofs (not now)
- [ ] Data/code deposit prepared if the paper has empirical/simulation/experimental work; theory-only numerics code prepared too
- [ ] Experiment materials (instructions, code, pre-registration) ready

### Declarations
- [ ] One Disclosure Statement PDF per coauthor (AEA policy; submissions without them are not reviewed)
- [ ] Confirmed not under review elsewhere; AI not listed as an author; any AI use described in the submission form
- [ ] Verified the venue (AEJ: Micro, not AEJ: Applied or a specialist theory journal)

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue aej-microeconomics-skills   # from a clone of the AJS repository
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

- Abstract over 100 words, or missing JEL codes
- Significance asterisks, or a load-bearing proof exiled to supplementary files
- Treating the data/code deposit as a post-acceptance afterthought (the Data Editor checks before acceptance)
- Confusing the submission fee with the later $15/page publication charge
- Leaving author names, affiliations, the acknowledgement footnote, or "our previous work" in the manuscript PDF — submissions must now be anonymized

## Output format

```
【Front matter】anonymized PDF + separate title page; abstract ≤100 words + JEL + keywords? [Y/N]
【Format/style】numbered results; proofs self-contained; no asterisks? [Y/N]
【Fee】AEA submission fee ready (amount confirmed)? [Y/N]
【Data/code】deposit prepared (incl. theory-only numerics)? [Y/N]
【Declarations】disclosure; not under review; AI not an author? [Y/N]
【Next step】submit via AEA system → aejmic-referee-strategy for what to expect
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — 8-section pre-submission self-check
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official AEA/AEJ: Micro URLs behind every fact
