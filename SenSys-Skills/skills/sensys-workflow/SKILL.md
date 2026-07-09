---
name: sensys-workflow
description: Use when planning a SenSys campaign against the two-deadline calendar — deciding which deadline to target and which edition it feeds, backward-scheduling so energy campaigns and long-term deployments finish before freeze, budgeting time for the resubmission-with-revision path, and sequencing fit, building, writing, and submission.
---

# SenSys Workflow

A SenSys campaign is governed by two facts the calendar imposes: SenSys runs **two submission
deadlines per cycle**, and its evidence is **physical**, so the schedule is dominated by
wall-clock time you cannot compress — a 47-day deployment takes 47 days. This skill turns the
cycle into a backward schedule that leaves room for the measurements and, if needed, the
resubmission.

## Anchor the calendar first

Before scheduling anything, pin down against the live CFP and HotCRP `/deadlines` page:

- **Which deadline** you are targeting (first or second) and **which edition it feeds**. As of
  2026-07-09 the open gate is **SenSys 2027** (New York, May 10-13, 2027), with a **first-round
  deadline of June 6, AoE**; the second-round deadline is **待核实**.
- The **AoE** cutoff, converted per coauthor.
- Whether an **abstract-registration** step precedes the paper upload this edition.

Treat the numbers here as a 2026-27 snapshot; the live page controls.

## Backward schedule from the deadline

Deployment and energy campaigns, not writing, are the long pole. Schedule from T-0 (paper cutoff)
backward:

| Phase | Window | What must be true by the end |
|---|---|---|
| Fit + framing | T-16 wk | `sensys-topic-selection` cleared; the system's claim is decided |
| Build + instrument | T-14 to T-8 wk | Hardware built, energy instrument set up, testbed reserved |
| Deployment / energy campaign | T-10 to T-4 wk | Long-term runs finished; traces captured (cannot compress) |
| Analysis + writing | T-6 to T-2 wk | Figures from real traces; body drafted against the worked example |
| Reproducibility freeze | T-3 wk | Provenance captured while the testbed is still live |
| Submission audit | T-1 wk to T-0 | `sensys-submission` end to end on the exact upload candidate |

The overlap is deliberate: writing starts while later deployment runs finish, because you cannot
begin the 6-week deployment at T-4.

## Budget for the two-deadline reality

The two-deadline model changes planning in a way a single-deadline venue does not:

```text
If targeting the FIRST deadline:
  - A reject can resubmit at the SECOND deadline — but only WITH a substantive revision.
  - Reserve testbed time AFTER the first notification for the new measurements a revision needs.

If targeting the SECOND deadline as a resubmission of a first-deadline reject:
  - The revision + Response to Reviewers is REQUIRED, not optional (sensys-author-response).
  - Back-schedule the new deployment/energy runs against the second cutoff BEFORE you commit.
```

A blocking reviewer objection that needs a fresh energy-harvesting deployment cannot be answered
in two weeks — decide *at notification* whether the resubmission is feasible on the calendar, not
after you have already missed the window to start the runs (`sensys-review-process`).

## Sequence the whole cycle

```text
1. Fit          → sensys-topic-selection (is it SenSys after the merger?)
2. Build        → hardware + instrumentation; reserve the testbed
3. Measure      → sensys-experiments + sensys-reproducibility (traces captured live)
4. Write        → sensys-writing-style + sensys-supplementary + sensys-related-work
5. Submit       → sensys-submission (audit the exact PDF; HotCRP fields verbatim)
6. Notification → sensys-review-process (classify), then:
     accept     → sensys-artifact-evaluation + sensys-camera-ready
     resubmit   → sensys-author-response, back-scheduled to the next deadline
```

## Standing risks to track

- **Testbed contention** — shared hardware is the schedule's single point of failure; reserve early.
- **Deployment failures** — a node dying mid-run is normal; build slack for a re-run.
- **Provenance loss** — capture energy method and ground truth *before* teardown, not after.
- **Edition drift** — re-confirm which edition your deadline feeds each cycle; it can shift.

## Output format

```text
[Target]   which deadline + which edition it feeds + AoE cutoff in local time
[Longpole] the deployment/energy campaign duration and its start-by date
[Schedule] backward plan T-0 → T-16wk with the freeze and audit points
[Resub]    if a reject, is a next-deadline resubmission feasible on the calendar? Y/N
[Open]     the scheduling risk most likely to break the plan
```
