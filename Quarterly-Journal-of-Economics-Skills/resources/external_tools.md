# External Tools & Resources for QJE-Style Empirical Micro

Data sources, software, and packages useful when preparing a *Quarterly Journal of
Economics* (QJE) submission — a big empirical-micro question with credible causal
identification (RCT, DID/event study, IV, RDD), an extensive online appendix, and a
reproducible replication package. Check licenses and current access terms before use.

## 1. Data sources

### US administrative & survey micro
| Source | Provider | Typical use |
|--------|----------|-------------|
| IPUMS (CPS, ACS, USA, International) | University of Minnesota | Labor, demography, long-run comparisons |
| Census / IRS restricted data (FSRDC) | US Census Bureau | Firm/worker matched, place effects |
| Opportunity Insights data | Harvard | Mobility, place effects, education |
| PSID / NLSY | U. Michigan / BLS | Life-cycle, intergenerational dynamics |
| HRS | U. Michigan / NIA | Health, aging, retirement |
| LEHD / QWI | US Census Bureau | Employment, earnings dynamics |

### International & development
| Source | Provider | Typical use |
|--------|----------|-------------|
| World Bank WDI / Microdata Library | World Bank | Cross-country, development |
| DHS Program | USAID | Health, demography (developing world) |
| LSMS | World Bank | Household welfare, consumption |
| AEA RCT Registry | AEA | Pre-registration of field experiments |

### Economic history & political economy
| Source | Provider | Typical use |
|--------|----------|-------------|
| Historical censuses (IPUMS, NAPP) | Multiple | Long-run persistence, mobility |
| Replication archives of published QJE/AER papers | Journals / ICPSR | Building on prior natural experiments |
| Digitized administrative records (national archives) | Country-specific | Novel-data identification |

## 2. Statistical software

### Stata (common in empirical micro)
- DID / event study: `csdid` (Callaway–Sant'Anna), `eventstudyinteract` (Sun–Abraham), `did_multiplegt` / `did_multiplegt_dyn` (de Chaisemartin–D'Haultfœuille), `bacondecomp` (Goodman-Bacon)
- IV: `ivreg2`, `ivreghdfe`, weak-IV-robust inference (`weakiv`, `condivreg`)
- RDD: `rdrobust`, `rddensity` (manipulation test), `rdbwselect`
- Fixed effects at scale: `reghdfe`
- Inference: `boottest` (wild-cluster bootstrap), `ritest` (randomization inference), multiple-hypothesis adjustments
- Synthetic control: `synth`, `synth_runner`, `sdid`

### R
- DID / event study: `did` (Callaway–Sant'Anna), `fixest` (`sunab`, fast FE/event study), `didimputation`, `bacondecomp`
- RDD: `rdrobust`, `rddensity`
- IV: `fixest::feols` IV, `ivreg`, weak-IV diagnostics
- Inference: `fwildclusterboot`, `sandwich`/`clubSandwich`
- Synthetic control: `Synth`, `synthdid`, `tidysynth`
- Reproducibility: `renv` (pin package versions), `targets` (pipeline)

### Python
- `pandas`, `numpy` — data wrangling
- `statsmodels`, `linearmodels` (panel IV / FE) — estimation
- `scikit-learn` — ML nuisance functions for double/debiased ML
- `econml`, `doubleml` — heterogeneous/causal ML
- `matplotlib` / `seaborn` — figures; `binsreg` for binscatter
- `pip freeze` / `requirements.txt` — pin the environment

## 3. Identification toolkit by design

| Design | Core checks | Packages |
|--------|-------------|----------|
| Staggered DID | Goodman-Bacon decomposition, modern estimator, event-study leads | `csdid`, `did`, `did_multiplegt_dyn`, `fixest` |
| RDD | McCrary/CJM density, optimal bandwidth, bandwidth robustness | `rdrobust`, `rddensity` |
| IV | First-stage F, weak-IV-robust CIs, reduced form | `ivreg2`, `weakiv`, `linearmodels` |
| RCT | Balance, attrition (Lee bounds), MHT correction | `ritest`, `randcmd`, custom |
| Synthetic control | Donor-pool fit, placebo-in-space/time | `synthdid`, `sdid`, `tidysynth` |

## 4. Figures (QJE is figure-forward)
- Event-study plots, RDD discontinuity plots, binned scatters (`binsreg` / `binscatter2`)
- Confidence bands shown; avoid chartjunk (no 3D, minimal color)
- Vector output (PDF/EPS) for print resolution

## 5. Reproducibility & replication
- Pin software and package versions (`renv.lock`, `requirements.txt`, recorded `ssc`/`net` versions)
- One master script (`run_all`) regenerating every table and figure from raw data
- Set and report random seeds for bootstrap / randomization inference / simulation
- Deposit per the current QJE/data-editor policy (verify on the official page); archive on a stable repository (e.g., ICPSR/openICPSR, Zenodo)

## 6. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote — set to **author-date** style
- Typesetting: LaTeX (TeX Live / MacTeX, Overleaf); OUP submission accepts standard formats — confirm current guidance
- Language polish: keep prose legible to a general-interest reader (see qje-writing-style)

## 7. Process & portal
| Item | Note |
|------|------|
| Submission portal | Editorial Express (`editorialexpress.com/qje`) — PDF only |
| Submission fee | None stated on the official pages (no fee); re-confirm before submitting |
| Replication deposit | Required for accepted empirical papers; verify current data-editor policy |
| Publisher | Oxford University Press |

## 8. Cautions
1. **Verify volatile specifics** (fee, editors, deposit rules, portal URL) on the official journal page — they change.
2. **Respect data licenses**; restricted data (FSRDC, registry data) require formal access and disclosure review.
3. **Match estimator to design** — plain TWFE on staggered timing is a known pitfall.
4. **Reproducibility is checked** — build the package as you go, not at the end.
