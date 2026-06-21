---
name: jedpsych-open-science-and-transparency
description: Use when meeting the Journal of Educational Psychology's open-science requirements — the Transparency and Openness subsection stating data/materials/analysis-code availability with persistent identifiers, JARS-compliant reporting, preregistration disclosure (encouraged, not mandatory), and Open Science Badges. Prepares compliance for masked review; it does not waive requirements.
---

# Open Science & Transparency (jedpsych-open-science-and-transparency)

The Journal of Educational Psychology follows APA's transparency-and-openness framework. Manuscripts
include a **Transparency and Openness subsection** that states whether **data, materials, and analysis
code** are deposited in **trusted repositories with persistent identifiers** — or states that they are
unavailable (with reasons). Reporting follows **JARS**; **preregistration is encouraged but not
mandatory** (disclose status and link); and **Open Science Badges** (Open Data, Open Materials,
Preregistered) are available with a signed disclosure form (检索于 2026-06；以官网为准). Prepare this
early — and keep every shared link **anonymized** for masked review.

## When to trigger

- Building data/materials/code deposits and the Transparency and Openness subsection
- Deciding whether (and how) to claim that data cannot be shared
- Disclosing and linking a preregistration / analysis plan
- Deciding whether to apply for Open Science Badges
- A reviewer or editor flagged transparency, reporting standards, or reproducibility

## What JEP expects (verify current wording on the official page)

1. **Transparency and Openness subsection.** State, for **data**, **materials**, and **analysis code**,
   whether each is openly available, available under restriction, or unavailable — and where (repository +
   **persistent identifier / DOI**). If something is not shared, say so and why.
2. **JARS reporting standards.** Follow the APA Journal Article Reporting Standards for your design
   (quantitative, qualitative, or mixed methods), and **JARS-REC** for race, ethnicity, and culture
   reporting. Meta-analyses follow the meta-analysis reporting standards.
3. **Preregistration (encouraged).** Disclose whether the study was preregistered and provide the registry
   link; report deviations from the plan. Preregistration is weighed favorably but is not required.
4. **Persistent identifiers.** Use trusted repositories (OSF, ICPSR, Dataverse, Zenodo) with DOIs — not
   transient personal links.
5. **Open Science Badges.** Optionally earn Open Data, Open Materials, and Preregistered badges; each
   requires a **signed badge disclosure form** submitted as supplemental material.
6. **Anonymize for masked review.** Repository and preregistration links must not reveal author identity
   (use anonymized views); strip identifying metadata.

## Build-it-right checklist

- [ ] **Data** deposited with a **DOI** (or restricted-access statement + reason); **codebook** included
- [ ] **Analysis code** deposited; results regenerate in a fresh session
- [ ] **Materials** (instruments, intervention protocol, stimuli) deposited with a DOI (or license-limited
  statement)
- [ ] **Transparency and Openness subsection** drafted covering data, materials, and code availability
- [ ] **Preregistration** disclosed and linked (anonymized); deviations reported
- [ ] **JARS / JARS-REC** checklist walked for your design; participant/context reporting complete
- [ ] **Badge disclosure form** signed if applying for Open Science Badges
- [ ] Shared links **anonymized** for masked submission; identifying metadata stripped

## Restricted data (educational settings — do it honestly)

- Student data are frequently protected (FERPA, IRB, district agreements). If data cannot be fully shared,
  state exactly **what** is withheld, **why**, and **how** others can access or approximate it (application
  path, de-identified/synthetic data, secure enclave, code release). Document this in the subsection;
  unjustified opacity counts against the paper.

## Transparency and Openness subsection — worked draft (illustrative)

A model statement for the cluster-randomized reading trial. Confirm the exact required headings/wording
against the journal's current submission guidelines.

```
Transparency and Openness
Data:        De-identified student-level data for the trial are available
             at OSF (DOI 10.XXXX/osf.io/abcde) with a codebook; raw
             identifiable data are governed by the district agreement and
             available via application (path described).
Materials:   The intervention protocol, fidelity rubric, and comprehension
             measures (license permitting) are deposited (DOI 10.XXXX/osf.io/fghij).
Analysis:    Analysis code (R, lme4 / lavaan) reproduces all reported values
             in a fresh session; a run log is included (DOI 10.XXXX/osf.io/klmno).
Preregistration: The design, hypotheses, and analysis plan were preregistered
             before data collection (osf.io/pqrst); one ATI analysis is
             reported as exploratory. Reporting follows JARS (and JARS-REC).
```

## Transparency-readiness decision table

| Situation | Editorial read | What to deposit / state |
|-----------|----------------|-------------------------|
| Fully shareable de-identified data + materials | strong baseline | DOIs for data, materials, code + run log; consider badges |
| Protected student records (FERPA/IRB/district) | acceptable if justified | de-identified/synthetic data + gated access path; share code |
| Proprietary/licensed instrument | partial | share what license allows; cite source; share scoring code |
| Secondary / third-party dataset | acceptable with provenance | link source, share derivation code, document version |
| "Available on request" | reads as weak | replace with a persistent DOI or a documented access path |

## Reviewer / editor pushback and the venue fix

- "No DOI, just a personal link" → swap transient links for persistent identifiers before the masked
  submission goes out.
- "Subsection says available but the repo is empty" → deposit first, draft the subsection from live DOIs.
- "Preregistration deviates and you didn't flag it" → add a deviations note; relabel post hoc as
  exploratory; keep confirmatory/exploratory consistent end to end.
- "Repository page reveals author identity" → use anonymized views for masked review.
- "JARS participant/context reporting incomplete" → complete the JARS / JARS-REC items for your design.

## Anti-patterns

- Omitting or burying the Transparency and Openness subsection
- Personal/transient links instead of persistent identifiers
- Treating restricted student data as a reason to share nothing (share code + access path)
- Claiming a preregistration that does not match the analyses, or hiding deviations
- Identifying author info in repository/preregistration links during masked review

## Output format

```
【Data】deposited + DOI + codebook (or justified restriction)? [Y/N]
【Materials】deposited + DOI (or license statement)? [Y/N]
【Analysis code】deposited + fresh-session reproducible? [Y/N]
【Transparency subsection】drafted covering data/materials/code? [Y/N]
【Preregistration】disclosed + linked (anonymized) + deviations noted? [Y/N/NA]
【JARS / JARS-REC】walked for this design? [Y/N]
【Anonymized】links + metadata for masked review? [Y/N]
【Next】jedpsych-review-process
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — OSF, ICPSR, Dataverse, Zenodo, JARS checklists, preregistration templates, DOIs
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — Transparency and Openness, JARS, preregistration, and Open Science Badge policy
