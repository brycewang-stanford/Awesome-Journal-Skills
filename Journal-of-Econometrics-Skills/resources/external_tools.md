# External Tools & Resources for Journal-of-Econometrics-Style Methodology

Software, libraries, and references useful when preparing a *Journal of Econometrics* (JoE)
submission — a **methodological** paper whose core is a new estimator, test, identification result,
or asymptotic theory, supported by **Monte Carlo evidence** and (often) an **empirical
illustration**. The center of gravity is the proof and the simulation, not a single applied finding.
Verify current licenses and terms before use.

## 1. Symbolic / analytical and proof support
- **Symbolic algebra:** Mathematica, SymPy (Python), Maxima — derive influence functions,
  asymptotic variances, expansions, and bias terms; check algebra in long derivations.
- **LaTeX + `amsmath` / `amsthm`:** theorem-and-proof environments; the journal uses the Elsevier
  **`elsarticle`** document class. `mathtools`, `bm` for clean estimator notation.
- **Numerical verification of analytic results:** confirm a derived asymptotic variance against a
  high-replication Monte Carlo before claiming it; mismatch usually signals an algebra slip.

## 2. Monte Carlo & simulation
| Tool | Typical use |
|------|-------------|
| R (`Rcpp`, `RcppArmadillo`, `future`/`parallel`) | Fast, parallel DGP loops; size/power tables |
| MATLAB | Common in econometric theory; matrix-native estimator prototyping |
| Python (`numpy`, `numba`, `joblib`) | Vectorized/JIT simulation, embarrassingly parallel designs |
| Julia | High-performance simulation when inner loops dominate |
| Stata (`simulate`, `postfile`) | Simulation when the estimator ships as an ado-command |

Design discipline: report **empirical size at nominal 5%/10%**, **size-adjusted power**, and
sensitivity across **sample sizes, DGPs, error distributions, and tuning parameters (bandwidth,
lag length, penalty)**. Fix and report seeds; report replication count and Monte Carlo standard
errors.

## 3. Estimation / inference building blocks
- **GMM / M-estimation:** `gmm` (R), `linearmodels`/`statsmodels` (Python), `gmm` (Stata) — sandwich
  variance, two-step and CUE.
- **HAC / cluster-robust / bootstrap:** `sandwich`, `clubSandwich`, `boot`, `fwildclusterboot` (R);
  `boottest` (Stata); long-run-variance / kernel-HAC estimators.
- **High-dimensional / regularized:** `glmnet`, `hdm` (R), `doubleml`, `econml` (Python) for
  double/debiased ML, post-selection inference, Neyman-orthogonal moments.
- **Nonparametric / semiparametric:** `np` (R), local-polynomial and series estimators, `rdrobust`
  for sharp local methods used as building blocks.
- **Time series / panel:** `vars`, `urca`, `dynlm` (R); unit-root, cointegration, factor and
  long-memory toolkits relevant to JoE's time-series tradition.

## 4. Reproducible computation (methodology норм)
- Pin versions: `renv.lock` (R), `requirements.txt` / `conda` env (Python), recorded `ssc`/`net`
  versions (Stata), `Project.toml`/`Manifest.toml` (Julia).
- One master script (`run_all`) that regenerates **every theorem-illustrating figure, every Monte
  Carlo table, and the empirical illustration** from raw inputs.
- Record seeds, replication counts, and hardware/runtime for heavy simulations.
- Package a new estimator as a reusable command/function with a minimal worked example, so referees
  can run it.

## 5. Data citation & availability (Elsevier policy)
- Cite underlying/relevant datasets in the text **and** in the reference list, tagged **`[dataset]`**
  with author(s), title, repository, version, year, and persistent identifier (DOI).
- A **data availability statement** is supported. JoE does **not** (as of access date) operate a
  single mandatory central code/data archive comparable to the JAE Data Archive or Econometric
  Society replication packages — replication materials for applied illustrations are **encouraged**
  rather than universally mandated.
- Optional **Data in Brief / MethodsX** co-submission exists via Editorial Manager.

## 6. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote, Mendeley — any CSL-compatible manager can
  produce the **Elsevier** numbered or author-year style.
- Typesetting: LaTeX (TeX Live / MacTeX, Overleaf) with **`elsarticle`**; initial submission is a
  single **PDF** (structured formatting is enforced at revision/acceptance).

## 7. Process & portal
| Item | Note (re-verify on official pages — see official-source-map.md) |
|------|------|
| Author-submission portal | Current official pages split guidance: ScienceDirect/new-submission link points to **Editorial Manager**; JoE Google Sites and the EE page remain relevant for **Editorial Express** resubmission/track flows. |
| Submission fee | **USD $75** nonrefundable (new + resubmissions > 1 yr); VAT for EU authors; no student discounts/refunds. |
| Format at submission | ScienceDirect route asks for editable source files; Editorial Express resubmission flow asks for **PDF only**, ~40 pages, ≥1.5 spacing, 11pt. |
| Abstract | ≤ **250 words**; concise and factual. |
| Review model | **Single anonymized**; ≥2 referees after editor screen. |
| Tracks | **Regular / Annals / Themed** Issues. |
| Publisher | **Elsevier**. |

## 8. Cautions
1. **Verify volatile specifics** (portal routing, editors, open themed calls) on the official
   journal pages before submission.
2. **Match the Monte Carlo to the theory** — a theorem with no finite-sample evidence, or
   simulations that never stress the assumptions, is the most common methodological weakness.
3. **State and check every regularity condition** — referees will probe whether they are primitive,
   verifiable, and not silently assuming the conclusion.
4. **Reproducibility is expected** — build the estimator command and the `run_all` pipeline as you
   go, not at the end.
