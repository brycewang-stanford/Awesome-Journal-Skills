---
name: uai-submission
description: Use when auditing a UAI submission for OpenReview readiness, covering the February paper deadline, the 8-page main part with unlimited appendices in one PDF, the 15 MB file cap, the optional 50 MB supplementary ZIP, double-blind rules, the reviewer-volunteer agreement, dual-submission checks, and desk-reject triage before upload.
---

# UAI Submission

Run this audit before uploading to the UAI OpenReview site. Every number below was read
from the UAI 2026 pages on 2026-07-08; treat them as one cycle's snapshot and reopen the
current Call for Papers and submission instructions at auai.org before acting on any of
them.

## What the 2026 cycle required

UAI packages the whole submission into a single PDF, which changes how deadline week
feels compared with venues that collect a separate supplement later:

- Submission ran on OpenReview (the `auai.org/UAI/2026/Conference` group), open from
  January 25, 2026 and closing February 25, 2026, 23:59 Anywhere on Earth. No separate
  abstract-registration deadline was posted for 2026 — do not assume one exists, and do
  not assume one will never appear.
- The main part of the manuscript could not exceed 8 pages. References and appendices
  (proofs, experimental protocols, extra detail) were unlimited but had to follow the
  main part **inside the same PDF**.
- The PDF itself was capped at 15 MB; an optional supplementary ZIP (source code, data)
  was capped at 50 MB. Reviewers were not required to look inside the ZIP.
- Manuscripts had to use the UAI LaTeX template.
- At least one author of every submission agreed to review for UAI if the Program
  Chairs asked — plan that reviewing capacity into the group's spring calendar.

## Anonymity sweep, UAI phrasing

The UAI instructions are specific: refer to your own prior work in the third person, keep
names out of the acknowledgements, omit detailed grant information, and drop any external
link that could reveal identity or affiliation. Because appendices ride inside the
reviewed PDF, an identity leak in a proof appendix is exactly as fatal as one on page 1.

Sweep in this order: author block, running headers, acknowledgements, grant numbers,
self-citations ("our earlier method [3]" is a leak when [3] is yours), repository URLs,
dataset-hosting links, notebook screenshots in the appendix, and PDF metadata.

```bash
# Pre-upload mechanical checks on the single submission PDF and ZIP
pdfinfo paper.pdf | grep -Ei 'author|creator'          # metadata identity fields
pdftotext paper.pdf - | grep -nEi 'github\.com|gitlab|acknowledg|grant no' | head
du -h paper.pdf supplement.zip                          # 15 MB PDF / 50 MB ZIP caps
unzip -l supplement.zip | grep -Ei '\.git/|DS_Store|/home/|users/' | head
```

Treat any hit as a blocker, not a judgment call: the double-blind language in the UAI
instructions is written as a requirement on authors, not as advice.

## Desk-risk triage

| Finding at audit time | Risk level for UAI | What actually fixes it |
|---|---|---|
| Main part runs to page 9 | Rejection-grade format violation | Move protocol detail to the in-PDF appendix, not smaller fonts |
| Appendix separated into the ZIP | Reviewers may never read your proofs | Merge appendices back into the single PDF |
| Identity-revealing link anywhere | Explicitly forbidden by the CFP | Replace with an anonymized archive inside the 50 MB ZIP |
| PDF over 15 MB | Upload refusal | Downsample figures; vectorize plots instead of PNG screenshots |
| Same paper under review elsewhere | Dual-submission violation | Withdraw one venue before the UAI deadline, and say nothing false on the form |
| First-person self-citations | Anonymity breach | Rewrite in third person; keep the citation itself |

## Ordering the final week

1. Freeze the 8-page main part first; the appendix can absorb overflow until the end,
   the main part cannot.
2. Assemble the combined PDF (main + references + appendices) and run the mechanical
   checks above on the merged file, not on the parts.
3. Build the supplementary ZIP last, from a clean export — never from a working
   directory containing `.git`, environment files, or cluster paths.
4. Complete OpenReview metadata (title, abstract, authors, conflicts, subject areas)
   a day early; the form, not the PDF, is what desk officers read first.
5. Re-download your own submission from OpenReview and open it cold. What you see is
   what reviewers get.

## Template discipline

Compile with the current year's official class file, unmodified: no geometry
overrides, no `\vspace` compression rituals, no font substitutions. Two-column
probabilistic papers overflow through display math, so recover space legitimately —
`align` consolidation, inline-izing trivial equations, moving derivation chains to
the appendix — rather than through spacing hacks that chairs can detect mechanically.

## Claims the paper must survive

UAI reviews against four posted criteria: technical correctness, novelty, whether claims
are backed up convincingly, and clarity of writing. A submission audit is therefore not
only formatting. Before upload, confirm that every theorem's assumptions are stated where
the theorem is, that every empirical claim has a table or figure behind it, and that the
abstract promises nothing the appendix cannot deliver. Code and data release is strongly
encouraged by the CFP — if you are not releasing, be ready to explain why during review
rather than hoping nobody asks.

## OpenReview form, drafted before deadline day

The PDF gets the attention; the form causes the late-night surprises. Draft every
field a day early:

```yaml
# openreview-form-draft.yaml — fill before the final upload session
title:            # identical to the PDF, including capitalization
abstract:         # word-for-word match with the PDF abstract; it drives bidding
authors:          # complete, ordered, each with an active OpenReview profile
conflicts:        # domain conflicts for every author, checked against coauthors
subject_areas:    # chosen for reviewer routing, not breadth (see uai-review-process)
supplementary:    # ZIP attached? or deliberately none — decide, don't default
volunteer_ack:    # reviewer-volunteer agreement acknowledged by the author list
dual_submission:  # confirmed false at every coauthor's institution, in writing
```

Abstract-field drift is the sneaky one: edits to the PDF abstract in the last hours
rarely make it back into the form, and reviewers bid on the form.

## Cycle-volatile items — reverify every year

- Exact deadlines and the AoE convention; 2026's February 25 date is history, not policy.
- Page, PDF-size, and ZIP-size caps (8 pages / 15 MB / 50 MB were the 2026 numbers).
- Whether an abstract deadline, checklist, or AI-use disclosure is added in a later cycle
  (none was posted for 2026 — 待核实 each new cycle).
- Reviewer-volunteer wording and dual-submission scope.

## Output format

```text
[UAI submission status] ready / blocked / needs review
[Format] main-part pages, PDF size, ZIP size vs current caps
[Anonymity] clean / leaks found: <location list>
[Criteria exposure] weakest of: correctness / novelty / backing / clarity
[Fix queue] <ordered actions before the deadline>
```
