---
name: sigcomm-writing-style
description: Use when revising an ACM SIGCOMM paper for its house style — leading with measured operational pain, stating a design principle rather than a behavior, pairing every claim with testbed/trace/deployment evidence, reporting tails instead of superlatives, and fitting the argument into 12 figure-inclusive pages while keeping blinding clean.
---

# SIGCOMM Writing Style

Use this when revising the main paper. A SIGCOMM paper has to make a networking mechanism feel
inevitable: the reader should see the measured problem, the principle that solves it, and the
evidence that it works under real conditions — inside 12 pages where figures count. Reopen the
current CFP for format specifics.

## Revision rules

- **Lead with measured pain.** Put the operational cost in numbers on the first page — which
  percentile, how bad, under what traffic — not "congestion is a well-known problem." An
  asserted motivation is the first thing a SIGCOMM reviewer discounts.
- **Name the design principle.** State the invariant your mechanism defends, not just what it
  does. "Steer at the timescale congestion forms" is a principle; "avoids hotspots" is a
  behavior.
- **Pair every claim with evidence.** Each performance claim maps to a table, a figure, a
  sweep, or a documented break point — and the evidence lives on a testbed, trace, or
  deployment, not in simulation alone for a fabric claim.
- **Report the distribution.** Tails are usually the point in networking; give percentiles and
  variance over repeated trials, and hold the fair variable (throughput, load) fixed.
- **Spend the 12 pages on the spine.** Figures count against the cap, so every figure must earn
  its space; push depth to appendix and artifact without making the body incomplete.
- **Keep blinding clean.** Anonymize authorship *and* deployment identity — a named backbone
  plus a topology detail can deanonymize as surely as a byline.

## Sentence-level rewrites

| Draft pattern | SIGCOMM-safe rewrite |
|---|---|
| "significantly improves performance" | "cuts 99th-percentile FCT by 2.4x at matched throughput" |
| "congestion is a serious problem" | "incast inflates P99 short-flow FCT by 3.1x on our testbed" |
| "our system avoids hotspots" | "reroutes flowlets on instantaneous backlog, so response tracks queue buildup" |
| "outperforms in most cases" | claim scoped to the workloads and topologies actually tested |
| "we evaluate in simulation" | "we measure on a 128-server testbed replaying a production trace" |

## Structure discipline

- The first page carries problem, principle, mechanism, and headline evidence; a reviewer
  should be able to accept-or-reject on the first page and have the rest confirm it.
- Every declarative claim near a number is something a reviewer may try to reproduce; do not
  write a sentence you cannot back with a run.
- Separate what you **measured** from what you **designed** from what you **conjecture**;
  mixing an unproven stability claim into a measured-result paragraph is a credibility leak.
- Motivate with measurement, then build the mechanism; the "measurement motivates mechanism"
  arc (as in VL2) reads as native SIGCOMM.

## Vignette: compressing into 12 figure-inclusive pages

A draft with eight figures and a sprawling background section: keep the measured-motivation
figure and the two decision-critical tail plots in the body, fold three micro-benchmarks into
one multi-panel figure, move two sweeps to an appendix with forward references, and compress
background into contribution contrasts. The test of a good cut: a reviewer reconstructs the
whole argument from the body alone, and no surviving figure is decorative.

## Output format

```text
[Writing diagnosis] clear / under-motivated / behavior-not-principle / mean-only / overloaded
[First-page fix] <measured pain + principle + headline evidence>
[Claim discipline] <claim -> table / figure / sweep / break point>
[Tail reporting] <percentiles + variance + fixed fair variable>
[Compression cuts] <merge / move / delete>
[Anonymity edits] <authorship + deployment phrases to neutralize>
```
