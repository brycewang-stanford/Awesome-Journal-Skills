---
name: wacv-submission
description: Use when auditing a WACV submission before an OpenReview round deadline, covering the Round 1 vs Round 2 choice, the Applications vs Algorithms track field, the 8-page-including-figures limit, double-blind anonymity and OpenReview-profile requirements, the anonymized supplement, dual submission, and desk-reject triage.
---

# WACV Submission

Run this audit in the two weeks before a WACV **round** deadline. The specifics below are
the WACV 2026/2027 cycles as read on 2026-07-09; chairs rewrite details each edition, and
WACV uniquely runs **two rounds**, so reopen the current Author Guidelines, Dates page, and
the correct OpenReview round group at wacv.thecvf.com before acting on any number here.

## First decision: which round, which track

Two fields on the OpenReview form change everything downstream, and both are chosen before
you write a word of the audit:

1. **Round 1 or Round 2.** They are *different OpenReview groups*. Round 1 (reported paper
   deadline June 26, 2026 for WACV 2027) gives you a rebuttal and the Revise-and-Resubmit
   safety net — a paper that is close but not done can be invited back rather than killed.
   Round 2 (reported August 28, 2026) is Accept/Reject with **no rebuttal**; it is for
   polished work and for revised Round 1 papers. Submitting a borderline paper straight to
   Round 2 throws away the mechanism WACV built to help it.
2. **Applications or Algorithms track.** The two tracks are reviewed against different
   criteria (systems-level innovation and comparative assessment vs algorithmic novelty and
   matched-baseline evaluation). Pick the track where the contribution is *stronger*, and
   make the first page argue for that lens — a mis-tracked paper draws a reviewer asking the
   wrong question, which is a fast route to Revise and Resubmit.

## Format discipline, WACV flavor

The cap is **8 pages including figures and tables**, in the WACV style, with extra pages
for cited references only. That "including figures" clause makes a qualitative grid or a
result table a page-budget line item, not a decoration. Build from the current WACV author
kit unmodified; treat any style-file edit, margin nudge, or font substitution as a
desk-reject trigger. Every author needs a **valid OpenReview profile by the round
deadline** — an incomplete profile on the advisor added late or the intern who wrote one
module is desk-reject exposure for the whole paper.

## Anonymity and the anonymized supplement

WACV is double-blind: reviewers should not be able to infer authorship "beyond reasonable
doubt" from the paper or the supplement. Anonymize acknowledgements (no co-workers, grant
IDs), PDF metadata, self-citations (third person), filenames, and any movie titles or
overlays in supplementary videos; do not link to sites that identify the authors. A
technical report / arXiv preprint is handled under the current prior-publication rule —
check it rather than assuming, and never rely on an external link to carry review content.

```bash
# Mechanical sweep on the final build, ten minutes before upload
pdftotext paper.pdf - | grep -nEi 'github\.com|drive\.google|project page|our (prior|previous) work' | head
pdfinfo paper.pdf | grep -Ei 'author|creator|producer'      # identity in metadata
grep -rn 'vspace\|\\addtolength\|geometry' main.tex         # style-tampering tells
pdftotext paper.pdf - | awk 'END{print NR" lines extracted"}'   # sanity: text present, not raster
```

## Desk-reject and triage table

| Finding | Severity at WACV | Recoverable? |
|---|---|---|
| Coauthor without a valid OpenReview profile at the round deadline | Desk reject | Only before that deadline |
| Page 9 contains anything besides references | Rejected without review | Only before the round deadline |
| Style file modified / margins compressed | Rejected without review | Fix and rebuild |
| Identity leak (metadata, acknowledgements, linked repo, video overlay) | Desk reject | Sweep before upload |
| Wrong track for the contribution | Not a reject, but Revise-and-Resubmit risk | Re-frame first page before deadline |
| Same work under review elsewhere in violation of the dual-submission rule | Administrative rejection | Withdraw one venue first |
| Borderline paper sent straight to Round 2 | No rebuttal, no R&R net | Prefer Round 1 next time |

## Final-week sequence

1. Confirm the **round** and **track** fields; they set every other decision.
2. Freeze the 8-page body; late edits go to the supplement queue, not the main PDF.
3. Rebuild from a clean checkout of the WACV author kit; verify no local style patches
   leaked in and pages 9+ are references only.
4. Run the mechanical sweep above; treat every hit as a blocker.
5. Confirm every coauthor's OpenReview profile is valid, and that the OpenReview abstract
   matches the PDF abstract verbatim.
6. Upload, re-download, and read your own submission cold — including checking figures at
   print zoom, since applications reviewers judge qualitative results visually.

## Reverify each cycle

- Both round deadlines and whether the two-round model still holds for the target year.
- The page cap and whether references-only overflow still applies.
- The track definitions and review criteria (Applications vs Algorithms).
- The prior-publication / arXiv rule and the dual-submission window.
- Supplementary size/format caps (not fetchable for 2026 — 待核实).

## Output format

```text
[WACV submission] ready / blocked / at-risk
[Round] R1 (rebuttal + R&R net) / R2 (Accept-Reject, no rebuttal) — chosen: <one>
[Track] Applications / Algorithms — first page argues for it: yes/no
[Profiles] all coauthors valid on OpenReview: yes/no
[Format] pages used (of 8 incl. figures/tables) · refs-only overflow ok
[Anonymity/links] clean / violations: <list>
[Fix queue] <ordered blockers>
```
