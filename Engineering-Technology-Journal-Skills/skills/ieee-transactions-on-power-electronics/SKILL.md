---
name: ieee-transactions-on-power-electronics
description: Use when targeting IEEE Transactions on Power Electronics (TPEL) or deciding whether a power-conversion manuscript fits this venue. Encodes the journal's fit, the hardware-validation bar, the converter-and-control scope, the TPEL-vs-TIE routing, house style, official-submission re-check, and desk-reject heuristics.
---

# IEEE Transactions on Power Electronics (ieee-transactions-on-power-electronics)

## Journal positioning

IEEE Transactions on Power Electronics (TPEL) is the leading archival venue for power
conversion: converter and inverter topologies, motor drives, control of
power-electronic systems, magnetics and passive components, wide-bandgap devices in
circuits, and power-electronics-enabled energy systems. The defining expectation is a
**concrete power-conversion advance backed by experimental validation** — a topology,
modulation, or control method whose benefit (efficiency, power density, reliability,
dynamic response) is demonstrated on hardware, not only in simulation. Simulation-only
proposals and minor topology permutations without measured benefit are a weak fit.
This skill is a **fit / venue-selection / re-framing** tool. It does not replace the
journal's current official author guidelines. Before submitting, re-check the live
IEEE Transactions on Power Electronics author information and submission system.

## When to trigger

- The author names TPEL for a converter, inverter, drive, or power-electronic-control
  manuscript and wants a fit/framing check.
- A design must be re-framed from "we built a converter" into a generalizable
  power-conversion contribution with measured, benchmarked benefit.
- The author is choosing between TPEL and `ieee-transactions-on-industrial-electronics`
  (broader industrial electronics) or an energy-systems venue.
- The author needs the hardware-validation bar and desk-reject heuristics specific to
  power electronics.

## Scope & topic fit

- Converter and inverter topologies: DC-DC, DC-AC, AC-DC, multilevel, resonant, and
  soft-switching converters with a clear conversion advantage.
- Modulation and control of power-electronic systems: current/voltage control, model
  predictive control, stability of grid-tied and standalone converters.
- Motor drives and electric-machine control from the power-electronics side: drive
  topologies, modulation, and torque/efficiency performance.
- Wide-bandgap (SiC/GaN) device application in converters, gate drives, packaging, and
  thermal management with measured impact.
- Magnetics, passive components, EMI, and reliability of power-electronic converters;
  power-electronics interfaces for renewables, storage, and transportation.

## Method & evidence bar

- The contribution is a **power-conversion method with experimental validation** — a
  hardware prototype with measured efficiency, power density, thermal, dynamic, or
  reliability results, typically expected at this venue.
- Simulation establishes design and operating principles but generally does not
  substitute for measurement; the absence of any hardware result is a common weakness.
- Efficiency and performance must be benchmarked against the relevant state-of-the-art
  topology/control under comparable conditions, with operating points and loss
  breakdowns reported.
- Claims (e.g., higher efficiency, lower EMI, better dynamics) must be supported by
  instrumented measurements with stated test conditions, component ratings, and
  control parameters.
- The contribution must generalize beyond one built unit: the design principle,
  trade-offs, and applicable operating range should be made explicit.

## Structure & house style

- IEEE format; TPEL publishes full **Papers** and shorter **Letters** — match scope to
  the article type and re-check current definitions and limits on the live guide.
- The introduction motivates the conversion problem and positions against prior
  topologies/control; the analysis derives the operating principle before the
  experiment validates it.
- Figures are central and quantitative: schematics, modulation/control diagrams,
  measured waveforms, efficiency/loss curves, thermal images, and prototype photos.
- Hardware specifications (devices, magnetics, switching frequency, power level) must
  be reported in enough detail to reproduce the result.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and
  `../../resources/official-source-map.md`; start from the IEEE Author Center anchors,
  then cite the current Transactions on Power Electronics page you checked.
- Search the live site for "IEEE Transactions on Power Electronics information for
  authors" and follow the current submission-system version.
- Re-check article types (Paper vs. Letter), length/overlength policy, and the IEEE
  template.
- Confirm expectations for experimental validation, measured-data reporting, and any
  reproducibility requirements.
- Re-check ORCID, competing-interests, funding, author-contribution, and AI-use
  disclosure requirements, and IEEE open-access options.
- If the live official instructions conflict with this skill, the official
  instructions win.

## Pre-submission self-check

- [ ] The contribution is a generalizable power-conversion advance, not a one-off build or a minor topology permutation.
- [ ] A hardware prototype provides measured efficiency/dynamic/thermal/reliability results, not simulation only.
- [ ] Performance is benchmarked against the relevant state-of-the-art topology/control under comparable conditions.
- [ ] Loss breakdowns, operating points, and test conditions are reported.
- [ ] Component ratings, switching frequency, and control parameters are detailed enough to reproduce.
- [ ] Article type (Paper vs. Letter) and length fit current limits.

## Common desk-reject triggers

- Simulation-only converter/control proposal with no experimental validation.
- A minor topology permutation with no measured efficiency/performance benefit over existing designs.
- Efficiency claims with no loss breakdown, no benchmark, or under non-comparable test conditions.
- Results from a single built unit with no generalizable design principle or trade-off analysis.
- Application/integration paper where power electronics is incidental and no converter-level advance is shown.

## Re-routing decision

- Broader industrial-electronics, drives, or industrial-systems emphasis → `ieee-transactions-on-industrial-electronics`.
- Grid/system-level integration rather than the converter → `ieee-transactions-on-power-systems`.
- Energy-system performance is the primary narrative → `applied-energy`.
- Battery/storage-cell or device materials focus → `journal-of-power-sources` / `energy-storage-materials`.
- Broad tutorial/survey of a power-electronics area → `proceedings-of-the-ieee`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] IEEE Transactions on Power Electronics
[Topic tags] <2–3 closest power-electronics subtopics>
[Conversion advance] <the topology/control idea and the metric it improves>
[Hardware validation] <prototype + measured results present? benchmarked?>
[Top risk] <the single most likely reason for rejection>
[Article type] Paper / Letter
[Official items to re-check] <article type / length / experimental-validation / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
