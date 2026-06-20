---
name: journal-of-the-mechanics-and-physics-of-solids
description: Use when targeting the Journal of the Mechanics and Physics of Solids (JMPS) or deciding whether a fundamental solid-mechanics manuscript fits this venue. Encodes the journal's fit, the physical-insight-plus-mathematical-rigor bar, breadth across solid mechanics, the JMPS-vs-plasticity-journal routing, official-submission re-check, and desk-reject heuristics.
---

# Journal of the Mechanics and Physics of Solids (journal-of-the-mechanics-and-physics-of-solids)

## Journal positioning

The Journal of the Mechanics and Physics of Solids (JMPS) is a leading archival
journal for **fundamental solid mechanics**: constitutive theory, fracture and
damage, micromechanics, instabilities and bifurcation, and the mechanics of soft
and active materials. Its defining expectation is a genuine advance in physical
understanding of how solids deform, fail, or respond — delivered with mathematical
rigor and, where relevant, decisive experimental or computational evidence. JMPS
rewards papers that uncover a mechanism or a governing principle, not papers that
run a finite-element case study of one geometry and report numbers. Breadth is
intentional: plasticity is one of many topics here, alongside elasticity, waves,
contact, and continuum-to-microstructure bridging. This skill is a **fit /
venue-selection / re-framing** tool. It does not replace the journal's current
official author guidelines. Before submitting, re-check the live JMPS Guide for
Authors.

## When to trigger

- The author names JMPS for a solid-mechanics manuscript and wants a fit/framing check.
- A mechanics paper must be re-framed from "we simulated this structure" into a
  general mechanism, model, or principle of solid behavior.
- The author is deciding between JMPS (broad fundamental solid mechanics) and a
  plasticity-centric venue (`international-journal-of-plasticity`).
- The author needs JMPS's insight-plus-rigor bar and desk-reject heuristics.

## Scope & topic fit

- Constitutive theory and continuum mechanics: finite-deformation kinematics,
  thermodynamically consistent material models, nonlinear elasticity.
- Fracture, damage, and failure: crack-tip fields, cohesive/phase-field fracture,
  fatigue mechanics, and toughening principles with a governing-law contribution.
- Micromechanics and homogenization: linking microstructure to effective response,
  defect mechanics, dislocation and interface mechanics.
- Instabilities, bifurcation, and pattern formation: buckling, wrinkling,
  localization, and post-instability response in structured or soft solids.
- Mechanics of soft, active, and architected materials: gels, elastomers,
  growth/morphogenesis, mechanical metamaterials, coupled multiphysics response.
- Waves, contact, and adhesion when the contribution is a mechanism or analytical
  result, not a parametric simulation sweep.

## Method & evidence bar

- The central object is a **mechanism or governing principle** of solid behavior,
  derived with mathematical care — not a number produced by a black-box solver.
- Analysis must be rigorous: clearly stated kinematics and constitutive assumptions,
  correct field equations, and derivations that a specialist can verify.
- Computation, when central, must be a means to physical insight (mechanism, scaling,
  bifurcation structure) — a converged FE simulation of one part is not a result.
- Experiments, when present, should isolate the mechanism and be quantitatively
  compared to theory, with controlled conditions and reported uncertainty.
- Position the contribution against the closest mechanics results: what new physics,
  weaker assumptions, or broader class of behavior does it establish.
- Reproducibility: state the model, boundary/initial conditions, and any numerical
  scheme in enough detail that the analysis can be reconstructed.

## Structure & house style

- Standard full-length research-article structure; JMPS publishes archival papers,
  not rapid letters — route urgent short results elsewhere and re-check article
  types on the live guide.
- The introduction motivates the mechanics gap (what is not understood), not an
  application; the body develops theory, then evidence, then physical interpretation.
- Equations are load-bearing and must be self-consistent; notation should follow
  standard continuum-mechanics conventions and be defined on first use.
- Figures support the argument: field maps, bifurcation/phase diagrams, theory-vs-data
  overlays, and mechanism schematics — not decorative renderings.
- Lengthy derivations and supporting computations go to appendices/supplementary
  material; the main text must carry the central insight unaided.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and
  `../../resources/official-source-map.md`; start from the Elsevier anchors, then
  cite the current JMPS Guide for Authors page you checked.
- Search the live site for "Journal of the Mechanics and Physics of Solids guide for
  authors" and follow the current Elsevier/Editorial Manager version.
- Re-check article types, length/figure expectations, and the data- and
  code-availability policy for computational work.
- Confirm formatting of equations, notation, and any structured-abstract or highlights
  requirement.
- Re-check competing-interests, funding, author-contribution (CRediT), and AI-use
  disclosure requirements.
- If the live official instructions conflict with this skill, the official
  instructions win.

## Pre-submission self-check

- [ ] The contribution is a mechanism or governing principle of solid behavior, not a one-off finite-element case study.
- [ ] Kinematics, constitutive assumptions, and field equations are stated explicitly and are internally consistent.
- [ ] Any computation serves physical insight (scaling, bifurcation, mechanism), not just a converged number.
- [ ] Experiments, if used, isolate the mechanism and are compared quantitatively to theory.
- [ ] Novelty is pinned to specific prior mechanics results (new physics / weaker assumptions / broader class).
- [ ] The article type and length fit JMPS's archival full-paper format.

## Common desk-reject triggers

- Applied finite-element case study of one component or geometry with no fundamental advance.
- Parametric simulation sweep reported as a result, with no mechanism or governing law extracted.
- Constitutive model proposed with no derivation, thermodynamic consistency, or validation.
- Experiment-only report of a deformation/failure observation without mechanics interpretation.
- Scope mismatch: a materials-processing, structural-design, or pure-numerical-methods paper with mechanics as a label.
- Better framed as a plasticity-specific constitutive study or a materials/structures application.

## Re-routing decision

- Plastic deformation / constitutive-model-centric contribution → `international-journal-of-plasticity`.
- Microstructure-first mechanism (processing–structure–property) → `acta-materialia`.
- Composite-material mechanics or structural composites → `composites-part-b-engineering`.
- AM-process-driven mechanics with materials focus → `additive-manufacturing`.
- Highest-impact conceptual mechanics-of-materials advance for a broad audience → `nature-materials`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Journal of the Mechanics and Physics of Solids
[Topic tags] <2–3 closest solid-mechanics subtopics>
[Mechanism/principle] <the governing insight in one line>
[Method/evidence] <does the analysis clear JMPS's insight + rigor bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / length / data-code / abstract / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
