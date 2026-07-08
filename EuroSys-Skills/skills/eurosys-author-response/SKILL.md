---
name: eurosys-author-response
description: Use when writing a EuroSys rebuttal or managing a one-shot revision — reading reviews against the three possible outcomes (accept, revise, reject), answering systems reviewers' measurement and design objections, and turning a revision offer's condition list into a resubmission plan for the next EuroSys deadline.
---

# EuroSys Author Response

Use this once EuroSys reviews arrive, or when a revision decision lands. The
decisive EuroSys fact: every submission ends as **accept, reject, or a one-shot
revision offer** (EuroSys 2026/2027 CFPs, rendered 2026-07-08). A response is not
just damage control — it is the input that decides which of the three bins the PC
discussion puts you in. Rebuttal mechanics (window length, word caps, whether a
response phase exists at all in the current round) are set per cycle in HotCRP —
待核实 against the round's own instructions before drafting.

## Read the reviews as a bin-sorting problem

| Review pattern | Likely bin | Response goal |
|---|---|---|
| Positive scores, factual misreadings | Accept-adjacent | Correct the record crisply; give the champion ammunition |
| "Promising but evaluation incomplete" | Revision candidate | Show the missing experiment is bounded and specific |
| Disputed novelty or contribution | Contested | Name the delta against the exact cited system |
| Fundamental design objection | Reject-adjacent | Concede scope honestly; salvage what is defensible |

The revision-candidate row matters most at this venue: reviewers who believe the
fix is *enumerable* can argue for a revision offer instead of a reject, and the
condition list they write becomes your contract.

## Drafting rules for systems reviewers

- Lead with the one correction that changes a score, not with thanks.
- Quote the paper by section and figure number; EuroSys reviewers re-open the PDF.
- Answer measurement objections with the measurement's own terms: workload,
  hardware, baseline version, repetition count — not adjectives.
- Never promise results you have not already produced; a EuroSys revision offer
  will convert vague promises into explicit conditions you must then meet.
- Stay anonymous. The double-blind contract holds through the response phase.

## Response skeleton

```text
R2's central concern: the comparison against <baseline> uses its default config.
- Fact: §5.2 tunes <baseline> per the authors' published guidance (Fig. 7 caption).
- New clarification: at the tuned setting, the gap is 1.8x, not the 3x headline;
  the 3x case is the untuned default, which §5.2 labels as such.
- Text change if accepted/revised: promote the tuned number to the abstract.
Minor points: [R1-a] typo confirmed. [R3-b] the trace is public; link withheld
under double-blind, provenance stated in §4.1.
```

## If the outcome is a one-shot revision

The offer arrives with a list of necessary conditions — extra analysis,
experiments, or comparisons that substantiate the claims. Treat it like a
shepherded contract with a hard deadline: the **next** EuroSys submission round.

1. Convert each condition into a task with an owner and a machine reservation.
2. Decide within a week whether every condition is physically satisfiable before
   that round's paper gate; declining early beats failing late.
3. Write the revision note as condition → change → location-in-paper, one row per
   condition, so the returning reviewers can verify without rereading everything.
4. Do not smuggle in a new contribution; the revision is judged on the list, and
   scope creep reads as instability.

A revision accepted at the following round is presented at the edition it lands
in — plan travel and camera-ready effort accordingly (see `eurosys-workflow`).

## Word-budget allocation

Whatever cap the round sets, spend it in this ratio:

| Share | Spend it on |
|---|---|
| ~50% | The single score-moving objection, answered with evidence |
| ~25% | Factual corrections that change how reviews read each other |
| ~15% | The most likely revision conditions, pre-scoped and bounded |
| ~10% | Minor points, batched one line each with review IDs |

Resist symmetric per-reviewer allocation: the PC discussion is one
conversation, not four, and the meta-question it settles is "does the author
team understand what is actually wrong?"

## Timeline discipline

- Draft the bin-sort within 24 hours of reviews landing; the first reading
  under emotion misclassifies severity in both directions.
- Circulate the score-moving answer to all authors before polishing minor
  points — co-author disagreement about the central concession is the thing
  you cannot fix on deadline morning.
- If the round runs reviewer-author discussion rather than a one-shot
  rebuttal (待核实 per round), answer early; late replies reach reviewers
  who have already argued their position in the PC thread.
- Keep a copy of exactly what was submitted; a later revision offer will be
  interpreted against the rebuttal's promises.

## What sinks responses here

- Arguing taste ("we believe the design is elegant") instead of evidence.
- Burying the score-moving answer under ten minor-point replies.
- Disputing a reviewer's competence — the PC discussion is a room of their peers.
- Treating a revision offer as a soft accept; unmet conditions produce a reject
  and the same-season resubmission ban that follows it.

## Output format

```text
[Bin estimate] accept-adjacent / revision candidate / contested / reject-adjacent
[Score-moving issue] <the one objection worth most of the word budget>
[Fact corrections] <misreading -> section/figure evidence>
[Revision-condition plan] <condition -> task -> feasible by next round? yes/no>
[Anonymity check] passed / issues
```
