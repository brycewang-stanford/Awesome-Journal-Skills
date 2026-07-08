---
name: icra-workflow
description: Use when planning an ICRA submission calendar end to end — the September paper deadline, the two video-attachment windows, winter review silence, late-January notification, March camera-ready, and the May/June conference — or when interleaving a fallback RA-L or IROS plan around the single annual ICRA shot.
---

# ICRA Workflow

ICRA runs on one unforgiving annual clock: papers due mid-September, decisions at
the end of January, camera-ready in early March, conference late May or early June.
There is no abstract-registration step, no rebuttal window to buy time, and the
video attachment has its own separate deadlines that surprise first-time authors.
This skill turns that clock into a working plan with named owners and fallbacks.

## The verified 2026-cycle clock (anchor, not prophecy)

| Milestone | ICRA 2026 (Vienna) actual | Owner in your plan |
|---|---|---|
| Submission site opens (PaperPlaza) | July 15, 2025 | corresponding author |
| Video window 1 | Aug 5 – Sep 9, 2025 | experiments lead |
| Paper deadline | Sep 15, 2025, 23:59 Pacific | everyone |
| Video window 2 (post-deadline) | Sep 17 – 22, 2025 | experiments lead |
| Review period (no author contact) | Oct 2025 – Jan 2026 | — |
| Accept/reject notification | Jan 31, 2026 | corresponding author |
| Camera-ready deadline | Mar 6, 2026 | writing lead |
| Conference | Jun 1 – 5, 2026 | presenting author |

ICRA 2027 is announced for **May 24-28, 2027, COEX, Seoul**; its paper deadline was
not yet posted at check time (2026-07-08) — plan against mid-September 2026 as the
working hypothesis and verify at `2027.ieee-icra.org` before circulating dates.

## Backward planning from the September deadline

Robotics papers die on hardware time, not writing time. Count backward:

- **T minus 16 weeks (late May):** freeze the task definition and success metric.
  Changing the task after this point invalidates collected trials.
- **T minus 12 weeks:** platform bring-up complete; baselines running on the real
  system, not just in simulation. Order spare parts now — a burned motor driver in
  August is a cycle-killer.
- **T minus 8 weeks:** main-method trials underway with the logging harness from
  `icra-reproducibility` already in place; begin capturing raw video during every
  session so the attachment is assembled from real footage, not re-staged runs.
- **T minus 4 weeks:** full experimental table exists in draft form; writing
  becomes the critical path. Cut experiments, not analysis quality.
- **T minus 1 week:** paper into the `icra-submission` audit; video edited to the
  180-second cap; PaperPlaza metadata entered; PDF compliance checked.
- **Deadline week:** upload at least 24 hours early. PaperPlaza slows measurably
  in the final hours of Pacific-time deadline day.

## The winter silence and how to spend it

Between September and late January the pipeline is closed to authors — no status
pings, no updated PDFs, no supplementary additions. Productive uses:

1. Extend experiments toward the camera-ready and toward the journal version.
2. Prepare the RA-L conversion of the same line of work (a *different* paper —
   never the identical manuscript, which would be dual submission).
3. Draft the workshop or late-breaking submission for the same conference; those
   calls typically open in winter with their own deadlines.
4. Budget conference logistics early: Vienna 2026 drew 8,000+ attendees and Seoul
   2027 anticipates around 10,000, so housing and visas (Schengen, then Korea)
   need lead time measured in months, not weeks.

## Fallback lattice

```text
Sep ICRA deadline missed or reject in Jan?
 ├─ RA-L: rolling submission, ~3-month first decision,
 │        accepted letters transferable to a later RAS conference stage
 ├─ IROS: deadline typically ~March 1 for an autumn conference
 ├─ CoRL: learning-centric work, deadline typically ~June
 └─ ICRA workshops / late-breaking: same trip, lighter review,
          non-archival or lightly archival — check the current call
Rule: pick the fallback BEFORE notification day, so a reject
      converts to a resubmission in days, not months.
```

## Interleaving the RA-L track without fouling either

Teams running both roads (see `icra-topic-selection`) need sequencing rules:

- A given manuscript occupies exactly one pipeline at a time; the *project* may
  feed both only as genuinely different papers (different claims, different
  evidence) — when in doubt, assume the overlap is too high.
- The efficient braid: system paper → direct ICRA in September; the follow-up
  with the extended evaluation → RA-L in the spring, aiming its 270-day
  presentation-transfer window at the *next* ICRA or IROS.
- Put the RA-L first-decision estimate (~3 months from submission) on the same
  calendar as the ICRA milestones so revision labor never collides with
  camera-ready labor in the same fortnight.

## Failure modes this calendar prevents

- **The video afterthought.** Teams discover the attachment windows after the
  paper deadline and miss window 2; the paper then competes without the single
  most persuasive artifact a robotics reviewer sees.
- **Hardware heroics in September.** Last-fortnight soldering produces the thin
  trial counts that `icra-experiments` flags as a leading rejection cause.
- **Notification-day scramble.** No pre-chosen fallback means the January reject
  ages for a month while the team debates; the March IROS deadline then arrives
  with no revision done.
- **Camera-ready compression panic.** The 2026 final limit was 8 pages *including*
  references, while submissions ran 6+2; merging reviewer-requested additions into
  a tighter effective budget takes the two weeks the calendar reserves for it.

## Date-verification ritual

Every date in this file is a 2026-cycle anchor. Before propagating any of them
into a team plan:

1. Open the current year-site (`<year>.ieee-icra.org`) contribute/CFP pages.
2. Confirm the deadline's **time zone** — 2026 used Pacific, not AoE.
3. Confirm both video windows; they move independently of the paper deadline.
4. Record what you verified and when in the project log, so the next teammate
   does not re-trust a stale screenshot.

## Team checkpoint template

```text
[Cycle] ICRA <year> — deadline <verified date> (verify at <year>.ieee-icra.org)
[Today minus deadline] <n> weeks
[Hardware status] platform up? spares? trial count vs plan
[Evidence status] baselines real/sim, main table % complete
[Video status] raw footage hours banked, edit owner, window dates
[Writing status] section owners, page budget vs 6+2
[Fallback] <RA-L / IROS / CoRL> pre-selected: yes/no
[Next checkpoint] <date, ≤2 weeks out>
```
