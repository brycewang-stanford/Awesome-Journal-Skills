---
name: eccv-submission
description: Use when auditing an ECCV submission for the two-step registration-then-paper deadline chain, the 14-page LNCS single-column limit, CET (not AoE) cutoffs, the trailing supplementary deadline, double-blind rules, the four-page dual-submission definition, the social-media embargo, and reviewer-duty exposure before upload.
---

# ECCV Submission

Use this to run the final audit on an ECCV upload. The 2026 window has closed
(paper deadline March 5, 2026), so treat every number below as a 2026 anchor for
post-mortems and 2028 planning, and reopen the next cycle's Dates and Submission
Policies pages before quoting anything as current.

## The 2026 deadline chain (verified 2026-07-08)

ECCV runs a two-step front door with a trailing supplement — three separate
cutoffs, and the clock was **CET**, not AoE:

| Step | 2026 date | Trap it creates |
|---|---|---|
| Paper registration on OpenReview | February 26, 2026 (profiles completable to March 2, 11pm CET) | No registration record, no paper slot a week later |
| Full paper PDF | March 5, 2026, 11pm CET | Teams planning in AoE lose up to a day; no extensions were offered |
| Supplementary material | March 12, 2026 | The paper freezes first; the supplement cannot repair it |

Aggregators disagree by one day on the paper deadline (March 5 vs March 6) because
of timezone conversion — another reason to read the official Dates page in CET.

## Format gate

- LNCS single-column, **14 pages including figures and tables**; pages beyond 14
  may contain only cited references.
- The 2026 author kit stated the template changed after 2024 — a recycled
  ECCV 2024 `.cls` is a compliance risk, not a convenience.
- Single-column LNCS absorbs figures very differently from a two-column draft:
  full-width figures are cheap, side-by-side panels are not. Budget pages in the
  real template from the first draft.
- Submission platform: OpenReview, group `thecvf.com/ECCV/2026/Conference`.

## Policy gate

- **Dual submission**: ECCV 2026 defined a "publication" as any peer-reviewed,
  accepted written work longer than four pages excluding references; arXiv
  preprints and technical reports did not count. Violations meant rejection and
  a report to the other venue.
- **arXiv**: posting is not an anonymity violation, but the submission must not
  cite the authors' own public codebase.
- **Embargo**: papers publicly identified as ECCV submissions during the review
  embargo faced summary rejection — the media rule bans naming the venue, not
  discussing the work.
- **Reviewer duty**: all authors were expected to be willing to review; an
  author whose assigned reviews were late or "highly irresponsible" (including
  LLM-written) risked desk rejection of *all* their submissions.

## Pre-upload sweep

```text
□ Registration record exists for this exact title/author set (Feb deadline)
□ PDF built from the current-cycle author kit, 14 pages + refs only
□ CET deadline entered in the team calendar, not AoE
□ No self-identifying codebase links, acknowledgements, or grant strings
□ Dual-submission attestation true under the 4-page definition
□ Nobody on the author list has an unresolved reviewing assignment
□ Supplement plan for the +7-day deadline drafted before the paper freeze
```

## Severity ladder

| Failure | 2026 consequence |
|---|---|
| Missed registration step | Cannot submit at all |
| Page 15 contains a figure caption | Desk rejection |
| Venue named on social media during embargo | Summary rejection |
| Duplicate submission under the 4-page rule | Rejection plus report to the sibling venue |
| Co-author's irresponsible review | Desk rejection of every paper they are on |

The last row is the distinctly ECCV-2026 hazard: your submission's fate is coupled
to your co-authors' reviewing behavior, so confirm each co-author's reviewer
status during the audit, not after decisions.

## Missed-window arithmetic

Because ECCV is biennial, a slipped March deadline costs two years at this venue.
The realistic reroutes from a March miss: BMVC (spring deadline), WACV (summer
deadline), CVPR (November deadline), ICCV (next odd-year March). Route with
`eccv-workflow` rather than rushing a broken upload.

## Output format

```text
[ECCV upload verdict] go / fix first / reroute
[Deadline-chain status] <registration / paper / supplement, with CET times>
[Format violations] <page 15 content, template vintage, column abuse>
[Policy violations] <dual-submission / embargo / anonymity / reviewer duty>
[Ordered fixes] <what to change before the CET cutoff>
```
