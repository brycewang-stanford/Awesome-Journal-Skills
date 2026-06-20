# External Tools & Resources for Quantitative Economics (QE)

Data sources, software, and packages useful when preparing a *Quantitative
Economics* (QE) submission. QE is the Econometric Society's empirically and
computationally oriented general-interest journal, so a typical paper combines a
**substantive economic question** with **documented data and fully reproducible
code** — empirical, structural/computational, experimental, or simulation-based.
Because the ES Data Editor runs a **pre-acceptance reproducibility check**
(DCAS-compatible, not the JAE archive), build the replication package as you go.
Check licenses and current access terms before use; verify volatile process
specifics on the official Econometric Society pages.

## 1. Data sources

### Public-use micro & macro
| Source | Provider | Typical use |
|--------|----------|-------------|
| IPUMS (CPS, ACS, USA, International) | University of Minnesota | Labor, demography, structural life-cycle inputs |
| FRED / ALFRED | St. Louis Fed | Macro time series, real-time vintages |
| PSID / NLSY | U. Michigan / BLS | Dynamic/structural estimation, life-cycle |
| World Bank WDI / Microdata, LSMS | World Bank | Development, cross-country quantitative work |
| Compustat / CRSP (licensed) | WRDS | Firm dynamics, finance, IO calibration targets |

### Experimental & own-data (note QE's Jan 2026 rules)
| Source | Provider | Typical use |
|--------|----------|-------------|
| AEA RCT Registry | AEA | Pre-registration of field experiments (QE-accepted registry) |
| AsPredicted | Wharton Credibility Lab | Pre-registration of lab/online studies (QE-accepted) |
| OSF Registries | Center for Open Science | Pre-registration + materials hosting (QE-accepted) |
| oTree / Qualtrics / Prolific / MTurk | Various | Running lab-in-the-field, online experiments and surveys |

> QE (effective Jan 1, 2026): experimental submissions must include detailed
> instructions / survey transcripts **at initial submission**, and studies that
> generate their own data (RCTs, lab / lab-in-the-field, online experiments and
> surveys) must be **pre-registered** in a recognized registry; exemptions need
> prior editor approval.

## 2. Statistical & computational software

### Structural / computational (QE's core)
- Julia: optimization (`Optim.jl`, `JuMP`), automatic differentiation
  (`ForwardDiff.jl`), dynamic models (`QuantEcon.jl`), `DifferentialEquations.jl`
- MATLAB: Dynare (DSGE estimation), CompEcon toolbox, custom solvers
- Python: `numpy`/`scipy`, `numba`/`jax` for fast value-function iteration,
  `interpolation`, `estimagic` (structural estimation, MSM/MLE), `QuantEcon`
- Method-of-simulated-moments / indirect inference / SMM helpers; report the
  solver, tolerances, and starting values used

### Empirical micro / econometrics
- Stata: `reghdfe`, `ivreghdfe`, `csdid`/`did_multiplegt_dyn` (modern DID),
  `rdrobust`/`rddensity` (RDD), `boottest` (wild-cluster), `gmm`
- R: `fixest`, `did`, `rdrobust`, `gmm`/`momentfit`, `sandwich`/`clubSandwich`
- Python: `linearmodels`, `statsmodels`, `doubleml`/`econml` (causal ML)

### Reproducibility tooling (build for the ES Data Editor)
- Pin versions: `renv.lock` (R), `requirements.txt`/`conda env` (Python),
  `Project.toml`/`Manifest.toml` (Julia), recorded Stata `ssc`/`net` versions
- One master script (`run_all`) regenerating every table and figure from raw data
- Set and report seeds for simulation / bootstrap / randomization inference
- For long-running or hard-to-access computations, ship simplified/manageable
  versions and summary output files (QE explicitly encourages this)

## 3. Strategy toolkit by paper type

| Paper type | Core checks | Tools |
|------------|-------------|-------|
| Structural / computational | Identification of parameters, fit to targeted/untargeted moments, solver/tolerance reporting, counterfactual validity | Dynare, `estimagic`, `QuantEcon`, SMM/MSM code |
| Empirical (applied micro/finance) | Causal design diagnostics (pre-trends / density / first-stage / balance), modern DID estimators, clustered/robust inference | `csdid`, `rdrobust`, `ivreghdfe`, `boottest` |
| Experimental | Pre-registration, instructions/transcripts at submission, balance, attrition, MHT correction | AEA RCT Registry, `ritest`, OSF |
| Simulation-based | Documented DGP, seeds, convergence diagnostics, sensitivity to grid/tuning | Julia/Python sim code, profiling |

## 4. Figures & tables (QE house rules)
- **No asterisks or boldface** to denote statistical significance — report
  standard errors and confidence/coverage sets instead.
- Place figures and tables **in-text on the relevant page**, not collected at the
  end; vector output (`.eps`) or `.jpg` preferred for final files.
- Event-study plots, model-fit overlays (data vs. simulated moments), and policy
  counterfactual curves with uncertainty bands; avoid chartjunk.

## 5. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX. QE applies its own house style at
  copyediting, so the submitted manuscript need not pre-conform — keep references
  consistent and complete; entries must be published, in a stable public archive
  (e.g., SSRN), or author-provided at final publication.
- Typesetting: LaTeX (TeX Live / MacTeX / Overleaf); the ES LaTeX template is
  recommended (not required) — see e-publications.org/es/support.

## 6. Process & portal (verify on the official ES pages)
| Item | Note |
|------|------|
| Submission portal | Econometric Society "Online Submission" (ES e-publications); PDF, two attachments allowed (extra files zipped) |
| Membership | ES membership required — at least one author must be a member (join/renew via the ES register page) |
| Submission fee | US$100 regular / US$50 student, paid by card at submission; waived for Econometrica transfers and invited resubmissions; low-income-country exemption; not refunded if rejected without review |
| Econometrica transfer | Optional transfer of the coeditor decision letter, referee reports, and cover letters; QE process is independent; transfer waives the submission fee |
| Replication deposit | ES Data and Code Availability Policy (DCAS-compatible); ES Data Editor reproducibility check **before** acceptance; NOT the JAE Data Archive |
| Open Access | CC BY-NC; post-proof publication fee is based on 50% of production cost per page at the then-current rate, with listed student / low- and lower-middle-income / no-funding discounts |

## 7. Cautions
1. **Verify volatile specifics** (editors, fee, page charge, policy effective
   dates, registry list) on the official Econometric Society pages — they change.
2. **Reproducibility is checked before acceptance** — assemble raw data, code,
   and documentation early; document any partial-check scope in the README.
3. **Respect data licenses**; for proprietary or restricted data, state any
   exemption/limited-access request at **initial** submission (editor discretion).
4. **Match diagnostics to the paper type** — structural fit and identification of
   parameters for computational work; causal-design diagnostics for empirical work.
