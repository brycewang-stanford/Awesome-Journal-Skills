---
name: icassp-workflow
description: Use when planning an ICASSP project timeline — the annual clock from venue fit through the September paper deadline, single-blind review, the short winter rebuttal, spring notification, IEEE Xplore camera-ready, and the May conference — with backward-planning offsets and the choice among standard, OJSP-ICASSP, and grand-challenge tracks.
---

# ICASSP Workflow

Use this as the project-management skill for an ICASSP submission. Replace every date with the
current official timetable and work backward from the paper deadline. ICASSP is an **IEEE
Signal Processing Society conference**, rebuilt by a new local committee each year; it has no
standing editor-in-chief, and the cost model is registration, with the proceedings paper
published in IEEE Xplore.

## The annual clock (2026-cycle shape, verify each year)

- **September** — full-paper deadline on the CMS portal (ICASSP 2026: 17 Sep 2025; **ICASSP 2027
  reported ~16 Sep 2026, the next major gate as of 2026-07-09**).
- **Autumn/early winter** — single-blind technical-committee review.
- **December** — short rebuttal/author-response window (2026 cycle: reported to ~22 Dec 2025), if
  the cycle runs one.
- **Late winter** — notification; accepted-paper revision window (2026: to ~28 Jan 2026).
- **Spring** — IEEE Xplore camera-ready (PDF eXpress + IEEE copyright form), registration.
- **May** — the conference; in-person oral or poster presentation (ICASSP 2026 Barcelona, 4-8 May;
  ICASSP 2027 Toronto, 16-21 May).

## Milestones

- **Venue fit** — confirm the contribution is genuinely signal-processing and ICASSP-routed, not a
  generic-ML paper or a speech paper better suited to Interspeech (see `icassp-topic-selection`).
- **Evidence lock** — freeze the mechanism, the task-matched metric, the standard baseline, the
  condition sweep, and seeds.
- **Paper deadline** — upload the 4+1 PDF with the author list (single-blind), EDICS, and the
  ethical-standards statement through CMS.
- **Rebuttal** — if it runs, reply early and move the one decision-critical objection.
- **Notification and camera-ready** — integrate reviewer fixes within the accepted claim, pass PDF
  eXpress, sign the copyright form, register.
- **Conference** — present in person; ship the public artifact.

## Backward plan from the September deadline

| Weeks out (heuristic) | Milestone |
|---|---|
| 8+ | Mechanism frozen; standard corpus and scorer chosen |
| 6 | Baseline reproduced on the same corpus/split/scorer |
| 4 | Condition sweep and ablation complete, seeds logged |
| 3 | Full draft sitting in the IEEE 4+1 two-column template |
| 2 | Internal mock review by a subfield-fluent colleague |
| 1 | PDF eXpress pass, author-block/ethics check, figure legibility |
| 0 | Upload via CMS; download and re-read the stored PDF |

These offsets are planning heuristics — anchor each to the current official timetable, never to a
past cycle.

## Track decision (decide before the deadline)

```text
Standard 4+1        -> TPC review, IEEE Xplore proceedings, in-person present
OJSP-ICASSP 8+1     -> OJSP editorial review, open-access journal, present (not in proceedings),
                       earlier pre-registration deadline
SPS-journal present -> already-accepted SPS-journal paper, not re-reviewed, not in proceedings
Grand Challenge     -> short paper via the challenge, present, may appear in proceedings
```

## Failure modes by stage

- Choosing the corpus or metric late forces a scramble that a subfield reviewer sees through.
- Leaving format conversion to the final week surfaces four-page overflow too late; IEEE
  two-column is tighter than a working draft.
- Skipping the mock review forfeits the one chance to hear "that is the wrong metric for this
  task" from a friend rather than a reviewer.
- Missing a track's separate earlier deadline (OJSP pre-registration, grand challenge) forecloses
  the best-fit path.

## Coordination notes

- Assign one named owner for the CMS submission (format, EDICS, metadata) and another for the
  reproducibility package; shared ownership is how both slip.
- Archive the exact submitted PDF, since a rebuttal must quote it precisely.

## Output format

```text
[Current stage] idea / experiments / writing / submission / rebuttal / accepted / camera-ready
[Next official deadline] <date and source, or unknown>
[Track] standard / OJSP-ICASSP / journal-present / grand-challenge
[Critical path] <three tasks that determine readiness>
[Owner map] <task -> person or role>
```

## Currency note

The 2026-cycle dates and the ICASSP 2027 September gate were checked 2026-07-09 (see
`../../resources/official-source-map.md`); the 2027 exact deadline is 待核实 until its CFP is
readable directly. Nothing carries from Barcelona to Toronto automatically — re-open the current
call.
