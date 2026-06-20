# External Tools & Resources for JMF-Style Family Science

Data sources, software, and packages useful when preparing a *Journal of Marriage and Family* (JMF)
submission. JMF is the **interdisciplinary flagship of family science**: a submission may be
quantitative, qualitative, or multi-method, drawn from sociology, psychology, demography, and family
studies, on marriage and partnering, divorce and union dissolution, cohabitation and fertility,
parenting and child wellbeing, intergenerational and close relationships, gender, and family policy.
Match tools to your design and unit of analysis (individual, dyad, family, household, cohort). Check
licenses and current access terms before use, and verify any JMF-specific policy in
[`official-source-map.md`](official-source-map.md).

## 1. Data sources by family-science domain

### Family demography & life course (panel / longitudinal)
| Source | Provider | Typical use |
|--------|----------|-------------|
| PSID (Panel Study of Income Dynamics) + CDS/TAS | University of Michigan | Long-run family/household, intergenerational, economic dynamics |
| NLSY79 / NLSY97 (+ Child & Young Adult) | BLS / Ohio State | Union formation, fertility, parenting, child outcomes over time |
| Add Health (National Longitudinal Study of Adolescent to Adult Health) | UNC | Relationships, transitions to adulthood, health |
| Fragile Families & Child Wellbeing (Future of Families) | Princeton / Columbia | Nonmarital births, coparenting, child wellbeing |
| NSFG (National Survey of Family Growth) | NCHS/CDC | Marriage, cohabitation, fertility, family formation |
| Demographic and Health Surveys (DHS) | USAID/ICF | Cross-national fertility, marriage, household structure |
| HRS (Health and Retirement Study) | Michigan | Later-life couples, caregiving, intergenerational ties |

### Couples, dyads & close relationships
| Source | Provider | Typical use |
|--------|----------|-------------|
| NSHAP / couples sub-studies | NORC | Partnered older adults, intimacy, health |
| HCMST (How Couples Meet and Stay Together) | Stanford | Relationship formation, dissolution, same-sex couples |
| German Family Panel (pairfam) | Germany | Multi-actor dyadic/parent–child panel, partnering |
| Author-collected dyadic / daily-diary data | Various | APIM, dyadic process, daily-diary couple studies |

### Cross-national, household & policy
| Source | Provider | Typical use |
|--------|----------|-------------|
| Generations & Gender Survey (GGS) | GGP | Cross-national partnering, fertility, intergenerational |
| IPUMS-USA / IPUMS-International / CPS | Minnesota | Household and family structure, marriage, comparative |
| LIS (Luxembourg Income Study) | LIS | Cross-national family income, policy, inequality |
| OECD Family Database | OECD | Family policy indicators (leave, childcare, transfers) |

## 2. Software by method

### R
- Dyadic / multilevel: `nlme`, `lme4`, `glmmTMB`; APIM and dyadic SEM via `lavaan`; `dyadr`
- Longitudinal / growth: `lavaan` (latent growth, cross-lagged panel), growth-mixture (`lcmm`)
- Event history / survival: `survival`, `survminer`, discrete-time hazard via `glm`
- Family demography: `demography`, decomposition and standardization; `survey` for complex designs
- Causal / observational: `MatchIt`, `WeightIt`, `marginaleffects`, `mediation`, `sensemakr`
- Missing data: `mice` (multiple imputation), `Amelia`; reproducibility: `renv`, `targets`

### Stata
- Panel/multilevel: `mixed`, `meglm`, `xt*`; dyadic via `mixed` with actor/partner terms
- Survival: `stcox`, `streg`, `stpm2`; complex survey: `svy:` with weights/clusters/strata
- SEM/growth: `sem`, `gsem`; mediation via `gsem`/`khb`; `mi` for multiple imputation
- Decomposition: `oaxaca`; `coefplot`, `marginsplot` for exhibits

### Python
- `pandas`, `numpy`, `statsmodels`, `linearmodels`; `lifelines` (survival); `semopy` (SEM)
- `pingouin` / `statsmodels` mixed models; `matplotlib` / `seaborn` for exhibits
- Pin with `requirements.txt` / `pip freeze`

### Qualitative & mixed-methods
- CAQDAS: NVivo, ATLAS.ti, MAXQDA, Dedoose, Taguette (open source) — coding interviews, fieldnotes,
  family/couple narratives; dyadic and multi-perspective qualitative analysis
- Mixed-methods: explicit integration (joint displays), narrative + survey triangulation

## 3. Design, transparency & reproducibility
- Preregistration / pre-analysis plans: **OSF Registries**, AsPredicted (share an anonymized link for
  double-blind review); register confirmatory vs. exploratory analyses
- Power for multilevel/dyadic/longitudinal designs: simulation-based power (`simr` in R), APIM power
- Replication / data-sharing package destined for an approved repository (e.g., **OSF**, **ICPSR**,
  Harvard Dataverse), with a data availability statement (see `jmf-transparency-and-data-policy`)
- Many family datasets carry **restricted-use** agreements (PSID, Add Health, Fragile Families): plan
  for access instructions and synthetic/derived data rather than redistributing restricted files

## 4. Figures & exhibits
- Coefficient/marginal-effects plots (`marginaleffects`, `coefplot`); survival curves; growth
  trajectories; event-history/age-pattern plots; APIM path diagrams for dyads
- Family-structure and life-course visualizations; population pyramids / decomposition charts
- Colorblind-safe palettes; legible in grayscale; vector output (PDF/EPS) for print

## 5. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote — format to **modified APA style** (JMF's
  variant); keep one consistent style
- Typesetting: Word (JMF requests a Microsoft Word document, 12-pt font) or LaTeX→Word; prepare an
  **anonymized** manuscript (no names, affiliations, contact info, acknowledgements) for double-blind
  review; write a **structured abstract** (~200–225 words; Objective / Background / Method / Results /
  Conclusion / Implications)
- Use **bias-free language** per APA guidelines

## 6. Process & portal
| Item | Note |
|------|------|
| Submission portal | **Wiley Research Exchange** (new submissions after 25 Jun 2025); **ScholarOne Manuscript Central** for earlier submissions — confirm the current link |
| Owner / publisher | **NCFR** (National Council on Family Relations) / **Wiley** |
| Review model | **Double-blind anonymous** — anonymize the manuscript |
| Article formats | Original research (quantitative / qualitative / multi-method); **brief reports** (≤ 25 pp.) for focused contributions, replications, innovative designs, important null findings |
| Length | Article manuscript **≤ 35 pages** (incl. abstract, text, tables, figures); **Brief Report ≤ 25 pages** |
| Style | **Modified APA**; structured abstract ~200–225 words; bias-free language |
| Data policy | Replication-level detail; Wiley Data Availability Statement; document shared/restricted data access path |

## 7. Cautions
1. **Live-check volatile specifics** (editor roster, exact file requirements, fees, portal link,
   and any journal-specific data-policy wording) on the official NCFR/Wiley pages before upload.
2. **Anonymize properly** — JMF is double-blind; strip names, affiliations, contact info,
   acknowledgements, and self-references to work under review/forthcoming.
3. **Match the unit of analysis** — individual, dyad, family, household, or cohort; use dyadic/
   multilevel/longitudinal models that respect non-independence (couples, parents and children).
4. **Respect restricted-use data agreements** — many family datasets cannot be redistributed; supply
   access instructions and synthetic/derived data instead.
5. **Center family science** — a JMF paper must advance understanding of families and close
   relationships, with clear relevance to theory, policy, or practice.
