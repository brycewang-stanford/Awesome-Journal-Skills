---
name: iccv-workflow
description: Use when project-managing an ICCV campaign across the odd-year cycle, covering the autumn fork between CVPR and ICCV, the early-March registration and single submission deadline, May rebuttal week, late-June decisions, the October conference with international travel and visa lead times, and the ECCV/CVPR fallback ladder if the paper misses.
---

# ICCV Workflow

An ICCV campaign runs on a spring-deadline, autumn-conference rhythm that only
exists in odd years. The 2025 cycle — the most recent completed one, verified
2026-07-08 — ran: paper registration March 3, full submission **and** supplementary
March 7 (11:59pm HST), reviews to authors May 9, rebuttal May 10–16, decisions late
June, conference October 19–23 in Honolulu (workshops the 19th–20th, main program
the 21st–23rd). ICCV 2027 is announced for Hong Kong in early October 2027; its
deadline chain was unpublished at check time, so every date below is a
2025-cycle anchor for shape, not a promise.

## The autumn fork (the decision nobody schedules)

The ICCV cycle actually begins the *previous autumn*, when the team must choose
between the imminent CVPR deadline (November) and holding four more months for
ICCV (March). Make the fork an explicit meeting with a written outcome:

- Hold for ICCV when the missing evidence is real (a benchmark, a user study, a
  second domain) and four months genuinely closes it.
- Take CVPR when the paper is submittable now — holding a finished paper four
  months in a field with weekly arXiv turnover is negative-expected-value.
- Never split the difference by submitting to CVPR "as a free review round";
  overlapping CVF reviewer pools remember, and dual-submission windows can trap a
  paper that gets held over.

## Cycle plan with owners (2025-shaped)

| Window | Milestone | Failure this window causes |
|---|---|---|
| Sep–Oct (year before) | Autumn fork decided; claims frozen in one paragraph | Zombie project drifting between deadlines |
| Nov–Dec | Experiment matrix runs; draft skeleton with figure slots | March becomes an experiments deadline, not a writing one |
| Jan | Full internal draft; outside reader pass | No time to act on feedback |
| Feb | Baseline-freshness audit; anonymity sweep; supplement built **in parallel** | Same-day supplement rule catches the team |
| ~Mar 3 | Registration: title, abstract, full author list, complete OpenReview profiles | Registration lapse = no submission |
| ~Mar 7 | Paper + supplement, one upload event (2025: 11:59pm **HST**) | Anything unfinished is unfinished forever |
| Mar–May | Coauthors serve reviewer assignments — every author reviews at ICCV | Late reviews can desk-reject *your* paper |
| ~May 9–16 | Reviews land; seven-day rebuttal | Week lost to shock instead of triage |
| Late Jun | Decision | No plan B drafted |
| Summer | Camera-ready (exact 2025 deadline 待核实); artifact release runway | Promises to reviewers quietly expire |
| Oct | Conference week abroad | Visa/travel booked too late |

Note the timezone trap: 2025's deadline was Hawaii Standard Time — generous for
Europe and Asia, but teams that reflexively assume AoE have missed CVF deadlines
in both directions. Read the clock on the current Dates page, not from habit.

## Two ICCV-specific project risks

**The unified deadline.** Since 2025, ICCV takes paper and supplementary material
on the same day (an announced process change — it also shortened the decision
timeline). Plan the supplement as a parallel workstream from February, with its
own owner. Teams migrating from CVPR habits still budget a "supplement week" that
no longer exists.

**Reviewer duty with teeth.** Every author is expected to review unless exempt
(those new to or outside the vision community were exempted in 2025), each author
may register at most 25 submissions, and the 2025 chairs enforced quality: 25
reviewers were judged highly irresponsible and 29 of their authored papers were
desk-rejected, 12 of which would otherwise have been accepted. Treat coauthor
review assignments as deliverables on the project plan with a senior reviewer
proofreading first-timers' drafts.

## International logistics are part of the plan

ICCV rotates internationally by design — Honolulu in 2025, Hong Kong announced for
2027. For many team members that means visas, and visa appointment queues in some
countries exceed the June-decision-to-October-conference gap. Do not wait for the
decision:

```text
travel-readiness ledger (start at submission, not at acceptance)
  per author:  passport expiry ≥ 6 months past conference?  visa type needed?
               appointment backlog in their country (weeks)?
  per paper:   who presents if the first author cannot travel?
               funding source confirmed for at least one presenter?
  deadline:    visa paperwork drafted by decision day, filed within a week of it
```

## The fallback ladder (the biennial part)

Missing ICCV costs two years *of ICCV*, but not two years of publishing. Draft the
ladder before decisions arrive:

1. **Reviews were fixable** → ECCV (the following even-year spring) or the next
   CVPR (November): repair every factual objection first; pools overlap.
2. **Reviews said "sound but not exciting"** → in 2025, the new Findings workshop
   accepted technically sound rejected/withdrawn ICCV papers (a post-decision
   outlet — check whether it recurs); or WACV for application-leaning work.
3. **Reviews revealed a missing foundation** → journal track (TPAMI/IJCV) after
   real revision, or back to the bench.
4. **Idea overtaken during review** → salvage the reusable component; do not
   resubmit a superseded comparison table anywhere.

## Multi-paper labs, odd-year edition

In odd years a vision lab may push papers at CVPR (Nov), ICCV (Mar), *and* ICCV
workshops (summer CFPs) with the same people. Lab-level coordination: one shared
duty roster (a single delinquent reviewer-coauthor endangers every ICCV paper the
lab submitted), one shared compute reservation for rebuttal week in May, and one
person owning OpenReview profile hygiene across all submissions — the 2025 cycle
required complete profiles at registration.

## Reverify before trusting any date here

- The entire 2027 chain: registration/paper deadlines, timezone, rebuttal window,
  decision date, camera-ready — all 待核实 until iccv.thecvf.com posts them.
- Whether the single paper+supplement deadline persists.
- Whether Findings runs again in 2027.
- Registration and presentation obligations for accepted papers (not verified
  even for 2025 — 待核实).

## Output format

```text
[Cycle position] autumn-fork / building / deadline-month / in-review / rebuttal / decided / pre-conference
[Next 3 milestones] <date — item — owner>
[Duty roster] coauthor reviewer assignments tracked: yes/no
[Supplement workstream] parallel owner assigned: yes/no
[Travel readiness] visas/funding per presenter: green/amber/red
[Fallback ladder] <ranked next venues with their real deadlines>
```
