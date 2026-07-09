---
name: eacl-submission
description: Use when auditing an EACL submission before its single ACL Rolling Review cycle deadline, covering ACL-template compliance, the 8-page long / 4-page short content caps, the mandatory Limitations section, the Responsible NLP checklist, anonymization, preprint and resubmission declarations, and the no-fallback-cycle timing trap.
---

# EACL Submission

Run this audit before uploading to the ACL Rolling Review (ARR) cycle that feeds your target
EACL edition. EACL papers are never submitted to the conference directly: they enter an ARR
cycle on OpenReview, collect reviews and a meta-review, and are later *committed* to EACL,
which decides main / Findings / reject. Reopen the current EACL CFP and `aclrollingreview.org/cfp`
before trusting any number below.

## The one-cycle reality (EACL's defining trap)

- Confirm **which single ARR cycle feeds your edition, and treat it as unrepeatable.** For
  EACL 2027 the organizers named the **August 3, 2026 cycle the only viable cycle** — the
  conference sits early in the year, so there is **no later cycle to slip into**. Unlike ACL,
  a missed or wasted cycle here loses the whole edition.
- The ARR deadline is the hard one. **Commitment is a separate, later step** (October 11, 2026
  for EACL 2027) — see `eacl-workflow`.
- With no fallback, a thin-but-submittable draft is a real dilemma: submitting burns the only
  cycle, skipping loses the year. Decide deliberately, not by deadline reflex.

## Format gate

- Long papers: up to **8 content pages**. Short papers: up to **4**. Both get unlimited pages
  for references and appendices, plus unlimited space after the conclusion for the **required
  Limitations section** and an optional ethics statement.
- A missing Limitations section or overlength content is an explicit desk-reject condition
  under the ARR CFP — the most common self-inflicted rejection.
- Use the official ACL LaTeX/Word style files unmodified; margin, font, or spacing tampering
  is treated as a length violation and can be rejected without review.
- Appendices go after references in the same PDF; reviewers are not obliged to read them, so
  the 8 or 4 content pages must carry the whole argument.

## Anonymity gate

- The submission must be fully anonymized: no names, affiliations, acknowledgements, or
  self-revealing "in our prior work we showed" citations.
- Since January 2024 there is **no anonymity period**: a non-anonymous preprint is allowed at
  any time. But declare preprint status at submission; choosing "no non-anonymous preprint"
  earns award eligibility and borderline priority — then posting one anyway before meta-review
  release is a desk-reject offense.
- Supplementary archives, repo links, and dataset pages must be anonymized too; links to
  personally identifying hosting are disallowed.

## Declarations that gate the ARR form

| Form item | What ARR checks | Failure mode |
|---|---|---|
| Responsible NLP checklist | Completed, consistent with the PDF | Misleading answers → desk reject |
| Resubmission link | Prior ARR submission ID + change summary | Unacknowledged resubmission → desk reject |
| Preprint declaration | Matches what is actually on arXiv | Broken "no preprint" pledge → desk reject |
| Dual submission | Not under review anywhere archival | Violation → reject at ARR or EACL |
| AI assistance disclosure | Checklist item answered honestly | Undisclosed generative-AI use → policy breach |

## Long vs short

A **short paper is a genre, not a truncated long paper**: one claim, four pages. A compressed
eight-page study reads as thin (see the fastText exemplar in
`../../resources/exemplars/library.md`). See `eacl-topic-selection` for the full choice.

## Final-72-hours sequence for an NLP paper

1. Rebuild the PDF from the untouched style files and re-run the page count on **content pages
   only**.
2. Re-read Limitations: it must be substantive (languages, data, compute, scope), not a ritual
   paragraph.
3. Fill the Responsible NLP checklist against the actual PDF — every "yes" needs a section
   number.
4. Sweep the supplement archive for author names in paths, notebook metadata, git history, and
   license headers.
5. Confirm the OpenReview title/abstract match the PDF and the preprint declaration matches
   arXiv reality.
6. Submit hours early; ARR deadlines are AoE but OpenReview outages are not an accepted excuse,
   and there is no next cycle.

## Frequently mishandled cases

- **Assuming a fallback cycle exists.** For a single-cycle edition it does not; plan as if this
  is the only attempt.
- **Appendix used as overflow body.** Content pages must carry the argument; "see Appendix B"
  for a core mechanism fails self-containedness.
- **arXiv v2 posted mid-cycle** after declaring no preprint: a desk-reject liability.
- **Dataset "available on request":** allowed, but checklist answers must then explain
  reproduction honestly rather than imply release.

## Output format

```text
[ARR readiness] Ready / Needs fixes / Not ready
[Cycle plan] <single viable cycle -> EACL edition; fallback = none>
[Format gate] <length/Limitations/style-file findings>
[Anonymity + declarations] <checklist/preprint/resubmission/dual-submission findings>
[Desk-reject risks] <ranked list>
[Fix order] <what to change before the one cycle deadline>
```
