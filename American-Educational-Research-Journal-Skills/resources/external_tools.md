# External Tools & Resources for AERJ-Style Education Research

Data sources, software, and packages useful when preparing an *American Educational Research Journal*
(AERJ) submission. AERJ is a **field-wide generalist** education journal: a submission may be
**quantitative** (multilevel/HLM, IRT/measurement, value-added, quasi-experimental, RCT),
**qualitative** (ethnography, case study, interview, discourse, narrative), or **mixed methods**.
It may foreground policy/institutions, teaching/learning, human development, or a cross-cutting design.
Match tools to your dominant lens and design. Check licenses and current access
terms before use, and verify any AERJ-specific policy in
[`official-source-map.md`](official-source-map.md).

## 1. Data sources for education research

### US federal / large-scale assessment
| Source | Provider | Typical use |
|--------|----------|-------------|
| NCES / IES Data (ECLS-K, NELS, ELS, HSLS:09) | U.S. Dept. of Education | Longitudinal cohorts of students/schools |
| Common Core of Data (CCD) / IPEDS | NCES | School- and district-level / postsecondary administrative data |
| NAEP ("The Nation's Report Card") | NCES | Cross-state achievement, restricted-use NAEP DAS |
| Civil Rights Data Collection (CRDC) | OCR | Discipline, access, equity indicators by school |
| Stanford Education Data Archive (SEDA) | Stanford | District/county achievement gaps over time |

### International / comparative (SIA & comparative-education work)
| Source | Provider | Typical use |
|--------|----------|-------------|
| PISA / TALIS | OECD | Cross-national achievement, teacher/teaching surveys |
| TIMSS / PIRLS | IEA | Cross-national math/science/reading trends |
| UIS / World Bank EdStats | UNESCO / World Bank | Cross-country education indicators |

### State longitudinal & administrative data
| Source | Provider | Typical use |
|--------|----------|-------------|
| State Longitudinal Data Systems (SLDS) | State agencies | Student–teacher linked records, value-added |
| Research–practice partnership (RPP) data | Districts/agencies | Co-designed local studies (often restricted) |

### Qualitative & teaching-and-learning data
| Source | Provider | Typical use |
|--------|----------|-------------|
| Classroom video / observation corpora | Author- or project-collected | Discourse, instruction, interaction analysis |
| Interviews, fieldnotes, documents, artifacts | Author-collected | Ethnography, case study, narrative inquiry |
| QDR (Qualitative Data Repository) | Syracuse | Sharing/citing qualitative data with access controls |

## 2. Software by method

### R (widely used in quantitative education research)
- Multilevel / mixed models: `lme4`, `nlme`, `brms` (Bayesian), `WeMix` (survey-weighted multilevel)
- IRT / measurement / SEM: `mirt`, `TAM`, `lavaan`, `mplusAutomation`, `psych`
- Causal / quasi-experimental: `fixest`, `did` (Callaway–Sant'Anna), `rdrobust`, `MatchIt`, `estimatr`
- Large-scale-assessment plausible values & weights: `EdSurvey`, `intsvy`, `survey`
- Power for cluster/multisite trials: `PowerUpR`, `simr`
- Reproducibility: `renv` (pin versions), `targets` (pipelines)

### Stata
- `mixed` / `melogit` / `meqrlogit` (multilevel), `gsem` (SEM), `irt` suite
- `reghdfe`, `csdid`, `rdrobust`, `ivreghdfe`; `pv` / `repest` for plausible values and replicate weights
- `coefplot`, `estout`/`esttab` for exhibits

### Mplus / specialized
- **Mplus** for latent-variable, mixture, multilevel-SEM, and longitudinal growth models
- **HLM** software for hierarchical linear models; **IRTPRO / flexMIRT** for measurement

### Qualitative & mixed-methods
- CAQDAS: NVivo, ATLAS.ti, MAXQDA, Dedoose (mixed methods), Taguette (open source)
- Transcription/coding workflows; intercoder-reliability tools; audit-trail and memo systems
- Joint displays and integration matrices for mixed-methods convergence

## 3. Reporting standards, design & transparency
- **AERA Standards for Reporting on Empirical Social Science Research** (2006) — warranting +
  transparency, for quantitative **and** qualitative work; **Humanities-Oriented Research** standards
  (2009) for humanities-grounded scholarship
- Method-specific guidance: CONSORT-style trial reporting; What Works Clearinghouse (WWC) design
  standards for causal claims; reporting guidance for multilevel and SEM models
- Preregistration / pre-analysis plans: **OSF Registries**, AsPredicted, the **Registry of Efficacy
  and Effectiveness Studies (REES)** for education trials — share anonymized for masked review
- Power/design: `PowerUpR` and simulation-based power for multilevel and multisite cluster designs

## 4. Figures & exhibits (AERJ rewards clear, accessible, APA-formatted exhibits)
- Coefficient/forest plots, marginal-effects and predicted-probability plots (`ggplot2`/`broom`,
  `marginaleffects`, `coefplot`), growth-curve trajectories, RD/event-study plots
- Joint displays for mixed-methods integration; coding trees / thematic maps for qualitative findings
- Colorblind-safe palettes and grayscale-legible figures; vector output (PDF/EPS) for print
- APA 7th-edition table and figure formatting (titles, notes, probability notes)

## 5. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote — format to **APA 7th edition** (author-date);
  keep one consistent style throughout
- Typesetting: Word or LaTeX (apa7 class / `papaja` for R Markdown); prepare a **masked manuscript**
  (no identifying metadata, citations, or self-references) plus a separate **title page file**
- Include a **100–120-word abstract**; an ORCID iD for the corresponding author

## 6. Process & portal
| Item | Note |
|------|------|
| Submission portal | **ScholarOne Manuscripts** at `https://mc.manuscriptcentral.com/aerj` |
| Owner / publisher | **AERA** / **SAGE** |
| Integrated fit | Name the dominant education lens and field-wide significance; do not route by the former SIA/TLHD split |
| Review model | **Double-anonymous / masked** — anonymize the manuscript; names only on the title page file |
| Length | Manuscript **maximum 50 pages**, double-spaced, 12-pt, 1" margins, inclusive of tables/figures/notes/references |
| Abstract | **100–120 words** |
| Style | **APA 7th edition** (author-date) |
| Submission fee | SAGE guidelines state **no fee to publish or submit**; gold OA via **SAGE Choice** for a fee |
| Reporting standards | **AERA Standards for Reporting on Empirical Social Science Research** (quant + qual) |

## 7. Cautions
1. **Verify volatile specifics** (editors, SAGE Choice fee, portal behavior, data-policy wording) on the official AERA/SAGE pages before upload.
2. **Anonymize properly** — AERJ is masked; strip author metadata, self-citations, and identifying
   footnotes; put names only on the separate title page file.
3. **Match method to standards** — AERJ judges quantitative, qualitative, and mixed-methods work on
   its own terms; report against the AERA reporting standards appropriate to your method.
4. **Name the right AERJ lens** — policy/institutions/equity, teaching/learning/development, or cross-cutting; a narrow or unclear frame weakens review.
5. **Write for the whole field** — an AERJ paper must speak past one subfield to a general
   education-research audience, with explicit attention to significance for policy and/or practice.
