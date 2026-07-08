---
name: focs-workflow
description: Use when planning a FOCS (IEEE Symposium on Foundations of Computer Science) cycle end to end — working backward from the April 1 deadline, managing the live post-submission summer of the 2026 cycle, coordinating with the STOC beat, preparing the November conference, and scheduling a FOCS 2027 attempt.
---

# FOCS Workflow

The FOCS year is anchored in spring: the 2026 cycle closed submissions on
Wednesday, April 1, 2026, 5:00 PM EDT (21:00 UTC) on `focs26.hotcrp.com`, for a
conference in New York on November 8–11, 2026 (67th edition, checked
2026-07-08). As of that check date the cycle is in its post-submission phase:
papers are with the program committee, notification and camera-ready dates were
not yet published (待核实), and the workshop-proposal window is open. This
skill manages both the live phases and the planning of the next attempt.

## The 2026 cycle, seen from mid-July

| Phase | Status at 2026-07-08 | Author actions |
|---|---|---|
| Submission (Apr 1, 5 PM EDT) | Closed | None — do not contact reviewers |
| PC evaluation (spring–summer) | In progress | Keep the arXiv/ECCC version stable; log any bug fixes separately |
| Notification | Date 待核实 (historically midsummer) | Pre-draft both outcomes: camera-ready plan and resubmission memo |
| Workshop proposals | Open until **July 31, 2026 AoE** (to the workshop chairs; decisions August 14) | Consider proposing a Sunday Nov 8 workshop independent of paper outcome |
| Camera-ready | Date 待核实 (acceptance packet controls) | Reserve a two-week block after notification |
| Conference (Nov 8–11, New York) | Fixed | Budget travel early; November NYC hotel prices climb fast |

Two live rules for the waiting months: first, if you discover a genuine error
in a submitted proof, the honest channel is a note to the program chair, not a
silent arXiv update that de-synchronizes the record; second, do not submit the
same result elsewhere — SIGACT's simultaneous-submission policy governs this
IEEE venue and stays in force until decisions arrive.

## Backward plan for a FOCS 2027 attempt

FOCS 2027 had no published CFP, venue, or deadline at the check date (待核实).
The historical rhythm — CFP in late winter, deadline at the start of April,
conference in late autumn — is a pattern to plan by, not a fact to rely on.
A realistic backward schedule against a presumed early-April deadline:

```text
T-20 weeks (mid-Nov) : freeze the theorem list; run the significance test
                       (focs-topic-selection); pick FOCS vs. the STOC beat
T-14 weeks (early Jan): complete proofs of all main theorems; begin the
                       full-version write-up — at FOCS you submit the whole
                       paper, so writing cannot trail proving
T-8 weeks  (early Feb): STOC notifications land around now — merge any
                       resubmission into this plan within one week
T-5 weeks  (late Feb) : draft the first ten pages as a standalone document;
                       external read by a non-subarea theoretician
T-2 weeks  (mid-Mar)  : double-blind sweep, format floor check, external-
                       citation audit (focs-submission, focs-related-work)
T-3 days              : upload to HotCRP; verify the PDF has no copy/print
                       restrictions; re-upload cost is zero before the clock
```

## Coordinating the two-flagship year

From the FOCS seat, STOC is the community's other deadline, five months out of
phase. Practical coordination rules:

- Maintain one canonical LaTeX source per project with venue-agnostic theorem
  statements, so a FOCS rejection can be re-aimed at STOC without statement
  drift (see `focs-reproducibility`).
- Never hold a finished strong result half a year just to hit FOCS; theory
  moves by arXiv, and a posted preprint starts collecting concurrent-work
  complications immediately (see `focs-related-work`).
- Track the sibling clocks explicitly: STOC 2026 was due November 4, 2025 and
  met June 22–26, 2026; a FOCS 2026 rejection therefore has a natural next
  stop at the following STOC deadline (exact 2027 date 待核实).

## Owner matrix for a multi-author paper

| Deliverable | Single named owner | Deadline discipline |
|---|---|---|
| Proof completeness audit | Most senior theoretician | T-14 weeks |
| First-ten-pages narrative | Lead author | T-5 weeks |
| Anonymity + format sweep | Any co-author *not* writing prose that week | T-2 weeks |
| HotCRP metadata, conflicts, topics | Corresponding author | T-3 days |
| arXiv/ECCC full version | Lead author | At or shortly after submission |

The most common workflow failure at this venue is not missing the deadline —
it is arriving at T-2 weeks with proofs done and the ten-page front unwritten,
because the team treated FOCS like a journal where the whole manuscript is
read. Guard the T-5-week milestone above all others.

## The workshop lane, run in parallel

The FOCS week has a second entrance that authors chronically forget: the
Sunday workshop program. For 2026, proposals of two pages for 2.5-hour or
5-hour in-person workshops were due to the workshop chairs (Dakshita Khurana
and Sam Hopkins) by July 31, 2026 AoE, with decisions on August 14. A
workshop proposal is decided independently of your paper, gives your subarea
a stage in New York even if the paper loses, and is one of the few FOCS
levers still live during the review wait. If your group has three or more
people working the same emerging direction, the proposal costs an afternoon
and is usually worth it.

## Rhythm failure modes, named

- **The April surprise.** Teams calibrated to AoE deadlines discover on the
  day that 5 PM EDT is nine hours earlier than 23:59 AoE. Convert the clock
  once, in writing, at T-2 weeks.
- **The silent summer.** No news between April and notification is the
  system working; interpreting silence as rejection and posting the paper to
  another proceedings venue violates the simultaneous-submission bar while
  the paper is still under review.
- **The stale preprint.** Referees will read your arXiv version. If it is
  three revisions behind the submission, they will referee the wrong proofs.
  Synchronize at submission time, then freeze.
- **The double booking.** The same result groomed for both FOCS and a
  specialist deadline "to see which hits" is a policy violation at this
  venue, not a strategy — sequence attempts instead (`focs-topic-selection`
  for the ordering logic).
