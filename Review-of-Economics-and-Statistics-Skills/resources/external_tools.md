# External Tools & Resources for The Review of Economics and Statistics (REStat)

Data sources, software, and packages useful when preparing a *The Review of
Economics and Statistics* (REStat) submission. REStat is the MIT Press journal of
**applied economics and applied econometrics** edited at the Harvard Kennedy School,
with a long **measurement tradition**, so a typical paper pairs a substantive
applied question with **credible identification**, **careful measurement**, and a
**reproducible data-and-code package** deposited to the **REStat Harvard Dataverse**.
Build the replication package as you go. Check licenses and current access terms
before use; live-check volatile process specifics on the official MIT Press REStat pages
before submission.

## 1. Data sources

### Public-use micro & macro
| Source | Provider | Typical use |
|--------|----------|-------------|
| IPUMS (CPS, ACS, USA, International) | University of Minnesota | Labor, demography, education, public economics |
| FRED / ALFRED | St. Louis Fed | Macro time series, real-time vintages |
| PSID / NLSY | U. Michigan / BLS | Household dynamics, life-cycle, intergenerational work |
| World Bank WDI / Microdata, LSMS, DHS | World Bank / USAID | Development, health, cross-country applied work |
| Compustat / CRSP (licensed) | WRDS | Firm-level IO, finance, trade applications |
| UN Comtrade / BACI | UN / CEPII | International trade flows, shift-share exposure designs |

### Linked / administrative & restricted (note REStat's data policy)
| Source | Provider | Typical use |
|--------|----------|-------------|
| Census FSRDC | U.S. Census Bureau | Restricted-access linked employer–employee, firm data |
| Tax / social-security administrative data | National statistical agencies | Earnings, program participation (often proprietary) |

> REStat Data and Code Availability Policy: post data and code with documented
> README files **before publication**, sufficient to permit replication. For
> **proprietary/restricted** data, **indicate at submission** and document how other
> researchers can obtain it; do **not pay the US$125 submission fee** until the
> editorial office confirms compliance.

## 2. Statistical & computational software

### Empirical micro / applied econometrics (REStat's core)
- Stata: `reghdfe`, `ivreghdfe`, `csdid` / `did_multiplegt_dyn` (heterogeneity-robust
  DID), `eventdd`, `rdrobust` / `rddensity` (RDD), `boottest` (wild-cluster),
  `ppmlhdfe` (gravity/trade), `bartik_weight`
- R: `fixest`, `did`, `rdrobust`, `HonestDiD`, `sandwich` / `clubSandwich`,
  `ShiftShareSE`, `fwildclusterboot`
- Python: `linearmodels`, `statsmodels`, `doubleml` / `econml` (causal ML),
  `pyfixest`

### Measurement & data-quality tooling (REStat-signature)
- Reliability / attenuation: validation-sample estimators, errors-in-variables
  (`eivreg`), bounds for non-classical measurement error
- Index construction & validation: principal-components / factor tooling, external
  benchmarking against an independent measure
- Record linkage: `reclink` / `ftfy` / probabilistic matching for built measures

### Reproducibility tooling (build for the Harvard Dataverse deposit)
- Pin versions: `renv.lock` (R), `requirements.txt` / `conda env` (Python), recorded
  Stata `ssc` / `net` package versions
- One master script (`00_run_all`) regenerating every table and figure from raw data
- Set and report seeds for simulation / bootstrap / randomization inference

## 3. Strategy toolkit by paper type

| Paper type | Core checks | Tools |
|------------|-------------|-------|
| Applied causal (DID/RD/IV) | Heterogeneity-robust DID, density/manipulation, first-stage strength, clustered inference | `csdid`, `rdrobust`, `ivreghdfe`, `boottest` |
| Shift-share / exposure | Share- vs shock-exogeneity, correct exposure-design SEs | `bartik_weight`, `ShiftShareSE` |
| Measurement / new index | Construct validity, attenuation correction, external benchmarking | `eivreg`, factor tooling, validation samples |
| Structural-light applied | Estimand identification, untargeted-moment validation, honest counterfactual | `gmm`, custom solvers |

## 4. Figures & tables (REStat house rules)
- Report **standard errors in parentheses**; significance stars are permitted but
  must **accompany, never replace**, the SE. Self-contained exhibit notes.
- Make the headline result legible from **one main exhibit**; event-study / RD /
  validation figures with confidence bands are persuasive.
- Push supporting detail to the **online appendix (≤20 pages)**; keep the main paper
  self-contained.

## 5. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX. Standard economics house style;
  abstract ≤100 words (JEL-suitable); JEL codes + keywords on the title page.
- Typesetting: LaTeX (TeX Live / MacTeX / Overleaf) or Word; submit as **PDF**,
  12-point, double-spaced throughout.

## 6. Process & portal (verify on the official MIT Press REStat pages)
| Item | Note |
|------|------|
| Submission portal | **Editorial Express** (`editorialexpress.com/.../e-submit...?dbase=restat`) |
| Categories | Full-length **Articles**, **Notes**, **Short Papers** (≤6000 words, ≤5 exhibits since Dec 2019) |
| Submission fee | **US$125** nonrefundable per new submission, by credit card; proprietary-data fee held until compliance confirmed |
| Data/code archive | **REStat Harvard Dataverse** (NOT openICPSR, NOT the JAE archive); README permitting replication, before publication |
| Editors (2026) | Will Dobbie (Harvard), Raymond Fisman (Boston U) — co-chairs; confirm full board on the live MIT Press page |

## 7. Cautions
1. **Live-check volatile specifics** (editors, fee, abstract/appendix limits, category
   rules) on the official MIT Press REStat pages; they change.
2. **Use the right archive** — REStat deposits to **Harvard Dataverse**, not
   openICPSR or the JAE archive; mixing these up is a REStat-specific error.
3. **Declare proprietary data at submission** and hold the fee until the editorial
   office confirms policy compliance.
4. **Take measurement seriously** — REStat referees raise measurement-error and
   construct-validity objections that other venues sometimes wave through.
