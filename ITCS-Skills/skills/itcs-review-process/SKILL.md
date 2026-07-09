---
name: itcs-review-process
description: Use to model the ITCS reviewing pipeline — a program committee plus external reviewers, conceptual-novelty weighting, lightweight double-blind, no author-response/rebuttal phase, and a single accept/reject decision — and to understand where the (limited) author leverage actually is.
---

# ITCS Review Process

Understanding how ITCS decides tells you where your effort matters — and at ITCS, almost all of
it matters *before* the deadline, because there is **no rebuttal, no revise-and-resubmit, and no
second round.** The submission is judged as it stands. This skill models the pipeline so you can
calibrate expectations and pre-empt the objections you will never get to answer.

## The pipeline

1. **Registration then submission.** Title/abstract/authors/conflicts lock ~2 days before the
   paper (early September); the abstract drives PC bidding. Then the anonymized full PDF with
   complete proofs is uploaded to HotCRP.
2. **PC + external review.** A program committee (order of a few dozen members) handles the load;
   PC members review directly or solicit **external reviewers** (subreferees) for expertise. The
   PC — not the external reviewers — owns the decisions.
3. **Reviewing on the novelty axis.** Reviewers are briefed to weight **conceptual contribution**
   — a new model, question, or connection — over incremental technical depth. "Is this a new
   question worth asking, and is the model alive?" carries more weight than "is this the year's
   hardest theorem?" (contrast STOC/FOCS; see
   [`itcs-topic-selection`](../itcs-topic-selection/SKILL.md)).
4. **PC decision.** The committee reaches **accept/reject**. There is **no Major Revision**
   category and **no author-response phase** — the reviews are formed and the decision made
   without your input.
5. **Notification (~November)**, then camera-ready for LIPIcs.

## Lightweight double-blind, precisely

- The submitted PDF omits **author names, affiliations, and emails**; the prose avoids
  identity-revealing self-reference.
- But it is **lightweight**: the **reference list is not anonymized**, and authors are
  **encouraged to post a non-anonymous full version** to arXiv/ECCC/ePrint. Reviewers are not
  forbidden from encountering the preprint. The blinding reduces first-impression bias; it does
  not attempt airtight anonymity.
- Some editions have handled this as a "reveal after initial review" middle ground; treat the
  exact mechanism as cycle-volatile and read the current call (see
  [`../../resources/official-source-map.md`](../../resources/official-source-map.md)).

## The no-rebuttal reality

This is the single biggest difference from many CS venues, and it reshapes strategy:

- **You cannot correct a misunderstanding after the fact.** If a reviewer misreads your model or
  doubts your novelty, the paper must have forestalled it *in the text*.
- **The submission is the whole argument.** Everything a depth venue's authors would save for a
  rebuttal — the "is it trivial?" defense, the novelty delta, the scope caveats — must be present
  at upload.
- **See [`itcs-author-response`](../itcs-author-response/SKILL.md)** for how to operate when there
  is no response phase, and how the pre-emption work happens inside the paper.

## Where the (limited) leverage is

| Stage | Leverage | How to use it |
|---|---|---|
| Before submission | **High** | Pre-empt the three objections (trivial? new? why-care?) in the paper; prove the anchoring result in full |
| Abstract/registration | Medium | A precise, honest abstract improves PC bidding and reviewer match |
| Preprint | Low-medium | A clear full version helps a reviewer who wants more detail (allowed under lightweight double-blind) |
| After reviews arrive | **~None** | No rebuttal; reviews are usually returned with the decision |
| After reject | Medium (next venue) | Reviews are typically substantive; use them to sharpen a STOC/FOCS/SODA or journal resubmission |

## What reviewers are looking for (calibrate to these)

- **A genuinely new idea**, checkably new against the ITCS/ICS back-catalog and the connected
  area.
- **A model that is alive** — an anchoring separation/possibility/impossibility result.
- **Complete, correct proofs** of every central claim (the appendix counts; the external preprint
  does not, on its own).
- **Honest scope** — a bold first foray with candid open problems is a feature here, not a
  weakness.
- **A reason the community should care** — a connection, a reframing, an application sketch.

## Common misreadings to avoid

- Treating ITCS like STOC and optimizing for depth — the PC may find the paper strong but "not
  innovative enough."
- Assuming a rebuttal will let you fix a gap — there is none; the gap sinks the paper.
- Assuming the external full version will be read — the PC judges the submitted PDF.
- Anonymizing references or self-citations — that breaks the *lightweight* rule and can read as
  evasive (see [`itcs-related-work`](../itcs-related-work/SKILL.md)).

## Output format

```text
[ITCS review calibration]
[Novelty] is the new idea legible and checkably new to a briefed PC? yes/no
[Alive] anchoring result present? yes/no
[Proofs] all central claims fully proved IN the submitted PDF? yes/no
[Objections pre-empted] trivial? / new? / why-care? all answered in-text (no rebuttal to rely on)? yes/no
[Anonymity] names/affil/email removed, references NOT anonymized? yes/no
[Risk read] likely reviewer objection + where the paper already answers it (or must)
```
