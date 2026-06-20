# External Tools & Resources for AEJ: Macroeconomics

Data sources, software, and packages useful when preparing an *American Economic
Journal: Macroeconomics* (AEJ: Macro) submission. AEJ: Macro is the AEA's
broad-interest macro journal, so a typical paper combines a **substantive macro
question** with **quantitative discipline** — either an identified empirical
design (SVAR, local projections, narrative, high-frequency/proxy-VAR) or a
quantitative model (DSGE, HANK, structural estimation), and often both. Because
the **AEA Data Editor** runs a **pre-publication reproducibility check** that
covers simulation and model-solution code (not just data cleaning), build the
replication package as you go. Check licenses and current access terms before use;
verify volatile process specifics on the official AEA pages.

## 1. Data sources

### Macro time series & vintages
| Source | Provider | Typical use |
|--------|----------|-------------|
| FRED / ALFRED | St. Louis Fed | Macro time series; real-time (vintage) data via ALFRED |
| BEA / BLS | U.S. gov | NIPA, output, employment, prices |
| OECD / IMF (IFS, WEO) | OECD / IMF | Cross-country macro panels |
| Penn World Table | Groningen | Growth, cross-country income levels |
| Jordà–Schularick–Taylor Macrohistory DB | macrohistory.net | Long-run cross-country macro-finance |

### Shocks, surprises & narrative series
| Source | Provider | Typical use |
|--------|----------|-------------|
| High-frequency monetary surprises (e.g., Gürkaynak–Sack–Swanson-style, Nakamura–Steinsson) | published replication files | Monetary-shock identification |
| Romer–Romer narrative monetary/tax shocks | published replication files | Narrative identification |
| Auerbach–Gorodnichenko / Ramey defense-news fiscal shocks | published replication files | Fiscal-multiplier identification |

### Micro for macro & experiments (note AEA rules)
| Source | Provider | Typical use |
|--------|----------|-------------|
| IPUMS (CPS, ACS), PSID, SCF | Minnesota / Michigan / Fed | MPC distributions, HANK calibration targets, inequality |
| Compustat / CRSP (licensed) | WRDS | Firm dynamics, macro-finance |
| AEA RCT Registry | AEA | Pre-registration of field experiments (required) |

## 2. Statistical & computational software

### Quantitative-theoretical (DSGE / HANK / structural)
- **Dynare** (MATLAB/Octave): DSGE solution and Bayesian/likelihood estimation — record the Dynare version.
- **Julia**: `QuantEcon.jl`, `Optim.jl`, `ForwardDiff.jl`; sequence-space Jacobian / `SSJ`-style toolkits for HANK.
- **Python**: `numpy`/`scipy`, `numba`/`jax` for fast value-function iteration; `estimagic` (MSM/MLE); sequence-space-Jacobian toolkit for heterogeneous-agent models.
- **MATLAB**: CompEcon, custom global solvers; perturbation toolkits.
- Report the solver, perturbation order / grid, tolerances, starting values, and accuracy diagnostics (Euler errors).

### Identified-empirical macro (SVAR / LP / narrative)
- **Stata**: `var`/`svar`, `varbasic`, `lpirf` (local projections), `boottest`, `newey`; user packages for proxy-VAR / external-instrument SVAR.
- **R**: `vars`, `svars`, `lpirfs` (local projections), `sandwich`/`clubSandwich` (HAC/cluster), `BVAR`.
- **Python**: `statsmodels` (VAR), `local_projections`-style routines, `linearmodels`.
- For sign restrictions: report the full set and the identified-set / median-target, not a spurious point.

### Reproducibility tooling (build for the AEA Data Editor)
- Pin versions: `renv.lock` (R), `requirements.txt`/`conda env` (Python), `Project.toml`/`Manifest.toml` (Julia), recorded Stata `ssc`/`net` versions, **Dynare version**.
- One master script (`run_all`) regenerating every table and figure from raw data **including the model solution and simulation steps**.
- Set and report seeds for simulation / bootstrap / randomization.
- For long-running solves/simulations, ship cached intermediates and a reduced-scale switch; document full runtime (AEA encourages this).

## 3. Strategy toolkit by paper type

| Paper type | Core checks | Tools |
|------------|-------------|-------|
| Empirical shock-identification (SVAR / proxy-VAR) | ordering / sign set / instrument relevance & exogeneity; weak-IV-robust bands | Stata `svar`, R `svars`/`vars`, proxy-VAR code |
| Dynamic-effects (local projections) | lag length, controls, HAC inference; LP-IV first stage | `lpirf` (Stata), `lpirfs` (R) |
| Quantitative DSGE / HANK | calibration targets, parameter identification, solution accuracy, counterfactual validity | Dynare, `QuantEcon`, sequence-space Jacobian, `estimagic` |
| Structural estimation | moment↔parameter identification, sensitivity, Monte Carlo recovery | `estimagic`, SMM/MSM code |

## 4. Figures & tables (AEA house + macro conventions)
- **Impulse-response figures** with stated confidence bands, labeled horizon axes, and a zero line; sign-restricted responses shown as a set / median-target.
- **Model-fit overlays** (data vs. simulated moments; targeted + untargeted) for quantitative papers.
- Tables report the **macro quantity** (multiplier, peak response, welfare cost) with its SE/band; AEA tables conventionally use significance stars, but the SE/band must be present.
- Vector output (`.eps`/`.pdf`); legible after two-column AEA typesetting; no chartjunk.

## 5. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX. AEA applies its house style at copyediting; keep references complete and consistent.
- Typesetting: LaTeX (TeX Live / MacTeX / Overleaf); AEA provides a LaTeX template for accepted papers.

## 6. Process & portal (verify on the official AEA pages)
| Item | Note |
|------|------|
| Submission portal | AEA submission system (reached from the journal page); PDF |
| Review | Single-blind; editor/coeditor-managed; desk rejection possible |
| Submission fee | Scaled by AEA membership × country income tier; 50% refund if rejected without review (检索于 2026-06；以官网为准) |
| Publication fee | US$15 / typeset page at page proofs (post Feb 1, 2024; 检索于 2026-06；以官网为准) |
| Abstract | ≤100 words; JEL codes required |
| Length | ~40pp (11pt) / ~45pp (12pt), incl. figures/tables/refs/appendices |
| Replication deposit | AEA Data and Code Repository on openICPSR; AEA Data Editor check **before** publication; simulation/solver code included |
| Disclosure | Separate statement per coauthor; US$10,000 interested-party threshold |

## 7. Cautions
1. **Verify volatile specifics** (editors, fees, page charge, length guidance, policy dates) on the official AEA pages — they change.
2. **Reproducibility is checked before publication** — assemble data, code, **and simulation/solver code** early; document any restricted-data access path now.
3. **Respect data licenses**; for restricted data, request the exception, keep code public, and document the access path.
4. **Match diagnostics to the paper type** — identification diagnostics for empirical work; calibration/identification + solution accuracy for quantitative work; both for hybrids.
