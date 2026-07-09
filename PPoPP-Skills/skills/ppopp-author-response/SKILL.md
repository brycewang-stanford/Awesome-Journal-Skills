---
name: ppopp-author-response
description: Use when writing a PPoPP author-response rebuttal, covering the short fixed word-capped window, answering the recurring "does it scale?" and "what about baseline X?" questions with pre-run numbers, correcting factual misreadings of a concurrency argument, staying double-blind, and prioritizing the points that can actually move a decision.
---

# PPoPP Author Response

Write the rebuttal for the fixed **author-response window** (PPoPP 2026: 27–29 October 2025). This
is a **short, word-capped, single written turn** — as verified there is no guaranteed
revise-and-resubmit round to fall back on. Reviewers read it, discuss, and decide. Spend the budget
on the points that can change a verdict, answered with data, not adjectives.

## What the window is and is not

- It is a **2–3 day** window with a **word cap**; you cannot run a month of new experiments.
- It is **not** a debate forum or a place to relitigate taste. It is where you correct factual
  misreadings and supply the specific number a reviewer said was missing.
- It stays **double-blind**: reveal no identity, name no cluster/grant, add no author-revealing
  link.

## Triage the reviews first

```text
[Blocking + fixable]   a missing baseline you pre-ran; a scaling point you already have;
                       a misread correctness argument   -> answer these first, with data
[Blocking + not fixable in words]  a study-design gap needing new machine time
                       -> concede honestly, scope the claim down, or note it as future work
[Non-blocking]         wording, a citation, a minor clarification   -> one line each, or skip
```

Answer the reviewer who is closest to championing you and whose objection is concrete; a reviewer
who only questioned novelty rarely decides a systems paper.

## The two questions you must be ready for

PPoPP rebuttals live or die on two recurring asks. Prepare for both **before** reviews arrive
(see `ppopp-experiments`), because the window is too short to generate the runs from scratch:

1. **"Does it still scale at higher core counts / on another topology or GPU?"** — Have the larger
   core sweep or the second-machine run already measured. In the rebuttal, give the number:
   "At 128 cores throughput is <X>; the curve stays linear to 96 and flattens at 112 due to memory
   bandwidth, as we now quantify." A concrete point beats "we expect it to scale."
2. **"How does it compare to baseline X / the state of the art [k]?"** — Have the comparison ready.
   "Against [k] on the same 2-socket node, our structure is <Y>× at 64 threads and matches at 4."

Promising to run an experiment "in the final version" does not move a PPoPP reviewer; a measured
number does.

## Answering a misread correctness argument

If a reviewer misreads your linearizability or progress argument, correct it **precisely**: point
to the linearization point, the specific interleaving they worried about, and why your
synchronization (under the named memory model) handles it. Do not restate the whole proof — cite
the section and give the one clarifying sentence that dissolves the objection.

## Writing mechanics

- **Lead with the answer, then the evidence.** "Yes — measured: <number>." Reviewers skim under
  load.
- **Quote the reviewer's ask** in a few words so the mapping is unambiguous, then answer it.
- **Number your responses** to reviewer/point so the discussion can follow them.
- **Fit the cap.** Cut acknowledgements and restatement; every sentence should either supply a fact
  or correct one.
- **Concede what you cannot fix** and say what you will do — a candid, scoped concession reads
  better than an evasive claim, and reviewers reward honesty in the discussion.

## What not to do

- Do not argue that a request is unreasonable; either answer it or scope the claim.
- Do not introduce a new claim the reviewers could not check — it invites suspicion, not credit.
- Do not leak identity: no lab name, no named machine, no personal repo link, even mid-argument.
- Do not spend words on non-blocking nits while a blocking scaling question goes unanswered.

## Output format

```text
[Window] author-response dates, word cap
[Triage] blocking-fixable / blocking-not-fixable / non-blocking — points sorted
[Scaling answer] higher-core / second-machine number ready and stated? yes/no
[Baseline answer] comparison to the named competitor ready and stated? yes/no
[Correctness fix] misread interleaving corrected precisely? yes/no
[Anonymity] no identity/machine/grant/repo leak? yes/no
[Cuts] what to drop to fit the cap
```
