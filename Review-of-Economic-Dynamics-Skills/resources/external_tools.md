# External Tools — Quantitative & Dynamic Economics (RED-oriented)

A short, working list of tools and data sources that fit the Review of Economic Dynamics (RED)
house style: dynamic general-equilibrium models, business cycles, growth, labor, monetary/fiscal
policy, and international macro studied through theoretical, computational, or empirical dynamic
models. Choose tools that produce a clean, runnable replication archive — RED's
**Availability of Data and Computer Code** policy treats code as a first-class, citable object
(posted on the RED site and indexed as a RePEc "Computer Codes" series).

## Solving & estimating dynamic models

- **Dynare** (MATLAB / Octave) — perturbation and global solution of DSGE models, Bayesian and
  classical estimation, stochastic simulation, IRFs. The de facto standard for RED-style
  quantitative macro; archives reproduce cleanly when the `.mod` files and a master script are included.
- **Julia macro stack** — `SolveDSGE.jl`, `QuantEcon.jl`, `DifferentialEquations.jl`, and the
  Federal Reserve Bank of NY `DSGE.jl` for estimation. Strong for heterogeneous-agent and
  high-dimensional global solutions.
- **Sequence-Space Jacobian (SSJ)** toolkit (Python) — fast solution of heterogeneous-agent
  (HANK / Aiyagari / Krusell–Smith-type) models; pairs well with RED's computational scope.
- **Heterogeneous-agent solvers** — endogenous grid method (EGM), Krusell–Smith, and continuous-time
  (HACT / "Achdou–Han–Lasry–Lions–Moll") finite-difference codes for distributional dynamics.
- **CompEcon / Miranda–Fackler** routines — projection, collocation, and function approximation
  for global methods.

## Numerical computing & reproducibility

- **MATLAB / GNU Octave**, **Julia**, **Python (NumPy/SciPy/Numba)**, **Fortran/C** for hot loops.
- **Random-seed discipline** — fix and record seeds; RED's `readme.txt` explicitly asks for them.
- **Environment capture** — record software/OS versions, package versions (`Project.toml`/`Manifest.toml`,
  `requirements.txt`, `renv.lock`), and expected runtime; the RED readme requires execution order and
  expected computation time.
- **Open-standard archives** — package the archive as `.zip`, `.gz`, or `.gzip` (the formats the RED
  data/code editor accepts) with a master "run-all" script.
- **Repository/data-statement layer** — prepare repository DOI/links and data/software citations for
  Elsevier Option C, or draft the data-availability statement explaining why sharing is limited.

## Empirical / time-series & calibration data

- **FRED** (St. Louis Fed) — national accounts, labor, prices, rates for calibration and moment-matching.
- **OECD**, **IMF (IFS / WEO)**, **World Bank (WDI)**, **Penn World Table** — cross-country growth and
  international-macro panels.
- **BLS / BEA / Census** — micro and sectoral US series; **CPS / PSID / SCF** for labor and wealth
  distributions feeding heterogeneous-agent models.
- **Econometrics** — `R` (`vars`, `urca`, `dynlm`), `Stata`, and Python `statsmodels` for VARs,
  local projections, and structural estimation when the paper has an empirical component.

## Writing & submission

- **LaTeX** via Elsevier's `elsarticle` class (RED accepts LaTeX; initial formatting is "your paper your way").
- **BibTeX/biblatex** in **author-year (Harvard)** style to match RED's reference system.
- **SSRN** — RED offers free preprint posting during submission (public once past desk screen).

See [`official-source-map.md`](official-source-map.md) for the official URLs behind every RED-specific fact.
