# External Tools & Resources for Social-Forces-Style Sociology

Data sources, software, and packages useful when preparing a *Social Forces* (SF) submission. Social
Forces is a **generalist social-science** journal centered on sociology but explicitly
multidisciplinary — a submission may be quantitative, demographic, comparative-historical,
ethnographic, network-analytic, computational, or social-psychological, and it may reach into
anthropology, political science, history, or economics. Match tools to your subfield and design, and
mind the journal's defining constraint: **a 10,000-word cap that includes the reference list**, so
budget citations and exhibits accordingly. Check licenses and current access terms before use, and
verify any SF-specific policy in [`official-source-map.md`](official-source-map.md).

## 1. Data sources by subfield

### Stratification, mobility & demography
| Source | Provider | Typical use |
|--------|----------|-------------|
| GSS (General Social Survey) | NORC | Long-run US attitudes, mobility, social change |
| PSID (Panel Study of Income Dynamics) | Michigan | Income, mobility, household dynamics over time |
| IPUMS (USA / CPS / International) | Minnesota | Harmonized census/survey microdata for stratification & demography |
| NLSY (cohort studies) | BLS / Ohio State | Life-course, education-to-work transitions |
| LIS / LWS (Luxembourg Income Study) | LIS | Cross-national income and wealth inequality |
| Human Mortality / Fertility Databases | MPIDR | Formal demography, period/cohort analysis |

### Comparative-historical & political/economic sociology
| Source | Provider | Typical use |
|--------|----------|-------------|
| V-Dem | University of Gothenburg | Regime/institutional indicators, panel |
| QoG (Quality of Government) | U. Gothenburg | Compiled cross-country governance data |
| Comparative Welfare States / CWED | Multiple | Welfare-state and policy comparison |
| Archives / administrative records | Various | Process tracing, institutional and historical work |

### Social psychology, networks & computational
| Source | Provider | Typical use |
|--------|----------|-------------|
| Add Health | UNC / Carolina Population Center | Networks, health, adolescent-to-adult life course |
| Survey experiments / vignettes | Author-collected (Prolife/MTurk/Qualtrics panels) | Attitudes, perceptions, mechanisms |
| Digital trace / platform data | Author-collected APIs | Computational social science, diffusion, behavior |
| Qualitative interview / ethnographic data | Author-collected | Meaning, mechanisms, lived experience |

## 2. Software by method

### R
- Regression/panel: `fixest`, `lme4`/`glmmTMB` (multilevel), `survey` (complex designs), `marginaleffects`
- Causal inference: `did` (Callaway–Sant'Anna), `MatchIt`, `WeightIt`, `rdrobust`, `sensemakr`
- Demography: `demography`, `HMDHFDplus`, decomposition (`DemoDecomp`), `survival`
- Networks: `igraph`, `statnet`/`ergm`, `RSiena` (longitudinal networks)
- Text-as-data / computational: `quanteda`, `stm`, `text2vec`; embedding/LLM pipelines
- Reproducibility: `renv` (pin versions), `targets` (pipelines)

### Stata
- `reghdfe`, `csdid`, `did_multiplegt_dyn`, `ivreghdfe`, `gsem`/`sem` (latent variables, mediation)
- `mi` (multiple imputation), `svy` (complex survey), `margins`/`coefplot`, `oaxaca` (decomposition)
- `boottest` (wild-cluster bootstrap), `estout`/`esttab` for tables

### Python
- `pandas`, `numpy`, `statsmodels`, `linearmodels`; `lifelines` (survival/event-history)
- Networks: `networkx`; computational text: `spaCy`, `scikit-learn`, `transformers`
- `matplotlib` / `seaborn` for exhibits; pin with `requirements.txt` / `pip freeze`

### Qualitative & comparative
- CAQDAS: NVivo, ATLAS.ti, MAXQDA, Taguette (open source) — coding interviews, fieldnotes, documents
- QCA: `QCA` (R), fs/csQCA for set-theoretic comparative work
- Process tracing: explicit hypothesis tests (hoop / smoking-gun / straw-in-the-wind)

## 3. Transparency, documentation & deposit
- **Data availability statement** is **required** for published SF papers — draft it early; describe
  availability and give access means or a unique identifier (see `sf-data-and-transparency`).
- Public repositories where ethically feasible: **ICPSR/openICPSR**, the **Harvard Dataverse**, **OSF**,
  Zenodo — choose one with persistent identifiers and documentation support.
- Confidential/restricted data: document the access process (application, enclave, provider contact)
  in the statement; provide synthetic or simulated data where feasible so code can be run.
- Preregistration (for experiments/prospective designs): **OSF Registries**, AsPredicted — optional at
  SF but strengthens credibility; mark registered vs. exploratory analyses.

## 4. Figures & exhibits (SF caps you at 10 tables and figure panels)
- The combined limit is **10 tables and figure panels**, so each exhibit must earn its slot — prefer
  one informative figure to several near-duplicate tables.
- Coefficient/marginal-effects plots (`coefplot`, `ggplot2`/`broom`, `marginaleffects`), event-study
  and decomposition plots, survival curves, network diagrams where structure is the point.
- Colorblind-safe palettes; legible in grayscale; vector output (PDF/EPS) for print.
- Supplementary materials are capped at **10 pages** — they are not an unlimited overflow appendix.

## 5. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote — format to the **Chicago Manual of Style,
  17th edition (author-date)** at final submission (any readable style is accepted at first
  submission). Keep one consistent style.
- **Remember references count toward the 10,000-word limit** — trim redundant citation strings and
  avoid citation padding; this is a real constraint, not a formality.
- Typesetting: LaTeX (TeX Live / MacTeX, Overleaf) or Word/.odt; prepare a **double-anonymized**
  manuscript with all identifying information on a **separate title page**.

## 6. Process & portal
| Item | Note |
|------|------|
| Submission portal | **ScholarOne Manuscript Central** (`mc.manuscriptcentral.com/sf`) — Word/.odt |
| Owner / publisher | **University of North Carolina at Chapel Hill (Dept. of Sociology)** / **Oxford University Press** |
| Review model | **Double-anonymized** — anonymize the manuscript; separate title page |
| Length | **≤ 10,000 words including text, endnotes, AND references**; **≤ 10 tables and figure panels** |
| Style | **Chicago Manual of Style, 17th ed. (author-date)** at final submission |
| Fee | **$50 non-refundable processing fee** ($20 for student-only manuscripts); **no page charges** |
| Data policy | **Data availability statement required**; deposit in a public repository where ethically feasible |

## 7. Cautions
1. **Verify volatile specifics** (editor, exact caps, fee/APC, table limit, data-policy wording) on the
   official Oxford Academic / UNC pages — they change; unverified items are marked 待核实.
2. **The word cap includes references** — unlike journals that exclude them, SF counts your reference
   list; this disciplines both citation breadth and prose length.
3. **Anonymize properly** — SF is double-anonymized; move names, affiliations, acknowledgements, and
   funding details to a separate title page.
4. **Respect the 10-panel exhibit limit** — design exhibits to carry the argument, not to overflow it.
5. **Write for a general social-science audience** — SF prizes work that a reader outside your
   subfield (and outside sociology) can follow and find significant.
