# External Tools & Resources for JPART-Style Public Administration

Data sources, software, and packages useful when preparing a *Journal of Public Administration Research
and Theory* (JPART) submission. JPART publishes **theory-and-research** public-management work — survey,
lab, and field experiments on public employees and citizens; causal observational designs; multilevel
organizational data; and mixed methods. Match tools to your design. Check licenses and current access
terms before use, and verify any JPART-specific policy in
[`official-source-map.md`](official-source-map.md).

## 1. Data sources for public-administration research

### US federal & workforce
| Source | Provider | Typical use |
|--------|----------|-------------|
| Federal Employee Viewpoint Survey (FEVS) | OPM | Employee attitudes, PSM, engagement, performance |
| FedScope / Enterprise Human Resources Integration | OPM | Federal workforce demographics, representation |
| USAspending / SAM.gov | Treasury / GSA | Contracting, grants, network governance |
| Bureau / agency performance reports (GPRA/GPRAMA) | OMB / agencies | Goal ambiguity, performance management |

### State, local & nonprofit
| Source | Provider | Typical use |
|--------|----------|-------------|
| ICMA surveys | ICMA | Local-government management practices |
| Census of Governments / ASPEP | US Census Bureau | Local public employment, finance |
| IRS Form 990 / NCCS | IRS / Urban Institute | Nonprofit and co-production studies |
| State administrative / personnel records | State agencies | Representation, turnover, street-level behavior |

### Comparative & cross-national
| Source | Provider | Typical use |
|--------|----------|-------------|
| QoG (Quality of Government) | U. Gothenburg | Cross-country governance indicators |
| World Bank Worldwide Governance Indicators | World Bank | Government effectiveness, regulatory quality |
| European/national civil-service surveys | Various | Comparative bureaucracy, PSM cross-nationally |

## 2. Survey & experiment platforms (the JPART workhorse)
- Fielding: Qualtrics, Lucid/Cint, Prolific, YouGov; agency-recruited samples of **real public employees**
- Conjoint/factorial design: `cregg`/`cjoint` (R), `conjointSDT`; vignette/factorial-survey tooling
- Design diagnosis & power: `DeclareDesign` (declare → diagnose → redesign), simulation-based power
- Randomization inference: `ri2` (R), `ritest` (Stata)
- Sensitivity to unobserved confounding: `sensemakr`, `EValue`

## 3. Software by method

### R (common in PA methodology)
- Causal/observational: `fixest`, `did` (Callaway–Sant'Anna), `MatchIt`, `WeightIt`, `rdrobust`, `estimatr`
- Multilevel: `lme4`, `brms`, `glmmTMB` (employees nested in agencies/jurisdictions)
- Measurement/scales (PSM, red tape): `psych`, `lavaan` (CFA/SEM), `semTools`
- Mediation: `mediation`, `cmdstanr`-based Bayesian mediation
- Reproducibility: `renv` (pin versions), `targets` (pipelines)

### Stata
- `reghdfe`, `csdid`, `did_multiplegt_dyn`, `rdrobust`, `ivreg2`/`ivreghdfe`, `mixed`/`melogit` (multilevel)
- `boottest` (wild-cluster bootstrap), `ritest` (randomization inference), `coefplot`, `sem`/`gsem`

### Python
- `pandas`, `numpy`, `statsmodels`, `linearmodels`; `pymer4` for multilevel
- `matplotlib` / `seaborn` for exhibits; pin with `requirements.txt` / `pip freeze`

## 4. Common-method-bias toolkit (a recurring JPART referee focus)
- Separate sources for X and Y; objective/administrative outcomes where possible
- Marker-variable technique; temporal/psychological separation of measures
- Harman's single-factor test (necessary-not-sufficient — do not over-rely)

## 5. Preregistration, transparency & deposit
- Preregistration / pre-analysis plans: **OSF Registries**, AsPredicted, EGAP; share a **blinded** plan
  and mark confirmatory vs. exploratory analyses (JPART accepts blinded pre-reg reports)
- Public data + code deposit: **OSF**, **Harvard Dataverse**, or another trusted citable repository with a
  persistent identifier — required (where ethically possible) as a condition of publication
- Draft the mandatory **Data Availability Statement** (see `jpart-transparency-and-data`)

## 6. Figures & exhibits
- Coefficient/forest plots (`coefplot`, `ggplot2`/`broom`), marginal-effects and predicted-probability
  plots (`marginaleffects`), conjoint AMCE/marginal-means plots
- Multilevel: variance-component and random-effect plots; report ICCs
- Colorblind-safe palettes and figures legible in grayscale; vector output (PDF/EPS) for print

## 7. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote — format to JPART/OUP **author-date** with DOIs
- Typesetting: LaTeX or Word; prepare a **double-blind** manuscript (no identifying metadata, third-person
  self-citation) plus a separate cover sheet

## 8. Process & portal
| Item | Note |
|------|------|
| Submission portal | **Editorial Express** (`editorialexpress.com/jpart`) — single PDF |
| Owner / publisher | **PMRA** / **Oxford University Press** |
| Review model | **Double-blind** — anonymize the manuscript |
| Length | ~12,000 words **including abstract, tables, references** (verify) |
| Keywords | 3–5; first three signal theory / research theme / method |
| Data policy | Public release of data + code as a condition of publication; Data Availability Statement |
| Submission fee | None stated (verify); open-access APC handled by OUP after acceptance |

## 9. Cautions
1. **Verify volatile specifics** (editors, exact caps, fee/APC, data-policy wording) on the official
   OUP/JPART pages — they change; unverified items are marked 待核实.
2. **Anonymize properly** — JPART is double-blind; strip metadata, cite your own work in the third person.
3. **Confront common-method bias and selection** — these are the first objections in PA review.
4. **Build the public data-and-code package as you go** — release is a condition of publication.
5. **Lead with theory** — a public-management theory contribution, not a stand-alone policy finding.
