---
name: cikm-workflow
description: Use when planning a CIKM project calendar across the May abstract/paper gates, June short-track gates, August notification and camera-ready, and the November conference, including the post-submission phase now live in the 2026 cycle, multi-track coordination, and fallback planning toward CIKM 2027 or sibling venues.
---

# CIKM Workflow

CIKM runs a spring-submission, autumn-meeting year. The verified 2026 shape (source
map, 2026-07-08): full-paper abstract May 16 and paper May 23; short, resource, and
demo abstracts May 30 and papers June 6; notification for the listed tracks August 7;
camera-ready August 20; conference November 7-11 in Rome — every cutoff 11:59 PM AoE.
Replace these anchors with the current important-dates page before acting on any of
them; CIKM re-issues its calendar annually under a new host committee.

## Where the 2026 cycle stands now

As of 2026-07-08 all CIKM 2026 submission gates have closed. A team holding a
submission is in the review-wait phase; a team without one is planning CIKM 2027.
That split defines two working modes:

**Mode A — paper under review (July → August 7).** Do the work whose absence hurts in
August: keep the experimental environment runnable rather than dismantled, pre-draft
the camera-ready fixes you already know about, prepare the public artifact that the
anonymized submission could not name, and hold arXiv or publicity moves that conflict
with what was declared on the EasyChair form. If a response mechanism materializes
(unconfirmed for 2026 — 待核实), `cikm-author-response` takes over on short notice.

**Mode B — aiming at the next edition.** The May/November rhythm is a planning prior
only until the 2027 site posts dates. Build backward from a provisional mid-May gate
and treat the abstract deadline as the real freeze: title, abstract, author list —
authorship is frozen there under the ACM policy — and the track choice.

## Backward plan to a May full-paper gate

| Weeks before the paper deadline | Milestone for an IR/mining/KM paper |
|---|---|
| 10 | Track chosen (`cikm-topic-selection`); datasets and baselines secured |
| 7 | Core results in; mechanism ablations scheduled |
| 5 | Draft in ACM two-column format — appendices count inside the budget, so measure now |
| 3 | Internal read by someone from the *other* community lane the paper claims |
| 1.5 | Abstract gate: final title/abstract/authors/track in EasyChair |
| 1 | Anonymity sweep, GenAI Usage Disclosure section written, reviewer nomination assigned |
| 0 | PDF upload; declared arXiv status matches reality |

Two CIKM-specific traps in that table. First, the abstract deadline is one week
before the paper deadline and freezes authorship — late collaborator additions are
formally barred afterward. Second, the appendix-inside-the-limit rule means the
"we'll move it to the appendix" reflex saves nothing; overflow must move to the
cited artifact or be cut.

## Multi-track coordination

Groups often carry a full paper, a resource paper, and a demo toward the same CIKM.
Coordinate them: each needs its own EasyChair track selection and its own
author-reviewer nomination (a missed nomination is a stated desk reject), each needs
its own GenAI disclosure section, and the contributions must not overlap into
self-plagiarism. Stagger internal deadlines — the full paper to the May gate, the
short-form pieces to the June gate — so one team is not writing three papers in one
week.

## Role assignments that prevent CIKM-specific failures

The desk-reject triggers at this venue are administrative, so assign them to named
people rather than to "the team":

| Role | Owns | Failure it prevents |
|---|---|---|
| Form owner | EasyChair track choice, reviewer nomination, arXiv declaration | The two stated desk rejects |
| Budget owner | Page measurement with appendices counted in | Overflow discovered at upload |
| Compliance owner | GenAI Usage Disclosure section, anonymity sweep | ACM AI-policy and blinding violations |
| Artifact owner | Anonymous review artifact → public release path | Dead links at camera-ready |
| Logistics owner | Registration, visa, presentation planning | November scramble |

One person may hold several roles on a small team; no role may be unheld. Log who
holds what in the project tracker the day the track is chosen.

## Cycle-verification ritual

Because CIKM re-platforms annually, open each new cycle with a thirty-minute
verification pass before any planning meeting: locate the new host site from the
series page (the domain will have changed), read the important-dates page and diff
it against last year's rhythm, read the policies page for changed disclosure or
nomination rules, and confirm the submission platform — EasyChair in 2026, but
platform changes between editions are exactly the kind of fact teams assume
wrongly. Write the findings into the project tracker with the access date, source
map style. Every date in this skill is such a dated finding, not a rule.

## Fallback ring

A CIKM rejection lands in early August, in time for WSDM's traditional
late-summer gate (verify), ECIR in autumn, and SIGIR the following January.
Log which lane the reviews faulted; that tells you whether the fix is more evidence
(stay in the family) or a different audience (change family).

## The conference itself is a work object

The November meeting deserves calendar time as more than a talk slot. CIKM's
program concentrates the three communities this pack keeps invoking, plus the
workshop day where next year's boundary topics surface first; treat attendance as
pipeline work — scout which lanes are converging on your problem, note which
tracks absorbed papers like the one you are planning, and talk to the resource
authors whose datasets you will build on. For demo and applied authors the
conference *is* part of the deliverable (booth time, live systems), which the
logistics owner should plan for in the same tracker as the paper work.

## Annual rhythm, compressed

```text
Dec-Feb   route + build (topic selection, datasets, baselines)
Mar-Apr   results + draft in ACM format; internal cross-lane read
mid-May   abstract gate (freeze) → paper gate
June      short/resource/demo gates
Jul-early Aug   review wait = artifact + camera-ready prep (Mode A)
Aug       notification (7th in 2026) → 13-day camera-ready sprint (20th)
Sep-Oct   presentation prep, travel, demo hardening
Nov       conference; post-conference: absorb feedback, plan the next cycle
```

Dates shown are the verified 2026 instances; the shape recurs, the numbers do not.

## Output format

```text
[Mode] under-review wait / camera-ready sprint / next-edition build
[Next hard date] <date + which official page it came from>
[Freeze status] authorship frozen? track locked? artifact runnable?
[This week's three tasks] <ordered>
[Fallback] <next venue if the decision is negative, with its gate>
```
