---
name: msom-data-analysis
description: Use when executing and reporting the analysis for a Manufacturing & Service Operations Management (M&SOM) manuscript — proving structural results and running numerical studies for analytical work, or estimating and stress-testing identified effects for empirical work, plus meeting M&SOM's data-and-code replicability policy. Executes the analysis designed in msom-methods.
---

# Analysis & Replicability (msom-data-analysis)

## When to trigger

- Proofs are drafted and you need a numerical study that earns its keep
- Estimates exist and you must defend identification and robustness
- A reviewer says "the result is an artifact of the assumptions/specification"
- You are preparing the data and code disclosure M&SOM requires

## Analytical work: proofs plus a disciplined numerical study

M&SOM's dominant tradition is **analytical/stochastic modeling**, so rigor is judged first on the **proofs** and then on a numerical study that does real work:

- **Proofs**: state results as propositions/theorems; full proofs go in the online supplement (≤ 16 pages for a new submission). Verify monotonicity/convexity/threshold or base-stock structure rigorously.
- **Numerical study**: use realistic parameter ranges; quantify the *magnitude* of the structural effect, the value of the proposed policy versus benchmarks/heuristics, and the cost of relaxed assumptions. Report instance generation, seeds, and solver/settings so results reproduce.
- **Sensitivity**: show which assumptions bind and how conclusions move as primitives (demand variability, lead time, cost ratios) change.

## Empirical work: identified effects, not correlations

- Defend the **identification** designed in `msom-methods`: parallel-trends/event-study evidence for DiD, first-stage strength and exclusion for IV, density/covariate-balance for RDD, model fit and identification for structural estimation.
- Treat operational decisions (capacity, inventory, staffing, routing) as **endogenous**; address selection and simultaneity explicitly.
- **Robustness**: alternative specifications, samples, and operational measures; cluster standard errors at the operational unit; report effect *magnitudes* in operational terms (units, hours, dollars), not just significance.

## Replicability policy (M&SOM / INFORMS)

Manuscripts must contain enough detail and references to **permit replication**. You may be asked to provide raw data for editorial review, must be prepared to share it, and must **retain it** for a reasonable time after publication. For **licensed data** (Census, Compustat, CRSP, FactSet, WRDS) provide your **own code plus detailed access/linking instructions** so others can replicate without your redistributing the data. Any reuse of shared data/code beyond replicability verification must **cite the paper and acknowledge the source**.

## Checklist

- [ ] Analytical: results stated as propositions; full proofs in the ≤16-page supplement
- [ ] Numerical study with realistic ranges; magnitudes vs. benchmarks; seeds/settings reported
- [ ] Empirical: identification defended (trends/first-stage/balance); endogeneity addressed
- [ ] Robustness across specifications/samples/measures; SEs clustered at the operational unit
- [ ] Effects reported in operational magnitudes, not p-values alone
- [ ] Data/code disclosure prepared; licensed-data access instructions included; retention noted

## Anti-patterns

- "Numerical results show…" with no benchmark comparison or assumption stress-test.
- Proofs in the main text crowding out the operational insight (move them to the supplement).
- Treating capacity/inventory/staffing as exogenous in an empirical design.
- Reporting significance with no operational magnitude.
- Promising replication while withholding code/access instructions for licensed data.

## Output format

```
【Analytical】propositions proven; supplement proofs: yes/no
【Numerical study】ranges / benchmarks / magnitude / seeds ...
【Empirical identification】trends / first-stage / balance ...
【Robustness】specs / samples / measures; SE clustering ...
【Replicability】data+code disclosure; licensed-data access instructions ...
【Next step】msom-contribution-framing
```
