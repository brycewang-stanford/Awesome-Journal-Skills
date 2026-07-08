---
name: uai-experiments
description: Use when designing or auditing UAI experiments where inference quality is the endpoint, covering calibration and coverage measurement, posterior diagnostics, structure-recovery metrics for causal and graphical models, seeded repeated runs, baselines from both sampling and optimization families, and mapping each claim to its evidence.
---

# UAI Experiments

Use this while the empirical design is still changeable. At UAI the object under test is
usually an inference procedure — a posterior, a graph, an interval, a decision policy —
so the experimental question is rarely "is accuracy higher?" and usually "is the
uncertainty right, and at what cost?". Reviewers score whether claims are backed up
convincingly; design the study so each claim has a designated exhibit.

## Metrics follow the probabilistic object

| Claimed object | Primary metrics | Supporting diagnostics |
|---|---|---|
| Posterior approximation | Wasserstein/KL to gold-standard posterior on tractable cases | R-hat, ESS, trace plots; ELBO with restarts |
| Predictive uncertainty | NLL, CRPS, empirical coverage vs nominal | Reliability diagrams; ECE with stated binning |
| Conformal / interval methods | Coverage at each α, interval width | Conditional coverage slices, not just marginal |
| Causal structure | SHD, SID, edge precision/recall vs ground truth | Performance vs sample size; sensitivity to faithfulness violations |
| Treatment effects | Bias/RMSE on ATE/CATE with known ground truth | Overlap diagnostics; propensity calibration |
| Decision policies | Regret, expected utility under the stated prior | Robustness under prior misspecification |

The recurring UAI failure is a proxy mismatch: claiming better uncertainty while
measuring only accuracy, or claiming a better posterior while reporting only downstream
prediction. Pick the metric that measures the claimed object directly.

## The synthetic-to-real ladder

Because ground-truth posteriors and ground-truth graphs exist only where you construct
them, strong UAI papers climb a ladder:

1. **Exact-truth regime**: small models where exact inference or the true SCM is
   available — the only place "closer to the truth" is literally checkable.
2. **Stress regime**: the same generators with an assumption deliberately broken
   (unfaithful distributions, heavy-tailed noise, hidden confounding) — this is where
   your limitations section gets its numbers.
3. **Real-data regime**: demonstrates relevance, evaluated by proxies (held-out NLL,
   stability, downstream decisions) with the proxy status stated plainly.

A paper living only on rung 3 cannot back an inference-quality claim; one living only on
rung 1 will be asked why anyone should care. Budget experiments across all three.

## Stochasticity is part of the result

- Repeat over seeds and report dispersion (mean ± sd, or paired comparisons when
  methods share data draws); single-run tables at an uncertainty venue are
  self-refuting.
- Distinguish the two randomness sources — data generation and algorithm internals —
  and vary them separately when the claim depends on one of them.
- Fix the comparison protocol before running: same data splits, same compute budget or
  an explicit cost axis, same tuning effort for baselines as for the proposed method.

```python
# Paired, seeded comparison harness: every method sees identical data draws
import numpy as np

def run_grid(methods: dict, make_data, seeds=range(10)):
    rows = []
    for s in seeds:
        data = make_data(rng=np.random.default_rng(s))   # shared draw per seed
        for name, fit in methods.items():
            post = fit(data, seed=s)
            rows.append({"seed": s, "method": name,
                         "coverage@90": post.coverage(0.90),
                         "nll": post.nll(data.test),
                         "ess_min": post.min_ess()})
    return rows   # aggregate as mean ± sd; report per-seed table in the appendix
```

## Baseline selection that survives this reviewer pool

- Include the cheap classical baseline (exact inference where feasible, a well-tuned
  Laplace approximation, the PC algorithm, plain split conformal): UAI reviewers use
  these as sanity anchors, and their absence reads as fear.
- Include the strongest recent neighbor from UAI/AISTATS/NeurIPS, tuned in good faith
  with its search grid disclosed.
- When your method has a compute knob (chains, particles, restarts), plot the
  quality-versus-cost curve rather than a single operating point chosen post hoc.

## Compute fairness, concretely

- Match tuning budgets: if the proposed method saw 50 configurations, baselines see
  50, drawn from grids their authors would endorse.
- Match convergence criteria: comparing your converged sampler against a baseline's
  fixed-iteration run measures patience, not methods.
- When budgets cannot match (an exact baseline that only scales to n=100), report it
  at its feasible scale and mark the cell honestly rather than dropping the method.
- State who tuned what: "baseline hyperparameters from the original paper" and
  "tuned by us on the same validation split" are different evidentiary claims.

## Reporting block, standardized

Give every experiment family the same reporting block in the appendix, so reviewers
can audit uniformly and you can spot your own gaps:

```text
EXPERIMENT <id> — backs claim: <paper sentence, quoted>
  data:        <generator or dataset+version, splits, preprocessing>
  methods:     <proposed + baselines, tuning grids, selection rule>
  randomness:  <seeds, what varies per seed: data draw / init / both>
  compute:     <hardware, wall-clock per method>
  metrics:     <primary + diagnostics, with definitions or citations>
  result:      <table/figure reference; dispersion form (sd / CI / paired)>
  caveats:     <regimes where the result did not hold>
```

The `caveats` line is not decoration. At this venue an experiment section that admits
where the method loses reads as calibrated; one that never loses reads as curated.

## Ablations for mechanisms, not rituals

Design each ablation to isolate the component your theory says matters: remove the
coupling, swap the score function, freeze the calibration step. An ablation grid nobody
can interpret is appendix filler; a single ablation matching a theorem's prediction is
evidence.

## Output format

```text
[Claim → exhibit map] <each headline claim with its table/figure/diagnostic>
[Ladder coverage] exact-truth / stress / real — which rungs are missing
[Uncertainty of results] seeds, dispersion, pairing — adequate? 
[Baseline audit] classical anchor present? strongest neighbor tuned fairly?
[Proxy mismatches] <claims measured by the wrong metric>
```
