# Empirical-Accounting Tools & Resources (JAR)

This document lists external data sources, analysis software, and writing tools commonly
used when preparing an empirical-accounting manuscript for the **Journal of Accounting
Research (JAR)**. JAR's defining tradition is empirical-archival capital-markets work (the
Ball-Brown lineage), so the core toolkit is built around large-sample financial-statement
and market data and reproducible code, but JAR also publishes experimental, analytical, and
field-study work — the toolkit spans those traditions too. Because JAR **requires and hosts
replication materials** under its data-and-code sharing policy, treat clean, runnable code
as a first-class deliverable, not an afterthought. Always verify licensing terms and the
current JAR/Chookaszian Center and Wiley policies before using any resource.

## 1. Data Sources

### Financial-statement, market, and capital-markets archival data
| Source | Provider | Typical use |
|--------|----------|-------------|
| Compustat (North America / Global) | S&P Global Market Intelligence | Financial-statement fundamentals, segments |
| CRSP | Center for Research in Security Prices (Chicago Booth) | Stock returns, prices, delisting, market data |
| CRSP/Compustat Merged (CCM) | WRDS | Linking fundamentals to returns for event/returns tests |
| I/B/E/S | LSEG | Analyst forecasts, recommendations, actuals (expectations) |
| Thomson/Refinitiv 13F & Institutional | LSEG | Institutional ownership |
| Audit Analytics | Audit Analytics | Auditor, restatements, internal-control opinions, fees, comment letters |
| RavenPack / news analytics | RavenPack | Disclosure timing, sentiment, information events |
| TAQ | NYSE / WRDS | Intraday trades & quotes, liquidity, bid-ask spreads |
| Capital IQ / Orbis | S&P Global / Bureau van Dijk | Private firms, global and deal data |

### Regulatory, disclosure, and text data
| Source | Use |
|--------|-----|
| SEC EDGAR (10-K, 10-Q, 8-K, DEF 14A, comment letters) | Disclosure text, filings, governance, MD&A |
| SEC AAERs / litigation releases | Enforcement, misstatement/fraud settings |
| PCAOB inspection reports | Audit quality settings |
| FASB / IASB pronouncements & comment letters | Standard-setting and adoption shocks (natural experiments) |
| EDGAR Log File Data Set | Filing-download "attention" measures |

### Experimental / field-study infrastructure
| Source | Use |
|--------|-----|
| Prolific / Qualtrics / CloudResearch | Experiments with non-professional or screened participants |
| Practitioner / preparer / investor panels | Field experiments and surveys (often paired with Registered Reports) |

## 2. Analysis Software & Packages

### Archival capital-markets econometrics (the JAR workhorse)
- **Stata**: `reghdfe` (high-dimensional fixed effects), `ivreghdfe`/`ivreg2` (IV/2SLS), `xtreg`, `boottest` (wild-cluster bootstrap), `did`/`csdid` (modern staggered DiD), `rdrobust` (RD), `psmatch2`/`teffects` (matching), `estout`/`outreg2` (exhibit export).
- **SAS**: still common for building Compustat/CRSP/I/B/E/S panels and event-study return windows at scale.
- **R**: `fixest` (fast high-dimensional FE and clustered SE), `did` (Callaway-Sant'Anna), `RDHonest`, `sandwich`/`lmtest`, `modelsummary` for tables.
- **Python**: `pandas`, `linearmodels` (panel/IV), `wrds` API for pulling WRDS data programmatically.

### Standard-error and identification discipline
- Cluster by firm and/or year (two-way) as the setting requires; consider wild-cluster bootstrap when clusters are few.
- Event-study returns: market-model / Fama-French abnormal returns; calendar-time portfolios for long-window tests.

### Experimental and analytical work
- Experiments: `pwr`/`simr` (R) or G*Power for power; pre-registration via the JAR **Registered Reports** track (Stage 1 protocol) rather than only OSF/AsPredicted.
- Analytical/modeling: Mathematica or symbolic math for closed-form models that motivate empirical predictions.

## 3. Reference & Writing Tools

| Tool | Note |
|------|------|
| Zotero / EndNote / Mendeley | Configure to a **JAR / Chicago author-date** style, then reconcile against recent JAR articles |
| Overleaf / LaTeX | Common in archival accounting; verify Wiley Research Exchange accepts your format |
| Grammarly | Language polish |

JAR uses a custom author-date house style (consistent with Chicago author-date conventions);
it is **not** APA/numeric. Match the citation and reference formatting of recent JAR articles.

## 4. Submission, Fees & Process

- **Submission portal**: Wiley Research Exchange / Atypon Rex at `wiley.atyponrex.com/journal/JOAR`.
- **Tiered submission fee** (effective Jan 1, 2023): Tier One $750 / Tier Two $500 / Tier Three $50; the fee must be received within one week of submission or the paper is withdrawn (generally non-refundable; a non-conforming desk reject may receive a half refund). Confirm current amounts and your residency tier.
- **Submission cap**: at most four new papers per author over a rolling two-year period (R&R resubmissions excluded).
- **Article types**: Regular Manuscripts; Surveys/Methodological Contributions; Registered Reports.
- **Originality/integrity**: no simultaneous submission; AI tools cannot be authors.

## 5. Reproducibility & the JAR Data-and-Code Sharing Policy

JAR is distinctive among the top-three accounting journals in **requiring and hosting**
replication materials (datasheets and code posted as online supplements), not merely
encouraging them. Prepare for this from day one:

1. Keep clean, commented, top-to-bottom runnable scripts (Stata do-files, SAS, R, Python) that regenerate **every** table and figure from raw extracts.
2. Document data sources, sample-construction steps, screens, and exclusion rules; record WRDS/library vintages and access dates (raw licensed data usually cannot be redistributed).
3. Prepare the datasheet/code package and a README that lets a third party reproduce results; respect the policy's terms of use (academic-research-only, acknowledgement of the JAR publication and code authors, authors retain copyright).
4. For Registered Reports, the analysis code should match the pre-approved Stage 1 protocol.

## 6. Verify Before You Rely

Editor roster, submission portal, fee tiers, article-type rules, conference theme/deadlines,
and the exact wording of the data-and-code policy change over time. Always confirm current
requirements on the official Chookaszian Center JAR pages and the Wiley author guidelines
before submitting (see `official-source-map.md` for URLs).
