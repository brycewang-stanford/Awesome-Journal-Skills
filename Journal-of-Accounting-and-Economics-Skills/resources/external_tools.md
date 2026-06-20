# Positive-Accounting Research Tools & Resources (JAE)

This document lists external data sources, econometric software, and writing tools commonly used
when preparing a positive (economics-based) accounting manuscript for the **Journal of Accounting
and Economics (JAE)**. JAE's dominant methodology is large-sample empirical archival research
grounded in economics — capital-markets information content, financial contracting, agency/monitoring,
and corporate disclosure — plus analytical economic modeling in the Watts-Zimmerman tradition.
The toolkit below is weighted accordingly. Always verify licensing terms and current JAE/Elsevier
policies before using any resource.

## 1. Data Sources

### Capital-markets and accounting fundamentals
| Source | Provider | Typical use |
|--------|----------|-------------|
| Compustat (North America / Global) | S&P Global / WRDS | Accounting fundamentals, accruals, earnings |
| CRSP | Center for Research in Security Prices | Returns, prices, market reaction (event studies) |
| I/B/E/S | LSEG / WRDS | Analyst forecasts, consensus, earnings surprises |
| Compustat-CRSP Merged (CCM) | WRDS | Linking fundamentals to returns |
| Thomson Reuters 13F / s34 | WRDS | Institutional ownership, monitoring |
| TAQ | NYSE / WRDS | Intraday liquidity, bid-ask spreads, information asymmetry |
| RavenPack / Capital IQ Key Developments | Various | News, events, disclosure timing |

### Contracting, governance, and disclosure
| Source | Provider | Typical use |
|--------|----------|-------------|
| Execucomp | S&P Global / WRDS | Executive compensation, contracting incentives |
| ISS (RiskMetrics) | ISS / WRDS | Governance, board, antitakeover provisions |
| BoardEx | Management Diagnostics | Director networks, executive ties |
| DealScan | LSEG / WRDS | Private debt contracts, covenants |
| Audit Analytics | Audit Analytics | Restatements, auditor, internal-control opinions, fees |
| SEC EDGAR (10-K, 8-K, DEF 14A) | US SEC | Disclosure text, MD&A, restatements, filings |

### Standards, regulation, and the accounting profession
| Source | Use |
|--------|-----|
| FASB / IASB project records & comment letters | Standard-setting, determination of GAAP/IFRS |
| PCAOB inspection reports | Audit-quality regulation |
| SEC AAERs (enforcement releases) | Fraud, misreporting, enforcement |

## 2. Analysis Software & Packages

### Archival capital-markets econometrics (the JAE workhorse)
- **Stata**: `reghdfe` (high-dimensional fixed effects), `ivreghdfe`/`ivreg2` (IV/2SLS), `xtreg`, two-way clustering (`vce(cluster firm year)` / `reghdfe`), `csdid`/`did` (modern staggered DiD), `psmatch2`/`teffects` (matching), `winsor2` (winsorizing).
- **SAS**: still common for building Compustat/CRSP/I/B/E/S samples on WRDS; PROC SQL for merges, PROC REG/SURVEYREG.
- **R**: `fixest` (fast FE + clustered SE), `did`, `sandwich`/`lmtest`, `RPostgres` for WRDS cloud.
- **Python**: `pandas`, `linearmodels` (panel/IV), `wrds` package for programmatic WRDS pulls.

### Identification and causal design
- Event studies (short-window CARs around earnings/disclosure events); difference-in-differences around regulatory shocks (e.g., SOX, IFRS adoption, FAS/ASU changes); regression discontinuity; instrumental variables; Heckman selection. Cluster standard errors by firm and/or year to match the panel structure.

### Earnings quality / accruals measures
- Modified Jones discretionary accruals, Dechow-Dichev accrual quality, real-earnings-management proxies (Roychowdhury), conditional conservatism (Basu), value relevance (Ohlson) — implement in Stata/SAS from Compustat fundamentals.

### Analytical / modeling work
- **Mathematica** or **Maple** for closed-form contracting/disclosure models; **LaTeX** for proofs. JAE publishes economics-style analytical models (e.g., disclosure, agency, contracting), so a clean model section with assumptions, propositions, and proofs in an appendix is in-scope.

## 3. Reference & Writing Tools

| Tool | Note |
|------|------|
| LaTeX + elsarticle.cls + BibTeX | Elsevier's recommended LaTeX class for JAE; author-date (Harvard) style |
| Zotero / EndNote / Mendeley | Configure to Elsevier author-date (Harvard); reconcile against the current Guide for Authors |
| Overleaf | Convenient for elsarticle + BibTeX collaboration |
| Grammarly | Language polish (American spelling per JAE keywords) |

JAE uses Elsevier author-date (Harvard) referencing (alphabetical then chronological, a/b/c suffixes for
same-author/same-year). Configure your reference manager accordingly and reconcile against the current
Guide for Authors.

## 4. Submission & Process

- **Submission portal**: Elsevier **Editorial Manager (EM)**; local source-map defaults use **USD 650** for new manuscripts with no fee for resubmissions, paid via Elsevier's Submission Start portal (submissionstart.elsevier.com) — verify the current amount on the live Guide for Authors.
- **Required at submission**: anonymized manuscript (double-anonymized review) plus a separate title page with author details; **Highlights** (2-5 bullets, ≤125 chars each); up to **6 keywords**; up to **6 JEL codes**.
- **ORCID**: keep an ORCID linked to your EM account.
- **Originality**: Elsevier screens with Crossref Similarity Check (iThenticate); no simultaneous submission.

## 5. Reproducibility & Transparency

1. Keep clean, commented analysis scripts (Stata do-files, SAS/R programs) that regenerate every table from the raw WRDS pull.
2. Document the sample-construction waterfall (population, merges, exclusions, final N) — JAE reviewers expect a reproducible sample table.
3. Note that JAE does **not** mandate a replication archive (only Elsevier's voluntary "encourages" policy), unlike sister journal JAR or finance journals (JFE) that require deposits — but a voluntary Data Statement and well-documented code strengthen credibility.
4. Respect WRDS/vendor confidentiality and licensing terms before sharing any derived data.

## 6. Verify Before You Rely

The co-Editors, submission portal link, the fee amount, Highlights/keyword/JEL requirements, and
the research-data policy can change. Always confirm current requirements on the official JAE Guide
for Authors (ScienceDirect) and the Elsevier submission-fee policy page before submitting.
