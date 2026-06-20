---
name: annals-of-oncology
description: Use when targeting Annals of Oncology (ESMO) or deciding whether a clinical or translational oncology study fits this venue. Encodes the journal's fit, the practice-changing trial and ESMO-guideline evidence bar, reporting-guideline and registration requirements, ESMO house style, official-submission re-check, and desk-reject heuristics. Venue-fit aid only, not clinical advice.
---

# Annals of Oncology (annals-of-oncology)

## Journal positioning

Annals of Oncology is the flagship journal of the European Society for Medical Oncology
(ESMO), publishing clinical and translational oncology — practice-changing therapeutic
trials, biomarker and translational studies tied to clinical questions, and ESMO
clinical practice guidelines and consensus. It favors **rigorous, clinically
consequential oncology research with direct implications for the systemic treatment of
cancer**, with a strong emphasis on robust trial design, validated biomarkers, and
relevance to medical-oncology practice across tumor types. Single-arm early-phase
studies without a clear development path, retrospective series with limited
generalizability, and purely preclinical work with no clinical bridge are a weak fit.
This skill is a **fit / venue-selection / re-framing** aid; it is not clinical or
regulatory advice and does not replace the journal's current instructions for authors.
Before submitting, re-check the live Annals of Oncology author instructions.

## When to trigger

- The author names Annals of Oncology for a clinical or translational oncology study and
  wants a fit/framing check.
- A trial or biomarker study must be re-framed around a practice-changing,
  medical-oncology question with translational grounding.
- The author is choosing between Annals of Oncology, JAMA Oncology, and a review-only
  oncology venue.
- The author needs the journal's reporting-guideline, registration, and desk-reject
  expectations for clinical/translational oncology evidence.

## Scope & topic fit

- Randomized and well-designed therapeutic trials (systemic therapy, immunotherapy,
  targeted agents, combinations) with patient-important outcomes.
- Translational and biomarker studies tied to a clinical question, including predictive/
  prognostic biomarker development and validation.
- Practice-changing phase II/III studies and rigorous early-phase work with a clear
  development rationale and signal of efficacy/safety.
- Real-world, registry, and high-quality observational oncology studies with robust
  design and confounding control.
- ESMO clinical practice guidelines, consensus statements, and evidence syntheses
  (typically commissioned or aligned with ESMO process).
- Systematic reviews and meta-analyses resolving a focused, clinically consequential
  oncology question.

## Method & evidence bar

- Trials must be adequately powered with prespecified, patient-important primary
  outcomes (overall/progression-free survival, response with clinical anchoring, quality
  of life); surrogate endpoints need justification and, where relevant, validation.
- The applicable reporting guideline and completed checklist are expected: CONSORT for
  trials, STROBE for observational studies, PRISMA for systematic reviews, REMARK for
  prognostic-biomarker studies.
- Trials require prospective registration; the registration number, protocol, and
  statistical-analysis plan are expected; biomarker analyses should prespecify cut-offs
  and analysis populations.
- Translational claims must be supported by validated assays, appropriate controls, and,
  where possible, independent confirmation; preclinical-only work needs a clear clinical
  bridge.
- Observational and real-world claims must address confounding, immortal-time and
  selection bias, and missing data; causal language must match the design.
- Effect estimates need confidence intervals and absolute as well as relative measures;
  toxicity/safety reporting must be complete.

## Structure & house style

- ESMO/Annals format with a structured abstract; re-check current article types
  (original article, ESMO guideline, etc.) and limits on the live guide.
- The introduction frames the medical-oncology gap; the discussion states the
  practice-changing implication, the translational rationale, and limitations plainly.
- A CONSORT/STROBE/PRISMA/REMARK flow diagram and checklist are expected where
  applicable; tables/figures follow the journal's statistical-reporting standards.
- Supplementary material carries protocol, full statistical and translational methods,
  safety detail, and additional analyses; a data-sharing statement is expected.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and
  `../../resources/official-source-map.md`; start from the ICMJE/EQUATOR and ESMO
  anchors, then cite the current Annals of Oncology page you checked.
- Search the live site for "Annals of Oncology guide for authors" and follow the current
  version.
- Re-check article types, structured-abstract format, and word/reference/figure limits.
- Confirm trial registration, the reporting checklist (CONSORT/STROBE/PRISMA/REMARK),
  protocol/SAP, biomarker-analysis prespecification, and data-sharing statement.
- Re-check IRB/ethics and consent, ICMJE authorship and conflict-of-interest disclosure
  (notable for industry-sponsored oncology trials), funding, and AI-use disclosure.
- If the live official instructions conflict with this skill, the official instructions
  win.

## Pre-submission self-check

- [ ] The study answers a practice-changing medical-oncology question with translational grounding where relevant.
- [ ] The primary outcome is prespecified and patient-important; the study is adequately powered.
- [ ] The correct reporting checklist (CONSORT/STROBE/PRISMA/REMARK) is completed and attached.
- [ ] Trials are prospectively registered with the number in the manuscript; protocol/SAP and biomarker cut-offs prespecified.
- [ ] Confounding, selection/immortal-time bias, missing data, and complete safety reporting are addressed; causal language matches the design.
- [ ] IRB/consent, ICMJE disclosures (including industry sponsorship), and a data-sharing statement are prepared.

## Common desk-reject triggers

- Single-arm early-phase or retrospective series with limited generalizability and no clear development path.
- Purely preclinical or mechanistic work with no clinical bridge or translational endpoint.
- Surrogate endpoints presented as definitive without justification or validation.
- Missing trial registration, protocol, complete safety data, or the required reporting checklist.
- Underpowered or single-center observational analyses with overstated causal/efficacy claims.
- Unsolicited guideline-style reviews not aligned with ESMO process, or narrow scope without practice relevance.

## Re-routing decision

- JAMA Network family or US-centric clinical-oncology framing → `jama-oncology`.
- Authoritative, commissioned clinical-oncology review or perspective (not primary data) → `nature-reviews-clinical-oncology`.
- Cancer epidemiology with a population/policy core rather than a treatment endpoint → `the-lancet-public-health`.
- Oncology imaging with an imaging-method core → `radiology`.
- Broad, practice-changing significance beyond oncology specialty → general medicine (`jama` / NEJM / The Lancet in the natural-science bundle).

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Annals of Oncology (ESMO)
[Specialty tags] <2–3 closest clinical/translational oncology topics>
[Study design / reporting guideline] <RCT-CONSORT / biomarker-REMARK / cohort-STROBE / review-PRISMA>
[Method/evidence] <power, endpoint, registration, translational validation — does it clear the practice-changing bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / registration / checklist / biomarker prespecification / ethics / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
