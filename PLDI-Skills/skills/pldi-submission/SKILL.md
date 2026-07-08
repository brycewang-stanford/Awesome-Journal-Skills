---
name: pldi-submission
description: Use when auditing a PLDI submission for HotCRP readiness — the single annual November deadline, the 20-pages-of-text-excluding-bibliography cap in single-column acmsmall format, double-blind hygiene across tool names and repositories, dual-submission rules, and summary-rejection triggers before the cutoff.
---

# PLDI Submission

Run this audit before the upload, not after. The numbers below were read from the
PLDI 2026 Call for Papers and track pages on 2026-07-08 (via search renderings of
the official URLs — see `resources/official-source-map.md`); they describe one
cycle and must be rechecked against the live CFP for the cycle you are entering.
The PLDI 2027 call was not yet posted at that date.

## The 2026-cycle mechanics

- **One deadline a year.** PLDI 2026 papers were due Thursday, November 13, 2025.
  There is no second round; a missed November costs twelve months.
- **HotCRP, not OpenReview.** Submission ran at `pldi2026.hotcrp.com` — profile,
  conflicts, and topic areas live there, and each edition gets a fresh instance.
- **Page budget: at most 20 pages of *text*, excluding bibliography**, in the
  single-column ACM `acmsmall` layout (10 pt font, 12 pt line spacing, text block
  5.478 in x 7.884 in), the format PACMPL publishes in. Build with
  `sample-acmsmall-conf.tex` from the acmart package.
- **Summary rejection is the stated penalty** for a different format — smaller
  fonts, a larger text block, squeezed spacing. The chairs do not negotiate
  margins.
- **Double-blind**, and PLDI has used it for years: reviewers must not learn who
  you are from the PDF or anything it links to.

## Where PL papers leak identity

Compiler and tool papers leak differently from ML papers. The usual culprits: a
tool name already public on GitHub under your lab, benchmark harness URLs,
`\author` metadata inside the PDF, grant numbers in acknowledgements, and commit
histories inside supplementary archives.

```bash
pdfinfo paper.pdf | grep -Ei 'author|creator'
pdftotext paper.pdf - | grep -niE 'github\.com/[^ ]+|gitlab|acknowledg|grant no' | head
unzip -l supplement.zip | grep -Ei '\.git/|/home/|/Users/' | head
```

Cite your own prior work in the third person, and if the tool is already public,
discuss with your co-authors whether to rename it in the submission or accept the
risk explicitly — do not discover the collision during reviewing.

## Summary-rejection and triage table

| Trigger | Consequence at PLDI | Recoverable? |
|---|---|---|
| Modified format (font, text block, spacing) | Summary rejection, stated in the CFP | No, after the deadline |
| Over the text-page cap | Summary rejection risk | No |
| Author identity visible in PDF or links | Desk-level double-blind violation | No |
| Same work under review elsewhere | Dual-submission violation under SIGPLAN/ACM policy | No |
| Evaluation missing baselines or variance | Survives triage, dies in review | Only before submission |
| Artifact unplanned | No submission penalty, but AE starts right after acceptance | Yes, but plan now |

## Final week, in order

1. Freeze the claim list; every abstract sentence must have a section that proves it.
2. Rebuild the PDF from a clean tree with the unmodified `acmsmall` class and
   recount text pages against the current cap.
3. Run the leak scan above on the PDF and every supplementary archive.
4. Verify HotCRP conflicts and topics; a stale conflict list misroutes reviewers.
5. Check the CFP's dual-submission and republication wording against anything you
   have on arXiv or under review elsewhere.
6. Submit a day early. HotCRP deadlines are hard cutoffs.

## What this cycle did not settle (待核实)

Whether an abstract-registration step precedes the paper deadline, exact
supplementary-material rules, and any AI-assistance disclosure requirement were
not confirmed in accessible renderings of the 2026 pages — read the live CFP
rather than assuming either way.

## Output format

```text
[PLDI readiness] Ready / Needs fixes / Not ready
[Format] acmsmall unmodified? text pages vs cap?
[Anonymity] PDF metadata / links / tool name / supplement
[Policy] dual submission / arXiv posture / AI disclosure (待核实)
[Fix order] <ordered list before the November deadline>
```
