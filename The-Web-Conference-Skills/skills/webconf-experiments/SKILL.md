---
name: webconf-experiments
description: Use when designing or auditing the empirical section of a Web Conference (WWW) paper — matching evidence to the claim's scale, choosing datasets with provenance and freshness, blocking temporal and popularity leakage, running honest baselines from the sibling circuit, and deciding when live-platform or user-study evidence is required.
---

# Web Conference Experiments

The empirical bar at this venue is not "more datasets" — it is **evidence whose
scale, freshness, and realism match the claim**. A method claiming web-scale
efficiency must show the scaling curve; a measurement claiming platform-general
behavior must show more than one platform; a system claiming deployability must
show cost under realistic load. Audit the claim-evidence match before adding
anything.

## Claim-to-evidence contract

| Claim type | Minimum honest evidence | Habitual shortfall |
|---|---|---|
| "Outperforms" (quality) | Tuned recent baselines, repeated runs, variance, significance | Untuned baselines from 3-year-old code |
| "Scales" (efficiency) | Cost curves across ≥2 orders of magnitude, hardware stated | One big-dataset wall-clock number |
| "Generalizes" (external validity) | ≥2 platforms/domains or a stated single-platform scope | Silent single-platform universality |
| "Measures" (phenomenon) | Construct definition, sampling frame, bot/spam handling, error bars | Convenience crawl treated as census |
| "Deploys" (system) | Load, latency percentiles, failure behavior; A/B where claimed | Demo-grade throughput on toy traffic |

## Dataset selection with provenance

- Prefer datasets with **documented collection**: source, crawl window, sampling
  rule, known biases. An undocumented Kaggle mirror of a platform dump is a
  provenance liability reviewers now flag.
- **Freshness is evidential** here: user behavior and platform mechanics drift, so
  a 2015 interaction dataset supports historical claims, not claims about current
  platforms. Either add a recent corpus or scope the claim in time.
- Report per-dataset statistics (nodes/edges/users/items/time span) in a table, and
  state *why this set of datasets spans the claim* — heterogeneity in domain, size,
  and density is the point, not the count.
- For data you collected: consent/ToS posture and aggregation level belong beside
  the dataset description (body text, per `webconf-writing-style`).

## Leakage: the venue's most-caught methodological bug

Web data is temporal, popularity-skewed, and duplicated across the crawl. Three
specific leaks to audit:

1. **Temporal**: random splits on interactions or evolving graphs train on the
   future. Use a time-based split rule and state it ("train < T ≤ test").
2. **Popularity**: negative sampling that mirrors test popularity inflates ranking
   metrics; report at least one popularity-debiased or full-ranking metric.
3. **Duplication/contamination**: near-duplicate pages across splits, and — for
   LLM-era pipelines — benchmark text present in a foundation model's pretraining.
   State the dedup rule; where an external LLM is a component, discuss
   contamination explicitly rather than hoping no one asks.

## Baselines and ablations

Baselines come from the **sibling circuit's current cycle** (WWW, WSDM, SIGIR,
KDD, CIKM within ~2 years), tuned with the same budget as your method — state the
search space for both, since asymmetric tuning is the most common quiet unfairness.
Ablate the *claimed mechanism*, not everything: if the paper's story is "the
crawl-time signal is what helps," the ablation table must contain exactly the row
that removes it.

```text
Experiment matrix skeleton (fill per claim, not per dataset):
  claim C1 "quality"  : datasets D1-D3 x {ours, B1..B4} x 5 seeds -> mean±sd, test
  claim C2 "scales"   : D_synthetic sized 10^6..10^9 edges x {ours, B1} -> cost curve
  claim C3 "mechanism": ours minus {signal S, module M} on D1-D3    -> delta table
  claim C4 "external" : platform P2 replication of headline result  -> one table
Every table row answers a named claim; rows answering nothing get cut.
```

## Statistics that survive review

- Repeated runs with different seeds wherever training is stochastic; report
  mean ± sd and the number of runs.
- Significance tests matched to the design (paired across datasets/queries), with
  effect sizes — at web scale everything is "significant," so the delta's
  *magnitude and cost* carry the argument.
- Percentiles, not means, for latency and exposure-type quantities; web
  distributions are heavy-tailed and means mislead.

## When offline evidence is not enough

Claims about *user response* (satisfaction, engagement shifts, behavior change)
need a user study or an online experiment, with ethics posture stated; claims about
*production viability* need load realism. If neither is obtainable, weaken the
claim to what offline evidence supports — "improves offline ranking quality" is
publishable; "improves user satisfaction" without users is a rebuttal-week wound
that cannot be healed in seven days.

## Predictable objections and their cheap preemptions

Four objections recur across this venue's tracks; each has a preemption that
costs a sentence or a table row, not a new experiment campaign:

- *"Gains may come from capacity, not the proposed component"* — include one
  parameter-matched ablation row and state parameter counts in the caption.
- *"Datasets are all from one platform family"* — either add the second-family
  corpus or write the scope sentence in the conclusion; silence converts a
  limitation into a discovered flaw.
- *"The baseline numbers differ from the original paper"* — declare the
  re-implementation and the protocol difference (split, metric variant,
  preprocessing) in a footnote at first mention; unexplained deltas read as
  either sloppiness or gaming.
- *"Efficiency claims lack a cost axis"* — every quality table involving a
  method whose selling point includes scale gets a companion column (time,
  memory, or queries), because at web scale a 0.5-point win at 10x cost is a
  negative result.

The meta-rule: reviewers here are drawn from a circuit that reviews the same
methods at WSDM, SIGIR, and KDD in the same year; they have seen this quarter's
common failure modes several times already. The paper that names its own
weaknesses first is the one whose rebuttal week is quiet.

## Audit checklist

- [ ] Every headline claim mapped to a table/figure that can carry it.
- [ ] Split rules stated; temporal/popularity/duplication leaks addressed.
- [ ] Baselines recent, tuned symmetrically, search spaces disclosed.
- [ ] Variance, tests, and effect sizes present; percentiles for tails.
- [ ] Scope sentences where evidence is single-platform or offline-only.

## Output format

```text
[Claim-evidence map] C1..Cn -> table/figure or GAP
[Leakage audit] temporal / popularity / duplication: clean or findings
[Baseline fairness] recency, tuning symmetry: pass/fail
[Scale realism] does evidence scale match claim scale? <notes>
[Required additions] <ranked by review risk, with cost estimate>
```
