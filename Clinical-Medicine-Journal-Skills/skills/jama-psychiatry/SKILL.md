---
name: jama-psychiatry
description: Use when targeting JAMA Psychiatry or deciding whether a clinical-psychiatry or mental-health study fits this venue. Encodes the journal's fit, the psychiatric-trial and observational/neuropsychiatric evidence bar, reporting-guideline and trial-registration requirements, JAMA Network house style, official-submission re-check, and desk-reject heuristics. Venue-fit aid only, not clinical advice.
---

# JAMA Psychiatry (jama-psychiatry)

## Journal positioning

JAMA Psychiatry is a JAMA Network specialty journal for clinical psychiatry and
mental-health research relevant to the practice of psychiatry. It favors rigorous,
practice-relevant work — randomized psychiatric and psychotherapy trials, large
epidemiologic and registry studies, and neuropsychiatric/biomarker and neuroimaging
studies tied to clinical phenotypes — with JAMA's emphasis on validated outcomes,
adequate power, and direct relevance to mental-health care. It is a JAMA Network venue
with a North-American clinical center of gravity, distinct from the Lancet family's
global-mental-health reach. Small symptom-scale studies, underpowered neuroimaging
with no replication, and biomarker correlations without clinical endpoints are a weak
fit. This skill is a **fit / venue-selection / re-framing** aid; it is not clinical or
regulatory advice and does not replace the journal's current instructions for authors.
Before submitting, re-check the live JAMA Psychiatry author instructions.

## When to trigger

- The author names JAMA Psychiatry for a psychiatric trial, epidemiologic, or
  neuropsychiatric study and wants a fit/framing check.
- A mental-health study must be re-framed around a validated clinical outcome and a
  practice-relevant question for a psychiatry readership.
- The author is choosing between JAMA Psychiatry, JAMA, and the Lancet family
  (`the-lancet-psychiatry`).
- The author needs the journal's reporting-guideline, registration, and desk-reject
  expectations for psychiatry work.

## Scope & topic fit

- Randomized trials of pharmacologic, psychotherapeutic, neuromodulation, or digital
  mental-health interventions with validated symptom or functional outcomes.
- Large psychiatric epidemiology, registry, and longitudinal cohort studies on
  incidence, course, comorbidity, and mortality.
- Neuropsychiatric and neuroimaging studies (structural/functional MRI, EEG) tied to
  diagnosis, prognosis, or treatment response, with adequate power and replication.
- Genetic and biomarker studies validated against a clinical phenotype or outcome.
- Suicide, substance-use, and severe-mental-illness research with appropriate ethics
  and safety monitoring.
- Health-services, disparities, and mental-health-policy research; focused systematic
  reviews and meta-analyses.

## Method & evidence bar

- Trials must be adequately powered with a prespecified primary outcome using a
  validated, clinically meaningful measure; minimal clinically important differences and
  response/remission definitions should be addressed.
- The applicable reporting guideline and checklist are required: CONSORT for trials
  (including extensions for non-pharmacologic/psychotherapy and digital interventions),
  STROBE for observational studies, PRISMA for systematic reviews.
- Trials require prospective registration; registration number, protocol, and
  statistical-analysis plan are expected.
- Blinding is often imperfect in psychotherapy/behavioral trials; the report must state
  who was blinded and how outcome ascertainment was protected from bias.
- Neuroimaging/biomarker work needs adequate power, correction for multiple comparisons,
  and ideally independent replication or external validation.
- Observational claims must address confounding, reverse causation, and missing data;
  causal language must match the design.

## Structure & house style

- JAMA Network format with a structured abstract and a Key Points box; re-check current
  article types (Original Investigation, Brief Report, Research Letter, etc.) and limits
  on the live guide.
- The introduction frames a focused, practice-relevant psychiatric question; the
  discussion states the clinical implication plainly and avoids overstatement.
- Tables/figures follow JAMA Network statistical-reporting standards; CONSORT/STROBE
  flow diagrams and outcome-trajectory figures are expected where applicable.
- Supplements carry the protocol, SAP, scale definitions, and additional analyses.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and
  `../../resources/official-source-map.md`; start from the ICMJE and JAMA Network
  anchors, then cite the current JAMA Psychiatry page you checked.
- Search the live site for "JAMA Psychiatry instructions for authors" and follow the
  current version.
- Re-check article types and word/reference/table limits, structured-abstract and Key
  Points format, and the JAMA Network statistical-reporting requirements.
- Confirm trial registration, the reporting checklist (CONSORT/STROBE/PRISMA), the
  data-sharing statement, and protocol/SAP submission.
- Re-check IRB/ethics, consent (including capacity to consent in severe mental illness),
  safety monitoring for suicide/self-harm studies, ICMJE disclosures, funding, and
  AI-use disclosure.
- If the live official instructions conflict with this skill, the official instructions
  win.

## Pre-submission self-check

- [ ] The study answers a practice-relevant psychiatric question with a validated, clinically meaningful outcome.
- [ ] The primary outcome is prespecified; response/remission and clinically important differences are addressed; the study is adequately powered.
- [ ] The correct reporting checklist (CONSORT/STROBE/PRISMA) is completed and attached; blinding and outcome ascertainment are described.
- [ ] Trials are prospectively registered with the number in the manuscript; protocol/SAP provided.
- [ ] Neuroimaging/biomarker work corrects for multiple comparisons and addresses replication; confounding and reverse causation are handled.
- [ ] IRB/consent (including capacity), safety monitoring, ICMJE disclosures, and a data-sharing statement are prepared.

## Common desk-reject triggers

- Underpowered symptom-scale trials or single-site studies with no clear practice relevance.
- Neuroimaging studies underpowered, uncorrected for multiple comparisons, or without replication.
- Biomarker/genetic correlations with no clinical phenotype, endpoint, or validation.
- Behavioral/psychotherapy trials with undescribed blinding and bias-prone outcome ascertainment.
- Missing trial registration, protocol, or the required reporting checklist.
- Narrow neuroscience or basic-affective-science interest better served by a neuroscience journal.

## Re-routing decision

- Lancet-family, global-mental-health, or LMIC-focused framing → `the-lancet-psychiatry`.
- Broadly practice-changing, top-tier psychiatry trial → general medicine (`jama` / NEJM / The Lancet in the natural-science bundle).
- Neurological-disease primary focus over psychiatric phenotype → `jama-neurology` / `brain`.
- Child/adolescent mental-health with a developmental center of gravity → `jama-pediatrics`.
- General internal-medicine relevance over psychiatry specialty → `jama-internal-medicine`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] JAMA Psychiatry
[Specialty tags] <2–3 closest psychiatry/mental-health topics>
[Study design / reporting guideline] <RCT-CONSORT / cohort-STROBE / review-PRISMA>
[Method/evidence] <does power, validated outcome, registration, blinding, and replication clear the bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / registration / checklist / blinding / consent-capacity / safety / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
