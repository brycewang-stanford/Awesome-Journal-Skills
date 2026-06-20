---
name: international-journal-of-plasticity
description: Use when targeting the International Journal of Plasticity (IJP) or deciding whether a plastic-deformation modeling manuscript fits this venue. Encodes the journal's fit, the constitutive-model-plus-experimental-validation bar, the plasticity-centric scope, the IJP-vs-JMPS routing, official-submission re-check, and desk-reject heuristics.
---

# International Journal of Plasticity (international-journal-of-plasticity)

## Journal positioning

The International Journal of Plasticity (IJP) is a leading archival journal focused
specifically on the **theory and modeling of plastic deformation** of solids:
rate-dependent and rate-independent constitutive models, crystal plasticity,
finite-deformation plasticity, and the coupling of plasticity with damage, fracture,
and phase transformation. Unlike a broad solid-mechanics journal, IJP is
plasticity-centric — its center of gravity is a new or improved constitutive
description of inelastic behavior, formulated rigorously and validated against
experiment. Papers that report a deformation observation with no constitutive
contribution, or that apply an off-the-shelf plasticity model to one part with no
modeling advance, are a weak fit. This skill is a **fit / venue-selection /
re-framing** tool. It does not replace the journal's current official author
guidelines. Before submitting, re-check the live IJP Guide for Authors.

## When to trigger

- The author names IJP for a plasticity, crystal-plasticity, or inelastic-behavior
  manuscript and wants a fit/framing check.
- A paper must be re-framed from "we observed plastic deformation" into a
  constitutive-model contribution validated against data.
- The author is choosing between IJP (plasticity-centric, constitutive focus) and a
  broader fundamental-mechanics venue (`journal-of-the-mechanics-and-physics-of-solids`).
- The author needs IJP's constitutive-model rigor bar and desk-reject heuristics.

## Scope & topic fit

- Phenomenological constitutive models of plasticity/viscoplasticity:
  rate-dependent and rate-independent flow rules, hardening laws, yield-surface
  evolution, anisotropy.
- Crystal plasticity: single-crystal and polycrystal models, slip/twinning kinematics,
  texture evolution, and grain-scale-to-macroscale linking.
- Finite-deformation and large-strain plasticity: kinematic decompositions,
  objective formulations, and their numerical implementation.
- Coupled plasticity: plasticity coupled with damage, ductile fracture,
  phase transformation, recrystallization, or thermomechanical effects.
- Gradient, size-dependent, and dislocation-based plasticity capturing length-scale
  effects with a constitutive contribution.
- Plasticity of advanced materials (high-entropy alloys, TWIP/TRIP steels, polymers,
  metallic glasses) when the advance is the constitutive model, not just the material.

## Method & evidence bar

- The central object is a **constitutive model** of inelastic behavior — clearly
  formulated, thermodynamically and kinematically consistent, and physically motivated.
- Models must be **validated against experimental data** across more than one loading
  path or condition; fitting a single curve is not validation.
- Calibration and identification of parameters must be transparent: state the data,
  the procedure, and the predictive (not merely fitted) evidence.
- Numerical implementation, when central, must be verified (e.g., convergence,
  objectivity, consistency of the tangent) and clearly described.
- Position against the closest existing plasticity models: what behavior, coupling,
  or class of materials does the new model capture that prior ones do not.
- Reproducibility: report model equations, parameter values, loading protocols, and
  material/microstructure details sufficient to reproduce the predictions.

## Structure & house style

- Standard full-length research-article structure; IJP publishes archival modeling
  papers — re-check article types on the live guide.
- The introduction motivates the constitutive gap (what inelastic behavior is not
  captured); the body develops the model, its identification, and its validation.
- Equations are central and must be self-consistent; use standard finite-deformation
  plasticity notation and define all internal variables.
- Figures carry the validation: model-vs-experiment overlays across loading paths,
  yield-surface/texture evolution, and parameter-sensitivity plots.
- Implementation details, derivations, and extended calibration go to
  appendices/supplementary material; the main text must establish the model and its
  predictive validity unaided.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and
  `../../resources/official-source-map.md`; start from the Elsevier anchors, then
  cite the current IJP Guide for Authors page you checked.
- Search the live site for "International Journal of Plasticity guide for authors" and
  follow the current Elsevier/Editorial Manager version.
- Re-check article types, length/figure expectations, and the data- and
  code-availability policy (model parameters, implementation, raw test data).
- Confirm equation/notation formatting and any highlights or graphical-abstract
  requirement.
- Re-check competing-interests, funding, author-contribution (CRediT), and AI-use
  disclosure requirements.
- If the live official instructions conflict with this skill, the official
  instructions win.

## Pre-submission self-check

- [ ] The contribution is a constitutive model of inelastic behavior, not a deformation observation or an off-the-shelf application.
- [ ] The formulation is thermodynamically and kinematically consistent with explicit internal variables.
- [ ] The model is validated against experiment across multiple loading paths/conditions, not a single fitted curve.
- [ ] Parameter identification is transparent and the predictive (not just fitted) evidence is shown.
- [ ] Novelty is pinned to specific prior plasticity models (new coupling / behavior / material class).
- [ ] The article type and length fit IJP's archival modeling format.

## Common desk-reject triggers

- Applying an existing plasticity model to one component with no constitutive advance.
- A new model fitted to a single test curve and presented as validated.
- Experiment-only deformation study with no constitutive modeling contribution.
- Constitutive equations proposed without thermodynamic/kinematic consistency or numerical verification.
- Scope mismatch: a broad solid-mechanics, materials-processing, or pure structural-FE paper with plasticity only as a label.
- Better framed as fundamental (non-plasticity) mechanics or a materials/microstructure study.

## Re-routing decision

- Broad fundamental solid mechanics (fracture, instabilities, soft matter) → `journal-of-the-mechanics-and-physics-of-solids`.
- Microstructure-first plasticity mechanism (processing–structure–property) → `acta-materialia`.
- Plasticity in composites or composite-structure inelasticity → `composites-part-b-engineering`.
- Forming/machining process mechanics where plasticity is the manufacturing tool → `international-journal-of-machine-tools-and-manufacture`.
- Highest-impact conceptual mechanics-of-materials advance for a broad audience → `nature-materials`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] International Journal of Plasticity
[Topic tags] <2–3 closest plasticity subtopics>
[Constitutive contribution] <the new model / coupling / behavior in one line>
[Method/evidence] <does the model clear IJP's formulation + multi-path validation bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / length / data-code / abstract / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
