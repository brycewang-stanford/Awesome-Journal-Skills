---
name: icra-review-process
description: Use when explaining or strategizing around ICRA's review pipeline — the RAS Conference Editorial Board of Editors and Associate Editors, reviewer recruitment through PaperPlaza, the absence of an author rebuttal in the classic ICRA flow, the January accept/reject decision, and how this differs from RA-L's revise-capable journal review.
---

# ICRA Review Process

ICRA review is run not by ad-hoc program committees but by a standing RAS
**Conference Editorial Board (CEB)** structure operating inside PaperPlaza. The
mechanics differ enough from both journals and ML conferences that authors
mis-model them — most consequentially around the rebuttal that never comes.

## The pipeline

```text
Sep 15   PaperPlaza deadline
   │
   ▼     Editor (area lead) assigns paper to an Associate Editor (AE)
   │     by keyword match from your chosen PaperPlaza topics
   ▼
Oct-Dec  AE recruits 2-3 reviewers; reviews written on the standard
   │     RAS form (contribution, technical soundness, clarity,
   │     experimental validation, video comments)
   ▼
Dec-Jan  AE writes a summary report reconciling the reviews and
   │     recommends; Editors + program committee calibrate across areas
   ▼
Jan 31   accept or reject — no conditional accepts, no shepherding,
   │     and in the classic ICRA flow NO author rebuttal phase
   ▼
Mar      camera-ready with voluntary reviewer-driven revisions
```

Two structural notes. First, keyword choice at submission is not paperwork — it
routes the manuscript to an Editor's area and thereby to the reviewer pool most
or least sympathetic to it. Second, reviewer identity practice: reviewers are
anonymous to authors, and from the 2026 cycle authors are anonymous to reviewers
too (double-anonymous; before 2025 inclusive, single-blind). Policies are set
per cycle — confirm on the current year-site.

## No rebuttal: consequences, not complaints

The classic ICRA pipeline gives authors no reply channel between submission and
decision (individual cycles have experimented; verify the current one). Plan
for it:

- **The paper must anticipate objections in advance** — the limitations
  paragraph and pre-answered comparisons (`icra-writing-style`) do the job a
  rebuttal does elsewhere.
- **Misunderstandings are terminal.** If a reviewer misreads the method, no one
  corrects them before the AE summarizes. Ambiguity is therefore a first-order
  risk, worth spending page budget to eliminate.
- **The video is your asynchronous rebuttal.** It answers "is this real / is it
  cherry-picked / how fast" before those objections are typed
  (`icra-supplementary`).
- Reviews arrive *with* the decision, and for accepted papers they function as
  camera-ready guidance (`icra-author-response` covers using them well).

## What the review form rewards

| Form dimension | What strong looks like at ICRA |
|---|---|
| Technical soundness | assumptions stated; math checkable; no hidden human-in-the-loop |
| Experimental validation | evidence rung matches claims; trials, dispersion, failure analysis |
| Novelty/contribution | mechanism-level delta over named prior systems |
| Clarity | figure chain self-sufficient; task-first narrative |
| Multimedia | uncut executions, labeled speeds, failure shown |

Borderline papers typically die on validation ("promising but insufficient
experimental support") rather than novelty — allocate effort accordingly.

## Where author leverage actually exists

With no rebuttal, influence concentrates before upload:

1. **Keyword selection** — the only routing input you control; choose for the
   reviewer pool you want, within honesty.
2. **The video** — the one channel that reaches reviewers with evidence after
   the PDF freezes their reading order but before they form judgments.
3. **Ambiguity elimination** — every sentence a reviewer could misparse is a
   decision risk with no correction mechanism.
4. **The limitations paragraph** — converts predicted objections from "flaw
   found" to "flaw acknowledged," a materially different review sentence.

## Calibrating expectations

- ICRA is large (thousands of submissions; Vienna 2026 drew 8,000+ attendees);
  historical acceptance rates have floated in the 40-45% band, far gentler than
  ML flagship venues but with high variance across areas. Treat any specific
  rate as unverified until the year's numbers are published.
- Acceptance is to the program as a whole; presentation format (interactive/
  poster session structure) is a program decision, not a quality tier ranking
  in the proceedings record.
- Decisions are binary. "Reject with encouraging reviews" is the common fate of
  good-but-thin papers; the correct read is "fund one more experiment rung and
  resubmit" (IROS in March, RA-L any time).

## Contrast with RA-L review

Authors choosing between routes (see `icra-topic-selection`) should model the
review differences, not just the deadlines:

- RA-L is journal review: an AE plus reviewers, a first decision targeted
  within ~3 months, and crucially a **revise-and-resubmit** outcome that lets
  authors answer reviewers with a response letter — the interaction ICRA lacks.
- RA-L decisions bind publication in the journal; conference presentation is a
  separate transfer step afterward.
- The reviewer pools overlap heavily; a paper rejected at ICRA and sent to
  RA-L unchanged may meet the same reviewer with the same objection — revise
  first.

## Reading a decision packet

1. Sort comments into: factual error (yours), misunderstanding (their reading,
   your ambiguity), scope demand (wants a different paper), and taste.
2. Reject case: fix the first two categories before any resubmission clock; a
   misunderstanding at ICRA predicts the same misunderstanding at IROS.
3. Accept case: triage which comments to honor in camera-ready given the
   8-page-total final limit (`icra-camera-ready`).
4. Update your model: which claims drew fire predicts how to scope the next
   submission's evidence ladder.

## Output format

```text
[Stage] pre-submission / under review / decision received
[Pipeline model] AE area = <keyword>, predicted reviewer pool concern: <one line>
[No-rebuttal mitigation] top 3 objections pre-answered in draft: <list>
[Decision triage] factual / misunderstanding / scope / taste = <counts>
[Next move] camera-ready plan | resubmission target + what changes
```
