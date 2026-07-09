---
name: ppopp-writing-style
description: Use when drafting or tightening a PPoPP paper's prose and structure, covering the two-column acmart sigplan layout, the 10-page text+figures budget, stating the concurrency-correctness and scalability claim up front, presenting speedup curves and core sweeps, and the parallel-programming conventions PPoPP reviewers expect.
---

# PPoPP Writing Style

Write to the PPoPP bar: a parallel-programming contribution that is **correct under concurrency and
measurably scalable**, presented in **two-column `acmart` `sigplan`** within **10 pages** of text
and figures (references unlimited). The reader is a parallel-systems expert who will look for the
speedup curve, the baseline, and the correctness argument before they finish the introduction.

## The first-page contract

By the end of page 1 a PPoPP reviewer should know:

1. **The parallel-programming problem** — what breaks or stalls when you go parallel (contention, a
   sequential bottleneck, poor locality, divergence, a memory-model hazard).
2. **The contribution** — the structure, runtime, algorithm, or technique, in one sentence, framed
   so parallelism is clearly the point (not a compiler pass or a proof in disguise).
3. **The twin claim** — that it is correct under concurrency *and* how much it scales, with the
   headline number ("linear to 96 cores," "1.8× over the state-of-the-art lock-free map at 64
   threads").
4. **The evidence shape** — the hardware, the workloads, and the baseline you beat.

A PPoPP introduction that describes a mechanism but never states a scaling number, or that promises
correctness without naming the concurrency hazard it handles, reads as unfinished.

## Two-column, 10-page discipline

- The two-column `acmart` layout is unforgiving of wide figures. Speedup plots, roofline charts,
  and code listings must fit one column or span both deliberately — plan figure placement early.
- **10 pages of text and figures**; references are free, so cite fully (all authors, no "et al.").
  Do not pad the body with material that belongs in the artifact (`ppopp-supplementary`).
- Recover space by cutting prose, merging plots (small multiples of a core sweep beat five separate
  charts), and pushing full sweeps to the artifact — never by shrinking the template.

## Structure that fits the venue

```text
1  Introduction        problem -> contribution -> twin claim (correctness + scaling) -> evidence
2  Background/Model    the concurrency model, memory model, and hardware assumptions you rely on
3  Design              the structure/runtime/algorithm; where parallelism is exposed and bounded
4  Correctness         the argument: linearizability/progress, race-freedom, or a checked property
5  Implementation      what a reader needs to reproduce: pinning, allocation, topology awareness
6  Evaluation          speedup curves, core/GPU sweeps, NUMA effects, variance, baselines
7  Related work        delta-first against the nearest parallel-programming competitor
8  Conclusion
```

Sections 4 and 6 are the twin load-bearing walls: skip the correctness argument and a reviewer
distrusts the speedups; skip the sweep and they distrust the correctness claim's relevance.

## Presenting parallel performance

- **Show the curve, not one point.** Report throughput/speedup as a function of thread or core
  count; a single configuration hides where you saturate or collapse.
- **Name the baseline and the machine in the caption.** "Speedup over <named competitor> on a
  2-socket 96-core node" — an unlabeled y-axis or an unnamed baseline invites a reject.
- **Show variance.** Repeated runs with error bars; a bar chart of single runs reads as noise.
- **Be honest about where it stops scaling.** A paper that explains its saturation point is
  stronger than one that hides it behind a truncated x-axis.

## Language conventions

- Prefer precise concurrency vocabulary: linearizable, lock-free vs. wait-free, quiescent
  consistency, false sharing, memory-order (acquire/release/seq_cst), work-span, strong vs. weak
  scaling. Reviewers read imprecision here as inexperience.
- Distinguish **strong scaling** (fixed problem, more cores) from **weak scaling** (problem grows
  with cores) explicitly; conflating them is a classic PPoPP tell.
- State the memory model you assume (C/C++11, the GPU model, hardware TSO) rather than leaving it
  implicit.

## Common PPoPP writing failures

- **A mechanism with no number** — design described lovingly, scaling never quantified.
- **A number with no machine** — speedups whose hardware and baseline are unstated.
- **Correctness by testing** — "no data race observed" without an argument over interleavings.
- **Strawman baselines** — beating your own unoptimized code instead of the real competitor.
- **Wide figures that overflow the column** — a two-column layout problem, caught at compile time.

## Output format

```text
[First-page contract] problem / contribution / twin claim (correctness+scaling) / evidence — all present?
[Format] two-column acmart sigplan, <=10 pages text+figs, refs full (no et al.)?
[Correctness] hazard named + argument (linearizability/progress/race-freedom)? yes/no
[Scaling] curve over cores/GPU, named baseline, named machine, variance shown? yes/no
[Cut list] prose/figures to trim or move to the artifact to hit 10 pages
```
