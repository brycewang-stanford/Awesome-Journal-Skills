# External Tools & Resources for Criminology-Style Research

Data sources, software, and packages useful when preparing a submission to *Criminology* (the ASC /
Wiley flagship). *Criminology* is **interdisciplinary** and **theory-forward**: a submission may be
quantitative, qualitative, or mixed-methods, drawing on sociology, psychology, economics, public
health, geography, and the criminal-legal system. Match tools to your design. Check licenses, IRB,
and data-use agreements before use, and verify any *Criminology*-specific policy in
[`official-source-map.md`](official-source-map.md).

## 1. Crime, justice & victimization data sources

### Official US crime and justice statistics
| Source | Provider | Typical use |
|--------|----------|-------------|
| UCR (Uniform Crime Reports) / SRS | FBI | Agency-level reported crime counts and rates (legacy) |
| NIBRS (National Incident-Based Reporting System) | FBI / Crime Data Explorer | Incident-level offenses, victims, offenders, arrests |
| NCVS (National Crime Victimization Survey) | BJS / Census | Self-reported victimization, the "dark figure" of crime |
| NACJD (Nat'l Archive of Criminal Justice Data) | ICPSR / Michigan | Restricted + public criminology datasets, replication archives |
| BJS series (NPS, SISFCF, recidivism) | Bureau of Justice Statistics | Corrections, sentencing, prisoner recidivism |
| FARS / CDC WONDER / WISQARS | NHTSA / CDC | Homicide, fatal injury, mortality linkage |

### Longitudinal, life-course & developmental data
| Source | Provider | Typical use |
|--------|----------|-------------|
| Add Health | UNC | Adolescent-to-adult offending, peers, networks |
| NLSY79 / NLSY97 | BLS / Ohio State | Criminal careers, employment–crime linkage over the life course |
| PHDCN (Project on Human Development in Chicago Neighborhoods) | ICPSR | Neighborhoods, collective efficacy, developmental trajectories |
| Pathways to Desistance | ICPSR | Serious adolescent offenders, desistance processes |
| Cambridge Study in Delinquent Development | UK / ICPSR | Classic prospective criminal-career cohort |
| Monitoring the Future / NSDUH | Michigan / SAMHSA | Self-reported delinquency, substance use, trends |

### Self-report, survey & administrative
- Self-report delinquency instruments; school, court, and police administrative records (with DUA/IRB)
- Linked administrative data (arrest–sentencing–corrections) for criminal-career and recidivism work

## 2. Software by method

### R
- Crime mapping / spatial: `sf`, `sp`, `spatstat`, `spdep`, `sparr` (kernel density), `GISTools`
- Trajectory / group-based models: `crimCV`, `flexmix`, `lcmm`, `kml` (k-means longitudinal)
- Survival / desistance / recidivism: `survival`, `survminer`, `cmprsk` (competing risks)
- Multilevel (people-in-places): `lme4`, `nlme`, `brms`
- Count models for crime counts: `MASS::glm.nb`, `pscl` (zero-inflated / hurdle), `glmmTMB`
- Causal inference: `MatchIt`, `WeightIt`, `fixest`, `did` (Callaway–Sant'Anna), `rdrobust`, `sensemakr`
- Reproducibility: `renv`, `targets`

### Stata
- `reghdfe`, `csdid`, `ivreghdfe`, `rdrobust`, `boottest` (wild-cluster bootstrap)
- `traj` plugin (Nagin group-based trajectory models — a criminology staple), `nbreg`/`zinb` (counts)
- `stcox`/`streg` (survival), `xtmixed`/`mixed` (multilevel), `coefplot`

### Python
- `pandas`, `numpy`, `statsmodels`, `linearmodels`, `lifelines` (survival)
- `geopandas`, `pysal`/`esda` (spatial autocorrelation, hotspots), `scikit-learn`
- `matplotlib` / `seaborn` for exhibits; pin with `requirements.txt` / `pip freeze`

### Qualitative & mixed-methods
- CAQDAS: NVivo, ATLAS.ti, MAXQDA, Taguette (open source) — coding interviews, ethnographic fieldnotes,
  court files
- Narrative / life-history methods; analytic induction; case-comparative designs

## 3. Criminology-specific methods to get right
- **Group-based trajectory models (GBTM)** / growth mixture models — report BIC, group shares, average
  posterior probabilities (AvePP ≥ 0.7), and odds of correct classification; do not over-interpret group count
- **Criminal-career parameters** — onset, frequency (λ), seriousness, duration, desistance; distinguish
  prevalence from incidence
- **Age–crime curve** and within-individual change; between- vs. within-person effects (fixed effects)
- **Hot-spot / near-repeat** spatial analysis; place-based designs and randomized patrol experiments
- **Recidivism survival analysis** with competing risks and right-censoring handled explicitly

## 4. Transparency, preregistration & replication
- Preregistration / pre-analysis plans: **OSF Registries**, AsPredicted. Wiley's current Author
  Compliance Tool row for *Criminology* says it **does not accept preprints**, so do not post a
  manuscript preprint unless the live Wiley guidance changes.
- Replication and restricted-data archiving: **ICPSR / NACJD** (incl. controlled-access deposits)
- Wiley **Open Science / Open Research Badges** (Open Data, Open Materials, Preregistered) — see
  `crim-data-and-transparency`; badge prompts depend on the live submission portal

## 5. Figures & exhibits
- Age–crime curves, trajectory-group plots, survival/recidivism curves, coefficient/forest plots,
  event-study and RD plots, predicted counts/probabilities (`marginaleffects`)
- Crime maps and hot-spot/kernel-density figures (`sf`, `tmap`); colorblind-safe palettes; grayscale-legible

## 6. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote — format to **APA style** (the journal uses a
  form of APA; fall back to **APA 6th** for anything unspecified), author-date
- Prepare an **anonymized main document** plus a **separate title page**; use **bias-free, person-first
  language** for justice-involved populations (per APA guidance)
- Typesetting: LaTeX (TeX Live / MacTeX, Overleaf) or Word; submit via the official ASC/Wiley online
  submission link

## 7. Cautions
1. **Verify volatile specifics** (length/abstract caps, portal prompts, editor text, and article-type
   details) on the official Wiley/ASC pages at upload. The source map records current ACT facts for
   review model, APC, ORCID, data-policy field, and preprints.
2. **Mind the dark figure** — UCR/NIBRS (reported crime), NCVS (victimization), and self-report capture
   different things; triangulate and state which construct you measure.
3. **Restricted data** — many criminology datasets (NACJD restricted-use, juvenile records) require DUAs
   and secure enclaves; plan access and a transparency/exemption path early.
4. **Theory-forward** — *Criminology* rewards a theoretical contribution, not a bare correlation; tie
   every analysis back to mechanism and to the criminological literature.
5. **Bias-free language** — use person-first, non-stigmatizing terms for people who offend, are
   victimized, or are justice-involved.
