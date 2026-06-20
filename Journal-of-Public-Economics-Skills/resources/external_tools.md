# External Tools & Resources for JPubE-Style Public Economics

Data sources, software, and packages useful when preparing a *Journal of Public
Economics* (JPubE) submission — typically a tax, transfer, social-insurance, public-
expenditure, or fiscal-policy question identified off administrative or policy
variation, with a transparent design and (often) a welfare or sufficient-statistics
interpretation. Check licenses, disclosure/IRB requirements, and current access
terms before use. Live-check operational journal specifics (fee, required fields,
research-data wording) on the official Guide for Authors before upload.

## 1. Data sources

### Tax, transfer & administrative micro
| Source | Provider | Typical use |
|--------|----------|-------------|
| IRS / Statistics of Income (SOI), restricted IRS data | US Treasury / Census FSRDC | Tax responses, EITC, bunching at kinks |
| LEHD / QWI, administrative employer-employee data | US Census Bureau | Earnings, UI, labor-supply responses |
| Social Security / DI / SSI records | SSA (restricted) | Disability, retirement, social insurance |
| Scandinavian / European population registers | National statistical agencies | Whole-population tax & transfer designs |
| TAXSIM | NBER | Simulating federal + state tax liabilities / MTRs |

### Public expenditure, health & local public finance
| Source | Provider | Typical use |
|--------|----------|-------------|
| Medicaid / Medicare / MAX / CMS data | CMS (restricted) | Health insurance, public-program effects |
| Census of Governments, ACS, SAIPE | US Census Bureau | Local public finance, redistribution |
| OECD Tax Database, OECD.Stat | OECD | Cross-country tax & expenditure comparisons |
| World Bank WDI / Microdata Library | World Bank | Development public finance, incidence |

### Policy variation & program rules
| Source | Provider | Typical use |
|--------|----------|-------------|
| Tax Policy Center / NBER TAXSIM parameters | TPC / NBER | Reform-induced variation, marginal rates |
| University of Kentucky Center for Poverty Research (UKCPR) policy database | UKCPR | State transfer-program rules over time |
| AEA RCT Registry | AEA | Pre-registration of field experiments |

## 2. Statistical software

### Stata (common in public economics)
- DID / event study: `csdid` (Callaway–Sant'Anna), `eventstudyinteract` (Sun–Abraham), `did_multiplegt_dyn` (de Chaisemartin–D'Haultfœuille), `bacondecomp` (Goodman-Bacon)
- Bunching estimators: `bunching` (Cattaneo et al.), polynomial-counterfactual bunching code (Chetty/Saez/Kleven lineage) for kinks and notches
- IV: `ivreg2`, `ivreghdfe`, weak-IV-robust inference (`weakiv`, `condivreg`)
- RDD / RKD: `rdrobust`, `rddensity` (manipulation test), `rdbwselect`, kink (RKD) variants
- Fixed effects at scale: `reghdfe`
- Inference: `boottest` (wild-cluster bootstrap), `ritest` (randomization inference)
- Tax simulation: NBER TAXSIM via `taxsim35`

### R
- DID / event study: `did`, `fixest` (`sunab`, fast FE/event study), `didimputation`, `bacondecomp`
- RDD / RKD: `rdrobust`, `rddensity`
- IV: `fixest::feols` IV, `ivreg`, weak-IV diagnostics
- Inference: `fwildclusterboot`, `sandwich` / `clubSandwich`
- Reproducibility: `renv` (pin versions), `targets` (pipeline)

### Python
- `pandas`, `numpy` — data wrangling
- `statsmodels`, `linearmodels` (panel IV / FE) — estimation
- `econml`, `doubleml` — heterogeneous / causal ML for treatment effects
- `matplotlib` / `seaborn` — figures; `binsreg` for binscatter / bunching plots

## 3. Identification toolkit by design (public-economics flavored)
| Design | Core checks | Packages |
|--------|-------------|----------|
| Bunching at kinks/notches | Excess-mass estimate, counterfactual fit, elasticity recovery, round-number diagnostics | `bunching`, custom polynomial code |
| RKD (regression kink) | Slope-change identification, placebo kinks, bandwidth robustness | `rdrobust` (kink), `rddensity` |
| Staggered DID (reform rollout) | Goodman-Bacon decomposition, modern estimator, event-study leads | `csdid`, `did`, `did_multiplegt_dyn` |
| IV (policy instrument) | First-stage F, weak-IV-robust CIs, reduced form, exclusion argument | `ivreg2`, `weakiv`, `linearmodels` |
| Sufficient statistics | Map estimated elasticities to a welfare formula; state primitives held fixed | analytics + `bootstrap` for SEs |

## 4. Figures (JPubE is figure-forward for design transparency)
- Bunching density plots (observed vs. smooth counterfactual around a kink/notch)
- Event-study and RKD/RD discontinuity plots with confidence bands
- Binned scatters (`binsreg` / `binscatter2`); incidence / distributional plots
- Vector output (PDF/EPS) for print; minimal chartjunk

## 5. Reproducibility & data (Elsevier Option C)
- Deposit research data in a relevant repository, cite/link the dataset in the article, or state why research data cannot be shared
- Provide a **data-availability statement**; where data are open, link a repository (e.g., Mendeley Data, ICPSR/openICPSR, Zenodo) and include code to regenerate results
- Pin software/package versions; one master script (`run_all`) rebuilding every table and figure
- Restricted tax/health/register data: document the access path; supply programs even when microdata are proprietary

## 6. Writing, references & submission
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote — set to **author-date (name-and-year)**
- Typesetting: LaTeX (.tex accepted; double-column allowed) or Word (single-column); supply editable source files
- Submission portal: **Editorial Manager** (Elsevier); optional **SSRN** preprint at submission
- Fee: **US$165** unsolicited / **US$82.50** students / **waived** for article-transfer submissions

## 7. Cautions
1. **Live-check operational specifics** (fee, editor roster, upload fields, data-policy wording) on the official Guide for Authors before upload.
2. **Respect data licenses and disclosure review** — IRS/SSA/CMS and register data require formal access and output clearance.
3. **Match estimator to design** — plain TWFE on staggered reform timing is a known pitfall; bunching needs a defensible counterfactual.
4. **Build the replication package as you go**, not at the end.
