# External Tools & Resources for JME-Style Monetary & Macro Research

Data sources, software, and packages useful when preparing a *Journal of Monetary
Economics* (JME) submission — monetary theory and policy, central banking, business
cycles, growth, financial intermediation, fiscal interactions, and expectations, in both
theoretical/quantitative (DSGE) and empirical/applied-policy modes. JME enforces a strict
**40-page / ≤10 tables-and-figures** cap on accepted papers (online supplements exempt) and
a **ScienceDirect / Mendeley Data** supplementary-materials deposit policy, so build the
appendix and replication package as online supplements from the start. Check licenses and
current access terms before use.

## 1. Macro & monetary data sources

### US macro, money, and policy
| Source | Provider | Typical use |
|--------|----------|-------------|
| FRED / ALFRED | Federal Reserve Bank of St. Louis | Macro aggregates, real-time vintages, rates |
| FOMC statements, minutes, SEP, transcripts | Federal Reserve Board | Narrative shocks, communication, forward guidance |
| Fed funds / OIS / Eurodollar futures | CME / Bloomberg / Refinitiv | High-frequency monetary-policy surprises |
| Treasury yield curve (GSW) | Federal Reserve Board | Term structure, term premia, expectations |
| Flow of Funds (Z.1) / Financial Accounts | Federal Reserve Board | Intermediation, leverage, credit |
| Greenbook / Tealbook forecasts | Philadelphia Fed (real-time data set) | Information effect, forecast errors |

### International & cross-country
| Source | Provider | Typical use |
|--------|----------|-------------|
| BIS statistics (credit, policy rates, FX) | Bank for International Settlements | Cross-country credit, global financial cycle |
| ECB Statistical Data Warehouse | European Central Bank | Euro-area policy, monetary aggregates |
| IMF IFS / WEO | International Monetary Fund | Cross-country macro, inflation, exchange rates |
| OECD.Stat | OECD | Comparable macro and labor aggregates |
| Jordà–Schularick–Taylor Macrohistory DB | Authors / public | Long-run credit, money, and crises panels |

### Micro-to-macro and expectations
| Source | Provider | Typical use |
|--------|----------|-------------|
| Survey of Professional Forecasters | Philadelphia Fed | Inflation/output expectations, disagreement |
| Michigan Survey / NY Fed SCE | U. Michigan / NY Fed | Household inflation expectations |
| Compustat / CRSP | WRDS | Firm-level investment, financial frictions |
| Bank call reports / supervisory data | FFIEC / Fed | Bank lending, the credit channel |

## 2. Software for quantitative macro (DSGE) and computation

- **Dynare** (MATLAB/Octave) — log-linear and nonlinear DSGE solution, Bayesian estimation, IRFs, forecast-error variance decompositions; the field default for JME-style structural macro.
- **MATLAB** — global/perturbation methods, value-function iteration, Sims' `gensys`, occasionally-binding constraints (OccBin), heterogeneous-agent (HANK) toolkits.
- **Julia** — `DynareJulia`, `SolveDSGE.jl`, `QuantEcon.jl`, `DifferentiableStateSpaceModels.jl`; fast for large HANK / continuous-time (Achdou–Han–Lasry–Lions–Moll) models.
- **Python** — `quantecon`, `sequence-jacobian` (Auclert et al. SSJ for HANK), `numba`/`jax` for speed.
- **R / Stata** — for the empirical companion (VARs, local projections); see below.

## 3. Empirical macro toolkit by design

| Design | Core checks | Packages / tools |
|--------|-------------|------------------|
| High-frequency monetary surprises | Tight event window around FOMC; control for the Fed "information effect" (Romer–Romer / Nakamura–Steinsson / Miranda-Agrippino–Ricco) | Custom event-study; intraday futures data |
| Narrative monetary shocks | Romer–Romer narrative measure; orthogonalize to Greenbook forecasts | Published shock series; replication archives |
| SVAR / proxy-SVAR (external instruments) | Identification (recursive, sign, long-run, IV/proxy); IRF bands; lag selection | Stata `var`/`svar`, R `vars`/`svars`, `VARsignR`, MATLAB VAR toolboxes |
| Local projections (Jordà) | LP vs. VAR comparison; lag-augmentation; LP-IV; HAC/Newey–West or cluster SEs | Stata `lpirf`/`xtlpirf`, R `lpirfs`, `localprojections` |
| Sign/narrative-restricted VARs | Robustness to restriction set; prior sensitivity | `VARsignR`, BVAR routines |
| DSGE estimation | Prior/posterior plots, identification (Iskrev), MCMC convergence, posterior predictive | Dynare Bayesian estimation |

## 4. Identification staples in monetary economics

- **High-frequency identification:** monetary surprises from a narrow window around FOMC announcements; separate the pure policy shock from the information/forward-guidance component.
- **Narrative identification:** Romer–Romer-style records of policy intent; narrative fiscal shocks (military news, tax changes).
- **External instruments / proxy SVARs:** use the surprise series as an instrument for the policy rate inside a VAR.
- **Sign and long-run restrictions:** theory-consistent restrictions when timing/IV are unavailable.
- **Quantitative (model-based) identification:** discipline structural parameters with micro moments and matched second moments; report identification diagnostics.

## 5. Figures & exhibits (mind the 10 tables-and-figures cap)

- Impulse-response plots with confidence/credible bands; FEVD bar charts; IRF comparisons (VAR vs. LP).
- Keep the **combined count of tables and figures at or below 10** in the main text; push extra exhibits, derivations, and robustness to the **online supplementary appendix** (exempt from the page cap).
- Vector output (PDF/EPS) for print resolution; consistent shock units (e.g., a 100-bp or one-standard-deviation policy shock) labeled on every IRF.

## 6. Reproducibility & the JME data policy

- Deposit appendices, computer programs, and data files on **ScienceDirect** (Mendeley Data supported) — JME strongly advises this and an editor **may require** data/code as a condition of publication.
- Pin software and package versions (record Dynare/MATLAB/Julia versions, `renv.lock`, `requirements.txt`, `ssc`/`net` versions).
- One master script (`run_all`) regenerating every table, figure, and IRF from raw data and model code; set and report seeds for MCMC, bootstrap, and simulation.
- Include the **declaration of any use of generative AI** in manuscript preparation, per Elsevier policy.

## 7. Process & portal
| Item | Note |
|------|------|
| Submission portal | Elsevier **Editorial Manager** at `editorialmanager.com/monec/` |
| Submission fee | **US$350** (US$200 full-time PhD students), paid up front; **no fee** on resubmission; half refunded on direct return |
| Review model | **Single anonymized** (single-blind); typically ≥ 2 reviewers; **"up or out"** on first revision |
| Length cap | **40 pages** text/refs/footnotes; **≤ 10** tables and figures combined (online supplements exempt) |
| Replication deposit | Supplementary materials on ScienceDirect / Mendeley Data; editor may require as a condition of publication |
| Publisher | **Elsevier** |

## 8. Cautions
1. **Verify volatile specifics** (fee, editors, page cap, portal URL, AI-declaration wording) on the official JME / Elsevier page — they change. See `official-source-map.md` for what is verified vs. **待核实**.
2. **Separate the policy shock from the information effect** — a raw high-frequency surprise that moves expectations is a known pitfall.
3. **Match the IRF method to the question** — VAR vs. local projections trade bias for variance; show both when feasible.
4. **Respect the length cap early** — design the main text for 40 pages and ≤ 10 exhibits, with everything else as an online supplement, rather than cutting at the end.
