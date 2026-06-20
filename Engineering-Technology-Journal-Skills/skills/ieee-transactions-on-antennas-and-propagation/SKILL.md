---
name: ieee-transactions-on-antennas-and-propagation
description: Use when targeting IEEE Transactions on Antennas and Propagation (TAP) or deciding whether an antennas, applied-electromagnetics, or wave-propagation manuscript fits this venue. Encodes the journal's fit, the theory-plus-simulation-plus-measurement evidence bar, EM-contribution rigor, house style, official-submission re-check, and desk-reject heuristics.
---

# IEEE Transactions on Antennas and Propagation (ieee-transactions-on-antennas-and-propagation)

## Journal positioning

IEEE Transactions on Antennas and Propagation (TAP), published by the IEEE
Antennas and Propagation Society, is a flagship archival venue for **antennas,
applied electromagnetics, and wave propagation**: antenna design and analysis,
electromagnetic theory, scattering and diffraction, computational EM,
metamaterials and metasurfaces for EM, and propagation/channel characterization.
The defining expectation is a genuine **antenna or electromagnetics contribution**
supported by the field's standard evidence chain — sound theory or formulation,
validating full-wave simulation, and, for most antenna papers, fabricated-prototype
**measurement**. Papers whose real contribution is a circuit, a communications
system, or an algorithm, with the antenna present only as a component, are a poor
fit. This skill is a **fit / venue-selection / re-framing** tool. It does not
replace the journal's current official author information. Before submitting,
re-check the live IEEE TAP author guidance and submission system.

## When to trigger

- The author names TAP for an antenna, applied-EM, scattering, or propagation
  manuscript and wants a fit/framing check.
- A design must be re-framed so the **electromagnetic** contribution — not the
  downstream system or circuit — is the headline.
- The author is unsure whether a metamaterial/metasurface result belongs in TAP
  (EM functionality) or an optics/materials venue.
- The author needs TAP's measurement-validation bar and desk-reject heuristics.

## Scope & topic fit

- Antenna design and analysis: arrays, wideband/multiband, electrically small,
  reconfigurable, mm-wave/THz, on-chip and integrated antennas, with a new principle
  or performance advance.
- Electromagnetic theory and methods: analytical formulations, Green's functions,
  and computational EM (MoM, FEM, FDTD, FMM) when the contribution is the method or insight.
- Scattering, diffraction, and inverse scattering; radar cross-section; rough-surface
  and random-media interaction.
- Metamaterials, metasurfaces, frequency-selective surfaces, and engineered EM
  media when the advance is an electromagnetic functionality (not just a material).
- Wave propagation and channel modeling grounded in electromagnetics: terrestrial,
  indoor, ionospheric, and near-field propagation phenomena.
- Antenna measurement techniques, near-field/far-field transformation, and
  characterization methodology.

## Method & evidence bar

- The standard evidence chain is **theory/formulation → full-wave simulation →
  measurement**; most antenna papers require a fabricated prototype with measured
  results, not simulation alone.
- Report simulation setup fully: solver, mesh/convergence, boundary conditions, and
  excitation — and reconcile measured vs. simulated results, explaining discrepancies.
- Measurements must include the relevant antenna metrics under stated conditions:
  S-parameters, realized gain/efficiency, radiation patterns (co/cross-pol), bandwidth.
- For theory/computational-EM papers, validate against canonical analytical solutions
  or reference results and quantify accuracy and cost.
- Benchmark against the closest prior antenna/EM designs on the metrics that matter
  (size, bandwidth, gain, efficiency, polarization), not a strawman.
- The electromagnetic mechanism (resonance, mode, surface-wave, coupling) must be
  explained, not just reported as a working geometry.

## Structure & house style

- IEEE double-column format; TAP publishes full **Papers** and shorter
  **Communications** — match the article type to the contribution and re-check
  current definitions and length policy on the live guide.
- The introduction motivates the EM/antenna gap and states the contribution; avoid
  framing the paper around a communications-system application the antenna merely serves.
- Figures are load-bearing: geometry with dimensions, simulated/measured S-parameters,
  radiation patterns, current/field distributions illustrating the mechanism.
- Include a fabrication photo and the measurement configuration for prototype papers.
- Keep system/link-level material proportionate; the paper stands on its EM contribution.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and
  `../../resources/official-source-map.md`; start from the IEEE Author Center
  anchors, then cite the current TAP-specific page you checked.
- Search the live site for "IEEE Transactions on Antennas and Propagation information
  for authors" and follow the current ScholarOne/IEEE version.
- Re-check article types (Paper vs. Communication), page/length limits and overlength
  policy, and the IEEE double-column template.
- Confirm expectations on measurement data, simulation reproducibility, and any
  supplementary material.
- Re-check ORCID, competing-interests, funding, author-contribution, and AI-use
  disclosure requirements, and IEEE open-access options.
- If the live official instructions conflict with this skill, the official
  instructions win.

## Pre-submission self-check

- [ ] The headline contribution is an antenna/electromagnetics advance, not a circuit, system, or algorithm.
- [ ] The evidence chain is complete: theory/formulation, full-wave simulation, and (for antennas) measured prototype.
- [ ] Measured and simulated results are reconciled, with discrepancies explained.
- [ ] The EM mechanism (mode/resonance/coupling) is explained, not just a working geometry shown.
- [ ] Performance is benchmarked against the closest prior designs on the right metrics.
- [ ] Article type (Paper vs. Communication) and length fit current TAP limits.

## Common desk-reject triggers

- Antenna design with simulation only and no measurement, with no justifying reason.
- A circuit, RF front-end, or communications-system paper where the antenna/EM contribution is incidental.
- Incremental geometry variation with marginal, unbenchmarked improvement and no new EM insight.
- Computational-EM paper with no validation against canonical or reference solutions.
- Scope mismatch: a pure photonics/optics, pure materials, or pure signal-processing paper labeled "EM."

## Re-routing decision

- Communications-system or link-level contribution as the core → an IEEE communications venue.
- Microwave circuits, filters, or active RF front-ends as the core → `ieee-transactions-on-microwave-theory-and-techniques`.
- Optical/photonic metasurface or device physics as the core → `optica`.
- Signal processing (beamforming, DOA, array processing) as the core → `ieee-transactions-on-signal-processing`.
- Materials-science advance of the metamaterial itself → a materials venue.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] IEEE Transactions on Antennas and Propagation
[Topic tags] <2–3 closest antenna/EM subtopics>
[EM contribution] <the antenna/electromagnetics advance in one line>
[Method/evidence] <does theory + simulation + measurement clear TAP's validation bar?>
[Top risk] <the single most likely reason for rejection>
[Article type] Paper / Communication
[Official items to re-check] <article type / length / template / measurement-data / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
