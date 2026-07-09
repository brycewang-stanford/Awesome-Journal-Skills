---
name: ase-submission
description: Use when auditing an ASE (IEEE/ACM Automated Software Engineering) research-track submission for HotCRP readiness, covering the ACM acmart sigconf template and the 10+2 page budget, double-anonymous review, the mandatory Data Availability Statement, the early-rejection stage before rebuttal, and desk-reject triage before the deadline.
---

# ASE Submission

Run this audit before uploading to `ase26.hotcrp.com`. ASE research papers are published in the
proceedings of the **IEEE/ACM International Conference on Automated Software Engineering**, indexed
in **both IEEE Xplore and the ACM Digital Library**. Every number below was read from the ASE 2026
research-track call on 2026-07-09 via search renderings of the `conf.researchr.org` URLs (see
`resources/official-source-map.md`); treat them as a one-cycle snapshot and reopen the live call
first.

## Calendar and portal

- **Portal:** HotCRP at `ase26.hotcrp.com`. NIER, Tools-and-Datasets, and Journal-First each have
  their own site/track — do not upload a research paper to the wrong one.
- **ASE 2026 research dates:** submission **26 March 2026**, notification **25 May 2026** (Munich,
  Oct 12-16 2026). The exact abstract-registration deadline that precedes the full-paper deadline
  is **待核实** — confirm it, because a missed abstract registration can forfeit the submission slot.
- As of 2026-07-09 the ASE 2026 notification has passed; the next *submission* target is ASE 2027
  (host/dates **待核实**). Reverify the whole calendar before acting.

## Format and page budget

- **Template:** for ASE 2026, the ACM Primary Article (Proceedings) Template —
  `\documentclass[sigconf,review,anonymous]{acmart}`. Note the ASE nuance: because the conference
  is **dual IEEE/ACM sponsored**, the mandated template has varied across editions (an IEEE
  two-column format in some years, ACM `acmart` sigconf for 2026). Confirm which the current call
  requires before you format anything — carrying an old IEEEtran or acmart habit forward is a
  classic ASE mistake.
- **Page budget:** **10 pages** for all content — text, figures, tables, and appendices — **plus 2
  pages** for references only. There is no unlimited appendix inside the paper; anything a reviewer
  must read to judge the work lives inside the 10 pages.
- **Mandatory Data Availability Statement:** placed **after the Conclusions** and **inside the
  10-page limit**. It is not optional and it is not free space — budget for it.
- Accepted papers are typically allowed **one additional content page** for revisions; do not
  pre-spend it in the submission.

## Double-anonymous sweep

ASE runs **double-anonymous** review: author names and affiliations are omitted and prior work is
cited in the third person. Automated-SE papers leak identity through their *tools* more than their
prose, so the surface is wide:

```bash
# Mechanical pass on the submission PDF and any anonymized artifact archive
pdfinfo paper.pdf | grep -Ei 'author|creator|producer'
pdftotext paper.pdf - | grep -nEi 'github\.com/[a-z0-9-]+|gitlab|zenodo\.org/record|acknowledg|grant' | head
unzip -l artifact.zip | grep -Ei '\.git/|\.DS_Store|/home/|/Users/' | head
grep -rniE 'university|@[a-z0-9.]*\.edu|our (tool|group|lab)|named after' artifact/ --include='*.md' | head
```

The ASE-specific leaks: a **tool named after your lab or a prior project**, a screenshot of an IDE
showing a username, a Data Availability link pointing at a personal GitHub, commit metadata inside a
zipped repository, subject-system paths under `/home/<you>/`, and self-citations phrased in the
first person. Re-host the tool and dataset behind an anonymizing service *before* upload.

## Data Availability and open science at submission time

- The **Data Availability Statement is required** and reviewed. State what exists (tool, dataset,
  scripts, logs), where it will live after acceptance, and provide an **anonymized** link or upload
  now.
- "Available upon request" reads as a scored weakness, not a neutral choice. If you genuinely cannot
  share (industrial confidentiality, license limits), say so and why.
- For automated-SE tools: pin the exact commit, subject-system versions/SHAs, configuration, and
  seeds; cache any LLM outputs now — they cannot be reconstructed at review time.

## Desk-risk triage

| Finding at audit time | Severity | Real fix |
|---|---|---|
| Content over 10 pages (refs are separate) | Desk-reject-grade | Cut or move to the artifact; the 2 reference pages do not absorb body text |
| Wrong template (IEEEtran when ACM `acmart` is required, or vice versa) | Named desk-reject ground | Recompile in the mandated template; recover space editorially |
| No Data Availability Statement, or it sits outside the 10 pages | Policy violation | Add it after Conclusions, inside the budget |
| Identity leak in PDF, artifact, or tool name | Anonymity violation | Re-anonymize and re-host; scrub PDF metadata |
| Abstract not registered by the earlier date | No submission slot exists | Nothing fixes this post-deadline — calendar it now |
| Same study under review elsewhere | Dual-submission exposure | Withdraw one venue; verify the current concurrent-submission wording |

## Final-week order of operations

1. Freeze the body early; references can churn, the argument cannot.
2. Register title/abstract/authors/conflicts before the (earlier) abstract deadline.
3. Anonymize the tool and dataset, re-host behind an anonymizing service, and write the Data
   Availability Statement after Conclusions.
4. Run the mechanical anonymity checks on the *final* PDF and the *final* archive, not drafts.
5. Fill every HotCRP field — area tags that match your automation, conflicts for every coauthor's
   institution and recent collaborators — a day early; late conflicts are the classic failure.
6. Re-download the uploaded PDF and read it cold to confirm it is the file you meant.

## Reverify each cycle

- The required template (IEEE two-column vs. ACM `acmart`) and the page budget.
- The abstract-registration and submission deadlines, and whether the year runs one submission
  cycle or more.
- Data Availability wording, artifact-track timing, dual-submission wording, and any AI-disclosure
  rule — all cycle-volatile.

## Output format

```text
[ASE submission status] ready / blocked / needs work
[Registration] abstract/authors/conflicts locked by the earlier deadline? yes/no
[Format] template (acmart sigconf? IEEE?), pages used (content/refs), Data Availability present & inside 10pp?
[Anonymity] clean / leaks: <where, incl. tool name>
[Open science] anonymized tool + dataset link present?
[Fix queue] <ordered, with owners and dates before the deadline>
```
