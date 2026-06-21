# External Tools & Resources for JOLE-Style Labor Economics

Data sources, software, and packages useful when preparing a *Journal of Labor Economics* (JOLE)
submission — applied or theoretical work on wages and earnings, employment and unemployment, human
capital and education, labor supply and demand, household and family economics, discrimination, unions,
migration, and labor-market institutions and policy. JOLE publishes empirical / simulation / experimental
papers only when the data are documented and available for replication, so build the replication package
as you go. Check licenses and current access terms before use.

## 1. Data sources

### US labor-market micro (the JOLE workhorse datasets)
| Source | Provider | Typical use |
|--------|----------|-------------|
| CPS (Current Population Survey, incl. ASEC / MORG) via IPUMS-CPS | BLS / Census, U. Minnesota | Wages, earnings, employment, labor supply |
| ACS / Decennial Census via IPUMS-USA | US Census Bureau, U. Minnesota | Earnings, migration, education, demographics |
| LEHD / QWI and LBD (FSRDC) | US Census Bureau | Matched employer–employee earnings & job flows |
| NLSY79 / NLSY97 | BLS | Human capital, life-cycle earnings, careers |
| PSID | U. Michigan | Intergenerational mobility, family labor supply |
| SIPP | US Census Bureau | Program participation, labor supply dynamics |
| O*NET / DOT task data | US DOL | Occupational tasks, skills, automation |

### International & administrative labor data
| Source | Provider | Typical use |
|--------|----------|-------------|
| Linked employer–employee registers (e.g., German IAB, Scandinavian registers) | National statistical agencies | Firm wage premia, AKM models, displacement |
| ILOSTAT | International Labour Organization | Cross-country labor-market indicators |
| Luxembourg Income Study (LIS) | LIS Cross-National | Comparative earnings & inequality |
| AEA RCT Registry | AEA | Pre-registration of labor field experiments |

## 2. Statistical software

### Stata (dominant in applied labor)
- AKM / two-way FE wage decompositions: `reghdfe`, `a2reg`, `leave-out` connected-set tools
- DID / event study: `csdid` (Callaway–Sant'Anna), `eventstudyinteract` (Sun–Abraham), `did_multiplegt_dyn` (de Chaisemartin–D'Haultfœuille), `bacondecomp` (Goodman-Bacon)
- IV: `ivreg2`, `ivreghdfe`, weak-IV-robust inference (`weakiv`, `condivreg`)
- RDD: `rdrobust`, `rddensity`, `rdbwselect`
- Wage decompositions: `oaxaca` (Blinder–Oaxaca), `rif`/`rifreg` (RIF / unconditional quantile)
- Labor supply / selection: `heckman`, structural discrete-choice via `asclogit`
- Inference: `boottest` (wild-cluster bootstrap), `ritest` (randomization inference)

### R
- DID / event study: `did`, `fixest` (`sunab`, `feols` with high-dimensional FE), `didimputation`
- AKM / FE: `lfe::felm`, `fixest::feols`, `igraph` for connected sets
- RDD: `rdrobust`, `rddensity`
- Decompositions: `oaxaca`, `dineq`, `Counterfactual`
- Reproducibility: `renv` (pin versions), `targets` (pipeline)

### Python
- `pandas`, `numpy` — data wrangling
- `linearmodels`, `statsmodels` — panel IV / FE estimation
- `pyfixest` — fast fixed effects / event studies
- `econml`, `doubleml` — heterogeneous / causal ML for labor
- `matplotlib` / `binsreg` — figures and binscatters
- `pip freeze` / `requirements.txt` — pin the environment

## 3. Identification toolkit by design (labor norms)
| Design | Core checks | Packages |
|--------|-------------|----------|
| Staggered DID (policy/minimum-wage/reform) | Goodman-Bacon decomposition, modern estimator, event-study leads | `csdid`, `did`, `did_multiplegt_dyn`, `fixest` |
| RDD (program eligibility thresholds) | Density manipulation test, optimal bandwidth, robustness | `rdrobust`, `rddensity` |
| IV (e.g., shift-share / Bartik) | First-stage F, weak-IV-robust CIs, exposure-share exogeneity | `ivreg2`, `weakiv`, `linearmodels` |
| RCT (labor field experiment) | Balance, attrition (Lee bounds), MHT correction | `ritest`, `randcmd` |
| AKM firm–worker FE | Connected set, limited-mobility-bias / leave-out correction | `reghdfe`, leave-out estimators |

## 4. Figures & tables
- Event-study plots, RDD discontinuity plots, binned scatters (`binsreg`), wage-profile and decomposition charts
- Remember JOLE's word economy: **a full-page table or figure counts as 500 words** toward the ~20,000-word
  limit, so every exhibit must earn its space
- Vector output (PDF/EPS) for print resolution; self-contained notes

## 5. Reproducibility & replication (JOLE Dataverse)
- After acceptance, deposit **data, programs, and documentation** to **JOLE's Dataverse Repository** before
  publication; for econometric/simulation papers, include the final-model datasets and programs plus a
  description of how intermediate datasets/programs built the final dataset (JOLE follows the **AER
  data-availability policy adopted February 2009**)
- One master script (`run_all`) regenerating every table and figure from the analysis data
- Pin software/package versions; set and report random seeds
- **Notify the editor at submission** if data are proprietary or replication requirements cannot be met

## 6. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote — set to **Chicago author-date**; remember JOLE's
  in-text ordering convention is **chronological, then alphabetical within a year** (a, b disambiguation),
  with **"et al." for three or more authors** — not purely alphabetical
- Typesetting: LaTeX (TeX Live / MacTeX, Overleaf); JOLE accepts LaTeX with `.bib`/`.bst` rules and
  Biblatex/Biber (required directive line) — confirm current guidance
- Title page must carry **all co-authors' names, institutions, and emails** (single-blind review)

## 7. Process & portal
| Item | Note |
|------|------|
| Submission portal | Editorial Manager (`editorialmanager.com/jole`) |
| Submission fee | **$100 SOLE members / $175 non-members** (since July 1, 2018), non-refundable even on desk reject; decisions withheld until paid — live-check during upload |
| Society tie | Official journal of the **Society of Labor Economists (SOLE)**; membership lowers the fee |
| Review model | **Single-blind** (referees anonymous, authors named) |
| Replication deposit | Required for accepted empirical/simulation/experimental papers → JOLE Dataverse |
| Publisher | University of Chicago Press |

## 8. Cautions
1. **Live-check upload specifics** (portal banner, fee prompts, editor conflicts, deposit wording) on the
   official journal pages and upload screen.
2. **Do NOT anonymize** the manuscript — JOLE is single-blind; the title page names all authors and
   references are not blinded (the opposite of double-blind journals).
3. **Respect data licenses**; restricted data (FSRDC, registry data) require formal access and disclosure
   review — flag proprietary data to the editor at submission.
4. **Match estimator to design** — plain TWFE on staggered timing and uncorrected AKM limited-mobility
   bias are known labor pitfalls.
5. **Mind the word economy** — the ~20,000-word soft cap counts each full-page exhibit as 500 words.
