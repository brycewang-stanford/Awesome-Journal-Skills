# External Tools & Resources for Demography-Style Population Science

Data sources, software, and packages useful when preparing a *Demography* submission. Demography is a
**multidisciplinary population-science** journal: a submission may be formal demography, fertility,
mortality, migration, family/households, health and aging, or population dynamics, drawn from
anthropology, biology, economics, epidemiology, geography, history, psychology, public health,
sociology, or statistics. Match tools to your question and the demographic method. Check licenses and
current access terms before use, and verify any Demography-specific policy in
[`official-source-map.md`](official-source-map.md).

## 1. Population data sources by domain

### Mortality, fertility & longevity
| Source | Provider | Typical use |
|--------|----------|-------------|
| Human Mortality Database (HMD) | UC Berkeley / MPIDR | Life tables, death rates, cohort/period mortality |
| Human Fertility Database (HFD) | MPIDR / VID | Age-specific fertility, parity, tempo/quantum |
| WHO Mortality Database / GBD | WHO / IHME | Cause-of-death, global burden, comparative mortality |
| US CDC WONDER / NCHS Vital Statistics | CDC | US births, deaths, period rates |

### Surveys, cohorts & censuses
| Source | Provider | Typical use |
|--------|----------|-------------|
| IPUMS (USA / International / CPS / DHS / NHIS) | University of Minnesota | Harmonized census/survey microdata |
| Demographic and Health Surveys (DHS) | USAID / ICF | Fertility, child health, mortality in LMICs |
| HRS / ELSA / SHARE | NIA / consortia | Aging, health, retirement panels |
| PSID / NLSY | ISR Michigan / BLS | Longitudinal family, income, life-course data |
| Add Health, Fragile Families (FFCWS) | UNC / Princeton | Life-course, family demography |

### Migration, spatial & projections
| Source | Provider | Typical use |
|--------|----------|-------------|
| UN World Population Prospects (WPP) | UN DESA | Estimates and projections, by country/age/sex |
| Eurostat / national statistical offices | Eurostat / NSOs | Migration flows, population registers |
| Global Bilateral Migration / IMAGE | World Bank / academic | International migration stocks and flows |
| Geo-referenced data (GADM, WorldPop, gridded pop.) | various | Spatial demography, small-area estimation |

## 2. Software by demographic method

### R (widely used in formal demography)
- Life tables & mortality: `demography`, `DemoTools`, `MortalityLaws`, `lifecontingencies`, `LifeTables`
- Fertility / tempo-quantum: `tempo`, `HMDHFDplus` (pull HMD/HFD), `bayesTFR`
- Event history / survival: `survival`, `eha`, `flexsurv`, `survminer`, `mstate` (multistate)
- Age-period-cohort: `apc`, `Epi` (APC), `bamp`; identification-aware models
- Decomposition: `DemoDecomp` (Horiuchi/stepwise, Arriaga, Kitagawa), `DemoTools`
- Projections / microsimulation: `bayesPop`, `MicSim`, `socsim` interfaces
- Standardization & rates: `epitools`, `popEpi`, `PHEindicatormethods`

### Stata
- Survival/event history: `stset`, `streg`, `stcox`, `stcompet` (competing risks)
- Decomposition: `mvdcmp`, Oaxaca-type `oaxaca`; standardization `dstdize`/`istdize`
- Demographic rates and survey design: `svy:` estimators for complex samples

### Python
- `pandas`, `numpy`, `statsmodels`, `lifelines` (survival), `scikit-survival`
- Microsimulation / agent-based: `mesa`, custom cohort-component models
- Plotting: `matplotlib` / `seaborn`; mapping: `geopandas`

### Specialized demographic tools
- **HMD/HFD protocols** (Methods Protocol) for consistent life-table and fertility estimation
- **MORTPAK** and **UN Spectrum/DemProj** for population estimates and projections
- **SOCSIM** / **APC** microsimulation traditions for kinship and cohort dynamics

## 3. Distinctive demographic methods (match to design)
- **Life tables** (period and cohort), abridged vs. complete; multiple-decrement and multistate tables
- **Decomposition** of differences/changes in rates (Kitagawa, Arriaga, Horiuchi continuous, Das Gupta)
- **Event-history / survival analysis** (Cox, parametric, discrete-time, competing risks, multistate)
- **Age-period-cohort** models (be explicit about the identification problem and the constraints used)
- **Standardization** (direct/indirect) and decomposition of standardized rates
- **Microsimulation** and **cohort-component projections**; stable/stationary population theory
- **Kinship models** (matrix demography, e.g., the Goodman-Keyfitz-Pullum / Caswell traditions)

## 4. Reproducibility & data deposit
- Demography requires a **data availability statement** and encourages **reproducible code**; the
  journal **hosts no repository** — deposit in a FAIR repository (see `demog-data-and-reproducibility`)
- Repositories: **ICPSR / openICPSR**, **Harvard Dataverse**, **Zenodo**, **OSF**; find one via
  **FAIRsharing.org** and **re3data.org**
- Pin versions: `renv` (R), `requirements.txt` / `pip freeze` (Python), recorded `ssc`/`net` (Stata);
  set and report seeds for simulation/microsimulation; one master script regenerates every exhibit

## 5. Figures & exhibits (Demography rewards clear demographic graphics)
- **Population pyramids** (age-sex structure), **Lexis surfaces/diagrams** (age x period x cohort),
  **survival/hazard curves**, **age schedules** of fertility/mortality/migration
- Coefficient/marginal-effects plots; small-multiple maps for spatial variation (`sf`, `tmap`)
- Colorblind-safe palettes, grayscale-legible, vector output (PDF/EPS); self-contained titles/notes

## 6. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote — format **loosely to APA** (Demography's house
  style); Merriam-Webster spelling
- Typesetting: LaTeX (TeX Live / MacTeX / Overleaf) or Word; prepare a **double-blind** manuscript
  (avoid self-identifying references) plus required front matter (abstract <= 200 words, <= 5 keywords,
  3-5 highlights)

## 7. Process & portal
| Item | Note |
|------|------|
| Submission portal | **ScholarOne Manuscripts** (since May 31, 2024 — confirm current link) |
| Owner / publisher | **Population Association of America (PAA)** / **Duke University Press** |
| Review model | **Double-blind** — avoid self-identifying references |
| Access model | **Subscribe to Open (S2O)** — free to readers; not an APC journal |
| Article types | Research Article (<= 8,000 words) · Research Note (<= 4,000) · Commentary (<= 2,000) |
| Front matter | Abstract **<= 200 words**; **up to 5 keywords**; **3-5 highlights** (<= 85 chars each) |
| Fees | **$35 submission** + **$1,000 editorial-management at acceptance** (both waivable; not an OA APC) |
| Data policy | **Data availability statement** at acceptance + persistent IDs; reproducible code encouraged |

## 8. Cautions
1. **Verify volatile specifics** (editor, exact caps, fee amounts/waivers, which volume is open this
   year, portal link, data-policy wording) on the official PAA/Duke pages — they change; unverified
   items are marked 待核实.
2. **The $1,000 fee is not an open-access charge** — Demography is free to read under S2O; do not
   describe it as an APC.
3. **Match the method to the demographic question** — life tables, decomposition, event history, APC,
   multistate, and microsimulation each answer different questions; pick deliberately.
4. **Be explicit about identification** — especially the **age-period-cohort** identification problem;
   state the constraint or model assumption you rely on.
5. **Build the reproducibility materials as you go** — a data availability statement plus runnable,
   commented code deposited in a FAIR repository, with seeds for any simulation.
