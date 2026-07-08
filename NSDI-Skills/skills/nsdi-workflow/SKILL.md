---
name: nsdi-workflow
description: Use when planning an NSDI campaign across the spring and fall deadlines — sequencing abstract and paper gates, notification waits, one-shot revision windows, artifact evaluation, and the May symposium — so a networked-systems project always knows which of the two yearly gates it is really building toward.
---

# NSDI Workflow

NSDI is a calendar problem disguised as a conference. One edition, two submission
gates, two decision cohorts, and a revision mechanism that spans deadlines — a team
that plans "for NSDI" without naming the gate usually discovers it planned for
neither. Dates below are the NSDI '27 cycle as rendered on 2026-07-08; treat them as
this cycle's snapshot and re-pull the HotCRP `/deadlines` pages before acting.

## The '27 clock

| Gate | Date (11:59 pm US EDT) | Cohort |
|---|---|---|
| Spring abstracts | April 16, 2026 | spring |
| Spring full papers | April 23, 2026 | spring |
| Spring notification | July 23, 2026 | spring |
| Fall abstracts | September 10, 2026 | fall |
| Fall full papers | September 17, 2026 | fall |
| Fall notification | December 8, 2026 | fall |
| Symposium | May 11-13, 2027, Providence, RI | both |

Where "today" (2026-07-08) sits: spring authors are two weeks from notification; a
fresh submission has nine weeks to the fall abstract gate. Camera-ready dates and the
'27 artifact schedule were not yet rendered — 待核实, watch the conference page.

## One project, four legal paths through the cycle

```text
Path A  fall '26 submit -> accept (Dec 8) -> final paper + AE -> present May '27
Path B  fall '26 submit -> one-shot revision -> resubmit spring '27 (next edition)
Path C  fall '26 submit -> reject -> BARRED from spring '27; rework for fall '27
Path D  spring '26 one-shot revision (notif Jul 23) -> revise -> fall '26 resubmit
```

Path C is the one teams forget: a plain rejection carries a one-deadline ban, so the
cheapest-looking option — "just submit and see" — silently spends two deadlines, not
one. Build the decision into the plan: submit only when the evidence would survive
review, otherwise hold for the next gate and use the time on the testbed.

## Working backward from a gate

A fall-2026 target, walked backward:

- **T-9 to T-6 weeks:** freeze the design; the evaluation plan (workloads, baselines,
  scale points) written down and reviewed as if it were the paper
  (`nsdi-experiments`). Trace collection and testbed reservations start now — cluster
  time is the resource that cannot be compressed in deadline week.
- **T-6 to T-3:** experiments run continuously with provenance capture
  (`nsdi-reproducibility`); the paper skeleton fills section by section
  (`nsdi-writing-style`); related-work sweep across both NSDI cohort lists of the
  current edition (`nsdi-related-work`).
- **T-2:** full internal read against the 12-page budget; appendix triage
  (`nsdi-supplementary`).
- **T-1 week (Sept 10):** abstract, authors, track, and conflicts registered on the
  fall HotCRP site. The abstract gate is a hard prerequisite, not a formality.
- **T-0 (Sept 17):** final PDF through the submission audit (`nsdi-submission`),
  uploaded and marked complete with hours to spare.

## The waits, and what to do inside them

NSDI's review silences are long (spring: April to late July; fall: September to early
December). Productive uses that pay off regardless of outcome:

- Harden the artifact toward badge evaluation — the accept-case deliverable
  (`nsdi-artifact-evaluation`), and the Community Award requires public code/data by
  the final-papers deadline.
- Keep the testbed alive and re-runnable; a one-shot revision letter often demands new
  experiments on a 3-4 month fuse, and a decommissioned cluster turns a feasible
  revision into a forfeit.
- Draft the extension or the next paper; do **not** submit the same work elsewhere —
  concurrent submission violates USENIX policy.

## Revision-window management (path B/D)

A one-shot revision arrives with a reviewer-authored list of required issues and a
deadline implied by the next submission gate. Run it as a mini-project:

1. Within a week: map every required issue to an owner and a cost (new experiment,
   new analysis, rewrite).
2. Reserve infrastructure immediately for any issue needing measurements.
3. Maintain the change-highlighted PDF and the change-summary memo *as you go* — both
   are mandatory auxiliary material at resubmission (`nsdi-author-response`).
4. Freeze two weeks before the gate; a revision that misses its window or dodges an
   issue is rejected with no further revision option.

## Choosing between the gates when both are open

Early in a cycle, spring-vs-fall is a real decision, not a default:

- **Spring favors** projects whose evaluation is already running: an accept yields
  ten months of artifact and presentation runway, and even a one-shot revision
  recycles into the same edition's fall gate (path D) — the gentlest failure mode
  NSDI offers.
- **Fall favors** projects still building: five more months of testbed time, at the
  cost of a compressed post-accept pipeline and a revision that lands in the *next*
  edition.
- **Never split one paper across both** by submitting a weak spring version as a
  placeholder — the rejection ban (path C) converts that hedge into exclusion from
  the very fall gate the team was counting on.

## Standing risks with named owners

- **Gate confusion** — someone plans for "the NSDI deadline" without saying which.
  Owner: project lead; fix: every milestone names spring/fall + year.
- **Time-zone drift** — '27 uses US EDT where '26 used PDT; a reused conversion table
  is an hour-scale landmine. Owner: submitter of record.
- **Cap collisions** — eight submissions per author per edition across both deadlines;
  large groups reconcile author lists before each abstract gate. Owner: most-senior
  common author.
- **Infrastructure decay during waits.** Owner: artifact lead.

## Output format

```text
[Target gate] spring / fall + year (papers due <date>)
[Today's position] weeks to next gate; cohort status of any pending submission
[Backward plan] milestone -> week -> owner
[Ban check] any cohort-ban or revision window constraining this plan?
[Wait-time tasks] artifact / testbed / next-paper assignments
[Top schedule risk] <one item + mitigation>
```
