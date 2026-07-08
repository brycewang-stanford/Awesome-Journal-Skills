---
name: naacl-author-response
description: Use when writing the ARR author response for a paper headed to NAACL — deciding which reviewer objections to spend the window on, drafting replies that give the action editor a citable meta-review sentence, and protecting the score record that NAACL's committee will later read at commitment.
---

# NAACL Author Response

The response you write inside an ARR cycle is read twice: once by the
reviewers and action editor who finish the meta-review, and once more —
frozen — by NAACL's senior area chairs when you commit the package. That
second audience changes the calculus. A reply that merely wins an argument
helps less than a reply that leaves a clean, quotable record showing the
objection was answered.

## Budgeting the window

ARR response windows are short and reviewers rarely return for a second
round. Rank objections by what they cost you downstream:

| Objection class | Downstream cost if unanswered | Response priority |
|---|---|---|
| Soundness attack (flawed eval, wrong baseline, leakage suspicion) | Sinks both ARR scores and any NAACL commitment | Answer first, with evidence coordinates |
| Coverage attack ("claims exceed the languages/domains tested") | Recurring killer for Americas-flavored papers | Concede scope or cite the table that grants it |
| Novelty doubt | Damaging but survivable if excitement holds | Answer with a two-sentence delta statement |
| Presentation complaints | Cheap to fix, cheap to promise | Batch into one short commitment list |
| Requests for infeasible new experiments | Low — ARR forbids judging you on promises alone | Scope honestly; run only what fits the window |

## Reply mechanics that fit ARR

- Anchor every factual claim to a coordinate the reviewer can check in the
  version they read: section, table, appendix, line of the checklist.
- New numbers are admissible only if they can be produced inside the window
  and stated in the response text itself; anything else is a camera-ready
  promise, labeled as such.
- Keep anonymity intact — no lab names, no repository owners, no "as we
  showed at last year's workshop in Oaxaca."
- Write the concession sentences yourself. An AC who finds "the authors agree
  the claim should be scoped to the five languages tested" in your words will
  reuse it; one who has to infer it may write something harsher.

## Skeleton for a soundness reply

```text
R2 raises leakage: the eval set may overlap pretraining data.
1. What we already did: §4.2 reports n-gram-overlap screening
   against the released corpus list (Table 5, appendix C).
2. What we ran this window: exact-match dedup on the 2 newest
   models; contaminated items = 0.8%, results shift < 0.3 F1.
3. What we will state at camera-ready: the screening protocol
   moves from appendix to §4, with the dedup numbers added.
```

Three moves — existing evidence, in-window evidence, camera-ready promise —
each labeled, none blurred into the others.

## Tone repairs that change outcomes

The frozen record amplifies tone: a defensive sentence reads worse at
commitment than it did in the heat of the window.

| Instinctive draft | What the record shows | Repaired version |
|---|---|---|
| "The reviewer clearly did not read Section 4." | Author hostility, unresolved thread | "Section 4.2 addresses this directly; we suspect the two-column layout buried it, and will promote the key sentence." |
| "This is standard practice in the field." | Appeal to authority, no evidence | "Three recent papers on this task use the same protocol [refs in §2]; we follow them for comparability." |
| "We will add these experiments to the final version." | An unverifiable promise doing a result's job | "We ran the two feasible configurations this week: X and Y (numbers below); the full grid is future work." |
| "We respectfully disagree." (paragraph follows) | Disagreement without a decision path | "The disagreement reduces to one empirical question: Q. Table 3 answers it as follows." |

## The commitment-record test

Before sending, reread each reply pretending you are a NAACL SAC months
later, skimming to decide Main versus Findings versus reject. Ask:

- Does the thread end with the objection visibly resolved, narrowed, or
  honestly conceded — or does it just stop?
- Did you correct a reviewer misreading politely and *in one place*, so the
  meta-review inherits the correction?
- If scores stay low, does your final note give the commitment-stage reader
  a reason the paper is stronger than its numbers?

A response that fails this test may still sway one reviewer; it will do
nothing for the audience that actually admits papers to NAACL.

## Playing for the tier, not just the acceptance

Because NAACL sorts committed papers into Main and Findings, the response
has two distinct win conditions, and knowing which one you are playing for
changes the drafting:

- If the reviews question **soundness**, you are playing to stay eligible
  at all — spend everything on the correctness record, and treat
  presentation complaints as an afterthought.
- If the reviews concede soundness but doubt **excitement or breadth**,
  you are playing for Main over Findings — the highest-value sentences are
  the ones that reframe significance concretely: who uses this result,
  what it unblocks, which prior conclusion it revises.
- A response cannot manufacture excitement that the paper lacks, but it
  can prevent an excitement objection from mutating into a soundness one
  ("limited scope" drifting toward "claims exceed evidence") by fixing the
  claim's wording on the spot.

State the tier goal in the team's triage notes before anyone drafts; mixed
responses that half-defend correctness and half-oversell impact do neither
job well.

## Timing inside the cycle

1. Day 0-1: triage all reviews; classify by the table above; assign owners.
2. Day 1-3: run only the experiments that fit the window and change a score.
3. Day 3-4: draft, cross-check coordinates against the submitted PDF.
4. Final day: trim each reply toward its single decisive point; submit well
   before the AoE cutoff — OpenReview outages at deadlines are routine.

## Output format

```text
[Objection map] <reviewer -> class -> priority>
[In-window evidence] <what was actually run, with results>
[Concessions] <exact sentences offered>
[Camera-ready promises] <bounded list>
[Commitment-record check] pass / weak / fail per thread
```
