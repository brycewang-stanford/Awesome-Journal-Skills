---
name: jama-internal-medicine
description: Use when targeting JAMA Internal Medicine or deciding whether an internal-medicine clinical study fits this venue. Encodes the journal's fit, the clinical-evidence and methodological-rigor bar, reporting-guideline and trial-registration requirements, JAMA Network house style, official-submission re-check, and desk-reject heuristics. Venue-fit aid only, not clinical advice.
---

# JAMA Internal Medicine (jama-internal-medicine)

## Journal positioning

JAMA Internal Medicine is a JAMA Network specialty journal for clinical research,
evidence synthesis, and health-policy scholarship relevant to the practice of adult
internal medicine. It favors rigorous, clinically important work — randomized trials,
high-quality comparative-effectiveness and observational studies, and analyses that
challenge low-value care or inform practice and policy — with a strong emphasis on
methodological soundness and direct relevance to patient care and clinical decision
making. Underpowered single-center studies, descriptive case series, and analyses
with no clear practice implication are a weak fit. This skill is a **fit /
venue-selection / re-framing** aid; it is not clinical or regulatory advice and does
not replace the journal's current instructions for authors. Before submitting,
re-check the live JAMA Internal Medicine author instructions.

## When to trigger

- The author names JAMA Internal Medicine for an internal-medicine clinical or
  health-services study and wants a fit/framing check.
- A clinical study must be re-framed around a clear practice-changing or
  policy-relevant question for a general internal-medicine readership.
- The author is choosing between JAMA Internal Medicine, JAMA, and a subspecialty
  journal.
- The author needs the journal's reporting-guideline, registration, and desk-reject
  expectations.

## Scope & topic fit

- Randomized clinical trials in adult internal medicine, including pragmatic and
  de-implementation ("less is more") trials.
- Comparative-effectiveness, cohort, and large database studies with rigorous design
  and confounding control.
- Diagnostic, screening, and prognostic studies with clinically meaningful endpoints.
- Health-policy, quality, value-of-care, and health-services research relevant to
  internal medicine.
- Systematic reviews and meta-analyses that answer a focused clinical question.

## Method & evidence bar

- Studies must be adequately powered with prespecified, patient-centered primary
  outcomes; surrogate-only endpoints need strong justification.
- The applicable reporting guideline must be followed and its checklist supplied:
  CONSORT for trials, STROBE for observational studies, PRISMA for systematic reviews.
- Trials require prospective registration; the trial-registration number and a
  protocol/statistical-analysis plan are expected.
- Observational claims must address confounding, bias, and missing data explicitly;
  causal language must match the design.
- Effect estimates should be reported with confidence intervals and absolute as well
  as relative measures; clinical (not just statistical) significance must be argued.

## Structure & house style

- JAMA Network format with a structured abstract and a Key Points box; re-check
  current article types (Original Investigation, Research Letter, etc.) and limits on
  the live guide.
- The introduction frames a focused clinical question and its importance; the
  discussion states the practice or policy implication plainly.
- Tables/figures follow JAMA Network statistical-reporting standards; a CONSORT/STROBE
  flow diagram is expected where applicable.
- Supplements carry the protocol, full statistical methods, and additional analyses.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and
  `../../resources/official-source-map.md`; start from the ICMJE and JAMA Network
  anchors, then cite the current JAMA Internal Medicine page you checked.
- Search the live site for "JAMA Internal Medicine instructions for authors" and follow
  the current version.
- Re-check article types and word/reference/table limits, structured-abstract and Key
  Points format, and the JAMA Network statistical-reporting requirements.
- Confirm trial registration, the reporting checklist (CONSORT/STROBE/PRISMA), data-sharing
  statement, and protocol/SAP submission.
- Re-check IRB/ethics and consent statements, ICMJE authorship and conflict-of-interest
  disclosure, funding, and AI-use disclosure.
- If the live official instructions conflict with this skill, the official instructions
  win.

## Pre-submission self-check

- [ ] The study answers a focused, clinically important question with a clear practice or policy implication.
- [ ] The primary outcome is prespecified and patient-centered; the study is adequately powered.
- [ ] The correct reporting checklist (CONSORT/STROBE/PRISMA) is completed and attached.
- [ ] Trials are prospectively registered with the number in the manuscript; protocol/SAP provided.
- [ ] Confounding, bias, and missing data are addressed, and causal language matches the design.
- [ ] IRB/consent, ICMJE disclosures, and a data-sharing statement are prepared.

## Common desk-reject triggers

- Underpowered or single-center studies with limited generalizability and no clear practice change.
- Observational analyses with inadequate confounding control or overstated causal claims.
- Missing trial registration, protocol, or the required reporting checklist.
- Surrogate-only endpoints presented as clinically definitive.
- Narrow subspecialty interest better served by a specialty journal, or limited general-internal-medicine relevance.

## Re-routing decision

- Practice-changing, broadly significant trial → general medicine (`jama` / NEJM / The Lancet in the natural-science bundle).
- Oncology focus → `jama-oncology` / `annals-of-oncology`.
- Cardiology / neurology / nephrology subspecialty → `jama-cardiology` / `jama-neurology` / `journal-of-the-american-society-of-nephrology`.
- Population-health or policy intervention → `the-lancet-public-health`.
- Psychiatry / surgery focus → `jama-psychiatry` / `jama-surgery`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] JAMA Internal Medicine
[Specialty tags] <2–3 closest internal-medicine topics>
[Study design / reporting guideline] <RCT-CONSORT / cohort-STROBE / review-PRISMA>
[Method/evidence] <does power, design, and registration clear the bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / registration / checklist / ethics / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
