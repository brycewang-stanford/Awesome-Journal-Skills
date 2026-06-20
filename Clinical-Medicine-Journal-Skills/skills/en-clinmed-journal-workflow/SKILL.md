---
name: en-clinmed-journal-workflow
description: Use when deciding which English specialty clinical-medicine journal skill to invoke next, comparing fit across the 30-journal clinical-medicine roadmap, or routing a manuscript before venue-specific re-framing. Routes by specialty, study design (RCT / observational / diagnostic-accuracy / review), and evidence strength, and flags trial registration and the reporting checklist as prerequisites.
---

# Clinical-medicine journal workflow (en-clinmed-journal-workflow)

## Purpose

This is the routing skill for the specialty-clinical bundle. It does not replace a
single-journal profile; it first classifies the study by **specialty, study design,
and evidence strength**, then routes into the matching per-journal skill for fit and
re-framing. It is a sibling to `en-natsci-journal-workflow` (which holds the general
big-four and broad-specialty clinical flagships). These skills are venue-fit aids
only — not clinical, diagnostic, or regulatory advice.

## Ask four things first

1. **Specialty:** internal/general medicine, oncology, cardiology, neurology,
   pediatrics, psychiatry, surgery, respiratory/critical care, nephrology,
   endocrinology/diabetes, hepatology/GI, allergy/immunology, rheumatology, stroke,
   radiology, anesthesiology, obstetrics/gynecology, or urology?
2. **Study design:** randomized controlled trial, prospective cohort / observational
   study, diagnostic-accuracy study, systematic review / meta-analysis, guideline /
   consensus, mechanistic/translational study, or narrative/invited review?
3. **Evidence strength & impact:** practice-changing definitive trial, an important
   but not definitive result, a hypothesis-generating or exploratory finding, or a
   synthesis?
4. **Audience:** the whole specialty (a society/JAMA-Network/Lancet specialty
   flagship), a sub-specialty community, or a general-medicine audience (route up to
   the big-four in the natural-science bundle)?

## Quick routing

| Manuscript signature | Prefer skill |
|---|---|
| General internal-medicine trial / comparative effectiveness | `jama-internal-medicine` |
| Oncology clinical trial / practice-changing | `jama-oncology` / `annals-of-oncology` |
| Authoritative oncology review | `nature-reviews-clinical-oncology` |
| Cardiology specialty study | `jama-cardiology` |
| Neurology clinical study | `jama-neurology` |
| Neuroscience-to-clinical brain disorders, mechanism + clinical | `brain` |
| Cerebrovascular / stroke | `stroke` |
| Pediatrics | `jama-pediatrics` |
| Psychiatry / mental-health (clinical or population) | `jama-psychiatry` / `the-lancet-psychiatry` |
| Surgery / perioperative outcomes | `jama-surgery` |
| Respiratory / pulmonary / critical-care medicine | `the-lancet-respiratory-medicine` / `american-journal-of-respiratory-and-critical-care-medicine` |
| Intensive / critical care | `critical-care-medicine` |
| Diabetes / endocrinology (clinical or population) | `the-lancet-diabetes-and-endocrinology` / `journal-of-clinical-endocrinology-and-metabolism` / `diabetologia` |
| Nephrology / kidney disease | `journal-of-the-american-society-of-nephrology` / `kidney-international` |
| Liver disease / hepatology | `journal-of-hepatology` / `hepatology` |
| Gastroenterology (clinical) | `american-journal-of-gastroenterology` |
| Allergy / clinical immunology | `journal-of-allergy-and-clinical-immunology` |
| Rheumatology / autoimmune | `arthritis-and-rheumatology` |
| Public-health / population-health intervention | `the-lancet-public-health` |
| Diagnostic imaging / imaging AI | `radiology` |
| Anesthesiology / perioperative medicine | `anesthesiology` |
| Obstetrics / gynecology | `american-journal-of-obstetrics-and-gynecology` |
| Urology | `european-urology` |

## Sibling-journal disambiguation

| Confusable targets | Decision rule |
|---|---|
| A JAMA Network specialty title vs the general big-four (NEJM/JAMA/Lancet/BMJ in the natural-science bundle) | A practice-changing, broadly significant trial may belong at the general venue; a strong specialty-relevant result routes to the JAMA Network / Lancet specialty title. |
| `jama-oncology` vs `annals-of-oncology` | Route by audience and society fit (JAMA Network vs ESMO) and re-check current scopes; both take high-quality oncology clinical research. |
| `journal-of-the-american-society-of-nephrology` vs `kidney-international` | Both are top nephrology venues (ASN vs ISN); route by society fit and emphasis and re-check current scopes. |
| `journal-of-hepatology` vs `hepatology` | EASL vs AASLD flagships; route by society fit and audience and re-check current scopes. |
| `the-lancet-psychiatry` vs `jama-psychiatry` | Both are top psychiatry venues; route by family fit (Lancet vs JAMA Network) and the framing/audience. |
| Specialty journal vs `the-lancet-public-health` | A population-health/policy intervention routes to public health; a disease-specific clinical result routes to the specialty journal. |

## Decision rules

- **Match the reporting guideline before submitting.** RCT → CONSORT + prospective
  trial registration (number in the manuscript); systematic review → PRISMA;
  observational → STROBE; diagnostic accuracy → STARD. These are prerequisites, not
  nice-to-haves, at these venues.
- **Evidence hierarchy sets the venue.** A definitive randomized trial outranks an
  observational study, which outranks a single-center case series; route the design to
  the venue that expects that level of evidence.
- **Specialty fit beats prestige.** A strong nephrology or rheumatology result is often
  better served by the society specialty flagship than by a general journal that will
  desk-reject for limited general interest.
- **Review vs primary.** Nature Reviews Clinical Oncology and similar are largely
  invited/commissioned — propose, do not submit unsolicited primary data.
- **Ethics, consent, and disclosures** (IRB approval, informed consent, ICMJE COI and
  authorship, data sharing) are gating items at every clinical venue.
- Always enter the single-journal skill's official-submission checklist before
  submitting; never rely on a stale template.

## Output format

```text
[Top journal skill] <skill-name>
[Alt 1] <skill-name> (reason)
[Alt 2] <skill-name> (reason)
[Do not submit to] <journal> (one-line mismatch reason)
[Study design / reporting guideline] <RCT-CONSORT / cohort-STROBE / review-PRISMA / diagnostic-STARD>
[Biggest current gap] evidence-strength / specialty-fit / registration / reporting-checklist / ethics / official requirements
[Next step] invoke <skill-name> for single-venue fit and re-framing
```
