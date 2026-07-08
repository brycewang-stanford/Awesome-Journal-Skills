---
name: sigmod-workflow
description: Use when planning a SIGMOD project calendar under the PACMMOD round system, covering round selection and hopping, backward planning from abstract and paper cutoffs, the feedback and revision windows, embargo-aware contingencies, and coordinating a systems-building team against quarterly deadlines.
---

# SIGMOD Workflow

SIGMOD project management differs from single-deadline conferences in kind:
with four research rounds a year feeding PACMMOD issues, the strategic
variable is *which* round, and the punishment structure (a 12-month embargo
on rejection, one month to execute a revision) rewards teams that plan the
whole round, not just the deadline. Anchor every date below to the live
important-dates page before acting; the quarterly pattern is durable, the
dates are not.

## The round as a five-act unit

```text
Act 1  Abstract + COIs        (deadline minus ~1 week)
Act 2  Paper deadline         (the 17th of the round month, AoE, for 2027)
Act 3  Feedback phase         (~2 months in; one-week reply window)
Act 4  First verdict          (~3 months in: accept / reject / revision)
Act 5  Revision + final       (+1 month to resubmit, ~+3 weeks to decide)
```

Block engineer time for Acts 3 and 5 when you submit, not when they arrive:
the feedback week may need a fast counter-experiment, and the revision month
is a sprint that assumes the original evaluation was scripted end to end
(see `sigmod-reproducibility`).

## Round selection under the embargo

| Situation | Recommended move |
|---|---|
| Evaluation complete, writing mature | Nearest round |
| Core result solid, one comparison missing | Next round; a missing baseline reads as reject, not revision |
| System working, evaluation thin | Skip two; thin evaluations burn the embargo |
| Racing a known competing group | Weigh nearest round against reject risk; PVLDB's monthly gate may beat waiting |
| Paper rejected last round | Different venue — the track is closed for ~3 rounds |

The asymmetry to internalize: submitting early costs a possible year;
waiting costs three months. Under uncertainty, waiting is usually the
cheaper mistake at this venue.

## Backward plan from a paper cutoff

- T-16 weeks: freeze the system's architecture; feature work after this
  point invalidates measurements.
- T-10: evaluation matrix locked (workloads × baselines × sweeps); harness
  and seeds committed.
- T-6: full experiment pass complete once; draft carries real numbers, not
  placeholders.
- T-4: internal adversarial read by a colleague who builds systems;
  schedule their week now.
- T-2: rerun-from-scratch of every figure; repro ledger shows zero DEBT.
- T-1 week + a few days: abstract, authors, topics, COIs into CMT.
- T-0: PDF up; verify the uploaded file, not the local one.

## Team coordination specifics

- Name one owner for the measurement harness and a different owner for the
  anonymity sweep; both jobs fail under shared custody.
- Keep a submissions ledger across the group: PACMMOD's exclusivity rule
  and the 10-papers-per-author annual cap are portfolio constraints, not
  per-paper ones.
- Archive the exact submitted PDF, the CMT confirmation, and the frozen
  artifact snapshot; the revision letter must quote and diff against them.
- Pre-agree the reject plan (PVLDB? ICDE? rework?) while everyone is calm;
  deciding it the day the verdict lands produces venue-shopping errors.

## Interleaving multiple projects

Quarterly rounds let a group pipeline: project A in Round 1, its revision
landing while project B targets Round 3. The trap is revision collision —
two revisions in the same month exceed most teams' experiment bandwidth.
When two papers are near-ready, split them across non-adjacent rounds
deliberately rather than shipping both into one.

## Small-team and solo variants

The five-act structure assumes bench depth; without it, adjust:

- A solo author cannot staff a feedback week and a revision month on top
  of other obligations — prefer the round *after* the one that looks
  feasible, and treat the slack as the plan, not padding.
- Compress the evaluation matrix before compressing run hygiene; fewer
  workloads with clean provenance beat a wide matrix that cannot be
  regenerated during a revision.
- Recruit the adversarial reader early even when solo — the T-4 external
  read is the step small teams skip and most regret at verdict time.
- Consider whether PVLDB's monthly gate suits a solo pipeline better; a
  missed monthly deadline costs weeks, a failed SIGMOD round costs a year.

## Conference layer

Publication and presentation decouple: your issue ships on the round's
schedule, and the talk happens at the next conference edition (SIGMOD 2027:
June 13–19, 2027, Huntington Beach; SIGMOD 2026 was May 31–June 5,
Bengaluru). Budget registration and travel when the acceptance lands, and
schedule the ARI artifact push (`sigmod-artifact-evaluation`) into the gap
between issue and conference.

## Output format

```text
[Target round] round + year, with selection rationale
[Stage now] pre-abstract / submitted / feedback / verdict / revision
[Backward plan] next three milestones with owners
[Bandwidth check] feedback + revision windows staffed yes/no
[Portfolio constraints] cap headroom, exclusivity conflicts, collisions
[Reject plan] pre-agreed next venue
```
