# External Tools & Resources for JCF-Style Empirical Corporate Finance

Data sources, software, and packages useful when preparing a *Journal of Corporate
Finance* (JCF) submission — typically a firm-level empirical corporate-finance question
(capital structure, governance, payout, M&A, financial contracting, innovation,
international corporate finance) with a credible identification strategy, careful
robustness, and an Elsevier Option C data-availability statement. Check licenses and
current access terms before use.

## 1. Data sources

### Firm financials, prices, ownership
| Source | Provider | Typical use |
|--------|----------|-------------|
| Compustat (North America / Global) | S&P Global / WRDS | Accounting fundamentals, leverage, payout |
| CRSP | CRSP / WRDS | Stock prices, returns, event-study windows |
| CRSP/Compustat Merged (CCM) | WRDS | Linked accounting + returns panels |
| Thomson/Refinitiv SDC Platinum | LSEG | M&A, IPO/SEO, syndicated loans, repurchases |
| Refinitiv/Thomson 13F & institutional holdings | LSEG | Institutional ownership, monitoring |
| BoardEx / ISS (RiskMetrics) | WRDS | Boards, directors, governance (E-/G-index) |
| Execucomp | S&P / WRDS | Executive pay, incentives |
| Capital IQ | S&P Global | Private firms, deal detail, capital structure |
| DealScan | LSEG/WRDS | Syndicated loans, covenants, contracting |
| Mergent FISD | WRDS | Corporate bonds, covenants, ratings |
| Audit Analytics | WRDS | Restatements, internal controls, auditor |

### Governance, law, and international
| Source | Provider | Typical use |
|--------|----------|-------------|
| Worldscope / Datastream | LSEG | Cross-country firm panels |
| ORBIS / Amadeus | Bureau van Dijk | Private and international firm data |
| La Porta et al. legal-origin / investor-protection indices | Academic archives | Law-and-finance, international corp. finance |
| SEC EDGAR full-text | SEC | 10-K/8-K/DEF-14A text, filings, disclosure |

## 2. Statistical software

### Stata (common in empirical corporate finance)
- Panel FE at scale: `reghdfe` (firm × year × industry FE), `ppmlhdfe`
- Event studies (returns): `eventstudy2`, custom CAR/BHAR with `estudy`
- DID / staggered timing: `csdid` (Callaway–Sant'Anna), `did_multiplegt_dyn`, `eventstudyinteract` (Sun–Abraham), `bacondecomp`
- IV / endogeneity: `ivreg2`, `ivreghdfe`, `xtabond2` (dynamic panel GMM for leverage)
- RDD: `rdrobust`, `rddensity`
- Matching: `psmatch2`, `teffects`, entropy balancing (`ebalance`)
- Inference: `boottest` (wild-cluster bootstrap), two-way clustering (`vcemway`)
- Winsorizing/standard tooling: `winsor2`, `estout`/`esttab` for tables

### R
- Panel/FE & IV: `fixest` (`feols`, fast multi-way FE, `sunab`), `plm`
- DID: `did`, `didimputation`, `bacondecomp`
- Event studies: `eventstudies`, `estudy2`-style custom CAR
- Matching/weighting: `MatchIt`, `WeightIt`, `ebal`
- Reproducibility: `renv` (pin versions), `targets` (pipeline)

### Python
- `pandas`, `numpy`, `wrds` (WRDS API) — data wrangling and pulls
- `linearmodels` (panel IV / FE), `statsmodels` — estimation
- `pyfixest` — fast fixed-effects / DID in Python
- `matplotlib` / `seaborn` — figures; `pip freeze` / `requirements.txt` to pin

## 3. Identification toolkit by design (corporate finance)

| Design | Core checks | Packages |
|--------|-------------|----------|
| Staggered DID (law/reg shocks) | Goodman-Bacon decomposition, modern estimator, parallel-trends/event-study leads | `csdid`, `did`, `did_multiplegt_dyn`, `fixest` |
| Event study (returns) | Clean window, confounding-news screen, BHAR/CAR robustness | `eventstudy2`, `estudy` |
| IV / GMM | First-stage F, exclusion argument, weak-IV-robust CIs; dynamic-panel GMM for leverage | `ivreg2`, `xtabond2`, `linearmodels` |
| RDD (e.g., voting/index thresholds) | Density/manipulation test, bandwidth robustness | `rdrobust`, `rddensity` |
| Matching / weighting | Covariate balance, common support, sensitivity | `psmatch2`, `teffects`, `ebalance` |

## 4. Figures and tables
- Event-study/CAR plots with confidence bands; binned scatters for nonlinearity
- Self-contained table notes: sample, FE, clustering, winsorizing, units
- Vector output (PDF/EPS) for print; avoid chartjunk

## 5. Reproducibility & data policy (Elsevier Option C)
- JCF follows Elsevier **Option C**: state data availability at submission; deposit/cite/link
  research data and code or explain why it cannot be shared. There is **no** JFE-Data-Archive-style
  mandatory finance-society archive — verify on the current Guide for Authors.
- Deposit code/data (where licenses allow) on Mendeley Data, Zenodo, or openICPSR; cite with a DOI.
- For licensed data (Compustat, CRSP, SDC, DealScan), share **code + variable construction +
  access instructions**, not the proprietary raw data.
- One master script (`run_all`) regenerating every table/figure; pin software versions; set seeds.

## 6. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote — set to **author-date (Harvard)** style
- "Your paper, your way" at first submission: any consistent style with all required elements; DOIs encouraged; full Elsevier styling at revision
- Free integrated **SSRN** preprint posting is offered at submission (Elsevier/SSRN perk)

## 7. Process & portal
| Item | Note |
|------|------|
| Submission portal | **Editorial Manager**, reached from the ScienceDirect "Submit your article" link |
| Submission fee | **US$340 non-refundable**, paid during submission; not refunded on desk reject — verify current amount |
| Review model | **Single-anonymized (single-blind)**; minimum two reviewers; active desk-rejection |
| Abstract | **≤ 250 words**; 1–7 keywords; no references in abstract |
| Declarations | Generative-AI disclosure + competing-interest declaration required |
| Publisher | Elsevier |

## 8. Cautions
1. **Verify volatile specifics** (fee, editors, abstract cap, data policy, review model) on the official Guide for Authors — they change. Items marked 待核实 in `official-source-map.md` are not load-bearing.
2. **Respect data licenses**; WRDS/Compustat/CRSP/SDC/DealScan terms prohibit redistributing raw data.
3. **Match estimator to design** — plain TWFE on staggered governance/regulation shocks is a known pitfall.
4. **Budget the US$340 fee** — it is charged up front and not refunded even on desk rejection.
