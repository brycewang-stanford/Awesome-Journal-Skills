---
name: jleo-submission
description: Use when running the final pre-submission preflight for a Journal of Law, Economics, and Organization (JLEO) manuscript via the Editorial Express portal — files, anonymization, format, disclosures, and data-policy readiness for the Oxford University Press journal. Final checks; it does not draft content.
---

# Submission Preflight (jleo-submission)

## When to trigger

- "Submitting tomorrow" — last check before uploading to the Editorial Express portal
- Unsure which files and declarations JLEO's submission system expects
- Confirming format, anonymization, and house style are JLEO-compliant
- Confirming the paper is data-policy- and COPE-ready should it advance

## Process facts (检索于 2026-06-22；以官网为准 — re-confirm on academic.oup.com/jleo)

- JLEO is published by **Oxford University Press**; founded **1985 by Oliver E. Williamson and Jerry L. Mashaw**; triannual; Print ISSN **8756-6222**, Online ISSN **1465-7341**. Editor-in-Chief: **Andrea Prat** (Columbia), confirmed current as of **2026-06-22** (re-verify before submission).
- **Submission portal:** manuscripts are submitted through **Editorial Express** (editorialexpress.com/jleo), not ScholarOne or Editorial Manager. Verify the current upload form and accepted file types live.
- **Publication ethics:** JLEO is a **COPE** member and follows OUP's conflict-of-interest policy; editors recuse on conflicts. One paper under review at a time; no simultaneous submission elsewhere; AI cannot be listed as an author (per OUP policy).
- **Review model (single- vs. double-blind):** 待核实 — confirm on the JLEO submission-online page and anonymize accordingly before uploading.
- **Length / abstract limits, citation style, exact data-and-code policy, and any submission/page fees or open-access (licensing) charges:** 待核实 — JLEO's General Instructions point to a detailed submission page; read it and conform before submitting. OUP "encourages online licensing"; treat any open-access/licensing charge as separate from submission.

## Preflight checklist

### Format & front matter
- [ ] Manuscript in the format the Editorial Express form requires (PDF or as specified); pages numbered
- [ ] Title, abstract, keywords, and JEL codes present (confirm JEL requirement on the submission page — 待核实)
- [ ] If review is anonymous (待核实): author identifiers, acknowledgments, and identifying self-citations removed; a separate title page prepared
- [ ] References complete and in the JLEO/OUP house style (待核实 — match the journal's current style)

### Exhibits & content
- [ ] Tables/figures legible; the institutional comparison readable from each exhibit; notes self-contained
- [ ] Standard errors / confidence intervals reported on every estimate; clustering stated
- [ ] Online appendix prepared for supplementary material, kept separate from the main paper

### Files, policy & declarations
- [ ] All required files staged for the Editorial Express upload (manuscript, title page, appendix, any cover letter)
- [ ] Replication package buildable (jleo-replication-package); Data Availability Statement drafted; confirm the live data-and-code policy
- [ ] Disclosure / conflict-of-interest statement per OUP/COPE policy; funding sources listed
- [ ] Confirmed not under review elsewhere; AI not listed as an author
- [ ] A short cover letter stating the institutional/organizational contribution and why JLEO

## Anti-patterns

- Assuming ScholarOne/Editorial Manager — JLEO uses **Editorial Express**; uploading to the wrong system stalls the paper
- Guessing the blinding rule instead of confirming it and anonymizing correctly (待核实)
- Quoting a fee, word limit, or citation style from memory rather than the live JLEO pages
- Treating the replication package as an afterthought, then scrambling at revision
- A cover letter that does not state the organization/PPE payoff distinguishing JLEO from JLE

## Output format

```text
【Portal】Editorial Express upload ready (correct files/types)? [Y/N]
【Format & front matter】title/abstract/keywords/JEL + house style? [Y/N]
【Blinding】review model confirmed and MS anonymized accordingly? [Y/N / 待核实]
【Exhibits】SEs/CIs reported, notes self-contained, appendix separate? [Y/N]
【Data policy】replication package buildable + DAS drafted? [Y/N]
【Declarations】disclosure/COI done; not under review elsewhere; no AI author? [Y/N]
【Next step】submit via Editorial Express → jleo-rebuttal after the decision
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — submission self-check
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — lightweight manuscript scaffold
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official OUP/JLEO URLs and volatile facts
