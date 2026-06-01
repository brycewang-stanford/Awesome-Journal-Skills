# OR/MS Methodology Tools & Resources (Operations Research)

This document lists modeling languages, solvers, simulation and stochastic-modeling
software, and writing/reproducibility tools commonly used when preparing a
methodology-driven manuscript for **Operations Research (OR)**, the flagship
journal of INFORMS. OR prizes mathematically rigorous OR/MS contributions —
optimization, stochastic/probabilistic models, simulation, decision analysis — with
provable results (theorems and proofs) alongside data-driven and applied work.
The toolkit therefore spans mathematical modeling, computation, and reproducibility.
Always verify licensing terms and the current OR/INFORMS policies before using any
resource.

## 1. Modeling Languages & Solvers

### Algebraic modeling languages
| Tool | Provider | Typical use |
|------|----------|-------------|
| AMPL | AMPL Optimization | Algebraic modeling, large-scale LP/MILP/NLP |
| GAMS | GAMS Development | Modeling across many solvers |
| JuMP (Julia) | open source | Modeling LP/MILP/conic/NLP, callbacks |
| Pyomo (Python) | open source | Modeling, decomposition, stochastic programming |
| gurobipy / docplex | Gurobi / IBM | Solver-native Python modeling APIs |

### Solvers (verify academic licensing)
| Solver | Class |
|--------|-------|
| Gurobi, CPLEX, FICO Xpress, COPT | LP / MILP / QP / (some) conic |
| Mosek | Conic / SDP / second-order cone |
| HiGHS, SCIP, CBC, GLPK | Open-source LP/MILP (SCIP also MINLP) |
| Ipopt, KNITRO, BARON, Couenne | (MI)NLP, global optimization |
| OR-Tools (Google) | CP-SAT, routing, scheduling |

## 2. Stochastic, Simulation & Decision Tools

### Stochastic / probabilistic modeling
- Markov chains, queueing, and MDP/dynamic-programming analysis: `QuantEcon`, `pymdptoolbox`, custom Julia/Python.
- Stochastic programming / robust optimization: `SDDP.jl`, `PySP`/`mpi-sppy`, `RSOME`, `ROME`.
- Approximate dynamic programming / reinforcement learning for OR: `RLlib`, custom value/policy iteration.

### Discrete-event & Monte Carlo simulation
- **Simulation software**: Arena, AnyLogic, Simio, FlexSim; SimPy (Python), `simmer` (R).
- **Variance reduction / output analysis**: common random numbers, control variates, batch-means and confidence-interval procedures; ranking-and-selection libraries.
- **Simulation optimization**: `SimOpt` testbed; stochastic-gradient and surrogate methods.

### Decision & risk analysis
- Decision trees, influence diagrams, multi-attribute utility: Analytica, PrecisionTree, custom.
- Risk measures (VaR/CVaR) and chance constraints via the conic/stochastic stacks above.

## 3. Theory, Proofs & Computation

| Tool | Note |
|------|------|
| LaTeX (+ INFORMS `opre`/INFORMS style files) | Required format; amsmath/amsthm for theorems and proofs |
| TikZ / PGFPlots | Vector figures, polytopes, network diagrams |
| SageMath, SymPy, Mathematica, Maple | Symbolic checking of derivations and bounds |
| Jupyter / Pluto.jl notebooks | Reproducible numerical experiments |
| benchmarking sets (MIPLIB, DIMACS, TSPLIB, QPLIB) | Standard instances for computational studies |

## 4. Reproducibility & the ORJournal Workflow

OR enforces a **Code and Data Disclosure Policy**: for papers with algorithmic or
empirical components, authors are expected to provide all code, scripts, and data
with instructions sufficient for others to reproduce the results. Materials are
deposited in the journal's **ORJournal GitHub** organization and reviewed through a
**pull-request** process.

1. Prepare a repository following the prescribed directory structure with a **README**
   and **LICENSE**.
2. Document **hardware, software, data, installation, and run** instructions; pin
   versions and random seeds so tables/figures regenerate exactly.
3. Provide scripts that reproduce every reported number, table, and figure from raw
   inputs; separate data preparation from experiments.
4. If data are confidential/licensed/non-public, or the paper is purely
   methodological, request an **exemption with rationale in the cover letter** (decided
   by the Area Editor with final EiC authority).
5. Retain raw data sufficient to support verification/replication if asked during
   editorial review.

## 5. Reference & Writing Tools

| Tool | Note |
|------|------|
| Zotero / JabRef | Free; export to BibTeX for the INFORMS author-year style |
| BibTeX + INFORMS `.bst` | Author-year references, e.g., (Norman 1977) |
| Overleaf | Collaborative LaTeX; load the INFORMS `opre` template |
| Grammarly / language tools | Polish — keep the equation-free introduction readable |

Configure references to the INFORMS author-year convention and reconcile against the
current submission guidelines.

## 6. Submission & Process

- **Portal**: ScholarOne Manuscripts via the INFORMS Author Portal (verify the current OR link).
- **ORCID**: keep an ORCID linked to your account.
- **Area selection**: choose the correct editorial area; recommend 3 Associate Editors and suggest 5 reviewers.
- **AI**: follow the current INFORMS Generative AI Guidelines and disclose as required.

## 7. Verify Before You Rely

Editor-in-Chief, area editors, submission links, page tiers, formatting limits, fees,
and the code/data policy change over time. Always confirm the current requirements on
the official OR submission-guidelines page, the Code and Data Disclosure Policy, and
the ORJournal Instructions for Authors before submitting.
