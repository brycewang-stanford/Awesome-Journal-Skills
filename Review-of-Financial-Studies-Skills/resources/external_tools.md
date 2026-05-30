# Finance Research: External Tools & Data Sources

Reference list of data sources and software for empirical and theoretical finance manuscripts
targeted at *The Review of Financial Studies (RFS)*. Access terms, coverage, and licensing
change — verify current availability through your institution and the provider.

## 1. Data sources

### Core US market & accounting data (typically via WRDS)
| Source | Provider | Typical use |
|--------|----------|-------------|
| CRSP | Center for Research in Security Prices | Stock prices, returns, delisting, market cap |
| Compustat | S&P Global | Firm fundamentals, financial statements |
| CRSP/Compustat Merged (CCM) | WRDS | Linked returns + fundamentals (point-in-time linking) |
| TAQ | NYSE | Intraday trades & quotes, microstructure |
| IBES | LSEG/Refinitiv | Analyst forecasts and recommendations |
| Thomson/Refinitiv 13F | LSEG/Refinitiv | Institutional holdings |
| Mergent FISD | Mergent | Corporate bond issues and characteristics |
| TRACE | FINRA | Corporate bond transactions |
| OptionMetrics (IvyDB) | OptionMetrics | Options prices and implied volatilities |
| Dealscan | LSEG | Syndicated loans |

### Macro / factor / international
| Source | Provider | Typical use |
|--------|----------|-------------|
| Ken French Data Library | Dartmouth | Factor returns (FF3/FF5, momentum), portfolios |
| AQR / Global Factor data | AQR, public repos | Factor benchmarks, replication |
| FRED | Federal Reserve Bank of St. Louis | Macro & rates series |
| Datastream / Worldscope | LSEG | International equities and fundamentals |
| Compustat Global | S&P Global | Non-US firm fundamentals |
| BIS / IMF / World Bank | Official | Cross-country banking, capital flows |

### Frontier / specialized (fintech, climate, household)
| Source | Typical use |
|--------|-------------|
| Survey of Consumer Finances (SCF) | Household balance sheets |
| HMDA mortgage data | Mortgage lending, household finance |
| Crypto exchange / on-chain data (e.g., CoinGecko, blockchain explorers) | Digital assets, microstructure |
| Carbon emissions / ESG vendors (e.g., Trucost, MSCI, Sustainalytics) | Climate & sustainable finance |
| Regulatory filings (EDGAR / SEC) | Text analysis, disclosure, events |

> Always document point-in-time linking, delisting returns, survivorship, and look-ahead bias
> handling in the Internet Appendix.

## 2. Statistical software

### Stata
- Panel / FE: `reghdfe`, `xtreg`
- Modern DID: `csdid` (Callaway–Sant'Anna), `did_multiplegt`, `eventstudyinteract` (Sun–Abraham), `bacondecomp`
- IV: `ivreg2`, `ivreghdfe`, weak-IV: `weakivtest`
- RDD: `rdrobust`, `rddensity`
- Asset pricing: `asreg` (rolling/Fama–MacBeth), `xtfmb`, Newey–West / Driscoll–Kraay options
- Matching: `psmatch2`, `teffects`

### Python
- `pandas`, `numpy` — data wrangling
- `statsmodels`, `linearmodels` (PanelOLS, FamaMacBeth, IV2SLS)
- `wrds` — WRDS data API
- `scikit-learn` — ML / double-ML pipelines
- `matplotlib`, `seaborn` — figures

### R
- `data.table`, `dplyr` — data wrangling
- `fixest` (high-dimensional FE, IV, event study), `did`, `plm`
- `rdrobust`, `rddensity`
- `sandwich`, `lmtest` — robust / clustered SEs
- `frenchdata` — Ken French factor data

### MATLAB / Julia
- Structural estimation, DSGE, dynamic models, GMM/SMM

## 3. Identification & robustness helpers
- Multiple-testing: FDR/Holm/Bonferroni utilities; t-hurdle discussion per the asset-pricing replication literature (e.g., Harvey–Liu–Zhu)
- Synthetic control: `synth`, `synthdid`
- Bootstrap / randomization-inference routines for placebo tests

## 4. Writing, typesetting, reproducibility
- LaTeX (TeX Live / MacTeX; Overleaf for collaboration); `booktabs` for tables; `estout`/`esttab`, `outreg2`, `stargazer` for regression tables
- Reference management: Zotero, EndNote, BibTeX
- Reproducibility: Git + GitHub/GitLab; project structure with raw/derived data separation; a master script that reproduces every exhibit
- Internet Appendix and replication package prepared per current RFS data/code policy (verify on site)

## 5. Useful links (verify current URLs)
| Site | Purpose |
|------|---------|
| RFS at Oxford Academic | Journal home, author guidelines, scope |
| Society for Financial Studies (SFS) | Society norms, membership |
| WRDS | Data access portal |
| SSRN | Working-paper distribution |
| NBER | Working papers |
| Ken French Data Library | Factor data |

## 6. Notes
1. **Licensing**: respect provider terms; do not redistribute raw vendor data.
2. **Point-in-time discipline**: avoid look-ahead bias in fundamentals and factor construction.
3. **Reproducibility**: keep code and data versions that regenerate every table/figure.
4. **Data policy**: RFS data/code requirements evolve — confirm the current policy before submission.
