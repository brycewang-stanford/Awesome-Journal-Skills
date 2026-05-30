# External Tools & Data Sources (Empirical Finance for JF)

This document collects data sources, software, and packages commonly used in empirical
finance manuscripts targeted at *The Journal of Finance*. Always respect each provider's
license and your institution's data-use agreement; verify current access on the official sites.

## 1. Data sources

### Core empirical-finance databases (typically via WRDS)
| Source | Provider | Typical use |
|--------|----------|-------------|
| CRSP | Center for Research in Security Prices | Stock returns, prices, delisting, market cap |
| Compustat | S&P Global Market Intelligence | Firm fundamentals, accounting data |
| CRSP/Compustat Merged (CCM) | WRDS | Linked returns + fundamentals |
| TAQ (Trade and Quote) | NYSE / WRDS | Intraday trades & quotes, microstructure, liquidity |
| IBES | Refinitiv | Analyst forecasts, recommendations |
| Thomson/Refinitiv 13F | Refinitiv | Institutional holdings |
| Mergent FISD | Mergent | Corporate bond issue characteristics |
| TRACE | FINRA / WRDS | Corporate bond transactions |
| OptionMetrics (Ivy DB) | WRDS | Option prices, implied volatility |
| Dealscan | Refinitiv LPC | Syndicated loans |
| BoardEx / ISS / RiskMetrics | various / WRDS | Governance, boards, ownership |
| Capital IQ / Refinitiv Eikon | S&P / LSEG | Deals, ownership, global fundamentals |

### Factor & portfolio data
| Source | Use |
|--------|-----|
| Kenneth French Data Library | Fama–French factors, momentum, breakpoints, test portfolios |
| AQR Data Library | Factor returns, quality-minus-junk, betting-against-beta |
| q-factor data (Hou–Xue–Zhang) | q-factor model returns |
| FRED (St. Louis Fed) | Macro series, rates, indices |
| Global Financial Data / Datastream | Long-history and international series |

### International / banking / household
| Source | Use |
|--------|-----|
| Bankscope / Orbis Bank Focus | Bank financials |
| Worldscope / Datastream | International firm data |
| SCF (Survey of Consumer Finances) | Household balance sheets |
| Call Reports (FFIEC) | U.S. bank regulatory filings |

## 2. Statistical software & packages

### Stata
- Panel / FE: `reghdfe`, `xtreg`
- Difference-in-differences (staggered): `csdid` (Callaway–Sant'Anna), `did_multiplegt` (de Chaisemartin–D'Haultfœuille), `eventstudyinteract` (Sun–Abraham), `bacondecomp` (Goodman-Bacon)
- IV / GMM: `ivreg2`, `ivreghdfe`, `weakivtest`
- RDD: `rdrobust`, `rddensity`
- Asset pricing: `asreg` (rolling / Fama–MacBeth), `xtfmb` (Fama–MacBeth), `newey` (Newey–West)
- Sensitivity: `psacalc` (Oster's δ)
- Winsorize/format: `winsor2`, `estout`/`esttab`, `outreg2`

### Python
- `pandas`, `numpy` — data wrangling
- `statsmodels`, `linearmodels` — panel, IV, Fama–MacBeth (`linearmodels.FamaMacBeth`), clustered SEs
- `wrds` — programmatic WRDS access
- `scipy`, `scikit-learn` — statistics, ML for prediction tasks
- `matplotlib`, `seaborn` — figures

### R
- `data.table`, `dplyr` — data wrangling
- `fixest` — high-dimensional FE, fast clustered SEs, event studies
- `did` (Callaway–Sant'Anna), `didimputation`, `bacondecomp` — staggered DID
- `rdrobust`, `rddensity` — RDD
- `sandwich` + `lmtest` — robust / clustered / Newey–West SEs
- `frenchdata` — pull Kenneth French factors

## 3. Identification & robustness helpers

- Multiple-testing thresholds for cross-sectional asset pricing: apply the logic of Harvey, Liu & Zhu ("…and the Cross-Section of Expected Returns"); FDR/Bonferroni adjustments via standard packages
- Standard-error corrections: Shanken (two-pass EIV), Newey–West (overlapping/autocorrelated), two-way clustering (firm × time)
- Selection-on-unobservables bounds: Oster's δ (`psacalc` / manual)
- GRS test for portfolio alphas

## 4. Writing, references, and reproducibility

| Tool | Use |
|------|-----|
| LaTeX (TeX Live / MacTeX / Overleaf) | Typesetting; JF accepts LaTeX submissions |
| BibTeX / Zotero / EndNote | Reference management in the journal's style |
| Git + GitHub/GitLab | Versioning code and the replication package |
| esttab / estout / texreg / stargazer | Regression tables to LaTeX |

## 5. Submission & verification

- JF submissions: Manuscript Central / ScholarOne (verify the current portal URL).
- Submission fee / AFA membership norms: confirm the current amount and any membership requirement on the official AFA / JF author page before submitting.
- Replication package: prepare code + data-construction scripts; JF expects a data-availability statement and a sharable package on acceptance.

## 6. Notes & good practice

1. **Licensing**: WRDS and vendor data have strict redistribution rules — never post raw licensed data in a public replication package; share code and construction steps instead.
2. **Reproducibility**: keep a clean pipeline from raw extracts to tables; seed any randomization.
3. **Versioning**: record database snapshot dates (CRSP/Compustat are revised).
4. **Microstructure care**: TAQ cleaning conventions matter — document trade/quote filters.
5. **Backup**: retain code and intermediate data for the full review cycle and post-acceptance replication.
