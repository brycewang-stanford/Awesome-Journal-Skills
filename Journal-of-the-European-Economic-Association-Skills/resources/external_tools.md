# External Tools & Resources for JEEA

Data sources, software, and packages useful when preparing a *Journal of the
European Economic Association* (JEEA) submission. JEEA is the **EEA's
general-interest journal** (published by Oxford University Press), so a typical
paper pairs a **substantive, general-interest economic question** with execution
that clears a strong bar — a credible empirical design **or** a disciplined
theory/structural model — and, for empirical work, **documented data and fully
reproducible code**. Because the **JEEA Data Editor verifies replication before
formal acceptance** (DCAS standard, endorsed Feb 2024), build the replication
package as you go. Check licenses and current access terms before use; verify
volatile process specifics on the official EEA / OUP pages (source map refreshed 2026-06-20).

## 1. Data sources

### Public-use micro & macro
| Source | Provider | Typical use |
|--------|----------|-------------|
| IPUMS (CPS, ACS, USA, International) | University of Minnesota | Labor, demography, structural life-cycle inputs |
| Eurostat / OECD.Stat | EU / OECD | European cross-country macro & micro, harmonized indicators |
| FRED / ALFRED | St. Louis Fed | Macro time series, real-time vintages |
| World Bank WDI / Microdata, LSMS | World Bank | Development, cross-country quantitative work |
| Compustat / CRSP (licensed) | WRDS | Firm dynamics, finance, IO calibration targets |
| EU-SILC / SHARE (licensed) | Eurostat / SHARE-ERIC | European income, living conditions, ageing panels |

### Experimental & own-data
| Source | Provider | Typical use |
|--------|----------|-------------|
| AEA RCT Registry | AEA | Pre-registration of field experiments |
| AsPredicted | Wharton Credibility Lab | Pre-registration of lab/online studies |
| OSF Registries | Center for Open Science | Pre-registration + materials hosting |
| oTree / Qualtrics / Prolific | Various | Running lab-in-the-field, online experiments and surveys |

> Include detailed experimental instructions / survey transcripts at submission,
> and pre-register own-data studies in a recognized registry; report deviations.

## 2. Statistical & computational software

### Empirical micro / econometrics
- Stata: `reghdfe`, `ivreghdfe`, `csdid`/`did_multiplegt_dyn` (modern DID),
  `rdrobust`/`rddensity` (RDD), `boottest` (wild-cluster), `gmm`
- R: `fixest`, `did`, `rdrobust`, `gmm`/`momentfit`, `sandwich`/`clubSandwich`
- Python: `linearmodels`, `statsmodels`, `doubleml`/`econml` (causal ML)

### Theory / structural / computational
- Julia: optimization (`Optim.jl`, `JuMP`), automatic differentiation
  (`ForwardDiff.jl`), dynamic models (`QuantEcon.jl`)
- MATLAB: Dynare (DSGE estimation), CompEcon toolbox, custom solvers
- Python: `numpy`/`scipy`, `numba`/`jax` for fast value-function iteration,
  `estimagic` (structural estimation, MSM/MLE), `QuantEcon`
- For analytic theory: report assumptions, proofs (main result in main text),
  and comparative statics with economic interpretation

### Reproducibility tooling (build for the JEEA Data Editor)
- Pin versions: `renv.lock` (R), `requirements.txt`/`conda env` (Python),
  `Project.toml`/`Manifest.toml` (Julia), recorded Stata `ssc`/`net` versions
- One master script (`run_all`) regenerating every table and figure from raw data
- Set and report seeds for simulation / bootstrap / randomization inference
- For long-running or restricted-data computations, document the partial-check
  scope and ship simplified/manageable versions plus summary output files

## 3. Strategy toolkit by paper type

| Paper type | Core checks | Tools |
|------------|-------------|-------|
| Applied micro / development | Causal design diagnostics (pre-trends / density / first-stage / balance), modern DID estimators, clustered/robust inference | `csdid`, `rdrobust`, `ivreghdfe`, `boottest` |
| Theory | Minimal assumptions named, generality vs. tractability, comparative statics with interpretation, proof hygiene | LaTeX, analytic tools |
| Structural / quantitative | Parameter identification, fit to targeted/untargeted moments, solver/tolerance reporting, counterfactual validity | Dynare, `estimagic`, `QuantEcon`, SMM/MSM code |
| Experimental | Pre-registration, instructions/transcripts at submission, balance, attrition, MHT correction | AEA RCT Registry, `ritest`, OSF |

## 4. Figures & tables (JEEA house rules)
- **No asterisks or boldface** to denote statistical significance — report
  standard errors and confidence sets instead.
- Self-contained notes (sample, units, estimator, inference, N); three-line tables.
- Event-study plots, model-fit overlays (data vs. simulated moments), and policy
  counterfactual curves with uncertainty bands; vector output for final files.
- OUP house style is applied at copyediting; the submitted file need not pre-conform.

## 5. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX. JEEA applies OUP house style at
  copyediting; keep references complete and consistent.
- Typesetting: LaTeX (TeX Live / MacTeX / Overleaf); follow the current JEEA
  author guidelines on the OUP page for any template requirements.

## 6. Process & portal (source map refreshed 2026-06-20)
| Item | Note |
|------|------|
| Submission portal | EEA members-only submission flow; after fee payment a "Submit a paper to JEEA" link appears |
| Membership | EEA membership required — the **submitting author** must be a member to submit *and* to resubmit |
| Submission fee | €100 standard, effective Feb 1, 2026; waived if the submitting author and all coauthors are based in low-/middle-income countries (World Bank); non-refundable |
| Review | Single-blind; first read by a co-editor (desk-reject possible); fast-decision target (≈8 weeks where possible) |
| Replication deposit | DCAS-endorsed (since Feb 2024); JEEA Data Editor verifies replication **before** formal acceptance; packages posted to the JEEA Zenodo community; package ZIP submitted through the online data submission platform at Editorial Express |
| Publisher | Oxford University Press; Online ISSN 1542-4774; Print ISSN 1542-4766 |

## 7. Cautions
1. **Live-check volatile specifics** (editors, fee, portal, policy effective dates,
   registry list) on the official EEA / OUP pages — they change.
2. **Replication is checked before acceptance** — assemble raw data, code, and
   documentation early; document any partial-check scope in the README.
3. **Respect data licenses**; for proprietary or restricted data, state any
   exemption/limited-access request at **initial** submission.
4. **Match diagnostics to the paper type** — design diagnostics for empirical
   work; assumption/generality discipline for theory; parameter identification
   and counterfactual validity for structural work.
