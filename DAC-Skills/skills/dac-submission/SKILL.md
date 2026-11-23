---
name: dac-submission
description: Use when auditing an ACM/IEEE Design Automation Conference (DAC) Research-Manuscript submission for Softconf readiness, covering the two-stage abstract-then-manuscript deadline, the 6+1-page IEEE-template double-column page budget with its references-only last page, the double-blind anonymization sweep (including PDF metadata), TPC conflict-of-interest declaration, the AI-content disclosure, and desk-reject triage before the mid-November cutoff.
---

# DAC Submission

Run this audit before uploading to the DAC Softconf/START site. DAC Research Manuscripts are
**double-blind, archival** papers published in **IEEE Xplore and the ACM Digital Library**, judged
on novelty and measured design-quality impact. Every number below was read from the DAC 2027
Research Manuscript Submissions page (`dac.com/2027/program/research-manuscript-submissions`) on
2026-11-24 (see `resources/official-source-map.md`). The DAC 2027 research deadlines (abstract
11 November 2026, manuscript 18 November 2026) have passed; use this audit for the DAC 2028 cycle
only after reopening its call.

## The two-stage deadline

DAC separates **abstract submission** from **manuscript submission**, and both matter:

- **Abstract stage** (DAC 2027: 11 November 2026, 5:00 pm US Pacific): title, an abstract of
  **approximately 100 words**, and **every co-author** (names, affiliations, countries, emails)
  go into Softconf (`softconf.com/dac27/research`), with TPC conflicts. This seeds TPC bidding and
  conflict detection. Miss it and the system will not take your PDF.
- **Manuscript stage** (DAC 2027: 18 November 2026, 5:00 pm US Pacific): the anonymized 6+1-page
  PDF. There is **no grace period** to repair a malformed or de-anonymized file after the cutoff,
  and no co-author may be added or re-ordered after it.

Register the *real* title and abstract — a placeholder abstract worsens your reviewer match, which
is the single largest lever you control (see `dac-review-process`).

## Format and page budget (the 6+1 rule)

