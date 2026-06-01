# External Tools & Resources for Econometric Theory (ET) Submissions

Tools useful when preparing an *Econometric Theory* (ET) manuscript — a theorem-proof contribution
to the mathematical and statistical foundations of econometrics (asymptotic theory,
probability-theoretic methods, time series and nonstationarity, high-dimensional and non-standard
environments), typically with supporting lemmas, derivations, and (often) a Monte Carlo or
numerical illustration. Verify current licenses and the journal's live author instructions before
use; volatile specifics are flagged in `official-source-map.md`.

## 1. Typesetting and the theorem-proof environment

ET is theorem-proof first; the bottleneck is usually clean mathematical exposition, not data.

- **LaTeX** (TeX Live / MacTeX / Overleaf) — the default. ET accepts a single embedded-font PDF at
  submission; keep a clean LaTeX source for the post-acceptance stage.
- **amsmath / amsthm / mathtools** — numbered `theorem` / `lemma` / `proposition` / `corollary` /
  `assumption` environments; a consistent `\qedhere`-terminated `proof` environment.
- **cleveref** — stable cross-references to Assumption/Theorem/Lemma numbers (essential when long
  proofs move to the online Supplement and must still reference the main text correctly).
- **APA author-date references** — ET follows the APA Style Guide. Use `apacite` + `apalike`,
  `biblatex-apa` (with `biber`), or `natbib` configured for author-date. Set your reference manager
  (Zotero, BibTeX/BibLaTeX, EndNote) to APA, not numeric or Chicago.
- **Figure formats** — export to TIFF (line art >=600 dpi, greyscale >=300 dpi), EPS (fonts
  embedded), or PDF, legible at 50% reduction.

## 2. Symbolic and asymptotic derivation aids

| Tool | Typical use in ET-style work |
|------|------------------------------|
| Mathematica / SymPy | Symbolic expansions, characteristic functions, moment algebra, Edgeworth terms |
| SageMath / Maxima | Open-source symbolic algebra for closed-form variance/limit derivations |
| Matrix-calculus references | Clean derivation of asymptotic-variance and influence-function expressions |

These check algebra; they do not replace a rigorous proof. State every regularity condition.

## 3. Probabilistic / asymptotic toolkit (for the proofs themselves)

| Ingredient | Where it shows up | Standard references to cite (APA) |
|------------|-------------------|-----------------------------------|
| LLN / CLT, triangular-array CLTs | Consistency, asymptotic normality | White; Davidson |
| Functional CLT / weak convergence | Nonstationary / unit-root / FCLT limits | Phillips; Billingsley |
| Empirical-process theory | Uniform convergence, semiparametrics | van der Vaart & Wellner |
| Mixing / near-epoch dependence | Dependent-data limit theory | Davidson |
| Concentration inequalities | High-dimensional / many-regressor regimes | Boole/Bernstein-type results |
| Stochastic integrals, BM functionals | Nonstationarity, cointegration limits | Phillips & Durlauf |

Match the limit theory to the data environment (stationary vs nonstationary, fixed vs growing
dimension); ET referees are unforgiving about regularity conditions and edge cases.

## 4. Monte Carlo / numerical illustration

ET papers often include simulations showing finite-sample behavior tracks the asymptotics.

- **R** — `MASS`, `mvtnorm` (data generation); `boot`; `Matrix`; `RcppArmadillo` for speed.
- **MATLAB / Julia** — common for time-series and high-dimensional simulation; Julia (`Distributions`,
  `LinearAlgebra`) for fast, reproducible experiments.
- **Python** — `numpy`, `scipy.stats`, `statsmodels` for finite-sample size/power studies.
- **Reproducibility** — fix and report random seeds; report the number of Monte Carlo replications,
  sample sizes, and the data-generating process precisely enough to reproduce every table/figure.

## 5. Supplementary Material (ET-specific)

ET routinely moves long technical proofs/derivations to **online Supplementary Material** rather
than cutting them. That material must be **already reviewed**, submitted as a **separate clearly
labeled file** with the final manuscript, is **not copyedited/typeset**, and **may not introduce
new unseen results**. Build it as a self-contained LaTeX file that compiles independently but shares
assumption/notation conventions with the main paper.

## 6. Cautions

1. **Verify volatile specifics** (editors, fee/APC, portal URL, exact length/abstract caps) on the
   live ET author-instructions pages — ET changed editors and switched to ScholarOne in Jan 2026.
2. **Respect the 50-page ceiling** on Regular Articles; overflow belongs in the non-copyedited
   online Supplement, never new results.
3. **State every assumption**; an unproven regularity condition is the most common ET referee
   objection.
4. **APA author-date** references — not numeric, not Chicago.
5. **There is no mandatory data/code archive** at ET (theory journal); a reproducible numerical
   appendix is good practice, not a formal deposit requirement (see `official-source-map.md`).
