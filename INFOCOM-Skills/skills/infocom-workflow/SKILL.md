---
name: infocom-workflow
description: Use when planning an IEEE INFOCOM project timeline from venue fit through the two-step EDAS abstract-then-paper registration, the early-reject checkpoint, the December notification, the IEEE Xplore camera-ready with PDF eXpress and eCF, and presentation, with backward-planning offsets for a networking paper and honest handling of the single-summer deadline.
---

# INFOCOM Workflow

Use this as the project-management skill for an INFOCOM submission. Replace every date with the
current official timetable and work backwards from the **abstract/metadata deadline** (in late
July), which precedes the full-paper deadline by about a week. INFOCOM runs a **single annual
summer deadline**, so a missed cycle costs roughly a year — plan the calendar as tightly as the
paper.

INFOCOM is an IEEE ComSoc conference with **no standing editor-in-chief** and **no
article-processing charge**. Rotating leadership is the per-edition General Co-Chairs and TPC
Co-Chairs, appointed under ComSoc; the cost model is **conference registration**, and at least one
author must register for the paper to enter IEEE Xplore. Chairs rotate yearly; re-check the
organizing-committee page rather than carrying a name forward.

## Milestones

- **Venue fit:** confirm INFOCOM over SIGCOMM/NSDI/MobiCom and confirm the paper is ready this
  cycle (`infocom-topic-selection`).
- **Evidence lock:** freeze the system model, theorems/proofs, simulator setup, baselines, and the
  evaluation results.
- **Abstract/metadata registration:** enter real title, abstract (≤200 words), co-authors, and
  topic tags into EDAS by the abstract deadline (INFOCOM 2026: 24 Jul 2025; 2027: 24 Jul 2026).
- **Full-paper submission:** upload the anonymized IEEEtran PDF (INFOCOM 2026: 31 Jul 2025; 2027:
  31 Jul 2026), within the 10-page / ≤9-page-of-text budget.
- **Early-reject checkpoint (if the cycle runs one):** INFOCOM 2027 posts early-reject on 9 Oct
  2026 — a mid-cycle signal, not a final verdict.
- **Notification:** final decision (INFOCOM 2026: 8 Dec 2025; 2027: 8 Dec 2026).
- **Camera-ready:** eCF copyright, PDF eXpress validation, IEEE Xplore-compliant PDF (INFOCOM 2026:
  9 Jan 2026), plus author registration.
- **Presentation:** at least one author registers and presents at the conference.

## Backward plan from the full-paper deadline

| Weeks out (heuristic) | Networking-paper milestone |
|---|---|
| 12+ | Problem formulated; system model and assumptions fixed; baselines chosen |
| 10 | Theorems proved / protocol designed; simulator or testbed built |
| 8 | Experiments/simulations complete; seeds and configs logged |
| 6 | Analysis done; plots and tables built; proofs written up |
| 4 | Full draft in IEEEtran; measured against the 9-page text boundary (refs excluded) |
| 3 | Internal mock review by a reader from the other side (theory ↔ systems) |
| 2 | Baselines hardened, related-work delta sharpened, page budget met |
| 1 | Double-blind sweep on the PDF and metadata; abstract entered in EDAS |
| 0 | Full paper on EDAS within the budget; five-paper cap re-checked |

These offsets are planning heuristics only — anchor every one to the current Call for Papers, never
to a previous cycle's calendar.

## The single-summer calendar reality

INFOCOM runs one annual research deadline in **late July**, with notification in **December** and
the conference the following **May**. As of 2026-07-09, INFOCOM 2026 (Tokyo) is decided, so the
live next target is **INFOCOM 2027** (Honolulu; abstract 24 Jul 2026, paper 31 Jul 2026). Two
planning consequences:

- **A near-miss on the July deadline costs a full year** at INFOCOM; a sibling flagship
  (SIGCOMM/NSDI/MobiCom) or a journal (ToN/JSAC) may have a nearer date — factor that into routing
  rather than idling.
- **There is no rebuttal to plan for** (traditionally): budget the pre-submission mock review as
  the one and only chance to hear "your baseline is unfair" from a friend instead of a reviewer.

## Failure modes by stage

- **Evidence still moving at week 4** forces last-minute simulation nobody has audited — the classic
  soundness reject.
- **Discovering the paper is a page over at week 1** with appendices counted inside the nine pages —
  a not-reviewed outcome that editing weeks earlier would have prevented.
- **Skipping the cross-side mock review** forfeits the chance to catch an unstated assumption
  (theory reader) or an unrealistic topology (systems reader).
- **Forgetting the five-paper cap** on a group's submission sprint, so a sixth paper is dropped.

## Coordination notes

- Assign one owner for the EDAS metadata/topic tags (they drive automated assignment) and another
  for the double-blind sweep; shared ownership is how both slip.
- Archive the exact submitted PDF and the simulator/testbed configuration — the camera-ready must
  match, and any released artifact must reproduce it.

## Output format

```text
[Current stage] idea / evidence / writing / abstract-registered / submitted / early-reject / accepted
[Next official deadline] <date and source, or unknown>
[Critical path] <three tasks that determine readiness>
[Risk register] <page budget / double-blind / evidence / baselines / author cap / registration>
[Owner map] <task -> person or role>
```
