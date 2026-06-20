---
name: radiology
description: Use when targeting Radiology (RSNA) or deciding whether a medical-imaging study fits this venue. Encodes the journal's fit, the diagnostic-accuracy and imaging-methodology bar, STARD/CLAIM reporting and reproducibility expectations, RSNA house style, official-submission re-check, and desk-reject heuristics. Venue-fit aid only, not clinical advice.
---

# Radiology (radiology)

## Journal positioning

Radiology is the flagship journal of the Radiological Society of North America (RSNA),
publishing original research across diagnostic and interventional imaging — imaging
physics and technique, diagnostic accuracy, image-guided intervention, and imaging
artificial intelligence — with a strong emphasis on rigorous design, adequate sample
size, and clinical relevance. The defining expectation is a **methodologically sound
imaging study with a clinically meaningful question and an appropriate reference
standard**, not a small retrospective series or an AI model evaluated on a single
internal dataset. This skill is a **fit / venue-selection / re-framing** aid; it is
not clinical or regulatory advice and does not replace the journal's current
instructions. Before submitting, re-check the live Radiology author instructions.

## When to trigger

- The author names Radiology for a diagnostic-imaging, imaging-physics, interventional,
  or imaging-AI study and wants a fit/framing check.
- An imaging study must be re-framed around a clinically meaningful diagnostic or
  outcome question with a valid reference standard.
- The author is choosing between Radiology, a subspecialty imaging journal, and a
  general clinical journal.
- The author needs the journal's diagnostic-accuracy reporting and reproducibility
  expectations (STARD, CLAIM for AI).

## Scope & topic fit

- Diagnostic-accuracy studies across modalities (CT, MRI, ultrasound, PET, radiography)
  with an appropriate reference standard.
- Imaging physics, acquisition, reconstruction, and quantitative-imaging biomarker
  development and validation.
- Image-guided and interventional procedures with outcome data.
- Artificial intelligence and machine learning for imaging, with rigorous training/
  validation/test design and external validation.
- Prognostic and screening imaging studies with clinically meaningful endpoints.

## Method & evidence bar

- Diagnostic-accuracy studies need an adequate, representative sample, a valid and
  independent reference standard, and reporting per STARD; spectrum and verification
  bias must be addressed.
- Sample size and statistical power must be justified; reader studies require adequate
  readers and inter-/intra-reader agreement analysis.
- AI/ML studies require clearly separated training/validation/test data, external/
  multi-site validation, and reporting per CLAIM; performance must be benchmarked
  against a clinically relevant baseline (e.g., radiologists or standard of care).
- Quantitative-imaging claims need repeatability/reproducibility evidence and, where
  relevant, multi-vendor/multi-site generalizability.
- Retrospective designs must address selection bias and confounding; prospective and
  multi-center evidence strengthens fit.

## Structure & house style

- RSNA format with a structured abstract and a short "key results" / summary statement;
  re-check current article types (Original Research, etc.) and limits on the live guide.
- A STARD (or CLAIM for AI) flow diagram and completed checklist are expected where
  applicable.
- Figures are central and must be high-quality, de-identified images with clear
  annotations; report acquisition parameters.
- Methods must give enough acquisition, analysis, and (for AI) model and data detail
  to allow reproduction; data/code sharing strengthens the submission.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and
  `../../resources/official-source-map.md`; start from the ICMJE/EQUATOR and RSNA
  anchors, then cite the current Radiology page you checked.
- Search the live site for "Radiology RSNA instructions for authors" and follow the
  current version.
- Re-check article types, abstract/summary format, and word/figure limits.
- Confirm the STARD (diagnostic) or CLAIM (AI) checklist, and prospective registration
  where the study design requires it.
- Re-check IRB/ethics and consent, patient-image de-identification and consent, ICMJE
  authorship and conflict-of-interest disclosure, funding, data/code availability, and
  AI-use disclosure.
- If the live official instructions conflict with this skill, the official instructions
  win.

## Pre-submission self-check

- [ ] The study asks a clinically meaningful imaging question with a valid, independent reference standard.
- [ ] Sample size/power is justified; reader studies report inter-/intra-reader agreement.
- [ ] AI/ML work separates train/validation/test data and includes external/multi-site validation (CLAIM).
- [ ] Diagnostic-accuracy reporting follows STARD with a flow diagram; spectrum/verification bias addressed.
- [ ] Images are de-identified, high-quality, and annotated; acquisition parameters reported.
- [ ] IRB/consent, disclosures, and a data/code-availability statement are prepared.

## Common desk-reject triggers

- Small, single-center retrospective series with no reference-standard rigor or limited generalizability.
- AI models evaluated only on internal data, with no external validation or clinical baseline.
- Diagnostic-accuracy studies with verification or spectrum bias and no STARD reporting.
- Quantitative-imaging claims with no repeatability/reproducibility evidence.
- Pure technical/phantom work with no clinical relevance, better suited to a physics or subspecialty journal.

## Re-routing decision

- Subspecialty imaging focus (neuro/cardiac/abdominal) → a dedicated subspecialty imaging journal.
- Imaging-AI methodological advance over clinical validation → a medical-imaging methods venue (e.g., `ieee-transactions-on-medical-imaging` in the engineering bundle).
- Cardiology/neurology clinical outcome dominant over imaging method → `jama-cardiology` / `jama-neurology` / `stroke`.
- Oncology imaging with a clinical-oncology endpoint → `jama-oncology` / `annals-of-oncology`.
- Broad, practice-changing significance → general medicine (`jama` / NEJM in the natural-science bundle).

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Radiology (RSNA)
[Imaging tags] <modality + task, e.g. MRI diagnostic accuracy, imaging AI>
[Design / reporting guideline] <diagnostic-STARD / AI-CLAIM / interventional-outcome>
[Method/evidence] <reference standard, sample size, external validation>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / STARD or CLAIM / registration / de-identification / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
