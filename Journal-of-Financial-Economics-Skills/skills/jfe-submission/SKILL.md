---
name: jfe-submission
description: Use when running the final pre-submission preflight for a Journal of Financial Economics (JFE) manuscript — formatting, anonymity, references, exhibits, code/data deposit, the editorial system, and the submission fee. Checks submission readiness; it does not revise the science.
---

# Submission Preflight (jfe-submission)

## When to trigger

- "We are submitting this week"
- Final check before pressing submit in the editorial system
- Unsure which files and statements the system requires

## The JFE-specific facts (verify on jfinec.com before relying)

> ACCURACY NOTE (re-verified 2026-11-23 on jfinec.com): the **US$850** fee, the submission-file rules below, and the masthead are current — **Editor-in-Chief Toni M. Whited (U. Michigan); Co-Editors Dimitris Papanikolaou, Philipp Schnabl, Nikolai Roussanov**. Re-verify before submission.

- **Portal:** submit through **Editorial Manager** at **editorialmanager.com/finec** (the JFE database code is `finec`, not the journal's old abbreviation).
- **Submission fee:** **US$850** for an initial submission (re-verified 2026-11-23, unchanged), paid at submission and largely non-refundable. **No fee** for a revise-and-resubmit. Referees who report on time earn **submission rights** that cut the fee (roughly US$567 with one right, US$283 with two, **$0 with three**). Only **US$400** is refunded on a desk reject (capped at four desk-reject refunds per author per calendar year), and the **whole fee is refunded if a decision takes more than 120 days**.
- **Required files (jfinec.com/submissions):** a **manuscript PDF without identifying information** (no author information or acknowledgments; title + abstract), a separate **title page PDF** (title; name, affiliation and email of each author; acknowledgments footnote), and **conflict-of-interest disclosure statements for all authors gathered in one PDF** uploaded separately — required even when there is nothing to disclose (say so explicitly), and again at resubmission. **Do not upload anything as "Supplementary Material"** — papers that do are returned.
- **Abstract:** **100 words maximum.** Include JEL codes and keywords (good practice; jfinec.com does not itself state a JEL/keyword rule).
- **Format:** **double-spaced, 12-point-or-larger font, at least one-inch margins.**
- **References:** JFE uses an **author-date (name-year)** in-text style with a reference list — not a numbered style.
- **Internet/online appendix:** JFE expects any online appendix **attached to the end of the main manuscript file** at submission (a JFE quirk — it is not always a wholly separate upload). Still number it as its own IA series.
- **Code & data:** for papers originally submitted on/after **1 July 2021**, **code and non-proprietary data are mandatory** at acceptance, deposited to **Mendeley Data** (or a domain repository) and linked from ScienceDirect. Any exemption (e.g., for proprietary CRSP/Compustat data) must be **requested in the cover letter of the initial submission** to the editor-in-chief.

## Pre-submission checklist

### Manuscript & format
- [ ] Title page PDF separate from the anonymized manuscript PDF (jfinec.com: the manuscript PDF "must be anonymous")
- [ ] Abstract **<= 100 words**, result-forward; JEL codes and keywords included
- [ ] **Double-spaced, 12-pt+ font, >= 1-inch margins**
- [ ] Sections, tables, and figures numbered consistently; every in-text reference resolves
- [ ] Equations numbered; notation consistent throughout
- [ ] **Author-date** reference style (name-year), per the JFE guide

### Anonymity (required by jfinec.com/submissions; re-verified 2026-11-23)
- [ ] No author-identifying content in the manuscript body
- [ ] Self-citations phrased neutrally, not "in our prior work"
- [ ] Acknowledgments and funding moved off the anonymized file
- [ ] File metadata (document properties) scrubbed of author names

### Exhibits & Internet Appendix
- [ ] Main-text exhibits triaged; the long tail is in the Internet Appendix
- [ ] Every "untabulated" / "see Internet Appendix" pointer resolves
- [ ] Internet Appendix numbered in its own IA series and **appended to the end of the main file** per JFE practice

### Code & data deposit (JFE policy)
- [ ] Code + non-proprietary data prepared for **Mendeley Data** deposit (mandatory for post-2021 submissions)
- [ ] Proprietary-data exemption, if needed, **stated in the cover letter**
- [ ] A reader could in principle reproduce the headline tables from the deposit

### References
- [ ] Every in-text citation appears in the reference list and vice versa
- [ ] Recent top-3 finance work on the topic is cited
- [ ] No broken DOIs / incomplete entries

### Editorial system & fee
- [ ] Submit via **editorialmanager.com/finec**
- [ ] **US$850** fee ready (or submission-rights code applied); know the desk-reject (US$400) and 120-day refund rules
- [ ] Cover letter states the contribution and fit briefly; any data/code exemption requested here; suggested/opposed referees as the system allows
- [ ] Conflict-of-interest disclosure statement for **every** author, combined into one PDF and uploaded separately (explicit "nothing to disclose" if so); prior-presentation notes on the title page
- [ ] Nothing uploaded as "Supplementary Material"; notes to referees (resubmissions) attached at the end of the paper, anonymized

## Submission-system pointers

- Confirm the current fee, portal, file-size limits, and accepted formats on jfinec.com before uploading — these change.
- Have the anonymized manuscript (with the appended online appendix), title page, and code/data ready.
- Double-check that the version uploaded is the final one (not a tracked-changes draft).

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue jfe-skills   # from a clone of the AJS repository
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

- Submitting a manuscript whose metadata still names the authors
- "See Internet Appendix" pointers that go nowhere
- Assuming last year's fee — it is US$850 unless you hold submission rights
- Forgetting to request a data/code exemption in the cover letter when you rely on proprietary data
- Reference list in a numbered (not author-date) style
- Uploading a draft with visible tracked changes or comments

## Output format

```
【Anonymity】pass / fix: [...]
【Format】abstract <=100w? double-spaced? author-date refs? yes/no
【Exhibits + IA】pointers resolve? IA appended? yes/no
【Code/data deposit】Mendeley-ready? exemption in cover letter? yes/no
【References】in-text == list? yes/no
【Fee & portal】US$850 (or rights code) ready; finec portal confirmed? yes/no
【Cover letter】contribution + fit stated? yes/no
【Next】await decision -> jfe-referee-strategy (pre-empt) / jfe-rebuttal (on R&R)
```

## Resources

- [`templates/manuscript_template.md`](templates/manuscript_template.md) — JFE-style manuscript skeleton (abstract, variable-definition table, exhibit and reference conventions)
- [`templates/checklist.md`](templates/checklist.md) — full pre-submission self-check across format, anonymity, exhibits, code/data, references, and system
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — finance data sources (CRSP / Compustat / TAQ / WRDS) and Stata / R / Python packages
