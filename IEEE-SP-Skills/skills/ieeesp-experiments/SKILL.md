---
name: ieeesp-experiments
description: Use when designing or auditing the evaluation of an IEEE S&P (Oakland) paper, including end-to-end attack demonstration, adaptive-adversary evaluation of defenses, measurement sampling and validity, baselines and ablations, statistical reporting of attack success, and the ethics constraints that shape what experiments are permissible.
---

# IEEE S&P Experiments

Use this to build or audit the evidence an S&P paper stands on. The venue's
reviewers are professional adversaries; an evaluation that would satisfy a
systems or ML PC often leaves an Oakland reviewer's central question — "does
this survive a real, adaptive attacker?" — unanswered.

## Match the evaluation to the contribution type

| Contribution | Evaluation that closes the loop | Fatal gap |
|---|---|---|
| Attack | End-to-end demonstration against a realistic, current target | Toy target; unrealistic preconditions |
| Defense | Adaptive adversary who knows the design; cost/overhead | Only non-adaptive or prior attacks |
| Measurement | Representative sampling + validation + ethics | Convenience sample presented as population |
| System | Security property demonstrated *and* performance | Property asserted, not tested |
| SoK | Systematic re-analysis under one framework | Cherry-picked coverage |

## The adaptive-adversary rule dominates defense papers

A defense evaluated only against existing or non-adaptive attacks is the most
common S&P defense rejection. The standard:

- Define the adaptive adversary explicitly: knows the mechanism, the
  parameters, and the deployment.
- Show your defense against attacks *designed to break it*, not just
  yesterday's attacks it happens to stop.
- Report the cost of adaptation for the attacker and the overhead for the
  defender — both are part of the security claim.
- If a class of adaptive attack is out of scope, say so in the threat model
  and own the boundary; do not leave it for a reviewer to discover.

## Measurement validity is an evidence question and an ethics question

For measurement papers, the sampling story and the ethics story are the same
paragraph in reviewers' minds:

- State the population, the frame, and the sampling method; quantify coverage
  and bias.
- Validate a subsample by an independent method where possible.
- Active measurement (scanning, probing) must respect opt-out norms, rate
  limits, and the ethics record (`ieeesp-review-process`) — an experiment
  that harms the systems it measures is a reject regardless of results.
- Human-subjects components need IRB determination *before* running, not a
  post-hoc note.

## Statistics for attacks and fuzzing

Security evidence is often probabilistic and gets held to a real bar:

```text
Attack-success reporting:
  n trials (state n) · success rate ± dispersion · target set described
  → "worked" without n is an anecdote, not a result

Fuzzing / bug-finding comparison (the field's known pitfalls):
  - equal budgets (CPU-time, not wall-clock)
  - ≥ 5–10 campaigns per configuration; report variance
  - identical seed corpora across compared tools
  - a ground-truth or triage method for "unique" bugs
  → a single-run bug count comparison is not evidence of superiority

Timing / side-channel:
  noise floor stated · machine quiescence (isolated cores, freq pinning)
  · distinguisher's statistical test named
```

## Baselines and ablations Oakland reviewers ask for

- The **strongest** prior attack/defense, at its best configuration, not a
  weakened reimplementation.
- An ablation isolating the component you claim is responsible for the
  security gain.
- A cost baseline: what does the attacker/defender spend, and is it
  realistic at the claimed scale?
- Negative results where they bound the claim (attack fails against target
  class Y — state it; it strengthens the scoped claim).

## Ethics as an experimental design constraint, not an afterthought

Some experiments are simply not runnable as first imagined:

- Testing an exploit against live third-party systems without authorization
  is out; build a representative testbed instead.
- Collecting user data beyond what the IRB and the ethics record cover is
  out.
- Disclosure timing constrains *when* certain measurements can be published
  — design the timeline so the evidence and the fix do not collide
  (`ieeesp-reproducibility`).

## Audit worksheet

```text
For each experiment:
  claim it supports | contribution type | adaptive adversary evaluated? |
  strongest baseline used? | n trials + dispersion | ethics clearance |
  realistic target? | rerunnable? (→ ieeesp-reproducibility)
Flag any row with: non-adaptive-only defense · anecdotal success rate ·
  weakened baseline · unmet ethics precondition
```

## Output format

```text
[Contribution type] attack / defense / measurement / system / SoK
[Loop closed?] <the demonstration/eval that proves the claim> ✓/✗
[Adaptive adversary] evaluated ✓/✗/n-a — scope stated?
[Baselines] strongest prior used ✓/✗ · ablation ✓/✗ · cost baseline ✓/✗
[Statistics] trials+dispersion ✓/✗ · fuzzing pitfalls avoided ✓/✗/n-a
[Ethics preconditions] IRB ✓/✗/n-a · authorization ✓/✗ · disclosure timing ok ✓/✗
```
