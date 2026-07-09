---
name: eacl-workflow
description: Use when planning an EACL project timeline through ACL Rolling Review, covering the single viable ARR cycle with no fallback, backward planning from the one deadline, the rebuttal window, the commitment decision to EACL, notification, and camera-ready through ACL Anthology publication, plus re-routing since the next chance is another conference.
---

# EACL Workflow

Use this as the project-management skill for an EACL submission. EACL is a conference routed
through ACL Rolling Review: it has no standing editor-in-chief and no article-processing charge.
The rotating leadership is the per-edition General Chair and Program Chairs (EACL 2027: General
Chair Isabelle Augenstein; Program Chairs Malvina Nissim, Roi Reichart, Sara Tonelli — verified
2026-07-09). The cost model is registration; the Anthology is open access with no author fee.
Replace every date below with the current official timetable.

## The single-cycle calendar (EACL 2027 anchor)

Because EACL 2027 sits early in the year, the organizers named **one viable ARR cycle** — there
is **no fallback**. That reshapes planning around a single hard gate:

| Milestone | EACL 2027 anchor date | Owner |
|---|---|---|
| ARR submission (only cycle) | August 3, 2026 | ARR |
| Rebuttal window | in-cycle (待核实 exact dates) | Authors |
| Meta-review | in-cycle | Action editor |
| Commitment to EACL | October 11, 2026 | Authors |
| Notification | November 12, 2026 | EACL |
| Camera-ready | November 26, 2026 | Authors |
| Conference | March 9-14, 2027, Athens | EACL |

All ARR/commitment deadlines run anywhere-on-Earth; confirm exact times on the live pages.

## Backward-planning offsets

```text
Work backwards from the single ARR deadline (D):
  D-8 weeks: freeze scope; lock experiments (eacl-experiments)
  D-6 weeks: first full draft; run the worked-example arc (eacl-writing-style)
  D-4 weeks: related-work freshness sweep (eacl-related-work)
  D-3 weeks: reproducibility + artifact packaging (eacl-reproducibility, eacl-artifact-evaluation)
  D-2 weeks: Limitations + supplementary placement (eacl-supplementary)
  D-1 week:  checklist, anonymization, page count (eacl-submission)
  D-3 days:  smoke-check archive; submit early
```

## Plan the fallback that is not a next cycle

- The usual *ACL "resubmit next cycle" safety net **does not exist** for a single-cycle EACL
  edition. Before the deadline, decide the **re-route plan**: if the paper misses or is rejected,
  which sibling venue (ACL, EMNLP, NAACL, AACL) is next, and the ARR reviews travel with it.
- This makes the submit-thin-or-wait decision from `eacl-submission` a real fork — resolve it
  early, not on deadline night.

## At each gate

- **Submission:** run `eacl-submission`; there is no second attempt this edition.
- **Rebuttal:** run `eacl-author-response`; fix what fits the window because you cannot defer.
- **Commitment:** run `eacl-review-process`; weigh main vs Findings vs re-route.
- **Camera-ready:** run `eacl-camera-ready`; author list is frozen from commitment.

## Cadence caution

- EACL does not run every year and its calendar slot moves; do **not** carry the 2027 timing to
  another edition. Confirm the edition exists and reopen its CFP before planning.

## Output format

```text
[Timeline] <backward-planned dates from the single ARR deadline>
[Single-cycle risk] <readiness for the one gate>
[Rebuttal plan] <what can be fixed in-window>
[Commitment decision] <main / Findings / re-route>
[Re-route fallback] <named sibling venue + ARR-review carry-forward>
[Camera-ready + logistics] <deadlines, registration, presentation>
```
