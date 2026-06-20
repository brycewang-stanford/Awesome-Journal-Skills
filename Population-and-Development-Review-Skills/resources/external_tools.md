# External Tools & Resources for Population-and-Development Research

Data sources, software, and packages useful when preparing a *Population and Development Review* (PDR)
submission. PDR sits at the **intersection of demography and development**: a submission may combine a
population process (fertility, mortality, migration, ageing, structure) with social, economic, or
environmental change and policy. Match tools to your question and the method. Check licenses and current
access terms before use, and verify any PDR-specific policy in
[`official-source-map.md`](official-source-map.md).

## 1. Population data sources by domain

### Mortality, fertility & longevity
| Source | Provider | Typical use |
|--------|----------|-------------|
| Human Mortality Database (HMD) | UC Berkeley / MPIDR | Life tables, death rates, cohort/period mortality |
| Human Fertility Database (HFD) | MPIDR / VID | Age-specific fertility, parity, tempo/quantum |
| WHO Mortality Database / GBD | WHO / IHME | Cause-of-death, global burden, comparative mortality |
| UN World Population Prospects (WPP) | UN DESA | Estimates and projections by country/age/sex |

### Surveys, cohorts & censuses
| Source | Provider | Typical use |
|--------|----------|-------------|
| IPUMS (USA / International / DHS / CPS) | University of Minnesota | Harmonized census/survey microdata |
| Demographic and Health Surveys (DHS) | USAID / ICF | Fertility, child health, mortality in LMICs (licensed) |
| MICS (Multiple Indicator Cluster Surveys) | UNICEF | Child/maternal health and development indicators |
| HRS / ELSA / SHARE | NIA / consortia | Ageing, health, retirement panels |
| Add Health, PSID / NLSY, FFCWS | UNC / ISR / BLS / Princeton | Life-course and family demography |

### Development, environment & policy linkage (the PDR "development" side)
| Source | Provider | Typical use |
|--------|----------|-------------|
| World Development Indicators (WDI) | World Bank | GDP, schooling, poverty, labor — development outcomes |
| UNDP Human Development Index / reports | UNDP | Composite development, gender, inequality |
| National Transfer Accounts (NTA) | NTA network | Demographic dividend, age-economic flows |
| Climate / emissions (Our World in Data, EM-DAT, gridded climate) | OWID / CRED / various | Population–environment and climate-vulnerability work |
| WorldPop / GADM / gridded population | academic | Spatial demography, small-area and exposure estimates |

## 2. Software by method

### R (widely used in formal demography)
- Life tables & mortality: `demography`, `DemoTools`, `MortalityLaws`, `lifecontingencies`
- Fertility / tempo-quantum: `HMDHFDplus` (pull HMD/HFD), `bayesTFR`
- Event history / survival: `survival`, `eha`, `flexsurv`, `mstate` (multistate)
- Age-period-cohort: `apc`, `Epi`, `bamp`; identification-aware models
- Decomposition: `DemoDecomp` (Horiuchi/stepwise, Arriaga, Kitagawa), `DemoTools`
- Projections / dividend: `bayesPop`, cohort-component tooling; NTA-style accounting
- Survey / development data: `survey`, `srvyr`; `wbstats` / `WDI` (World Bank), `idbr` (IDB)

### Stata
- Survival/event history: `stset`, `streg`, `stcox`, `stcompet` (competing risks)
- Decomposition & standardization: `mvdcmp`, `oaxaca`; `dstdize`/`istdize`
- Survey design: `svy:` estimators for complex samples; `wbopendata` for World Bank data

### Python
- `pandas`, `numpy`, `statsmodels`, `lifelines` (survival), `scikit-survival`
- `world_bank_data` / `wbgapi` for WDI; `geopandas` for spatial work
- Plotting: `matplotlib` / `seaborn`

### Specialized tools
- **HMD/HFD protocols** for consistent life-table and fertility estimation
- **MORTPAK** and **UN Spectrum/DemProj** for population estimates and projections
- **National Transfer Accounts (NTA)** methods for the demographic dividend

## 3. Distinctive methods (match to design)
- **Life tables** (period/cohort), abridged vs. complete; multiple-decrement and multistate
- **Decomposition** of differences/changes in rates (Kitagawa, Arriaga, Horiuchi, Das Gupta)
- **Event-history / survival** (Cox, parametric, discrete-time, competing risks, multistate)
- **Age-period-cohort** models (be explicit about the identification problem and the constraints)
- **Cohort-component projections** and scenario analysis tied to policy/development futures
- **Demographic-dividend accounting** (NTA, age-structure × economic-support-ratio decompositions)
- Causal designs (DiD, IV, RDD, DML) where the question is causal — see the `code/` skeleton

## 4. Reproducibility & data deposit
- PDR follows **Wiley's** data-sharing framework: a **data availability statement** with persistent IDs;
  the journal **hosts no repository** — deposit in a FAIR repository (see `popdevr-transparency-and-data`)
- Repositories: **ICPSR / openICPSR**, **Harvard Dataverse**, **Zenodo**, **OSF**; find one via
  **FAIRsharing.org** and **re3data.org**
- **Licensed data (DHS, census microdata)**: share the **extract specification and code**, not the raw
  microdata; cite the provider's persistent access path
- Pin versions: `renv` (R), `requirements.txt` / `pip freeze` (Python), recorded `ssc`/`net` (Stata);
  set and report seeds for simulation; one master script regenerates every exhibit

## 5. Figures & exhibits (PDR rewards clear graphics that carry the development point)
- **Population pyramids** (age-sex structure, across development levels), **age schedules** of
  fertility/mortality/migration, **survival/hazard curves**, **projection fans / scenario plots**
- **Cross-country scatter / small-multiples** linking a population quantity to a development indicator
  (with comparability caveats); small-multiple **maps** (`sf`, `tmap`)
- Colorblind-safe palettes, grayscale-legible, vector output (PDF/EPS); self-contained titles/notes

## 6. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote — **Free Format** first round (any consistent
  style), **APA-style** house style applied at revision
- Typesetting: LaTeX (TeX Live / MacTeX / Overleaf) or Word; prepare a **double-anonymized** manuscript
  (remove all co-author identifiers) plus abstract and keywords

## 7. Process & portal
| Item | Note |
|------|------|
| Submission portal | **ScholarOne Manuscripts** (confirm current link) |
| Owner / publisher | **Population Council** (owner) / **Wiley** (publisher); founded **1975** |
| Review model | **Double-anonymized** (≥2 referees), editorial/committee screen first, ~3-month decision |
| Submission format | **Free Format** first round; APA-style at revision |
| Article types | Research Article (~8,000–10,000 words) · Notes & Commentary · Data & Perspectives · Archives · Book Review |
| Fees | **No author fees / no APC** under the standard model (Online Open APC optional) |
| Data policy | **Data availability statement** + persistent IDs (Wiley framework); reproducible code |

## 8. Cautions
1. **Verify volatile specifics** (current editors, exact caps, fee/Online Open options, portal link,
   data-policy wording, Free Format scope) on the official Wiley / Population Council pages — they
   change; unverified items are marked 待核实.
2. **Connect population to development** — a clean estimate alone is off-fit; state the social,
   economic, or environmental meaning of the population quantity.
3. **Match the method to the question** — life tables, decomposition, event history, APC, projections,
   and causal designs each answer different questions; pick deliberately.
4. **Respect data licenses** — DHS and census microdata are often not redistributable; share extract
   code, not raw microdata.
5. **Build the reproducibility materials as you go** — a data availability statement plus runnable,
   commented code in a FAIR repository, with seeds for any simulation.
