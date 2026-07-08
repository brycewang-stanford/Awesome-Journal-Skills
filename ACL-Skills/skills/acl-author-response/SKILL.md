---
name: acl-author-response
description: Use when drafting an ACL author response inside an ACL Rolling Review cycle on OpenReview, covering the response window before meta-review, reviewer discussion dynamics, score-change strategy, flagging review issues to the area chair, anonymity rules, and deciding between responding now versus revising for a later ARR cycle.
---

# ACL Author Response

Use this when ARR reviews land. The response is written inside the review cycle,
*before* the meta-review is finalized — its primary reader is the area chair who
will summarize your paper for whatever conference you later commit to. Reopen
aclrollingreview.org/reviewing for the current cycle's exact window and rules.

## What the response can actually move

- ARR assigns at least three reviewers; after the author response there is a
  reviewer-discussion phase in which reviewers are expected to update reviews.
  A response that gives a reviewer a concrete reason to revise is worth more
  than one that argues.
- The meta-review travels with the paper to commitment. Senior area chairs at
  the venue read the meta-review first, so your real goal is to shape what the
  AC writes, not to win a debate transcript.
- Scores are not the only currency: a meta-review that says "the main weakness
  was resolved in discussion" can rescue a committed paper that scores alone
  would sink.

## Triage order

1. Factual errors in reviews (wrong dataset, misread table, missed section).
2. Misunderstandings a two-sentence clarification can dissolve.
3. Requests satisfiable from submitted material — appendix tables, checklist
   answers, the supplement archive.
4. Requests needing new experiments: promise only what is genuinely small, or
   explicitly defer to a revision cycle (ARR is built for resubmission).
5. Taste disagreements: answer once, briefly, without heat.

## NLP-reviewer objection patterns

| Objection | Underlying worry | Response that works at ACL |
|---|---|---|
| "Only evaluated on English" | Overclaimed generality | Scope the claim explicitly; cite the multilingual appendix run if one exists |
| "Gains may be contamination" | Test data in pretraining | Point to the decontamination check or concede and describe the planned audit |
| "No error analysis" | Numbers without understanding | Quote the analysis section or summarize 2-3 systematic error classes from logged outputs |
| "Human eval lacks agreement stats" | Unreliable judgments | Report the IAA already computed; never invent a number in the response box |
| "Missing recent baseline X" | Stale comparison set | Distinguish X technically, or accept it as revision work with a stated plan |

## Rules of the response box

- Stay anonymous: no names, lab hints, grant numbers, or identifying links.
- Never claim results that are not in the submitted PDF, supplement, or
  checklist; ARR reviewers can and do check.
- Keep each reviewer reply skimmable — lead with the single sentence you want
  quoted in the meta-review.
- If a review is deficient (template text, wrong paper, LLM-generated, hostile),
  use the current cycle's review-issue flag to the AC rather than fighting it in
  the reply thread.

## Respond now or resubmit later

- Respond in-cycle when the objections are misreadings or scoping problems —
  these are exactly what discussion can fix before the meta-review.
- Prefer withdrawing the commitment plan and revising for a later cycle when
  reviews identify real missing experiments; a resubmission must carry a
  point-by-point revision note anyway, so bank the work.
- Remember the asymmetry: reviews and meta-review persist and follow a
  resubmission. An abrasive response is permanent record.

## Skeleton reply

```text
We thank Reviewer X. Main point first: [one-sentence resolution].

1. [Factual correction] The model is trained only on the training split
   (Section 3.2, line refs); Table 2 reports held-out results.
2. [Clarification] The claim is scoped to the five languages tested
   (Section 5); we will tighten the abstract wording.
3. [Evidence pointer] Seeds, prompts, and compute are in Appendix C and
   checklist items C1-C3.
4. [Deferred work] A comparison to X requires retraining; we commit to it
   in a revision and note why it should not change the ranking.
```

## Tone calibration for the ARR record

- Write for three audiences at once: the reviewer being answered, the AC
  composing the meta-review, and the venue chairs who will skim the thread
  months later at commitment.
- Concede fast and specifically; a clean concession plus a scoped fix reads
  as competence, while minimizing a real weakness reads as evasion.
- Quantify wherever a reviewer hedged: replace "we believe the effect is
  robust" with the interval, the seed count, or the appendix table number.
- Do not thank effusively or argue emotionally; both waste the reader's
  attention budget in a thread they are legally required to skim.
- If two reviewers contradict each other, say so neutrally and let the AC
  arbitrate — pointing out the contradiction is legitimate and effective.

## A workable 5-day response window

1. **Day 1**: read all reviews twice; extract every distinct objection into
   a sheet with owner and evidence anchor; no drafting yet.
2. **Day 2**: run any genuinely small verification (a re-scoring, a missing
   statistic already computable from logged outputs).
3. **Day 3**: draft all replies; lead each with its one-sentence resolution.
4. **Day 4**: internal cold read by a co-author who did not draft; cut 30%.
5. **Day 5**: post early, not at the buzzer — reviewers who will engage in
   discussion tend to do it once, soon after your reply appears.

## If the real answer is "withdraw and revise"

- Skipping the response entirely is a signal too — reviewers note silence
  in discussion, and the package records it. A short, gracious reply that
  acknowledges the substantive points costs little and keeps the record
  clean for the resubmission's mandatory revision note.
- Harvest the reviews immediately into the revision plan while the team
  still has context; the next cycle's point-by-point response is easiest
  to write as a running document, not a deadline reconstruction.

## Output format

```text
[Response stance] clarify-in-cycle / concede-and-revise / mixed
[Meta-review target] <sentence you want the AC to write>
[Per-reviewer plan] <R1/R2/R3: main point + evidence anchor>
[Review-issue flags] <deficient-review reports to AC, if any>
[Deferred to resubmission] <experiments promised for a later cycle>
```
