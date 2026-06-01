---
name: ors-data-analysis
description: Use when running and reporting the computational study for an Operations Research (OR) manuscript — benchmark instances, baselines, reproducible experiments, statistical care for stochastic output, and the ORJournal code-and-data reproducibility workflow. Executes and reports the numerical evidence; it does not prove the results (ors-methods) or lay out the exhibits (ors-tables-figures).
---

# Computational Study & Reproducibility (ors-data-analysis)

## When to trigger

- Theory is in place and you need numerical evidence that the method works and scales.
- You must benchmark against credible baselines on standard instances.
- You are preparing the code/data deposit for the ORJournal reproducibility review.

## Design a defensible computational study

*Operations Research* judges computation as evidence supporting a methodological
claim, not as the contribution by itself. Make it convincing:

- **Instances:** use recognized benchmark libraries (e.g., MIPLIB, TSPLIB, DIMACS,
  QPLIB) plus, where relevant, instances from the motivating application; report sizes
  and characteristics so difficulty is visible.
- **Baselines:** compare against the *closest* prior methods and a strong off-the-shelf
  solver, not a weak strawman. Tie experiments to the claims in `ors-literature-positioning`.
- **Metrics:** report what the theory predicts — optimality gap, solution time,
  iterations/oracle calls, scaling with size, and where relevant the quality at a fixed
  budget. Show how empirics corroborate proved bounds/rates.
- **Reporting:** specify hardware, solver versions, time limits, and termination
  criteria. State which configuration produced each table.

## Statistical care for stochastic output

Where output is random (simulation, randomized algorithms, learning-driven OR):

- Report **confidence intervals**, not point estimates, with the procedure
  (replications, batch means, regenerative) and the number of replications.
- Use **common random numbers** for paired comparisons and report the paired analysis.
- For ranking/selection or sim-opt, report the statistical guarantee and the budget.
- Average over multiple seeds; report dispersion, and fix seeds for reproducibility.

## The ORJournal code-and-data workflow (mandatory where applicable)

For papers with algorithmic or empirical components, *Operations Research* expects
**all code, scripts, and data** with instructions sufficient to reproduce the results.
Materials are deposited in the journal's **ORJournal GitHub** organization and reviewed
through a **pull-request** process:

- Provide a **README** and **LICENSE** and follow the prescribed **directory structure**.
- Document **hardware, software, data, installation, and run** steps; pin versions and
  seeds so every table/figure regenerates exactly from raw inputs.
- Separate data preparation from experiments; one command per reported result where possible.
- If data are confidential/licensed/non-public, or the paper is purely methodological,
  request an **exemption with rationale in the cover letter** (Area Editor decides, EiC final).
- Retain raw data sufficient to support verification/replication if the editors ask.

## Anti-patterns

- Cherry-picked instances or a tuned method vs. a default-config baseline.
- Reporting means of stochastic runs with no confidence intervals or seeds.
- Unspecified hardware/solver/time-limit, making results irreproducible.
- Treating the computational section as the contribution when the theory is thin.
- Planning to "share code on request" instead of using the ORJournal deposit.

## Output format

```
【Instances】benchmark + application; sizes reported
【Baselines】closest prior + strong solver (no strawman)
【Metrics】gap / time / scaling; corroborates proved bounds?
【Stochastic care】CIs, CRN, seeds, replications ...
【Reproducibility】ORJournal repo: README/LICENSE/structure; exemption? 
【Next step】ors-tables-figures
```
