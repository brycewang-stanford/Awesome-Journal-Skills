# External Tools & Resources for JHR-Style Applied Micro

Data sources, software, and packages useful when preparing a *Journal of Human
Resources* (JHR) submission — empirical microeconomics with a credible
causal-identification and **public-policy** emphasis across labor, development,
health, the economics of education, discrimination, and retirement. The deliverable
JHR ultimately requires is a **CC0 public-domain replication package** (data, code,
read-me) deposited in an external public repository with a DOI Data Availability
Statement. Check licenses and current access terms before use.

## 1. Data sources (by JHR field)

### Labor, education, retirement (US micro)
| Source | Provider | Typical use |
|--------|----------|-------------|
| IPUMS (CPS, ACS, USA) | University of Minnesota | Employment, wages, schooling, demography |
| Current Population Survey (CPS) | BLS / Census | Labor supply, earnings, policy variation |
| PSID / NLSY79 / NLSY97 | U. Michigan / BLS | Life-cycle earnings, intergenerational links |
| HRS | U. Michigan / NIA | Retirement, aging, Social Security claiming |
| LEHD / QWI (FSRDC) | US Census Bureau | Matched employer-employee earnings dynamics |
| State/district admin education records | State agencies | Test scores, attainment, program effects |

### Health economics
| Source | Provider | Typical use |
|--------|----------|-------------|
| MEPS | AHRQ | Health expenditure, insurance, utilization |
| NHIS / NHANES | CDC/NCHS | Health behaviors, outcomes |
| Vital Statistics (Natality/Mortality) | NCHS | Birth outcomes, mortality, policy shocks |
| Medicaid/Medicare claims (restricted) | CMS / ResDAC | Coverage, treatment, cost |

### Development & discrimination
| Source | Provider | Typical use |
|--------|----------|-------------|
| World Bank Microdata Library / LSMS | World Bank | Household welfare in developing settings |
| DHS Program | USAID | Health/demography in the developing world |
| AEA RCT Registry | AEA | Pre-registration of field experiments (RCTs) |
| Audit/correspondence-study data | Author archives | Discrimination in hiring/housing |

## 2. Statistical software (Stata-first is common in applied labor)

### Stata
- DID / event study: `csdid` (Callaway-Sant'Anna), `eventstudyinteract` (Sun-Abraham), `did_multiplegt_dyn` (de Chaisemartin-D'Haultfoeuille), `bacondecomp` (Goodman-Bacon)
- IV: `ivreg2`, `ivreghdfe`, weak-IV-robust inference (`weakiv`, `condivreg`)
- RDD: `rdrobust`, `rddensity` (manipulation test), `rdbwselect`
- Fixed effects at scale: `reghdfe`
- Inference: `boottest` (wild-cluster bootstrap), `ritest` (randomization inference), `wyoung` / `rwolf` (multiple-hypothesis adjustment)
- Decompositions (wage gaps / discrimination): `oaxaca`, `rif` / RIF-regression, `jmpierce`

### R
- DID / event study: `did`, `fixest` (`sunab`, fast FE/event study), `didimputation`, `bacondecomp`
- RDD: `rdrobust`, `rddensity`
- IV: `fixest::feols` IV, `ivreg`, weak-IV diagnostics
- Inference: `fwildclusterboot`, `sandwich` / `clubSandwich`
- Reproducibility: `renv` (pin package versions), `targets` (pipeline)

### Python
- `pandas`, `numpy` — data wrangling
- `statsmodels`, `linearmodels` (panel IV / FE) — estimation
- `econml`, `doubleml` — heterogeneous/causal ML
- `matplotlib` / `seaborn` — figures; `binsreg` for binscatter
- `pip freeze` / `requirements.txt` — pin the environment

## 3. Identification toolkit by design (applied micro)
| Design | Core checks | Packages |
|--------|-------------|----------|
| Staggered DID | Goodman-Bacon decomposition, modern estimator, event-study leads | `csdid`, `did`, `did_multiplegt_dyn`, `fixest` |
| RDD | McCrary/CJM density, optimal bandwidth, bandwidth robustness | `rdrobust`, `rddensity` |
| IV | First-stage F, weak-IV-robust CIs, reduced form | `ivreg2`, `weakiv`, `linearmodels` |
| RCT | Balance, attrition (Lee bounds), MHT correction, PAP deviations | `ritest`, `randcmd`, `wyoung` |
| Decomposition | Oaxaca-Blinder / RIF for wage and discrimination gaps | `oaxaca`, `rif` |

## 4. Reconciliation & sensitivity (a JHR-specific expectation)
JHR judges papers partly on whether they **reconcile** their estimates with prior
published work and may require comparative estimation and sensitivity tests.
- Re-estimate with the **prior literature's** specification/sample, then yours, side by side
- Specification-curve / multiverse tooling (`specchart`, `speccurve`) to show robustness across reasonable choices
- Sensitivity to unobservables: `psacalc` / Oster (2019) coefficient-stability bounds

## 5. Reproducibility & replication (JHR CC0 deposit)
- One master script (`run_all`) regenerating every table and figure from raw data
- A **read-me** file mapping each exhibit to the code that produces it (required)
- Pin software/package versions (`renv.lock`, `requirements.txt`, recorded `ssc`/`net` versions)
- Set and report random seeds for bootstrap / randomization inference / simulation
- Deposit data + code in a **public repository** — examples JHR names: **ICPSR**, the **Dataverse Project**, or an **institutional repository** — released under **CC0 1.0 Universal**, with a **persistent (DOI) link**
- Provide an **archive plan footnote** at submission and a **Data Availability Statement** on the title page; for proprietary data, request a **waiver at initial submission** with a path for others to obtain the data

## 6. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote
- Typesetting: LaTeX (TeX Live / MacTeX, Overleaf) or Word — keep within the 40-page (12pt, 1.5-spacing) limit; push overflow to an Online Appendix
- The specific manuscript citation style is not named on the official pages (待核实) — follow the live guidance

## 7. Process & portal
| Item | Note |
|------|------|
| Submission portal | http://jhr.msubmit.net — do NOT email the editor/office directly |
| Submission fee | Nonrefundable; $175 on the live Authors page ($150 in the Sept-2024 PDF) — verify before paying; hardship exemption may be requested |
| Length | Page-count limit (40 pp incl. refs/tables/figs; 50 if double-spaced), not word count |
| Review | Single-anonymous; fast desk-reject possible without outside review |
| Replication deposit | Required for accepted papers; CC0 in ICPSR/Dataverse/institutional repo |
| Publisher | University of Wisconsin Press (IRP, UW-Madison) |

## 8. Cautions
1. **Scope first.** JHR is empirical microeconomics, NOT "HR management." Out-of-scope (management/personnel) papers are desk-rejected and the fee is **not refunded**. Confirm fit before paying.
2. **Verify volatile specifics** (Editor, fee amount, page limit, deposit rules) on the official page — they change; the Editor changes on 2026-07-01.
3. **Respect data licenses**; restricted data (FSRDC, CMS/ResDAC, registry data) require formal access and IRB/disclosure review (disclose IRB status per author).
4. **Match estimator to design** — plain TWFE on staggered timing is a known pitfall.
5. **Build the CC0 package as you go**, not at the end; resolve any proprietary-data waiver at the time of initial submission.
