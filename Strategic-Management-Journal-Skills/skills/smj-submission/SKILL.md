---
name: smj-submission
description: Use when running the final pre-submission preflight for a Strategic Management Journal (SMJ) manuscript via Wiley Research Exchange — format, anonymization, files, and cover letter. Checks readiness; it does not write the paper or the rebuttal.
---

# Submission Preflight (smj-submission)

## When to trigger

- "I'm submitting tomorrow"
- Final check before clicking submit in Wiley Research Exchange (wiley.atyponrex.com/journal/SMJ)
- Unsure which files and metadata the system needs
- Preparing the cover letter and reviewer suggestions

## Before anything: verify the live guidelines

SMJ is published by **Wiley on behalf of the Strategic Management Society (SMS)**. New submissions go to SMJ's **Wiley Research Exchange** site (**wiley.atyponrex.com/journal/SMJ**); **ScholarOne Manuscript Central (mc.manuscriptcentral.com/smj)** is the legacy system for older papers. Per the SMJ Author Guidelines (last updated 23 May 2025; re-read 2026-11-23): "There is no fee for submitting manuscripts to SMJ. The only fee(s) associated with publishing an accepted article are optional" — open access (OnlineOpen, or free via a Wiley transformative agreement) is decided after acceptance. Page limits, fee/open-access options, and required statements are periodically updated. **Verify the current Author Guidelines on the official SMJ page** before submitting — do not rely on remembered numbers. Use this skill for the durable process; confirm volatile specifics yourself.

## Manuscript readiness

- [ ] Structure complete: intro, theory & hypotheses, methods, results, discussion, references
- [ ] Contribution to strategy theory is explicit in the introduction
- [ ] Endogeneity / identification is addressed in the body (the most-scrutinized element)
- [ ] **Two abstracts**: a *research summary* (≤125 words, stands alone, no citations) **and** a *managerial summary* (≤125 words, plain practitioner language). This dual-abstract requirement is distinctive to SMJ — AMJ/ASQ require only one abstract
- [ ] **Five (5) keywords** selected; length within the guidelines ("We strongly suggest that you limit the paper size to 40 pages, which includes figures and tables"; commentaries 20 pages; short research articles no more than 20 pages including title page, abstract, text, figures, tables, and references)
- [ ] Format: 12-point readable font (preferably Times New Roman), double-spaced body, single-spaced references, 1-inch margins, Letter page, **page numbers on**, left-justified text, American English
- [ ] Tables/figures self-contained; secondary material in an online supplement
- [ ] References in **APA 7th edition** author-date style (e.g., "(Collins, 2005a, 2005b)"); every in-text cite appears in the list and vice versa

## Anonymization (double-blind)

SMJ uses double-blind review. Before upload:

- [ ] Author names, affiliations, and acknowledgments removed from the manuscript file
- [ ] Self-citations phrased neutrally ("prior work shows (Author, 2021)"), not "in our earlier paper"
- [ ] Funding/acknowledgment details placed **only on the separate title page** (they move into the paper after acceptance)
- [ ] File metadata/properties scrubbed of author identity (Word files not rendered as PDF reach reviewers *with* their metadata)
- [ ] File names contain no author or institution names
- [ ] No identifying data-provider or proprietary-dataset language that reveals the team

## Files & metadata in Research Exchange

- [ ] Anonymized main manuscript (with embedded or separate exhibits per guidelines)
- [ ] Title page as a **separate file**: title, all authors' names, titles, emails, affiliations with addresses, a running head of up to 60 characters, acknowledgments
- [ ] Word (.doc/.docx) or LaTeX (.tex, with PDF as a supplemental file)
- [ ] Cover letter (see below)
- [ ] Online appendix / supplementary materials, if any
- [ ] Tell the Editor at submission if access to the data or code is restricted (SMJ may ask authors to give editors/reviewers access to data and programs during review); acknowledge any generative-AI use in the paper
- [ ] Requested Associate Editors or reviewers (no conflicts), named in the cover letter
- [ ] Correct article type selected (Research Article, Commentary, Prospective, or Special Issue Article)

## Cover letter

- **Required:** answer SMJ's three questions — (1) Has another manuscript from this same database been accepted or published in SMJ or elsewhere? (Yes/No) (2) Has another manuscript from this database been submitted to SMJ, or is one under review here or elsewhere? (Yes/No) (3) Does this manuscript cite all relevant published work of all authors? (Yes/No/N/A). A "yes" to 1-2 or "no" to 3 needs an explanation plus full citations of the related papers.
- If the paper is a close variant of one SMJ rejected before, say so and explain the differences.
- Brief: state the title, the strategy contribution in 2–3 sentences, and why **SMJ** (not the SMS siblings SEJ or GSJ) is the right outlet.
- Confirm the work is original, not under review elsewhere, and that all authors approve.
- Note any special-issue call you are responding to.
- Do not oversell or summarize the whole paper; a Co-Editor screens it first and an action editor reads the manuscript.

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue smj-skills   # from a clone of the AJS repository
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

- Submitting one abstract when SMJ requires both a research summary and a managerial summary
- Leaving author identity in metadata or acknowledgments under double-blind review
- A reference list still in a default citation-manager style, not APA author-date
- A cover letter that pitches generic "management" relevance instead of the strategy (competitive-advantage / performance) contribution
- Omitting the three required cover-letter answers on same-database papers and self-citation
- Routing an entrepreneurship- or internationalization-first paper to SMJ when SEJ or GSJ fits better

## Output format

```
【Guidelines verified on official page】yes / TO DO
【Dual abstracts】research summary [n≤125] / managerial summary [n≤125]
【Keywords】[5]
【Anonymization】pass / fix: [...]
【Files staged】main, title page, cover letter, supplement, statements
【Reference style】APA author-date conformed / fix
【Cover-letter 3 questions】answered / missing
【Article type】Research Article / Commentary / Prospective / special issue: [name]
【Reviewer suggestions】[n]
【Next step】smj-review-process (then smj-rebuttal on decision)
```

## Templates & resources

- [`templates/checklist.md`](templates/checklist.md) — full pre-submission self-check (format, anonymization, identification, files, cover letter)
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — SMJ-style manuscript skeleton (research + managerial summary, hypotheses, variable table, identification section, APA references)
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — strategy data sources (Compustat / CRSP / SDC / BoardEx / Orbis / patents) and Stata / R / Python packages
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official SMJ/SMS/Wiley URLs and what each verifies (editors, dual abstracts, page limits, reference style)
