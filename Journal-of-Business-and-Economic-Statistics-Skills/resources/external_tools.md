# External Tools & Resources for JBES-Style Methods Work

Software, libraries, and references useful when preparing a *Journal of Business & Economic
Statistics* (JBES) submission — a **new or improved statistical/econometric method** with
clear empirical relevance, supported by **asymptotic theory, Monte Carlo evidence, and a
substantive empirical application**, plus a **reproducible data-and-code supplement** under
ASA policy. Check licenses and current access terms before use.

## 1. Method development & simulation

### Symbolic / analytic
- Asymptotics, expansions, influence functions: `SymPy` (Python), `Mathematica`, `Maxima`
- Matrix algebra and derivations: NumPy/SciPy, `Matrix` (R), pen-and-paper checked numerically

### Monte Carlo engines (size, power, coverage, bias/RMSE)
- R: `future`/`furrr`, `parallel`, `foreach`+`doParallel`; `microbenchmark` for timing
- Python: `joblib`, `multiprocessing`, `numba`/`Cython` for inner loops; `numpy.random.Generator`
- Stata: `simulate`, `postfile`, `parallel`; `set seed` and store the version of every command
- Always: fix and report seeds; report Monte Carlo standard errors of simulated rejection rates

## 2. Econometric / statistical libraries by method family

| Method family | R | Python | Stata |
|---|---|---|---|
| GMM / M-estimation | `gmm`, `momentfit` | `linearmodels`, `statsmodels` | `gmm`, `ml` |
| Time series / volatility | `forecast`, `rugarch`, `vars`, `urca` | `statsmodels.tsa`, `arch` | `arima`, `arch`, `var` |
| Panel / fixed effects | `fixest`, `plm` | `linearmodels` | `reghdfe`, `xtreg` |
| Quantile / distributional | `quantreg` | `statsmodels` QuantReg | `qreg`, `sqreg` |
| Bootstrap / subsampling | `boot` | `scipy.stats.bootstrap`, `arch.bootstrap` | `bootstrap`, `boottest` |
| Nonparametric / kernel | `np`, `KernSmooth` | `statsmodels` KDE, `scikit-learn` | `npregress`, `lpoly` |
| HAC / robust inference | `sandwich`, `clubSandwich` | `statsmodels` cov_type | `newey`, `vce(robust/cluster)` |
| ML for econometrics | `grf`, `glmnet`, `hdm`, `DoubleML` | `econml`, `doubleml`, `scikit-learn` | `lassopack`, `pdslasso` |
| Bayesian computation | `rstan`, `brms`, `cmdstanr` | `PyMC`, `numpyro` | `bayes:` prefix |

## 3. Empirical-application data (the "clear empirical relevance" requirement)

JBES expects a *substantive* application, not a toy illustration. Common sources:

| Source | Provider | Typical use |
|---|---|---|
| FRED / FRED-MD / FRED-QD | St. Louis Fed | Macro time series, factor models, forecasting |
| CRSP / Compustat (WRDS) | Wharton (licensed) | Asset pricing, volatility, high-frequency finance |
| TAQ / high-frequency trade data | NYSE / WRDS | Realized volatility, microstructure methods |
| IPUMS (CPS, ACS) | U. Minnesota | Cross-section/panel micro applications |
| World Bank WDI / OECD | World Bank / OECD | Cross-country panels |
| Penn World Table | UC Davis / Groningen | Growth, productivity panels |

## 4. Reproducibility & the data/code supplement (ASA policy)

Under ASA journal policy, authors are **strongly encouraged** to provide **data sets and code
as supplementary material** that demonstrate the article's results, to make underlying data
publicly available, and to include a **data availability statement**; editors may set stricter
rules and a waiver path exists for confidential data. Practical tooling:

- Pin environments: `renv.lock` (R), `requirements.txt`/`environment.yml`/`uv.lock` (Python),
  recorded `ssc`/`net` versions + Stata version (Stata)
- One master script (`run_all`) that regenerates **every table, figure, and Monte Carlo number**
- Record seeds, wall-clock runtime, hardware, and total simulation replications
- Containerize heavy simulations where helpful (`Docker`); archive on a stable repository
  (Zenodo, OSF, or the journal's supplementary-material system). **Note: JBES does NOT use the
  JAE Data Archive (that belongs to the Journal of Applied Econometrics, a separate Wiley
  journal); check live T&F instructions before asserting stricter JBES-specific enforcement.**

## 5. Tables, figures & typesetting (methods papers)
- Simulation tables: `kableExtra`/`modelsummary` (R), `stargazer`, `esttab`/`estout` (Stata),
  `pandas.Styler.to_latex` (Python); report size/power side-by-side across DGPs and sample sizes
- Figures: size-power curves, coverage plots, empirical-vs-nominal QQ plots, sampling
  distributions; vector output (PDF/EPS); avoid chartjunk
- Typesetting: LaTeX (TeX Live / MacTeX / Overleaf); confirm current T&F/JBES style on the
  live author-instruction page before filing

## 6. References & process
- Reference managers: Zotero, BibTeX/BibLaTeX — set to the journal's required style after the live
  T&F check
- Process specifics (submission platform, fee, length limit, review model) are live-page preflight
  items; confirm on the JBES instructions-for-authors page before relying on them

## 7. Cautions
1. **Verify volatile specifics** (fee, length, review model, deposit rules, portal) on the official
   JBES page before filing.
2. **Match the asymptotics to the DGP** — report Monte Carlo standard errors, not just point
   rejection rates; show where the method breaks (small n, heavy tails, dependence).
3. **An empirical application is part of scope** — a pure derivation with no application is
   off-fit for JBES.
4. **Build the reproducible supplement as you go**, not at the end; ASA expects code+data to
   demonstrate the published results.
