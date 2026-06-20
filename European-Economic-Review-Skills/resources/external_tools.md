# External Tools & Resources for the European Economic Review (EER)

Data sources, software, and packages useful when preparing a *European Economic
Review* (EER) submission. EER is **Elsevier's general-interest European economics
journal** (founded 1969), covering **all fields, theory and empirical**, so a typical
paper combines a **broad-interest economic question** with a credible identification
or model and — for empirical/simulation/experimental work — a **reproducible
replication package** (EER's mandatory replication policy requires data, code, and
computational details before publication). Check licenses and current access terms
before use; verify volatile process specifics on the official Elsevier / ScienceDirect
pages (检索于 2026-06；以官网为准).

## 1. Data sources

### Public-use micro & macro
| Source | Provider | Typical use |
|--------|----------|-------------|
| Eurostat / national statistical institutes | EU / member states | European labor, public, regional, macro data |
| IPUMS (CPS, ACS, USA, International) | University of Minnesota | Labor, demography, structural inputs |
| FRED / ALFRED | St. Louis Fed | Macro time series, real-time vintages |
| OECD.Stat, World Bank WDI / Microdata | OECD / World Bank | Cross-country, development, comparative work |
| PSID / NLSY / SOEP / SHARE | Various | Dynamic/structural, life-cycle, panel work |
| Compustat / CRSP / Orbis (licensed) | WRDS / Bureau van Dijk | Firm dynamics, finance, IO calibration targets |

### Experimental & own-data
| Source | Provider | Typical use |
|--------|----------|-------------|
| AEA RCT Registry | AEA | Pre-registration of field experiments |
| AsPredicted | Wharton Credibility Lab | Pre-registration of lab/online studies |
| OSF Registries | Center for Open Science | Pre-registration + materials hosting |
| oTree / Qualtrics / Prolific / MTurk | Various | Running lab, lab-in-the-field, online experiments and surveys |

## 2. Statistical & computational software

### Empirical micro / econometrics
- Stata: `reghdfe`, `ivreghdfe`, `csdid`/`did_multiplegt_dyn` (modern DID), `rdrobust`/`rddensity` (RDD), `boottest` (wild-cluster), `gmm`
- R: `fixest`, `did`, `rdrobust`, `gmm`/`momentfit`, `sandwich`/`clubSandwich`, `HonestDiD`
- Python: `linearmodels`, `statsmodels`, `doubleml`/`econml` (causal ML)

### Macro / quantitative & structural
- MATLAB: Dynare (DSGE estimation), CompEcon toolbox, custom solvers
- Julia: `Optim.jl`, `JuMP`, `QuantEcon.jl`, automatic differentiation (`ForwardDiff.jl`)
- Python: `numpy`/`scipy`, `numba`/`jax`, `estimagic` (MSM/MLE) — report solver, tolerances, starting values

### Reproducibility tooling (build for the mandatory replication policy)
- Pin versions: `renv.lock` (R), `requirements.txt`/`conda env` (Python), `Project.toml`/`Manifest.toml` (Julia), recorded Stata `ssc`/`net` versions
- One master script (`run_all`) regenerating every table and figure from raw data
- Set and report seeds for simulation / bootstrap / randomization inference

## 3. Strategy toolkit by paper type

| Paper type | Core checks | Tools |
|------------|-------------|-------|
| Applied micro / labor / public | Causal-design diagnostics (pre-trends / density / first-stage / balance), modern DID, clustered/robust inference | `csdid`, `rdrobust`, `ivreghdfe`, `boottest`, `HonestDiD` |
| Macro / quantitative | Model discipline, calibration/estimation, fit to targeted + untargeted moments, counterfactual validity | Dynare, `estimagic`, `QuantEcon` |
| Theory | Generality of the result, minimal assumptions, intuition | (analytical; LaTeX) |
| Experimental | Pre-registration, instructions at submission, balance, attrition, MHT correction | AEA RCT Registry, `ritest`, OSF |

## 4. Figures & tables (EER / Elsevier house rules)
- **Report standard errors** (and increasingly CIs); do not let significance stars replace SEs/magnitudes.
- Event-study plots with confidence bands; model-fit overlays; counterfactual curves with uncertainty.
- Supply **editable/vector source** for final figures; avoid chartjunk; colorblind-safe palettes.

## 5. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX. EER applies Elsevier's reference style; re-confirm the exact style on the guide for authors (检索于 2026-06).
- Typesetting: LaTeX (TeX Live / MacTeX / Overleaf) or Word — **editable source is required** to typeset the final article.
- Research highlights are an Elsevier requirement; prepare a few concise bullet findings.

## 6. Process & portal (verify on the official Elsevier / ScienceDirect pages)
| Item | Note |
|------|------|
| Submission portal | Editorial Manager — `https://www.editorialmanager.com/eerev` |
| Review model | Single-anonymized (single-blind); editor desk-screen → ≥2 referees (检索于 2026-06) |
| Submission fee | Non-refundable EUR 125 (EUR 100 PhD-student contact author); Research4Life Group A waiver via voucher requested before submission (检索于 2026-06) |
| Replication deposit | Mandatory replication policy: data, code, computational details before publication; deposit location per current Elsevier policy (检索于 2026-06) |
| Open access | Optional Gold OA with an APC; subscription route has no APC (re-confirm amount — 检索于 2026-06) |
| Appeals | One formal appeal per submission (Elsevier appeal policy); decision final |

## 7. Cautions
1. **Verify volatile specifics** (fee, abstract limit, reference style, OA APC, editors, replication-deposit location) on the official Elsevier / ScienceDirect pages — they change.
2. **The replication policy is mandatory for accepted empirical/simulation/experimental papers** — assemble raw data, code, and documentation early; do not assert a verification step or repository the current policy does not state.
3. **The submission fee is non-refundable** — do not submit a marginal-fit paper that risks a desk reject; request any Research4Life voucher *before* submitting.
4. **Match diagnostics to the paper type** — causal-design diagnostics for empirical work; model discipline and identification of parameters for quantitative work; generality and intuition for theory.
