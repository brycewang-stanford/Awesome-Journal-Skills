---
name: ieee-transactions-on-biomedical-engineering
description: Use when targeting IEEE Transactions on Biomedical Engineering (TBME) or deciding whether a biomedical-engineering methods manuscript fits this venue. Encodes the journal's fit, the engineering-method-validated-on-biological-or-clinical-data bar, validation rigor, the TBME-vs-NBME-vs-TMI routing, house style, official-submission re-check, and desk-reject heuristics.
---

# IEEE Transactions on Biomedical Engineering (ieee-transactions-on-biomedical-engineering)

## Journal positioning

IEEE Transactions on Biomedical Engineering (TBME), published by the IEEE
Engineering in Medicine and Biology Society, is a flagship archival venue for
**engineering methods applied to biology and medicine**: biosignal processing,
biomedical instrumentation and devices, neural engineering, biomechanics,
physiological-system modeling, and therapeutic/diagnostic technology. The defining
expectation is a sound engineering contribution **validated on appropriate
biomedical evidence** — measured data, phantoms, animal models, or human subjects —
with a clear biomedical rationale. Pure methods with no biomedical validation, and
clinical observations with no engineering contribution, are both poor fits.
Siblings: `nature-biomedical-engineering` (broader significance and translational
reach) and `ieee-transactions-on-medical-imaging` (imaging-specific methods). This
skill is a **fit / venue-selection / re-framing** tool. It does not replace the
journal's current official author information. Before submitting, re-check the live
IEEE TBME author guidance and submission system.

## When to trigger

- The author names TBME for a biosignal, instrumentation/device, neural-engineering,
  or physiological-modeling manuscript and wants a fit/framing check.
- A method must be re-framed so the **engineering contribution and biomedical
  validation** are both clear, not just an algorithm or just a clinical finding.
- The author is choosing among TBME, `nature-biomedical-engineering`, and
  `ieee-transactions-on-medical-imaging`.
- The author needs TBME's validation bar and desk-reject heuristics.

## Scope & topic fit

- Biosignal processing and analysis: ECG/EEG/EMG and other physiological signals,
  with a methodological advance validated on real recordings.
- Biomedical instrumentation, sensors, and devices: design, characterization, and
  demonstration on phantoms, benchtop, or subjects.
- Neural engineering: brain–machine interfaces, neural recording/stimulation, and
  decoding methods with experimental validation.
- Biomechanics, rehabilitation engineering, and wearable/assistive systems evaluated
  on subjects or realistic models.
- Physiological-system and computational modeling validated against measured
  biological/clinical data or making tested predictions.
- Therapeutic and diagnostic technology (e.g., stimulation, ultrasound therapy,
  point-of-care diagnostics) with quantitative evaluation.

## Method & evidence bar

- The contribution must pair a clear **engineering method** with **biomedical
  validation**: measured data, phantoms, animal models, or human-subject results,
  appropriate to the claim.
- Report study/data details: subjects/samples, acquisition and instrumentation,
  protocol, and reference/ground truth; underpowered single-subject demos rarely suffice.
- Use task-appropriate, statistically supported metrics; benchmark against established
  biomedical methods, not a strawman, with fair tuning.
- For devices/instrumentation, report performance characterization (accuracy,
  sensitivity, SNR, safety-relevant parameters) under stated conditions.
- Address robustness and generalization across subjects, conditions, or sites, and
  discuss limitations and failure modes relevant to use.
- Reproducibility: enough detail (and ideally code/data per policy) to reproduce the
  reported results.

## Structure & house style

- IEEE double-column format; TBME publishes full **Papers** and shorter
  contributions — match the article type to the contribution and re-check current
  definitions and length policy on the live guide.
- The introduction motivates the biomedical need and the engineering gap, then states
  the contribution; pure-method or pure-clinical framings are discouraged.
- Figures are load-bearing: device/signal schematics, representative recordings with
  the proposed analysis, and quantitative comparison plots with error bars.
- The methods section specifies instrumentation, data, and protocol precisely; a
  results section with quantitative tables across subjects/conditions is central.
- Keep clinical narrative proportionate to the engineering contribution.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and
  `../../resources/official-source-map.md`; start from the IEEE Author Center
  anchors, then cite the current TBME-specific page you checked.
- Search the live site for "IEEE Transactions on Biomedical Engineering information
  for authors" and follow the current ScholarOne/IEEE version.
- Re-check article types, page/length limits and overlength policy, and the IEEE
  double-column template.
- Confirm human-subjects/animal ethics (IRB/IACUC), data/code-availability, and any
  de-identification and safety-reporting requirements.
- Re-check ORCID, competing-interests, funding, author-contribution, and AI-use
  disclosure requirements, and IEEE open-access options.
- If the live official instructions conflict with this skill, the official
  instructions win.

## Pre-submission self-check

- [ ] The paper pairs a clear engineering method with appropriate biomedical validation, not one without the other.
- [ ] Data/study details (subjects, instrumentation, protocol, reference standard) are reported and adequately powered.
- [ ] Metrics are task-appropriate with statistics; baselines are established biomedical methods.
- [ ] Device/method robustness and generalization across subjects/conditions are addressed.
- [ ] Ethics (IRB/IACUC), data provenance, and safety-relevant parameters are documented.
- [ ] Article type and length fit current TBME limits; methods are reproducible.

## Common desk-reject triggers

- A pure algorithm or model with no biomedical data validation and no clear biomedical rationale.
- A clinical observation or case study with no engineering contribution.
- Single-subject or underpowered demonstration presented as general validation.
- Missing ethics/IRB/IACUC statement for human or animal data.
- Inappropriate or absent baselines; unfair comparisons; no statistical support for claims.

## Re-routing decision

- Medical-image formation/reconstruction/analysis as the core → `ieee-transactions-on-medical-imaging`.
- Highest-significance, broadly translational biomedical advance → `nature-biomedical-engineering`.
- Core contribution is a general signal-processing method → `ieee-transactions-on-signal-processing`.
- Assistive/surgical robotics as the central result → `ieee-transactions-on-robotics`.
- Wearable/optical sensing where the photonic device is the core → `optica`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] IEEE Transactions on Biomedical Engineering
[Topic tags] <2–3 closest biomedical-engineering subtopics>
[Engineering + validation] <the method and its biomedical validation in one line>
[Method/evidence] <do the data + metrics + baselines clear TBME's validation bar?>
[Top risk] <the single most likely reason for rejection>
[Article type] Paper / shorter contribution
[Official items to re-check] <article type / length / template / ethics-data / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
