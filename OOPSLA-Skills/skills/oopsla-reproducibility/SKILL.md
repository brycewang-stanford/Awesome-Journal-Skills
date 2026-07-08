---
name: oopsla-reproducibility
description: Use when hardening an OOPSLA paper's empirical claims to the SIGPLAN Empirical Evaluation Guidelines — managed-runtime measurement discipline, warmup and variance reporting, corpus and benchmark provenance, environment pinning, and a Data-Availability Statement that the eventual artifact can actually honor.
---

# OOPSLA Reproducibility

OOPSLA carries a particular historical burden here: the venue itself
published the papers showing that sloppy runtime measurement produces wrong
conclusions — Georges, Buytaert & Eeckhout's statistical-rigor paper (OOPSLA
2007) and the DaCapo suite's methodology argument (OOPSLA 2006); see
`resources/exemplars/library.md`. Reviewers steeped in that lineage apply the
SIGPLAN Empirical Evaluation Guidelines
(`sigplan.org/Resources/EmpiricalEvaluation/`) as a working checklist, and
the two-round model gives them a Minor/Major Revision lever to demand rigor
rather than merely complain about it. Reproducibility work done before
Round N is cheaper than the revision it preempts.

## The four guideline pillars, operationalized

| Pillar | Reviewer question | Concrete obligation in the paper |
| --- | --- | --- |
| Clear claims | What exactly is asserted, on what workloads, on what hardware? | Claims scoped with population, platform, and configuration |
| Suitable comparison | Is the baseline the strongest sensible one, correctly configured? | Baseline versions, flags, and tuning documented |
| Principled benchmarks | Why these programs/corpora and not cherry-picked ones? | Selection rule stated; exclusions listed with reasons |
| Adequate data analysis | Do the numbers separate signal from noise? | Repetitions, warmup policy, dispersion, and summary statistic all named |

## Managed-runtime and PL-specific traps

- **JIT warmup**: steady-state and startup are different claims; measure and
  label both or pick one explicitly.
- **Nondeterministic compilation**: JIT tiering, GC scheduling, and ASLR mean
  run-to-run variance is structural — report distributions, not best-of.
- **Geometric vs arithmetic means** across benchmarks: choose deliberately
  and say why; ratios of means and means of ratios diverge.
- **Corpus studies** (the Meyerovich–Rabkin lane): repository selection bias,
  fork/duplicate contamination, and time-of-scrape all belong in the paper,
  since the corpus *is* the instrument.
- **Mechanized proofs**: state the proof assistant version, axioms/assumed
  lemmas, and which theorems are checked vs paper-only.

## Reproducibility ledger

Keep one machine-readable ledger from the first experiment; it becomes the
artifact's spine and the Data-Availability Statement's evidence.

```yaml
experiment: table3-throughput
runtime: OpenJDK 21.0.2 (Temurin), -Xmx16g, JIT default
hardware: 2x Xeon 6338, 256 GiB, SMT off, governor=performance
benchmarks: dacapo-23.11-chopin subset (selection rule: R1)
protocol: 30 invocations x 10 iterations, discard warmup by CUSUM
stats: geomean ratio + 95% bootstrap CI, per-benchmark violin in appendix
seed_policy: fixed seeds logged; randomized order per invocation
data: raw CSV -> artifact path /results/table3/
```

## Statement discipline

The Data-Availability Statement (required before the references —
`oopsla-submission`) is a promissory note the artifact must later redeem
under badge review (`oopsla-artifact-evaluation`). Write it from the ledger:
name what is included, what is excluded and why (license, privacy, scale),
and on what hardware results were produced. A statement that overpromises is
worse than a modest one — evaluators check.

## Pre-round self-audit

1. Re-derive every headline number from the ledger with one command.
2. Delete one machine from the picture: does any claim silently depend on
   unstated hardware?
3. Hand a labmate the guidelines' four pillars and the PDF; each pillar they
   cannot check off in the text is a revision demand waiting to be written.

## Output format

```text
[Pillar audit] claims/comparison/benchmarks/analysis: pass|gap each
[Runtime traps] <warmup, variance, mean-choice, corpus, proofs — issues found>
[Ledger] complete / missing fields: <list>
[Statement] redeemable as written: yes / overpromises: <items>
[Revision exposure] what a reviewer could demand in Round N+1
```
