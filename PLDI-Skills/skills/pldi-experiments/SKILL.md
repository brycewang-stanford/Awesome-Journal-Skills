---
name: pldi-experiments
description: Use when designing or auditing a PLDI evaluation — choosing defensible benchmark suites and baseline compiler configurations, measuring runtime, compile time, and memory with warmup and variance discipline, running ablations that isolate the claimed mechanism, and scoping claims to the platforms measured.
---

# PLDI Experiments

A PLDI evaluation answers one question: *does the claimed mechanism cause the
claimed effect on programs that matter?* Everything in the design flows from
making that causal link auditable. The community's shared rubric is SIGPLAN's
Empirical Evaluation checklist (see `pldi-reproducibility` for the measurement
hygiene); this skill covers the design choices above the hygiene layer.

## Benchmark choice is an argument, not a default

- **Justify the suite** relative to the claim: an allocation optimizer needs
  allocation-heavy programs *and* allocation-light ones (to show no regression);
  a parser-facing analysis needs real grammars, not microbenchmarks.
- **Use community suites where they exist** and state versions; add real-world
  applications when the suite is known to under-represent your phenomenon.
- **List exclusions with reasons.** "We exclude two SPEC programs that use
  `setjmp`, which our restriction rejects (§4.4)" builds trust; silent dropping
  destroys it.
- **Include programs your technique should *not* help.** Flat results on those
  are evidence the instrument works.

## Baselines that survive the PC

| Weak move | Defensible move |
|---|---|
| Compare against -O0 or an untuned build | Strongest published configuration of the standard toolchain (state version + flags) |
| Reimplement a rival technique quickly | Use the authors' artifact where one exists; note deviations |
| Compare only against your own prior system | Add the external baseline reviewers will name in review |
| Report best-of-N runs | Report distribution over all N runs |
| One aggregate number | Aggregate + per-benchmark table, so wins and losses show |

The reviewers most likely to be assigned your paper wrote the baselines. Assume
the baseline's author reads your flags line.

## Ablations isolate the mechanism

The claim "our escape signatures cause the speedup" needs the experiment where
signatures are replaced by the prior summary while everything else stays fixed.
Design one ablation per mechanism named in the contributions list; a mechanism
with no ablation is a mechanism the paper does not actually test.

## The three currencies

Runtime, compile time, and memory are all first-class at PLDI. A technique that
buys 1.1x runtime with 3x compile time must say so in the abstract, not in a
footnote. Report all three, each with repetitions and dispersion, even when one
of them is "no change" — especially when it is "no change."

## Anticipated-objection pass

Run this list before the deadline; it is roughly what a PLDI review's evaluation
section says when it goes badly:

```text
[ ] Is the delta bigger than the noise band? (CI overlap check per benchmark)
[ ] Does the effect survive on a second microarchitecture?
[ ] Are the flags/version of every baseline stated and current?
[ ] Is there a benchmark where we lose, and do we explain it?
[ ] Does the ablation exist for every mechanism we claim credit for?
[ ] Is warmup/steady-state handling stated per benchmark family?
[ ] Could the speedup come from an unrelated engineering change? (same-codebase control)
```

## Negative and neutral results

A paragraph explaining the two programs where the technique regresses — with a
cause, not a shrug — routinely appears in accepted PLDI papers and in
Distinguished Paper profiles. Reviewers read it as instrument calibration.
Deleting the losing rows reads as the opposite.

## Output format

```text
[Suite] chosen + justified? versions pinned? exclusions listed?
[Baselines] strongest config? external baseline present? flags stated?
[Ablations] mechanism -> ablation experiment (n/n covered)
[Currencies] runtime / compile time / memory each measured with variance?
[Objection pass] items failing from the checklist above
```
