---
name: acta-materialia
description: Use when targeting Acta Materialia or deciding whether a structural-materials / physical-metallurgy manuscript fits this venue. Encodes the journal's fit, the processing–structure–property–performance mechanism bar, characterization rigor, house style, the Acta-vs-Scripta and Acta-vs-functional-materials routing, official-submission re-check, and desk-reject heuristics.
---

# Acta Materialia (acta-materialia)

## Journal positioning

Acta Materialia is a leading archival journal of materials science and engineering
with a structural-materials and physical-metallurgy center of gravity: the
quantitative relationships among **processing, microstructure, properties, and
performance** in metals, alloys, ceramics, and structural composites. The journal
rewards papers that establish a mechanism — why a microstructure forms and how it
governs a property — over papers that merely report that a new processing route
changed a number. Purely incremental "new alloy, slightly better property" studies
without mechanistic insight are a weak fit. This skill is a **fit / venue-selection
/ re-framing** tool. It does not replace the journal's current official author
guidelines. Before submitting, re-check the live Acta Materialia Guide for Authors.

## When to trigger

- The author names Acta Materialia for a metallurgy, ceramics, or structural-materials
  manuscript and wants a fit/framing check.
- A materials paper must be re-framed from "we made and measured X" into a
  processing–structure–property mechanism story.
- The author is deciding between Acta Materialia, a rapid-communication outlet
  (Scripta Materialia), and the functional-materials family (`advanced-materials`,
  `nature-materials`).
- The author needs Acta's characterization-rigor bar and desk-reject heuristics.

## Scope & topic fit

- Physical metallurgy and alloy design: phase transformations, precipitation,
  recrystallization, texture, and the resulting mechanical behavior.
- Deformation and failure mechanisms: plasticity, creep, fatigue, fracture — when
  tied to microstructural evidence and, ideally, modeling.
- Microstructure evolution under processing (casting, thermomechanical processing,
  additive manufacturing, irradiation) with quantitative structure–property links.
- Ceramics and structural composites where the advance is mechanistic, not just a
  property table.
- Computational materials science (phase-field, CALPHAD, crystal plasticity,
  atomistics) when validated against or predictive of experiment.

## Method & evidence bar

- The central claim is a **mechanism** connecting processing, microstructure, and
  property — supported by quantitative, statistically meaningful characterization,
  not representative micrographs alone.
- Characterization must be appropriate and rigorous: electron microscopy (SEM/TEM/EBSD),
  diffraction (XRD/neutron), and quantitative stereology with reported sampling;
  mechanical data with proper statistics and testing conditions.
- Modeling, when present, must be validated against experimental data or make tested
  predictions; a simulation with no experimental anchor is usually insufficient at
  this venue.
- Property improvements must be explained mechanistically and compared to the right
  baseline material/process, not to a strawman.
- Reproducibility: report composition, processing parameters, and testing protocol in
  enough detail to reproduce the microstructure and the measurement.

## Structure & house style

- Standard research-article structure (introduction, materials/methods, results,
  discussion); Acta Materialia publishes full-length archival articles — route short,
  urgent results elsewhere and re-check current article types on the live guide.
- The introduction motivates the materials-science gap (mechanism, not application
  novelty); the discussion is where the processing–structure–property argument is
  made explicit.
- Figures are load-bearing: micrographs with scale bars and quantitative analysis,
  property plots with error bars, and schematics of the proposed mechanism.
- Supplementary material carries extended characterization and full processing
  details; main-text figures must support the central mechanism on their own.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and
  `../../resources/official-source-map.md`; start from the Elsevier anchors, then cite
  the current Acta Materialia Guide for Authors page you checked.
- Search the live site for "Acta Materialia guide for authors" and follow the current
  Elsevier/Editorial Manager version.
- Re-check article types, length/figure expectations, and the data-availability and
  raw-data (e.g., microscopy/diffraction data) policy.
- Confirm graphical-abstract and highlights requirements if applicable.
- Re-check competing-interests, funding, author-contribution (CRediT), and AI-use
  disclosure requirements.
- If the live official instructions conflict with this skill, the official
  instructions win.

## Pre-submission self-check

- [ ] The contribution is a processing–structure–property mechanism, not just a new material with a better number.
- [ ] Characterization is quantitative and statistically representative (sampling reported), not single cherry-picked images.
- [ ] Property claims are benchmarked against the correct baseline and explained mechanistically.
- [ ] Any model is validated against experiment or makes a tested prediction.
- [ ] Processing, composition, and testing protocols are reported in reproducible detail.
- [ ] The article type and length fit Acta's archival (not rapid-communication) format.

## Common desk-reject triggers

- "New alloy / new process, slightly better property" with no mechanistic explanation.
- Characterization by representative micrographs only, with no quantification or sampling.
- Simulation-only studies with no experimental validation or testable prediction.
- Application-driven device papers where the materials-science mechanism is incidental.
- Better framed as a rapid communication (single incremental result) or as a
  functional-materials/device advance.

## Re-routing decision

- Short, urgent single result → Scripta Materialia (rapid communications).
- Conceptual functional-materials or device advance → `advanced-materials` / `nature-materials`.
- Additive-manufacturing process focus over metallurgy → `additive-manufacturing`.
- Polymer/structural composite emphasis → `composites-part-b-engineering`.
- Plasticity theory/constitutive modeling as the core → `international-journal-of-plasticity` / `journal-of-the-mechanics-and-physics-of-solids`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Acta Materialia
[Topic tags] <2–3 closest materials subtopics>
[Mechanism] <the processing–structure–property claim in one line>
[Method/evidence] <does characterization + modeling clear Acta's mechanism + rigor bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / data policy / graphical abstract / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
