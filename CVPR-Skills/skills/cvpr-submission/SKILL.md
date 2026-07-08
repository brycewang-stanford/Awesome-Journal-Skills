---
name: cvpr-submission
description: Use when auditing a CVPR submission before the OpenReview deadline, covering abstract registration and profile requirements, the 8-page limit including figures and tables, the Compute Reporting Form, anonymity and external-link bans, dual-submission attestations, reviewer-duty enrollment, and desk-reject triage.
---

# CVPR Submission

Run this audit in the two weeks before the CVPR paper deadline. All specifics below are
the CVPR 2026 cycle as read on 2026-07-08 (paper deadline November 13, 2025); the next
Program Chairs will rewrite details, so reopen the current Author Guidelines and Dates
pages at cvpr.thecvf.com before acting on any number here.

## The three deadlines that catch people

CVPR staggers three hard cut-offs a week apart, and the first one is the one teams miss:

1. **Abstract registration + OpenReview profiles** (Nov 6, 2025 in the 2026 cycle).
   Every listed author — including the advisor added "later" and the intern who wrote one
   module — needed a complete, valid OpenReview profile by this date. An incomplete
   profile on any coauthor is desk-reject exposure for the paper.
2. **Full paper** (Nov 13, 2025, 11:59pm AoE, announced as unmovable). The PDF, the
   author list, subject areas, conflicts, and the **Compute Reporting Form** all land
   here.
3. **Supplementary material** (Nov 20, 2025, AoE). One extra week — but only for the
   supplement; nothing in the main PDF can change after the paper deadline.

## Page discipline, CVPR flavor

The cap is **8 pages including figures and tables**, with extra pages permitted only for
cited references. That "including figures" clause is what distinguishes CVPR budgeting
from text-limited venues: a half-page teaser figure, two qualitative grids, and three
result tables can consume four of your eight pages. Plan figures as page-budget line
items, not decorations, and treat any style-file edit, margin nudge, or font substitution
as a desk-reject trigger — over-length and mis-formatted papers are rejected without
review. Build from the official author kit (`github.com/cvpr-org/author-kit`), current
year's branch, unmodified.

## The Compute Reporting Form

New in the 2026 cycle: every submission carried a CRF. Only Section 1 (hardware) and
Section 5 (verification) were mandatory — about five minutes of work — and a documented
opt-out path existed via the comments field for proprietary or unrecorded compute.
Fill the mandatory sections early; do not let a five-minute form become a deadline-night
blocker, and do not fabricate GPU-hour numbers to look either frugal or mighty.

## Anonymity and the external-link ban

CVPR is double-blind with two venue-specific wrinkles. First, **arXiv posting is not an
anonymity violation** — you may have a preprint up, and reviewers are told not to hunt
for it. Second, **external links are banned when they expand content or subvert
review**: an anonymous-looking project page, a Google Drive of extra results, or a demo
URL can breach anonymity, the media embargo, or the length limit all at once. Everything
reviewers need must live in the PDF and the uploaded supplement.

```bash
# Mechanical sweep on the final build, ten minutes before upload
pdftotext paper.pdf - | grep -nEi 'github\.com|drive\.google|project page|our (prior|previous) work' | head
pdfinfo paper.pdf | grep -Ei 'author|creator|producer'     # identity in metadata
grep -rn 'vspace\|\\addtolength\|geometry' main.tex        # style-tampering tells
pdftotext paper.pdf - | awk 'END{print NR" lines extracted"}'   # sanity: text present, not raster
```

## Dual submission and the media embargo

By submitting you attest that no substantially similar paper is under review at another
conference or workshop **during the defined review period** (Nov 13, 2025 – Feb 20, 2026
in the 2026 cycle). Two verified carve-outs: prior papers of **four pages or fewer** do
not trigger the rule, and GitHub documents are not publications. Separately, papers under
review are embargoed from proactive media discussion until acceptance — a violation can
remove the paper from the proceedings. A journalist writing about your arXiv preprint
without your involvement is not a violation; you pitching the story is.

## Reviewer duty is part of submitting

Submitting authors are enrolled into the reviewer pool. This is not symbolic: papers
authored by a reviewer who blows review deadlines or files highly irresponsible reviews
can be **desk-rejected wholesale** at PC discretion. Before the deadline, decide which
coauthors will absorb December–January reviewing load and calendar it.

## Desk-reject triage

| Finding | Severity | Recoverable? |
|---|---|---|
| Coauthor without a valid OpenReview profile at abstract deadline | Desk reject | Only before Nov 6 |
| Page 9 contains anything besides references | Rejected without review | Only before the paper deadline |
| Style file modified / margins compressed | Rejected without review | Fix and rebuild |
| Identity leak (metadata, acknowledgements, linked repo) | Desk reject | Sweep before upload |
| External link expanding content | Policy violation | Delete; move content into supplement |
| CRF missing | Incomplete submission | Complete Sections 1 and 5 |
| Same work under review elsewhere in the window | Administrative rejection | Withdraw one venue first |
| Assigned coauthor review never delivered (January) | All their papers at risk | Deliver the reviews |

## OpenReview form fields worth drafting early

The PDF gets the rehearsals; the form causes the midnight surprises. Draft these a day
ahead: the abstract field (verbatim from the PDF — reviewers bid on it), subject areas
(chosen for reviewer routing, not maximal coverage), conflicts (every coauthor's
domain conflicts, checked against the institution list), and the author order (frozen —
post-deadline author changes are a chairs-level exception, not an edit).

## Final 72 hours, in order

1. Freeze the 8-page body; late edits go to the supplement queue, not the PDF.
2. Rebuild from a clean checkout of the official kit and verify no local style patches
   leaked in.
3. Run the mechanical sweep above; treat every hit as a blocker.
4. Complete the OpenReview form fields and CRF a full day early; the abstract field must
   match the PDF verbatim because reviewers bid on it.
5. Upload, re-download, and read your own submission cold — including checking that
   figures render at print zoom, since reviewers judge qualitative results visually.

## Reverify each cycle

- All three deadlines and whether abstract registration exists in the current cycle.
- The page cap and whether references-only extra pages still apply.
- CRF existence, mandatory sections, and opt-out wording.
- Dual-submission window definition and the ≤4-page carve-out.
- Supplementary size/format caps (not fetchable for 2026 — 待核实).

## Output format

```text
[CVPR submission] ready / blocked / at-risk
[Profiles] all coauthors valid on OpenReview: yes/no
[Format] pages used (of 8 incl. figures/tables) · refs-only overflow ok
[CRF] mandatory sections complete: yes/no
[Anonymity/links] clean / violations: <list>
[Duty plan] reviewing coauthors named: yes/no
[Fix queue] <ordered blockers>
```
