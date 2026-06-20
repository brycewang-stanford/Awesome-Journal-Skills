# External Tools & Resources for JBF-Style Empirical Banking & Finance

Data sources, software, and packages useful when preparing a *Journal of Banking &
Finance* (JBF) submission — typically an empirical study of banks, financial
intermediaries, capital markets, investments, corporate finance, or financial
regulation, with a credible research design, robustness, and a data statement.
Check licenses and current access terms before use. Current JBF specifics were
refreshed from ScienceDirect / Elsevier on 2026-06-20 — see
`official-source-map.md`.

## 1. Data sources

### Bank & intermediary data
| Source | Provider | Typical use |
|--------|----------|-------------|
| FFIEC Call Reports / FR Y-9C | US Fed / FFIEC | US bank balance sheets, income, capital, risk |
| Bankscope / Orbis Bank Focus / BankFocus | Bureau van Dijk (Moody's) | Cross-country bank financials |
| FDIC SDI / BankFind | FDIC | US bank/thrift condition, failures, branches |
| SNL Financial / S&P Capital IQ Pro | S&P Global | Banks, insurers, deal-level data |
| ECB SDW, EBA stress tests, BIS statistics | ECB / EBA / BIS | Euro-area & global banking, regulation |
| Dealscan (LPC) | Refinitiv | Syndicated loans, lending terms |

### Markets, firms, securities
| Source | Provider | Typical use |
|--------|----------|-------------|
| CRSP | WRDS / CRSP | US stock prices, returns, market microstructure |
| Compustat (North America / Global) | S&P / WRDS | Firm fundamentals, corporate finance |
| TRACE | FINRA / WRDS | Corporate-bond transactions, liquidity |
| OptionMetrics / IvyDB | WRDS | Options, implied vol, investments |
| Mergent FISD | WRDS | Bond issuance, covenants, ratings |
| Datastream / Refinitiv Eikon | LSEG | International prices, FX, fixed income |

### Macro, regulation, supplementary
| Source | Provider | Typical use |
|--------|----------|-------------|
| FRED | St. Louis Fed | Rates, macro controls, policy series |
| Global Financial Development DB | World Bank | Cross-country financial structure |
| SEC EDGAR | SEC | Filings, text analysis, governance |

## 2. Statistical software

### Stata (common in empirical banking/finance)
- Panel & fixed effects at scale: `reghdfe`, `xtreg`
- Standard errors: cluster-robust, two-way clustering (`vce(cluster ...)`, `reghdfe`), `boottest` (wild-cluster bootstrap) for few clusters
- IV / GMM: `ivreg2`, `ivreghdfe`, `xtabond2` (dynamic panel / system GMM for bank panels), weak-IV-robust inference (`weakiv`)
- DID / event study: `csdid` (Callaway–Sant'Anna), `eventstudyinteract` (Sun–Abraham), `did_multiplegt_dyn`, `bacondecomp`
- Event studies (market model abnormal returns): `eventstudy2`, `estudy`
- RDD: `rdrobust`, `rddensity`
- Winsorizing / financial-ratio prep: `winsor2`

### R
- Panel / FE / IV: `fixest` (`feols`, fast FE, IV, clustering), `plm`, `lfe`
- DID / event study: `did`, `fixest::sunab`, `didimputation`
- Event studies: `estudy2`, `eventstudies`
- Inference: `sandwich`/`clubSandwich`, `fwildclusterboot`
- Reproducibility: `renv` (pin versions), `targets` (pipeline)

### Python
- `pandas`, `numpy`, `wrds` (WRDS API), `pandas-datareader` (FRED)
- `linearmodels` (panel IV / FE, two-way clustering), `statsmodels`
- `matplotlib` / `seaborn` for figures; `pip freeze` / `requirements.txt` to pin

## 3. Design toolkit by identification strategy

| Design | Core checks | Packages |
|--------|-------------|----------|
| Bank-panel TWFE / FE | Two-way clustering, within-bank variation, treatment timing | `reghdfe`, `fixest` |
| Staggered DID (reg/policy shocks) | Goodman-Bacon decomposition, modern estimator, event-study leads | `csdid`, `did`, `did_multiplegt_dyn` |
| IV / system GMM (dynamic panels) | First-stage F, weak-IV CIs, instrument-count / Hansen J | `ivreg2`, `xtabond2`, `linearmodels` |
| RDD (regulatory thresholds) | Density (McCrary), bandwidth robustness | `rdrobust`, `rddensity` |
| Event study (announcements) | Estimation/event windows, CAR/BHAR, cross-sectional regs | `eventstudy2`, `estudy2` |

## 4. Figures & tables
- Event-study / CAR plots with confidence bands; coefficient plots; binned scatters
- Report winsorization, variable definitions, and sample-selection waterfalls
- Vector output (PDF/EPS) for print resolution; self-contained table/figure notes

## 5. Reproducibility & data sharing (JBF / Elsevier Option C)
- JBF follows Elsevier **Option C** research-data instructions: deposit research data in a relevant repository and cite/link it in the article, or state why the data cannot be shared. A data statement is required at submission and appears with the published article.
- Pin software/package versions; provide one master script (`run_all`) regenerating every table and figure; set and report random seeds for any bootstrap/simulation.
- Document data licenses; much core data (CRSP, Compustat, Dealscan, Bankscope) is **proprietary** and cannot be redistributed — share code plus a data-access README instead.

## 6. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote — first submission may use any complete, consistent reference style; prepare for JBF's numbered Elsevier style at proof stage
- Provide 1-7 English keywords; keep JEL classification codes as optional finance metadata; Highlights are encouraged
- Free integrated **SSRN** preprint posting is offered at submission (posted once past initial desk review)

## 7. Process & portal
| Item | Note |
|------|------|
| Submission portal | Elsevier **Editorial Manager** (via the journal homepage) |
| Submission fee | **USD 350**, non-refundable, paid in Editorial Manager; waiver/discount codes for eligible authors |
| Review model | **Double anonymized** — anonymized manuscript + separate title page |
| Data sharing | Elsevier Option C: data statement plus deposit/cite/link, or explain why data cannot be shared |
| AI declaration | Generative-AI use must be declared at submission |
| Publisher | Elsevier |

## 8. Cautions
1. **Verify volatile specifics** (fee, editor roster, special-issue instructions) on the official ScienceDirect pages before submission.
2. **Respect data licenses** — CRSP/Compustat/Dealscan/Bankscope are proprietary; share code and access instructions, not the raw data.
3. **Match estimator to design** — plain TWFE on staggered policy timing, or system GMM with an unchecked instrument count, are known pitfalls in bank panels.
4. **Anonymize fully** under double-anonymized review — scrub author identity from the manuscript and PDF metadata; keep the title page separate.
