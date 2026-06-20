---
name: journal-of-power-sources
description: Use when targeting Journal of Power Sources or deciding whether an electrochemical-power-device manuscript fits this venue. Encodes the journal's fit, the device-and-electrochemistry contribution bar, cell-level performance and diagnostics rigor, house style, the device-vs-materials routing, official-submission re-check, and desk-reject heuristics.
---

# Journal of Power Sources (journal-of-power-sources)

## Journal positioning

Journal of Power Sources (Elsevier) is an archival venue for the **science and
technology of electrochemical power devices**: batteries, fuel cells, and
supercapacitors at the cell/electrode/electrolyte level — their engineering,
performance, degradation, and diagnostics. Its center of gravity is the **device and
its electrochemistry**: how an electrode, electrolyte, interface, or cell architecture
governs measured device behavior (capacity, rate, efficiency, cycle life, failure). A
paper that reports only a new active material's properties, with electrochemistry as an
afterthought, fits the materials family better; this journal rewards an advance you can
read in the cell's performance and diagnostics. This skill is a **fit / venue-selection
/ re-framing** tool. It does not replace the journal's current official author
guidelines. Before submitting, re-check the live Journal of Power Sources Guide for
Authors on the Elsevier site.

## When to trigger

- The author names Journal of Power Sources for a battery, fuel-cell, or supercapacitor
  manuscript centered on cell/electrode/electrolyte engineering or diagnostics.
- A paper must be re-framed from "we made a material" into a device-and-electrochemistry
  story tied to measured cell performance and degradation.
- The author is deciding between this device venue and the materials-mechanism venue
  `energy-storage-materials`, or the systems venue `applied-energy`.
- The author needs the journal's cell-level performance and diagnostics rigor bar and
  desk-reject heuristics.

## Scope & topic fit

- Batteries: electrode and electrolyte engineering, cell design, performance, and
  the electrochemistry governing rate, capacity, and efficiency at the device level.
- Degradation, aging, safety, and failure analysis: cycle-life, calendar aging,
  thermal behavior, and post-mortem/operando diagnostics of cells.
- Fuel cells and electrolyzers: catalyst layers, membranes/electrolytes, and
  cell/stack performance, durability, and water/thermal management.
- Supercapacitors and hybrid devices: electrode and electrolyte engineering with
  device-level rate and energy/power characterization.
- Diagnostics and characterization methods (EIS, operando, modeling of cells) that
  illuminate device behavior, performance, or degradation mechanisms.
- Cell-level modeling and battery-management-relevant analysis tied to measured devices.

## Method & evidence bar

- The central claim is a **device/electrochemistry advance**: the contribution must be
  legible in cell-level metrics under clearly stated, realistic protocols, not only in
  material characterization.
- Electrochemical testing must report mass/areal loading, current density (C-rate or
  mA cm⁻²), voltage window, electrolyte, and cell configuration; half-cell vs. full-cell
  context must be honest.
- Performance must be benchmarked against credible device-level state-of-the-art under
  comparable conditions; capacity/rate claims at trivial loadings are weak.
- Degradation/diagnostics claims require sufficient cycling/aging duration and a
  mechanism supported by operando or post-mortem evidence, not a single fade curve.
- Reproducibility: report cell-build details, number of cells, and statistics; safety-
  relevant claims need appropriate characterization.

## Structure & house style

- Standard research-article structure (introduction, experimental, results,
  discussion); the journal uses highlights and a graphical abstract — re-check current
  article types and requirements on the live guide.
- The introduction frames the device/electrochemistry gap and the performance or
  degradation problem; the discussion ties electrode/electrolyte/interface variables to
  measured cell behavior.
- Figures are load-bearing: rate and cycling data at stated loadings, voltage profiles,
  EIS/operando diagnostics, and post-mortem analysis with controls.
- Supporting information carries full cell-build and testing protocols and extended
  electrochemical data; main-text figures must support the device claim on their own.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and
  `../../resources/official-source-map.md`; start from the Elsevier anchors, then cite
  the current Journal of Power Sources Guide for Authors page you checked.
- Search the live site for "Journal of Power Sources guide for authors" and follow the
  current Elsevier/Editorial Manager version.
- Re-check article types, highlights and graphical-abstract requirements, and
  electrochemical-reporting conventions (loadings, current densities, cell type).
- Confirm data-availability and any expectation to report full cell-build and cycling
  protocols for reproducibility.
- Re-check competing-interests, funding, author-contribution (CRediT), and AI-use
  disclosure requirements.
- If the live official instructions conflict with this skill, the official
  instructions win.

## Pre-submission self-check

- [ ] The advance is legible in cell-level performance/degradation, not only in material characterization.
- [ ] Loading, current density, voltage window, electrolyte, and cell configuration are reported; half- vs full-cell context is honest.
- [ ] Performance is benchmarked against device-level state-of-the-art under comparable conditions, at realistic loadings.
- [ ] Degradation/diagnostics claims have sufficient duration and operando/post-mortem mechanism evidence.
- [ ] Cell-build details, number of cells, and statistics are reported for reproducibility.
- [ ] Highlights and graphical abstract represent the device/electrochemistry advance.

## Common desk-reject triggers

- Material-only study with token electrochemistry and no device-level contribution.
- Capacity/rate claims at trivial mass/areal loadings or with undisclosed test conditions.
- Half-cell results presented as if they were full-cell device performance.
- Single fade curve offered as degradation analysis with no mechanism or operando/post-mortem evidence.
- Performance benchmarked against a strawman or under non-comparable protocols.
- Pure materials-synthesis or pure mechanism paper better suited to a materials venue.

## Re-routing decision

- Electrode/electrolyte materials and structure–property mechanism as the core → `energy-storage-materials`.
- Systems-level energy integration / techno-economic scope → `applied-energy`.
- Membrane/electrolyte transport mechanism as the central science → `journal-of-membrane-science`.
- Applied electrocatalysis as a process/material advance → `chemical-engineering-journal`.
- Highest-profile energy-device breakthrough → `nature-energy` or `joule` (different selectivity/format; re-check).

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Journal of Power Sources
[Topic tags] <2–3 closest device subtopics (battery/fuel-cell/supercapacitor)>
[Device advance] <the cell/electrode/electrolyte advance read in device metrics, one line>
[Test conditions] <loading / current density / cell type / window stated?>
[Diagnostics/degradation] <duration + operando/post-mortem mechanism present?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / highlights / electrochemical-reporting / data policy / disclosures>
[Re-route suggestion] <if material/system-level, a better-matched venue>
```
