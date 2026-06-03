---
name: agsy-systems-framing-and-modeling
description: Use when framing the system and describing the model for an Agricultural Systems (AgSy) manuscript — defining system boundaries, components, hierarchical levels, and feedbacks, then choosing, describing, and calibrating the model (process/simulation, whole-farm, bio-economic, agent-based, or integrated assessment). This is the distinctive core of an AgSy paper. Structures the model and system; it does not run code for you.
---

# Systems Framing & Modelling (agsy-systems-framing-and-modeling)

This is the **distinctive core** of an Agricultural Systems paper. AgSy expects an explicit **system**
(boundaries, components, hierarchical levels, feedbacks) and a model that is **described, justified, and
calibrated** — not a black box. Frame the system first, then make the model reproducible enough that a
reader could re-implement it.

## When to trigger

- Defining the system boundary, components, and what counts as inside vs. outside
- Choosing a modelling approach and justifying it against alternatives
- Writing the model-description (methods) section
- A reviewer asked "what is the system?", "why this model?", or "how was it calibrated?"

## Step 1 — Frame the system

1. **Boundary.** State what is inside the system and what is an external driver (climate, prices,
   policy). Justify the boundary by the question.
2. **Components & interactions.** Name the components (crop, soil, water, livestock, labour, economics)
   and the **interactions** that matter — AgSy is about interactions, so make them explicit.
3. **Hierarchical levels.** Field → farm → landscape → region → food system: say which levels you
   model and how processes at one level **aggregate or constrain** another.
4. **Feedbacks & emergence.** Identify feedback loops and any emergent behavior the system can produce.
   A conceptual diagram (boxes/arrows) is usually expected.

## Step 2 — Choose and justify the model

- **Match model to question.** Process/simulation (APSIM/DSSAT/STICS/DNDC) for biophysical dynamics;
  **whole-farm** models for resource flows and trade-offs; **bio-economic / mathematical programming**
  for farmer decisions under constraints; **agent-based** for heterogeneity and emergence; **integrated
  assessment** for regional/food-system scenarios. (See `resources/external_tools.md`.)
- **Justify the choice** against the standard alternatives — what does this model represent that others
  cannot, and what does it omit?

## Step 3 — Describe the model so it can be reproduced

- **Version & provenance.** Exact model and version; any modifications you made.
- **Equations / structure.** Key state variables, processes, and (for ABM) the **ODD protocol**.
- **Parameters & inputs.** Sources for parameters and driving data; what is fixed vs. estimated.
- **Calibration.** What was calibrated, against which data, by what procedure — and what was held out
  for evaluation (hand off to `agsy-data-and-model-evaluation`).
- **Assumptions.** State the load-bearing assumptions and their plausible range.

## The "interaction or it isn't AgSy" test

Write one sentence: *"The result arises because component A interacts with component B such that ___;
absent that interaction the system would behave like ___."* If you cannot, you have a single-factor
study, not a systems analysis — reframe (back to `agsy-topic-selection`).

## Anti-patterns

- An undefined system boundary ("the farm" with no components or interactions specified)
- A model used as a black box: no version, equations, parameters, or calibration described
- Calibrating and evaluating on the **same** data (no independent evaluation)
- Choosing a model out of familiarity without justifying it against alternatives
- Hiding assumptions that drive the headline result

## Output format

```
【System boundary】inside vs. external drivers
【Components & interactions】the interactions that matter
【Hierarchical levels】modelled + how they link/aggregate
【Model & version】+ why this model vs. alternatives
【Calibration】what, against which data, what was held out
【Key assumptions】load-bearing ones + plausible range
【Next】agsy-data-and-model-evaluation
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — process, whole-farm, bio-economic, ABM, and integrated-assessment models; ODD protocol
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — AgSy's interaction- and modelling-centered scope
