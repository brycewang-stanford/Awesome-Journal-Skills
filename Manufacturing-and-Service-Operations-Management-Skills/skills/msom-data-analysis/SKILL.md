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

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). M&SOM mixes analytical and empirical OM; the chain below serves the empirical-OM lane, while analytical / queueing / optimization work is outside it.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or
  `benjamini_hochberg` — report the adjusted threshold.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`;
  multilevel data → cluster at the right level.
- **Re-fit off one handle:** `audit_result(result_id)` lists the missing checks and the
  exact `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Keep the decisive checks in the body and the exhaustive battery in the appendix. See the
executed chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
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

## Worked micro-example (illustrative)

Referees grade whether the analysis converts a model or dataset into a defensible operational claim: the analytical lane wants a structural result, a benchmark-anchored magnitude, the binding assumption stress-tested, and seeds/solver settings; the empirical lane wants an identified effect in operational units with clustered SEs, not stars alone.


Vignette: a data-calibrated inventory policy for an omnichannel retailer's fulfillment center, where ship-from-store substitutes for warehouse stock. Suppose the dual-index policy, benchmarked against the firm's base-stock rule, cuts expected backorders by 22% at a 1.3% inventory increase across 480 SKU-weeks (numbers illustrative). The discipline: make the 22%/1.3% trade the headline a manager weighs, not "the policy is optimal"; show the gain shrinks to an illustrative 9% once cross-store lead-time correlation is added, naming the assumption that carries the result; and report the fitting window, seed set, and solver tolerance so a referee could regenerate the table.

## Referee-pushback patterns and the venue fix

- *"The result is an artifact of the assumptions."* → Add the sensitivity panel that varies the binding primitive, show where the conclusion flips, and state the operational regime in which it holds.
- *"Capacity/inventory/staffing is treated as exogenous."* → Instrument it, exploit a natural experiment, or model the choice; an OM empirical paper that ignores operational endogeneity is rarely identified. (For Census/Compustat/CRSP/WRDS data, ship your own code plus access instructions; confirm the current data-and-code requirement against the journal's author guidelines.)

## Output format

```
【Analytical】propositions proven; supplement proofs: yes/no
【Numerical study】ranges / benchmarks / magnitude / seeds ...
【Empirical identification】trends / first-stage / balance ...
【Robustness】specs / samples / measures; SE clustering ...
【Replicability】data+code disclosure; licensed-data access instructions ...
【Next step】msom-contribution-framing
```
