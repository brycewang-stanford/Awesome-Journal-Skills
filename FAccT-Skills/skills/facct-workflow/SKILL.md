---
name: facct-workflow
description: Use when planning an ACM FAccT project timeline from venue fit through abstract registration, OpenReview submission, the rebuttal window, the new Accept/Revise/Reject revise-and-resubmit round, two-round camera-ready, and in-person presentation, with backward-planning offsets for an interdisciplinary responsible-AI paper and honest handling of the single annual deadline.
---

# FAccT Workflow

Use this as the project-management skill for a FAccT submission. Replace every date with the current
official Important Dates page and work backwards from the **abstract-registration deadline**, which
precedes the paper deadline and is a hard gate: miss it and OpenReview will not accept your PDF.
FAccT runs a **single annual research deadline**, and — new for the 2026 edition — a genuine
**Revise-and-resubmit** round sits inside the review cycle, so plan for a possible revision, not just
an accept/reject.

FAccT is a conference with **no standing editor-in-chief**; leadership is the per-edition General
Chairs and Program Chair (FAccT 2026: General Chairs Su Lin Blodgett and Zeerak Talat, PC Chair
Michael Madaio, verified 2026-07-09). Chairs rotate yearly; re-check the committees page rather than
carrying a name forward. Since 1 January 2026 all ACM proceedings are **Open Access**, so budget for
the ACM Open / APC question early rather than at camera-ready.

## Milestones (FAccT 2026 calendar as the worked example)

- **Venue fit:** confirm FAccT over a pure-ML/HCI/law venue and confirm the contribution is
  fairness/accountability/transparency-first (`facct-topic-selection`).
- **Abstract registration:** submit real title, abstract, authors, and **focus areas** by the
  abstract deadline (FAccT 2026: **8 January 2026**). This gate cannot be reopened.
- **Paper submission:** upload the anonymized acmart PDF with its endmatter statements
  (FAccT 2026: **13 January 2026**).
- **Preliminary reviews + rebuttal:** reviews released (FAccT 2026: **20 February 2026**); a short
  rebuttal window for **factual corrections**, not debate.
- **First notification:** Accept / **Revise** / Reject (FAccT 2026: **2 March 2026**).
- **Revision (if issued):** address Area-Chair-prioritized concerns and resubmit by the revision
  deadline (FAccT 2026: **25 March 2026**); re-reviewed before a final decision.
- **Camera-ready:** Round-1 accepts (FAccT 2026: **24 April 2026**); Revise-and-resubmit accepts
  (FAccT 2026: **11 May 2026**).
- **Present:** every accepted paper — archival or non-archival — is presented at the conference
  (FAccT 2026: Montréal, **June 25-28, 2026**).

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

FAccT runs **one annual research deadline**. As of 2026-07-09 the FAccT 2026 edition has just
concluded in Montréal, so the live next target is **FAccT 2027** (dates/venue 待核实). Two planning
consequences:

- **Missing the annual deadline costs roughly a year** at FAccT; if the work is time-sensitive, a
  sibling venue (AIES, a fairness-focused ML workshop, or a CHI/CSCW deadline) or the CRAFT track
  may have a nearer date — factor that into routing rather than idling.
- **A Revise decision keeps you inside the same cycle** (revision deadline weeks after
  notification), not a year later — but this revise-and-resubmit round is **new for 2026**, so
  confirm it still exists and re-read its exact timing before relying on it.

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
- Archive the exact submitted PDF and, later, the rebuttal and revision response — the re-review
  quotes them and the response must map each reviewer concern to a change.

## Output format

```text
[Current stage] idea / evidence / writing / registration / submitted / rebuttal / revise / accepted
[Next official deadline] <date and source, or unknown>
[Critical path] <three tasks that determine readiness>
[Risk register] <abstract gate / anonymity / endmatter statements / evidence / revision window / presentation>
[Owner map] <task -> person or role>
```
