---
name: sigmetrics-writing-style
description: Use when revising an ACM SIGMETRICS paper for a rigorously stated performance contribution on the first page, explicit modeling assumptions and their validity, theorems paired with numerical/empirical validation, evidence proportional to the claim, double-anonymous wording, and disciplined use of the 20-page single-column acmsmall budget.
---

# SIGMETRICS Writing Style

Use this when revising the main paper. SIGMETRICS papers are POMACS journal articles read by
performance-evaluation specialists, so they need a **precise performance contribution stated on the
first page** and claims a reviewer can *check*. The failure this skill prevents is a paper that
reads like a systems demo (numbers, no model) or a theory paper with no systems relevance
(theorems, no validation).

## Revision rules

- **Lead with the performance contribution, stated rigorously:** the systems-performance problem, a
  precise metric (mean vs. tail latency, throughput, regret, energy), why current models/policies
  fall short, the contribution (a model, policy, methodology — ideally with a proven bound), the
  validation, and what changes for real systems.
- **State assumptions where the result uses them.** A theorem is only as strong as its assumptions;
  name the arrival process, service distribution, independence, and stationarity your result needs,
  and show they are plausible for the target system. Hidden assumptions are the fastest reject.
- **Pair every quantitative claim with proportional evidence** — a proof for an analytic claim, a
  simulation whose curve matches the analysis, confidence intervals over repeated runs, effect
  sizes for a comparison — not adjectives.
- **Validate the model against measurement.** The SIGMETRICS signature move is showing that the
  analytic prediction and the measured/simulated data agree; a theorem with no validation, or a
  measurement with no model, is half a paper.
- **Respect the 20-page acmsmall budget as a design constraint.** References are unlimited, but body
  text, figures, and in-body appendices are not. A paper that only fits by shrinking the assumptions
  or the validation is over-scoped.
- **Maintain double-anonymity** in self-citations, system names, trace provenance, and
  acknowledgements (except in the Operational Systems Track).

## Performance-evaluation paper skeleton

| Section | Job it must do | Common failure |
|---|---|---|
| Intro | Problem, precise metric, inadequacy, contribution, validation preview, systems payoff — first page | Leads with a trend and "improves performance," no metric or model |
| Model / System | The model and its **assumptions**, stated precisely and justified | Assumptions hidden or unjustified against the real workload |
| Analysis | Theorems/bounds with proofs (full proofs in an appendix) | A claimed bound with a hand-waved or incomplete proof |
| Validation | Analysis-vs-simulation agreement; measurement of the real system | A plot with no analytic comparison, or no confidence intervals |
| Evaluation | Baselines, fairly tuned; the systems payoff on real workloads | Untuned baseline; toy inputs; benchmark score as the whole result |
| Assumption validity / threats | Where assumptions hold and where they are stressed | Deferred or absent; no estimation-error / robustness discussion |

## Sentence-level rewrites

| Draft pattern | SIGMETRICS-safe rewrite |
|---|---|
| "Our policy significantly improves performance." | "reduces p99 latency by X% (95% CI ...) over <tuned baseline> on <workload>, matching Thm. 1" |
| "We assume the standard queueing model." | "We assume M/G/1 with service-time distribution fit to the trace (§5.1, QQ-plot Fig. 6)" |
| "The bound holds in general." | "Thm. 1 holds under assumptions A1-A3; §6 quantifies degradation when A2 is violated" |
| "Simulation confirms our approach." | "the analytic p99 curve lies within the simulated confidence intervals across three distributions (Fig. 4)" |
| "State-of-the-art results." | Claim scoped to the metric, workload, and regime actually analyzed and measured |

## Assumption-and-validation discipline

```text
[Assumptions] list each (arrival, service, independence, stationarity); justify against the target
[Analysis]    prove the bound; put full derivations in an appendix within the reviewed pages
[Validation]  overlay analysis on simulation/measurement; report CIs and number of runs
[Robustness]  quantify what happens when an assumption is stressed (estimation error, heavy tails)
-> a theorem, its assumptions, and its validation are one unit -- present them together
```

## Vignette: compressing a proof-plus-measurement paper

A draft with three theorems, a long simulator description, and a sprawling measurement section: keep
all three theorem statements and their assumptions in the body, move full proofs to an appendix with
forward references, keep the one figure showing analysis-vs-simulation agreement and the table with
the trace-driven payoff, and cut redundant simulator detail to the artifact. The test of a good cut:
a reviewer should be able to answer "what is claimed, under what assumptions, and does the
measurement back it?" from the body alone.

## Output format

```text
[Writing diagnosis] clear / under-specified-assumptions / unvalidated / over-claimed / over-scoped
[First-page fix] <new framing leading with the precise performance contribution>
[Assumption audit] <assumption -> stated? justified against workload? where used?>
[Validation fix] <theorem/claim -> analysis-vs-measurement evidence to add>
[Anonymity edits] <system names / self-citations / trace provenance to rewrite>
```
