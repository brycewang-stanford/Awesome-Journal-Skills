---
name: ppopp-workflow
description: Use when planning a PPoPP submission campaign end to end, sequencing the summer paper deadline, the author-response rebuttal window, notification, the post-acceptance CGO-shared artifact-evaluation round, the camera-ready, and the presentation inside the co-located HPCA/CGO/PPoPP/CC week.
---

# PPoPP Workflow

Plan the whole cycle backward from the submission deadline. PPoPP's calendar is entangled with the
co-located **HPCA/CGO/PPoPP/CC** week, so several dates (artifact evaluation, camera-ready,
registration) move in step with CGO. The dates below are the PPoPP 2026/2027 snapshot read on
2026-07-09 (see `resources/official-source-map.md`); reopen the live Important Dates page first,
and confirm whether the year runs one submission round or two.

## The cycle at a glance (PPoPP 2026, the 31st edition)

```text
Sep  1, 2025  Full-paper submission (abstract 100-400 words + PDF), AoE
Oct 27-29     Author-response period (the rebuttal window)
Nov 10        Author notification
Nov 17        Artifact submission to the AE committee
Jan  5, 2026  Artifact-evaluation notification
Jan  9, 2026  Final (camera-ready) paper due
Jan 31-Feb 4  Conference, Sydney (co-located with HPCA/CGO/CC)
```

For **PPoPP 2027** (the 32nd edition, Salt Lake City, March 20–24, 2027), the **summer round**
posts submission **3 August 2026** (`ppopp27-summer.hotcrp.com`), author response **6–8 October
2026**, notification **26 October 2026**. Whether a **fall round** also runs is 待核实 — confirm
before you assume a second bite.

## Backward plan from the deadline

```text
T-0    Submission: 10-page two-column acmart PDF + 100-400 word abstract, double-blind
T-1wk  Freeze the scalability figures; run the double-blind sweep; set PC+ERC conflicts
T-3wk  Final experiments: fill in the core sweep, the strongest baseline, variance bars
T-6wk  Draft complete; run ppopp-writing-style and ppopp-experiments against it
T-3mo  Lock the study design: machines reserved, topology recorded, seeds fixed
```

The unmovable PPoPP-specific risk is **machine time**. Speedup curves, NUMA sweeps, and GPU runs
need reserved, quiescent hardware; a shared cluster the week before the deadline yields noisy,
unrepeatable numbers. Reserve the machine, and record its exact topology, before you need the
final figures.

## The rebuttal window (author response)

- The **author-response period** (PPoPP 2026: 27–29 October 2025) is a fixed 2–3 day window between
  reviews and notification. Treat it as a scheduled deliverable, not a surprise.
- It is short and word-capped; you cannot run a month of new experiments. The experiments that
  answer "does it scale?" and "what about baseline X?" must be **anticipated and pre-run** before
  reviews arrive. See `ppopp-author-response`.

## After notification

- **Accepted for a talk:** proceed to the artifact round and the camera-ready.
- **Automatic poster consideration:** a paper not accepted for a regular presentation is
  **automatically considered for the poster track**, with a **two-page summary in the proceedings**
  — a real, citable outcome. Decide in advance whether you would take it.
- **Rejected outright:** reroute via `ppopp-topic-selection` (CGO/PLDI/ASPLOS/SC or a later PPoPP
  round) rather than resubmitting unchanged.

## The artifact round (post-acceptance, CGO-shared)

- Artifact submission comes **about a week after notification** (PPoPP 2026: 17 November 2025) and
  evaluation runs into the new year (notification 5 January 2026). It is **separate from and
  independent of** the camera-ready.
- PPoPP's AE culture is shared with co-located **CGO**; confirm each cycle which committee runs it
  and which badge set applies. Build the reproducible package now — `ppopp-artifact-evaluation` and
  `ppopp-reproducibility` — not after the camera-ready.

## Camera-ready and presentation

- Camera-ready (PPoPP 2026: 9 January 2026) de-anonymizes, completes ACM rights/metadata, and
  fixes the artifact DOI and any earned badges — see `ppopp-camera-ready`.
- Presentation happens inside the co-located week; at least one author registers and presents.
  Registration and travel for the HPCA/CGO/PPoPP/CC venue are shared logistics — book early.

## Calibration and reverify

- Confirm the number of submission rounds and every date on the current Important Dates page.
- Confirm the artifact deadline is post-acceptance and CGO-shared, and the exact badge set.
- Do not assume last year's cadence; the summer/fall split is exactly the kind of thing that moves.

## Output format

```text
[Cycle target] PPoPP 20XX (edition), submission round, location, co-located family
[Critical path] machine reservation -> experiments -> draft -> double-blind -> submit
[Rebuttal readiness] pre-run experiments for the likely "does it scale / baseline X" asks
[Post-notification] talk / poster (auto-considered) / reroute
[Artifact] AE submission date, badge target, CGO-shared? camera-ready separate
```
