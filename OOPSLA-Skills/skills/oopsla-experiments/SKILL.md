---
name: oopsla-experiments
description: Use when designing or auditing the evaluation of an OOPSLA paper — matching evidence type to claim type across the venue's spread (benchmarks, corpus studies, case studies, user studies, mechanized proofs), building baselines and workloads that survive the SIGPLAN checklist, and sizing experiments to the round calendar.
---

# OOPSLA Experiments

OOPSLA's evaluation question is not "is there a big table?" but "does the
evidence *type* match the claim *type*?" The venue's published scope runs
from mathematical formalisms to empirical studies, and its exemplars span
benchmark suites, measurement methodology, corpus mining, and language
experience reports (`resources/exemplars/library.md`) — so the first design
act is choosing the right instrument, and the second is executing it to the
SIGPLAN Empirical Evaluation Guidelines standard that reviewers apply
checklist-in-hand (`oopsla-reproducibility` operationalizes the pillars).

## Claim-type → evidence-type routing

| Claim type | Primary evidence | Common OOPSLA failure |
| --- | --- | --- |
| "Faster / cheaper" | Benchmarks vs strongest baseline, variance reported | Weak baseline; startup vs steady-state conflated |
| "More expressive / safer" | Formal result + programs witnessing the boundary | Expressiveness asserted by example only |
| "Programmers benefit" | User study or field data with a design | Anecdote from the authors' own use |
| "Occurs in practice" | Corpus study with stated selection rule | Convenience sample of famous repos |
| "The design generalizes" | Second instantiation (language/runtime/domain) | Single-host generalization claims |
| "Semantics is right" | Mechanization or proofs + conformance tests | Calculus untethered from the implementation |

A paper may need two rows; it rarely supports five. Cutting a claim is
cheaper than defending its missing evidence through a Major Revision.

## Baselines and workloads that survive scrutiny

- The baseline is what a skeptical expert would actually use today, tuned the
  way its own paper tunes it — document versions and flags in the paper.
- Workload selection needs a *rule* (suite version, corpus filter, sampling
  frame) stated before results; exclusions listed with reasons. Curated-only
  workload sets are the most quietly fatal reviewer finding.
- For LLM-era tooling claims, hold out for contamination: date-split corpora,
  and report sensitivity to prompt/configuration where relevant.
- Negative controls: include a configuration where your mechanism should
  *not* help and show that it doesn't. Nothing signals honesty faster.

## Sizing experiments to the round calendar

The two-round system changes experimental economics. Between an R1 verdict
and the R2 resubmission there are only months, so:

```text
Design now, before Round N:
  - matrix of runs a reviewer could plausibly demand (extra baseline,
    larger corpus, second platform) with wall-clock + hardware cost each
  - keep the harness parameterized so a demanded cell is a config change
  - archive raw results per run (the ledger of oopsla-reproducibility)
Payoff: a Minor Revision executes in days; a Major Revision's
expectation list maps to known cells instead of new engineering.
```

## Analysis floor

- Repetition counts, warmup handling, and dispersion (CI or IQR) for every
  performance number; significance or effect size where comparisons are the
  claim.
- Summaries chosen deliberately (geomean for ratios) and stated.
- Human-subject work: sample size rationale, task design, and ethics/IRB
  status — the venue takes the human-aspects lane seriously enough to review
  it by social-science norms.
- Case studies report failures encountered, not only successes; an
  experience report with zero friction reads as marketing
  (`oopsla-writing-style`).

## Output format

```text
[Routing] claim → evidence rows used + mismatches found
[Baseline audit] strongest-sensible test: pass / gaps
[Workload rule] stated / absent; exclusions justified: yes/no
[Demand matrix] anticipated reviewer demands with cost estimates
[Analysis floor] repetitions/dispersion/summary-statistic compliance
```
