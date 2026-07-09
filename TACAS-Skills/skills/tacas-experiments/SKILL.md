---
name: tacas-experiments
description: Use when designing or auditing a TACAS (ETAPS) evaluation, covering shared verification benchmarks (SV-COMP-style task sets), fair baseline configuration and equal time budgets, honest wall-clock/scalability reporting on stated hardware, soundness checking of results, reproducibility on the clean artifact VM, and how a TACAS tool-paper evaluation differs from a SV-COMP competition entry.
---

# TACAS Experiments

Use this before submission when the empirical story is not yet locked. TACAS reviewers are
verification experts, and the evaluation is where a tool or algorithm is won or lost. The organizing
principle is **honest, reproducible comparison**: the experiment must test the claim on **shared
benchmarks**, against a **fairly configured baseline**, with every number **reproducible in the
artifact** (mandatory for tool papers).

## Evaluation audit

- **Use community benchmarks.** Draw tasks from established suites (e.g., SV-COMP task sets, model-
  checking or SMT benchmark libraries, prior tool distributions) rather than a private set of
  favourable inputs. A benchmark nobody else uses invites the "cherry-picked" reject.
- **Configure baselines fairly.** Compare against the **strongest available** competing tool, with a
  **documented, equal time and memory budget** on the **same hardware**. An untuned or crippled
  baseline is a scored weakness, and reviewers often know the baseline's authors.
- **Report the right quantities.** Solved/unsolved counts, wall-clock time with the **timeout stated**,
  memory, and the largest instance handled — not a single ratio. State the machine (CPU, RAM) and the
  number of repetitions for any variance.
- **Check your results for soundness.** Verification tools can be fast because they are wrong: report
  how you validated answers (cross-checking against a reference tool, witness validation, known
  expected verdicts), and disclose any incorrect results rather than hiding them.
- **Reproduce in the artifact.** Every table and figure must regenerate from a script in the artifact
  on the **clean ETAPS VM**; a tool paper whose numbers cannot be reproduced fails the mandatory
  artifact evaluation and endangers the paper.
- **Bound external validity.** Say which languages, property classes, or system sizes the results
  cover, and name the ones they do not.

## Claim-to-evidence design table

| Verification claim | Matching evidence | Reject pattern avoided |
|---|---|---|
| "Verifies more tasks than prior tools" | Solved counts on a shared benchmark set vs a tuned baseline, equal timeout | "Evaluated on our own examples only" |
| "Faster / more scalable" | Wall-clock and memory across realistic sizes, hardware stated | "Speedup ratio with no timeout or machine given" |
| "Finds real bugs" | Reproducible counterexamples/witnesses on real code, validated | "Warnings with no confirmed true positives" |
| "Sound (or sound up to k)" | Correctness argument + no incorrect verdicts on a validation set | "Fast because it silently under-approximates" |
| "General technique" | Multiple property classes / languages + stated limits | "One benchmark family, claimed universal" |

## Fair-comparison checklist

```text
[Baseline]    strongest competitor, latest version, cited; not a straw man
[Budget]      identical timeout and memory limit for every tool; state them
[Hardware]    one machine, described; note any parallelism and core counts
[Tasks]       a named, shared benchmark set; report per-category, not just totals
[Validation]  answers cross-checked / witnesses validated; incorrect results disclosed
[Determinism] fix seeds/options; report variance across repetitions where relevant
```

## SV-COMP vs a TACAS tool-paper evaluation

TACAS **hosts SV-COMP**, but a competition entry and a tool-paper evaluation are different
deliverables — do not conflate them:

- **SV-COMP** runs your verifier on the **common task set** under the organizers' harness and rules,
  and reports a ranked, uniform comparison across all participants; your contribution is a short
  competition paper plus a conforming tool.
- **A tool paper** is peer-reviewed prose making a **specific claim** about your tool, evaluated on
  benchmarks *you* justify, judged on contribution and a reproducible artifact — not on a
  leaderboard position. You may *use* SV-COMP benchmarks in a tool paper, but cite them and keep the
  comparison fair and reproducible.

## Vignette: evaluating a new model checker

Suppose the paper claims a new checker verifies more C tasks than the prior tool. The matching plan:
take a shared C benchmark set (with categories), run both tools with an identical timeout and memory
limit on one stated machine, report per-category solved/unsolved and wall-clock, **validate**
verdicts (cross-check disagreements, validate violation witnesses), disclose any wrong answers,
state which property classes are out of scope, and ship a clean-VM artifact whose scripts regenerate
every table.

## Reporting floor

- Machine description, timeout, and memory limit for every experiment.
- Per-benchmark or per-category results, not only aggregate totals.
- A soundness/validation statement and honest disclosure of incorrect results.
- Artifact scripts that regenerate each table/figure on the ETAPS VM.

## Output format

```text
[Evaluation readiness] strong / adequate / weak
[Claim -> evidence map] <claim: benchmark set / metric / baseline>
[Baseline fairness] <baseline -> latest? equal budget? same hardware? documented?>
[Soundness] <validation method; any incorrect results disclosed? yes/no>
[Reproducibility] <every number regenerates on the clean VM? yes/no>
[Decision-critical next run] <one experiment or validation to add>
```
