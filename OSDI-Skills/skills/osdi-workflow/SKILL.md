---
name: osdi-workflow
description: Use when planning or managing a full OSDI cycle — the December abstract-registration and submission deadlines on HotCRP (December 1 / 8, 2026 for OSDI '27), the silent no-rebuttal review window, March notification, the post-acceptance artifact deadline, June shepherded final papers, and the July conference — including rejection retargeting to SOSP or NSDI.
---

# OSDI Workflow

Project-manage the OSDI year. All dates below are the verified OSDI '27 pipeline
(re-verified 2026-11-24 against the live CFP and HotCRP clock) and are one cycle's
snapshot. As of that date the registration gate is a week away.

## The OSDI '27 pipeline, with what each date actually demands

| Date (OSDI '27 cycle) | Gate | What must be true by then |
|---|---|---|
| Dec 1, 2026, 5:59 pm EST (2:59 pm PST) | Abstract registration (both tracks) | Title, real abstract, authors, conflicts, track, senior reviewer (or exemption) on HotCRP |
| Dec 8, 2026, 5:59 pm EST (2:59 pm PST) | Complete paper | Final anonymized 12-page PDF (+ optional supplementary files) uploaded |
| Mar 16, 2027 | Notification | Decision: accept / conditional accept / reject |
| Artifact deadline — 待核实 | Artifact submission | Archive + AE README ready (accepted papers); '27 call not yet published |
| Jun 3, 2027 | Final papers | Shepherd-approved 14-page PDF (+ references) in the system |
| Jul 7–9, 2027 | Conference (Baltimore) | Presenter registered at full price and prepared |

History: OSDI '26 ran Dec 4 / Dec 11, 2025 (2:59 pm PST) → March 26 → artifacts May 8
→ final papers June 9 → Seattle, July 13–15, 2026.

Three structural notes that surprise newcomers:

- **The deadlines are US clock time, not AoE.** 5:59 pm EST (2:59 pm PST) is late-night only in
  Europe; in East Asia it is early morning the next day. Compute your local cutoff
  explicitly and pin it in the team calendar.
- **Registration is a real deadline a week before the paper.** Miss December 1 and
  December 8 is irrelevant; a placeholder abstract is desk-rejected.
- **Nothing happens between December and March that you can influence.** OSDI '26
  removed the author-response period and the '27 CFP describes none, so the review
  window is silent by design — except that the named senior reviewer may be invited to
  review up to four papers in the first full round. Budget their time.

## Backward plan from December

Work backward from submission, owning each risk by name:

```text
T-16 weeks  evaluation hardware secured; baselines building and running
T-12 weeks  end-to-end workload runs on the full system; first honest numbers
T-8  weeks  design sections drafted; experiment matrix frozen (osdi-experiments)
T-5  weeks  full draft at ~12 pages; internal "hostile PC" read scheduled
T-3  weeks  rewrite from the hostile read; every objection answered in-text,
            because no rebuttal will exist to answer it later
T-1  week   register title/abstract/track/senior reviewer on HotCRP (the Dec 1 gate)
T-3 days    anonymization sweep: names, institutions, renamed system, metadata
T-0         submit; verify by re-downloading from HotCRP, not from memory
```

The hostile-read slot at T-5 is the workflow's load-bearing beam in a no-response
cycle: it is the only rebuttal your paper will ever get, so schedule real colleagues
against real review criteria, not a proofread.

## The silent window (December → March)

Use the review window for work that pays regardless of outcome:

- Prepare the artifact **now** — the latest Call for Artifacts (OSDI '26) explicitly
  encouraged preparing while the paper is under consideration, and its deadline landed
  about six weeks after notification (`osdi-artifact-evaluation`; '27 dates 待核实).
- Keep the testbed image and traces frozen; a conditional accept can mandate new
  experiments on short notice (`osdi-author-response`).
- Draft the retarget: if rejected, which venue, and what must change beyond formatting.

## Notification branches (March 16, 2027)

- **Accept** — proceed to `osdi-camera-ready`; June 3 is closer than it looks once the
  artifact appendix and de-anonymization are in the loop.
- **Conditional accept** — the heavyweight branch: the PC's mandated changes must be
  completed by the final-paper deadline and approved by the shepherd, or the paper is
  rejected from the program; there is no revise-and-resubmit. Treat the shepherd letter
  as a contract with a June 3 delivery date (`osdi-author-response`).
- **Reject** — run the retarget within two weeks while the reviews are fresh. Both
  flagships are annual now (OSDI since 2021, SOSP since 2024), so the realistic map is
  SOSP or NSDI next, EuroSys or the ACM SIGOPS-stewarded ATC as the widening circle.
  Fix what reviews actually said before re-aiming; systems PCs overlap heavily — and OSDI
  '27 itself asks resubmissions of papers rejected elsewhere for an improvement summary.

## The retargeting calendar

Because OSDI (annual since 2021) and SOSP (annual since 2024) both offer a deadline
every year, a systems paper is never more than a few months from its next flagship
shot. Sketch of the circuit as of late 2026 — every row 待核实 against the live
CFP before committing, since each venue re-sets dates annually:

| Venue | Historical deadline zone | Check |
|---|---|---|
| OSDI | early December (Dec 1/8, 2026 for OSDI '27) | usenix.org/conference/osdi<yy> |
| SOSP | spring (varies by edition) | sosp.org / SIGOPS pages |
| NSDI | two deadlines per year (spring + fall) | usenix.org/conference/nsdi<yy> |
| EuroSys | spring and/or fall (varies) | euro-sys.org |
| FAST | autumn | usenix.org/conference/fast<yy> |
| ATC successor (ACM SIGOPS) | new cadence — verify | SIGOPS announcements |

Retargeting rule: one venue hop per revision. Note the collision OSDI '27 called out: a
paper still under NSDI '27 Fall review on December 8, 2026 cannot go to OSDI '27. Fix what the reviews said, then aim
once; papers that ricochet unchanged through the circuit meet the same reviewers.

## Failure modes this skill exists to prevent

- Discovering the EST/PST convention at 11 pm AoE on deadline day.
- Skipping title registration because "the paper deadline is the deadline."
- Spending the silent window idle, then hitting the artifact deadline with nothing and June 3 with
  unshepherded mandated changes.
- Resubmitting a rejected paper unchanged to a PC that half-overlaps last year's.

## Multi-paper coordination

Groups submitting several papers to one OSDI deadline inherit extra constraints: the
**eight-submissions-per-author cap** binds across the group's author lists, so
reconcile who is on what before registration week, not after; shared infrastructure
(testbed, trace archive, figure pipeline) should be frozen once for all papers to
prevent one team's kernel upgrade from invalidating another's runs; and the
December 1 registration gate is the natural checkpoint for a group-level go/no-go
on each paper — a weak submission spends reviewer goodwill that a strong one from
the same group may need.

## Output format

```text
[Cycle] OSDI '<yy> — dates confirmed live? yes/no (if no: 待核实)
[Today's phase] pre-registration / silent window / shepherding / camera-ready / retarget
[Next gate] date + what must be true + owner
[Local cutoff] 5:59 pm EST deadline converted to team time zone
[Risk ledger] top 3 risks to the next gate, each with a named owner
```
