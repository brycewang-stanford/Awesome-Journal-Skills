# External Tools & Resources for NEJM Submissions

A working list of registries, standards, software, and references useful when preparing a clinical manuscript for *The New England Journal of Medicine* (NEJM). Always confirm specifics against the current [NEJM Author Center](https://www.nejm.org/author-center) and the [ICMJE Recommendations](http://www.icmje.org/recommendations/).

## 1. Trial registration & registries

| Need | Resource |
|------|----------|
| Primary trial registration (US) | [ClinicalTrials.gov](https://clinicaltrials.gov/) |
| WHO network of primary registries | [WHO ICTRP](https://www.who.int/clinical-trials-registry-platform) |
| EU trials | [EU Clinical Trials Register / CTIS](https://euclinicaltrials.eu/) |
| UK / other regional | [ISRCTN registry](https://www.isrctn.com/) |
| Systematic-review protocol registration | [PROSPERO](https://www.crd.york.ac.uk/prospero/) |

> ICMJE requires **prospective** registration **before the first patient is enrolled**. The registration number is reported in the abstract and Methods. Retrospective registration is generally disqualifying for an Original Article.

## 2. Reporting guidelines (EQUATOR Network)

- [EQUATOR Network](https://www.equator-network.org/) — index of reporting guidelines by study type.
- [CONSORT](https://www.consort-spirit.org/) — RCTs; 25-item checklist **+ participant flow diagram** (and extensions: cluster, non-inferiority, pragmatic, harms).
- [STROBE](https://www.strobe-statement.org/) — observational studies (cohort, case-control, cross-sectional).
- [PRISMA](https://www.prisma-statement.org/) — systematic reviews and meta-analyses (+ selection flow diagram).
- [SPIRIT](https://www.consort-spirit.org/) — trial protocols.
- [CARE](https://www.care-statement.org/) — case reports.
- [STARD](https://www.equator-network.org/reporting-guidelines/stard/) — diagnostic accuracy studies.

## 3. Editorial policy & integrity standards

- [ICMJE Recommendations](http://www.icmje.org/recommendations/) — authorship, disclosures, data sharing, overlapping publication.
- [ICMJE disclosure form](http://www.icmje.org/disclosure-of-interest/) — competing-interests reporting for all authors.
- [Declaration of Helsinki (WMA)](https://www.wma.net/policies-post/wma-declaration-of-helsinki/) — ethical principles for human-subjects research.
- [ICH Good Clinical Practice (GCP)](https://www.ich.org/page/efficacy-guidelines) — trial conduct standard.
- [CRediT](https://credit.niso.org/) — contributor-role taxonomy.
- [ORCID](https://orcid.org/) — author identifiers.
- [GRADE](https://www.gradeworkinggroup.org/) — rating certainty of evidence and strength of recommendations.
- [COPE](https://publicationethics.org/) — publication-ethics guidance and flowcharts.

## 4. Data management & sharing

- [REDCap](https://www.project-redcap.org/) — secure clinical data capture.
- Individual-participant-data sharing: [Vivli](https://vivli.org/), [YODA Project](https://yoda.yale.edu/), [ClinicalStudyDataRequest.com](https://www.clinicalstudydatarequest.com/).
- De-identified datasets / general repositories: [Dryad](https://datadryad.org/), [Zenodo](https://zenodo.org/), [Figshare](https://figshare.com/).
- De-identification standards: HIPAA Safe Harbor; remove all 18 identifiers from data and images.

## 5. Statistics & reproducibility

- R ([survival](https://cran.r-project.org/package=survival), [survminer](https://cran.r-project.org/package=survminer) for Kaplan–Meier, [meta](https://cran.r-project.org/package=meta)/[metafor](https://www.metafor-project.org/) for meta-analysis, [tableone](https://cran.r-project.org/package=tableone) for Table 1 with standardized differences).
- Stata ([stcox](https://www.stata.com/), `sts graph` for K–M, `meta` suite, `table1`), SAS for regulated-trial analyses.
- Python ([lifelines](https://lifelines.readthedocs.io/) for survival, [statsmodels](https://www.statsmodels.org/)).
- Sample size / power: [PASS](https://www.ncss.com/software/pass/), [G*Power](https://www.psychologie.hhu.de/arbeitsgruppen/allgemeine-psychologie-und-arbeitspsychologie/gpower).
- Reproducibility: record software versions, seeds, and analysis code; share the SAP.

## 6. References & writing

- Reference managers: [Zotero](https://www.zotero.org/), [EndNote](https://endnote.com/) — use an **NEJM / Vancouver (ICMJE)** style; verify the author cutoff and NLM abbreviations on a final pass.
- Journal abbreviations: [NLM Catalog](https://www.ncbi.nlm.nih.gov/nlmcatalog/journals).

## 7. Useful pages

| Page | URL |
|------|-----|
| NEJM Author Center | https://www.nejm.org/author-center |
| NEJM new-manuscripts guidance | https://www.nejm.org/author-center/new-manuscripts |
| ICMJE Recommendations | http://www.icmje.org/recommendations/ |
| ClinicalTrials.gov | https://clinicaltrials.gov/ |
| EQUATOR Network | https://www.equator-network.org/ |

## 8. Notes

1. **Single-blind** review is typical at NEJM — do not anonymize unless instructed.
2. A **statistical reviewer** is commonly involved; expect rigorous methods scrutiny and be ready to re-run analyses with CIs.
3. NEJM publishes the **protocol and statistical analysis plan** with trials — keep them submission-ready and dated.
4. NEJM enforces an **embargo / Ingelfinger** policy on prior dissemination — coordinate any press and check the policy before posting or presenting.
5. The **data-sharing statement** is required for clinical trials (ICMJE) — decide what/when/to-whom/how before submission.
