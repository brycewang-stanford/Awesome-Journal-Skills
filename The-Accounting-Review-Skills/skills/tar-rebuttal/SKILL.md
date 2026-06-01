---
name: tar-rebuttal
description: Use when drafting the revision and response letter after a The Accounting Review (TAR) revise-and-resubmit — structuring point-by-point responses to the editor and the (minimum two) reviewers across a multi-round developmental process, including identification, contribution, and data-authenticity demands. Drafts the response after revisions; it does not interpret the decision letter (tar-review-process).
---

# R&R Response & Rebuttal (tar-rebuttal)

## When to trigger

- You received a TAR R&R and have planned the revision (via `tar-review-process`)
- You have made (or scoped) the manuscript and code changes and need to write the response document
- You must reconcile conflicting reviewer demands for the editor to adjudicate
- A later-round decision asks you to defend or further revise prior changes

> Write the response **after** revising the manuscript and the code, not before — the letter
> documents changes you have made, not promises. TAR's process is developmental and typically
> multi-round; resubmit the revised manuscript and response through Editorial Manager
> (editorialmanager.com/accr), keep anonymity intact, and remember the revised submission still
> respects the **55-page** budget (references, tables, figures, appendices included).

## Response-document structure

1. **Opening letter to the editor.** Thank the editor and reviewers; summarize the most important
   changes in 2–4 sentences; explicitly state how you addressed the **editor's stated priorities**.
   Note where reviewers conflicted and how you resolved it.
2. **Per-reviewer sections.** For each reviewer (a minimum of two), restate every comment verbatim
   or faithfully numbered, then respond.
3. **Point-by-point format** for each comment:
   - **Comment** (quoted/numbered)
   - **Response** (what you did and the economic/econometric reasoning)
   - **Location** (section/page/table where the change appears)
   - Quote new manuscript text where helpful.

## How to respond to TAR's signature demands

- **"Identification is not clean."** Add or strengthen the design — pre-trends/dynamic effects, a
  better instrument, a placebo/falsification test, an alternative shock, or a robustness battery —
  and explain why it resolves the threat (see `tar-methods`, `tar-data-analysis`). Do not argue the
  endogeneity away in prose alone.
- **"The contribution is incremental."** Sharpen what the accounting field learns and reconcile with
  the conflicting prior results; revise the contribution sentences, not just citations (see
  `tar-contribution-framing`, `tar-literature-positioning`).
- **"Show the data are authentic / share the code."** Provide the data description and **processing
  computer code** for public databases, the abstraction methodology plus code for abstracted data,
  or sufficient detail / corroborating parties for private data — this is a TAR requirement, not a
  courtesy.
- **"Add a test / robustness."** An additional specification, partition, or (for behavioral work) a
  follow-up experiment that nails the mechanism is often decisive — but watch the 55-page budget;
  heavy new material usually lives in an online appendix so the main body stays within limit.

## Tone and tactics

- **Be respectful and substantive.** Reviewers are colleagues investing in your paper; engage
  seriously even when disagreeing.
- **Concede gracefully** where they are right; make the change.
- **Disagree with evidence, not assertion.** If you decline a request, give an economic/empirical
  reason and, where possible, an alternative analysis showing robustness.
- **Address every point.** A non-trivial point left unanswered reads as evasion and can sink a round.
- **Surface conflicts to the editor.** When reviewers ask for opposite things, explain the trade-off
  and your chosen resolution for the editor to adjudicate.
- **Preserve anonymity** in the resubmission and keep the revised files reproducible.

## Checklist

- [ ] Manuscript and code actually revised before the letter was written
- [ ] Editor's priorities addressed first and explicitly in the opening letter
- [ ] Every reviewer comment (min. two reviewers) restated and answered (none skipped)
- [ ] Each response names the location of the change and quotes new text where useful
- [ ] Identification and contribution demands met with real changes, not citations only
- [ ] Data-authenticity / code-access requests satisfied per data type
- [ ] Declined requests justified with evidence and an alternative test where possible
- [ ] Reviewer conflicts surfaced and resolved for the editor; 55-page budget respected

## Anti-patterns

- Writing the response before making the changes (or before updating the code).
- Skipping or burying an inconvenient comment.
- Answering "we added a citation" to a "deepen the contribution" or "fix identification" request.
- Arguing endogeneity away in prose with no new test.
- Declining a request by assertion ("we believe this is fine") with no evidence.
- Silently siding with one reviewer when two conflict, leaving the editor to discover it.

## Output format

```
【Decision round】1st R&R / 2nd round / ...
【Editor priorities addressed】1... 2... 3...
【Per-reviewer coverage】R1: x/x comments, R2: x/x (+R3 if any) — all answered? yes/no
【Major changes】identification: ... contribution: ... new test/study: ...
【Data authenticity】code/description provided per data type? yes/no
【Declined requests + justification】...
【Reviewer conflicts resolved】...
【Budget】revised main body ≤ 55 pages? overflow → online appendix
【Next step】resubmit via Editorial Manager; on next decision → tar-review-process
```
