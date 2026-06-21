# External Tools & Resources for Journal of Educational Psychology Submissions

Software, repositories, and packages useful when preparing a *Journal of Educational Psychology* (JEP, APA)
submission. JEP is an **empirical educational-psychology** journal whose evidence comes from classroom/
school experiments, randomized field trials, quasi-experiments, longitudinal studies, and **multilevel/SEM/
growth** models of students nested in classes and schools. It enforces **APA 7th** style, **masked
review**, **JARS** reporting, and a **Transparency and Openness** subsection (data + materials + analysis
code with persistent identifiers). Tools below support those norms. Verify any journal-specific policy in
[`official-source-map.md`](official-source-map.md).

## 1. Power & sample-size justification (for NESTED designs)
| Tool | Use |
|------|-----|
| **PowerUpR** (R) + the PowerUp! framework | Power / minimum detectable effect size (MDES) for cluster-randomized and multisite trials with covariates |
| **Optimal Design** (software) | Power for group-randomized and longitudinal designs |
| **`simr`** (R) | Simulation-based power for mixed/multilevel models |
| **G\*Power** | Power for simpler t-test/ANOVA/regression components |
| Monte Carlo power in **Mplus** / **lavaan** | Power for SEM, mediation, and growth models |

> Power at the **level of randomization** (classrooms/schools), using the ICC and covariate adjustment —
> the central JEP design requirement (see `jedpsych-study-design`).

## 2. Multilevel, SEM & growth modeling
### R (dominant)
- Multilevel: `lme4`, `nlme`, `lmerTest`, `glmmTMB`; Bayesian `brms`
- SEM / mediation / growth: `lavaan`, `OpenMx`; multilevel mediation via `lavaan` / `mediation`
- Effect sizes + uncertainty: `effectsize`, `MOTE`, `emmeans`, `marginaleffects`, `parameters`
- Meta-analysis (for the occasional synthesis): `metafor`, `robumeta` (robust variance estimation)
- Missing data: `mice` (multiple imputation), FIML via `lavaan`/`lme4`
### Commercial / other
- **Mplus** (multilevel SEM, growth mixture, complex survey), **HLM**, **Stata** (`mixed`, `gsem`), **SAS** (`PROC MIXED`/`GLIMMIX`), **SPSS** (MIXED)

## 3. Preregistration & registered analysis plans
| Tool | Use |
|------|-----|
| **OSF Registries** (osf.io) | Preregister hypotheses, design, and analysis plan; mint a DOI |
| **AsPredicted** | Lightweight preregistration |
| **Registry of Efficacy and Effectiveness Studies (REES)** | Registration tailored to education trials |
| Secondary-data preregistration templates | For confirmatory analyses of existing datasets |

> Preregistration is **encouraged, not mandatory** at JEP — disclose status and link it (anonymized for
> masked review).

## 4. Open data, materials & persistent identifiers
| Repository | Use |
|------------|-----|
| **OSF** (osf.io) | Data, materials, analysis code, codebooks; component DOIs; anonymized view for masked review |
| **ICPSR** (incl. its education data archives) | Archived, often access-controlled education datasets with DOIs |
| **Harvard Dataverse** | Datasets with DOIs |
| **Zenodo / figshare** | General-purpose data/material archiving with DOIs |
| **GitHub + Zenodo release** | Versioned analysis code with a citable DOI |

> JEP requires **persistent identifiers (DOIs)** for shared data/materials/code and a **Transparency and
> Openness** subsection; for protected student data (FERPA/IRB/district), share de-identified/synthetic
> data + a documented access path and the analysis code.

## 5. Reporting standards (required)
- **APA JARS** — quantitative, qualitative, and mixed-methods reporting standards
- **JARS-REC** — reporting on race, ethnicity, and culture
- Meta-analysis reporting standards (for the occasional synthesis)
- Computational reproducibility check before deposit (fresh-session run of the master script)

## 6. Reproducible reporting, writing & style
- **Quarto / R Markdown / Jupyter** — analysis and manuscript from one reproducible source
- `papaja` (R) — APA 7th-edition manuscripts from R Markdown
- `renv` / `targets` — pin versions and build reproducible pipelines
- **APA Publication Manual, 7th edition**; Zotero/BibTeX with an APA CSL style, EndNote
- **Mask the manuscript** (no author names, grant numbers, IRB/site/district names, first-person self-cites)

## 7. Process & portal
| Item | Note |
|------|------|
| Submission portal | **Editorial Manager**, `editorialmanager.com/edu` |
| Owner / publisher | **American Psychological Association (APA)** |
| Review model | **Masked** (author + reviewer identities masked) |
| Length | body **≤ 12,000 words** (excluding references/tables/figures/appendices) |
| Abstract | **≤ 250 words** |
| Style | **APA 7th edition**, double-spaced |
| Transparency | **Transparency and Openness** subsection (data + materials + code with DOIs); JARS; preregistration encouraged |
| Fee | **No submission fee** (free peer review) |

## 8. Cautions
1. **Verify volatile specifics** (editor, exact word/abstract limits, transparency wording, badge rules)
   on the official APA page — they change.
2. **Power and analyze at the level of randomization** — clustered data modeled as independent is a routine
   JEP rejection reason.
3. **Report effect sizes with CIs and an educational interpretation** (months of progress, percentile,
   variance explained), test the **mechanism**, and follow **JARS / JARS-REC**.
4. **Prepare deposits and DOIs early** — the Transparency and Openness subsection is built from live
   identifiers, anonymized for masked review.
