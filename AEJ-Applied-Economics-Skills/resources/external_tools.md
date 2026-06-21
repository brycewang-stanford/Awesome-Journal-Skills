# External Tools & Resources for AEJ: Applied

Data sources, software, and packages useful when preparing an *American Economic
Journal: Applied Economics* (AEJ: Applied) submission. AEJ: Applied is the American
Economic Association's quarterly journal for **empirical applied microeconomics
with credible causal identification**, so a typical paper combines a **substantive
applied-micro question** with a **clean research design** and a **fully
reproducible data + code package**. Because the **AEA Data Editor (Lars Vilhuber)**
runs a **pre-publication reproducibility check** on the openICPSR deposit, build the
replication package as you go. Check licenses, access terms, and live AEA process
pages before use.

## 1. Data sources

### Public-use micro & administrative
| Source | Provider | Typical use |
|--------|----------|-------------|
| IPUMS (CPS, ACS, USA, International, Health) | University of Minnesota | Labor, demography, health, education |
| PSID / NLSY | U. Michigan / BLS | Life-cycle, intergenerational, labor dynamics |
| World Bank Microdata / LSMS / DHS | World Bank / USAID | Development microeconomics, health |
| Administrative registers (linked tax/education/health) | National statistical offices | Quasi-experimental designs (often restricted) |
| FRED / Census County Business Patterns | St. Louis Fed / Census | Local labor markets, shift-share exposure |

### Experimental & own-data
| Source | Provider | Typical use |
|--------|----------|-------------|
| AEA RCT Registry | AEA | Pre-registration of field experiments |
| AsPredicted | Wharton Credibility Lab | Pre-registration of lab/online studies |
| OSF Registries | Center for Open Science | Pre-registration + materials hosting |
| SurveyCTO / Qualtrics / oTree / Prolific | Various | Field/lab/online data collection |

> Pre-register own-data studies and keep instruments/instructions; the AEA data
> policy expects survey instruments and experiment instructions in the deposit.

## 2. Statistical & computational software

### Empirical micro / causal inference (AEJ: Applied core)
- Stata: `reghdfe`, `ivreghdfe`/`ivreg2`, `weakivtest`, `csdid`/`did_imputation`/
  `did_multiplegt_dyn` (modern DID), `eventdd`, `rdrobust`/`rddensity` (RD),
  `boottest` (wild-cluster), `ritest` (randomization inference), `psacalc` (Oster δ)
- R: `fixest`, `did` (Callaway–Sant'Anna), `HonestDiD`, `rdrobust`, `rdd`,
  `sandwich`/`clubSandwich`, `ivmodel`, `fwildclusterboot`
- Python: `linearmodels`, `statsmodels`, `differences`/`pyfixest`, `doubleml`/
  `econml` (causal ML), `rdrobust` (Python port)

### Reproducibility tooling (build for the AEA Data Editor)
- Pin versions: Stata `version` + recorded `ssc`/`net` package versions;
  `requirements.txt`/conda env (Python); `renv.lock` (R)
- One master script (`run_all`) regenerating every table and figure from raw data
- Set and report seeds for simulation / bootstrap / randomization inference
- Relative paths from a single root macro; AEA README template + Data Availability
  Statement; an exhibit-to-code map (Table 3 → `code/05_main.do`)

## 3. Strategy toolkit by design

| Design | Core checks | Tools |
|--------|-------------|-------|
| RCT / field experiment | pre-registration, balance, attrition (Lee bounds), MHT | AEA RCT Registry, `ritest`, `randomizr` |
| Difference-in-differences / event study | staggered-timing bias, pre-trends, honest-DID | `csdid`, `did`, `HonestDiD`, `bacondecomp` |
| Regression discontinuity | density/manipulation, bandwidth, bias-corrected CIs | `rdrobust`, `rddensity` |
| IV / shift-share | first-stage strength, exclusion, exposure design | `ivreg2`, `weakivtest`, shift-share diagnostics |

## 4. Figures & tables (AEA house rules)
- AEA permits **significance stars** but **expects standard errors** in
  parentheses; report the dependent-variable mean and the clustering level in
  self-contained notes.
- Lead with the design's signature figure (event-study with CIs, RD with density,
  balance with joint test); avoid chartjunk; vector output preferred for finals.
- Online appendix for supplementary tables/figures, kept separate from the main paper.

## 5. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX. AEA uses an author-date (Chicago-ish)
  house style; keep references complete and consistent.
- Typesetting: LaTeX (TeX Live / MacTeX / Overleaf) or Word; the AEA provides LaTeX
  templates for accepted manuscripts.

## 6. Process & portal (check official AEA pages before submission)
| Item | Note |
|------|------|
| Submission portal | AEA ScholarOne system; main PDF + supplemental appendix as needed |
| Review | Single-blind; author identities are visible to referees |
| Front matter | Title/byline/affiliations on first page; JEL codes; abstract of 100 or fewer words |
| Submission fee | AEA member/nonmember and country-income fee tiers; rejected-without-review papers receive a 50 percent refund |
| Publication fee | USD 15 per typeset page for accepted papers first submitted on or after 1 February 2024 |
| Replication deposit | AEA Data and Code Repository on openICPSR; Data Editor reproducibility check **before** publication |
| Disclosure | Funding and interested-party relationships per AEA disclosure policy |

## 7. Cautions
1. Check editor, fee, and policy details on the official AEA pages during
   submission week.
2. **Reproducibility is checked before publication** — assemble raw data, code, and
   documentation early; document restricted-data access and provide a synthetic
   extract where possible.
3. **Respect data licenses**; for restricted/administrative data, document the exact
   access procedure and flag any exemption at the earliest opportunity.
4. **Match diagnostics to the design** — balance/attrition for RCTs; pre-trends and
   heterogeneity-robust estimators for DID; density/bandwidth for RD; first-stage
   and exclusion for IV.