- **IEEE template, double-column, 9 or 10-pt font, single PDF.** This is the DAC 2027 requirement
  (DAC 2026 used the ACM template — the template has tracked the edition's copyright holder, so
  never reuse last year's class file without checking). Accepted papers sign the IEEE Copyright Form and
  appear in IEEE Xplore and ACM DL.
- **Leave room for the final version.** The review PDF must leave enough space for the author
  block and acknowledgements within the 6-page limit; the final version may not differ
  significantly from the reviewed one.
- **Page budget:** the manuscript is **within 6 pages excluding references**, plus **one additional
  page for references only**. This is the "6+1" budget — six double-column pages carry the entire
  technical argument, figures, and tables.
- **The extra page is references-only.** Putting *any* non-reference content (an extra figure, a
  paragraph of text, an appendix) on that seventh page is grounds for **desk rejection**. Do not
  try to smuggle body content there.
- Margins, columns, and font are fixed by the template; recover space by editorial compression and
  tighter figures, never by template tampering.

## Double-blind anonymization sweep

DAC review is **double-blind**: author names and affiliations must not appear anywhere in the
manuscript or abstract (an identity reveal is a desk reject), "omitted for blind review" citations
are **not permitted**, and the **PDF metadata must not contain author information**. Because EDA papers lean on tools, benchmark runs, and vendor flows, the leak surface is
wide:

```bash
# Mechanical pass on the submission PDF
pdfinfo paper.pdf | grep -Ei 'author|creator|producer'
pdftotext paper.pdf - | grep -nEi 'university|institute|@[a-z0-9.]+\.edu|acknowledg|funded|grant' | head
pdftotext paper.pdf - | grep -nEi 'our (tool|lab|group|flow)|github\.com/[a-z0-9-]+|gitlab' | head
```

DAC-specific leaks to hunt for:

- **Self-citations in the first person** — "in our prior work [7] we..." de-anonymizes. Cite your
  own prior papers in the **third person** ("Prior work [7] showed...").
- **A tool named after your lab or a public repo** that discloses authorship — rename or
  anonymize the tool for review.
- **A commercial-flow fingerprint** (a vendor tool version string, a proprietary PDK/library name
  under NDA) that both leaks identity and can raise a confidentiality flag.
- **Acknowledgements, funding, or grant numbers** left in the review version — remove them; they
  return in the camera-ready.
- **Benchmark or cluster paths** (`/home/username/...`, an internal server name) in a figure or log
  excerpt.

## TPC conflict-of-interest declaration

DAC asks authors to **declare conflicts of interest with Technical Program Committee members** at
submission and assumes none beyond those declared. DAC 2027 defines a conflict as advisor-advisee,
co-authorship in the last 24 months, same institution, co-PIs on a grant in the last 2 years, or a
close personal/family relationship — for every co-author. Missing a real COI, or marking a TPC
member who is not a conflict, leads to desk rejection.

Also in the form: **disclose related unpublished work** (under review or accepted) by listing it
and uploading the PDFs for the TPC Chair, and respect the cap of **20 research manuscripts per
author**. arXiv preprints are allowed if the submission stays double-blind compliant.

## AI-content disclosure

If LLM-generated text, figures, images or code appear in the paper, add a separate section headed
**"Content Generated by AI"** naming the LLMs and the sections affected. Editing, grammar,
translation and knowledge retrieval need no disclosure (it is recommended). LLMs cannot be
authors.

## Desk-risk triage

| Finding at audit time | Severity | Real fix |
|---|---|---|
| Body over 6 pages, or content on the references-only page | Named desk-reject ground | Cut/compress; the 7th page is references only |
| Template altered (columns, shrunk font, margins) or last year's ACM class used | Desk-reject-grade | Recompile in the clean IEEE double-column template; recover space editorially |
| Author identity leak (PDF metadata, first-person self-cite, "omitted for blind review", tool name) | Desk reject | Re-anonymize; scrub metadata; third-person self-citations |
| Abstract stage not completed by the earlier date | No submission slot exists | Nothing fixes this post-cutoff — calendar it now |
| No standard benchmark / private-data-only evaluation | Scored weakness | Add a recognized suite (ISPD/EPFL/ISCAS/ITC/TAU) or justify explicitly |
| Same result under review at ICCAD/DATE/ASP-DAC | Dual-submission exposure | Withdraw one; verify DAC's concurrent-submission wording |

## Final-week order of operations

1. Freeze the contribution and the QoR numbers; the argument cannot churn in the last week.
2. Complete the **abstract stage** (title/abstract/all co-authors) well before its cutoff.
3. Compile to the IEEE double-column template and confirm the **6-page body / 1-page references**
   split on the *final* PDF.
4. Run the double-blind sweep on the *final* PDF — metadata, self-citations, tool names, acks.
5. Enter TPC conflicts and topic areas in Softconf a day early; late conflicts are a classic
   midnight failure.
6. Upload, re-download, and read the PDF cold to confirm it is the file you meant.

## Reverify each cycle

- Exact abstract and manuscript deadlines and time zone (DAC 2027: 5:00 pm US Pacific).
- Page budget and template (DAC 2027: 6+1, double-column, IEEE; DAC 2026 was ACM).
- Whether a rebuttal/response period exists (DAC 2027: none in the timeline).
- Concurrent-submission wording versus ICCAD/DATE/ASP-DAC, and the AI-content disclosure rule.

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue dac-skills   # from a clone of the AJS repository
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
[DAC submission status] ready / blocked / needs work
[Abstract stage] title/abstract/all co-authors locked by the earlier deadline? yes/no
[Format] body pages used / references-only page clean? IEEE double-column compliance
[Anonymity] clean / leaks: <where>
[Evidence] standard benchmark suite present? baselines named?
[COI] TPC conflicts declared for every co-author? yes/no
[AI content] "Content Generated by AI" section needed? present? yes/no/n.a.
[Fix queue] <ordered, with owners and dates before the November cutoff>
```
