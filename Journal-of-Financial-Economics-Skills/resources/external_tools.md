# External Tools & Resources for JFE Empirical Work

Data sources, software, and packages commonly used in Journal of Financial Economics
submissions (empirical corporate finance and asset pricing). Always check each
provider's current access terms and the journal's current data-availability policy.

## 1. Data sources

### Core US market & accounting data (usually via WRDS)
| Source | Provider | Typical use |
|--------|----------|-------------|
| CRSP | Center for Research in Security Prices | Stock prices, returns, delistings, market cap |
| Compustat | S&P Global | Firm fundamentals, accounting data (North America & Global) |
| CRSP/Compustat Merged (CCM) | WRDS | Linking returns to fundamentals |
| TAQ | NYSE | Intraday trades and quotes, microstructure / liquidity |
| IBES | Refinitiv | Analyst forecasts and recommendations |
| Thomson/Refinitiv 13F | — | Institutional holdings |
| Dealscan | LSEG | Syndicated loans, covenants |
| SDC Platinum | LSEG | M&A, IPOs, securities issuance |
| Mergent FISD | — | Corporate bond issues and characteristics |
| TRACE | FINRA | Corporate bond transactions |
| Audit Analytics | — | Auditing, restatements, internal controls |
| BoardEx / ISS | — | Governance, board, executive data |
| OptionMetrics | — | Equity options (IvyDB) |

### Asset-pricing data libraries
| Source | Provider | Typical use |
|--------|----------|-------------|
| Kenneth French Data Library | Dartmouth | FF factors, portfolios, breakpoints |
| AQR / global factor data | various academic | Factor replications, global samples |
| FRED | Federal Reserve Bank of St. Louis | Macro and rate series |

### International & other
| Source | Provider | Typical use |
|--------|----------|-------------|
| Compustat Global / Datastream | S&P / LSEG | International firms and markets |
| Worldscope | LSEG | International fundamentals |
| World Bank WDI, OECD | — | Country-level controls |

> Many of these are accessed through **WRDS** (Wharton Research Data Services), which
> also hosts cleaned linking tables and SAS/Python/R query interfaces.

## 2. Software

### Stata
- Recommended for panel corporate-finance work.
- Useful packages:
  - `reghdfe` — high-dimensional fixed effects with multi-way clustering
  - `ivreghdfe` / `ivreg2` — IV/2SLS with HDFE; first-stage diagnostics
  - `csdid` (Callaway–Sant'Anna), `did_multiplegt` (de Chaisemartin–D'Haultfœuille), `eventstudyinteract` (Sun–Abraham) — staggered DID
  - `bacondecomp` — Goodman-Bacon decomposition
  - `rdrobust`, `rddensity` — RDD estimation and manipulation tests
  - `boottest` — wild-cluster bootstrap (few clusters)
  - `psmatch2`, `ebalance` — matching / entropy balancing
  - `asreg` / `xtfmb` — Fama–MacBeth and rolling regressions

### Python
- Useful libraries:
  - `pandas`, `numpy` — data handling
  - `statsmodels`, `linearmodels` (PanelOLS, FamaMacBeth, IV2SLS) — estimation
  - `wrds` — programmatic WRDS access
  - `scipy`, `numba` — numerics / speed
  - `matplotlib`, `seaborn` — figures

### R
- Useful packages:
  - `fixest` (`feols`) — high-dimensional FE, multi-way clustering, fast IV
  - `did` (Callaway–Sant'Anna), `didimputation`, `fwildclusterboot` — staggered DID and wild bootstrap
  - `rdrobust`, `rddensity` — RDD
  - `sandwich`, `lmtest` — robust/clustered SEs
  - `data.table`, `dplyr` — data wrangling

### MATLAB
- Common for structural estimation, GMM/SDF asset-pricing models, and simulation.

## 3. Method references to cite (verify exact citations)

- Staggered DID: Goodman-Bacon; Callaway–Sant'Anna; Sun–Abraham; de Chaisemartin–D'Haultfœuille.
- RDD: Calonico–Cattaneo–Titiunik (robust bias-corrected inference); McCrary / `rddensity` (manipulation).
- Weak IV: Olea–Pflueger effective F; Anderson–Rubin robust inference.
- Clustered/robust SEs: Petersen (panel SEs in finance); Cameron–Gelbach–Miller (multi-way).
- Multiple testing in asset pricing: Harvey–Liu–Zhu (and the broader factor-zoo literature).
- Omitted-variable sensitivity: Oster coefficient-stability bounds.

## 4. Writing & reproducibility

| Tool | Use |
|------|-----|
| LaTeX (TeX Live / MacTeX / Overleaf) | Typesetting; `booktabs` for clean tables |
| `estout` / `outreg2` (Stata), `modelsummary` (R), `pylatex`/`stargazer` | Regression tables to LaTeX |
| Git + GitHub/GitLab | Code version control |
| Zotero / EndNote / Mendeley | Reference management |
| iThenticate / Turnitin | Similarity check before submission |

## 5. Notes

1. **Data licensing:** WRDS and vendor data are licensed; document access paths but do
   not redistribute restricted data. State restrictions in the data-availability section.
2. **Reproducibility:** keep code and intermediate data organized so the headline tables
   can be reproduced; the journal's data/code deposit policy may require this (verify).
3. **Standard errors:** the cluster level is a modeling choice — justify it; for causal
   designs match it to the level of treatment assignment.
4. **Verify everything volatile:** submission portal, fee, anonymity policy, reference
   style, and data-availability rules all change — check the official author page.
