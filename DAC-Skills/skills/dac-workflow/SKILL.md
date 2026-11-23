---
name: dac-workflow
description: Use to plan a full ACM/IEEE Design Automation Conference (DAC) Research-Manuscript campaign backward from the mid-November manuscript deadline through the two-stage abstract-then-manuscript submission on Softconf, the winter review, the March notification, the end-of-March proceedings manuscript and IEEE copyright form for IEEE Xplore and the ACM Digital Library, the April registration and slide deadlines, and the July conference in San Jose — with the Engineering-Track side calendar.
---

# DAC Workflow

Run the DAC year backward from the deadline. DAC's Research-Manuscript cycle is a **single annual
deadline in mid-November** (DAC 2027: manuscript 18 November 2026) leading to a **July**
conference (DAC 2027: San Jose Convention Center, California, 11-14 July 2027). Unlike the
two-cycle software venues, DAC gives you one archival shot per year, so the calendar is
unforgiving. Every date below is the **DAC 2027 timeline** read on 2026-11-24 from
`dac.com/2027/program/research-manuscript-submissions`; its submission stages have already closed,
so for a new paper reopen the next call first (`resources/official-source-map.md`).

## The two-stage submission (do not miss stage one)

DAC splits the research submission into **two stages on the Softconf/START system** (DAC 2027:
`softconf.com/dac27/research`):

- **Stage 1 — Abstract.** Register title, an abstract of approximately 100 words, **all
  co-authors** (names, affiliations, countries, emails) and their TPC conflicts one week before
  the manuscript deadline. This stage seeds reviewer assignment and conflict detection; if
  you skip it, the system will not accept your PDF later.
- **Stage 2 — Manuscript.** Upload the anonymized 6+1-page PDF by the manuscript deadline. There is
  **no grace period** to fix a malformed or non-anonymous PDF after the cutoff.

Register with the real title and abstract, not a placeholder — the abstract drives which TPC
members bid on and are assigned to your paper.

## The DAC 2027 research calendar (official timeline — verify each cycle)

```text
[Nov 11, 2026]   Abstract stage closes, 5 PM US Pacific (title/abstract/co-authors/COIs)
[Nov 18, 2026]   Research Manuscript deadline, 5 PM US Pacific (anonymized 6+1 PDF)
[Nov 2026-Feb]   Double-blind TPC review + program-committee discussion
[Feb 22, 2027]   Accepted research-manuscript IDs published on the DAC website
[Mar 08, 2027]   Accept / reject notifications
[Mar 22, 2027]   Manuscript confirmation due
[Mar 31, 2027]   Proceedings manuscript deadline (IEEE Copyright Form emailed in March)
[Apr 10, 2027]   Author registration deadline (one full Speaker Registration per paper)
[Apr 15, 2027]   Draft slides due for review
[May 14, 2027]   Slide feedback provided
[May 21, 2027]   Final slides due
[Jul 11-14, 2027] DAC 2027, San Jose Convention Center — in-person talk + poster + exhibition
```

The DAC 2027 timeline has **no author rebuttal / response period** between the manuscript deadline
and the notifications — DAC's research review is TPC-driven without the ISCA/MICRO-style author
response. Do not plan a rebuttal window into your calendar.

## Side calendars (different deadlines — do not conflate)

- **Engineering Tracks** (Back-End Design, Front-End Design, IP, Systems and Software): separate
  call, separate Engineering Program Chair and committee, later deadline (DAC 2027: submissions
  11 January 2027; accept/reject 8 March 2027; presenter registration 10 April 2027). No
  manuscript, no publication; see `dac-topic-selection`.
- **Late Breaking Results (LBR):** DAC 2026 ran a short poster-style LBR track on
  `softconf.com/dac26/lbr26`; the DAC 2027 call lists none as of 2026-11-24 (**待核实** whether
  one is added). Rejected research manuscripts may instead be **invited to a Work-in-Progress
  poster** (not published).
- **Special Sessions / Panels / Tutorials / Workshops:** proposal-based, their own timelines.

## Backward plan from the November manuscript deadline

```text
[Deadline − 12 wk]  Lock the contribution and the QoR claim; pick benchmark suites (ISPD/EPFL/
                    ISCAS/ITC/TAU/CircuitNet) and the baselines you must beat
[Deadline − 8 wk]   Freeze the experimental harness; start the runs that take longest (full-flow
                    P&R, large-benchmark sweeps) — these cannot be compressed at the end
[Deadline − 4 wk]   Full draft in the IEEE double-column template; check the 6-page body budget early
[Deadline − 2 wk]   Internal review; tighten to 6+1; build every figure at column width and legible
[Deadline − 1 wk]   Complete the abstract stage on Softconf with the real title/abstract/co-authors
[Deadline − 3 day]  Double-blind sweep on the PDF; re-run the headline numbers on a clean checkout
[Deadline − 1 day]  Upload; re-download and read the PDF cold; confirm it is the intended file
```

## Between notification and camera-ready

- **Accept:** confirm by the manuscript-confirmation date, de-anonymize, apply the IEEE template's
  final-version rules, sign the IEEE Copyright Form, hit the end-of-March proceedings deadline,
  register by the April author-registration deadline (publication in IEEE Xplore and ACM DL is
  contingent on registration and poster-session presentation), and prepare slides and a poster
  (`dac-camera-ready`).
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
[Post-decision]    camera-ready plan (IEEE copyright, end of March; registration, April) or reroute target (ICCAD/DATE/ASP-DAC)
```
