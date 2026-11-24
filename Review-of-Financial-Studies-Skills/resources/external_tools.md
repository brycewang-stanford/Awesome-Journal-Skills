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
- Internet Appendix and replication package prepared for RFS's **public code-release condition**: RFS's **Code and Data Sharing Policy** (applies to papers conditionally accepted on/after **1 October 2025**) requires a full replication **package — data (or documented non-public data plus pseudo data), code, README with a Data Availability Statement, and a license** — which the **RFS Data Editors** verify by reproducing the key tables and figures before final acceptance; the package is published in the RFS Dataverse. Any withholding/exemption request must be made **at submission** (uploaded in Editorial Express, Step 4); requests for licensed, non-public data are not needed

## 5. Useful links
| Site | URL | Purpose |
|------|-----|---------|
| RFS Instructions to Authors | https://academic.oup.com/rfs/pages/Instructions_To_Authors | Author guidelines, code-release policy |
| RFS Registered Reports | https://academic.oup.com/rfs/pages/registered_reports | Stage 1 / Stage 2 pre-results review |
| RFS–SFS Cavalcade dual submission | https://academic.oup.com/rfs/pages/dual-submission-with-the-sfs-cavalcade-2024 | Conference-to-journal route |
| SFS — RFS editorial team | https://sfs.org/review-of-financial-studies/editorial-team/ | Executive Editor + editors |
| Society for Financial Studies (SFS) | https://sfs.org/ | Society norms, membership |
| WRDS | https://wrds-www.wharton.upenn.edu/ | Data access portal |
| Ken French Data Library | https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html | Factor data |

> The handling structure (2026) is Executive Editor **Tarun Ramadorai** (LSE, 2024–2027)
> with editors including Viral Acharya, Xavier Giroud, Andrey Malenko, Anna Pavlova,
> Clemens Sialm, David Sraer, and Jessica Wachter. Verify the current board before relying on it.

## 6. Notes
1. **Licensing**: respect provider terms; do not redistribute raw vendor data.
2. **Point-in-time discipline**: avoid look-ahead bias in fundamentals and factor construction.
3. **Reproducibility**: keep code and data versions that regenerate every table/figure.
4. **Data policy**: RFS data/code requirements evolve — confirm the current policy before submission.
