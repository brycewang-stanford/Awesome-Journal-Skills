---
name: infocom-experiments
description: Use when designing or auditing IEEE INFOCOM evaluations, covering analytical results with stated and justified assumptions, simulation with a named simulator and logged seeds, testbed and measurement studies with real traffic, honest and tuned baselines, and matching evidence to the shape of each networking claim across the analysis-simulation-testbed spectrum.
---

# INFOCOM Experiments

Use this before submission when the evaluation is not yet locked. INFOCOM reviewers span the full
**analysis → simulation → testbed** spectrum, and the evaluation is where a good idea is won or
lost — especially since there is (traditionally) **no rebuttal** to repair a weak comparison. The
organizing principle is **evidence proportional to the claim**, delivered by the method the claim
demands: a bound needs a proof, a design needs a fair experiment, a behavior claim needs
measurement.

## Evaluation audit

- **Match the method to the claim.** An *optimality/approximation* claim needs a **proof** under
  stated assumptions; a *performance* claim needs a **fair experiment**; a *real-world behavior*
  claim needs **measurement** on real traffic. A simulation cannot substitute for a proof, and a
  proof under unrealistic assumptions cannot substitute for an experiment.
- **State and justify every assumption.** For analytical work, list the assumptions (A1, A2, ...)
  and defend each; a theorem true only under an assumption no network satisfies is a scored
  weakness a reviewer will name — and you cannot rebut it.
- **Name the simulator and pin the setup.** State whether it is ns-3, OMNeT++, a custom simulator,
  or a testbed; report the topology, traffic model, number of runs, seeds, and confidence intervals.
  "A large-scale simulation" with no setup is not evidence.
- **Choose honest baselines,** including the strongest prior scheme and a simple-but-reasonable
  alternative, each tuned with a documented, equal budget. An untuned baseline is the classic
  INFOCOM reject.
- **Report variance, not point estimates.** Confidence intervals over multiple seeded runs;
  appropriate statistics; say what the intervals represent.
- **For testbeds/measurement,** describe the hardware, the trace or workload, the collection
  methodology, and the confounds — and bound them.

## Claim-to-evidence design table

| Networking claim | Matching evidence | Reject pattern avoided |
|---|---|---|
| "Algorithm is near-optimal" | Proof of an approximation/competitive ratio under stated assumptions | "Only shown on examples the authors chose" |
| "Scheme improves throughput/delay" | Seeded simulation or testbed vs. a tuned baseline, with CIs | "Untuned baseline; single run; no variance" |
| "Scales to large networks" | Runtime/quality across realistic topology sizes | "Only a 10-node topology tested" |
| "Holds in real deployments" | Testbed or trace-driven measurement with real traffic | "Synthetic traffic claimed to generalize" |
| "The learner adds the value" | Ablation vs. a non-ML heuristic on the same inputs | "ML component's marginal value never isolated" |

## Simulation and reproducibility floor

```text
[Simulator]  name it (ns-3/OMNeT++/custom); pin the version; describe the model, not just the tool
[Topology]   real or realistic (e.g., from a topology dataset); state size and generation method
[Traffic]    the workload/trace and its source; synthetic models justified against real behavior
[Runs/seeds] multiple seeded runs; report the number and log the seeds; give confidence intervals
[Baselines]  the strongest competitor + a simple one, each tuned with a documented equal budget
[Compute]    the runtime/scale actually reached, not vague feasibility language
```

## Analytical-work floor

- List assumptions explicitly and justify each against real network conditions.
- Give proof sketches in the body and full proofs in a tight in-budget appendix (it counts toward
  the nine pages) or state where the full proof lives.
- Validate the theory in simulation: show the bound is tight/loose where the analysis predicts.

## Vignette: evaluating a caching/offloading policy

Suppose the paper claims an online caching policy with a competitive ratio that also beats prior
heuristics. The matching plan: prove the ratio under stated assumptions; then simulate on a real
request trace with multiple seeds, comparing against the strongest prior policy tuned with an equal
budget and a simple LRU baseline; report hit-rate and delay with confidence intervals; show where
the empirical gap matches the analytical bound; and state the regime (skewed vs. uniform demand)
where the guarantee is loose — every number traceable to a logged run.

## Statistical reporting floor

- Confidence intervals over seeded runs for every simulated/measured comparison; say what they
  represent.
- The number of runs and the source of randomness for any stochastic component.
- The topology sizes and traffic models actually used, not vague "large-scale" language.

## Output format

```text
[Evaluation readiness] strong / adequate / weak
[Claim -> method map] <claim: proof | simulation | testbed/measurement>
[Assumptions] <listed and justified? yes/no>
[Simulator/setup] <named? seeds logged? CIs reported? yes/no>
[Baseline fairness] <baseline -> tuned? equal budget? documented?>
[Decision-critical next run] <one experiment or proof to add before the deadline>
```
