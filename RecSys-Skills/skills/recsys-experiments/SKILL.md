---
name: recsys-experiments
description: Use when designing or auditing ACM RecSys experiments centered on offline-versus-online evaluation — temporal splits, equal-budget baseline tuning, full-ranking versus sampled metrics, off-policy estimators (IPS, SNIPS, doubly robust), A/B tests, exposure and popularity bias, seeds and variance, and matching each recommendation claim to its evidence.
---

# RecSys Experiments

Use this before submission when the empirical story is not yet locked. At RecSys the experiment
section is where papers are won or lost, because the community's reproducibility culture makes
reviewers read evaluation choices as a proxy for whether the gains are real.

## Experiment audit

- Map each recommendation claim to a table, figure, ablation, off-policy estimate, or A/B result.
- Tune every baseline under an **equal search budget**; an under-tuned baseline is the fastest
  route to a low score at this venue.
- Use a **leakage-aware split**: temporal or leave-one-last for sequential/session data, never a
  random split that lets future interactions into training.
- Rank over the **full item catalog** or state clearly that a sampled candidate set was used and
  why — sampled metrics can reorder methods.
- Report uncertainty: multiple seeds, mean ± sd, and a significance test on close results.
- Report the split, filtering, metrics and cutoffs, tuning grid and selection metric, seeds,
  hardware, and runtime.
- Add ablations that isolate the mechanism, not cosmetic variants.

## Offline vs online: the RecSys distinctive

Offline metrics are cheap but only a proxy for deployed behavior. RecSys rewards papers that are
honest about the gap and, where possible, bridge it.

| Evaluation mode | What it establishes | What it cannot establish |
|---|---|---|
| Offline top-N on logged data | Ranking quality against past behavior | That live users engage more |
| Off-policy estimate (IPS / SNIPS / DR) | Estimated online reward under exposure correction | Anything, if propensities are missing or positivity fails |
| Simulator / semi-synthetic | Behavior under a controlled, known reward | Real-world generalization |
| A/B test | Actual deployed effect | Reproducibility without the platform |

The strongest design triad: a tuned offline study, an off-policy or simulator bridge showing the
offline gain tracks a deployment quantity, and — where available — an A/B result.

## Claim-to-evidence design table

| Recommendation claim | Matching experiment | Reject pattern avoided |
|---|---|---|
| "Ranks better than baselines" | Full-ranking metrics, equal-budget tuning, variance | "Beat only untuned defaults" |
| "Gain transfers to deployment" | Off-policy estimate or A/B result | "Offline nDCG assumed to imply engagement" |
| "Handles the exposure/popularity bias" | Debiased metric or propensity-corrected estimate | "Popularity bias reported but not corrected" |
| "Mechanism M drives the gain" | Ablation removing only M | "Improvement unattributed to any component" |

## Vignette: an off-policy ranking study

Suppose the paper claims an exposure-corrected ranker improves engagement. The matching plan: a
temporal split with full-ranking metrics and equal-budget baselines; a self-normalized IPS
estimate of reward with the positivity assumption stated; a semi-synthetic simulator sweeping
exposure strength to show the offline estimate and the known online reward move together; and an
ablation removing the exposure correction to isolate it — every panel tied to a numbered claim.

## Statistical reporting floor

```text
- Seeds and replication count for every stochastic table; captions name what the bars are.
- Split protocol and metric cutoff stated once, in the body.
- Tuning grid + selection metric per system, symmetric across baselines.
- Compute actually consumed, not vague feasibility language.
```

## Output format

```text
[Experiment readiness] strong / adequate / weak
[Claim -> evidence map] <claim: table / off-policy / A-B / simulator>
[Evaluation-validity risks] <baseline tuning / split leakage / sampled metrics>
[Offline-online bridge] present / missing / scoped-to-offline
[Decision-critical next run] <one experiment>
```
