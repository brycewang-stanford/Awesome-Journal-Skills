---
name: cscw-workflow
description: Use when planning a CSCW submission timeline end to end — the PACMHCI journal model, the retired fixed cycles versus the rolling 2027+ pathway, Revise-and-Resubmit rounds that span months, and back-planning so an acceptance lands before the conference-year presentation cutoff.
---

# CSCW Workflow

CSCW is not a deadline sprint. Since 2017 its papers have been journal articles in
PACMHCI, and since early 2026 the venue has been rolling out a fully journal-style
pipeline: **submit whenever the paper is ready, expect a decision in roughly 3-4
months, revise on the editor's clock, and present at whichever conference your
acceptance lands in front of.** Planning a CSCW project therefore means planning a
*revision campaign*, not a submission night.

## The two regimes (as of 2026-07-08)

| Aspect | Fixed cycles (through the May 2025 cycle) | Rolling (CSCW 2027 and beyond) |
| --- | --- | --- |
| Deadline | Hard cutoff (last: May 14, 2025, 12:00 EDT) | None — submit when ready |
| Platform | PCS | Manuscript Central (mc.manuscriptcentral.com/pacmhci) |
| Who handles the paper | Program committee (ACs) per cycle | Editorial board: EiC/AE by methodological track |
| First decision | Batched (first-round decisions ~6 months in) | Rolling, ~3-4 months from submission |
| Revision windows | Fixed dates (e.g., R&R due January 13, 2026) | Set per paper by the handling editor |
| Conference tie | Cycle mapped to a specific conference year | Accepted papers invited to the *next* CSCW, pending space |

The May 2025 cycle — the last of the old kind — is worth studying as a calibration
anchor even though it will never recur: submissions May 14, 2025 → internal
"Revise for External Review" resubmissions September 16, 2025 → first external
decisions November 2025 (66.2% of papers got Revise and Resubmit; only a third got
any final decision) → revised papers due January 13, 2026 → final decisions late
March 2026 → presentation at CSCW 2026 (Salt Lake City, October 10-14, 2026). That
is a **17-month arc from submission to podium**, and two-thirds of surviving papers
went through the full R&R loop.

## Cycle-hopping, translated for the rolling era

Under fixed cycles, authors managed risk by "hopping": if an R&R could not be turned
around by the resubmission date, the revision rolled into a later cycle and a later
conference. Rolling keeps the underlying skill and removes the calendar: the hop is
now **a negotiation with time, not with a deadline table**. Practical consequences:

- **Submission date is a strategic variable.** Count backward from the conference
  you want to attend: with ~3-4 months to first decision and a realistic multi-week
  revision round (PACMHCI revision periods are measured in weeks-to-months, not
  days), a paper submitted less than ~8-10 months before a conference is betting on
  a clean first decision. The exact cutoff by which a rolling acceptance is assigned
  to CSCW 2027 versus 2028 was 待核实 at check time — confirm it on
  cscw.acm.org/rolling.html before promising a travel year to anyone.
- **Revision capacity is the bottleneck.** An R&R that demands new data collection
  (a second interview wave, another deployment period) costs a season. Budget the
  team's field access *before* submitting, not when the decision arrives.
- **Nothing forces you to submit early — or lets you cram.** The rolling model
  rewards submitting a genuinely finished paper over hitting an arbitrary date with
  a rushed one; there is no deadline-night adrenaline to launder weak sections.

## Campaign plan skeleton

```text
[T0]       Internal full-draft review (simulate first-round: one skeptic per
           method tradition in the paper)
[T0+2wk]   Ethics/consent artifacts final; anonymization sweep #1
[T0+4wk]   Submit via the current platform (verify regime first)
[T0+4mo]   Expected decision window opens — pre-book revision capacity:
           who re-codes, who re-runs analyses, who drafts the response letter
[R&R]      Treat as a project phase with an owner, not a chore
           (see cscw-author-response)
[Accept]   Camera-ready + PACMHCI production (see cscw-camera-ready);
           confirm which conference year the paper presents at
[Confab]   Registration, travel, talk prep for the assigned CSCW
```

## Risks specific to this venue's shape

- **Stale-regime planning.** Advice, blog posts, and lab lore calibrated to PCS
  cycles is now wrong. Verify the live pathway before every new submission.
- **Indefinite-polish drift.** With no deadline, drafts can orbit forever. Set an
  internal submission date and treat it as real.
- **Same-reviewers memory.** R&R rounds return to the same reviewers; a revision
  that quietly ignores a request will be caught by the person who made it.
- **Presentation-slot ambiguity.** "Invited to present at the next conference,
  pending space" is a softer guarantee than a proceedings deadline; keep travel
  plans provisional until the assignment is explicit.

## Status-report format

```text
[Regime] rolling / residual fixed-cycle (verified <date> at cscw.acm.org)
[Stage] drafting / submitted / R&R round n / minor changes / production
[Clock] time since submission or since revision request
[Bottleneck] <the one resource gating the next stage>
[Conference target] CSCW <year> — assignment confirmed? yes / no / 待核实
```

Dates and statistics above are the 2026-07-08 snapshot of a venue mid-transition;
recheck cscw.acm.org and the rolling CFP before treating any of them as current.
