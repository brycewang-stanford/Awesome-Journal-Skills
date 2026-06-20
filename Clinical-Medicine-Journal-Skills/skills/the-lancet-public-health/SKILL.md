---
name: the-lancet-public-health
description: Use when targeting The Lancet Public Health or deciding whether a population-health study fits this venue. Encodes the journal's fit, the population-level intervention, epidemiology, and policy evidence bar, reporting-guideline and registration requirements, Lancet specialty house style, official-submission re-check, and desk-reject heuristics. Venue-fit aid only, not clinical advice.
---

# The Lancet Public Health (the-lancet-public-health)

## Journal positioning

The Lancet Public Health is a Lancet specialty journal for population and public-health
research — population-level interventions, health policy and systems, epidemiology and
disease burden, and global-health and health-equity research with population-level
relevance. It favors **rigorous studies whose unit of interest and consequence is the
population, not the individual patient**: large-scale epidemiology, policy and natural
experiments, modelling with clear public-health decision value, and interventions
addressing inequalities or the social determinants of health. The defining misfit is an
individual-level clinical study (a drug or device effect in patients) with no
population, policy, or equity dimension — that belongs in a clinical journal. This skill
is a **fit / venue-selection / re-framing** aid; it is not clinical or regulatory advice
and does not replace the journal's current instructions for authors. Before submitting,
re-check the live The Lancet Public Health author instructions.

## When to trigger

- The author names The Lancet Public Health for a population-health, epidemiology, or
  policy study and wants a fit/framing check.
- A study must be re-framed around a population-level intervention, burden, or policy
  question with equity relevance.
- The author is choosing between The Lancet Public Health, a clinical specialty journal,
  and general medicine.
- The author needs the journal's reporting-guideline, registration, and desk-reject
  expectations for population/policy evidence.

## Scope & topic fit

- Population-level interventions and policy/natural experiments (taxation, regulation,
  screening programmes, vaccination, public-health service delivery).
- Epidemiology, disease-burden, surveillance, and risk-factor studies at population
  scale, including global and comparative analyses.
- Health-systems, health-services, and health-economics research with population-level
  decision relevance.
- Health-equity, social-determinants, and inequalities research with population-level
  framing and policy implication.
- Modelling and forecasting studies (transmission, burden, intervention impact) with
  transparent assumptions and public-health decision value.
- Systematic reviews and meta-analyses answering a focused population-health or policy
  question.

## Method & evidence bar

- Studies must have a clear population-level question and an appropriate population
  denominator; individual-level clinical endpoints alone do not establish public-health
  relevance.
- The applicable reporting guideline and completed checklist are expected: STROBE for
  observational studies, CONSORT (incl. cluster-CONSORT) for trials, PRISMA for reviews,
  GATHER for global-health estimates, and modelling-reporting standards where relevant.
- Trials and pre-specified evaluations require prospective registration; protocols and
  analysis plans are expected, with cluster/stepped-wedge design detail where used.
- Observational and natural-experiment claims must address confounding, secular trends,
  ecological bias, and missing data; causal language must match the design.
- Modelling studies must state assumptions, perform sensitivity/uncertainty analysis,
  and report data sources transparently; code/data sharing strengthens the submission.
- Effect estimates need uncertainty intervals and, where relevant, equity-stratified or
  absolute population-impact measures.

## Structure & house style

- Lancet specialty format with a structured summary and a Research in context /
  evidence-before-this-study panel; re-check current article types and limits on the
  live guide.
- The introduction frames the population-health or policy gap; the discussion states the
  policy or public-health consequence and limitations plainly.
- A STROBE/CONSORT/PRISMA flow diagram and (for estimates) GATHER reporting are expected
  where applicable; tables/figures follow Lancet statistical-reporting standards.
- The role of the funding source statement and a data-sharing statement are expected;
  appendices carry protocol/model specification, full methods, and additional analyses.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and
  `../../resources/official-source-map.md`; start from the ICMJE/EQUATOR and Lancet
  anchors, then cite the current The Lancet Public Health page you checked.
- Search the live site for "The Lancet Public Health information for authors" and follow
  the current version.
- Re-check article types, structured-summary and Research in context format, and
  word/reference/figure limits.
- Confirm registration where applicable, the reporting checklist
  (STROBE/CONSORT/PRISMA/GATHER), protocol/model specification, role-of-funding-source,
  and data/code-sharing statement.
- Re-check IRB/ethics and consent or data-governance approvals, ICMJE authorship and
  conflict-of-interest disclosure, funding, and AI-use disclosure.
- If the live official instructions conflict with this skill, the official instructions
  win.

## Pre-submission self-check

- [ ] The study has a genuine population-level question, denominator, and policy/equity consequence.
- [ ] The correct reporting checklist (STROBE/CONSORT/PRISMA/GATHER) is completed and attached.
- [ ] Trials/evaluations are registered where applicable; protocol or model specification is provided.
- [ ] Confounding, secular trends, ecological bias, and missing data are addressed; causal language matches the design.
- [ ] Modelling assumptions, uncertainty, and data sources are transparent; code/data sharing is planned.
- [ ] Ethics/data-governance approvals, ICMJE disclosures, role-of-funding-source, and a data-sharing statement are prepared.

## Common desk-reject triggers

- Individual-level clinical studies with no population, policy, or equity dimension.
- Small or local descriptive surveys with no generalizable population-health implication.
- Modelling with opaque assumptions, no sensitivity analysis, or undocumented data sources.
- Ecological analyses with overstated individual-level causal claims.
- Missing reporting checklist, registration (where applicable), or data-governance approvals.
- Narrow scope without international or policy relevance, better suited to a regional or clinical venue.

## Re-routing decision

- Individual-level clinical trial or patient-outcome focus → the relevant clinical specialty journal or general medicine (`jama` / NEJM / The Lancet in the natural-science bundle).
- Population mental-health and psychiatric epidemiology dominant → `the-lancet-psychiatry`.
- Diabetes/obesity population research with a clinical-metabolic core → `the-lancet-diabetes-and-endocrinology`.
- Respiratory population/clinical research with a respiratory endpoint → `the-lancet-respiratory-medicine`.
- Cancer epidemiology with a clinical-oncology endpoint → `annals-of-oncology` / `jama-oncology`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] The Lancet Public Health
[Specialty tags] <2–3 closest population-health/policy/epidemiology topics>
[Study design / reporting guideline] <observational-STROBE / cluster-RCT-CONSORT / review-PRISMA / estimates-GATHER / modelling>
[Method/evidence] <population-level question, denominator, confounding/assumptions — does it clear the policy-relevance bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / registration / checklist / role-of-funding / ethics-data-governance / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
