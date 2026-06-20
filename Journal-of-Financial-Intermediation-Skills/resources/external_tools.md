# External Tools & Resources for JFI-Style Banking & Intermediation Research

Data sources, software, and packages useful when preparing a *Journal of Financial Intermediation*
(JFI) submission — theory or empirics on banks, intermediaries, corporate finance, regulation, and the
economics of financial institutions and markets. Check licenses and current access terms before use; many
bank-level and supervisory datasets are restricted or fee-based.

## 1. Data sources

### Banks, intermediaries & supervisory data
| Source | Provider | Typical use |
|--------|----------|-------------|
| Call Reports (FFIEC 031/041) & FR Y-9C | FFIEC / Federal Reserve | US bank/BHC balance sheets, income, capital |
| FDIC SDI / BankFind | FDIC | US bank financials, failures, branch structure |
| SNL / S&P Capital IQ (financials) | S&P Global | Bank fundamentals, deals, ownership |
| Bankscope / BankFocus / Orbis | Moody's / Bureau van Dijk | Global bank financials |
| ECB SDW, EBA transparency, BIS statistics | ECB / EBA / BIS | Euro-area & cross-border banking |
| Y-14 / FR Y-14 (restricted), DealScan / LPC | Fed / Refinitiv | Stress-test, syndicated-loan-level data |

### Credit, loans & markets
| Source | Provider | Typical use |
|--------|----------|-------------|
| DealScan (LPC) | Refinitiv | Syndicated loan terms, lead arrangers |
| Mergent FISD | Mergent | Corporate bond issues and covenants |
| HMDA | CFPB / FFIEC | Mortgage applications, lending discrimination |
| Y-14M, McDash / BlackKnight | Fed / ICE | Loan-level mortgage performance |
| CRSP / Compustat / TRACE | WRDS | Equity, firm fundamentals, bond trades |

### Regulation, policy & identification hooks
| Source | Provider | Typical use |
|--------|----------|-------------|
| Bank regulatory changes / Basel timelines | BIS / national regulators | Policy-shock identification |
| Branching-deregulation indices (e.g., IBBEA) | Academic archives | Staggered DID natural experiments |
| Fed funds / shadow-rate series, MP surprises | FRED / academic | Monetary-transmission designs |

## 2. Statistical software

### Stata (common in banking empirics)
- Panel / fixed effects: `reghdfe` (multi-way FE), `ppmlhdfe`
- DID / event study: `csdid` (Callaway–Sant'Anna), `eventstudyinteract` (Sun–Abraham), `did_multiplegt_dyn` (de Chaisemartin–D'Haultfœuille), `bacondecomp` (Goodman-Bacon)
- IV: `ivreg2`, `ivreghdfe`, weak-IV-robust inference (`weakiv`, `condivreg`)
- RDD: `rdrobust`, `rddensity`, `rdbwselect`
- Clustering / inference: `boottest` (wild cluster bootstrap), `acreg` (spatial/HAC)
- Bank-network / matched lender-borrower designs: `reghdfe` with absorbed bank×time and firm×time FE

### R
- `fixest` (high-dimensional FE, fast event studies), `did`, `didimputation`, `synthdid`
- `sandwich` / `lmtest` / `fwildclusterboot` for robust and cluster-robust inference
- `ivreg`, `AER` for IV; `rdrobust` for RDD

### Python
- `linearmodels` (PanelOLS, IV2SLS), `pyfixest` (fixest-style FE + event studies)
- `statsmodels`, `econtools`; `differences` for modern DID estimators

## 3. Theory & numerical toolkits (for theory-led JFI papers)

- LaTeX with `amsthm`/`amsmath` for theorem-proof exposition; `tikz` for timelines and model structure
- Mathematica / SymPy for comparative statics and symbolic derivations
- MATLAB / Python (`numpy`, `scipy`) for numerical examples, calibrated illustrations of a model's mechanism

## 4. Writing, references & submission

- Reference managers (Zotero, EndNote, BibTeX) — submit in any internally consistent style; Elsevier
  applies the journal's **author–date** style at proof, so keep author–year fields clean.
- Elsevier `elsarticle` LaTeX class and Word template for typesetting-ready editable files after acceptance.
- SSRN — optional free preprint posting offered during submission to Editorial Manager (does not count as
  prior publication).
- Data deposit: a general-purpose repository (e.g., Mendeley Data, Zenodo, ICPSR, openICPSR) linkable via
  Editorial Manager, with a published **Data Statement** and `[dataset]`-tagged references. JFI follows
  Elsevier Option C: deposit/cite/link research data where possible or explain why sharing is restricted;
  the Guide does not name a JFI-specific archive — see `jfi-replication-and-data-policy`.
