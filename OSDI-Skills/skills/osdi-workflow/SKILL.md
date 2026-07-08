---
name: osdi-workflow
description: Use when planning or managing a full OSDI cycle — the December title-registration and submission deadlines on HotCRP, the silent no-rebuttal review window, March notification, the May artifact deadline, June shepherded final papers, and the July conference — including rejection retargeting to SOSP or NSDI.
---

# OSDI Workflow

Project-manage the OSDI year. All dates below are the verified OSDI '26 pipeline
(read 2026-07-08) and are one cycle's snapshot; the '27 CFP was not yet posted at check
time (待核实), so anchor the next cycle only after `usenix.org/conference/osdi27`
publishes its dates.

## The 2026 pipeline, with what each date actually demanded

| Date (2026 cycle) | Gate | What must be true by then |
|---|---|---|
| Dec 4, 2025, 2:59 pm PST | Title/abstract registration (both tracks) | Title, abstract, authors, track choice on HotCRP |
| Dec 11, 2025, 2:59 pm PST | Full submission | Final anonymized 12-page PDF uploaded |
| Mar 26, 2026 | Notification | Decision: accept / conditional accept / reject |
| May 8, 2026, 8:59 pm PDT | Artifact submission | Archive + AE README ready (accepted papers) |
| Jun 9, 2026 | Final papers | Shepherd-approved 14-page PDF in the system |
| Jul 13–15, 2026 | Conference (Seattle) | Presenter registered and prepared |

Three structural notes that surprise newcomers:

- **The deadlines are Pacific clock time, not AoE.** 2:59 pm PST is late-night only in
  Europe; in East Asia it is early morning the next day. Compute your local cutoff
  explicitly and pin it in the team calendar.
- **Registration is a real deadline a week before the paper.** Miss December 4 and
  December 11 is irrelevant.
- **Nothing happens between December and March that you can influence.** OSDI '26 had
  no author-response period, so the review window is silent by design.

## Backward plan from December

Work backward from submission, owning each risk by name:

```text
T-16 weeks  evaluation hardware secured; baselines building and running
T-12 weeks  end-to-end workload runs on the full system; first honest numbers
T-8  weeks  design sections drafted; experiment matrix frozen (osdi-experiments)
T-5  weeks  full draft at ~12 pages; internal "hostile PC" read scheduled
T-3  weeks  rewrite from the hostile read; every objection answered in-text,
            because no rebuttal will exist to answer it later
T-1  week   register title/abstract/track on HotCRP (the Dec 4 gate)
T-3 days    anonymization sweep: names, institutions, renamed system, metadata
T-0         submit; verify by re-downloading from HotCRP, not from memory
```

The hostile-read slot at T-5 is the workflow's load-bearing beam in a no-response
cycle: it is the only rebuttal your paper will ever get, so schedule real colleagues
against real review criteria, not a proofread.

## The silent window (December → March)

Use the review window for work that pays regardless of outcome:

- Prepare the artifact **now** — the OSDI '26 Call for Artifacts explicitly encouraged
  preparing while the paper is under consideration, and the May 8 deadline lands close
  to the March 26 notification (`osdi-artifact-evaluation`).
- Keep the testbed image and traces frozen; a conditional accept can mandate new
  experiments on short notice (`osdi-author-response`).
- Draft the retarget: if rejected, which venue, and what must change beyond formatting.

## Notification branches (March 26)

- **Accept** — proceed to `osdi-camera-ready`; June 9 is closer than it looks once the
  artifact appendix and de-anonymization are in the loop.
- **Conditional accept** — the heavyweight branch: the PC's mandated changes must be
  completed by the final-paper deadline and approved by the shepherd, or the paper is
  rejected from the program. Treat the shepherd letter as a contract with a June 9
  delivery date (`osdi-author-response`).
- **Reject** — run the retarget within two weeks while the reviews are fresh. Both
  flagships are annual now (OSDI since 2021, SOSP since 2024), so the realistic map is
  SOSP or NSDI next, EuroSys or the ACM SIGOPS-stewarded ATC as the widening circle.
  Fix what reviews actually said before re-aiming; systems PCs overlap heavily.

## The retargeting calendar

Because OSDI (annual since 2021) and SOSP (annual since 2024) both offer a deadline
every year, a systems paper is never more than a few months from its next flagship
shot. Sketch of the circuit as of the 2026 cycle — every row 待核实 against the live
CFP before committing, since each venue re-sets dates annually:

| Venue | Historical deadline zone | Check |
|---|---|---|
| OSDI | early–mid December (Dec 4/11 in the '26 cycle) | usenix.org/conference/osdi<yy> |
| SOSP | spring (varies by edition) | sosp.org / SIGOPS pages |
| NSDI | two deadlines per year (spring + fall) | usenix.org/conference/nsdi<yy> |
| EuroSys | spring and/or fall (varies) | euro-sys.org |
| FAST | autumn | usenix.org/conference/fast<yy> |
| ATC successor (ACM SIGOPS) | new cadence — verify | SIGOPS announcements |

Retargeting rule: one venue hop per revision. Fix what the reviews said, then aim
once; papers that ricochet unchanged through the circuit meet the same reviewers.

## Failure modes this skill exists to prevent

- Discovering the PST convention at 11 pm AoE on deadline day.
- Skipping title registration because "the paper deadline is the deadline."
- Spending the silent window idle, then hitting May 8 with no artifact and June 9 with
  unshepherded mandated changes.
- Resubmitting a rejected paper unchanged to a PC that half-overlaps last year's.

## Multi-paper coordination

Groups submitting several papers to one OSDI deadline inherit extra constraints: the
**eight-submissions-per-author cap** binds across the group's author lists, so
reconcile who is on what before registration week, not after; shared infrastructure
(testbed, trace archive, figure pipeline) should be frozen once for all papers to
prevent one team's kernel upgrade from invalidating another's runs; and the
December 4 registration gate is the natural checkpoint for a group-level go/no-go
on each paper — a weak submission spends reviewer goodwill that a strong one from
the same group may need.

## Output format

```text
[Cycle] OSDI '<yy> — dates confirmed live? yes/no (if no: 待核实)
[Today's phase] pre-registration / silent window / shepherding / camera-ready / retarget
[Next gate] date + what must be true + owner
[Local cutoff] Pacific deadline converted to team time zone
[Risk ledger] top 3 risks to the next gate, each with a named owner
```
