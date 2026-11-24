---
name: ase-submission
description: Use when auditing an ASE (IEEE/ACM Automated Software Engineering) research-track submission for HotCRP readiness, covering the IEEE IEEEtran conference template (ASE 2027) and the 10+2 page budget, double-anonymous review, the Data Availability section, the early-rejection stage before rebuttal, and desk-reject triage before the deadline.
---

# ASE Submission

Run this audit before uploading to `ase2027.hotcrp.com`. ASE research papers are published in the
proceedings of the **IEEE/ACM International Conference on Automated Software Engineering**, indexed
by IEEE and ACM SIGSOFT (the ASE 2027 publication of record is the IEEE Digital Library). Every
number below was read directly from the ASE 2027 research-track call on 2026-11-24 (see
`resources/official-source-map.md`); treat them as a one-cycle snapshot and reopen the live call
first.

## Calendar and portal

- **Portal:** HotCRP at `ase2027.hotcrp.com`. NIER, Tools-and-Datasets, and Journal-First each have
  their own site/track — do not upload a research paper to the wrong one.
- **ASE 2027 research dates (AoE):** paper submission **10 March 2027**; early-rejection
  notification **19 May 2027**; author response **19-24 May 2027**; initial notification **10 June
  2027**; major-revision submission **8 July 2027**; final notification **27 July 2027**;
  camera-ready **11 August 2027** (El Paso, Texas, Oct 24-28 2027). The call describes an abstract
  stage (title, abstract, areas, conflicts — dummy placeholders are rejected), but the dates page
  lists no separate abstract date — **待核实**; confirm it, because a missed abstract registration
  can forfeit the submission slot.

## Format and page budget

- **Template:** for ASE 2027, the IEEE Conference Proceedings format — 24pt title, 10pt text,
  `\documentclass[10pt,conference]{IEEEtran}` **without** the `compsoc` or `compsocconf` option.
  Note the ASE nuance: because the conference is **dual IEEE/ACM sponsored**, the mandated template
  flips between editions (ACM `acmart` sigconf for 2026, IEEEtran for 2027). Confirm which the
  current call requires before you format anything — carrying last year's acmart habit forward is
  a classic ASE mistake.
- **Page budget:** **10 pages** of main text — text, figures, tables, and appendices — **plus up to
  2 pages** containing references and the Data Availability statement. There is no unlimited
  appendix inside the paper; anything a reviewer must read to judge the work lives inside the 10
  pages. Over-length or misformatted papers are desk-rejected.
- **Data Availability section:** a section named **Data Availability** after the Conclusion,
  stating the availability of a replication package (or why there is none). For 2027 it does **not**
  count toward the 10 pages (it shares the 2 extra pages with the references); keep it anonymous.
- Accepted papers get **one additional content page** (11 + 2); do not pre-spend it in the
  submission.
- **Generative AI:** ASE 2027 follows the IEEE policy — disclose AI-generated content (text,
  figures, images, code) in the **acknowledgments**, naming the system and the sections it produced;
  editing/grammar help is exempt (disclosure recommended). Research with human subjects needs an
  IRB/ethics and consent statement.

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

- The **Data Availability section is required** and reviewed. State what exists (tool, dataset,
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
| Wrong template (ACM `acmart` when IEEEtran is required for 2027, or vice versa) | Named desk-reject ground | Recompile in the mandated template; recover space editorially |
| No Data Availability section | Policy violation | Add it after the Conclusion (for 2027 it sits with the references, outside the 10 pages) |
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

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue ase-skills   # from a clone of the AJS repository
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
[ASE submission status] ready / blocked / needs work
[Registration] abstract/authors/conflicts locked by the earlier deadline? yes/no
[Format] template (IEEEtran conference for 2027?), pages used (content/refs+DA), Data Availability present after Conclusion?
[Anonymity] clean / leaks: <where, incl. tool name>
[Open science] anonymized tool + dataset link present?
[Fix queue] <ordered, with owners and dates before the deadline>
```
