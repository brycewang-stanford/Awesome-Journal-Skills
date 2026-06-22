---
name: ijoc-submission
description: Use when running the final pre-submission preflight for an INFORMS Journal on Computing (IJOC) submission via ScholarOne — page limit, LaTeX template, single-blind rules, technical-area choice, and the GitHub code/data deposit. Final checks; it does not draft content.
---

# Submission Preflight (ijoc-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit on ScholarOne
- Unsure which files, area, and declarations the IJOC submission expects
- Confirming the **25-page limit**, the LaTeX template, and the single-blind format are met
- Preparing (or stubbing) the **IJOC GitHub Software and Data Repository** deposit

## Process facts (source map refreshed 2026-06; re-confirm on the official INFORMS pages)

- IJOC is the **INFORMS** journal at the **OR/MS ↔ computer-science** interface; content is hosted on **INFORMS PubsOnline**. Submission is through **ScholarOne Manuscripts** at `mc.manuscriptcentral.com/ijoc`, a six-step process.
- **Technical area:** you select **one of the journal's 10 technical areas**; the **Area Editor** judges suitability and **desk-rejects roughly 40%**, then assigns an associate editor whose identity is **never disclosed** to authors.
- **Review model:** **single-blind** — reviewers see author names; the title page carries all authors and affiliations. (Do not blind the manuscript.)
- **Length policy (effective May 2025):** main manuscript **≤25 pages including all references, tables, and figures**, plus up to **10 pages of appendices**; longer appendices go to online supplements. Code/data are hosted on GitHub and excluded from the page count.
- **Abstract:** **≤300 words, no formulas or mathematical notation.**
- **Format:** single-column, **1.5-spaced, 12-point font, 1-inch margins**; **LaTeX strongly preferred** (`JOC-template.tex` in the Author Portal); MS Word accepted; PDF for the main document.
- **Editor-in-chief:** **David L. Woodruff** (UC Davis), succeeding Alice E. Smith (term ended 2025-12-31); confirmed via INFORMS (检索于 2026-06-22；投稿前以官网为准).
- **Open access:** optional INFORMS Open Option, **US$3,000** assessed at production (not a submission fee); standard publication has no APC.

## Preflight checklist

### Format & length
- [ ] Single-column, **1.5-spaced**, **12pt**, **1-inch margins**; pages numbered
- [ ] Main paper **≤25 pages** incl. references/tables/figures; appendices **≤10 pages** (longer → online supplement)
- [ ] **Abstract ≤300 words, no formulas**; covers questions/challenges → methodology/results → importance
- [ ] LaTeX `JOC-template.tex` used (or compliant Word); main document as PDF
- [ ] Algorithms as numbered pseudocode; equations numbered; notation defined once
- [ ] **No significance asterisks**; statistical comparisons reported in text/profiles

### Area, files & ScholarOne
- [ ] One of the **10 technical areas** chosen to match the *method*; justified in the cover letter if straddling
- [ ] Title page with all authors/affiliations (single-blind — not anonymized)
- [ ] Cover letter; supplemental files (long proofs, extra tables) designated as supplements
- [ ] Conflict-of-interest disclosure and ethical certifications completed in the six-step form

### Reproducibility deposit (IJOC GitHub)
- [ ] Repo started from the template `github.com/INFORMSJoC/2019.0000`; placeholders → manuscript ID
- [ ] Root files present: **README.md** (with `## Cite` first subheading), **LICENSE**, **AUTHORS**
- [ ] `src/ data/ scripts/ results/ docs/` organized; dependencies pinned (`requirements.txt`/`Manifest.toml`)
- [ ] README replication path regenerates each table/figure; results match the manuscript
- [ ] Aware that acceptance snapshots a tag `vXXXX.YYYY` and mints a code DOI `…​.cd`

## Anti-patterns

- Submitting to a technical area that mismatches the method → fast Area-Editor desk reject
- Anonymizing the manuscript as if double-blind (IJOC is single-blind)
- Exceeding 25 main pages by leaving full proofs and raw result tables in the body
- A formula in the abstract, or significance asterisks in tables
- Treating the GitHub deposit as an after-acceptance chore; arriving with no reproducible artifact
- Mistaking the US$3,000 Open Option for a required submission fee

## Output format

```text
【Format】1.5-spaced / 12pt / 1-in margins / ≤25pp main (+≤10 appendix)? [Y/N]
【Abstract】≤300 words, no formulas? [Y/N]
【Area】one of 10, matched to method? [area]
【Single-blind】title page with authors, not anonymized? [Y/N]
【Exhibits】no significance asterisks; tests in text/profiles? [Y/N]
【Deposit】template/README+Cite/LICENSE/AUTHORS/scripts ready? [Y/N]
【Next step】submit via ScholarOne → ijoc-review-process for what to expect
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — submission self-check
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — lightweight manuscript scaffold
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official URLs and volatile facts
