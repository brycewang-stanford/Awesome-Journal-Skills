---
name: cav-experiments
description: Use when designing or auditing a CAV (Computer Aided Verification) empirical evaluation, covering standard benchmark sets (SV-COMP/SMT-COMP/HWMCC/VNN-COMP), fair baseline solvers with pinned versions and equal resource limits, timeout-dominated comparisons, soundness cross-checks and proof witnesses, cactus/scatter reporting, and matching evidence to the shape of each verification claim.
---

# CAV Experiments

Use this before submission when the evaluation is not yet locked. CAV reviewers are verification
researchers; the empirical section is where a good technique is won or lost. The organizing principle
is **evidence proportional to the claim** — the evaluation must test what the paper asserts, on
benchmarks and baselines a skeptic accepts, under a resource budget that makes the comparison fair.

## Evaluation audit

- **Match evidence to the claim shape.** A **soundness** claim needs a proof and/or a checkable
  witness, not a benchmark score. A **performance** claim needs a fair comparison on standard
  benchmarks under equal limits. A **capability** claim ("solves instances prior tools cannot") needs
  those instances and the prior tools actually run.
- **Use standard benchmark sets** at a **pinned revision** (SV-COMP, SMT-COMP, HWMCC, VNN-COMP, or a
  documented domain set). State the subset you ran and why; a hand-picked set invites the
  "cherry-picked" reject.
- **Choose fair baselines:** the strongest relevant prior tool(s), at their **latest released
  version**, run with a **documented, equal resource limit** (per-instance time and memory) on the
  same hardware. An outdated or mis-configured baseline is a scored weakness.
- **Respect that verification comparisons are timeout-dominated.** Report the limit explicitly;
  distinguish solved / unsolved / timeout / memout / error; and prefer **cactus plots** (instances
  solved vs. time) and **scatter plots** (per-instance head-to-head) over a single mean that a few
  timeouts distort.
- **Cross-check soundness.** Run a **differential check** against a trusted tool on all verdicts and
  report disagreements (ideally none); ship proof witnesses where correctness is the claim.
- **Design limits in, not on:** know before you run which logics, property classes, or sizes the
  method will not cover, and report them honestly.

## Claim-to-evidence design table

| Verification claim | Matching evidence | Reject pattern avoided |
|---|---|---|
| "Procedure is sound/complete" | Theorem + proof; witness + independent checker | "Soundness asserted, never checked" |
| "Faster than prior tool" | Standard set (pinned), latest baseline, equal limits, cactus+scatter | "Untuned/old baseline; unequal limits" |
| "Solves instances others cannot" | Those instances run on both tools, at the stated limit | "Only our tool was run on them" |
| "Scales to large systems" | Runtime/memory across realistic sizes; largest instance stated | "Only small inputs; 'large' undefined" |
| "General across a theory/domain" | A diverse benchmark sample + explicit out-of-scope classes | "One family, claimed universal" |

## Fair-comparison checklist (the reviewer's first objections)

```text
[Baseline]   latest released version? documented configuration? cited correctly?
[Limits]     identical per-instance time and memory for all tools? stated hardware and cores?
[Set]        standard benchmark set at a pinned revision? subset justified? instance list archived?
[Accounting] solved/unsolved/timeout/memout/error reported separately, not merged into one number?
[Soundness]  differential check across tools? disagreements reported? witnesses for UNSAT/verified?
[Variance]   for randomized/portfolio runs: seeds fixed, repetitions and variance reported?
```

## Reporting floor

- Report the **resource limit** with every runtime claim; a speed number without a timeout is
  meaningless.
- Use **cactus and/or scatter plots** for multi-instance comparisons; report how many instances each
  tool uniquely solved.
- State the **hardware, core count, and number of runs**; note any tool that errored or was excluded
  and why.

## Vignette: evaluating a model-checking technique

Suppose the paper claims a new abstraction lets a model checker verify properties prior tools time
out on. The matching plan: draw instances from a standard set at a pinned revision; run the new tool
and the strongest prior checker(s), at their latest versions, under one uniform time/memory limit on
stated hardware; report a cactus plot and a scatter plot, with solved/timeout/error broken out and
the uniquely-solved instances named; differential-check verdicts against a trusted checker; and state
the property classes and system sizes out of scope as declared limits — every number traceable to a
logged run in the artifact.

## Output format

```text
[Evaluation readiness] strong / adequate / weak
[Claim -> evidence map] <claim: benchmark set(revision)/baseline+version/limits, or proof+witness>
[Baseline fairness] <baseline -> latest version? equal limits? documented config?>
[Soundness check] <differential check + witnesses present? yes/no>
[Reporting] <cactus/scatter? solved/timeout/error separated? hardware+seeds stated?>
[Limits-by-design] <logic/property-class/size out of scope -> stated?>
[Decision-critical next run] <one experiment to add or fix>
```
