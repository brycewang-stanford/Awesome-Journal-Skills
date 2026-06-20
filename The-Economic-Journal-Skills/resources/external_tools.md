# External Tools & Resources for The Economic Journal (EJ)

Data sources, software, and packages useful when preparing a *The Economic Journal* (EJ)
submission. EJ is the **Royal Economic Society's** flagship general-interest journal (founded
1891, published by **Oxford University Press**), so a typical paper pairs a **substantial,
broadly interesting economic question** with **credible identification and fully reproducible
code**. Because EJ runs a **pre-acceptance reproducibility check** via the **EJ Data Editor**
(DCAS-endorsed; accepted packages deposited to **Zenodo**), build the replication package as you
go. Check licenses and current access terms before use; verify volatile process specifics on the
official OUP/RES pages.

## 1. Data sources

### Public-use micro & macro
| Source | Provider | Typical use |
|--------|----------|-------------|
| IPUMS (CPS, ACS, USA, International) | University of Minnesota | Labor, demography, life-cycle inputs |
| FRED / ALFRED | St. Louis Fed | Macro time series, real-time vintages |
| PSID / NLSY / Understanding Society | U. Michigan / BLS / ISER (UK) | Dynamic/structural estimation, life-cycle |
| World Bank WDI / Microdata, LSMS | World Bank | Development, cross-country quantitative work |
| Eurostat / UK Data Service / ONS | EU / UK | European & UK applied work (EJ's strong base) |
| Compustat / CRSP (licensed) | WRDS | Firm dynamics, finance, IO calibration targets |

### Experimental & own-data
| Source | Provider | Typical use |
|--------|----------|-------------|
| AEA RCT Registry | AEA | Pre-registration of field experiments |
| AsPredicted | Wharton Credibility Lab | Pre-registration of lab/online studies |
| OSF Registries | Center for Open Science | Pre-registration + materials hosting |
| oTree / Qualtrics / Prolific | Various | Running lab-in-the-field, online experiments and surveys |

> Pre-register own-data studies and include instructions/materials; document deviations.

## 2. Statistical & computational software

### Empirical micro / econometrics
- Stata: `reghdfe`, `ivreghdfe`, `csdid`/`did_multiplegt_dyn` (modern DID),
  `rdrobust`/`rddensity` (RDD), `boottest` (wild-cluster), `gmm`
- R: `fixest`, `did`, `rdrobust`, `gmm`/`momentfit`, `sandwich`/`clubSandwich`
- Python: `linearmodels`, `statsmodels`, `doubleml`/`econml` (causal ML)

### Structural / computational
- Julia: `Optim.jl`, `JuMP`, `ForwardDiff.jl`, `QuantEcon.jl`
- MATLAB: Dynare (DSGE estimation), custom solvers
- Python: `numpy`/`scipy`, `numba`/`jax`, `estimagic` (structural estimation, MSM/MLE), `QuantEcon`
- Report the solver, tolerances, and starting values used

### Reproducibility tooling (build for the EJ Data Editor)
- Pin versions: `renv.lock` (R), `requirements.txt`/`conda env` (Python),
  `Project.toml`/`Manifest.toml` (Julia), recorded Stata `ssc`/`net` versions
- One master script (`run_all`) regenerating every table, figure, and in-text number from raw data
- Set and report seeds for simulation / bootstrap / randomization inference
- Provide complete variable documentation; if data are in a proprietary format (e.g., Stata `.dta`),
  also provide an ASCII/plain-text version such as CSV.

## 3. Strategy toolkit by paper type

| Paper type | Core checks | Tools |
|------------|-------------|-------|
| Empirical (applied micro/macro) | Causal-design diagnostics (pre-trends / density / first-stage / balance), modern DID estimators, clustered/robust inference, external validity | `csdid`, `rdrobust`, `ivreghdfe`, `boottest` |
| Structural / computational | Identification of parameters, fit to targeted/untargeted moments, solver/tolerance reporting, counterfactual validity | Dynare, `estimagic`, `QuantEcon`, SMM/MSM code |
| Theory | Sharp comparative statics, existence/uniqueness, welfare, intuition stated in words | LaTeX, symbolic tools |
| Experimental | Pre-registration, instructions/materials, balance, attrition, MHT correction | AEA RCT Registry, `ritest`, OSF |

## 4. Figures & tables (EJ house rules)
- Report **economic magnitudes** (mean-relative effect, elasticity, welfare), not stars alone.
- Make every exhibit **self-contained and legible to a generalist** — EJ's broad-interest, exposition-first identity.
- Event-study plots, model-fit overlays, and counterfactual curves with confidence bands; avoid chartjunk.
- For a **short paper** (AER:Insights style), keep within ~5 exhibits and push the rest to the online appendix.

## 5. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX. EJ uses an **author-date** style; arrange references
  alphabetically and then chronologically for each author. Cite datasets and replication packages
  where relevant.
- Typesetting: LaTeX (TeX Live / MacTeX / Overleaf) or Word; submit as a **single PDF** including appendices.
- Accepted-author metadata: short title <=40 characters, abstract <=100 words, keywords <=20
  characters each.
- Acknowledge all sources of research funding in the manuscript.

## 6. Process & portal (verify on the official OUP/RES pages)
| Item | Note |
|------|------|
| Submission portal | **Editorial Express** (editorialexpress.com) — NOT ScholarOne; single PDF incl. appendices |
| Review model | **Single-blind** — referees anonymous to authors; authors not anonymized |
| Format options | Full-length article, or **short paper (AER:Insights style, <6,000 words, ~5 exhibits)** |
| Metadata | JEL classification codes + keywords entered in Editorial Express |
| Replication | RES/EJ data-and-code policy (DCAS-endorsed); EJ Data Editor pre-acceptance check; **Zenodo** deposit |
| Restricted data | Request exemption **at first submission** |
| Submission fee | RES charges new EJ submissions; current fee depends on membership category and is plus VAT; resubmissions are fee-exempt |
| Funding | All research funding sources acknowledged in the manuscript |

## 7. Cautions
1. **Verify volatile specifics** (editor roster, submission fees, OA/colour charges, and special calls)
   on the official OUP/RES pages — they change.
2. **Reproducibility is checked before final acceptance** — assemble raw data, code, and
   documentation early; provide an ASCII companion for proprietary-format data.
3. **Respect data licenses**; for proprietary or restricted data, request the exemption at **first** submission.
4. **EJ's bar is broad interest** — match the framing and exposition to a generalist economist, not only your subfield.
