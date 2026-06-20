# External Tools & Resources for JPAM-Style Policy Analysis

Data sources, software, and packages useful when preparing a *Journal of Policy Analysis and Management*
(JPAM) submission. JPAM publishes **credibly identified evaluations of policies and programs** across the
policy fields, with a premium on **cost-benefit and distributional** analysis and clear policy
implications. Match tools to your field and design. Check licenses and current access terms before use,
and verify any JPAM-specific policy in [`official-source-map.md`](official-source-map.md).

## 1. Policy-evaluation data sources by field

### Labor, welfare & income
| Source | Provider | Typical use |
|--------|----------|-------------|
| Current Population Survey (CPS / ASEC) | Census/BLS (IPUMS) | Employment, earnings, transfer receipt |
| SIPP | U.S. Census Bureau | Program participation dynamics, take-up |
| PSID | Michigan | Long-run income, intergenerational mobility |
| State UI / TANF / SNAP administrative records | State agencies | Program evaluation (often restricted) |

### Education
| Source | Provider | Typical use |
|--------|----------|-------------|
| NCES (CCD, IPEDS, ECLS, NELS/HSLS) | U.S. Dept. of Education | Schools, enrollment, attainment |
| State longitudinal data systems (SLDS) | State education agencies | Student-level evaluation (restricted) |
| Stanford Education Data Archive (SEDA) | Stanford | District-level achievement |

### Health
| Source | Provider | Typical use |
|--------|----------|-------------|
| NHIS / MEPS / BRFSS | CDC/AHRQ | Coverage, utilization, health behavior |
| Medicaid/Medicare claims (CMS), HCUP | CMS / AHRQ | Insurance-policy evaluation (restricted) |
| Natality / mortality files | CDC NCHS | Birth/infant outcomes, minimum-wage & policy effects |

### Crime, housing, environment & immigration
| Source | Provider | Typical use |
|--------|----------|-------------|
| UCR / NIBRS, BJS, NCVS | FBI / BJS | Crime and justice policy |
| HUD PIC/TRACS, AHS | HUD / Census | Housing assistance and quality |
| EPA AQS, ECHO; EIA | EPA / EIA | Environmental & energy policy |
| ACS, DHS Yearbook, New Immigrant Survey | Census / DHS | Immigration policy |

## 2. Software by method

### R
- Causal inference: `fixest`, `did` (Callaway–Sant'Anna), `didimputation`, `rdrobust`, `rddensity`,
  `MatchIt`, `WeightIt`, `estimatr`, `Synth`/`tidysynth`/`augsynth` (synthetic control), `sensemakr`
- Reproducibility: `renv` (pin versions), `targets` (pipelines)

### Stata
- `reghdfe`, `csdid`, `did_multiplegt_dyn`, `eventstudyinteract`, `rdrobust`, `rddensity`,
  `ivreg2`/`ivreghdfe`, `weakivtest`, `boottest` (wild-cluster bootstrap), `synth`/`synth_runner`, `coefplot`

### Python
- `pandas`, `numpy`, `statsmodels`, `linearmodels`, `doubleml` / `econml` (DML, heterogeneous effects),
  `differences` (modern DiD); `matplotlib` / `seaborn` for exhibits; pin with `requirements.txt`

## 3. Cost-benefit & distributional analysis (JPAM premium)
- **Marginal Value of Public Funds (MVPF):** the Policy Impacts library / welfare-analysis toolkits;
  follow the perspective and discount-rate conventions in the cost-benefit literature
- **Benefit-cost analysis:** OMB Circular A-4 (discounting, sensitivity), agency BCA guidance
- **Distributional incidence:** decompositions by income/race/region; tax-transfer microsimulation
  (e.g., TAXSIM for federal/state tax-benefit calculations)

## 4. Preregistration & transparency
- Preregistration / pre-analysis plans: **OSF Registries**, AEA RCT Registry (for field experiments)
- Replication repositories: **openICPSR**, **Harvard Dataverse**, **OSF** (persistent identifiers);
  confirm the journal's designated/recommended repository on the author page
- Restricted-data workflow: document the data-request process; share code + synthetic/derived data
  (see [`../skills/jpam-transparency-and-data/SKILL.md`](../skills/jpam-transparency-and-data/SKILL.md))

## 5. Figures & references
- Coefficient/forest plots (`coefplot`, `ggplot2`/`broom`), event-study and RD plots, marginal-effects
  plots (`marginaleffects`); colorblind-safe palettes; vector output (PDF/EPS) for print
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote — format to the current Wiley/APPAM house style
- Prepare a **double-blind** manuscript (no identifying metadata, no obvious self-references) + a
  separate title page; corresponding-author ORCID

## 6. Process & portal
| Item | Note |
|------|------|
| Submission portal | **Wiley Authors / Research Exchange** — verify the live prompts before upload |
| Owner / publisher | **APPAM** / **Wiley** |
| Review model | **Double-blind/anonymized preflight** — anonymize the manuscript and keep a separate title page ready |
| Article types | Feature Research · Methods for Policy Analysis · Policy Retrospective (peer-reviewed) · Point/Counterpoint · Policy Insights (invited, not reviewed) · Book Reviews |
| Fee / membership | Free for APPAM members; non-members **USD 100 professional / USD 40 student**; no resubmission fee; waivers available |
| Data policy | Prepare a data-availability statement plus archived code/data in a persistent repository; Research Exchange governs exact prompts |

## 7. Cautions
1. **Verify volatile specifics** (editor/team, exact caps, accepted types, data-policy wording,
   portal prompts) on the official Wiley/APPAM pages and in Research Exchange.
2. **Anonymize properly** — JPAM is double-blind; strip metadata and obvious self-references.
3. **Plan for restricted data** — policy evaluations often use administrative microdata; document an
   access path and provide runnable code on synthetic data.
4. **Do the cost-benefit and distributional work** — it is what distinguishes a JPAM analysis from a
   field-economics paper.
5. **Calibrate the implication** — recommend only within what the design and cost-benefit support.
