---
name: field-crops-research
description: Use when targeting Field Crops Research or deciding whether an agronomy / crop-physiology manuscript fits this venue. Encodes the journal's fit, the field-scale multi-environment and replication bar, data-reporting expectations, house style, official-submission re-check, and desk-reject heuristics.
---

# Field Crops Research (field-crops-research)

## Journal positioning

Field Crops Research, published by Elsevier, is an agronomy and crop-physiology journal
centred on **field-scale crop performance**: yield and its determinants, resource-use
efficiency (water, nitrogen, radiation), cropping systems, crop modeling, and management
across environments. Its defining expectation is **rigorous, adequately replicated field
experimentation that generalizes across environments** — multi-site and/or multi-season
evidence, or modeling validated against field data. A single site-year, unreplicated trial,
or a pot/glasshouse study generalized to the field without field validation is a poor fit.
This skill is a **fit / venue-selection / re-framing** tool. It does not replace the
journal's current author guidelines. Before submitting, re-check the live Field Crops
Research author guidance.

## When to trigger

- The author names Field Crops Research and wants a fit/framing check for a field-agronomy or
  crop-physiology paper.
- A management, genotype, or resource-efficiency result must be framed for generalizability
  across environments rather than as a one-off trial.
- The author is choosing between Field Crops Research, `agronomy-for-sustainable-development`,
  and `agriculture-ecosystems-and-environment`.
- The author needs the venue's desk-reject heuristics around replication and field validity.

## Scope & topic fit

- Crop yield and yield-component determinants under field conditions across genotypes and
  environments.
- Resource-use efficiency: water-, nitrogen-, and radiation-use efficiency and the trade-offs
  among them.
- Cropping systems and management: rotations, intercropping, planting density, sowing date,
  and agronomic interventions evaluated in the field.
- Crop physiology underpinning yield formation: phenology, source–sink relations, canopy and
  root function at field scale.
- Crop simulation modeling calibrated and validated against field data, including
  genotype × environment × management analysis.
- Yield-gap analysis and benchmarking across regions and production systems.

## Method & evidence bar

- The contribution must be **field-relevant and generalizable**: adequately replicated
  experiments across sites and/or seasons, or modeling validated on independent field data.
- Experimental design must be sound: stated design (RCBD, split-plot, etc.), true replication,
  randomization, and appropriate error terms; pseudoreplication is disqualifying.
- Statistics must match the design: mixed models for multi-environment data, correct
  treatment of site/year as random or fixed, and reported variance/uncertainty.
- Yield and efficiency claims need full agronomic context: soil, weather, inputs, and
  management documented so results are interpretable and reproducible.
- Models must report calibration/validation separately, skill metrics against measured data,
  and parameter sources; data and key code/inputs should be available per Elsevier policy.

## Structure & house style

- Standard IMRaD; the introduction must state the agronomic problem and the across-environment
  question, not just describe a local trial.
- Materials and methods must fully document environments (soil, climate), design, replication,
  and management so the study is reproducible.
- Figures/tables should carry the across-environment argument (G×E×M, response curves,
  yield-gap or efficiency comparisons) with variability shown.
- A data-availability statement and complete agronomic metadata are expected; supplementary
  material carries site-by-site detail.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and
  `../../resources/official-source-map.md`; start from the official source anchors, then
  cite the current Field Crops Research page you checked.
- Search the live site for "Field Crops Research guide for authors" and follow the current
  Elsevier version.
- Re-check article types, structure, word/figure expectations, and abstract format.
- Confirm the data-availability/repository policy and reporting of environmental and
  management metadata.
- Re-check competing-interests, funding, author-contribution, and AI-use disclosure, and
  open-access terms.
- If the live official instructions conflict with this skill, the official instructions
  win.

## Pre-submission self-check

- [ ] Evidence spans multiple sites and/or seasons, or modeling is validated on independent field data.
- [ ] The design has true replication and randomization; there is no pseudoreplication.
- [ ] Statistics match the design (e.g., mixed models for multi-environment data) with uncertainty reported.
- [ ] Soil, weather, inputs, and management are fully documented for reproducibility.
- [ ] Models report calibration and validation separately with skill metrics against measured data.
- [ ] Data-availability statement and agronomic metadata are prepared.

## Common desk-reject triggers

- A single site-year, unreplicated trial presented as a general agronomic finding.
- A pot/glasshouse-only study generalized to the field with no field validation.
- Pseudoreplication, or statistics that ignore site/year structure in multi-environment data.
- Yield/efficiency claims with missing soil, weather, or management context.
- A crop model reported without independent validation or skill metrics against field data.

## Re-routing decision

- Explicit sustainability framing, or review/meta-analysis of cropping systems → `agronomy-for-sustainable-development`.
- Environmental fluxes (GHG, nutrient losses), biodiversity, or water quality dominant → `agriculture-ecosystems-and-environment`.
- Soil-process mechanism (SOM, microbial, nutrient cycling) is the core → `soil-biology-and-biochemistry`.
- Broad food-systems significance → `nature-food`.
- Crop physiology/genetics with mechanistic plant-science reach → `new-phytologist` or `the-plant-journal`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Field Crops Research
[Topic tags] <2–3 closest field-agronomy topics>
[Generalizability] <multi-environment evidence or validated model that transfers>
[Method/evidence] <does replication + design + statistics clear Field Crops Research's bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / data policy / metadata reporting / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
