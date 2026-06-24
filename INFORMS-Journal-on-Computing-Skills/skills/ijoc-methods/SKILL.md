---
name: ijoc-methods
description: Use when the method choice, baselines, and computational-experiment design need alignment for an INFORMS Journal on Computing (IJOC) manuscript — before the experiments are run at scale. Designs a fair, reproducible experimental protocol; it does not write the algorithm proofs (see ijoc-theory-development).
---

# Method & Experimental Design (ijoc-methods)

## When to trigger

- The algorithm is settled but the **experimental protocol** (instances, baselines, tuning, hardware, metrics) is not designed
- You are about to run experiments and want to avoid a protocol a referee will reject after the fact
- A referee challenges the **fairness** of a comparison (asymmetric tuning, mismatched time limits, weak baseline)
- You must choose **what to measure** so the computational claim is actually supported

## Designing an IJOC-grade computational experiment

At IJOC the experiment *is* the evidence, so it is held to a high methodological standard. Design it before running it, around five pillars. Getting these right up front is cheaper than re-running after an R&R.

1. **Instances.** Use **public, standard benchmark sets** wherever they exist (e.g., MIPLIB-class libraries, TSPLIB-style, established generators) so results are comparable and not cherry-picked. If you must generate instances, document the generator, the parameter ranges, and the seeds, and deposit them. Report the size distribution; do not test only on the sizes where you win.
2. **Baselines.** Compare against the **strongest available** method, not a strawman: the leading published algorithm and, for exact methods, a current commercial/open solver (CPLEX/Gurobi/SCIP/HiGHS) at default and tuned. A win over a weak baseline is not a win.
3. **Fair tuning.** Tune your method and the baselines with the **same budget on a disjoint tuning set**, then report on a held-out test set. Disclose the tuning procedure; never tune on the test instances. Asymmetric tuning is the single most common fatal flaw.
4. **Hardware & time.** Report CPU/GPU, cores used, memory, language/solver versions, and the **time limit**. Compare at equal wall-clock or equal hardware; if you must compare across machines, normalize and say how. State whether runs are single- or multi-threaded.
5. **Metrics & statistics.** Pick metrics that match the claim — solve time, optimality gap, primal/dual bound at time limit, solution quality, number solved, generalization error, estimator variance. Run **multiple seeds** for stochastic methods and report dispersion, not just means. Plan the **statistical test** (Wilcoxon signed-rank, performance profiles) now.

## Method choice should follow the structure, not fashion

Choose the method because the **problem structure** warrants it: decomposition when the model is block-angular; column generation when columns are exponential but priceable; a learned heuristic when many similar instances are solved repeatedly; variance reduction when the simulation estimand is rare-event-like. "We used deep learning because it is popular" invites the reviewer to ask what it buys over a tuned classical baseline — so include that baseline.

## Common protocol traps by archetype

The fair-comparison standard bites differently across archetypes, and each has a signature trap:

- **Exact methods:** comparing your tuned cuts against a solver with cuts/presolve turned off — disclose every solver parameter you changed, and justify it.
- **Heuristics:** reporting the best of many runs as "the result." Report a fixed budget and the distribution; the comparison is run-to-run, not best-to-best.
- **ML-for-OR:** training and testing on instances from the same generator seed, so "generalization" is memorization. Hold out an out-of-distribution instance family and report it.
- **Simulation:** unequal replication counts across methods, or comparing variance without equalizing CPU effort. Fix the budget, then compare variance.

## Reproducibility is part of the method

Because accepted papers deposit code/data in the **IJOC GitHub repository**, build the experiment so the deposit is trivial: scripted runs (`scripts/`), pinned dependencies (`requirements.txt` / `Manifest.toml`), fixed seeds, and a `results/` layout that maps to the paper's tables. Log raw outputs (not just summaries) so a reviewer can recompute your statistics. Designing this in from the start means the reproducibility deposit is a snapshot, not a scramble.

## Execution bridge (StatsPAI / Stata MCP)

For the **empirical / causal lane**, estimate and audit rather than only specify. Full
map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). INFORMS JoC is computing / algorithms and methodology; the causal-inference chain below applies only to its empirical-evaluation papers, not to algorithm design.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result` to
  enumerate the checks the design owes.
- **Panel / staggered DiD:** `callaway_santanna` / `sun_abraham` + `bacon_decomposition`
  + `honest_did_from_result`. **IV:** `effective_f_test` + `anderson_rubin_ci`. **RDD:**
  `rdrobust` + `mccrary_test`.
- **Experiments:** randomization-based inference and `romano_wolf` for the many-outcome
  family-wise correction reviewers expect.

Match the toolchain to the **reviewer pool**, and report the effect size the venue
wants. A run end-to-end (synthetic data, real returns) is in the
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Instances are public/standard or fully documented + deposited; size range is representative
- [ ] Baselines include the strongest published method and a current solver at default + tuned
- [ ] Tuning uses equal budget on a disjoint set; test set is held out; procedure disclosed
- [ ] Hardware, cores, memory, versions, and time limit are reported
- [ ] Metrics match the claim; multiple seeds for stochastic methods with dispersion reported
- [ ] A statistical comparison (Wilcoxon / performance profile) is planned
- [ ] Method choice is justified by problem structure, not popularity
- [ ] The run is scripted and seeded so the GitHub deposit is a snapshot

## Anti-patterns

- Strawman baseline (e.g., textbook B&B) instead of a current solver/leading method
- Tuning your method hard while running baselines at default
- Reporting only mean runtime over one seed for a randomized algorithm
- Hiding the hardware/time limit, or comparing across machines without normalization
- Testing only on instance sizes where the method wins
- Picking a method by fashion and omitting the classical baseline it must beat

## Output format

```text
【Journal】INFORMS Journal on Computing
【Skill】ijoc-methods
【Method + why】structure that justifies it
【Instances】public/standard or documented+deposited; size range
【Baselines】strongest method + solver (default/tuned)
【Tuning】equal budget, disjoint set, held-out test? [Y/N]
【Hardware/time】CPU/GPU, cores, versions, limit
【Metrics + test】metric(s); Wilcoxon / performance profile; #seeds
【Next skill】ijoc-data-analysis
```
