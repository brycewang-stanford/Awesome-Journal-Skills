---
name: jama-cardiology
description: Use when targeting JAMA Cardiology or deciding whether a cardiovascular-medicine study fits this venue. Encodes the journal's fit, the cardiovascular-trial and outcomes evidence bar, reporting-guideline and trial-registration requirements, JAMA Network house style, official-submission re-check, and desk-reject heuristics. Venue-fit aid only, not clinical advice.
---

# JAMA Cardiology (jama-cardiology)

## Journal positioning

JAMA Cardiology is a JAMA Network specialty journal for cardiovascular clinical
research relevant to the practice of cardiology and cardiovascular medicine. It favors
rigorous, practice-relevant work — randomized cardiovascular trials, large outcomes and
registry analyses, prevention and risk-factor studies, and cardiac imaging studies tied
to clinical outcomes — with JAMA's emphasis on hard endpoints, absolute risk, and
direct relevance to patient care. Mechanistic bench cardiology, small physiology
studies with surrogate-only readouts, and imaging-technique papers with no outcome link
are a weak fit. This skill is a **fit / venue-selection / re-framing** aid; it is not
clinical or regulatory advice and does not replace the journal's current instructions
for authors. Before submitting, re-check the live JAMA Cardiology author instructions.

## When to trigger

- The author names JAMA Cardiology for a cardiovascular clinical, outcomes, or
  imaging-outcome study and wants a fit/framing check.
- A cardiovascular study must be re-framed around a hard clinical endpoint (MACE,
  mortality, hospitalization) for a practicing-cardiology audience.
- The author is choosing between JAMA Cardiology, JAMA, and a cardiology-society
  journal.
- The author needs the journal's reporting-guideline, registration, and desk-reject
  expectations for cardiovascular work.

## Scope & topic fit

- Randomized cardiovascular trials (drug, device, procedural, or strategy) with
  clinically meaningful endpoints, including pragmatic and de-implementation designs.
- Large outcomes, registry, and claims analyses on cardiovascular events, heart
  failure, arrhythmia, and structural/interventional outcomes.
- Cardiovascular prevention, risk-factor, lipid, hypertension, and population
  cardiovascular-health studies.
- Cardiac imaging (echo, CMR, CCT, nuclear) studies where the contribution is a
  clinical-outcome or prognostic association, not a pure imaging technique.
- Cardiovascular biomarker and risk-prediction studies validated against outcomes.
- Systematic reviews and meta-analyses answering a focused cardiovascular question.

## Method & evidence bar

- Trials must be adequately powered with a prespecified primary endpoint, ideally a
  hard clinical outcome or validated composite (with the composite components reported);
  surrogate-only endpoints need strong justification.
- The applicable reporting guideline and checklist are required: CONSORT for trials
  (with device/procedure extensions where relevant), STROBE for observational studies,
  PRISMA for systematic reviews; risk-model work should follow TRIPOD-style reporting.
- Trials require prospective registration; registration number, protocol, and
  statistical-analysis plan are expected, including for device and procedural trials.
- Effect estimates need absolute and relative measures, confidence intervals, adequate
  follow-up, and adjudicated endpoints where feasible.
- Registry/observational claims must address confounding by indication, immortal-time
  bias, and missing data; causal language must match the design.
- Risk-prediction and biomarker claims need internal and ideally external validation,
  calibration, and discrimination metrics.

## Structure & house style

- JAMA Network format with a structured abstract and a Key Points box; re-check current
  article types (Original Investigation, Brief Report, Research Letter, etc.) and limits
  on the live guide.
- The introduction frames a focused, practice-relevant cardiovascular question; the
  discussion states the clinical implication and absolute benefit/harm plainly.
- Tables/figures follow JAMA Network statistical-reporting standards; CONSORT/STROBE
  flow diagrams, event-free survival curves with numbers at risk, and adjudicated-event
  tables are expected where applicable.
- Supplements carry the protocol, SAP, endpoint definitions, and additional analyses.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and
  `../../resources/official-source-map.md`; start from the ICMJE and JAMA Network
  anchors, then cite the current JAMA Cardiology page you checked.
- Search the live site for "JAMA Cardiology instructions for authors" and follow the
  current version.
- Re-check article types and word/reference/table limits, structured-abstract and Key
  Points format, and the JAMA Network statistical-reporting requirements.
- Confirm trial registration, the reporting checklist (CONSORT/STROBE/PRISMA), the
  data-sharing statement, and protocol/SAP submission.
- Re-check IRB/ethics and consent statements, ICMJE authorship and conflict-of-interest
  disclosure (device/industry ties scrutinized), funding, and AI-use disclosure.
- If the live official instructions conflict with this skill, the official instructions
  win.

## Pre-submission self-check

- [ ] The study answers a practice-relevant cardiovascular question with a hard or validated clinical endpoint.
- [ ] The primary endpoint is prespecified and adjudicated where feasible; the study is adequately powered.
- [ ] The correct reporting checklist (CONSORT/STROBE/PRISMA/TRIPOD) is completed and attached.
- [ ] Trials are prospectively registered with the number in the manuscript; protocol/SAP provided.
- [ ] Confounding by indication, immortal-time bias, and missing data are addressed; causal language matches the design.
- [ ] IRB/consent, ICMJE disclosures (including device/industry ties), and a data-sharing statement are prepared.

## Common desk-reject triggers

- Underpowered trials or surrogate-only physiology studies framed as practice-relevant.
- Imaging-technique papers with no clinical-outcome or prognostic link.
- Registry/observational analyses with confounding by indication or immortal-time bias and overstated causal claims.
- Risk models or biomarkers without validation, calibration, or discrimination reporting.
- Missing trial registration, protocol, endpoint adjudication, or the required reporting checklist.
- Mechanistic/basic cardiology better served by a cardiovascular-science journal.

## Re-routing decision

- Broadly practice-changing, top-tier cardiovascular trial → general medicine (`jama` / NEJM / The Lancet in the natural-science bundle).
- General internal-medicine relevance over cardiology specialty → `jama-internal-medicine`.
- Cardiac imaging with an imaging-method core over clinical outcome → `radiology`.
- Cerebrovascular/stroke-specific cardiovascular focus → `stroke`.
- Surgical/perioperative cardiac focus → `jama-surgery`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] JAMA Cardiology
[Specialty tags] <2–3 closest cardiovascular topics>
[Study design / reporting guideline] <RCT-CONSORT / cohort-STROBE / model-TRIPOD / review-PRISMA>
[Method/evidence] <does power, endpoint, registration, and validation clear the bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / registration / checklist / endpoint adjudication / ethics / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
