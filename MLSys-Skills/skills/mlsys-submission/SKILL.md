---
name: mlsys-submission
description: Use when auditing an MLSys submission for OpenReview readiness, covering the two-column 10-page body excluding references, the separate appendix upload, double-blind rules that still permit arXiv posting, research-versus-industrial track requirements, dual-submission exceptions, style-kit compliance, and desk-reject triage before the deadline.
---

# MLSys Submission

Use this to run a pre-deadline audit of a Conference on Machine Learning and Systems
submission. Facts below are anchored to the 2026 cycle (verified 2026-07-08); reopen the
current Call for Research Papers and the Industrial Track call on mlsys.org before acting,
because MLSys restructures its calls between cycles — the Industrial Track itself only
appeared in 2026.

## Track decision comes first

Everything downstream differs by track, so settle this before formatting anything.

| Question | Research track | Industrial track (new in 2026) |
|---|---|---|
| Novelty required? | Yes — previously unpublished research | No — but design methodology and detailed benchmarks of a built, large-scale system are expected |
| Anonymization | Full: authors, affiliations, self-references, acknowledgements | Author names hidden, but company names, product names, and URLs may remain |
| Typical author | Academic or industrial researcher with a new mechanism | Team reporting a production ML system's design and measured behavior |
| Cross-track submission | Forbidden to submit the same paper to both tracks | Same |

If the paper's strongest asset is deployment scale and operational insight rather than a new
idea, the industrial track is the honest home — reviewers there are told not to demand
novelty but will demand benchmark depth.

## Format audit (2026-cycle anchors)

- Two-column layout from the official style kit (`mlsys2026style.zip` in 2026, explicitly the
  same format as 2025). Do not touch margins, fonts, or spacing macros.
- Main body up to 10 pages, references excluded. Every reference must list **all** authors —
  no "et al." truncation in the bibliography; this is an explicit MLSys rule that automated
  `.bst` choices can silently violate.
- Appendices are unlimited but are uploaded **separately** from the main PDF, are due at the
  same time, and reviewers are not required to read them. Anything decision-critical —
  the key ablation, the baseline configuration table — must live in the 10 pages.
- Abstract, title, and author fields in OpenReview must match the PDF; the submission goes
  through the MLSys OpenReview group (in 2026: `MLSys.org/2026/Conference`).

## Anonymity model — stricter and looser than you expect

MLSys is double-blind **and** arXiv-tolerant: posting the paper publicly is allowed, but the
submitted PDF must still make a good-faith anonymization effort. Practical consequences:

- Strip affiliations, acknowledgements, and grant numbers; rewrite "our system X, deployed at
  <company>" phrasing in the research track.
- Self-citations stay in third person ("Prior work [12] showed...", not "In our prior work").
- Do not cite your own arXiv version in a way that equates it with the submission.
- GitHub links in a research-track submission should point to anonymized mirrors; the named
  repository comes back at camera-ready and artifact evaluation.

```bash
# Pre-upload leak sweep on the built PDF and source tree
pdfinfo paper.pdf | grep -iE 'author|producer'          # metadata identity
pdftotext paper.pdf - | grep -inE 'acknowledg|grant|@|github.com/[a-z0-9-]+' | head
grep -rinE 'copyright|institute|univers' *.tex | grep -v style | head
```

## Dual-submission rules

- Ineligible: any paper simultaneously under review elsewhere or already published.
- Explicitly allowed: arXiv/technical-report versions of the submission.
- Conditionally allowed: expanded versions of papers from workshops **with proceedings**,
  subject to program-chair approval — email the workshop paper to the chairs and explain the
  delta; reviewers judge the added contribution, not the whole paper.
- The industrial track applies the same no-concurrent-review rule.

## Desk-reject and triage table

| Trigger | Severity | Repair window |
|---|---|---|
| Body over 10 pages or modified style kit | Desk reject | None after the deadline |
| Identity leak in a research-track PDF | Desk reject or chair flag | None |
| Same paper in both tracks | Desk reject of both | None |
| Concurrent submission discovered | Reject plus venue-relations damage | None |
| References missing full author lists | Chair-level format flag | Before deadline only |
| Headline claim only supported in the appendix | Review-stage damage | Fixable in the writing pass |

## Final-week sequence for a systems paper

1. Freeze the evaluation: no new runs after this point except reviewer-anticipation ablations
   already scripted; late numbers breed inconsistent tables.
2. Rebuild every figure and table from logged results with one command, so the PDF and the
   future artifact cannot diverge.
3. Move one decision-critical element back from the appendix into the body — the most common
   MLSys structural error is a main paper that outsources its proof of work.
4. Run the anonymity sweep above on PDF, appendix, and any linked anonymous repo.
5. Verify the bibliography lists all authors per reference; regenerate with a compliant style.
6. Upload paper, then appendix (separate file), then re-open both from OpenReview as a
   logged-out check that the right files landed.

## OpenReview field audit

The form is part of the submission; mismatches between form and PDF surface at the worst
possible times (proceedings generation, conflict detection, notification email).

- Title and abstract: character-identical to the PDF — the form copy feeds the program
  and, on acceptance, the proceedings page.
- Author list: complete and ordered at submission time even though hidden from
  reviewers; adding an author later requires chair intervention.
- Conflicts: every author's DBLP-visible collaborators and institutions, including
  recent internships — MLSys's reviewer pool is small enough that a missed conflict is
  likely to actually bite.
- Subject areas: choose from the current CFP's list (systems-for-ML and ML-for-systems
  areas differ in reviewer routing); a mis-tagged paper draws the wrong culture of
  reviewer, which is a real scoring effect at this venue.
- Track selector: research vs industrial, irreversible after the deadline.
- Appendix upload slot: the separate file, confirmed present — an empty slot is a silent
  loss, not an error.

## Cycle-volatility warnings

- The 10-page limit, separate-appendix mechanic, style-kit name, and track structure are
  2026-cycle facts; the 2027 call may change any of them.
- No AI-use policy for authors was verifiable for the 2026 cycle (待核实) — check the current
  call rather than assuming either permission or prohibition.
- Deadlines in this pack's workflow skill are historical anchors, not next-cycle predictions.

## Output format

```text
[MLSys readiness] Ready / Needs fixes / Not ready
[Track] research / industrial / undecided (reason)
[Blocking checks] <pages/style/anonymity/appendix-split/references/dual-submission>
[Decision-critical content in body?] yes / no -> <what to pull forward>
[Desk-reject risk] <single highest risk>
[Fix order] <ordered fixes before upload>
```
