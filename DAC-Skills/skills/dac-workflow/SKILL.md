---
name: dac-workflow
description: Use to plan a full ACM/IEEE Design Automation Conference (DAC) Research-Manuscript campaign backward from the mid-to-late-November manuscript deadline through the two-stage abstract-then-manuscript submission on Softconf, the winter review, the March notification, the April camera-ready and copyright for the ACM Digital Library, and the July conference in Long Beach — with the Engineering-Track and Late-Breaking-Results side calendars.
---

# DAC Workflow

Run the DAC year backward from the deadline. DAC's Research-Manuscript cycle is a **single annual
deadline in mid-to-late November** (DAC 2026: manuscript ~19 November 2025) leading to a **July**
conference (DAC 2026: Long Beach, California, 26-29 July 2026). Unlike the two-cycle software
venues, DAC gives you one archival shot per year, so the calendar is unforgiving. Every date below
is a **DAC 2026 snapshot** read on 2026-07-09; reopen the live event pages first
(`resources/official-source-map.md`).

## The two-stage submission (do not miss stage one)

DAC splits the research submission into **two stages on the Softconf/START system** (`dac26`):

- **Stage 1 — Abstract.** Register title, full abstract, and **all co-authors** roughly a week
  before the manuscript deadline. This stage seeds reviewer assignment and conflict detection; if
  you skip it, the system will not accept your PDF later.
- **Stage 2 — Manuscript.** Upload the anonymized 6+1-page PDF by the manuscript deadline. There is
  **no grace period** to fix a malformed or non-anonymous PDF after the cutoff.

Register with the real title and abstract, not a placeholder — the abstract drives which TPC
members bid on and are assigned to your paper.

## The DAC 2026 research calendar (snapshot — verify each cycle)

```text
[~Nov 12, 2025]  Abstract stage closes (title/abstract/co-authors on Softconf)   待核实 exact day
[Nov 19, 2025]   Research Manuscript deadline (final anonymized 6+1 PDF)          待核实 exact day
[Nov 2025-Feb]   Double-blind TPC review + program-committee discussion
[Feb 23, 2026]   Accepted research-manuscript IDs published
[Mar 9, 2026]    Accept / reject notifications
[Mar 23, 2026]   Acceptance confirmation forms due
[Apr 14, 2026]   Copyright form + final (proceedings) manuscript due — ACM DL camera-ready
[Jul 26-29, 2026] DAC 2026, Long Beach Convention Center — presentation + exhibition
```

Whether DAC 2026 runs an **author rebuttal / response period** between review and notification is
**待核实** — DAC's research review has historically been TPC-driven without the ISCA/MICRO-style
author response. Do not plan a rebuttal window into your calendar until the live cycle confirms one.

## Side calendars (different deadlines — do not conflate)

- **Engineering Track:** separate call, separate committee, later Call-for-Contributions deadline
  (DAC 2026 extended to ~20 January 2026). Presentation-oriented; see `dac-topic-selection`.
- **Late Breaking Results (LBR):** short poster-style track on `softconf.com/dac26/lbr26`, deadline
  in early 2026 (extended in past cycles into ~March). Good for a timely, early result that is not
  yet an archival Research Manuscript.
- **Special Sessions / Panels / Tutorials / Workshops:** proposal-based, their own timelines.

## Backward plan from the November manuscript deadline

```text
[Deadline − 12 wk]  Lock the contribution and the QoR claim; pick benchmark suites (ISPD/EPFL/
                    ISCAS/ITC/TAU/CircuitNet) and the baselines you must beat
[Deadline − 8 wk]   Freeze the experimental harness; start the runs that take longest (full-flow
                    P&R, large-benchmark sweeps) — these cannot be compressed at the end
[Deadline − 4 wk]   Full draft in the ACM double-column template; check the 6-page body budget early
[Deadline − 2 wk]   Internal review; tighten to 6+1; build every figure at column width and legible
[Deadline − 1 wk]   Complete the abstract stage on Softconf with the real title/abstract/co-authors
[Deadline − 3 day]  Double-blind sweep on the PDF; re-run the headline numbers on a clean checkout
[Deadline − 1 day]  Upload; re-download and read the PDF cold; confirm it is the intended file
```

## Between notification and camera-ready

- **Accept:** de-anonymize, apply the ACM template's final-version rules, complete metadata and the
  copyright form, and hit the April proceedings deadline for the **ACM Digital Library** archival
  version (`dac-camera-ready`).
- **Reject:** DAC has no formal appeal; reroute promptly — **ICCAD** (fall), **DATE** (Europe),
  **ASP-DAC** (January), or a journal (TCAD/TODAES) — using `dac-topic-selection`.

## Standing reminders

- One archival deadline a year: a missed November means a full year, so calendar the abstract stage,
  not just the manuscript stage.
- The 6-page body budget is tight; plan the paper's argument to *fit* six double-column pages rather
  than writing long and cutting.
- Track choice (Research vs Engineering) is a workflow decision made *before* the deadline, not a
  fallback after rejection.

## Output format

```text
[Cycle target]     DAC 20XX research manuscript / engineering track / LBR
[Abstract stage]   locked by the earlier cutoff? yes/no
[Manuscript stage] on track for the November deadline? blockers?
[Longest runs]     which experiments gate the deadline; started? yes/no
[Post-decision]    camera-ready plan (ACM DL, April) or reroute target (ICCAD/DATE/ASP-DAC)
```
