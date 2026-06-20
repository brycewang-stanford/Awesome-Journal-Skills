---
name: journal-of-fluid-mechanics
description: Use when targeting the Journal of Fluid Mechanics (JFM) or deciding whether a fundamental fluid-mechanics manuscript fits this venue. Encodes the journal's fit, the physical-understanding bar across analysis/computation/experiment, the insight-not-application scope, official-submission re-check, and desk-reject heuristics.
---

# Journal of Fluid Mechanics (journal-of-fluid-mechanics)

## Journal positioning

The Journal of Fluid Mechanics (JFM), published by Cambridge University Press, is a
leading archival journal for **fundamental fluid mechanics**. It publishes
analytical, computational, and experimental studies whose purpose is physical
understanding of fluid phenomena — turbulence, hydrodynamic instabilities, multiphase
and interfacial flows, geophysical and biological flows, and the dynamics that
govern them. The defining expectation is **new insight into the mechanics of a
flow**, not a demonstration that a method or device works. Applied CFD of a specific
piece of equipment, or a parametric simulation with no extracted physics, is a poor
fit. JFM values clean problem formulation, careful evidence, and an interpretation
that advances how the community understands the flow. This skill is a **fit /
venue-selection / re-framing** tool. It does not replace the journal's current
official author instructions. Before submitting, re-check the live JFM author
information.

## When to trigger

- The author names JFM for a fluid-mechanics manuscript and wants a fit/framing check.
- A flow study must be re-framed from "we simulated/measured this device" into a
  contribution to the physical understanding of a fluid phenomenon.
- The author is choosing between JFM and an applied-CFD, engineering-application, or
  physics-family venue.
- The author needs JFM's physical-insight bar and desk-reject heuristics.

## Scope & topic fit

- Turbulence: transition, coherent structures, wall-bounded and free-shear flows,
  turbulence modeling when it yields mechanistic understanding.
- Hydrodynamic stability and instabilities: linear/nonlinear analysis, bifurcation,
  and the route to complex flow states.
- Multiphase, interfacial, and free-surface flows: drops, bubbles, films, capillarity,
  and phase-change-coupled dynamics with a mechanics contribution.
- Geophysical and environmental fluid dynamics: stratified, rotating, convective, and
  buoyancy-driven flows.
- Biological and low-Reynolds-number flows: swimming, flow in/around organisms,
  microfluidic and suspension mechanics with fundamental insight.
- Compressible flows, waves, and vortex dynamics when the advance is physical
  understanding rather than a specific configuration.

## Method & evidence bar

- The central claim is **new physical understanding** of a flow — a mechanism, scaling
  law, instability, or governing balance — supported by analysis, well-resolved
  computation, or controlled experiment.
- Computation must be verified and adequately resolved, with the physics extracted;
  an under-resolved or unvalidated CFD run of one geometry is not evidence.
- Experiments must report flow conditions, diagnostics, and uncertainty, and isolate
  the phenomenon of interest with appropriate controls.
- Analysis must be mathematically careful: clear governing equations, justified
  approximations (scaling, asymptotics), and self-consistent derivations.
- Position against the closest fluid-mechanics results: what new regime, mechanism,
  or scaling does the work establish relative to prior understanding.
- Reproducibility: report governing equations, boundary/initial conditions, numerical
  schemes or experimental setups in enough detail to reconstruct the study.

## Structure & house style

- Standard full-length research-article structure; JFM also publishes shorter
  **Rapids** for concise high-impact results — match scope to article type and
  re-check current definitions on the live guide.
- The introduction frames the fluid-mechanics question and the gap in understanding,
  not an engineering application.
- Equations and notation follow standard fluid-mechanics conventions and must be
  internally consistent; nondimensionalization and key parameters (Reynolds, etc.)
  stated clearly.
- Figures are load-bearing: flow visualizations with quantification, spectra, scaling
  collapses, and theory-vs-data/computation comparisons.
- Supplementary material and movies carry extended data; the main text must establish
  the central physical insight on its own.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and
  `../../resources/official-source-map.md`; start from the Cambridge University Press
  anchors, then cite the current JFM author-information page you checked.
- Search the live site for "Journal of Fluid Mechanics information for authors" and
  follow the current Cambridge/submission-system version.
- Re-check article types (full article vs. Rapids), length/figure expectations, and
  the JFM style/template conventions.
- Confirm data-availability, supplementary-movie, and reproducibility expectations for
  computational and experimental work.
- Re-check competing-interests, funding, author-contribution, and AI-use disclosure
  requirements, and any open-access options.
- If the live official instructions conflict with this skill, the official
  instructions win.

## Pre-submission self-check

- [ ] The contribution is new physical understanding of a flow (mechanism / scaling / instability), not a device demonstration.
- [ ] Computations are verified and resolved, and the physics is extracted — not a single unvalidated CFD run.
- [ ] Experiments report conditions, diagnostics, and uncertainty, and isolate the phenomenon.
- [ ] Analysis has clear governing equations and justified approximations, with key dimensionless parameters stated.
- [ ] Novelty is pinned to specific prior fluid-mechanics results (new regime / mechanism / scaling).
- [ ] The article type (full vs. Rapids) and length fit JFM's format.

## Common desk-reject triggers

- Applied CFD of a specific device or geometry with no fluid-mechanics insight extracted.
- Under-resolved or unvalidated simulations presented as physical evidence.
- Parametric study reporting numbers with no mechanism, scaling, or governing balance.
- Experiment-only flow report with no quantification, uncertainty, or mechanics interpretation.
- Scope mismatch: a heat-transfer-equipment, chemical-process, or numerical-methods paper with fluid mechanics as a label.
- Better framed as an engineering-application or computational-methods contribution.

## Re-routing decision

- Broad-audience high-impact fluid-physics discovery → `nature-physics` (conceptual-advance bar) or `science-advances`.
- Solid-mechanics rather than fluid mechanics → `journal-of-the-mechanics-and-physics-of-solids`.
- Manufacturing/process flow where the device is the point → `international-journal-of-machine-tools-and-manufacture`.
- Aerospace-flow review/survey rather than primary research → `progress-in-aerospace-sciences`.
- Applied-CFD methods or engineering-configuration focus → a computational-fluids or applications venue.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Journal of Fluid Mechanics
[Topic tags] <2–3 closest fluid-mechanics subtopics>
[Insight] <the new physical understanding of the flow in one line>
[Method/evidence] <does the analysis/computation/experiment clear JFM's physical-insight bar?>
[Top risk] <the single most likely reason for rejection>
[Article type] full article / Rapids
[Official items to re-check] <article type / length / data-movie / template / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
