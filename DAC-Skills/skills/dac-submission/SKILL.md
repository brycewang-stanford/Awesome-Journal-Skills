---
name: dac-submission
description: Use when auditing an ACM/IEEE Design Automation Conference (DAC) Research-Manuscript submission for Softconf readiness, covering the two-stage abstract-then-manuscript deadline, the 6+1-page ACM double-column page budget with its references-only last page, the double-blind anonymization sweep, TPC conflict-of-interest declaration, and desk-reject triage before the mid-to-late-November cutoff.
---

# DAC Submission

Run this audit before uploading to the DAC Softconf/START site. DAC Research Manuscripts are
**double-blind, archival** papers published on the **ACM Digital Library**, judged on novelty and
measured design-quality impact. Every number below was read from the DAC 2026 Call and Research
Manuscripts Guidelines on 2026-07-09 via search renderings of the `dac.com/2026` pages (see
`resources/official-source-map.md`); treat them as a one-cycle snapshot and reopen the live call
first.

## The two-stage deadline

DAC separates **abstract submission** from **manuscript submission**, and both matter:

- **Abstract stage** (~one week early): title, full abstract, and **every co-author** go into
  Softconf. This seeds TPC bidding and conflict detection. Miss it and the system will not take
  your PDF.
- **Manuscript stage** (DAC 2026: ~19 November 2025): the anonymized 6+1-page PDF. There is **no
  grace period** to repair a malformed or de-anonymized file after the cutoff.

Register the *real* title and abstract — a placeholder abstract worsens your reviewer match, which
is the single largest lever you control (see `dac-review-process`).

## Format and page budget (the 6+1 rule)

- **ACM template, double-column, 9 or 10-pt font, single PDF.** This is DAC's current requirement;
  ACM is the 2026 copyright holder and the paper is archived on ACM DL.
- **Page budget:** the manuscript is **within 6 pages excluding references**, plus **one additional
  page for references only**. This is the "6+1" budget — six double-column pages carry the entire
  technical argument, figures, and tables.
- **The extra page is references-only.** Putting *any* non-reference content (an extra figure, a
  paragraph of text, an appendix) on that seventh page is grounds for **desk rejection**. Do not
  try to smuggle body content there.
- Margins, columns, and font are fixed by the template; recover space by editorial compression and
  tighter figures, never by template tampering.

## Double-blind anonymization sweep

DAC review is **double-blind**: author names and affiliations must not appear anywhere on the
manuscript. Because EDA papers lean on tools, benchmark runs, and vendor flows, the leak surface is
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
submission and assumes none beyond those declared. Declare every co-author's advisor/advisee,
recent (typically last-few-years) collaborators and co-authors, same-institution members, and close
family — under-declaring a real COI is an integrity problem, not a shortcut to a friendlier
reviewer.

## Desk-risk triage

| Finding at audit time | Severity | Real fix |
|---|---|---|
| Body over 6 pages, or content on the references-only page | Named desk-reject ground | Cut/compress; the 7th page is references only |
| Template altered (columns, shrunk font, margins) | Desk-reject-grade | Recompile clean ACM double-column; recover space editorially |
| Author identity leak (PDF metadata, first-person self-cite, tool name) | Anonymity violation | Re-anonymize; scrub metadata; third-person self-citations |
| Abstract stage not completed by the earlier date | No submission slot exists | Nothing fixes this post-cutoff — calendar it now |
| No standard benchmark / private-data-only evaluation | Scored weakness | Add a recognized suite (ISPD/EPFL/ISCAS/ITC/TAU) or justify explicitly |
| Same result under review at ICCAD/DATE/ASP-DAC | Dual-submission exposure | Withdraw one; verify DAC's concurrent-submission wording |

## Final-week order of operations

1. Freeze the contribution and the QoR numbers; the argument cannot churn in the last week.
2. Complete the **abstract stage** (title/abstract/all co-authors) well before its cutoff.
3. Compile to the ACM double-column template and confirm the **6-page body / 1-page references**
   split on the *final* PDF.
4. Run the double-blind sweep on the *final* PDF — metadata, self-citations, tool names, acks.
5. Enter TPC conflicts and topic areas in Softconf a day early; late conflicts are a classic
   midnight failure.
6. Upload, re-download, and read the PDF cold to confirm it is the file you meant.

## Reverify each cycle

- Exact abstract and manuscript deadlines and time-zone/AoE convention.
- Page budget and ACM template revision (DAC 2026: 6+1, double-column).
- Whether a rebuttal/response period exists (**待核实** for DAC 2026).
- Concurrent-submission wording versus ICCAD/DATE/ASP-DAC, and any generative-AI disclosure rule.

## Output format

```text
[DAC submission status] ready / blocked / needs work
[Abstract stage] title/abstract/all co-authors locked by the earlier deadline? yes/no
[Format] body pages used / references-only page clean? ACM double-column compliance
[Anonymity] clean / leaks: <where>
[Evidence] standard benchmark suite present? baselines named?
[COI] TPC conflicts declared for every co-author? yes/no
[Fix queue] <ordered, with owners and dates before the November cutoff>
```
