# Operations-Management Tools & Resources (M&SOM)

This document lists modeling environments, solvers, data sources, and writing tools
commonly used when preparing a **Manufacturing & Service Operations Management
(M&SOM)** manuscript. M&SOM publishes both **analytical/stochastic OM modeling**
(optimization, queueing, stochastic models, game theory, revenue management) and
**rigorous empirical OM / data-driven analytics**, so the toolkit spans both
traditions. The non-negotiable common thread: an **operations decision/problem must be
central** to the contribution. Check INFORMS/M&SOM policies and license terms before
using any resource.

## 1. Analytical / Optimization Modeling

### Algebraic modeling languages & solvers
| Tool | Provider | Typical use |
|------|----------|-------------|
| Gurobi | Gurobi Optimization | LP / MILP / QP / MIQP, large-scale OM models |
| CPLEX | IBM | LP / MILP / QP, classic OR workhorse |
| MOSEK | MOSEK | Conic / SOCP / SDP (robust & distributionally robust OM) |
| AMPL / GAMS / Pyomo / JuMP | AMPL, GAMS, COIN-OR, Julia | Model formulation, decomposition, callbacks |
| SCIP / HiGHS | ZIB / open source | Open MILP, academic licensing |

### Stochastic, queueing & dynamic models
- **Dynamic programming / MDPs**: value/policy iteration, approximate DP (ADP), reinforcement learning for sequential operations decisions.
- **Queueing analysis**: M/M/c, M/G/1, Jackson/BCMP networks, heavy-traffic / diffusion approximations for service-system staffing and congestion.
- **Stochastic programming**: two-stage and multistage with recourse (SDDP), sample-average approximation (SAA); chance constraints.
- **Robust & distributionally robust optimization (RO/DRO)**: ambiguity sets, Wasserstein DRO for inventory/pricing under uncertainty.
- **Game theory / mechanism design**: equilibrium computation for supply-chain contracting, platforms, and competition.

### Simulation
- **Discrete-event simulation**: Arena, AnyLogic, Simio, SimPy (Python) — service systems, supply-chain, manufacturing flow.
- **Monte Carlo**: policy evaluation, revenue-management simulation, validating analytical approximations.

## 2. Empirical OM & Data-Driven Analytics

### Econometrics / causal inference
- **Stata**: `reghdfe` (high-dimensional FE), `ivreg2`/`ivreghdfe` (IV/2SLS), `csdid`/`did` (modern DiD), `rdrobust` (RDD), `teffects`/`psmatch2` (matching).
- **R**: `fixest`, `did`, `rdrobust`, `MatchIt`, `sandwich` (clustered SE).
- **Python**: `statsmodels`, `linearmodels`, `econml`/`dowhy` (causal ML).
- Field experiments / A-B tests with operational partners; structural estimation of operational models (e.g., dynamic discrete choice, EM for demand under censoring).

### Prescriptive analytics / data-driven OM
- **Python**: `scikit-learn`, `PyTorch`/`TensorFlow`, `cvxpy` (convex optimization), contextual/prescriptive optimization, SAA from data.
- Demand forecasting, newsvendor-with-ML, learning-and-earning / bandit pricing, inventory analytics.

### OM-relevant data sources
| Source | Use |
|--------|-----|
| Compustat / CRSP / WRDS | Firm financials, inventory turns, performance (licensed) |
| FactSet / Bloomberg | Supply-chain links, transactions |
| Census / economic microdata | Plants, establishments, production |
| Platform / firm partnerships | Transaction-level ops data (ride-hailing, retail, healthcare, e-commerce) |
| Hospital / healthcare datasets (e.g., HCUP) | Service operations, congestion, scheduling |
| Customs / shipment records | Global supply-chain flows |

> Per the M&SOM data & code disclosure policy, **licensed data** (Census, Compustat, CRSP, FactSet, WRDS) requires you to provide **your own code plus detailed access/linking instructions** so others can replicate — you need not redistribute the licensed data itself.

## 3. Reference & Writing Tools

| Tool | Note |
|------|------|
| LaTeX / Overleaf | Use the **official M&SOM LaTeX style files**; the 32-page cap is measured on them |
| Word (M&SOM template) | Official Word style file alternative |
| EndNote | INFORMS author-year style file (v1.6) available |
| Zotero / Mendeley | Configure to INFORMS author-year output and reconcile against the style file |

The page count is **typeset against the official template** (one column, 11-pt, 1-inch margins) and **includes references, tables, figures, and appendices** — draft in the template from the start, not at the end.

## 4. Submission & Process

- **Submission portal**: ScholarOne Manuscripts at `mc.manuscriptcentral.com/msom` — single PDF.
- **Department routing**: you choose a primary editorial Department and name **2 preferred Department Editors**; respect the Manufacturing-and-Supply-Chain first/second-choice rule.
- **Double-anonymous**: remove all author names, affiliations, and acknowledgments from the manuscript PDF.
- **Structured abstract**: ≤ 300 words with Problem definition / Methodology-results / Managerial implications.

## 5. Reproducibility & Transparency

1. Keep clean, commented model/analysis code (solver scripts, simulation seeds, do-files, notebooks) that regenerates every result, table, and figure.
2. For analytical papers: provide proofs in the online supplement (≤ 16 pages) and numerical-study code; document parameter ranges and instance generation.
3. For empirical papers: document sample construction, exclusions, and identification; be prepared to share raw data for editorial verification and to **retain it** after publication.
4. For licensed data: ship your code plus access/linking instructions; cite and acknowledge any reused shared data/code.
5. Verify all license and confidentiality terms before depositing or sharing.

## 6. Verify Before You Rely

Editorial team, department rosters, submission links, the page/abstract limits, fees,
and data/code policies change over time. Confirm current requirements on the official
M&SOM submission-guidelines page and the INFORMS style files before submitting.
