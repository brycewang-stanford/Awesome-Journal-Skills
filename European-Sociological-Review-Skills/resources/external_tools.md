# External Tools & Resources for ESR-Style Quantitative Sociology

Data sources, software, and packages useful when preparing a *European Sociological Review* (ESR)
submission. ESR is the **flagship quantitative-sociology journal** of the ECSR (published by Oxford
University Press): comparative cross-national and longitudinal work on stratification and mobility,
education, labor markets, family and life course, migration and ethnicity, and attitudes, with rigorous
multilevel, panel/event-history, SEM, and causal-inference methods. Match tools to your design. Check
licenses and current access terms before use, and verify any ESR-specific policy in
[`official-source-map.md`](official-source-map.md).

## 1. European comparative & longitudinal data sources

### Cross-national attitudes, stratification, labor
| Source | Provider | Typical use |
|--------|----------|-------------|
| ESS (European Social Survey) | ESS ERIC | Attitudes, values, cross-national comparison (rotating modules) |
| EU-SILC | Eurostat | Income, poverty, deprivation across EU; longitudinal component |
| EVS / WVS | EVS / WVS consortia | Long-run values change, cross-national |
| ISSP | ISSP consortium | Repeated cross-national attitude modules |
| European Labour Force Survey (EU-LFS) | Eurostat | Employment, education-to-work, harmonized |

### Panel & life-course
| Source | Provider | Typical use |
|--------|----------|-------------|
| SOEP (Socio-Economic Panel) | DIW Berlin | German household panel; income, employment, life course |
| SHARE | SHARE ERIC | Ageing, health, retirement across Europe |
| Understanding Society / BHPS | ISER, Essex | UK household panel |
| CNEF-linked panels | Cornell/various | Cross-nationally comparable panels |
| GGS (Generations & Gender) | GGP | Family, fertility, life course, cross-national |

### Register / administrative & comparative micro
| Source | Provider | Typical use |
|--------|----------|-------------|
| National register data (e.g., Nordic registers) | National statistical offices | Administrative, full-population designs (under DUA) |
| IPUMS-International | U. Minnesota | Harmonized census microdata |
| Comparative mobility tables / CASMIN-coded data | Various | Social mobility, intergenerational analysis |
| PISA / PIAAC / TIMSS | OECD / IEA | Education, skills, cross-national achievement |

## 2. Harmonization & measurement schemes (ESR house staples)
- **Education**: ISCED, CASMIN — harmonized comparative education coding
- **Occupation/class**: ISCO → ISEI (status), SIOPS, EGP / ESeC class schemes, Oesch class
- **Measurement equivalence**: configural / metric / scalar invariance (MGCFA, alignment method)

## 3. Software by method

### R
- Multilevel: `lme4`, `glmmTMB`, `brms` (Bayesian multilevel), `merTools`, `performance`
- Measurement / SEM & invariance: `lavaan`, `semTools` (`measurementInvariance`), `sirt` (alignment)
- Survey design: `survey`, `srvyr` (weights, clustering, strata)
- Panel / fixed effects: `fixest`, `plm`; staggered DiD: `did`, `fixest::sunab`, `didimputation`
- Event history / survival: `survival`, `eha`, `coxme`, `frailtypack`
- Few-cluster inference: `clubSandwich` (CR2), `fwildclusterboot` (wild cluster bootstrap)
- Decomposition / inequality: `oaxaca`, `dineq`; sequence analysis: `TraMineR`
- Reproducibility: `renv`, `targets`

### Stata
- `mixed` / `melogit` / `meglm` (multilevel), `gsem`/`sem` (SEM + invariance), `xtreg` (panel)
- `stcox` / `streg` (event history), `svy:` (survey estimation)
- `reghdfe`, `csdid` / `eventstudyinteract` / `did_imputation` (staggered DiD)
- `boottest` (wild cluster bootstrap), `oaxaca`, `ineqdeco`; `coefplot`, `estout`/`esttab`

### Python
- `pandas`, `numpy`, `statsmodels` (mixedlm), `linearmodels` (panel), `pymer4`, `bambi` (Bayesian)
- `semopy` (SEM), `lifelines` (survival); `matplotlib`/`seaborn`; pin with `requirements.txt`

## 4. Figures & exhibits
- Country forest / caterpillar plots of random effects; predicted-margins interaction plots
- Mobility / transition tables and flow diagrams; survival and cumulative-incidence curves
- Growth-trajectory plots; colorblind-safe palettes; grayscale-legible; vector output (PDF/EPS)
- ESR counts tables and figures *outside* the ~8,000-word limit, but they must be clear and self-contained

## 5. Writing, references & reproducibility
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote — format to OUP/ESR **author-date** style
- Prepare a **completely anonymous** manuscript (no author identity, no identifying acknowledgments)
- Repositories for the **replication package**: OSF, Zenodo, GESIS Data Archive (citable DOI)
- Master script + pinned versions + seeds + archived harmonization code (see `resources/code/`)

## 6. Process & portal
| Item | Note |
|------|------|
| Submission portal | **ScholarOne Manuscripts**, `mc.manuscriptcentral.com/esr` |
| Owner / publisher | **ECSR** (European Consortium for Sociological Research) / **Oxford University Press** |
| Review model | **Double-blind** — completely anonymous manuscript |
| Article length | Articles **~8,000 words** incl. endnotes + references (tables/figures excluded); longer with justification (待核实 on any stricter cap) |
| Abstract | **≤200 words**, non-identifying |
| Data policy | **Data Availability Statement required** (from 5 Sep 2022); **replication package** for statistical/computational work (submissions from 1 Jan 2025), qualitative exempt |
| Article types | research Articles, Comments/Replies, **Data Briefs** |

## 7. Cautions
1. **Verify volatile specifics** (editor and term, exact caps, policy dates, OA charges) on the official
   OUP/ECSR pages — they change. Unverified items are 待核实.
2. **Establish measurement equivalence** before any cross-national latent comparison — it is ESR's most
   common fatal design flaw.
3. **Handle few clusters honestly** — ~20-30 countries cannot support strong macro-level inference with
   naive SEs; use df-aware or Bayesian methods.
4. **Plan the replication package early** — for statistical/computational work it is a condition of
   publication, not an afterthought; restricted data still requires shareable code + an access path.
5. **Anonymize fully** and never submit elsewhere while under ESR review.
