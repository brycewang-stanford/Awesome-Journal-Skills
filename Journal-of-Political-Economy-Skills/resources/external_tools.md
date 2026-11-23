# External Tools & Resources for JPE Submissions

Data sources and software for economics research targeted at the Journal of Political
Economy (JPE), covering identification, structural estimation, theory/computation, and
replication. JPE values both credible identification and explicit economic mechanism, so
the toolkit spans reduced-form, structural, and computational methods. Always respect each
data provider's license, and confirm the current data/code policy on the journal's official
page.

## 1. Data sources

### U.S. micro / administrative
| Source | Provider | Typical use |
|--------|----------|-------------|
| IPUMS (CPS, ACS, USA, International) | University of Minnesota | Labor, demography, public |
| Census / LEHD / LBD (FSRDC) | U.S. Census Bureau | Firms, workers, restricted-access |
| PSID, NLSY | ISR Michigan / BLS | Life-cycle, labor, household |
| HRS | University of Michigan | Health, aging, retirement |
| IRS / SOI, Opportunity Insights | Treasury / Opportunity Insights | Income, mobility, tax |

### Macro / financial / international
| Source | Provider | Typical use |
|--------|----------|-------------|
| FRED | Federal Reserve Bank of St. Louis | Macro time series |
| BEA, BLS | U.S. government | National accounts, prices, employment |
| Penn World Table | UC Davis / Groningen | Cross-country growth |
| World Bank WDI, IMF IFS | World Bank / IMF | International comparison |
| CRSP, Compustat (WRDS) | WRDS | Asset prices, firm financials |

### Trade, IO, and firm-level
| Source | Provider | Typical use |
|--------|----------|-------------|
| Compustat / Orbis | WRDS / Bureau van Dijk | Firm structure, IO |
| UN Comtrade, CEPII | UN / CEPII | Trade flows, gravity |
| NBER-CES Manufacturing Industry Database | NBER | Industry productivity |

## 2. Reduced-form / causal inference

### Stata
- `reghdfe` — high-dimensional fixed effects
- `csdid`, `did_multiplegt`, `eventstudyinteract`, `did_imputation` — heterogeneity-robust DID / event study
- `bacondecomp` — Goodman-Bacon decomposition for staggered DID
- `ivreg2`, `weakivtest` — IV with weak-IV diagnostics (effective F)
- `rdrobust`, `rddensity` — RDD with bias-corrected CIs and manipulation tests
- `psmatch2`, `csdid` — matching and DID-matching
- `boottest` — wild cluster bootstrap (few clusters)
- `psacalc` — Oster (2019) selection-on-unobservables bound

### R
- `fixest` — fast high-dimensional FE, IV, and event studies
- `did` (Callaway–Sant'Anna), `didimputation`, `staggered` — modern DID
- `rdrobust`, `rddensity` — RDD
- `ivreg`, `AER`, `ivmodel` — instrumental variables
- `sensemakr`, `robomit` — sensitivity / omitted-variable bounds

### Python
- `linearmodels` — panel, IV (2SLS/GMM), system estimation
- `statsmodels`, `pandas`, `numpy` — modeling and data work
- `pyfixest` — fixest-style high-dimensional FE
- `econml`, `doubleml` — double/debiased ML and heterogeneous effects

## 3. Structural estimation & computation

- **Stata/Mata, MATLAB, Julia, Python** — workhorses for structural estimation
- `Optim.jl`, `JuMP` (Julia), `scipy.optimize`, `NLopt`, `Knitro` — optimization for SMM / MLE / GMM
- Dynare (MATLAB/Octave/Julia) — DSGE solution and estimation
- `QuantEcon` (Python/Julia) — dynamic programming, value-function iteration, computational economics
- BLP / demand estimation: `pyblp` (Python) for differentiated-products demand
- Method of simulated moments / indirect inference — pair an optimizer with bootstrapped/clustered inference

## 4. Theory & exposition

- LaTeX (TeX Live / MacTeX) with `amsmath`, `amsthm` for propositions and proofs
- TikZ / PGFPlots for analytical figures and model schematics
- Overleaf for collaborative drafting
- Mathematica / SymPy for symbolic comparative statics

## 5. Exhibits & visualization

- `estout` / `esttab` (Stata), `modelsummary` (R), `stargazer` — regression tables with economic magnitudes
- `coefplot` (Stata), `ggplot2` (R), `matplotlib`/`seaborn` (Python) — coefficient and event-study plots with confidence bands
- Keep figures grayscale-legible; avoid 3-D and chartjunk per UChicago Press style

## 6. Replication package (AEA Data Editor standard)

- README template: the AEA Data and Code Availability Policy README skeleton (overview, data availability statement, computational requirements, run instructions, code→exhibit map)
- A single **master script** (`.do`, `.R`, `.py`, or a `make`/snakemake pipeline) reproducing every exhibit from raw inputs
- Pin software/package versions; record random seeds; use relative paths only
- Environment capture: `renv` (R), `conda`/`pip freeze` or `uv` (Python), `version` logging (Stata)
- Deposit-ready archives: the journal/AEA-designated repository (verify current policy)

## 7. Reference management

| Tool | Note |
|------|------|
| BibTeX / BibLaTeX | Author-date styles (e.g., `chicago`/`authoryear`) match JPE house style |
| Zotero | Free; exports BibTeX; Chicago author-date style available |
| EndNote | Journal style files; common in economics departments |

## 8. Useful sites

| Site | Use |
|------|-----|
| Journal of Political Economy (official page) | Scope, author guidelines, fee, data/code policy — verify current details |
| Editorial Manager | JPE submission portal |
| NBER, SSRN, RePEc / IDEAS | Working papers and preprints |
| AEA Data Editor / Social Science Data Editors | Replication standards and README template |
| Google Scholar, Web of Science | Literature search |

## 9. Notes

1. **Data compliance** — honor licenses (WRDS, IPUMS, restricted Census/FSRDC); never redistribute restricted data.
2. **Reproducibility from day one** — fix seeds, pin versions, and keep a master script so the replication package is not a last-minute scramble.
3. **Economic interpretation** — every estimate and every structural parameter needs a stated economic meaning; tools serve the argument, not the reverse.
4. **Verify volatile facts** — submission fee, exact format limits, and the data/code policy change over time; confirm on the official page before submitting.
