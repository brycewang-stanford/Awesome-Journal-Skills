# External Tools & Resources for Review of Finance (Empirical + Theory)

Data sources, software, and packages useful when preparing a *Review of Finance* (RoF)
submission. RoF publishes **general-interest finance at the level of the top-three
finance journals**, spanning **empirical** work (asset pricing, corporate finance,
banking, household finance, market microstructure) and **theoretical** work (asset-pricing
theory, contract/security design, market-microstructure theory). Check licenses and
current access terms before use. Verify volatile RoF specifics on the official pages
(see `official-source-map.md`).

## 1. Data sources (empirical finance)

### Asset pricing & markets
| Source | Provider | Typical use |
|--------|----------|-------------|
| CRSP | Wharton / WRDS | Stock returns, prices, delisting |
| Compustat | S&P / WRDS | Firm fundamentals, accounting |
| TRACE | FINRA / WRDS | Corporate bond transactions |
| OptionMetrics (IvyDB) | WRDS | Option prices, implied vol |
| TAQ | NYSE / WRDS | Intraday trades & quotes, microstructure |
| Ken French Data Library | Dartmouth | Factor returns, portfolios, breakpoints |

### Corporate, banking, household
| Source | Provider | Typical use |
|--------|----------|-------------|
| Thomson/Refinitiv (SDC, I/B/E/S, 13F) | LSEG / WRDS | Deals, analyst forecasts, holdings |
| Call Reports / FR Y-9C | Federal Reserve / FFIEC | Bank balance sheets, regulation |
| Capital IQ / Orbis-Amadeus | S&P / Bureau van Dijk | Private firms, international |
| Dealscan | LSEG | Syndicated loans |
| SEC EDGAR | SEC | Filings, text analysis |
| Survey of Consumer Finances (SCF) | Federal Reserve | Household portfolios, wealth |

## 2. Statistical software

### Stata (common in empirical finance)
- Panel / FE at scale: `reghdfe`, `ivreghdfe`
- Asset pricing: `asreg` (rolling betas, Fama–MacBeth), `xtfmb` (Fama–MacBeth), portfolio sorts
- IV / weak-IV: `ivreg2`, `weakiv`, `condivreg`
- DID / event study: `csdid` (Callaway–Sant'Anna), `eventstudyinteract` (Sun–Abraham), `did_multiplegt_dyn`, `bacondecomp`
- RDD: `rdrobust`, `rddensity`, `rdbwselect`
- Inference: `boottest` (wild-cluster bootstrap), two-way clustering (`vce(cluster)` / `reghdfe`)

### R
- Asset pricing & factors: `frenchdata`, `tidyfinance`, `PerformanceAnalytics`, `sandwich`/`lmtest` (Newey–West)
- Panel / FE: `fixest` (`feols`, two-way clustering, IV), `plm`
- DID / event study: `did`, `fixest::sunab`, `didimputation`
- RDD: `rdrobust`, `rddensity`
- Reproducibility: `renv` (pin versions), `targets` (pipeline)

### Python
- `pandas`, `numpy` — data wrangling; `wrds` — WRDS access
- `statsmodels`, `linearmodels` (`FamaMacBeth`, panel IV/FE) — estimation
- `arch` — volatility / GARCH; `cvxpy` — portfolio optimization
- `matplotlib` / `seaborn` — figures; `pip freeze` / `requirements.txt` to pin

## 3. Empirical-finance method toolkit
| Design | Core checks | Packages |
|--------|-------------|----------|
| Portfolio sorts / factor models | Newey–West / robust SE, alpha tests, GRS | `frenchdata`, `linearmodels`, custom |
| Fama–MacBeth cross-section | Shanken correction, two-pass errors-in-variables | `asreg`, `xtfmb`, `linearmodels` |
| Event study (returns) | Market-model abnormal returns, BHAR/CAR, calendar-time | `eventstudy`, custom |
| Staggered DID (policy/reform) | Goodman-Bacon, modern estimator, pre-trends | `csdid`, `did`, `fixest` |
| IV / instrument | First-stage F, weak-IV-robust CIs, exclusion argument | `ivreg2`, `weakiv`, `linearmodels` |

## 4. Theory & numerical work (RoF also publishes theory)
- Symbolic / proofs: write assumptions, lemmas, propositions cleanly; keep proofs self-contained in an appendix within the 60-page cap.
- Numerical solution & calibration: `QuantEcon` (Python/Julia), `Dynare` (DSGE-style), MATLAB; pin solver settings and report convergence tolerances.
- Reproducible computation: a master script that regenerates every numerical table/figure; set and report seeds for any simulation/Monte Carlo.

## 5. Figures & exhibits
- Cumulative-return / event-time plots, sorted-portfolio bars, factor loadings, impulse responses for theory.
- Confidence bands shown; avoid chartjunk; vector output (PDF/EPS).
- Remember the **hard 60-page cap includes figures and tables** — budget exhibit space deliberately.

## 6. Reproducibility & the RoF Code Sharing and Data Availability Policy
- Policy applies to papers **first submitted on/after 1 January 2022**: provide replication programs (with software details + comments), actual data if non-proprietary (or a **pseudo-dataset + log files** if proprietary), a **Data Availability Statement**, and **formatted dataset citations**.
- It is a **condition of publication**: accepted papers appear online only **after code is received**, unless an exception is requested in the **cover letter at initial submission**.
- Packages are hosted on the **OUP website as supplementary material** (no separate named archive). Verify current wording on `revfin.org/code-sharing-policy/`.

## 7. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote — set to **Chicago** style.
- Typesetting: LaTeX (TeX Live / MacTeX, Overleaf); export a clean **PDF** (first page numbered page 1) per RoF formatting.

## 8. Process & portal
| Item | Note |
|------|------|
| Submission portal | **Editorial Express** (`editorialexpress.com/rof`) |
| Submission fee | **EUR 350 regular / EUR 300 EFA members**; verify current amount |
| Fast-Track | **EUR 900** first submission, **14-day** decision; verify before paying |
| Review model | **Double-blind**; two-round decision philosophy |
| Replication deposit | Required as a condition of publication; OUP supplementary hosting |
| Publisher | Oxford University Press for the **EFA** |

## 9. Cautions
1. **Verify volatile specifics** (fees, refunds, editors, page/abstract limits, policy wording) on the official pages — they change.
2. **Respect data licenses**; WRDS/CRSP/Compustat redistribution is restricted — share a **pseudo-dataset + log files** when data are proprietary.
3. **Match estimator to design** — plain TWFE on staggered timing, or naïve standard errors in panel finance, are known pitfalls.
4. **Build the replication package as you go** — it is a condition of publication, not an afterthought.
5. **Mind the 60-page cap** — appendices, bibliography, figures, and tables all count.
