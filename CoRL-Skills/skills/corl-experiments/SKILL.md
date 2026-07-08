---
name: corl-experiments
description: Use when designing or auditing experiments for a CoRL robot-learning paper — seeds and evaluation-episode counts, task-suite breadth, real-robot versus simulation evidence, sim-to-real gap measurement, baseline fairness across BC/RL/VLA families, generalization splits, and statistics for success-rate claims.
---

# CoRL Experiments

At CoRL the object under evaluation is a *learned policy*, which makes the
evidence problem statistical twice over: training is stochastic (seeds, data
order, initialization) and execution is stochastic (initial states, physics,
sensor noise). An experimental design that controls only one of the two is the
most common weakness this reviewer pool writes up.

## Match the evidence to the claim, not the venue

| Claim in the paper | Minimum credible evidence shape |
|---|---|
| "Method X learns task family T" | Multiple training seeds; per-task success over many scripted-reset episodes |
| "X outperforms baseline Y" | Same data, same evaluation protocol, same tuning effort for both; dispersion reported |
| "X transfers sim-to-real" | The *same checkpoint* evaluated in sim and on hardware; the gap reported as a number |
| "X generalizes to novel objects/scenes/instructions" | Held-out splits defined before training; per-split breakdown, not a pooled average |
| "X scales with data" | ≥3 dataset sizes on the same axis; no two-point "trends" |
| "X runs in real time on the robot" | Latency/frequency measured on the deployed compute, stated with hardware |

The routing consequence: if none of your claims require the last four rows, ask
whether the paper is CoRL-shaped at all (`corl-topic-selection`).

## The two-layer randomness protocol

- **Training layer**: train ≥3 seeds (5 where budget allows) per method per
  configuration. Report the spread across seeds — a method whose best seed wins
  but whose median loses has not demonstrated superiority.
- **Evaluation layer**: for each trained policy, evaluate over a fixed, scripted
  set of initial conditions — in simulation, dozens to hundreds of episodes per
  task is cheap and expected; on hardware, 10–25 trials per task per policy is
  typical practice, with the success criterion written down verbatim.
- Never mix the layers in reporting: "80% success" must decompose into "mean over
  k seeds of per-seed success over n episodes," and the paper states k and n in
  the table caption, not only in the appendix.

```python
# Evaluation bookkeeping: per-seed success with a binomial interval,
# then dispersion across seeds — the two layers stay separate.
import numpy as np
from scipy import stats

def summarize(results):           # results[seed] = list of 0/1 episode outcomes
    per_seed = {}
    for seed, eps in results.items():
        n, k = len(eps), int(np.sum(eps))
        lo, hi = stats.beta.ppf([0.025, 0.975], k + 1, n - k + 1)  # Jeffreys-ish CI
        per_seed[seed] = dict(rate=k / n, n=n, ci=(lo, hi))
    rates = [v["rate"] for v in per_seed.values()]
    return per_seed, dict(mean=np.mean(rates), sd=np.std(rates), seeds=len(rates))
```

Small-n hardware caveat: with 15 trials, a 73% vs 60% difference is not
resolvable — either add trials, aggregate over tasks with a paired design, or
soften the comparative language.

## Sim, real, and the space between

- Declare each experiment's regime in the table itself (sim / real / sim-trained
  real-evaluated). Reviewers at this venue actively hunt for regime laundering —
  headline numbers from sim standing in for a "real-world" abstract claim.
- If the paper's story includes transfer, the **sim-to-real delta is a result**,
  not an embarrassment: evaluate the identical checkpoint in both regimes on
  matched task instances and print the gap. A measured 20-point drop with
  analysis outranks an unmeasured claim of robustness.
- Describe the reality of hardware evaluation: reset procedure (human or
  scripted), object pose randomization method, stopping rule, and any trials
  excluded — exclusions disclosed with cause, never silently.
- Simulation-only papers survive at CoRL when the sim is a recognized benchmark
  and the claims stay inside it; say why the simulator is adequate for the claim
  (contact fidelity, sensor models, prior validated transfer).

## Baseline fairness across method families

Robot-learning baselines span imitation (BC, diffusion policies), offline/online
RL, and pretrained VLA models — families with wildly different data appetites:

- Give every family its natural input: comparing your method-with-demos against
  an RL baseline denied demos measures data access, not algorithms. Either equal
  data or an explicit data-budget axis.
- Tune baselines with the same effort budget you spent on your method and say so
  ("each method: 24 GPU-hours of search over its authors' recommended grid").
- Pin baseline provenance: re-implementation vs official code vs released
  checkpoint — each is a different evidentiary object; name which one each row is.
- Include one strong recent robot-learning baseline (not only classical control),
  because this reviewer pool benchmarks your table against the current PMLR
  volume, and one simple sanity baseline (scripted policy, nearest-neighbor over
  demos) to calibrate task difficulty.

## Generalization splits that survive scrutiny

- Freeze train/held-out splits (objects, scenes, language instructions, layouts)
  before training and publish the split lists in the supplementary.
- Report per-axis breakdowns: "novel object, seen scene" and "seen object, novel
  scene" are different claims; a pooled number hides which one failed.
- For language-conditioned policies, separate paraphrase-level from task-level
  novelty — reviewers with VLA experience will ask.

## Ablations and the Limitations coupling

- Ablate the components you advertise: each named contribution in the intro gets
  a row showing the system without it.
- Feed the failures you observe into the mandatory Limitations section
  (`corl-writing-style`); a Limitations section that matches the failure cases in
  your video reads as credible, and one that contradicts them reads as concealment.

## Design-review checklist

```text
[ ] Every abstract-level claim mapped to a table/figure with regime declared
[ ] k seeds x n episodes stated per cell; two randomness layers separated
[ ] Hardware protocol written: resets, success criterion, stopping rule, exclusions
[ ] Same-checkpoint sim/real pairing for any transfer claim; gap printed
[ ] Baselines: fair data, disclosed tuning, pinned provenance, one recent + one simple
[ ] Splits frozen pre-training; per-axis generalization breakdown
[ ] Compute + data volumes reported (GPU-hours, demo counts, env steps)
```

Evidence norms here are community culture rather than a posted rulebook — they
move each year with the field. Calibrate against the newest PMLR volume
(v305 = CoRL 2025) and the current reviewer instructions at corl.org.
