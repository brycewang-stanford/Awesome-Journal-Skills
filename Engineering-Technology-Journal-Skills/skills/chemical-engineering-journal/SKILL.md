---
name: chemical-engineering-journal
description: Use when targeting Chemical Engineering Journal or deciding whether an applied chemical-engineering / functional-materials manuscript fits this venue. Encodes the journal's fit, the applied-advance-with-mechanism bar, performance and benchmarking rigor, house style, the applied-vs-fundamentals routing, official-submission re-check, and desk-reject heuristics.
---

# Chemical Engineering Journal (chemical-engineering-journal)

## Journal positioning

Chemical Engineering Journal (Elsevier) is a broad, high-volume venue for chemical
engineering with a strong **applied and functional-materials emphasis**: reaction
engineering and catalysis for environmental and energy applications, adsorption and
separation, functional materials engineered for chemical-engineering processes, and
water/energy treatment and conversion. Where AIChE Journal rewards the transferable
principle, this journal rewards a demonstrated, well-characterized advance on a real
process problem — provided the work still explains *why* it works, not only *that* it
works. Papers that report a new material and a property number with no mechanistic or
process insight, or that lack credible benchmarking, are a weak fit. This skill is a
**fit / venue-selection / re-framing** tool. It does not replace the journal's current
official author guidelines. Before submitting, re-check the live Chemical Engineering
Journal Guide for Authors on the Elsevier site.

## When to trigger

- The author names Chemical Engineering Journal for an applied catalysis, adsorption,
  separation, functional-materials, or water/energy-process manuscript.
- A paper must be re-framed from "we synthesized a material" into an
  application-with-mechanism story tied to a chemical-engineering process.
- The author is choosing between this journal's applied slant and AIChE Journal's
  fundamentals bar, or between it and a pure-materials venue.
- The author needs the journal's performance-and-benchmarking rigor bar and
  desk-reject heuristics.

## Scope & topic fit

- Catalysis and reaction engineering for environmental and energy uses: pollutant
  degradation, CO2 conversion, photo/electro/thermal catalysis with process relevance.
- Adsorption and separation: sorbents, ion exchange, and separation processes with
  capacity, kinetics, selectivity, and regeneration data.
- Functional materials engineered for a chemical-engineering function (membranes,
  catalysts, sorbents, electrodes) where the process performance is central.
- Water and wastewater treatment: advanced oxidation, membrane and hybrid processes,
  resource recovery, with mechanism and performance under realistic conditions.
- Energy-related processes: conversion, storage materials in a process context, and
  energy-efficient separations where the chemical-engineering advance is clear.
- Process and reactor engineering for the above, including intensification and scale
  considerations.

## Method & evidence bar

- The central claim is a **demonstrated applied advance with mechanism**: a material or
  process that performs better, with direct evidence for *why* (active site,
  transport, structure–performance link), not a property table alone.
- Performance must be quantified and benchmarked against credible state-of-the-art and
  measured under realistic, clearly stated conditions (concentration ranges, matrices,
  cycling, stability).
- Mechanism claims need direct evidence (operando/in-situ characterization, kinetic
  analysis, controlled variation), not morphology-property correlation alone.
- Stability, reusability, and applicability under non-idealized conditions are
  expected for any application claim; single-cycle ideal-solution results are weak.
- Characterization must be appropriate and statistically representative; report
  conditions, controls, and reproducibility.

## Structure & house style

- Standard research-article structure (introduction, materials/methods, results,
  discussion); the journal also uses highlights and a graphical abstract — re-check
  current article types and requirements on the live guide.
- The introduction frames the process/application gap and the mechanistic question;
  the discussion ties structure or process variables to the measured performance.
- Figures are load-bearing: performance curves with benchmarks and error bars,
  mechanism schematics, and characterization supporting the active-site/transport claim.
- Supporting information carries full synthesis, extended characterization, and
  stability/recyclability data; main-text figures must stand alone for the central claim.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and
  `../../resources/official-source-map.md`; start from the Elsevier anchors, then cite
  the current Chemical Engineering Journal Guide for Authors page you checked.
- Search the live site for "Chemical Engineering Journal guide for authors" and follow
  the current Elsevier/Editorial Manager version.
- Re-check article types, highlights and graphical-abstract requirements, and
  length/figure expectations.
- Confirm data-availability and any deposition/sharing requirements for datasets.
- Re-check competing-interests, funding, author-contribution (CRediT), and AI-use
  disclosure requirements.
- If the live official instructions conflict with this skill, the official
  instructions win.

## Pre-submission self-check

- [ ] The contribution is an applied advance with direct mechanistic evidence, not a new material plus a property number.
- [ ] Performance is benchmarked against credible state-of-the-art under realistic, clearly stated conditions.
- [ ] Mechanism is supported by operando/in-situ or kinetic evidence, not morphology-property correlation alone.
- [ ] Stability, reusability, and non-idealized-condition performance are reported for application claims.
- [ ] Characterization is appropriate, controlled, and statistically representative.
- [ ] Highlights and graphical abstract represent the actual process advance.

## Common desk-reject triggers

- "New material, better number" with no mechanism and no process relevance.
- Performance claims without credible benchmarking or measured only under idealized lab conditions.
- Adsorption/catalysis studies missing stability, regeneration, or realistic-matrix data.
- Mechanism asserted from morphology alone, with no operando/in-situ or kinetic support.
- Pure-chemistry or pure-materials paper with chemical-engineering process relevance only as a label.
- Incremental variant of a known sorbent/catalyst with marginal improvement and no new insight.

## Re-routing decision

- Fundamental, generalizable transport/thermo/reaction-engineering science → `aiche-journal`.
- Membrane materials and transport mechanism as the core → `journal-of-membrane-science`.
- Systems-level energy conversion / techno-economic scope → `applied-energy`.
- Electrode/electrolyte materials for batteries as the core → `energy-storage-materials`.
- Environmental-process work with environmental-science framing → `environmental-science-and-technology`.
- Catalysis as a chemistry/mechanism advance over process engineering → `nature-catalysis`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Chemical Engineering Journal
[Topic tags] <2–3 closest applied-CE subtopics>
[Applied advance] <the material/process advance and what it improves, one line>
[Mechanism] <the why-it-works evidence in one line>
[Benchmarking] <state-of-the-art comparison + realistic conditions present?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / highlights / graphical abstract / data policy / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
