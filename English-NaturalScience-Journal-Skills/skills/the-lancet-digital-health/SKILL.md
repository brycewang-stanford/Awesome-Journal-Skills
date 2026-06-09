---
name: the-lancet-digital-health
description: Use when targeting The Lancet Digital Health (Lancet Digit. Health) or deciding whether a digital-health, clinical-AI, or health-informatics manuscript fits this open-access clinical venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# The Lancet Digital Health (the-lancet-digital-health)

## Journal positioning

The Lancet Digital Health is an Elsevier open-access title in the Lancet family, and it is a leading venue for clinically grounded digital health research. Its defining character is clinical rigor applied to digital and data-driven medicine: it rewards work where an algorithm, digital intervention, or informatics method is validated against clinically meaningful endpoints and reported to the standards expected of any Lancet clinical study, not technical novelty alone. The journal publishes AI/ML in healthcare, digital interventions, telemedicine, wearable and sensor research, and health informatics — but the bar is demonstrated or credible clinical impact, external validation, and transparent reporting. Readership spans clinicians, data scientists, informaticians, and health-policy audiences. This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Lancet Digital Health site.

## When to trigger

- The author has a clinical AI/ML, digital-intervention, or health-informatics study with patient- or population-level relevance and names this journal as the venue.
- A manuscript develops or validates a clinical prediction model, diagnostic algorithm, or digital tool, and the author is choosing between this journal and Nature Medicine, Science Translational Medicine, or Cell Reports Medicine.
- A model-development paper needs to be held to clinical reporting standards (TRIPOD, CONSORT-AI, SPIRIT-AI) and external validation before submission.
- The author needs the journal's clinical-validation expectations, scope boundaries, and desk-reject criteria.

## Scope & topic fit

- Clinical AI/ML: diagnostic, prognostic, or treatment-recommendation models developed and externally validated on clinical data (imaging, EHR, signals, pathology, genomics) with clinically meaningful endpoints.
- Digital interventions and their trials: app-, web-, or device-delivered interventions evaluated in randomized or rigorous comparative designs with health outcomes.
- Health informatics and data science: methods for clinical data linkage, phenotyping, real-world-evidence generation, and learning health systems where the clinical use case is central.
- Telemedicine, remote monitoring, wearables, and sensors: studies evaluating accuracy, clinical utility, equity, or outcomes of remote and digital care.
- Implementation, safety, fairness, and evaluation of deployed digital-health and AI systems, including algorithmic bias, generalizability, and human-AI interaction in clinical workflows.
- Digital epidemiology and public-health informatics where data methods drive a clinically or policy-relevant conclusion.

## Method & evidence bar

- The clinical question and the clinically meaningful endpoint must be explicit; technical performance metrics alone (AUC on a single dataset) do not establish fit.
- Prediction and diagnostic models must follow TRIPOD (or TRIPOD-AI) reporting and report external/independent validation, calibration, and clinically relevant performance — not just internal cross-validation.
- Trials of AI or digital interventions must follow the relevant CONSORT-AI / SPIRIT-AI extensions; registration of prospective trials is expected.
- Datasets, cohorts, and patient populations must be described with attention to representativeness, bias, and generalizability across sites and subgroups (fairness/equity reporting).
- Data and code availability is expected to the extent permitted by patient privacy; deposit code and provide data-access statements, with reproducibility supported where data cannot be shared.
- Observational components should follow STROBE; systematic reviews/meta-analyses should follow PRISMA. Ethics approval and consent for clinical/patient data must be documented.

## Structure & house style

- The Lancet family uses a structured abstract and a defined Lancet article format; re-check current article types (Articles, Health Policy, Viewpoints, Comments) and their length limits on the live site.
- A Research in context panel (evidence before this study / added value / implications) is a Lancet hallmark and is typically required for research articles.
- Reporting-guideline checklists (TRIPOD-AI, CONSORT-AI, SPIRIT-AI, STROBE, PRISMA) are submitted alongside the manuscript as applicable.
- Methods must give enough detail — model architecture, training/validation data provenance, preprocessing, and evaluation protocol — for independent appraisal and, ideally, reproduction.
- Figures should communicate clinical performance and utility (calibration, decision-curve, subgroup) rather than only technical benchmarks; tables report cohort characteristics transparently.
- As an open-access journal, an article-processing charge applies; confirm current APC and licensing (CC BY) terms.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "The Lancet Digital Health information for authors" / "submission guidelines" and follow the current Elsevier/Lancet version.
- Confirm the required reporting guideline(s) and checklists (TRIPOD/TRIPOD-AI, CONSORT-AI, SPIRIT-AI, STROBE, PRISMA) for your study type and prepare them.
- Re-check trial-registration requirements, the Research in context panel format, structured-abstract rules, and current word and reference limits by article type.
- Re-check data-sharing, code-availability, ethics/consent, competing-interests, funding, AI-use disclosure, open-access licensing, and current APC.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence — the clinical question, the clinically meaningful endpoint, and why a digital/AI approach changes care.
- [ ] The model or intervention is externally/independently validated, with calibration and clinically relevant performance reported, not internal metrics alone.
- [ ] The applicable reporting checklist (TRIPOD-AI / CONSORT-AI / SPIRIT-AI / STROBE / PRISMA) is completed and the trial registered if prospective.
- [ ] Cohort representativeness, bias, and subgroup/equity performance are reported and discussed.
- [ ] Data-access statement, code availability, ethics approval, and consent are documented.
- [ ] The Research in context panel is drafted and the manuscript fits the article-type length limits.

## Common desk-reject triggers

- A technically novel model evaluated only on one dataset with internal cross-validation and no external validation or clinical endpoint.
- A digital-intervention or AI trial reported without the relevant CONSORT-AI/SPIRIT-AI standards or without prospective registration.
- A manuscript with no clinically meaningful outcome — performance metrics without demonstrated or credible patient/population impact.
- Missing ethics approval, consent, or data-governance documentation for clinical/patient data.
- A model developed on a non-representative cohort with no assessment of bias, generalizability, or subgroup performance.

## Re-routing decision

- Primary clinical research with broad medical significance where the digital method is one component: Nature Medicine (`nature-medicine`).
- Mechanistic or translational work bridging technology and disease biology toward the clinic: Science Translational Medicine (`science-translational-medicine`).
- Translational or early-clinical medicine studies of broad interest: Cell Reports Medicine (`cell-reports-medicine`).
- A methods- or algorithm-focused paper without clinical validation: a machine-learning or biomedical-informatics methods venue (e.g., a JAMIA-style informatics or ML-methods journal).

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] The Lancet Digital Health
[Topic tags] <2–3 closest topics>
[Method/evidence] <is there a clinically meaningful endpoint with external validation and reporting-standard compliance (TRIPOD-AI/CONSORT-AI/SPIRIT-AI), not technical metrics alone?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <reporting checklist / trial registration / Research-in-context panel / data-code & ethics / open-access APC & licensing>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
