---
name: jama-oncology
description: Use when targeting JAMA Oncology or deciding whether a clinical-oncology study fits this venue. Encodes the journal's fit, the cancer-trial and outcomes-research evidence bar, reporting-guideline and trial-registration requirements, JAMA Network house style, official-submission re-check, and desk-reject heuristics. Venue-fit aid only, not clinical advice.
---

# JAMA Oncology (jama-oncology)

## Journal positioning

JAMA Oncology is a JAMA Network specialty journal for clinical and translational
oncology research aimed at a broad cancer-care readership — medical, surgical, and
radiation oncologists, as well as cancer-epidemiology and outcomes researchers. It
favors practice-relevant work: randomized cancer trials, comparative-effectiveness and
real-world outcomes analyses, screening and prevention studies, and biomarker work tied
to a clinically meaningful endpoint. It is positioned as a general oncology venue with
JAMA's emphasis on absolute benefit, toxicity, and patient-centered outcomes, distinct
from a society flagship such as Annals of Oncology (ESMO). Single-arm early-phase
reports with no comparator, descriptive molecular series, and surrogate-only signals
with weak clinical translation are a weak fit. This skill is a **fit /
venue-selection / re-framing** aid; it is not clinical or regulatory advice and does
not replace the journal's current instructions for authors. Before submitting, re-check
the live JAMA Oncology author instructions.

## When to trigger

- The author names JAMA Oncology for a clinical, epidemiologic, or outcomes oncology
  study and wants a fit/framing check.
- A cancer study must be re-framed around a clinically meaningful survival, toxicity,
  or quality-of-life endpoint for a broad oncology audience.
- The author is choosing between JAMA Oncology, JAMA, and a society or subspecialty
  oncology journal (e.g., Annals of Oncology).
- The author needs the journal's reporting-guideline, registration, and desk-reject
  expectations for oncology work.

## Scope & topic fit

- Randomized oncology trials (phase 2/3) reporting survival, response, toxicity, or
  patient-reported outcomes, including practice-de-escalation trials.
- Comparative-effectiveness and real-world-evidence studies using cancer registries,
  claims, or institutional cohorts with rigorous confounding control.
- Cancer screening, early-detection, and prevention studies with clinically meaningful
  endpoints and harms accounting.
- Prognostic and predictive biomarker studies validated against an outcome, not just
  associated with a molecular feature.
- Health-services, disparities, financial-toxicity, and survivorship research in
  oncology.
- Pooled analyses and meta-analyses answering a focused, decision-relevant cancer
  question.

## Method & evidence bar

- Trials must be adequately powered with a prespecified primary endpoint; overall
  survival and validated surrogates are preferred, and surrogate-only endpoints need
  explicit justification of clinical relevance.
- The applicable reporting guideline and checklist are required: CONSORT for trials,
  STROBE for observational/registry studies, PRISMA for systematic reviews, REMARK-style
  rigor for tumor-marker work.
- Trials require prospective registration; registration number, protocol, and
  statistical-analysis plan are expected, including amendments.
- Survival analyses must report absolute differences, hazard ratios with confidence
  intervals, and adequate follow-up; toxicity (graded per a standard scheme) must be
  reported alongside efficacy.
- Real-world/registry claims must address immortal-time, selection, and indication bias;
  causal language must match the design.
- Biomarker claims need a prespecified cut-point, an independent validation set, and
  reporting of analytic performance.

## Structure & house style

- JAMA Network format with a structured abstract and a Key Points box; re-check current
  article types (Original Investigation, Brief Report, Research Letter, etc.) and limits
  on the live guide.
- The introduction frames a focused, decision-relevant cancer question; the discussion
  states the practice implication and net clinical benefit plainly.
- Tables/figures follow JAMA Network statistical-reporting standards; CONSORT/STROBE
  flow diagrams, Kaplan-Meier curves with numbers at risk, and toxicity tables are
  expected where applicable.
- Supplements carry the protocol, SAP, full toxicity and subgroup analyses, and
  consort/biomarker checklists.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and
  `../../resources/official-source-map.md`; start from the ICMJE and JAMA Network
  anchors, then cite the current JAMA Oncology page you checked.
- Search the live site for "JAMA Oncology instructions for authors" and follow the
  current version.
- Re-check article types and word/reference/table limits, structured-abstract and Key
  Points format, and the JAMA Network statistical-reporting requirements.
- Confirm trial registration, the reporting checklist (CONSORT/STROBE/PRISMA), the
  data-sharing statement, and protocol/SAP submission.
- Re-check IRB/ethics and consent statements, ICMJE authorship and conflict-of-interest
  disclosure (industry ties are scrutinized in oncology), funding, and AI-use disclosure.
- If the live official instructions conflict with this skill, the official instructions
  win.

## Pre-submission self-check

- [ ] The study answers a decision-relevant cancer question with a clinically meaningful endpoint and net-benefit framing.
- [ ] The primary endpoint is prespecified; survival/toxicity are reported with absolute and relative measures and adequate follow-up.
- [ ] The correct reporting checklist (CONSORT/STROBE/PRISMA) is completed and attached.
- [ ] Trials are prospectively registered with the number in the manuscript; protocol/SAP provided.
- [ ] Registry/real-world analyses address immortal-time, selection, and indication bias; biomarkers are independently validated.
- [ ] IRB/consent, ICMJE disclosures (including industry funding), and a data-sharing statement are prepared.

## Common desk-reject triggers

- Single-arm early-phase reports with no comparator presented as practice-relevant.
- Surrogate-only endpoints (e.g., response rate, PFS) framed as definitive clinical benefit without justification.
- Registry/real-world analyses with immortal-time or indication bias and overstated causal claims.
- Biomarker associations with no prespecified cut-point or independent validation.
- Missing trial registration, protocol, or toxicity reporting alongside efficacy.
- Narrow molecular or subspecialty interest better served by a society or basic-science cancer journal.

## Re-routing decision

- ESMO-society readership or European practice framing → `annals-of-oncology`.
- Broadly practice-changing, top-tier cancer trial → general medicine (`jama` / NEJM / The Lancet in the natural-science bundle).
- General internal-medicine relevance over oncology specialty → `jama-internal-medicine`.
- Cancer imaging with an imaging-method core → `radiology`.
- Surgical-oncology technique or perioperative focus → `jama-surgery`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] JAMA Oncology
[Specialty tags] <2–3 closest oncology topics>
[Study design / reporting guideline] <RCT-CONSORT / registry-STROBE / review-PRISMA / biomarker-REMARK>
[Method/evidence] <does power, endpoint, registration, and validation clear the bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / registration / checklist / toxicity / ethics / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
