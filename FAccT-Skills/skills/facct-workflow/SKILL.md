---
name: facct-workflow
description: Use when planning an ACM FAccT project timeline from venue fit through abstract registration, OpenReview submission, the Accept/Revise/Reject decision, the combined revision-plus-rebuttal round, camera-ready, and presentation, with backward-planning offsets for an interdisciplinary responsible-AI paper and honest handling of the single annual deadline.
---

# FAccT Workflow

Use this as the project-management skill for a FAccT submission. Replace every date with the current
official Important Dates page and work backwards from the **abstract-registration deadline**, which
precedes the paper deadline and is a hard gate: miss it and OpenReview will not accept your PDF.
FAccT runs a **single annual research deadline** — since FAccT 2027 it falls in late October /
early November of the year *before* the conference — and a genuine **Revise-and-resubmit** round
(introduced in 2026) sits inside the review cycle, so plan for a possible revision, not just an
accept/reject. Every author must also sign up to review (FAccT 2027), so put that form on the plan.

FAccT is a conference with **no standing editor-in-chief**; leadership is the per-edition General
Chairs and Program Chairs (FAccT 2027 Program Chairs per the CFP: Remi Denton, David Leslie, Aurelia
Tamò-Larrieux, Isabel Valera — a blog byline lists a different four, 待核实; 2027 General Chairs not
yet announced; checked 2026-11-24). Chairs rotate yearly; re-check the committees page rather than
carrying a name forward. Since 1 January 2026 all ACM proceedings are **Open Access**, so budget for
the ACM Open / APC question early rather than at camera-ready.

## Milestones (FAccT 2027 calendar as the worked example)

- **Venue fit:** confirm FAccT over a pure-ML/HCI/law venue and confirm the contribution is
  fairness/accountability/transparency-first (`facct-topic-selection`).
- **Abstract registration:** submit real title, abstract, authors, and **focus areas** by the
  abstract deadline (FAccT 2027: **27 October 2026**). This gate cannot be reopened, and the
  author list and archival/non-archival choice freeze here.
- **Paper submission:** upload the anonymized acmart PDF with its endmatter statements
  (FAccT 2027: **3 November 2026**).
- **Reviews + first-round decision:** Accept / **Revise (major or minor)** / Reject, released with
  the reviews and meta-review (FAccT 2027: **22 December 2026**). There is no separate rebuttal
  before this decision in 2027 (FAccT 2026 had one, due 24 February 2026).
- **Revision + rebuttal (if Revise):** address the Area-Chair-prioritized concerns, submit the
  revised paper (up to 15 pages) with a rebuttal (FAccT 2027: **28 January 2027**); re-reviewed by
  the same reviewers and AC.
- **Final notification:** Accept (with minor revisions) / Reject (FAccT 2027: **23 March 2027**).
- **Camera-ready:** FAccT 2027 date **TBD** on the CFP (FAccT 2026 used two: 24 April for round-1
  accepts and 11 May 2026 for Revise accepts).
- **Present:** every accepted paper — archival or non-archival — is presented at the conference,
  in person by default with a virtual option (FAccT 2027: Porto, Portugal, **June 21-24, 2027**).

## Backward plan from the paper deadline

| Weeks out (heuristic) | Interdisciplinary-responsible-AI milestone |
|---|---|
| 10+ | Research/critical question fixed; affected populations and disciplinary lane named |
| 8 | Data collected / interviews done / legal-doctrinal analysis drafted; provenance and consent logged |
| 6 | Analysis complete; disaggregated results or qualitative codes done; limitations drafted alongside |
| 4 | Full draft in the acmart template; endmatter statements drafted (ethics, adverse impacts) |
| 3 | Internal mock review by a reader *outside* your discipline (the mixed-reviewer stress test) |
| 2 | Harm/limitations hardened; related-work delta across disciplines sharpened; page budget met |
| 1 | Anonymity sweep (strip positionality/acks); Generative AI Usage Statement written; focus areas set |
| 0 | Abstract registered by its earlier gate, then paper + endmatter on OpenReview |

These offsets are planning heuristics only — anchor every one to the current Important Dates page,
never to a previous cycle.

## The single-deadline calendar reality

FAccT runs **one annual research deadline**. As of 2026-11-24 the FAccT 2027 paper deadline
(3 November 2026) has passed and the cycle is in review; the next open target is **FAccT 2028**,
whose call is not yet published — expect a similar autumn deadline, but do not plan on a date until
it is posted. Two planning consequences:

- **Missing the annual deadline costs roughly a year** at FAccT; if the work is time-sensitive, a
  sibling venue (AIES, a fairness-focused ML workshop, or a CHI/CSCW deadline) or the CRAFT track
  may have a nearer date — factor that into routing rather than idling.
- **A Revise decision keeps you inside the same cycle** (revision deadline weeks after
  notification), not a year later — the revision window in 2027 is about five weeks over the
  December holidays (22 Dec 2026 to 28 Jan 2027); confirm it still exists and re-read its exact
  timing before relying on it.

## Failure modes by stage

- **Missing the abstract-registration gate** — the single most common fatal error; without a
  registered abstract and focus areas there is no paper slot at all.
- **Leaving endmatter statements to the final night** — a rushed Ethical Considerations or Adverse
  Impacts statement reads as an afterthought to reviewers who take reflexivity seriously.
- **Skipping the cross-discipline mock review** — forfeits the one chance to hear "a lawyer/social
  scientist will not accept this framing" from a friend instead of a reviewer.
- **Treating a Revise as a guaranteed accept** — the re-review is real; budget the short revision
  window like a deadline.
- **Positionality/acknowledgement leak** — placing an identity-revealing statement in the anonymous
  submission is an anonymity violation, not a virtue.

## Coordination notes

- Assign one owner for the **endmatter statements** (ethics, adverse impacts, Generative AI Usage)
  and another for the **anonymity sweep**; shared ownership is how both slip.
- Archive the exact submitted PDF and, later, the revised PDF and its rebuttal — the re-review
  quotes them and the response must map each reviewer concern to a change.

## Output format

```text
[Current stage] idea / evidence / writing / registration / submitted / revise + rebuttal / accepted
[Next official deadline] <date and source, or unknown>
[Critical path] <three tasks that determine readiness>
[Risk register] <abstract gate / anonymity / endmatter statements / evidence / revision window / presentation>
[Owner map] <task -> person or role>
```
