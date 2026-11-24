---
name: jmgmt-submission
description: Use when running the final pre-submission preflight for the Journal of Management (JOM) via SAGE/ScholarOne — the 50-page limit, 15-word title, 250-word abstract, masked review, the anonymized data transparency table, the JOM Style Guide, the no-stars reporting rule, the AI-use disclosure, and required declarations. Final checks; it does not draft content.
---

# Submission Preflight (jmgmt-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit on the SAGE/ScholarOne portal
- Unsure which files JOM's submission expects (masked manuscript, title page, transparency table)
- Confirming the format and length rules are JOM-compliant
- The paper has data overlap with the authors' other work and you must disclose it correctly

## Process facts (source map re-verified 2026-11-24; re-confirm on the SAGE JOM author-instructions page)

- JOM is the **Southern Management Association's** journal, published by **SAGE**; new manuscripts are submitted through SAGE's online system (**ScholarOne Manuscript Central**, 待核实 exact portal label). Editor-in-Chief: **Christopher C. Rosen (University of Arkansas, Sam M. Walton College of Business)** since **2026-07-01**, succeeding Cynthia E. Devers (Virginia Tech). Re-verified 2026-11-24 (SAGE author instructions now direct queries to Rosen); confirm the current editor on the live SAGE/SMA pages before submission (以官网为准).
- **Length:** a **50-page limit that includes everything** — text, notes, references, non-supplementary appendices, tables, and figures; 12-pt Times New Roman, double-spaced throughout, 1-inch margins (re-verified 2026-11-24；以官网为准). **Initial (first) submissions may not include any online supplement material** — overflow must be cut, not offloaded.
- **Title and abstract caps entered in the portal:** **title ≤ 15 words**, **abstract ≤ 250 words**; the abstract goes only in the portal field — not in the main document — and no title page goes in the main document (re-verified 2026-11-24；以官网为准).
- **Masked (double-blind) review:** the manuscript must be **anonymized** — no author names, no identifying self-citations in the open, no acknowledgments revealing identity.
- **Data transparency table (distinctive):** JOM requires an **anonymized data transparency table** disclosing any actual or potential overlap between the focal manuscript's data and the authors' other published or in-process papers. Prepare this so it preserves masking during review.
- **Style:** the **JOM Style Guide** — JOM's own author–date format ("Barney, J. 1991. Title. *Journal of Management*, 17: 99-120."), not APA 7th; notes in a FOOTNOTES section after the references; acknowledgements typed into the portal, not the manuscript (re-verified 2026-11-24；以官网为准).
- **Quantitative reporting:** authors attest to JOM's Reporting Requirements — SEs and test statistics with **precise p values, no significance stars**; a full correlation matrix with means, SDs, reliabilities and Ns.
- **AI policy:** if AI was used for writing, images/graphics, or data collection/analysis, name the tool and how it was used **in the Methods section of all versions** of the paper.
- **Article types accepted:** empirical, theoretical, and **review/meta-analytic** articles (the latter feature in the biannual Review Issues).

## Preflight checklist

### Format & length
- [ ] Within the **50-page** inclusive limit (text + notes + references + tables + figures)
- [ ] **Title ≤ 15 words**; **abstract ≤ 250 words**
- [ ] **JOM Style Guide** citations, reference list, headings; bias-free language
- [ ] Tables/figures formatted per the JOM Style Guide; exact p values, no stars; **no online supplement attached** (first submission)

### Masking & transparency
- [ ] Manuscript fully **anonymized** (no names, no identity-revealing self-citations/acknowledgments, scrubbed file metadata)
- [ ] **Anonymized data transparency table** completed (data overlap with authors' other papers disclosed)
- [ ] Separate **title page** (with full authorship/affiliations) uploaded as a non-masked file

### Declarations & files
- [ ] Masked main manuscript (PDF/Word per portal)
- [ ] Title page; data transparency table; cover letter
- [ ] Conflict-of-interest / funding disclosure; ethics/IRB statement for human-subjects data
- [ ] Confirmed not under review elsewhere; AI not listed as an author; any AI use described in the Methods section
- [ ] (Meta/review) PRISMA-style flow inside the 50 pages; coding protocol ready to share if requested in review

## The data transparency table, done right

This is the JOM submission step most authors get wrong. The table exists so reviewers and editors can see whether the focal manuscript's sample, variables, or analyses overlap with the authors' other published, in-press, or under-review papers — a guard against "salami slicing" and undisclosed double-publication. Build it so that:

- Each related paper is listed with its constructs, sample, and what is shared vs. unique relative to the focal manuscript.
- The disclosure is written to **preserve masking** — describe the overlapping work without naming the authors (e.g., "a related study using the same 2023 employee panel, currently under review elsewhere").
- Genuinely non-overlapping work need not be padded in; the point is honest disclosure of *overlap*, not a CV.

A complete, mask-safe transparency table signals integrity and removes a common reason editors hold or return a submission.

## Last-mile preflight sequence

1. Run the length count *including* references, tables, and figures — not just body text.
2. Strip identity from the manuscript file *and* its document metadata; move all author info to a separate title page.
3. Verify title (≤15 words) and abstract (≤250 words) match what you will paste into the portal fields.
4. Confirm the JOM Style Guide reference format throughout (not APA 7th); spot-check the reference list against in-text citations; replace any significance stars with exact p values.
5. Complete and mask-check the data transparency table.
6. Attach declarations (COI, funding, ethics/IRB) and the cover letter.

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue journal-of-management-skills   # from a clone of the AJS repository
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

- Submitting an **un-anonymized** manuscript to a masked-review journal (instant friction)
- **Omitting the data transparency table**, or filling it in a way that breaks masking
- Blowing the **50-page** limit by counting only text and forgetting tables/references
- Title or abstract over the **15-word / 250-word** caps
- Mixed citation style, or APA 7th instead of the JOM Style Guide format
- Significance stars in tables, or an online supplement attached to a first submission
- Leaving identifying metadata in the file even after scrubbing names from the body
- Treating JOM like AMJ on submission mechanics without checking JOM's own SAGE page

## Output format

```
【Length】≤50 inclusive pages (text+notes+refs+tables+figs)? [Y/N]
【Title/abstract】≤15 words / ≤250 words? [Y/N]
【JOM Style Guide】citations + references + headings; no stars? [Y/N]
【Masking】fully anonymized; title page separate? [Y/N]
【Transparency table】completed and mask-safe? [Y/N]
【Declarations】COI / funding / ethics / not-elsewhere? [Y/N]
【Next step】submit via SAGE/ScholarOne → jmgmt-review-process
```
