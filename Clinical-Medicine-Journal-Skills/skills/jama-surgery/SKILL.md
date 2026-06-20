---
name: jama-surgery
description: Use when targeting JAMA Surgery or deciding whether a surgical-outcomes or surgical-trial study fits this venue. Encodes the journal's fit, the surgical-trial and perioperative evidence bar, surgical-reporting challenges, reporting-guideline and trial-registration requirements, JAMA Network house style, official-submission re-check, and desk-reject heuristics. Venue-fit aid only, not clinical advice.
---

# JAMA Surgery (jama-surgery)

## Journal positioning

JAMA Surgery is a JAMA Network specialty journal for surgical clinical research across
general, vascular, thoracic, transplant, trauma, and surgical-subspecialty practice. It
favors rigorous, practice-relevant work — randomized and well-designed surgical trials,
large surgical-outcomes and registry analyses, perioperative and quality-improvement
research, and comparative-effectiveness studies — with JAMA's emphasis on patient-
centered outcomes, adequate risk adjustment, and direct relevance to surgical care.
Single-surgeon case series, descriptive technique reports without comparative outcomes,
and underpowered studies are a weak fit. This skill is a **fit / venue-selection /
re-framing** aid; it is not clinical or regulatory advice and does not replace the
journal's current instructions for authors. Before submitting, re-check the live JAMA
Surgery author instructions.

## When to trigger

- The author names JAMA Surgery for a surgical trial, outcomes, or perioperative study
  and wants a fit/framing check.
- A surgical study must be re-framed around a comparative, patient-centered outcome with
  appropriate risk adjustment for a practicing-surgery audience.
- The author is choosing between JAMA Surgery, JAMA, and a surgical-subspecialty
  journal.
- The author needs the journal's surgical-trial reporting, registration, and
  desk-reject expectations.

## Scope & topic fit

- Randomized and pragmatic surgical trials (operative vs. nonoperative, technique vs.
  technique, or perioperative interventions) with patient-centered outcomes.
- Large surgical-outcomes, registry, and claims analyses (e.g., NSQIP-style) with robust
  risk adjustment for case mix.
- Perioperative, enhanced-recovery, anesthesia-surgery interface, and surgical-safety
  research.
- Comparative-effectiveness and value-of-surgery studies, including de-implementation of
  low-value operations.
- Surgical quality, volume-outcome, disparities, and health-services research.
- Systematic reviews and meta-analyses answering a focused surgical question.

## Method & evidence bar

- Studies must use patient-centered outcomes (mortality, complications graded by a
  standard scheme, function, quality of life) with adequate risk adjustment; technical
  success alone is insufficient.
- The applicable reporting guideline and checklist are required: CONSORT for trials,
  STROBE for observational studies, PRISMA for systematic reviews; surgical-innovation
  work should engage IDEAL-framework stages where relevant.
- Surgical-trial reporting challenges must be addressed explicitly: blinding is often
  impossible (state who was blinded — patients, assessors, analysts), the learning curve
  and surgeon/center experience must be reported, and the intervention must be
  standardized and described reproducibly.
- Trials require prospective registration; registration number, protocol, and
  statistical-analysis plan are expected.
- Observational/registry claims must address confounding by indication, selection bias,
  and clustering by surgeon/center; causal language must match the design.
- Volume-outcome and center-effect analyses need appropriate multilevel modeling.

## Structure & house style

- JAMA Network format with a structured abstract and a Key Points box; re-check current
  article types (Original Investigation, Brief Report, Research Letter, etc.) and limits
  on the live guide.
- The introduction frames a focused, practice-relevant surgical question; the discussion
  states the clinical implication and net benefit/harm plainly.
- Tables/figures follow JAMA Network statistical-reporting standards; CONSORT/STROBE
  flow diagrams, complication tables, and risk-adjusted outcome figures are expected
  where applicable.
- Supplements carry the protocol, SAP, intervention standardization details, and
  additional analyses.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and
  `../../resources/official-source-map.md`; start from the ICMJE and JAMA Network
  anchors, then cite the current JAMA Surgery page you checked.
- Search the live site for "JAMA Surgery instructions for authors" and follow the
  current version.
- Re-check article types and word/reference/table limits, structured-abstract and Key
  Points format, and the JAMA Network statistical-reporting requirements.
- Confirm trial registration, the reporting checklist (CONSORT/STROBE/PRISMA), the
  data-sharing statement, and protocol/SAP submission.
- Re-check IRB/ethics and consent statements, ICMJE disclosures (including
  device/industry ties), funding, and AI-use disclosure.
- If the live official instructions conflict with this skill, the official instructions
  win.

## Pre-submission self-check

- [ ] The study answers a practice-relevant surgical question with a comparative, patient-centered outcome and adequate risk adjustment.
- [ ] Blinding, the learning curve, and surgeon/center experience are reported; the intervention is standardized and reproducibly described.
- [ ] The correct reporting checklist (CONSORT/STROBE/PRISMA) is completed and attached; complications are graded by a standard scheme.
- [ ] Trials are prospectively registered with the number in the manuscript; protocol/SAP provided.
- [ ] Confounding by indication, selection bias, and surgeon/center clustering are addressed; causal language matches the design.
- [ ] IRB/consent, ICMJE disclosures (including device ties), and a data-sharing statement are prepared.

## Common desk-reject triggers

- Single-surgeon or single-center case series and technique reports with no comparator or risk adjustment.
- Outcomes reported as technical success only, without complications, function, or patient-centered endpoints.
- Surgical trials that ignore blinding, the learning curve, or intervention standardization.
- Registry analyses with confounding by indication or unaddressed surgeon/center clustering and overstated causal claims.
- Missing trial registration, protocol, or the required reporting checklist.
- Narrow surgical-subspecialty interest better served by a subspecialty journal.

## Re-routing decision

- Broadly practice-changing, top-tier surgical trial → general medicine (`jama` / NEJM / The Lancet in the natural-science bundle).
- Surgical-oncology with a cancer-endpoint center of gravity → `jama-oncology` / `annals-of-oncology`.
- Cardiac/cardiovascular surgical outcomes tied to cardiology endpoints → `jama-cardiology`.
- Neurosurgical/cerebrovascular focus → `jama-neurology` / `stroke` / `brain`.
- General internal-medicine or perioperative-medicine relevance over surgery → `jama-internal-medicine`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] JAMA Surgery
[Specialty tags] <2–3 closest surgical topics>
[Study design / reporting guideline] <RCT-CONSORT / registry-STROBE / review-PRISMA / innovation-IDEAL>
[Method/evidence] <does outcome choice, risk adjustment, blinding/learning-curve, and registration clear the bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / registration / checklist / standardization / ethics / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
