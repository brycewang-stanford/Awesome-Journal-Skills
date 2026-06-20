---
name: jama-neurology
description: Use when targeting JAMA Neurology or deciding whether a clinical-neurology study fits this venue. Encodes the journal's fit, the neurological-trial and observational evidence bar, reporting-guideline and trial-registration requirements, JAMA Network house style, official-submission re-check, and desk-reject heuristics. Venue-fit aid only, not clinical advice.
---

# JAMA Neurology (jama-neurology)

## Journal positioning

JAMA Neurology is a JAMA Network specialty journal for clinical neurology research
across the breadth of neurological disease — neurodegenerative, cerebrovascular,
neuroimmune, epilepsy, movement, neuromuscular, and headache disorders. It favors
randomized clinical trials and rigorous observational and biomarker studies tied to
clinically meaningful neurological outcomes, with JAMA's emphasis on adequate power,
validated endpoints, and direct relevance to neurological practice. Mechanistic
bench neuroscience, small case series, and biomarker correlations without clinical
endpoints are a weak fit; that work belongs to a translational-neuroscience venue.
This skill is a **fit / venue-selection / re-framing** aid; it is not clinical or
regulatory advice and does not replace the journal's current instructions for authors.
Before submitting, re-check the live JAMA Neurology author instructions.

## When to trigger

- The author names JAMA Neurology for a clinical-neurology trial, cohort, or biomarker
  study and wants a fit/framing check.
- A neurological study must be re-framed around a validated clinical or functional
  endpoint (disability scale, cognitive measure, seizure freedom) for a practicing-
  neurology audience.
- The author is choosing between JAMA Neurology, JAMA, a mechanistic-translational venue
  (`brain`), or a cerebrovascular-specific venue (`stroke`).
- The author needs the journal's reporting-guideline, registration, and desk-reject
  expectations for neurology work.

## Scope & topic fit

- Randomized clinical trials in neurology (disease-modifying, symptomatic, or
  device/neuromodulation), including pragmatic designs.
- Observational and cohort studies across neurodegenerative (Alzheimer, Parkinson),
  cerebrovascular, demyelinating, epilepsy, and neuromuscular disease with clinical
  endpoints.
- Fluid and imaging biomarker studies (e.g., amyloid/tau, neurofilament, MRI markers)
  validated against diagnosis, progression, or outcome.
- Diagnostic, prognostic, and natural-history studies with validated neurological scales
  and meaningful follow-up.
- Health-services, epidemiology, and disparities research in neurological disease.
- Systematic reviews and meta-analyses answering a focused neurological question.

## Method & evidence bar

- Trials must be adequately powered with a prespecified, clinically meaningful primary
  endpoint using validated neurological/functional outcome measures; biomarker-only
  endpoints need strong justification.
- The applicable reporting guideline and checklist are required: CONSORT for trials,
  STROBE for observational studies, PRISMA for systematic reviews; biomarker/diagnostic
  work should follow STARD-style rigor where relevant.
- Trials require prospective registration; registration number, protocol, and
  statistical-analysis plan are expected.
- Outcome scales must be validated and analyzed appropriately (e.g., ordinal/repeated-
  measures methods); minimal clinically important differences should be addressed.
- Observational and biomarker claims must address confounding, verification bias, and
  the diagnosis reference standard; causal language must match the design.
- Longitudinal/progression studies need adequate follow-up and handling of dropout and
  competing risks.

## Structure & house style

- JAMA Network format with a structured abstract and a Key Points box; re-check current
  article types (Original Investigation, Brief Report, Research Letter, etc.) and limits
  on the live guide.
- The introduction frames a focused, practice-relevant neurological question; the
  discussion states the clinical or diagnostic implication plainly.
- Tables/figures follow JAMA Network statistical-reporting standards; CONSORT/STROBE
  flow diagrams and outcome-distribution figures are expected where applicable.
- Supplements carry the protocol, SAP, scale definitions, and additional analyses.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and
  `../../resources/official-source-map.md`; start from the ICMJE and JAMA Network
  anchors, then cite the current JAMA Neurology page you checked.
- Search the live site for "JAMA Neurology instructions for authors" and follow the
  current version.
- Re-check article types and word/reference/table limits, structured-abstract and Key
  Points format, and the JAMA Network statistical-reporting requirements.
- Confirm trial registration, the reporting checklist (CONSORT/STROBE/PRISMA), the
  data-sharing statement, and protocol/SAP submission.
- Re-check IRB/ethics and consent statements (including capacity/surrogate consent in
  cognitive-impairment studies), ICMJE disclosures, funding, and AI-use disclosure.
- If the live official instructions conflict with this skill, the official instructions
  win.

## Pre-submission self-check

- [ ] The study answers a practice-relevant neurological question with a validated, clinically meaningful endpoint.
- [ ] The primary endpoint uses an appropriate, validated scale analyzed correctly; the study is adequately powered.
- [ ] The correct reporting checklist (CONSORT/STROBE/PRISMA/STARD) is completed and attached.
- [ ] Trials are prospectively registered with the number in the manuscript; protocol/SAP provided.
- [ ] Confounding, verification bias, dropout, and the diagnosis reference standard are addressed; causal language matches the design.
- [ ] IRB/consent (including surrogate consent where relevant), ICMJE disclosures, and a data-sharing statement are prepared.

## Common desk-reject triggers

- Small case series or single-center cohorts with no validated endpoint or generalizability.
- Biomarker correlations with no clinical/diagnostic endpoint or independent validation.
- Trials using non-validated or improperly analyzed outcome scales, or underpowered for the endpoint.
- Observational analyses with verification bias or overstated causal claims.
- Missing trial registration, protocol, or the required reporting checklist.
- Mechanistic/bench neuroscience better served by a translational-neuroscience journal.

## Re-routing decision

- Mechanistic translational neuroscience-to-clinical advance → `brain`.
- Cerebrovascular/stroke-specific clinical focus → `stroke`.
- Broadly practice-changing, top-tier neurology trial → general medicine (`jama` / NEJM / The Lancet in the natural-science bundle).
- General internal-medicine relevance over neurology specialty → `jama-internal-medicine`.
- Neuropsychiatric/mental-health primary focus → `jama-psychiatry` / `the-lancet-psychiatry`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] JAMA Neurology
[Specialty tags] <2–3 closest neurology topics>
[Study design / reporting guideline] <RCT-CONSORT / cohort-STROBE / biomarker-STARD / review-PRISMA>
[Method/evidence] <does power, validated endpoint, registration, and validation clear the bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / registration / checklist / scale validation / consent / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
