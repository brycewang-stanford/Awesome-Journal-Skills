---
name: fast-workflow
description: Use when planning a USENIX FAST project timeline from venue fit through choosing a Spring or Fall deadline, double-blind submission, the author-response period, shepherding or a one-shot revision, artifact evaluation, and the open-access camera-ready, with backward-planning offsets tuned to storage evaluation and honest handling of the two-deadline cycle.
---

# FAST Workflow

Use this as the project-management skill for a FAST submission. Replace every date with the current
official timetable and work backwards from the deadline you choose. FAST — the USENIX Conference on
File and Storage Technologies — runs **two deadlines a year**, has an **author-response** period,
and can issue a **one-shot revision** that spans into the next deadline, so plan for a longer arc
than a plain accept/reject conference.

FAST is a USENIX conference: it has **no standing editor-in-chief** and **no article-processing
charge**. Rotating leadership is the per-edition Program Co-Chairs and the program committee, and
the cost model is registration plus USENIX membership — proceedings are open access. Chairs and the
Artifact Evaluation Committee rotate yearly; re-check the current committee page rather than carrying
a name forward (FAST '27 rosters: **待核实** beyond what the CFP names).

## Choose the deadline, then plan backward

FAST '27 offers **Spring** (submit 17 Mar 2026, notify 4 Jun 2026, final files 28 Jul 2026) and
**Fall** (submit 15 Sep 2026, notify 8 Dec 2026, final files 26 Jan 2027). Pick by *evidence
readiness* — storage measurements at steady state on real, aged devices take real calendar time —
not by whichever is nearest. As of 2026-07-09 the Spring round is notified and the live target is
the **Fall deadline, 15 Sep 2026**.

## Milestones

- **Venue fit:** confirm FAST over OSDI/ATC/EuroSys and that the core lesson is storage
  (`fast-topic-selection`).
- **Evidence lock:** freeze the testbed (devices, firmware, kernel), the workloads/traces, the
  device-state protocol (aging, fill, TRIM), the baselines, and the metrics.
- **Registration:** register real title, abstract, authors, topics, and conflicts on the *correct*
  Spring/Fall HotCRP instance.
- **Submission:** upload the anonymized, double-blind PDF and the availability statement.
- **Author response:** during the response window, answer reviewer questions with existing evidence
  or a concrete, feasible plan.
- **Decision:** Accept / Accept-with-shepherding / **One-shot Revision** / Reject.
- **Shepherding or one-shot revision (if issued):** make the required changes; a one-shot revision
  may demand *new experiments* and is resubmitted at the next deadline.
- **Acceptance:** prepare the open-access camera-ready, pursue USENIX artifact badges on the AEC's
  own timeline, register, and present.

## Backward plan from the submission deadline

| Weeks out (heuristic) | Storage-evaluation milestone |
|---|---|
| 12+ | Testbed fixed: device models/firmware, kernel, mkfs options; workloads/traces chosen |
| 10 | Device-state protocol locked (aging/preconditioning, fill level, TRIM); baselines built and tuned |
| 8 | Measurement runs complete at steady state; device counters (SMART/logs) captured; provenance logged |
| 6 | Analysis done; tail-latency distributions, write-amplification, endurance projections computed |
| 4 | Full draft in the USENIX template; artifact + trace-replay scripts assembled and anonymized |
| 3 | Internal mock review by a storage reader |
| 2 | Caveats hardened, related-work delta sharpened, page limit met |
| 1 | Double-blind sweep on PDF and artifact; availability statement final |
| 0 | Register the abstract on the correct HotCRP, then upload |

These offsets are planning heuristics only — anchor every one to the current Important Dates block,
never to a previous cycle's calendar. Note that storage runs (aging a drive, replaying a long trace,
an endurance test) can dominate the schedule; size them explicitly.

## The two-deadline reality and one-shot revision

- **Missing one deadline is not a lost year.** The other FAST deadline is months away — but so is a
  sibling (OSDI/ATC/EuroSys) date; factor that into routing rather than idling.
- **A one-shot revision is a second full deadline, not a formality.** Its instructions can require
  specific new experiments, the revised paper is re-read, and it can be rejected. Budget the
  revision window like a fresh submission, and note the paper stays *under review at FAST* during it,
  so it cannot go elsewhere in parallel.

## Failure modes by stage

- **Testbed still moving at week 6** forces last-minute measurements nobody audited — the classic
  storage-soundness reject in the making.
- **Reporting fresh-out-of-box instead of steady-state** numbers invites the "did you precondition?"
  objection that can sink an SSD paper.
- **Leaving the anonymized artifact and trace hosting to the final week** is how a device dump,
  hostname, or personal trace URL leaks identity under double-blind.
- **Treating a one-shot revision as an accept** and under-budgeting its experiments turns a winnable
  revision into a reject.

## Coordination notes

- Assign one owner for the testbed/provenance log and another for the double-blind sweep; shared
  ownership is how both slip.
- Archive the exact submitted PDF, artifact, and (later) the response/revision documents — the
  revision round must quote reviews precisely and stay anonymous.

## Output format

```text
[Current stage] idea / evidence / writing / registration / submitted / response / shepherd-or-revision / accepted
[Target deadline] Spring / Fall <date and source, or unknown>
[Critical path] <three tasks that determine readiness — often measurement-time-bound>
[Risk register] <page limit / anonymity / device state / provenance / tail latency / artifact>
[Owner map] <task -> person or role>
```
