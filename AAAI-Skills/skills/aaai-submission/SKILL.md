---
name: aaai-submission
description: Use when auditing an AAAI main technical track submission for OpenReview readiness, double-blind anonymity, page limits, reproducibility checklist, supplementary material, author limits, multiple-submission policy, and AAAI AI-use policy compliance.
---

# AAAI Submission

Use this for an AAAI main technical track submission audit. Reopen the current conference page,
Author Kit, CFP, submission instructions, review process page, supplementary-material page, and
author policies before giving deadline-ready advice.

## Submission audit

- Confirm the target track: Main Track, AI for Social Impact, AI Alignment, or another AAAI program.
  Track-specific rules can differ.
- Verify OpenReview account/profile readiness, conflicts, author list, subject areas, and submission
  metadata before the abstract and paper deadlines.
- Check the current AAAI author kit. AAAI-26 submissions used AAAI two-column camera-ready style,
  US Letter PDF, and 7 pages of technical content plus pages solely for references and the
  reproducibility checklist.
- Confirm double-blind compliance in the PDF, file names, references to prior work, supplement,
  code/data, and metadata. Omit acknowledgments in the review version.
- Include the reproducibility checklist after references when current instructions require it.
- Enforce the author submission limit and author-change rules. AAAI-26 limited each author to 10
  combined technical-track submissions and did not allow authors to be added after submission.
- Check multiple-submission compliance. An AAAI submission under review cannot simultaneously be
  under review at another archival venue.
- Apply the current AAAI AI-use policy: editing/polishing author-written text may be allowed, but
  LLM-generated manuscript text, AI authorship, and AI-generated citations are policy risks.

## Blocking risks

- Over-limit technical content or malformed PDF.
- Missing reproducibility checklist.
- Identity leakage in paper, supplement, links, code, data, or prior-work citations.
- Author added after the allowed window.
- Concurrent archival submission.
- Web pointers to mutable supplementary material.
- Policy-violating LLM-generated text, hallucinated references, or plagiarism.

## Summary-reject screen

AAAI's large reviewer pool and high volume mean a desk-level or Phase-1 cut is the most likely way to
lose, so screen for the mechanical failures first.

| Check | Fast-fail trigger | Where it bites |
| --- | --- | --- |
| Page limit | technical content over the cap | desk return |
| Anonymity | author name in PDF, code, or metadata | policy reject |
| Checklist | missing or contradictory | Phase-1 distrust |
| Dual submission | concurrent archival venue | ethics reject |

## Pre-deadline evidence packet

Build a single review-version packet before the abstract deadline, then refresh it before final
submission. The packet is not a substitute for the official instructions; it is a way to make the
submission audit reproducible and to keep late fixes from creating new policy problems.

| Packet item | What to capture | Failure it prevents |
| --- | --- | --- |
| Policy snapshot | current conference page, Author Kit, submission instructions, supplementary-material rules, and AI-use policy checked dates | applying stale AAAI-26 facts to a later cycle |
| PDF proof | page count, paper size, style file, checklist placement, font/figure warnings, and metadata scrub result | desk return for formatting or anonymity |
| Author ledger | OpenReview profiles, conflicts, subject areas, author-limit count, and author-list freeze status | profile conflict, over-limit author, late author change |
| Supplement ledger | every appendix, multimedia, code/data ZIP, README, license note, and anonymous link policy decision | mutable web pointer or identity leak |
| Ethics ledger | dual-submission status, human-subjects/data constraints, AI-use disclosure, plagiarism/citation check | policy reject after submission |

For each item, record the evidence path and the person who can fix it. If a rule is uncertain, mark it
as "requires current chair/author-kit confirmation" instead of guessing.

## Anonymity sweep order

Run anonymity checks in a fixed order so fixes do not reintroduce leaks:

1. PDF text: names, affiliations, acknowledgments, grants, self-identifying project names, and obvious
   self-citations.
2. PDF metadata: title, author, producer, comments, embedded attachments, and file name.
3. References: prior work phrased as "our previous" or "submitted to" when blind citation would be
   required.
4. Supplement: ZIP names, directory names, notebooks, comments, plots, data paths, license files, and
   executable logs.
5. External references: GitHub, project pages, anonymous archives, videos, demos, or issue trackers.
6. OpenReview metadata: author list, conflicts, subject areas, institutional hints in abstract or
   keywords.

The output should separate "must fix before submission" from "acceptable but document why." Do not rely
on a single manual skim; use PDF metadata tools, archive listing, and text search when available.

## Worked vignette

A robotics-learning team has 7 strong technical pages but left an acknowledgments line and a GitHub
URL with their lab name in the supplement. The audit flags anonymity as the highest summary-reject
risk: the fix order is strip the acknowledgment, replace the link with an anonymous archive, scrub
ZIP metadata, then re-export and re-run the anonymity sweep before the paper deadline.

## Output format

```text
[AAAI readiness] Ready / Needs fixes / Not ready
[Track] Main / AI for Social Impact / AI Alignment / other
[Blocking checks] <page/anonymity/checklist/supplement/author-limit/dual-submission/AI-policy>
[Highest summary-reject risk] <one issue>
[Fix order] <ordered fixes before submission>
```
