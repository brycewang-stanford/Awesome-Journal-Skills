---
name: ijcai-experiments
description: Use when designing or auditing IJCAI or IJCAI-ECAI experiments, baselines, ablations, statistical evidence, hyperparameter reporting, compute descriptions, dataset handling, ethics risks, and reproducibility evidence for AI papers.
---

# IJCAI Experiments

Use this before submission when the experimental story is not yet locked. IJCAI reviewers
can score novelty, correctness, clarity, significance, impact, presentation, ethics, and
reproducibility.

## Experiment audit

- Map each major claim to a table, figure, theorem, ablation, proof, or qualitative analysis.
- Include strong, current, and properly tuned baselines; explain any missing baseline before
  reviewers ask.
- Report dataset splits, preprocessing, metrics, search ranges, final hyperparameters,
  selection criteria, random seeds or repeats, and compute infrastructure.
- Add ablations for the core mechanism, not just peripheral architecture choices.
- Use uncertainty estimates, paired tests, confidence intervals, or repeated runs when small
  differences could change the conclusion.
- For sensitive data or human-facing systems, document privacy, consent, copyright, safety,
  fairness, misuse, and deployment limits.
- Keep enough details in the main paper for credible reproduction even if reviewers ignore
  the supplementary material.

## What IJCAI reviewers score the evidence on

IJCAI draws reviewers from symbolic AI, search, planning, constraint satisfaction, KR,
multi-agent systems, game theory, ML, NLP, and vision, so the experimental section must read
across subcommunities. Calibrate evidence to the claim type rather than copying an ML-only
template.

| Contribution type | Decisive evidence | Common reject trigger |
| --- | --- | --- |
| Search / planning | Coverage, anytime quality, expansion counts, time/memory cutoffs, per-domain breakdown | Single suite, no domain table, missing strong planner baseline |
| Constraint / SAT | Cactus plots, instances within timeout, solver versions | No virtual-best comparison |
| Multi-agent / game theory | Welfare/equilibrium metrics, agent-count scaling, seeds | Claims hold at one population size only |
| Learning method | Strong current baselines, core-mechanism ablations, variance | Cherry-picked seeds, weak baselines |
| Theory-plus-experiment | Experiments confirming the proven bound | Empirics outside the theorem's regime |

## Worked vignette: a heuristic-search paper

A submission proposes a learned heuristic for cost-optimal classical planning and reports a
single aggregate "12% fewer expansions" number. Apply the decision rules:

1. Evidence and baseline: replace the single mean with a per-domain coverage and expansion
   table, and add a strong admissible-heuristic baseline that shows optimality is preserved.
2. Core ablation: isolate the learned component from the search framework so the gain is not
   credited to engineering, and report multiple training seeds since the heuristic is stochastic.
3. Compute: state the planner, time and memory limits, and machine, since coverage is
   meaningless without a stated timeout.

## Reviewer pushback and the venue-specific fix

- "Only one benchmark family." Add a second problem class or justify the scope; an IJCAI
  cross-section reviewer distrusts single-suite claims.
- "Baseline is outdated." Cite and run a current top method; the broad PC notices stale
  comparisons.
- "Gains are within noise." Provide repeats, paired tests, or confidence intervals before the
  response, since no new results may be added later.

## Output format

```text
[Experiment readiness] strong / adequate / weak
[Claim -> evidence map] <claim: section/table/figure>
[Missing baseline or ablation] <item>
[Reproducibility gaps] <hyperparameters/seeds/compute/data/code>
[Decision-critical next run] <one experiment>
```
