# External Tools & Resources for AER: Insights

Data sources, software, and packages useful when preparing an *American Economic
Review: Insights* (AER: Insights) submission. AER: Insights publishes **short,
self-contained papers built around a single important idea** — empirical,
theoretical, or methodological — under a **hard length cap** (≤7,000 words minus
200 per exhibit, ≤5 exhibits) and a **fast, decisive review** (conditional accept
or reject, no traditional R&R). Because the **AEA Data Editor** runs a
**pre-publication reproducibility check**, build the replication package as you go.
Check licenses and current access terms before use; verify volatile process
specifics on the official AEA pages.

## 1. Data sources

### Public-use micro & macro
| Source | Provider | Typical use |
|--------|----------|-------------|
| IPUMS (CPS, ACS, USA, International) | University of Minnesota | Labor, demography, one clean cross-section/panel result |
| FRED / ALFRED | St. Louis Fed | Macro time series, real-time vintages |
| PSID / NLSY | U. Michigan / BLS | Life-cycle, dynamic single-fact papers |
| World Bank WDI / Microdata, LSMS | World Bank | Development, cross-country quantitative facts |
| Administrative / registry data (via agreements) | Various | The clean administrative-data fact AER: Insights favors |
| Compustat / CRSP (licensed) | WRDS | Firm/finance facts and quasi-experiments |

### Experimental & own-data
| Source | Provider | Typical use |
|--------|----------|-------------|
| AEA RCT Registry | AEA | Pre-registration of field experiments |
| AsPredicted | Wharton Credibility Lab | Pre-registration of lab/online studies |
| OSF Registries | Center for Open Science | Pre-registration + materials hosting |
| oTree / Qualtrics / Prolific | Various | Running lab-in-the-field, online experiments and surveys |

> A short experiment paper reports **one pre-registered primary estimand** in-text;
> additional arms and heterogeneity go to the Supplemental Appendix.

## 2. Statistical & computational software

### Empirical micro / econometrics (the most common AER: Insights paper)
- Stata: `reghdfe`, `ivreghdfe`, `csdid` / `did_multiplegt_dyn` (modern DiD),
  `rdrobust` / `rddensity` (RDD), `boottest` (wild-cluster), `eventstudyinteract`
- R: `fixest`, `did`, `rdrobust`, `sandwich` / `clubSandwich`
- Python: `linearmodels`, `statsmodels`, `doubleml` / `econml` (causal ML)

### Structural / theory (kept minimal for the short format)
- Python: `numpy`/`scipy`, `numba`/`jax`, `estimagic` (MSM/MLE), `QuantEcon`
- Julia: `Optim.jl`, `JuMP`, `QuantEcon.jl`; MATLAB: Dynare, CompEcon
- Report only the one identifying moment and one counterfactual in-text; estimation
  detail to the appendix

### Reproducibility tooling (build for the AEA Data Editor)
- Pin versions: `requirements.txt`/`conda` (Python), `renv.lock` (R),
  `Project.toml`/`Manifest.toml` (Julia), recorded Stata `ssc`/`net` versions
- One master script (`run_all`) regenerating **every** exhibit and in-text number
  (including Supplemental Appendix results — they are in scope)
- Set and report seeds for simulation / bootstrap / randomization inference
- AEA / Social Science Data Editors README template with an exhibit→code map

## 3. Strategy toolkit by paper type

| Paper type | Core checks (in-text minimum) | Tools |
|------------|-------------------------------|-------|
| Causal empirical | one design diagnostic in-text (pre-trends / density / first-stage / balance); robustness battery to appendix | `csdid`, `rdrobust`, `ivreghdfe`, `boottest` |
| Experiment | pre-registration; primary estimand; attrition bounds | AEA RCT Registry, `ritest`, OSF |
| Structural | one identifying moment + sensitivity in-text; recovery MC in appendix | `estimagic`, `QuantEcon`, SMM/MSM code |
| Theory | minimal model; one headline result + intuition in-text; proofs in appendix | LaTeX, symbolic checks |

## 4. Figures & tables (AER: Insights house rules)
- **≤5 exhibits, each ≤1 page**; each exhibit costs 200 words of the main-text budget.
- **No asterisks or boldface** for significance — report standard errors / confidence
  sets in the cell or note (AEA-wide convention).
- Lean **visual**: event-study plots, RD plots, treatment-effect figures that are
  self-reading; avoid dense multi-panel tables.

## 5. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX. AEA house (author-date) style; the
  reference list is excluded from the word count, but keep it tight and complete.
- Typesetting: LaTeX (TeX Live / MacTeX / Overleaf). Follow AEA first-page metadata
  rules for single-blind review.

## 6. Process & portal (verify on the official AEA pages)
| Item | Note |
|------|------|
| Submission portal | AEA online submission system; PDF main text + Supplemental Appendix |
| Length gate | ≤7,000 − 200×(#exhibits) words; ≤5 exhibits, each ≤1 page; over → returned unreviewed |
| Abstract | ≤100 words |
| Review model | Conditional accept or reject; **no traditional R&R**; ~8-week conditional window, usually no second referee round |
| Fees | Submission fee by membership × income band; publication fee ~US$15/typeset page (re-confirm) |
| Replication | AEA Data and Code Availability Policy; AEA Data Editor pre-publication check; openICPSR deposit |
| Editor | Matthew Gentzkow (since Jan 2024); founding editor Amy Finkelstein |

## 7. Cautions
1. **The cap is a gate, not a guideline** — reconcile words and exhibits before
   submitting; an over-cap paper is returned unreviewed.
2. **There is no R&R** — pre-empt the decisive objections before submission.
3. **Reproducibility is checked before publication** — assemble the package early;
   appendix results are in scope.
4. **One insight only** — secondary results belong in the Supplemental Appendix or a
   different paper.
5. **Verify volatile specifics** (editor, fees, page charge) on the official AEA pages.
