# External Tools & Resources for Journal of Applied Psychology Submissions

Software, repositories, and packages useful when preparing a *Journal of Applied Psychology* (JAP)
submission. JAP is the **APA flagship of industrial-organizational (I-O) psychology**: it rewards a
genuine **theoretical contribution** plus **rigorous measurement and design** — construct validity,
common-method-variance control, multilevel/nested data, SEM, HLM, mediation/moderation, and
meta-analysis — written in **APA 7th-edition** style and held to the **TOP** open-science framework.
Tools below support those norms. Verify any journal-specific policy in
[`official-source-map.md`](official-source-map.md).

## 1. Preregistration & registered reports
| Tool | Use |
|------|-----|
| **OSF Registries** (osf.io) | Preregister hypotheses, design, measures, and analysis plan; mint a DOI |
| **AsPredicted** | Lightweight preregistration (9 questions) for experiments |
| Secondary-data / archival preregistration templates | For confirmatory analyses on existing organizational data |
| **Registered Reports** templates | If/where JAP offers the route — confirm on the official page (待核实) |

## 2. Open data, materials & persistent identifiers
| Repository | Use |
|------------|-----|
| **OSF** (osf.io) | Data, materials, scales, manipulations, code, codebooks; component DOIs |
| **ICPSR** | Archived social-science / organizational datasets with DOIs and access controls |
| **Harvard Dataverse** | Archived datasets with DOIs |
| **figshare / Zenodo** | General-purpose data/material archiving with DOIs |
| **GitHub + Zenodo release** | Versioned analysis code with a citable DOI |

> JAP expects **persistent identifiers (DOIs)** for shared data/materials/code, a **data-availability
> statement**, and a **prior-use disclosure** when datasets are reused across papers. Prepare early.

## 3. Measurement, construct validity & CMV
- **CFA / measurement invariance**: `lavaan` (R), **Mplus**, `semTools` (R, invariance helpers)
- **Reliability**: `psych` (R; omega, alpha), composite reliability / AVE for SEM
- **Common-method-variance remedies**: marker-variable / CFA-marker technique, ULMC; design-based
  separation (temporal, source, measurement) — plan in advance, not post hoc
- **Aggregation diagnostics**: ICC(1), ICC(2), r_wg(j) for justifying team/unit-level constructs (`multilevel`, `psych`)

## 4. Analysis (effect sizes + CIs are expected)
### R (dominant)
- SEM / path / mediation: `lavaan`, `semTools`, `tidySEM`; bootstrap/Monte Carlo indirect-effect CIs
- Multilevel / HLM: `lme4`, `nlme`, `lmerTest`; multilevel SEM via `lavaan`/`Mplus`
- Mediation/moderation: `mediation`, `interactions`, `bda`; Monte Carlo CI tools (e.g., `RMediation`)
- Meta-analysis: `metafor`, `metaSEM`, `psychmeta` (psychometric meta-analysis with artifact corrections)
- Effect sizes / estimation: `effectsize`, `emmeans`, `parameters`, `marginaleffects`
- Power: `simr` (mixed-model power by simulation), Monte Carlo power for multilevel mediation
### Mplus
- Workhorse for SEM, multilevel SEM, mediation with bootstrap CIs, and complex measurement models
### Python
- `statsmodels`, `pingouin` (effect sizes + CIs), `semopy` (SEM), `pandas`/`numpy`; pin with `requirements.txt`

## 5. Reproducible reporting & disclosure
- **Quarto / R Markdown / Jupyter** — analysis and manuscript from one reproducible source
- `papaja` (R) — APA 7th-edition manuscripts from R Markdown
- Full-disclosure reporting of how sample size was determined and **all** exclusions, conditions, and
  measures (the "21-word-solution" spirit), reported per level of analysis
- Computational reproducibility check before deposit (fresh-session run of the master script)

## 6. Writing, style & format
- **APA Publication Manual, 7th edition** — required style
- `papaja`, Zotero/BibTeX with an APA 7th CSL style, EndNote
- Report effect sizes and CIs, exact p-values, and SEM fit indices; format Table 1 with reliabilities
- **Mask the manuscript** for anonymized review (no author-identifying information; separate title page)

## 7. Process & portal
| Item | Note |
|------|------|
| Submission portal | **Editorial Manager**, `editorialmanager.com/apl` |
| Owner / publisher | **American Psychological Association (APA)** |
| Review model | **Masked (anonymized)** peer review; action-editor model |
| Main types | **Feature Article** (length commensurate with contribution); **Research Report** (tighter, 待核实) |
| Other types | Theory-development, integrative review, qualitative research, meta-analysis |
| Style | **APA 7th edition**; structured abstract (limit 待核实) |
| Open science | **TOP framework** (since 1 Nov 2021): data/materials/code availability + statement + preregistration weighed |

## 8. Cautions
1. **Verify volatile specifics** (editor, length caps, abstract limit, exact TOP level, accepted types)
   on the official APA page — they change.
2. **Theory is the first gate** — a rigorous but atheoretical paper is the venue's most common reject.
3. **Design against CMV and model the nesting** before data; a post hoc Harman's test is not enough.
4. **Report measurement before structure** — CFA fit and reliabilities precede the structural model.
5. **Open science is held to TOP** — deposit data/materials/code with DOIs and write the
   data-availability statement before submission; disclose any dataset reuse.
