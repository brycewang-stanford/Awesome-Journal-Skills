---
name: edbt-workflow
description: Use when planning an EDBT project timeline across the multiple-cycle rolling model — choosing a submission cycle, backward-planning through the author-feedback phase and the in-cycle revise-and-resubmit window, and handling the cycle-to-conference roll — for a database-systems paper published open access on OpenProceedings.
---

# EDBT Workflow

Use this as the project-management skill for an EDBT submission. EDBT's defining rhythm is the
**multiple-cycle rolling model** (three cycles a year since 2022), so the first planning act is not
"hit the deadline" but **"choose the cycle my evidence is ready for."** Replace every date with the
current host-site timetable; the per-cycle author-feedback and revision windows are decided per
edition.

EDBT is a conference whose proceedings are **open access on OpenProceedings.org** (CC-BY-NC-ND, no
APC): it has **no standing editor-in-chief**, the rotating leadership is the per-edition General and
Program Chairs appointed with the EDBT Association, and the host site moves each year (Barcelona
2025, Tampere 2026). Re-check the current host page rather than carrying a name or URL forward.

## The cycle structure (one cycle, end to end)

Each EDBT cycle runs the same five-step arc (EDBT 2022 timeline; reverify dates per edition):

```text
[1] Submission             upload PDF + artifact to Microsoft CMT by the cycle deadline
[2] Author feedback phase  a short window to respond to initial reviews
[3] Notification #1        accept / REVISE / reject
[4] Revised submission     if REVISE: upload the revised paper + change letter
[5] Notification #2        accept / reject on the revision
```

The **revise** branch is a genuine in-cycle revise-and-resubmit re-read by the same reviewers — plan
for it, do not treat it as a formality. Papers accepted in the earlier cycles present at that year's
conference; papers accepted in the **last** cycle roll to the **next** edition.

## Choosing a cycle

| Situation | Cycle choice |
|---|---|
| Evidence complete, artifact built, writing solid | The nearest cycle — do not wait a full third of a year for polish |
| One key experiment still running | The next cycle — a rushed submission burns a revise chance you could earn |
| You want to present at this specific edition | An earlier cycle of that year; the last cycle rolls forward |
| Just rejected from an EDBT track in this format | None for 12 months — the resubmission ban applies (`edbt-submission`) |

## Milestones

- **Venue fit + shape:** confirm EDBT over SIGMOD/VLDB/ICDE/ICDT and pick Regular / Experiments-&-
  Analysis / Vision (`edbt-topic-selection`).
- **Evidence lock:** freeze workloads, datasets, baselines, measurements, and the artifact contents.
- **Cycle choice:** commit to a cycle and back-plan from its deadline.
- **Submission:** upload the PDF and artifact to Microsoft CMT.
- **Author feedback:** answer the initial reviews concisely in the feedback window
  (`edbt-author-response`).
- **Revise (if issued):** execute the revised paper plus a point-by-point change letter within the
  in-cycle window, re-read by the original reviewers.
- **Decision:** archive reviews, responses, and every submitted version.
- **Acceptance:** prepare the OpenProceedings camera-ready, finalize the artifact and its DOI
  archive, register, and present at the edition your cycle feeds.

## Backward plan from a cycle deadline

| Weeks out (heuristic) | Database-systems milestone |
|---|---|
| 10+ | Problem and claims fixed; workloads, datasets, and baselines chosen |
| 8 | System/prototype stable; measurement harness and provenance logging in place |
| 6 | Full evaluation run; results and scope drafted alongside them |
| 4 | Full draft in the host/OpenProceedings template; artifact assembled |
| 3 | Internal mock review by a DB-systems reader; baseline fairness challenged |
| 2 | Scope hardened, related-work delta sharpened, page budget met for the shape |
| 1 | Artifact re-run clean; availability/reproducibility statement final |
| 0 | CMT fields complete; PDF + artifact uploaded before the cycle cutoff |

These offsets are planning heuristics only — anchor every one to the current host-site timetable,
never to a previous cycle's calendar.

## Cycle-hopping: the honest calendar reality

- **A revise you cannot finish in the in-cycle window** is not automatically portable to the next
  cycle — the revision is scored *within* the cycle. Budget the revision window like a hard deadline
  rather than assuming a rollover.
- **Missing a cycle costs roughly a third of a year, not a whole one** — EDBT's biggest scheduling
  advantage over single-deadline venues. But a rejected paper still owes the 12-month
  same-format resubmission ban, so a rushed reject is expensive.
- **The cycle-to-conference roll is real:** a last-cycle acceptance presents at the *following*
  edition. If presenting at a specific city/year matters (travel, graduation, funding), target an
  earlier cycle of that year.

## Failure modes by stage

- **Submitting into an early cycle with evidence still moving** forfeits the revise opportunity you
  could have earned with two more weeks of measurement.
- **Treating the revise as a formality** and under-budgeting the in-cycle window turns a winnable
  revise-and-resubmit into a reject.
- **Skipping the mock review** forfeits the one chance to hear "your baseline is unfair" or "this
  scale is unrealistic" from a friend instead of a reviewer.
- **Assuming the last cycle presents this year** — it rolls to the next edition; plan travel
  accordingly.

## Coordination notes

- Assign one owner for the artifact/reproducibility package and another for the measurement harness;
  shared ownership is how provenance slips.
- Archive the exact submitted PDF and artifact — the revision round and the change letter must quote
  them precisely.

## Output format

```text
[Current stage] idea / evidence / cycle-chosen / submitted / author-feedback / revise / accepted
[Target cycle] cycle N, deadline <date and source>, presents at <edition/year>
[Critical path] <three tasks that determine readiness>
[Revise risk] <can the likely revision be finished inside the in-cycle window?>
[Owner map] <task -> person or role>
```
