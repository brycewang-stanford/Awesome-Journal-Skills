---
name: vldb-submission
description: Use when auditing a PVLDB submission before a monthly deadline, covering the mandatory abstract on the 25th, the CMT window, the 1st-of-month 5:00 PM Pacific cutoff, category and page-budget choice, single-blind cover-page requirements, the per-month and per-year author caps, and desk-reject hazards specific to VLDB.
---

# VLDB Submission

Run this in the two weeks before a PVLDB monthly deadline. VLDB research papers
enter through PVLDB (Proceedings of the VLDB Endowment), and the volume's own
guidelines page — not the conference site's summary — is the governing document.
Everything dated below was checked 2026-07-08 and re-verified 2026-11-24; reopen the live volume page first.

## The three clocks of one deadline

PVLDB splits a single submission across three dates, and missing the first one
kills the cycle quietly:

1. **20th of the prior month** — CMT opens for the cycle.
2. **25th of the prior month** — mandatory abstract (title, authors, abstract,
   subject areas) registered in CMT. No abstract, no paper slot.
3. **1st of the month, 5:00 PM Pacific Time** — full paper due. This is a
   Pacific-clock deadline, not AoE; for most of the world it lands in the
   middle of the night *before* the date your calendar shows. No extensions.

## Category and budget check

Pick the category deliberately — reviewers calibrate expectations to it:

| Category (VLDB 2026 cycle) | Body budget | What reviewers expect |
|---|---|---|
| Regular Research | 12 pp + refs | New technique with systems evidence |
| Experiment, Analysis & Benchmark | 12 pp + refs | Rigorous study; reproducibility evaluation is mandatory |
| Scalable Data Science | 8 pp + refs | Data-science pipeline at scale, practice-forward |
| Vision | 6 pp + refs | Agenda-setting argument, less evidence |

References are uncapped, but appendices and acknowledgements count inside the
budget. The four categories and budgets above are confirmed for Vol 20 (re-verified
2026-11-24); non-regular categories also need the category tag as a title suffix
(e.g. "[Vision]") in both the PDF and CMT. Reconfirm when Vol 21 is published.

## Identity and caps

- PVLDB review is **single-blind**: author names and affiliations belong on the
  paper. Do not strip them the way SIGMOD or ML venues require — an anonymous
  PVLDB submission is a formatting error, not a virtue. The Vol 20 wording:
  "VLDB is a single-blind conference. Therefore, authors MUST include their
  names and affiliations on the first page of the manuscript."
- Count coauthor load before promising a submission: Vol 20 caps each author at
  **two papers per month** and **twelve per year**, tracked against one CMT
  account per author; every submission also nominates a qualified author as a
  possible Light Load Reviewer.
- Submit supplemental code/data in a public archival repository (not a personal
  page) or explain why not; EA&B papers must link the full reproducibility
  package already at initial submission.
- Declare related concurrent submissions by the same authors, cited as
  "under submission".
- Declare conflicts accurately in CMT; the review board assignment runs on them.

## Pre-deadline audit sequence

```text
[ ] Live volume identified (Vol 20 on 2026-11-24) and its guidelines reopened
[ ] Abstract registered in CMT before the 25th, title/author list final
[ ] Category chosen; page budget measured with appendix included
[ ] Volume template applied unmodified; fonts legible at print size
[ ] Author names and affiliations present (single-blind), conflicts declared
[ ] Caps checked for every author, not just the lead
[ ] Artifact URL decided: include now or forfeit the availability signal
[ ] Deadline converted to your local time from 5:00 PM PT on the 1st
```

## What draws a desk rejection here

- Overrunning the category budget or squeezing with template edits.
- Submitting to a closed cycle because the abstract step was missed.
- A cover page missing authors, or CMT metadata contradicting the PDF.
- Blowing an author's cap — the excess paper, not the earliest, is at risk.

One month's miss costs exactly one month — the next cycle opens on the 20th.
Submitting a half-ready paper to "make this month" wastes a cap slot and burns
the one revision the process will ever offer.

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue vldb-skills   # from a clone of the AJS repository
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

## Output format

```text
[Cycle] <volume / month targeted>
[Abstract stage] registered / at risk / missed
[Category + budget] <category, pages used vs. limit>
[Identity check] single-blind cover page complete / issues
[Cap status] <per-author counts vs. month and year caps>
[Blocking fixes] <ordered, with owner>
```
