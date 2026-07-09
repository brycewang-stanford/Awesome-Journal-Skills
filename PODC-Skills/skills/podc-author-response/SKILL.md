---
name: podc-author-response
description: Use when writing an ACM PODC rebuttal/author response, if the cycle runs one — covering how to correct a proof misreading, supply a missing lemma or bound within the anonymity envelope, prioritize soundness questions over taste, and behave correctly given that PODC has no revision round to fall back on.
---

# PODC Author Response

Write the response only if the cycle has one — and confirm first. PODC does **not always** run an
author-response/rebuttal phase, and whether the 2026 cycle does is **待核实**; check the call before
planning around one. If there is no rebuttal, all of this energy belongs *before* the deadline in the
submission itself (`podc-experiments`, `podc-reproducibility`). If there is a rebuttal, it is short,
high-stakes, and about the **proof**, not about persuasion.

## First: is there a rebuttal at all?

- Confirm on the current call / HotCRP whether a response phase exists and its length limit.
- If none: there is no second chance this cycle — the decision is on the submission as written. Skip
  to the "no-rebuttal" note below.
- If one exists: it is typically a brief, one-round text response to the reviews, still under
  lightweight double-blind (do not de-anonymize in the response).

## What a PODC rebuttal can and cannot do

A rebuttal moves a borderline **proofs** paper when it:

- **Corrects a factual misreading of the proof** — "Reviewer 2 reads Lemma 3 as assuming synchrony;
  it assumes only eventual delivery, as stated in the model box (§2)." This is the highest-value
  move: a reviewer who misread the argument may become an advocate once corrected.
- **Supplies a missing step a reviewer flagged** — a short proof of a lemma, a clarification of a
  case the reviewer thought was open, or a pointer to where in the full version it already appears.
- **States a bound or assumption precisely** — resolving an apparent gap that was really a notation
  ambiguity.

A rebuttal does **not** move a paper when it:

- **Argues taste or significance** — "we believe this is important" changes no mind; the committee
  weighs significance among themselves.
- **Adds a new result** — you cannot repair a fundamentally incomplete paper in a rebuttal; there is
  no revision round to carry new material into the final version safely.
- **Contests a real proof gap** — if the gap is genuine, no wording fixes it; concede and plan for a
  later venue.

## Prioritize by axis

Answer each reviewer on the axis they actually raised (`podc-review-process`):

```text
[Correctness question]  answer first and concretely: point to the model box, or give the short proof
[Model/assumption doubt] clarify exactly which assumption is used and where it is declared
[Novelty/delta doubt]    cite the precise prior bound and restate your delta in model+cost terms
[Significance opinion]   acknowledge briefly; do not spend the word budget litigating taste
```

Spend the limited length on the **soundness and model questions** that can actually flip a vote, not
on the subjective ones that cannot.

## Stay inside the anonymity envelope

- The response is still **double-blind**: do not reveal author names, affiliations, prior-work
  authorship ("in our earlier paper"), or grant/institution identifiers.
- If you must reference your own prior work to answer a question, keep it third-person, as in the
  submission (`podc-related-work`).
- Do not link to a de-anonymizing arXiv page or repository in the response.

## Tone and structure

- **Open with the single most consequential correction**, not with thanks-boilerplate.
- **Be specific and verifiable:** section/lemma numbers, one-line proofs, exact bounds. A reviewer
  will re-check what you claim.
- **Concede cleanly** where a reviewer is right; a targeted concession plus a fix elsewhere reads as
  competence, not weakness.
- **Stay brief.** Respect the length limit; a focused response on the two pivotal points beats a
  point-by-point wall that buries them.

## If there is no rebuttal (the common case)

- The decision is final on the submitted paper; there is no mechanism to add the missing lemma now.
- Channel the lesson into the resubmission: close the flagged gap, prove the matching lower bound, or
  reroute to DISC / a focused venue / a journal (`podc-topic-selection`).
- Post the corrected full version to arXiv so the community sees the complete, fixed argument.

## Common failures

- **Planning a rebuttal that does not exist this cycle** — confirm first.
- **Arguing significance** instead of answering the correctness question.
- **Promising a fix** as if there were a revision round to deliver it in.
- **De-anonymizing** in the response text or a linked page.
- **Ignoring the reviewer's actual axis** and answering a different objection.

## Output format

```text
[Rebuttal exists?] yes (length limit: <n>) / no — confirmed on the call
[Pivotal points] the 1-2 corrections that can actually flip a vote
[Per-review answers] review point -> axis -> concrete, verifiable response (or clean concession)
[Anonymity] response free of author identity and de-anonymizing links?
[If no rebuttal] resubmission/reroute plan; corrected arXiv full version posted?
```
