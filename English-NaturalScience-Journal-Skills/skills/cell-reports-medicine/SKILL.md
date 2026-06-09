---
name: cell-reports-medicine
description: Use when targeting Cell Reports Medicine (Cell Rep Med) or deciding whether a translational or clinical manuscript with mechanistic depth fits this open-access Cell Press venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Cell Reports Medicine (cell-reports-medicine)

## Journal positioning

Cell Reports Medicine, an open-access journal from Cell Press and the medical sister of Cell Reports, publishes translational and clinical research with mechanistic depth across the full spectrum of human disease. Its defining character is the pairing of clinical or translational relevance with rigorous biological insight: it favors work that does not merely report a clinical observation or a candidate biomarker, but connects it to mechanism, validates it across systems, and moves toward patient impact. The journal spans oncology, immunology, metabolism, infectious disease, neurology, cardiovascular medicine, and more, and welcomes clinical-trial results, biomarker and target discovery, disease-mechanism studies in human samples, and translational technology — provided the evidence is strong and the advance is meaningful for human health. Readership is the broad translational and clinical research community.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Cell Reports Medicine (Cell Press) site.

## When to trigger

- The author names Cell Reports Medicine as the target for a translational or clinical study with mechanistic depth.
- A study links a clinical observation, biomarker, or therapeutic response to an underlying biological mechanism and the author is choosing between Cell Reports Medicine and `nature-medicine` or `science-translational-medicine`.
- A solid clinical or translational result has broad interest but may not reach the top general medical journals, and the author wants a high-quality open-access Cell Press venue.
- The author needs the journal's scope, evidence bar, and desk-reject criteria before submission.

## Scope & topic fit

- Translational disease mechanism: studies in human samples (patient cohorts, biopsies, organoids, primary cells) that define how a disease process works and why it matters clinically.
- Biomarker and target discovery with validation: candidate biomarkers or therapeutic targets shown to be robust, with mechanistic and cohort-level support.
- Clinical and interventional studies: trials, observational studies, and real-world analyses, especially when paired with mechanistic or correlative biology.
- Therapeutics and pharmacology: mechanism of action, resistance, combination rationale, and translational pharmacodynamics.
- Immunotherapy, precision oncology, metabolic and immune-mediated disease, infectious disease, and neurological/cardiovascular medicine.
- Translational technologies (diagnostics, delivery, computational/AI clinical tools) when validated and clinically meaningful.

## Method & evidence bar

- Both relevance and rigor are required: a clinically interesting finding must be supported by strong, well-controlled evidence and, where the claim demands it, mechanistic causality (perturbation, functional validation), not correlation alone.
- Human-relevant validation strengthens claims: patient cohorts, primary samples, organoids, or appropriate in vivo models beyond cell lines.
- Clinical studies must report rigorously: pre-registration where applicable (e.g., ClinicalTrials.gov), CONSORT/STROBE-style reporting, defined endpoints, appropriate statistics, and effect sizes with confidence intervals.
- Cohort and biomarker claims require adequate sample size, and ideally independent validation cohorts; statistical reporting and multiple-testing handling are scrutinized.
- Reagent, antibody, and cell-line validation and ethics oversight (IRB/IACUC, informed consent) must be complete.
- Data and code must be deposited per Cell Press policy: omics/sequencing data in public repositories (GEO, SRA, PRIDE, dbGaP/EGA for controlled data), and analysis code made available (e.g., GitHub/Zenodo).

## Structure & house style

- Cell Press article formats apply (Article and shorter Report types, plus front-matter) — re-check current article types and limits on the live site.
- The abstract and introduction must state the clinical/translational question and the advance concisely for a broad biomedical readership, with patient relevance explicit early.
- Figures must integrate clinical and mechanistic evidence: cohort/clinical panels alongside functional or molecular validation; each panel must justify its inclusion.
- A STAR Methods (or current Cell Press methods format) section is expected, with complete reagent, cohort, and statistical detail enabling reproduction; supplementary materials carry additional data.
- Key Resources and reporting-standard tables are expected; the writing is dense and significance-driven.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "Cell Reports Medicine author guidelines" and follow the current Cell Press version, including article-type limits and STAR Methods format.
- Re-check data-availability and code-availability requirements; confirm accepted repositories (GEO/SRA/PRIDE; dbGaP/EGA for controlled-access human data) and code deposition.
- Re-check clinical-trial registration, CONSORT/STROBE reporting, ethics/IRB/IACUC approvals, and informed-consent statements.
- Re-check reagent/antibody validation, statistics reporting, competing-interests, funding, and AI-use disclosure; confirm preprint policy (medRxiv/bioRxiv posting is generally compatible) and open-access/APC terms.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence — the translational/clinical advance and the mechanism that supports it, and why it matters for patients.
- [ ] Evidence is strong and controlled; causal claims are backed by functional validation, not correlation alone.
- [ ] Clinical/cohort work meets reporting standards (registration, CONSORT/STROBE, endpoints, statistics) and ideally includes independent validation.
- [ ] Human-relevant validation (cohorts, primary samples, organoids, in vivo) supports the central claim.
- [ ] Required data are deposited (including controlled-access human data where applicable) and analysis code is available; accession details are ready.
- [ ] Ethics approvals, consent, reagent validation, and the positioning against recent literature are complete.

## Common desk-reject triggers

- A clinical observation or biomarker report with no mechanistic insight or independent validation where the claim requires it.
- A cell-line-only mechanistic study with no human-relevant or in vivo validation despite a clinical claim.
- An underpowered cohort or trial, or clinical work missing registration and standard reporting.
- An incremental translational result lacking broad significance for human health.
- Missing data deposition, ethics/consent documentation, or reagent validation.

## Re-routing decision

- A landmark clinical advance or practice-changing result for a top general medical audience: `nature-medicine`.
- A translational study where a novel mechanism-to-therapy bridge is the headline contribution at the highest tier: `science-translational-medicine`.
- A basic disease-mechanism study without a clinical/translational endpoint: a Cell Press primary journal (`cell`, `cell-metabolism`, `cancer-cell`) by topic.
- A primarily clinical trial without mechanistic biology: a specialty clinical journal.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Cell Reports Medicine
[Topic tags] <2–3 closest disease/translational topics>
[Method/evidence] <is the clinical/translational claim rigorous, mechanistically supported, and validated in human-relevant systems?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article-type limits / data-code deposition / trial registration & reporting / ethics & consent / disclosure / preprint & open-access>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
