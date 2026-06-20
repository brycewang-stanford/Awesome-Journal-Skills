---
name: nature-biomedical-engineering
description: Use when targeting Nature Biomedical Engineering or deciding whether a biomedical-engineering / health-technology manuscript fits this venue. Encodes the journal's fit, the Nature-style biomedical-significance and translational bar, validation and evidence rigor, house style, the device-vs-biomaterials-vs-clinical routing, official-submission re-check, and desk-reject heuristics.
---

# Nature Biomedical Engineering (nature-biomedical-engineering)

## Journal positioning

Nature Biomedical Engineering is the Nature Portfolio journal for engineering at the
interface with biology and medicine: devices, diagnostics, therapeutics, biomaterials,
and engineered systems whose advance carries **significance for medicine or biology and
plausible translational relevance**. It selects, in the Nature style, for work that
solves a real biomedical problem with rigorous, biologically or clinically meaningful
validation — not a clever engineering demonstration with no health significance. The
defining demand is that the engineering be motivated by, and validated against, a
genuine medical or biological need; a proof-of-concept device with only benchtop data
and no biological/clinical evidence is a poor fit. This skill is a **fit /
venue-selection / re-framing** tool. It does not replace the journal's current
official author guidelines. Before submitting, re-check the live Nature Biomedical
Engineering submission guidelines on the Nature Portfolio site.

## When to trigger

- The author names Nature Biomedical Engineering for a device, diagnostic, therapeutic,
  or biomaterial result and wants a fit/framing and significance check.
- An engineering result must be re-framed from a benchtop demonstration into a
  biomedical-significance and translational narrative with biological validation.
- The author is choosing between Nature Biomedical Engineering and `biomaterials`,
  `nature-electronics`, `ieee-transactions-on-biomedical-engineering`, or
  `nature-communications`.
- The author needs the journal's validation bar and its desk-reject heuristics.

## Scope & topic fit

- Medical devices and engineered systems: implantable, wearable, and point-of-care
  technologies validated against a clinical or biological endpoint.
- Diagnostics and biosensing: assays, imaging, and sensor platforms with demonstrated
  sensitivity/specificity on biologically or clinically relevant samples.
- Therapeutics and delivery: engineered drug/gene/cell-delivery systems and
  device-enabled therapies with mechanism and efficacy evidence in relevant models.
- Biomaterials and tissue engineering when the advance is engineering-driven and tied
  to a biomedical function and validation, not just material characterization.
- Bioelectronics, neural interfaces, and organ-on-chip / engineered tissue systems with
  measured biological performance.
- Computational and AI methods for biomedicine when validated on clinically or
  biologically meaningful data with appropriate endpoints.

## Method & evidence bar

- The contribution must carry an explicit **biomedical-significance argument**: the
  unmet need, the engineered solution, and why it matters for medicine or biology.
- Validation must match the claim's level: cell/tissue, animal-model, or human/clinical
  evidence with appropriate controls, endpoints, and statistics — benchtop performance
  alone is insufficient for a biomedical claim.
- Performance must be benchmarked against the relevant clinical or technological state
  of the art and reported under stated, comparable conditions.
- Biological and animal studies require proper experimental design (randomization,
  blinding where applicable, adequate N, ethics approval) and honest reporting of
  limitations.
- Translational claims must be calibrated to the evidence: clearly distinguish
  proof-of-concept from validated performance, and state remaining barriers.
- Reproducibility and reporting follow Nature-Portfolio expectations, including the
  reporting summary and relevant reporting guidelines for biomedical studies.

## Structure & house style

- Nature-Portfolio article structure with a significance-forward abstract and
  introduction; re-check current article types and length/format on the live guide.
- The introduction frames the clinical/biological problem and the engineering rationale
  before technical development, in accessible language.
- Main display items are curated and load-bearing: device/assay performance with
  statistics, in-vitro/in-vivo results with controls, and clear schematics of the
  system and its intended use.
- Methods and extended/supplementary material carry full fabrication, assay, model, and
  statistical detail; the main narrative must stand on the headline figures.
- Ethics, biosafety, and trial-registration statements must be present where applicable.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and
  `../../resources/official-source-map.md`; start from the Nature-Portfolio anchors,
  then cite the current Nature Biomedical Engineering guidelines page you checked.
- Search the live site for "Nature Biomedical Engineering submission guidelines" and
  follow the current Nature-Portfolio submission system.
- Re-check article types, length/format expectations, and the abstract requirements.
- Confirm ethics approval, animal-use (e.g., ARRIVE), clinical-trial registration, and
  relevant reporting-guideline requirements for biomedical studies.
- Confirm data-availability, code-availability, and reporting-summary requirements of
  Nature Portfolio.
- Re-check open-access options, ORCID, competing-interests, funding,
  author-contribution, and AI-use disclosure requirements.
- If the live official instructions conflict with this skill, the official instructions
  win.

## Pre-submission self-check

- [ ] The abstract/introduction states the unmet biomedical need and the translational significance in Nature style.
- [ ] Validation matches the claim level (cell / animal / human) with proper controls, endpoints, and statistics.
- [ ] Performance is benchmarked against the relevant clinical or technological state of the art.
- [ ] Animal/clinical studies report design (N, randomization/blinding), ethics approval, and limitations honestly.
- [ ] Translational claims are calibrated to the evidence, distinguishing proof-of-concept from validated performance.
- [ ] Data/code availability, reporting summary, and biomedical reporting guidelines are satisfied.

## Common desk-reject triggers

- An engineering demonstration with no biomedical significance or no biological/clinical validation.
- Benchtop-only performance presented as a biomedical claim without in-vitro/in-vivo evidence.
- Overstated translational claims unsupported by the level of validation provided.
- Animal or clinical data with inadequate design, missing controls, or absent ethics approval.
- Performance not benchmarked against the relevant clinical or technological standard of care.
- A materials or device paper better suited to a materials or specialty engineering venue.

## Re-routing decision

- Biomaterials advance centered on material design with biological evaluation → `biomaterials`.
- Bioelectronic/device physics advance without strong biomedical validation → `nature-electronics`.
- Specialty biomedical-engineering methods/instrumentation result → `ieee-transactions-on-biomedical-engineering`.
- Broad cross-disciplinary significance beyond biomedicine → `nature-communications` / `science-advances`.
- Mechanistic biology or therapeutic biology as the core → a dedicated biomedical/biology Nature-Portfolio venue.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Nature Biomedical Engineering
[Topic tags] <2–3 closest biomedical-engineering subtopics>
[Significance statement] <the unmet need + translational claim in one line>
[Validation level] benchtop / in-vitro / in-vivo / human-clinical
[Method/evidence] <does validation + benchmarking clear the biomedical significance + rigor bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / ethics & reporting guidelines / data & code / reporting summary / OA / disclosures>
[Re-route suggestion] <if no biomedical validation or better framed elsewhere, a matched venue>
```
