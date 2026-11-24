---
name: psychbull-submission
description: Use when running the final pre-submission preflight for Psychological Bulletin via APA Editorial Manager — masking, the ≤ 250-word abstract, APA 7th style, MARS/PRISMA/JARS checklists, and the transparency package. Final checks; it does not draft content.
---

# Submission Preflight (psychbull-submission)

The last check before pressing submit on **APA Editorial Manager**. Psychological Bulletin uses
**masked review**, so the most common avoidable failure is an under-masked manuscript — and the second
is a synthesis whose MARS/PRISMA reporting is incomplete. Verify volatile specifics on the official APA
page before relying on them.

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure which files/metadata Editorial Manager expects
- Confirming masking, the abstract cap, and the MARS/PRISMA checklist are satisfied

## Process facts (re-verified 2026-11-24 on the APA submission-guidelines page unless marked)

- **Owner / publisher:** American Psychological Association (APA).
- **Portal:** APA **Editorial Manager** (`editorialmanager.com/bul`).
- **Review model:** **masked (double-masked)** — author names, affiliations and contact details go in the
  portal's cover-letter box, not the file; no author clues in the file.
- **Editor:** **Stefan G. Hofmann** (Philipps-Universität Marburg) handles **all new submissions in 2026**
  as incoming (2027) editor; Blair T. Johnson is the outgoing editor.
- **What it publishes:** research **syntheses** (systematic reviews, meta-analyses, meta-reviews,
  meta-synthesis, qualitative reviews) — **not** original primary studies; original theory →
  *Psychological Review*.
- **Abstract:** **≤ 250 words**, on a separate page (stated on the 2025 guidelines; the March-2026 page
  no longer restates a limit — 待核实, keep 250 as the safe default).
- **Public Significance Statement:** **required** — 2–3 plain sentences on the abstract/keywords page,
  not lifted from the manuscript.
- **Style:** APA Publication Manual, **7th edition**.
- **Reporting:** **JARS / MARS** required (TOP Level 2); **PRISMA 2020** is an acceptable replacement.
- **Transparency (since Feb 1 2022):** **TOP Level 2** for citation, data, code, materials, reporting
  standards, study and analysis-plan preregistration (replication: Level 1). A Method subsection
  **"Transparency and openness"** states data/code/materials availability, preregistration (+ any
  deviations), **generative-AI use (or none)**, and the reporting guideline followed; supply
  **database, codebook, scripts** (anonymized links) for reviewers.
- **Fee:** submitting for peer review is **free**; an APC applies only to gold open access.

## Preflight checklist

### Fit & type
- [ ] It is a **synthesis**, not an original study or pure theory (else wrong journal)
- [ ] Synthesis type declared (meta-analysis / systematic / meta-review / qualitative)

### Masking
- [ ] No author names, affiliations, or acknowledgments in the manuscript
- [ ] Self-references neutralized; easily identified self-citations removed from the reference list
- [ ] **File metadata stripped** (document properties)
- [ ] PROSPERO/OSF appendix anonymized (no registration number or author names)

### Reporting & format
- [ ] Abstract ≤ 250 words on a separate page
- [ ] **Public Significance Statement** (2–3 plain sentences) on the abstract/keywords page
- [ ] APA 7th-edition formatting throughout
- [ ] **MARS / PRISMA / JARS** checklist completed for the synthesis type
- [ ] PRISMA flow diagram + forest/funnel exhibits present (see `psychbull-tables-figures`)

### Transparency & compliance
- [ ] "Transparency and openness" Method subsection: availability, preregistration + deviations, AI use, PRISMA/MARS followed
- [ ] Preregistration stated with access location (also in the author note on acceptance)
- [ ] Database + codebook + scripts deposited with a DOI; availability statement drafted
- [ ] Ethics/attribution compliant; original synthesis (no plagiarized text)

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue psychbull-skills   # from a clone of the AJS repository
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

- Author identifiers left in text, acknowledgments, or file metadata (breaks masking)
- A PROSPERO number visible in the masked appendix
- Abstract over 250 words
- Submitting an original empirical study or pure theory to the wrong venue
- Missing MARS/PRISMA checklist or an undeposited database

## Desk-reject patterns at the APA review flagship

Most avoidable failures at Psychological Bulletin are caught before peer review — at the editor's desk.
The recurring desk-reject patterns at the APA's flagship synthesis journal:

| Desk-reject pattern | Why it triggers | Pre-submission fix |
|---------------------|-----------------|--------------------|
| Wrong venue | A primary empirical study or pure theory was submitted | Confirm it is a synthesis; route theory to *Psychological Review* |
| Broken masking | Author names, affiliations, or file metadata remain | Strip identifiers from text and document properties |
| Visible registration | PROSPERO number/names left in the masked appendix | Anonymize the appendix before upload |
| Over-long abstract | Abstract exceeds 250 words | Trim to the cap on a separate page |
| Missing reporting | No MARS/PRISMA/JARS checklist or PRISMA diagram | Complete the checklist for the synthesis type |
| No deposited data | "Available on request" instead of a DOI'd package | Deposit database, codebook, scripts before submitting |

## Worked vignette — the final preflight pass

*Illustrative figures only.* The self-affirmation synthesis (k = 42, g = 0.34) clears preflight when:

- **Fit** is confirmed as a meta-analysis of existing trials, not new data.
- **Masking** is verified in the text, the neutralized self-citations, the stripped file metadata, and
  the anonymized OSF/PROSPERO appendix.
- **Abstract** is 218 words on its own page, stating k, the pooled g and CI, the moderator, and the
  robustness bottom line.
- **Reporting**: the MARS and PRISMA checklists are complete and the PRISMA diagram plus forest/funnel
  exhibits are attached.
- **Transparency**: the deposited database, codebook, and scripts carry a DOI and the availability
  statement is drafted. (TOP Level 2 re-verified 2026-11-24; submission is free.)

## Referee/editor pushback → venue-specific fix

- *"This appears to be a primary study."* → Reframe only if it genuinely synthesizes a literature;
  otherwise it is the wrong journal.
- *"Reviewer could infer the authors."* → Remove residual self-references and metadata; re-anonymize the
  registration appendix.
- *"MARS checklist is missing."* → Attach the completed checklist matched to the synthesis type before
  resubmitting.

## Output format

```
【Fit】synthesis, not primary study/theory? [Y/N]
【Type】meta-analysis / systematic / meta-review / qualitative
【Masked】text + self-refs + metadata + PROSPERO appendix clean? [Y/N]
【Abstract】word count (≤ 250)
【MARS/PRISMA/JARS】checklist complete? [Y/N]
【Transparency】database+codebook+scripts deposited + prereg stated? [Y/N]
【Next】await decision → psychbull-rebuttal on R&R
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reference managers, masking, repository/deposit tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — Editorial Manager, masked review, abstract, MARS/PRISMA/JARS, TOP
