---
name: cikm-submission
description: Use when auditing a CIKM submission for EasyChair readiness across the five tracks, covering page budgets with appendices counted inside, the mandatory GenAI Usage Disclosure section, author-reviewer nomination, double-blind rules with arXiv declaration, the abstract-gate authorship freeze, and desk-reject triggers.
---

# CIKM Submission

A CIKM submission clears three gates that generic conference checklists miss: an
EasyChair form with consequences (track selection, reviewer nomination, arXiv
declaration), a page budget that counts appendices inside it, and a named
GenAI Usage Disclosure section that must physically exist in the PDF. All specifics
below are the verified CIKM 2026 rules (source map, 2026-07-08); reopen the current
track call and policies page before certifying anything.

## Per-track budget card (2026)

| Track | Budget | Outside the budget |
|---|---|---|
| Full Research | 10 pages incl. figures, tables, **appendices** | up to 2 pages of references + GenAI disclosure |
| Short Research | 4 pages incl. appendix | references + GenAI disclosure |
| Applied Research | 7 pages incl. appendix | references + GenAI disclosure |
| Resource | 4 pages incl. appendices and acknowledgments | references + GenAI disclosure |
| Demonstration | 4 pages incl. appendices and acknowledgments | references + GenAI disclosure |

All tracks: ACM proceedings template (two-column), English, PDF. Applied Research
additionally requires practical-application evidence — a system launch, data
release, or equivalent — as part of the claim, not as decoration.

## The EasyChair form is part of the submission

- **Track selection.** Each track has a named EasyChair choice (e.g., "CIKM 2026 Full
  Research Track"); a paper filed under the wrong track competes under the wrong
  budget and criteria.
- **Author-reviewer nomination.** Every submission must nominate at least one of its
  authors to review for the conference, set inside EasyChair at submission time.
  CIKM 2026 states plainly that failure to nominate leads to desk rejection — treat
  the nomination as a required field, assign the most senior eligible author, and
  record who was named.
- **arXiv declaration.** If a non-anonymized version is online, or will go online
  before notification, that must be declared on the form. Not disclosing an existing
  public version is itself a desk-reject trigger — the risk is the silence, not the
  preprint.

## GenAI Usage Disclosure section

Every CIKM 2026 submission includes a section titled for GenAI usage disclosure,
placed after the main content and appendix and before the references, uncounted.
It must cover generative-AI use in *all* stages — research design, code, data, and
writing. Write it factually and specifically ("code assistants used for evaluation
scripts; no generated text in the manuscript" beats boilerplate), because the
conference reserves the right to run automated compliance checks against the ACM AI
policy. A missing section is a compliance failure on an explicitly stated rule.

## Anonymity sweep

Third-person self-citations; no author names, affiliations, acknowledgments, or
grant numbers; no identifying repository URLs, dataset host paths, or PDF metadata;
screenshots and demo figures scrubbed of usernames and org names. For Applied
Research papers this is the hard case — "deployed at our company" phrasing must
stay, but the company must not be inferable from logos, product names, or traffic
numbers only one operator could have.

## Abstract-gate week (the underestimated deadline)

The full-track abstract deadline sits one week before the paper deadline (May 16 vs
May 23 in 2026) and does more than reserve a slot:

- **Authorship freezes there.** The ACM authorship policy plus CIKM's explicit
  no-changes rule mean a collaborator not listed at the abstract gate cannot be
  added later — settle authorship debates the week before, not the night of.
- **The track choice is effectively made there**, since the abstract enters one
  track's EasyChair queue. Re-routing later means withdrawing and resubmitting,
  feasible only before the paper gate.
- **Title and abstract feed reviewer bidding.** In an EasyChair pool spanning three
  communities, a vague abstract draws the wrong lane's reviewers. Name the task,
  the data type, and the mechanism family so the right specialists bid — this is
  the cheapest review-quality lever the authors control.

## Template pitfalls specific to this stack

- Use the current ACM template configured for anonymous review; stale copies from a
  co-author's previous ACM paper are the usual source of format drift.
- `\authornote`, running headers, and PDF creator metadata leak identity even when
  the title block is clean — check document properties, not just the rendered page.
- The GenAI Usage Disclosure and references must appear in that order after the
  appendix; a disclosure section placed after the references technically violates
  the stated placement.
- ACM class options change what counts as a page; measure the budget in the exact
  submission configuration, since the camera-ready configuration differs.

## Sequenced final check

```text
1. Track call reopened; budget and template confirmed for THIS track
2. Page count measured with appendices in — trim to budget, not to hope
3. GenAI Usage Disclosure section present, specific, correctly placed
4. Anonymization pass: text, figures, metadata, links
5. EasyChair: correct track selected; reviewer nomination completed and logged
6. arXiv/public-version status declared truthfully
7. Abstract gate met a week early — title/abstract/authors frozen there
8. No concurrent submission of this work anywhere else (hard ban)
```

## Desk-reject ledger

| Trigger | Why it fires at CIKM |
|---|---|
| Missing reviewer nomination | Explicitly stated 2026 consequence |
| Undeclared public non-anonymized version | Explicitly stated 2026 consequence |
| Over budget once appendices are counted | Budget includes appendices by rule |
| Identity leakage in PDF or metadata | Double-blind policy |
| Concurrent submission elsewhere | Originality policy, no exceptions |
| Missing/hollow GenAI disclosure section | ACM AI-policy compliance, automated checks reserved |

## Output format

```text
[Verdict] submit / fix first / do not submit
[Track + budget] <track, measured pages vs limit>
[Form items] nomination: done? / arXiv declared? / track label correct?
[Compliance] GenAI section / anonymity / dual-submission
[Ordered fixes] <shortest path to a clean upload>
```
