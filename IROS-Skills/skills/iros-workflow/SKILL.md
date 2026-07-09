---
name: iros-workflow
description: Use when planning an IROS project timeline from venue fit through the spring paper deadline, the separate video deadline, the summer review silence, the June notification, the July camera-ready, IEEE Xplore publication, registration, and presentation, with backward-planning offsets for a real-robot paper on the fall IEEE/RSJ calendar.
---

# IROS Workflow

Use this as the project-management skill for an IROS submission. Replace every date with the current
official timetable and work backward from PaperPlaza cutoffs.

IROS is a conference, not a journal: it has no standing editor-in-chief and no article-processing charge.
It is **co-sponsored by IEEE RAS and the Robotics Society of Japan (RSJ)** — hence "IEEE/RSJ" — and the
organizing committee rotates yearly between regions, so re-check the current CFP and committee page
rather than carrying names or rules forward. The cost model is registration plus any per-page charge,
and proceedings go to IEEE Xplore.

## The fall-venue rhythm (2026 shape)

IROS is the **fall** IEEE-RAS mega-venue, the seasonal counterpart to ICRA's spring cycle. The 2026
edition ran a spring submission into an autumn conference:

- Paper deadline in **early spring** (2026: March 2).
- Video attachment a few days later (2026: March 5) — a distinct cutoff, not tied to the paper.
- A long **summer review silence**, then notification in **mid-June** (2026: June 16).
- **Camera-ready in July** (2026: July 10), then the conference in **late September/October** (2026:
  Sept 27 - Oct 1, Pittsburgh).

Knowing you are on the fall calendar changes routing: a project that misses IROS's spring deadline has
CoRL and the next ICRA as nearer alternatives than waiting a full IROS year.

## Milestones

- Venue fit: confirm the contribution is an integrated intelligent system with credible robot evidence.
- Evidence lock: freeze the platform, task distribution, trial protocol, baselines, and the video plan.
- Paper deadline: upload the anonymous PDF (references counted in the page budget) and PaperPlaza fields.
- Video deadline: upload the ≤ 60 s / ≤ 10 MB attachment by its own cutoff.
- Review silence: nothing to do but keep the robot and logs intact for camera-ready.
- Notification: triage reviews; there is traditionally no rebuttal, so plan camera-ready edits instead.
- Camera-ready: de-anonymize, integrate meta-review asks, file the IEEE copyright form, register.
- Presentation: at least one author presents in person; prepare the talk and any live/updated video.

## Backward plan from the paper deadline

| Weeks out (heuristic) | Real-robot systems milestone |
|---|---|
| 10+ | Platform frozen; task distribution and success criterion defined |
| 8 | Baselines implemented on the same hardware for a fair comparison |
| 6 | Main trials run, resets logged, failures categorized |
| 4 | Sim-to-real study complete; the gap is a number, not a hope |
| 3 | Full draft in IEEE two-column format; references budgeted as content |
| 2 | Video footage banked from real sessions; rough 60 s cut assembled |
| 1 | Anonymity sweep across PDF, figures, and video; PaperPlaza PINs collected |
| 0 | Paper uploaded; video by its separate cutoff |

These offsets are planning heuristics only — anchor each to the current official timetable, never to a
previous cycle's calendar.

## Failure modes by stage

- Filming on deadline week produces worse footage and worse anonymity than banking clips all along.
- Treating references as free space overruns the budget, because IROS counts them in.
- Assuming a rebuttal exists wastes the notification window; IROS traditionally ships reviews with the
  decision, so the only lever is camera-ready.
- Letting the robot get reconfigured before camera-ready makes a requested extra trial impossible.

## Coordination notes

- Assign one named owner for the video and one for the anonymity sweep; shared ownership is how both
  slip.
- Archive the exact submitted PDF and video, since the camera-ready must trace to the reviewed version.

## Output format

```text
[Current stage] idea / experiments / writing / submission / video / review / notified / camera-ready
[Next official deadline] <date and source, or unknown>
[Critical path] <three tasks that determine readiness>
[Risk register] <page-budget/anonymity/robot-evidence/video/transfer>
[Owner map] <task -> person or role>
```
