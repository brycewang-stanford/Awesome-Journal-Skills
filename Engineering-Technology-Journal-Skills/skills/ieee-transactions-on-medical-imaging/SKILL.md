---
name: ieee-transactions-on-medical-imaging
description: Use when targeting IEEE Transactions on Medical Imaging (TMI) or deciding whether a medical-imaging methods manuscript fits this venue. Encodes the journal's fit, the imaging-specific-method-with-proper-validation bar, dataset and evaluation rigor, house style, official-submission re-check, and desk-reject heuristics.
---

# IEEE Transactions on Medical Imaging (ieee-transactions-on-medical-imaging)

## Journal positioning

IEEE Transactions on Medical Imaging (TMI), published jointly by several IEEE
societies, is a flagship archival venue for **methods in medical image formation,
reconstruction, and analysis** across modalities (MRI, CT, PET/SPECT, ultrasound,
optical, and microscopy), including registration, segmentation, quantification,
and machine learning for medical imaging. The defining expectation is a method
whose contribution is **specific to medical imaging** and validated with
appropriate data and proper technical and, where relevant, clinical evaluation —
not a generic computer-vision method run on a medical dataset as an afterthought.
Papers without medical-imaging specificity, or evaluated on tiny/unrepresentative
data without rigorous protocol, are a poor fit. This skill is a **fit /
venue-selection / re-framing** tool. It does not replace the journal's current
official author information. Before submitting, re-check the live IEEE TMI author
guidance and submission system.

## When to trigger

- The author names TMI for an image reconstruction, registration, segmentation, or
  imaging-ML manuscript and wants a fit/framing check.
- A method must be re-framed so the **medical-imaging-specific** contribution — the
  physics, the modality, or the clinical task — is central, not a generic CV result.
- The author is unsure whether the contribution belongs in TMI (imaging methods) or
  a broader biomedical/translation venue.
- The author needs TMI's dataset-and-validation bar and desk-reject heuristics.

## Scope & topic fit

- Image formation and reconstruction: inverse problems and model-based or
  learning-based reconstruction for MRI, CT, PET/SPECT, ultrasound, and optical imaging.
- Image analysis: segmentation, registration, detection, and quantification with a
  medical-imaging-specific methodological advance.
- Machine learning for medical imaging when the method addresses imaging-specific
  challenges (modality physics, limited/heterogeneous labels, domain shift, artifacts).
- Quantitative imaging, biomarker extraction, and motion/artifact correction tied to
  a defined imaging or clinical task.
- Imaging-system and acquisition methods (sampling, hardware-aware reconstruction)
  evaluated on realistic or measured data.
- Computational/physics models of image formation validated against acquired data.

## Method & evidence bar

- The contribution must be **imaging-specific**: exploit modality physics, acquisition
  model, or clinical task; a generic network applied to images does not clear the bar.
- Validation must use appropriate datasets with adequate size and diversity; report
  data source, acquisition, ground-truth/reference standard, and any patient/ethics provenance.
- Evaluation must use task-appropriate metrics with statistics: reconstruction
  fidelity, segmentation overlap/boundary error, registration accuracy, detection
  performance — with confidence intervals or significance where claimed.
- Compare against the right baselines (established imaging methods, not only one CV
  model), with matched preprocessing and fair tuning; ablate key components.
- Address generalization and robustness: cross-site/scanner/protocol variation,
  out-of-distribution behavior, and failure modes relevant to clinical use.
- Reproducibility: enough detail (and ideally code and data access per policy) to
  reproduce the reported results.

## Structure & house style

- IEEE double-column format; TMI publishes full-length **Papers** — match the
  contribution to that archival scope and re-check current article types and length
  policy on the live guide.
- The introduction motivates the imaging/clinical gap and the methodological need,
  then states the contribution; avoid framing it as a generic-CV improvement.
- Figures are load-bearing: example images with the relevant overlays, quantitative
  comparison plots, and failure cases; include clinically meaningful visualizations.
- The methods section must specify the imaging model, data, and evaluation protocol
  precisely enough to reproduce.
- A results section with quantitative tables across datasets and baselines is central.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and
  `../../resources/official-source-map.md`; start from the IEEE Author Center
  anchors, then cite the current TMI-specific page you checked.
- Search the live site for "IEEE Transactions on Medical Imaging information for
  authors" and follow the current ScholarOne/IEEE version.
- Re-check article types, page/length limits and overlength policy, and the IEEE
  double-column template.
- Confirm data/code-availability, human-subjects/ethics/IRB, and any de-identification
  and reporting requirements.
- Re-check ORCID, competing-interests, funding, author-contribution, and AI-use
  disclosure requirements, and IEEE open-access options.
- If the live official instructions conflict with this skill, the official
  instructions win.

## Pre-submission self-check

- [ ] The contribution is medical-imaging-specific (physics/modality/clinical task), not a generic CV method on medical data.
- [ ] Validation uses appropriate, adequately sized and diverse datasets with documented reference standards.
- [ ] Metrics are task-appropriate and reported with statistics; baselines are the right imaging methods.
- [ ] Generalization across site/scanner/protocol and failure modes are addressed.
- [ ] Ethics/IRB and data provenance/de-identification are documented.
- [ ] Article type and length fit current TMI limits; methods are reproducible.

## Common desk-reject triggers

- A generic computer-vision/deep-learning method with no medical-imaging-specific contribution.
- Evaluation on a tiny, single-site, or unrepresentative dataset with no rigorous protocol.
- Missing or inappropriate baselines; unfair comparisons or no ablation of the claimed novelty.
- No ethics/IRB statement or data provenance for human-subject imaging data.
- Clinical-utility claims with no clinically meaningful validation or appropriate reference standard.

## Re-routing decision

- Broader biomedical engineering (devices, biosignals, non-imaging) → `ieee-transactions-on-biomedical-engineering`.
- Highest-significance clinical translation/impact story → `nature-biomedical-engineering`.
- Core contribution is a general signal-processing method → `ieee-transactions-on-signal-processing`.
- Surgical/medical-robotics contribution as the core → `ieee-transactions-on-robotics`.
- General computer-vision advance with no medical specificity → a computer-vision venue.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] IEEE Transactions on Medical Imaging
[Topic tags] <2–3 closest medical-imaging subtopics>
[Imaging-specific contribution] <what makes the method imaging-specific in one line>
[Method/evidence] <do the dataset + metrics + baselines clear TMI's validation bar?>
[Top risk] <the single most likely reason for rejection>
[Article type] Paper
[Official items to re-check] <article type / length / template / data-ethics / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
