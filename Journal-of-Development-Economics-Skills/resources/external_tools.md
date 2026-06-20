# External Tools & Resources for JDE-Style Development Economics

Data sources, software, and packages useful when preparing a *Journal of Development Economics*
(JDE) submission — empirical and theoretical work on low- and middle-income economies with credible
identification (RCT / field experiment, DID/event study, IV, RDD), an extensive online appendix, a
pre-registered or pre-results-reviewed design where applicable, and a mandatory replication package
deposited to Mendeley Data. Check licenses and current access terms before use.

## 1. Data sources (developing-country emphasis)

### Household & welfare micro
| Source | Provider | Typical use |
|--------|----------|-------------|
| LSMS / LSMS-ISA | World Bank | Household consumption, poverty, agriculture in LMICs |
| DHS Program | USAID | Health, fertility, nutrition, child mortality |
| World Bank Microdata Library | World Bank | Surveys across developing countries |
| WDI / World Development Indicators | World Bank | Cross-country growth, poverty, macro-development |
| IPUMS International | U. Minnesota | Harmonized census micro for many LMICs |

### Experiments, registries & impact evaluation
| Source | Provider | Typical use |
|--------|----------|-------------|
| AEA RCT Registry | AEA | Pre-registration of field experiments (required practice) |
| OSF Registries | Center for Open Science | Pre-analysis plans, pre-results material |
| J-PAL / IPA project data | J-PAL / IPA | RCT datasets and design references |
| 3ie Development Evidence Portal | 3ie | Impact-evaluation evidence base |

### Macro, trade, institutions, agriculture
| Source | Provider | Typical use |
|--------|----------|-------------|
| Penn World Table | Groningen | Cross-country growth and development accounting |
| FAOSTAT | FAO | Agriculture, food, land in developing economies |
| Afrobarometer / Latinobarómetro | Survey consortia | Institutions, governance, attitudes |
| Geo-referenced data (DHS GPS, nightlights, PRIO-GRID) | Various | Spatial development, conflict, market access |

## 2. Statistical software

### Stata (dominant in applied development micro)
- DID / event study: `csdid` (Callaway–Sant'Anna), `eventstudyinteract` (Sun–Abraham), `did_multiplegt` / `did_multiplegt_dyn` (de Chaisemartin–D'Haultfœuille), `bacondecomp` (Goodman-Bacon)
- IV: `ivreg2`, `ivreghdfe`, weak-IV-robust inference (`weakiv`, `condivreg`)
- RDD: `rdrobust`, `rddensity` (manipulation test), `rdbwselect`
- Fixed effects at scale: `reghdfe`
- Inference: `boottest` (wild-cluster bootstrap for few clusters), `ritest` (randomization inference for RCTs), `randcmd`; multiple-hypothesis adjustments (`wyoung`, `rwolf`)
- Power / design: `power`, `clustersampsi`, simulation-based MDE for clustered RCTs

### R
- DID / event study: `did` (Callaway–Sant'Anna), `fixest` (`sunab`, fast FE/event study), `didimputation`, `bacondecomp`
- RDD: `rdrobust`, `rddensity`, `rdpower` (RD power calculations)
- IV: `fixest::feols` IV, `ivreg`, weak-IV diagnostics
- Inference: `fwildclusterboot`, `sandwich`/`clubSandwich`, `multcomp` (MHT)
- Power: `DeclareDesign` (design diagnosis), `pwr`
- Reproducibility: `renv` (pin package versions), `targets` (pipeline)

### Python
- `pandas`, `numpy` — data wrangling
- `statsmodels`, `linearmodels` (panel IV / FE) — estimation
- `scikit-learn` — ML nuisance functions for double/debiased ML
- `econml`, `doubleml` — heterogeneous/causal ML (heterogeneous treatment effects across subgroups)
- `matplotlib` / `seaborn` — figures; `binsreg` for binscatter
- `pip freeze` / `requirements.txt` — pin the environment

## 3. Identification toolkit by design

| Design | Core checks | Packages |
|--------|-------------|----------|
| RCT / field experiment | Pre-analysis plan, balance, attrition (Lee bounds), MHT correction, randomization inference, power/MDE | `ritest`, `randcmd`, `wyoung`, `DeclareDesign` |
| Staggered DID | Goodman-Bacon decomposition, modern estimator, event-study leads | `csdid`, `did`, `did_multiplegt_dyn`, `fixest` |
| RDD | McCrary/CJM density, optimal bandwidth, bandwidth robustness | `rdrobust`, `rddensity`, `rdpower` |
| IV | First-stage F, weak-IV-robust CIs, reduced form | `ivreg2`, `weakiv`, `linearmodels` |

## 4. Figures (JDE rewards figure-forward exhibits)
- Event-study plots, RDD discontinuity plots, binned scatters (`binsreg` / `binscatter2`)
- Treatment-effect-by-subgroup plots for heterogeneity in LMIC samples
- Confidence bands shown; avoid chartjunk (no 3D, minimal color); maps/spatial figures where geography matters
- Vector output (PDF/EPS) for print resolution

## 5. Reproducibility & replication (mandatory at JDE)
- Pin software and package versions (`renv.lock`, `requirements.txt`, recorded `ssc`/`net` versions)
- One master script (`run_all`) regenerating every table and figure from raw (or constructed) data
- Set and report random seeds for bootstrap / randomization inference / simulation
- A README documenting data provenance, construction steps, and how to reproduce each exhibit
- **Deposit data, programs, and computational details to Mendeley Data** (JDE's hosting partner), posted alongside the published article; verify the current policy on the official page
- For restricted/proprietary survey data (e.g., government microdata), provide the programs and a clear access path even if raw data cannot be redistributed

## 6. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote — JDE accepts any consistent style at submission (applied at the proof stage), so set author-date and keep it consistent
- Use American or British English consistently, not a combination of both
- Typesetting: LaTeX (TeX Live / MacTeX, Overleaf) or Word; Elsevier accepts standard formats — confirm current guidance
- Citations use author-date (single author: name + year; two authors: both names + year; three or more: first author + "et al." + year)

## 7. Process & portal
| Item | Note |
|------|------|
| Submission portal | Editorial Manager (Elsevier) — confirm current URL in the Guide for Authors |
| Submission fee | None for standard subscription publication; optional open-access APC applies only after acceptance (verify current figure) |
| Review model | Single anonymized (referees know author identity; author does not know referees) |
| Pre-results review | Permanent Registered Reports track (Stage 1 proposal → in-principle acceptance → Stage 2), run with BITSS |
| Short-paper track | AER: Insights-style limited-revision track (≤6,000 words, ≤5 exhibits, ≤20-page appendix) |
| Submission cap | No more than three papers per author within any 12-month period |
| Replication deposit | Mandatory for accepted empirical/simulation/experimental papers; hosted on Mendeley Data |
| Publisher | Elsevier |

## 8. Cautions
1. **Verify volatile specifics** (APC, editors, deposit rules, portal URL, review model) on the official journal page — they change, and several Elsevier pages are not machine-readable.
2. **Respect data licenses**; restricted government/survey microdata require formal access and disclosure review, but the programs must still be shared.
3. **Match estimator to design** — plain TWFE on staggered timing is a known pitfall; cluster inference at the level of randomization in clustered RCTs.
4. **Reproducibility is checked** — data/code can be requested at the review stage, so build the package as you go, not at the end.
5. **Mind the submission cap** — do not exceed three submissions in any 12-month window.
