# External Tools & Resources for RJE-Style Industrial Organization

Data sources, software, and packages useful when preparing a *RAND Journal of
Economics* (RJE) submission — applied microeconomics with an industrial-organization
core (regulated industries, antitrust/competition, market structure, firm strategy,
the economic analysis of organizations). Both **structural** and **reduced-form**
empirical work is welcomed, alongside theory. Check licenses and current access terms
before use, and confirm volatile process facts on rje.org.

## 1. Data sources (IO-flavored)

### Firms, markets, antitrust
| Source | Provider | Typical use |
|--------|----------|-------------|
| Compustat / CRSP (WRDS) | Wharton / S&P | Firm financials, market structure, entry/exit |
| Nielsen Retail Scanner / Consumer Panel | Kilts Center, U. Chicago Booth | Demand estimation, pricing, product markets |
| IRI / NielsenIQ scanner data | Vendors | Brand-level demand, BLP-style estimation |
| FTC / DOJ antitrust case records, HMG | US agencies | Merger analysis, market definition |
| Census of Manufactures / CMF (FSRDC) | US Census Bureau | Plant-level productivity, concentration |

### Regulated industries & networks
| Source | Provider | Typical use |
|--------|----------|-------------|
| FCC spectrum auction / licensing data | FCC | Auctions, telecom market structure |
| FERC / EIA electricity & energy data | US agencies | Electricity markets, regulation |
| DOT / BTS airline (DB1B, T-100) | US DOT | Airline competition, pricing, entry |
| Medicare / CMS claims & plan data | CMS | Health-insurance markets, regulation |
| Patent / USPTO & PATSTAT | USPTO / EPO | Innovation, licensing, R&D, IP |

## 2. Statistical & structural software

### Stata
- Demand / IO structural: BLP-style estimation via user packages and custom code; `pyblp` (via Python) is the reference implementation
- Reduced-form: `reghdfe` (high-dimensional FE), `ivreghdfe`, `ppmlhdfe`
- DID / event study: `csdid` (Callaway–Sant'Anna), `did_multiplegt_dyn`, `eventstudyinteract` (Sun–Abraham)
- Auctions / discrete choice: `asclogit`, `cmclogit`/`cmmixlogit` (mixed logit)
- Inference: `boottest` (wild-cluster bootstrap), cluster-robust SEs at market level

### Python
- `pyblp` — random-coefficients (BLP) demand estimation, the IO workhorse
- `linearmodels` — panel IV / FE; `statsmodels` — discrete choice, GMM scaffolding
- `numpy` / `scipy` — custom structural estimation, nested fixed-point, MPEC
- `pandas` — data wrangling; `matplotlib` — exhibits

### R
- `BLPestimatoR` — BLP demand; `gmm` — GMM moment estimation
- `fixest` (`feols`, `sunab`) — fast FE, IV, event studies
- `mlogit` / `gmnl` — discrete-choice / mixed logit demand
- `did`, `bacondecomp` — modern DID diagnostics

## 3. IO identification & estimation toolkit by approach

| Approach | Core elements | Tools |
|----------|---------------|-------|
| BLP demand | Instruments for price (cost shifters, BLP/Gandhi–Houde), micro-moments | `pyblp`, `BLPestimatoR` |
| Production / productivity | Olley–Pakes / Levinsohn–Petrin / ACF control functions | `prodest`, custom |
| Dynamic / entry games | CCP estimation (Hotz–Miller), moment inequalities | custom, `pyblp` ecosystem |
| Auctions | First-order conditions, identification of value distributions | custom |
| Reduced-form merger/regulation | DID off a policy/merger shock, event study | `csdid`, `fixest` |

## 4. Figures & tables (RJE Style Guide)
- Sections numbered consecutively; **subsections left unnumbered**; equations numbered flush right, `(1a)/(1b)` for multi-part
- Demand/cost parameter tables, elasticity matrices, merger simulation tables, counterfactual welfare exhibits
- Vector output (PDF/EPS) for print; keep figures legible in greyscale

## 5. Reproducibility
- Pin software and package versions (`requirements.txt`, recorded `ssc`/`net` versions, `renv.lock`)
- One master script regenerating every table and figure (structural estimation can be slow — cache intermediate objects and document runtime)
- Set and report random seeds for simulation, bootstrap, and starting values in non-convex structural optimization
- **No official RJE data/code-deposit (replication-package) requirement was located — 待核实.** Build a clean package anyway; see `rje-replication-and-data-policy`.

## 6. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote — set to **author-date** style with **no page numbers in in-text cites** and **no issue numbers** in journal references (RJE Style Guide)
- The Style Guide directs authors to the **Chicago Manual of Style** (the page links to the **18th edition**)
- Typesetting: **Word or LaTeX** accepted at submission; observe house usage rules (because/as not *since*; whereas/although not *while*; "article" not "paper")

## 7. Process & portal
| Item | Note |
|------|------|
| Submission portal | **Wiley Research Exchange** — `wiley.atyponrex.com/journal/RAND` (mandatory since April 23, 2025; replaced Editorial Express / e-submit) |
| Submission fee | **Per-article fee** (Wiley guidelines); **non-refundable as of January 1, 2026** — exact amount 待核实 (snippets disagree, $100 vs $200; Wiley page HTTP 402), verify in portal |
| Page caps | Main text <=40 pp; appendices+refs <=10 pp; total <=50 pp; double-spaced |
| Abstract | <=100 words |
| Review | Editor screen → two anonymous referees → handling Editor |
| Publisher | RAND in partnership with **Wiley** |

## 8. Cautions
1. **Verify volatile specifics** (fee, editors, page caps, portal URL, data policy) on rje.org and the Wiley For Authors page — they change.
2. **Respect data licenses**; restricted data (FSRDC, Nielsen/Kilts, CMS) require formal access and disclosure review.
3. **Match estimator to the IO question** — a misspecified demand system or naive TWFE on staggered policy timing is a known pitfall.
4. **Page caps are hard at submission** — budget exposition; the 40/50-page limit is enforced, unlike word-count-only journals.
