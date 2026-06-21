# External Tools & Resources for AEJ: Economic Policy

Data sources, software, and packages useful when preparing an *American Economic Journal: Economic Policy*
(AEJ: Policy) submission. AEJ: Policy is the AEA's quarterly journal for the **economic analysis OF
policy**, so a typical paper combines a **broad-interest policy question**, a **credible quasi-experimental
or RCT evaluation**, a **welfare / cost-benefit / distributional reading**, and a **fully reproducible**
data-and-code deposit. Because the **AEA Data Editor** runs a **pre-publication** reproducibility check on a
deposit in the **AEA Data and Code Repository (openICPSR)**, build the replication package as you go.
Check licenses and current access terms before use; verify volatile process specifics on the official AEA
pages — *(检索于 2026-06；以官网为准)*.

## 1. Data sources

### Policy-evaluation micro & administrative data
| Source | Provider | Typical use |
|--------|----------|-------------|
| IPUMS (CPS, ACS, USA, International) | University of Minnesota | Labor, transfer, education, demographic policy |
| SEER / CDC WONDER / NHIS / MEPS | NCI / CDC / NCHS / AHRQ | Health-policy outcomes and utilization |
| State/federal administrative records (via DUA) | Agencies / state offices | Tax, transfer, UI, Medicaid program evaluation |
| EPA / EIA / emissions inventories | EPA / EIA | Environmental & energy policy outcomes |
| NCES / Common Core of Data / state longitudinal | NCES / states | Education-policy evaluation |
| World Bank WDI / Microdata, DHS, LSMS | World Bank / USAID | Development-policy evaluation |
| Policy databases (state law dates, tax schedules) | NBER TAXSIM, UKCPR, state-law trackers | Coding reform timing for DID; tax/benefit kinks |

> Many policy evaluations rely on **restricted administrative data**. Plan the Data Availability Statement
> and the access path (DUA process, wait time, cost) early — the AEA Data Editor verifies it (see
> `aejpol-replication-package`).

### Experiments & pre-registration
| Source | Provider | Typical use |
|--------|----------|-------------|
| AEA RCT Registry | AEA | Pre-registration + pre-analysis plan for field experiments |
| AsPredicted / OSF Registries | Wharton / COS | Pre-registration of lab/online studies and survey experiments |
| Qualtrics / Prolific / MTurk / oTree | Various | Running surveys and lab-in-the-field policy experiments |

## 2. Statistical & computational software

### Empirical policy evaluation (the core)
- Stata: `reghdfe`, `ivreghdfe`, `csdid`/`did_imputation`/`did_multiplegt_dyn` (modern DID),
  `rdrobust`/`rddensity` (RDD), `bunching`/`rdbwselect` (bunching/kinks), `boottest` (wild-cluster),
  `psacalc` (Oster), `honestdid` (Rambachan–Roth)
- R: `fixest`, `did`, `rdrobust`, `HonestDiD`, `bunching`, `sandwich`/`clubSandwich`
- Python: `linearmodels`, `statsmodels`, `differences`, `doubleml`/`econml` (causal ML)

### Welfare / cost-benefit tooling (AEJ: Policy-specific)
- **MVPF / sufficient-statistics**: implement the welfare ledger directly (numerator = recipient
  willingness-to-pay; denominator = net government cost incl. behavioral fiscal responses); see the
  Policy Impacts / MVPF literature for templates.
- **Tax/benefit microsimulation**: NBER TAXSIM, EUROMOD-style calculators, or hand-coded schedules for
  incidence and mechanical-vs-behavioral decomposition.
- **Synthetic control**: `synth`/`synthdid` (Stata/R) for single-policy case studies.

### Reproducibility tooling (build for the AEA Data Editor)
- Pin versions: `renv.lock` (R), `requirements.txt`/`conda` env (Python), recorded Stata `ssc`/`net`
  package versions; one master script (`run_all`) regenerating every exhibit and in-text number from
  analysis data; set and report seeds for simulation/bootstrap/randomization inference.

## 3. Strategy toolkit by paper type

| Paper type | Core checks | Tools |
|------------|-------------|-------|
| Reform / staggered adoption (DID) | Heterogeneity-robust DID, flat pre-trends, Bacon decomposition, honest-DID | `csdid`, `did_imputation`, `bacondecomp`, `honestdid` |
| Eligibility threshold (RDD) | Density (CJM) test, bandwidth robustness, bias-corrected CI | `rdrobust`, `rddensity` |
| Tax/benefit kink (bunching) | Counterfactual density, structural elasticity, donut checks | `bunching` |
| Field experiment / RCT | Pre-registration, balance, attrition, MHT, link to program cost | AEA RCT Registry, `ritest`, `randcmd` |
| Welfare / cost-benefit reading | Sufficient statistics, MVPF, incidence, uncertainty propagation | TAXSIM, MVPF ledger, bootstrap |

## 4. Figures & tables (AEA house rules)
- **No asterisks or boldface** for statistical significance — report standard errors (or CIs).
- One **self-contained headline exhibit** carrying the policy magnitude (and its welfare reading where
  possible); event-study / RDD / dose-response figures with uncertainty bands; vector output; readable
  greyscale; exhibit notes kept clean and self-contained (see `aejpol-tables-figures`).

## 5. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX. AEA **author–year** house style; the copyeditor applies
  final AEA style at acceptance, so keep references consistent and complete. Online appendix carries long
  material; the main text stays self-contained.
- Typesetting: LaTeX (TeX Live / MacTeX / Overleaf); AEA provides a LaTeX template / style files.

## 6. Process & portal (verify on the official AEA pages)
| Item | Note |
|------|------|
| Submission portal | AEA submission system; **single-blind** — manuscript carries title/byline/affiliations |
| Codes | JEL codes + keywords required on the form |
| Submission fee | Applies; reduced/waived categories exist — **amount VOLATILE, verify on the AEA site** |
| Disclosure | AEA Disclosure Policy — each author discloses funding / interested parties |
| Replication deposit | AEA Data and Code Availability Policy; AEA Data Editor reproducibility check **before** publication; deposit at openICPSR |
| Restricted data | ≥5-yr preservation, public code, documented sources; "upon request" not acceptable |

## 7. Cautions
1. **Verify volatile specifics** (fee, editors, format limits, registry list) on the official AEA pages —
   they change.
2. **Reproducibility is checked before publication** — assemble data, code, and documentation early;
   document any restricted-data access path in the README.
3. **Respect data licenses**; for proprietary/restricted data, state the access path at submission and
   provide all shareable code/extracts for the Data Editor.
4. **Always pair the estimate with a welfare/cost-benefit/distributional reading** — a clean causal effect
   with no policy "so what" is the AEJ: Policy off-fit (see `aejpol-topic-selection`).
