---
name: qje-submission
description: Use when running the final pre-submission preflight for the Quarterly Journal of Economics (QJE) via Editorial Express — single-PDF format, first-page author/word-count/abstract/JEL rules, author-date references, the no-fee policy, and supplementary files. Final checks; it does not draft content.
---

# Submission Preflight (qje-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit on Editorial Express
- Unsure which files Editorial Express expects at the initial-submission stage
- Confirming the single-PDF format, first-page requirements (names, word count, ≤250-word abstract, JEL codes), and author-date style are QJE-compliant
- Checking declarations and supplementary-materials requirements

## Process facts (official OUP instructions re-checked 2026-11-23; re-confirm specifics on the official page)

- QJE is published by **Oxford University Press** and **edited at Harvard University's Department of Economics** — the oldest English-language economics journal (founded **1886**) and one of the top-5. Source: academic.oup.com/qje; Wikipedia.
- Submission is through **Editorial Express** at `editorialexpress.com/qje` — the same Express platform used by several econ journals, *not* OUP's ScholarOne. Admin contact: `qje_admin@editorialexpress.com`.
- **There is no submission fee.** The official instructions, policies, and portal pages state none; this is unusual among top-5 journals (AER, JPE, REStud all charge); do not budget for one. QJE is hybrid open access, so an optional OA charge applies only *after* acceptance if you choose it.
- **Initial submission is a single PDF** containing the full manuscript, tables, figures, and appendices. **No Word files, no LaTeX source, no separate figure files** at this stage — source files are requested only after acceptance. Supplementary material may go in separate PDFs.
- **The manuscript is not anonymized.** The official instructions say the first page "must give the title of the article, contributor names," the corresponding author's full address and email, and the **total word count**; the title page carries the abstract (**no more than 250 words**, JEL codes at its end); funding and acknowledgments go in the first footnote (asterisk on the title). The instructions do not describe blind review.
- The editorial team — **five Editors, all at Harvard** (Robert J. Barro, Lawrence F. Katz, Nathan Nunn, Andrei Shleifer, and Stefanie Stantcheva, masthead re-verified 2026-06-22; re-check before submitting) — makes **fast desk decisions (roughly two weeks)**, the quickest among the top-5 flagships, so a clean, complete submission is part of clearing the first screen. (Acceptance runs ~1-4%; desk-reject ~60%+.)

## Preflight checklist

### Format & style

- [ ] One **single PDF** with manuscript, tables, figures, and appendices embedded (no Word, no separate figure files)
- [ ] References in **author-date (Chicago)** style; reference list alphabetical by surname
- [ ] Abstract **≤250 words** (official cap; ~150 reads best), no citations, **JEL codes at the end of the abstract**
- [ ] First page: title (all caps), contributor names, corresponding author's address + email, **total word count**
- [ ] Tables and figures numbered, called out in order, with self-contained notes
- [ ] Long manuscripts are fine (no hard page limit); an extensive **online appendix** is expected
- [ ] PDF compiles cleanly; figures legible at print resolution

### Author information (not anonymized)

- [ ] Contributor names centered on the first page; affiliations after the last line of text
- [ ] Funding sources and acknowledgments in the first footnote, marked by an asterisk on the title
- [ ] Self-citations still phrased neutrally ("Smith (2020) shows") — good style, though not an anonymity rule

### Files for Editorial Express

- [ ] Main manuscript as a single PDF (figures/tables/appendix embedded)
- [ ] Cover letter if any (optional in the portal; **required to flag proprietary data / exemption requests** under the data policy)
- [ ] Suggested / excluded referees prepared (expert, fair, conflict-free)
- [ ] Replication materials staged for the accepted stage (see qje-replication-package)

### Declarations

- [ ] Conflicts disclosed at submission (financial interests, connections, funding, relationships, direct competition) per the QJE Journal Policies page
- [ ] Funding and data-source disclosures prepared
- [ ] Confirmed the paper is not under review elsewhere

### Final content sanity

- [ ] Abstract states the finding with a number (see qje-writing-style)
- [ ] Identification diagnostics complete (see qje-identification, qje-robustness)
- [ ] No over-claiming beyond what the design supports

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue qje-skills   # from a clone of the AJS repository
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

- Uploading a Word file or separate figure files at initial submission (QJE wants one PDF)
- Mixed/inconsistent reference styles instead of clean author-date
- Stripping author names, contact details, or the word count from the first page as if QJE were double-blind (the instructions require them)
- Budgeting for a submission fee that does not exist at QJE
- A defensive, multi-page cover letter instead of a tight pitch the editors can read in two weeks
- Submitting a thin appendix to a journal that expects an extensive one

## Output format

```
【Single PDF】one file, all exhibits + appendix embedded? [Y/N]
【Reference style】author-date (Chicago), consistent? [Y/N]
【First page】names, contact, word count, abstract ≤250 + JEL codes? [Y/N]
【Files staged】PDF / cover letter / referees? [Y/N each]
【Declarations】conflict disclosure / funding footnote prepared? [Y/N]
【Content sanity】abstract states finding; identification complete? [Y/N]
【Next step】await ~2-week desk decision → qje-rebuttal on R&R
```

## Supplementary resources

- [`templates/manuscript_template.md`](templates/manuscript_template.md) — QJE-oriented manuscript skeleton (abstract, intro arc, design, exhibits, author-date references)
- [`templates/checklist.md`](templates/checklist.md) — 8-section pre-submission self-check
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — data sources and Stata/R/Python packages for credible-design empirical micro
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official QJE URLs behind every fact in this pack
