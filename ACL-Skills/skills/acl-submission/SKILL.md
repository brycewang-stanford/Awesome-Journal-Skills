---
name: acl-submission
description: Use when auditing an ACL submission before an ACL Rolling Review cycle deadline, covering long/short paper page budgets, the mandatory Limitations section, Responsible NLP checklist, anonymized PDFs and supplements, preprint declarations, dual-submission rules, resubmission linking, and ARR desk-reject triggers on OpenReview.
---

# ACL Submission

Run this audit before uploading to an ACL Rolling Review (ARR) cycle on OpenReview.
ACL papers are not submitted to the conference directly: they enter an ARR cycle,
collect reviews and a meta-review, and are later *committed* to ACL. Reopen the
current ARR CFP at aclrollingreview.org/cfp and the target conference's call
before trusting any number below.

## Two-step reality check

- Confirm which ARR cycles feed your target ACL edition. ACL 2026 accepted work
  from the October 2025 and January 2026 cycles; committing requires a complete
  review package, so the last eligible cycle is earlier than the conference date
  suggests.
- The ARR deadline is the hard one. Commitment is a separate, later form with its
  own deadline (March 14, 2026 for ACL 2026) — see `acl-workflow` for the calendar.
- All ARR deadlines run 11:59 pm UTC-12 (anywhere on Earth).

## Format gate

- Long papers: up to 8 content pages. Short papers: up to 4. Both get unlimited
  pages for references, plus unlimited space after the conclusion for the
  **required Limitations section** and an optional ethics statement.
- A missing Limitations section or overlength content is an explicit desk-reject
  condition under the ARR CFP — this is the most common self-inflicted rejection.
- Use the official ACL LaTeX/Word style files unmodified; margin, font, or
  spacing tampering is treated as a length violation.
- Appendices go after references in the same PDF; reviewers are not obliged to
  read them, so the 8 or 4 content pages must carry the whole argument.

## Anonymity gate

- The submission itself must be fully anonymized: no names, affiliations,
  acknowledgements, or self-revealing "we previously showed" citations.
- Since January 2024 there is **no anonymity period**: you may post a
  non-anonymous preprint at any time. But you must declare preprint status at
  submission, and choosing "no non-anonymous preprint" earns award eligibility
  and priority for borderline decisions — then posting one anyway before
  meta-review release is a desk-reject offense.
- Supplementary archives, repo links, and dataset pages must be anonymized too;
  links to tracked hosting (personal Dropbox/Drive) are disallowed.

## Declarations that gate the submission form

| Form item | What ARR checks | Failure mode |
|---|---|---|
| Responsible NLP checklist | Completed, consistent with the PDF | Misleading answers → desk reject |
| Resubmission link | Prior ARR submission ID + change summary | Unacknowledged resubmission → desk reject |
| Preprint declaration | Matches what is actually on arXiv | Broken "no preprint" pledge → desk reject |
| Dual submission | Not under review anywhere archival | Violation → reject at ARR or venue |
| AI assistance disclosure | Checklist item E answered honestly | Undisclosed generative-AI use → policy breach |

## Resubmission discipline

ARR is built for revise-and-resubmit across cycles. If this paper was reviewed
in an earlier cycle:

1. Link the previous submission ID in the form — omitting it is desk-rejectable.
2. Attach a summary of changes plus a point-by-point response to every weakness
   named in the old reviews.
3. If the previous meta-review scored 1, a resubmission within six months
   without wholesale revision can be desk rejected; cosmetic edits waste a cycle.
4. Decide whether to request the same reviewers — continuity helps when the
   revision genuinely answers them.

## Final-72-hours sequence for an NLP paper

1. Rebuild the PDF from the untouched style files and re-run the page count on
   content pages only.
2. Re-read Limitations: it must be substantive (scope, languages, data,
   compute), not a ritual paragraph.
3. Fill the Responsible NLP checklist against the actual PDF — every "yes"
   needs a section number.
4. Sweep the supplement archive for author names in paths, notebook metadata,
   git history, and license headers.
5. Verify title/abstract on OpenReview match the PDF, and the preprint
   declaration matches arXiv reality.
6. Submit hours early; ARR deadlines are AoE but OpenReview outages are not an
   accepted excuse.

## Cycle-choice quick checks

- Is the target conference actually accepting commitments from this cycle?
  Each edition names its eligible cycles; a mismatch strands the reviews.
- Does the team have bandwidth during this cycle's author-response window,
  roughly five weeks after the deadline?
- Would waiting one cycle allow the missing experiment that reviews will
  otherwise demand? A weak first cycle costs more than it saves, because the
  package follows the paper.
- Is any co-author's other submission in the same cycle a conflict for
  reviewer assignment? Register conflicts and profiles before deadline week.

## Frequently mishandled cases

- **Short paper padded to eight pages**: reviewers rate contribution against
  format; a four-page idea submitted long scores as thin, not as generous.
- **Appendix used as overflow body**: content pages must carry the argument;
  a method section that says "see Appendix B" for its core mechanism fails
  the self-containedness expectation.
- **arXiv v2 posted mid-cycle** after declaring no preprint: this converts a
  declaration into a desk-reject liability — update plans, not the preprint.
- **Dataset "available on request"**: allowed, but checklist answers must
  then explain reproduction honestly rather than implying release.
- **Same work at a non-archival workshop**: usually permitted, but most
  \*ACL workshop proceedings ARE archival — verify the workshop's archival
  status in writing before assuming.

## Output format

```text
[ARR readiness] Ready / Needs fixes / Not ready
[Cycle + venue plan] <ARR cycle -> intended commitment venue>
[Format gate] <length/Limitations/style-file findings>
[Anonymity + declarations] <checklist/preprint/resubmission/dual-submission findings>
[Desk-reject risks] <ranked list>
[Fix order] <what to change before the cycle deadline>
```
