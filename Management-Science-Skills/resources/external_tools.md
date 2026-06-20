# Management-Science Tools & Resources

This document lists external data sources, modeling/analysis software, and writing tools
commonly used when preparing a manuscript for **Management Science** (INFORMS). Because
Management Science is deliberately **bimethodological** — rigorous analytical/quantitative
modeling *and* empirical work across accounting, finance, marketing, operations,
information systems, strategy, entrepreneurship, organizations, and behavioral economics —
the toolkit spans optimization/OR, stochastic modeling, econometrics, experiments, and
data science. Match the toolset to your **Department**. Always verify licensing terms and
current INFORMS/Management Science policies before using any resource.

## 1. Analytical / OR modeling (the formal-theory lane)

### Optimization & mathematical programming
| Tool | Note |
|------|------|
| Gurobi | Commercial LP/MIP/QP solver; academic license available |
| CPLEX (IBM) | LP/MIP/QP; academic access |
| Mosek | Conic / semidefinite programming |
| JuMP (Julia) | Algebraic modeling layer over many solvers |
| Pyomo / `cvxpy` (Python) | Modeling for optimization and convex programs |
| AMPL / GAMS | Algebraic modeling languages |

### Stochastic models, simulation & game theory
- **Symbolic / analytical:** Mathematica, Maple, SymPy — closed-form derivations, comparative statics, proofs.
- **Stochastic processes / queueing / MDPs:** custom code in Julia/Python/MATLAB; `QuantEcon` for dynamic programming.
- **Discrete-event / agent-based simulation:** SimPy, AnyLogic, Arena; common variance-reduction and CI reporting.
- **Equilibrium / mechanism design:** numerical fixed-point and best-response solvers; verify uniqueness/existence arguments.

> For Optimization and Decision Analytics, Stochastic Models and Simulation, and Operations
> Management submissions, the bar is a clean model, stated assumptions, proved results
> (propositions/theorems), and managerial insight that travels beyond the specific instance.

## 2. Empirical analysis software (the data lane)

### Econometrics / archival (finance, accounting, strategy, IS)
- **Stata**: `reghdfe` (high-dimensional FE), `ivreghdfe`/`ivreg2` (IV/2SLS), `did`/`csdid` (modern DiD), `xtreg`, `psmatch2`/`teffects`, cluster-robust SE.
- **R**: `fixest`, `plm`, `did`, `MatchIt`, `sandwich`; **Python**: `linearmodels`, `statsmodels`, `econml` (heterogeneous treatment effects).

### Behavioral / experimental (Behavioral Economics & Decision Analysis, Marketing, OB)
- Experiment platforms: **oTree**, **Qualtrics**, **Prolific**, **MTurk**, **CloudResearch**.
- Power & design: **G*Power**, R `pwr`/`simr`.
- Structural / choice models: `apollo` (R), `biogeme` (Python) for discrete-choice estimation.

### Data science / ML (Data Science department)
- Python `scikit-learn`, `PyTorch`, `xgboost`; R `tidymodels`; reproducible pipelines with held-out validation and honest out-of-sample reporting.

## 3. Reproducibility — Data and Code Disclosure (front-loaded, verified)

Management Science enforces a **Code and Data Disclosure Policy** (effective June 1, 2019;
revised April 20, 2026). Authors provide an **AsCollected project-page URL** at submission,
and accepted numerical/computational papers must provide data, programs, and details
sufficient to permit replication before production. Build for this from day one:

1. A single master script that regenerates **every** table/figure/proposition-illustration in the main text from raw inputs.
2. A README with exact software versions, seeds, run order, and expected runtime; pin solver/package versions.
3. For analytical papers: numerical code and notebooks that reproduce every figure and computed example; symbolic-derivation files where used.
4. A data-availability statement, sources, and access/confidentiality terms; a de-identified dataset and codebook where sharing is permitted.
5. Author-contribution disclosure and an AsCollected project page URL provided at submission.
6. For proprietary or sensitive data, a disclosure plan that preserves replicability while respecting access limits.

## 4. Reference & writing tools

| Tool | Note |
|------|------|
| LaTeX / Overleaf | Common for analytical papers; INFORMS provides article templates — verify the portal accepts your format |
| Zotero / EndNote / Mendeley | Configure to **author-year (name–date)** output, e.g., (Norman 1977) |
| BibTeX `informs` / journal style | Reconcile against the current Management Science style |
| Grammarly | Language polish |

Management Science uses **author-year in-text citations** with an alphabetical reference
list; configure your reference manager accordingly and reconcile against the current
submission guidelines.

## 5. Submission & process

- **Portal:** ScholarOne Manuscripts ("Manuscript Central") at **mc.manuscriptcentral.com/mnsc** (via INFORMS PubsOnline); seven-step upload workflow.
- **Fee:** USD $79 per original submission (effective Aug 1, 2025), with INFORMS-member and low-income-economy waivers and an honor-based no-justification waiver — verify current amount and mechanics.
- **Abstract ≤ 250 words; 3–5 keywords;** double-anonymized review — remove all identifiers and disclose any conference-proceedings version anonymously in the cover letter.
- **ORCID:** keep an ORCID linked to your account.

## 6. Verify before you rely

Department/area-editor routing, the submission fee and waivers, length limits for invited
revisions, the citation style, and the Data and Code Disclosure verification workflow change
over time. Always confirm the current requirements on the official Management Science
submission guidelines and Code and Data Disclosure Policy pages before submitting.
