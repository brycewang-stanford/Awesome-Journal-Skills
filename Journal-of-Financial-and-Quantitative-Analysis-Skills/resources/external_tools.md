# External Tools & Resources for JFQA-Style Empirical & Quantitative Finance

Data sources, software, and packages useful when preparing a *Journal of Financial and
Quantitative Analysis* (JFQA) submission — empirical and quantitative work in corporate
finance, investments, asset pricing, market microstructure, and financial institutions,
with a credible research design and a reproducible code/data archive for the JFQA
Dataverse. Check licenses and current access terms before use; most finance data are
proprietary and subscription-gated.

## 1. Finance data sources

### Equities, fundamentals, returns
| Source | Provider | Typical use |
|--------|----------|-------------|
| CRSP (stock, mutual fund, Treasury) | CRSP / WRDS | Returns, delisting, market cap, share data |
| Compustat (North America, Global) | S&P / WRDS | Firm fundamentals, accounting variables |
| CRSP/Compustat Merged (CCM) | WRDS | Linked returns + fundamentals |
| IBES | LSEG / WRDS | Analyst forecasts, recommendations |
| Thomson/Refinitiv 13F, mutual fund holdings | LSEG / WRDS | Institutional ownership, holdings |

### Microstructure, fixed income, derivatives
| Source | Provider | Typical use |
|--------|----------|-------------|
| TAQ (trades & quotes) | NYSE / WRDS | Liquidity, microstructure, intraday |
| TRACE | FINRA / WRDS | Corporate-bond transactions |
| OptionMetrics (IvyDB) | WRDS | Option prices, implied vol surfaces |
| Mergent FISD | WRDS | Bond issue characteristics |
| Markit / CDS data | Markit | Credit spreads |

### Corporate events, ownership, banking
| Source | Provider | Typical use |
|--------|----------|-------------|
| SDC Platinum | LSEG | M&A, IPOs, SEOs, syndicated loans |
| BoardEx / ISS | WRDS | Governance, board, executive networks |
| Execucomp | S&P / WRDS | Executive compensation |
| Call Reports / FR Y-9C | FFIEC / Fed | Bank balance sheets, regulation |
| Dealscan | LSEG / WRDS | Syndicated loan terms |

### Factors & benchmarks
| Source | Provider | Typical use |
|--------|----------|-------------|
| Kenneth French Data Library | Dartmouth | FF factors, portfolios, momentum |
| Global Factor Data / open replications | Various | Factor benchmarks, anomaly tests |

## 2. Statistical & quantitative software

### Stata (very common in empirical finance)
- Panel/FE at scale: `reghdfe`, `ftools`
- Clustered & robust SEs: built-in `vce(cluster)`, two-way clustering (`reghdfe`, `vcemway`)
- Asset pricing: `asreg` (rolling betas, Fama-MacBeth), `xtfmb` (Fama-MacBeth)
- Event studies: `eventstudy2`, `estudy`
- Causal designs: `csdid` (Callaway-Sant'Anna), `did_multiplegt_dyn`, `rdrobust`, `ivreg2`/`ivreghdfe`
- Inference: `boottest` (wild-cluster bootstrap), `winsor2` (winsorizing)

### R
- Data: `data.table`, `dplyr`, `RPostgres` (WRDS cloud)
- Estimation: `fixest` (fast FE, IV, clustering), `lmtest`/`sandwich`, `plm`
- Asset pricing & portfolios: `PerformanceAnalytics`, `frenchdata`, `tidyfinance`
- Event studies / designs: `eventstudies`, `did`, `rdrobust`
- Reproducibility: `renv` (pin versions), `targets` (pipeline)

### Python
- Data: `pandas`, `numpy`, `wrds` (official WRDS client), `pandas-datareader`
- Estimation: `statsmodels`, `linearmodels` (`FamaMacBeth`, `PanelOLS`, IV)
- Portfolios / factors: custom sorts, `empyrical`
- Reproducibility: `pip freeze` / `requirements.txt`, virtual envs, set seeds

## 3. Design toolkit for finance questions

| Design | Core checks | Notes for finance |
|--------|-------------|-------------------|
| Portfolio sorts / Fama-MacBeth | Newey-West / clustered SEs, factor controls | Standard asset-pricing inference |
| Panel FE (firm × time) | Two-way clustering, within-variation | Workhorse in corporate finance |
| Staggered DID (policy/regulation shocks) | Modern estimator, event-study leads, parallel trends | Avoid plain TWFE on staggered timing |
| IV / natural experiment | First-stage F, weak-IV-robust CIs, exclusion logic | Instrument relevance + economic story |
| RDD (thresholds, index inclusion) | Density/manipulation test, bandwidth robustness | Index reconstitution, covenant cutoffs |
| Event study (announcements) | CAR/BHAR, market model, calendar clustering | Returns around corporate events |

## 4. Figures & tables (finance conventions)
- Report economic magnitudes, not just significance (e.g., effect per one-SD change)
- Winsorize/trim and disclose it; report number of firms/observations and clustering
- Standard exhibits: summary stats, correlation matrix, main regressions, robustness, heterogeneity
- Vector output (PDF/EPS); legible at print resolution

## 5. Reproducibility & the JFQA code/data archive
- The **JFQA Code Sharing Policy** (mandatory for accepted submissions made on/after **Jan 1, 2024**) requires posting source code, the raw datasets (or a **pseudo dataset** if data are confidential/proprietary), and a **read-me** with software/versions and a program-execution roadmap — archived in the **JFQA Dataverse** at the **Harvard University Dataverse**.
- Build one master script (`run_all`) that regenerates every reported table and figure from the raw (or pseudo) data; pin software/package versions; set and report seeds.
- Request any **exception** (e.g., delayed release for confidential data) **on the initial submission** — not later; granted exceptions are disclosed in the published paper.
- JFQA may run **random external code verification**; build the package as you go.

## 6. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote. No specific named style is mandated at initial submission (待核实); accepted papers follow the JFQA Style Guide.
- Typesetting: LaTeX (TeX Live / MacTeX, Overleaf) or Word, exported to a single text-searchable PDF.

## 7. Process & portal
| Item | Note |
|------|------|
| Submission portal | Editorial Manager (`editorialmanager.com/jfqa/`); separate account required |
| Submission fee | **$350**, credit card only; **$275 refunded** if not sent to a reviewer (desk reject keeps **$75**) |
| Review model | Double-anonymous; anonymize the manuscript and PDF |
| Abstract | One paragraph, **≤ 100 words** |
| Formatting | 8.5×11, 1-inch margins, 12-pt Times New Roman, double-spaced, text-searchable PDF |
| Code/data deposit | Required at acceptance for post-2024 submissions; JFQA Dataverse (Harvard) |
| Publisher | Cambridge University Press (for UW Foster School of Business) |

## 8. Cautions
1. **Verify volatile specifics** (fee, refund, editors, formatting, deposit rules, portal URL) on the official JFQA and Cambridge pages — they change.
2. **Respect data licenses**; CRSP/Compustat/TAQ and similar are proprietary — use the pseudo-dataset fallback for the archive when redistribution is barred.
3. **Match estimator to design** — plain TWFE on staggered timing and naive event-study clustering are known pitfalls.
4. **Disclose any prior rejection** of a resubmitted paper in the cover letter — failure triggers a one-year submission ban.
