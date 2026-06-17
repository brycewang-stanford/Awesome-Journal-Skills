---
name: lancet-reporting
description: Use to select and apply the correct EQUATOR reporting guideline for a Lancet manuscript — CONSORT for RCTs (with the mandatory flow diagram), STROBE for observational studies, PRISMA for systematic reviews/meta-analyses, SPIRIT for protocols — and to attach the completed checklist and study-flow diagram.
---

# Reporting Guidelines & Flow Diagrams (lancet-reporting)

## When to trigger

- The study type is settled and you need the matching reporting checklist.
- There is no participant flow diagram (CONSORT/PRISMA) in the manuscript.
- A reviewer or editor asks for a completed reporting checklist with page/line references.
- The manuscript mixes endpoints/numbers that the flow diagram should reconcile.

## Pick the guideline by study type (via EQUATOR)

The Lancet requires the appropriate [EQUATOR Network](https://www.equator-network.org/) reporting guideline and a completed checklist on submission.

| Study type | Guideline | Mandatory diagram |
|------------|-----------|-------------------|
| Randomized controlled trial | **[CONSORT](https://www.consort-spirit.org/)** (+ extensions: cluster, non-inferiority, pragmatic, harms, PRO) | **CONSORT flow diagram** (enrollment → allocation → follow-up → analysis) |
| Observational (cohort, case-control, cross-sectional) | **[STROBE](https://www.strobe-statement.org/)** | Participant flow / selection diagram |
| Systematic review / meta-analysis | **[PRISMA](https://www.prisma-statement.org/)** (+ PRISMA-P for protocols) | **PRISMA flow diagram** (records → screened → included) |
| Trial / review **protocol** | **SPIRIT** (trials) / **PRISMA-P** (reviews) | — |
| Diagnostic accuracy | **STARD** | Patient flow |
| Prediction model | **TRIPOD** | — |
| Quality improvement | **SQUIRE** | — |
| Economic evaluation | **CHEERS** | — |

## The flow diagram is mandatory for RCTs and systematic reviews

- [ ] **CONSORT flow diagram** present for every RCT: numbers assessed for eligibility, excluded (with reasons), randomized, allocated, lost to follow-up/discontinued (with reasons), and analyzed in each arm.
- [ ] **PRISMA flow diagram** present for every systematic review/meta-analysis: records identified, duplicates removed, screened, full-text assessed, excluded (with reasons), and included.
- [ ] Every number in the flow diagram **reconciles** with Table 1, the analysis populations, and the abstract.

## Checklist discipline

- [ ] Complete the official checklist for the chosen guideline.
- [ ] Map each item to a **page and line** in the manuscript (editors and reviewers check this).
- [ ] Use the correct **extension** (e.g., CONSORT cluster for cluster-randomized trials; CONSORT harms for adverse-event reporting; CONSORT-PRO for patient-reported outcomes).
- [ ] Submit the checklist as a supplementary file.

## Equity-relevant reporting

- Apply equity-focused extensions where relevant (e.g., **PRISMA-Equity**, **CONSORT-Equity** considerations) and the **PROGRESS-Plus** framework for reporting equity-relevant participant characteristics.
- Coordinate sex/gender and race/ethnicity reporting with `lancet-ethics` (SAGER guidelines).

## What Lancet editors and reviewers expect from reporting compliance

A completed checklist is a screening gate at The Lancet, not a formality. Editors and the statistical reviewer cross-read the flow diagram against Table 1 and the analysis populations; a discrepancy reads as a transcription error or selective reporting, and unexplained attrition is where bias hides. Desk-reject-adjacent patterns: no flow diagram for an RCT or review (effectively mandatory); base CONSORT where a cluster/non-inferiority extension fits; a checklist that says "throughout" instead of page/line; and numbers that do not reconcile. Confirm any current formatting requirement against the journal's author guidelines.

## Worked micro-example (illustrative numbers — not real data)

A hypothetical multi-country, individually randomised trial of an oral therapy versus placebo across 14 sites in 5 low- and middle-income countries.

```
Guideline: CONSORT 2010 + CONSORT-Harms; checklist page/line-mapped as a supplement.
CONSORT flow diagram (illustrative):
  Assessed 5 312 -> Excluded 1 108 (ineligible 842; declined 201; other 65)
  Randomised 4 204 -> intervention 2 102 / placebo 2 102
  Lost to follow-up: intervention 51, placebo 58 (reasons listed)
  Analysed (ITT): 2 102 / 2 102
Reconciliation: 4 204 = Table 1 total = abstract Findings denominator. PASS.
```

The reporting pass is the reconciliation: 4 204 appears identically in the diagram, Table 1, and the abstract, and every exclusion and dropout carries a reason.

## Reviewer-pushback patterns and the venue-specific fix

- *"The reporting checklist is incomplete / not page-referenced."* → Complete the official EQUATOR checklist and map each item to a page and line; resubmit as a supplement.
- *"This is a cluster-randomised trial but reported under standard CONSORT."* → Switch to CONSORT-Cluster with cluster-level flow and intracluster correlation reporting.
- *"Flow-diagram numbers do not match the analysis populations."* → Rebuild the diagram so randomised, analysed, and Table 1 totals reconcile; explain any gap.
- *"Equity-relevant characteristics are not reported."* → Add PROGRESS-Plus variables and a PRISMA-Equity/CONSORT-Equity lens; coordinate with `lancet-ethics`.

## Output format

```
【Study type】 RCT / observational / systematic review / protocol / other
【Guideline + extension】 CONSORT(+ext) / STROBE / PRISMA(+ext) / SPIRIT / STARD / TRIPOD / ...
【Flow diagram】 present & required? CONSORT / PRISMA / N/A  → gaps
【Flow numbers reconcile】 with Table 1 + analysis populations + abstract? yes/no
【Checklist】 completed + page/line mapped? yes/no
【Equity reporting】 PROGRESS-Plus / equity extension applied where relevant? yes/no
【Next】 lancet-statistics
```

## Anti-patterns

- **Do not** submit an RCT without a CONSORT flow diagram, or a systematic review without a PRISMA one.
- **Do not** leave flow-diagram numbers that disagree with the analysis populations or Table 1.
- **Do not** submit a checklist with "see manuscript" instead of specific page/line references.
- **Do not** use the base guideline when an extension fits the design better (cluster, non-inferiority, pragmatic, harms).
