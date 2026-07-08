---
name: vldb-submission
description: Use when auditing a PVLDB submission before a monthly deadline, covering the mandatory abstract on the 25th, the CMT window, the 1st-of-month 5:00 PM Pacific cutoff, category and page-budget choice, single-blind cover-page requirements, the per-month and per-year author caps, and desk-reject hazards specific to VLDB.
---

# VLDB Submission

Run this in the two weeks before a PVLDB monthly deadline. VLDB research papers
enter through PVLDB (Proceedings of the VLDB Endowment), and the volume's own
guidelines page — not the conference site's summary — is the governing document.
Everything dated below was checked 2026-07-08; reopen the live volume page first.

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
budget. Category continuation and budgets for the volume you target: confirm on
the live page (待核实 for Vol 20 beyond the sources in the source map).

## Identity and caps

- PVLDB review is **single-blind**: author names and affiliations belong on the
  paper. Do not strip them the way SIGMOD or ML venues require — an anonymous
  PVLDB submission is a formatting error, not a virtue. Reconfirm the wording
  on the live guidelines before submission.
- Count coauthor load before promising a submission: Vol 20 caps each author at
  **two papers per month** and **twelve per year**.
- Declare conflicts accurately in CMT; the review board assignment runs on them.

## Pre-deadline audit sequence

```text
[ ] Live volume identified (Vol 20 on 2026-07-08) and its guidelines reopened
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

## Output format

```text
[Cycle] <volume / month targeted>
[Abstract stage] registered / at risk / missed
[Category + budget] <category, pages used vs. limit>
[Identity check] single-blind cover page complete / issues
[Cap status] <per-author counts vs. month and year caps>
[Blocking fixes] <ordered, with owner>
```
