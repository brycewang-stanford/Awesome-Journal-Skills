---
name: vldb-workflow
description: Use when planning a VLDB project on the PVLDB rolling calendar, covering month-picking strategy, the volume-to-conference mapping and acceptance cutoff, budgeting a possible three-month revision, coordinating author caps across a group, and backward planning from the 25th-abstract / 1st-paper rhythm.
---

# VLDB Workflow

Use this as the project-management layer. PVLDB's defining freedom — a
deadline every month — is also its trap: with no scarcity forcing quality, the
calendar discipline must come from you.

## Know your volume geometry first

On 2026-07-08 the live volume is **Vol 20**: deadlines April 1, 2026 through
March 1, 2027, feeding VLDB 2027 (Athens, Aug 23-27, 2027). Vol 19 fed
VLDB 2026 (Boston, Aug 31 - Sep 4, 2026) with a June 15, 2026 acceptance
cutoff; acceptances after a cutoff roll to the next conference. Re-derive this
geometry from the live guidelines whenever you plan — it resets every volume.

## Month-picking, done as arithmetic

The right month is computed backward from what you want, not chosen by mood:

| Goal | Computation |
|---|---|
| Present at the volume's conference | Cutoff month − 1.5 months (review) − 3 months (possible revision) − 1.5 months (re-review) ⇒ submit roughly **6 months before the cutoff** to keep the revision path open |
| Accept-or-nothing, no revision slack | Cutoff − 1.5 months, accepting that a revise verdict rolls you past it |
| No conference-year preference | The month your weakest experiment is actually fixed |
| Thesis or job-market date | Decision date needed + 1 month safety, then backward as above |

The month itself carries no difficulty signal — the review board is standing
and the bar is flat. What varies is *your* readiness.

## One cycle, backward from the 1st

```text
Day -21        go/no-go: evaluation complete? loss map measured?
Day -14        internal builder-review (a colleague reads as Reviewer 2)
Day -10        fixes from mock review; freeze the claim set
Day -6 (25th)  abstract registered in CMT — title and authors final
Day -5..-2     full-text polish, artifact tag, fairness ledger check
Day -1         PDF built on the volume template; local time of 5PM PT confirmed
Day 0 (1st)    submit hours early; Pacific afternoon, not local midnight
```

If the go/no-go fails, slide one month. That sentence is the whole advantage
of this venue — use it instead of negotiating with your own evidence.

## Revision bandwidth is a scheduling object

A revise verdict opens a three-month window that will collide with whatever
else the group planned. Before submitting, name the two people who would own
a revision and check their next quarter. A revision no one has time to
execute converts positive signal into a rejection.

## Group-level calendar management

- Track every member's live submissions against the two-per-month and
  twelve-per-year caps in one shared sheet.
- Stagger related papers across months so a shared infrastructure fix does
  not block two deadlines at once.
- Log every cycle's dates the moment reviews arrive: decision on the ~15th,
  revision due date, expected issue. Rolling venues punish loose bookkeeping
  with silent misses.

## Conference logistics tail

Publication precedes presentation by months. After acceptance: registration,
visa lead time for the conference country (Greece for Vol 20's VLDB 2027),
and speaker assignment — obligations and pricing are cycle-specific (待核实
on the conference site).

## Output format

```text
[Volume geometry] <live volume, cutoff, conference>
[Target month + rationale] <computed, not vibes>
[Go/no-go state] <evaluation, loss map, artifact, writing>
[Revision bandwidth] <owners named, quarter checked>
[Cap ledger] <per-author counts>
[Slip plan] <what triggers moving one month>
```
