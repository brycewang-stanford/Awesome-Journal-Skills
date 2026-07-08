---
name: wsdm-experiments
description: Use when designing or auditing the evaluation of a WSDM paper - offline ranking and recommendation metrics with bias controls, temporal-split protocols for interaction logs, baseline selection from recent WSDM/SIGIR/KDD editions, ablations that isolate the mechanism, efficiency reporting, and online-evidence framing.
---

# WSDM Experiments

Design an evaluation that survives WSDM's mixed academic-industry PC with no
rebuttal to patch holes. The venue's evaluation culture is specific: reviewers
assume interaction data is biased until you control for it, assume random
splits leak until you say "temporal," and assume unnamed baselines were chosen
to lose. Build the section so each assumption meets its answer.

## The evidence quadrants

Cover the four questions every strong WSDM evaluation answers; weak papers
usually max one quadrant and ignore two:

| Quadrant | Question | Typical instruments |
|---|---|---|
| Effectiveness | Better on the task? | nDCG/MRR/MAP@k, Recall/HR@k, AUC/logloss for CTR |
| Validity | Better for the claimed reason, or an artifact? | Bias controls, leakage checks, ablations |
| Efficiency | Affordable at serving time? | Latency, throughput, index/memory cost, training compute |
| Robustness | Where does it break? | Cold-start slices, head/tail splits, temporal drift, adversarial cases |

Effectiveness without validity is the classic WSDM rejection ("gains may be
position-bias artifacts"); effectiveness without efficiency loses the industry
reviewer for interactive-serving claims.

## Protocol decisions to fix before running anything

1. **Split by time, and say so.** Interaction data demands temporal splits;
   document window boundaries and whether users span splits (see the manifest
   pattern in `wsdm-reproducibility`). If you must use a legacy
   leave-one-out protocol for comparability, run temporal as well and report
   both - protocols disagree often enough that the choice is a finding.
2. **Define the candidate set.** Sampled-negative evaluation (rank the true
   item against k sampled items) inflates and reorders metrics versus full
   ranking; state which you use and sample size. Mixing regimes across
   baselines invalidates the whole table.
3. **Fix the cutoff story.** Report metrics at cutoffs that match the claimed
   surface (@5/@10 for user-facing ranking; deeper cutoffs need justification).
4. **Pick the unit of significance.** Paired tests over queries/users/sessions,
   with the unit named. State the correction if testing many baselines.

## Baseline selection

- Include the strongest recent method from the venue's own conversation - a
  2027 submission compared only against pre-2023 baselines self-identifies as
  under-researched. Sweep the last two editions of WSDM, SIGIR, KDD, WWW, and
  RecSys for the topic's current best.
- Include the embarrassing-simple baseline (popularity, BM25, most-recent,
  logistic regression on hand features). WSDM reviewers are veterans of neural
  methods losing to tuned heuristics; showing the heuristic beaten builds
  trust, and omitting it suggests it wasn't.
- Tune baselines with the same budget as your method and say so - "default
  hyperparameters for baselines" is a read-and-reject phrase for this PC.
- For foundation-model comparisons, pin versions and dates and control the
  prompt-engineering effort across systems.

## Ablations that isolate the mechanism

The contribution sentence names a mechanism; the ablation table must isolate
it. Pattern:

```text
Full model                                    0.412
- remove the debiasing weight (the mechanism) 0.371  <- the claim's evidence
- remove auxiliary loss (engineering)         0.405
- replace learned propensity with uniform     0.383
Strongest baseline                            0.379
```

If removing the named mechanism hurts less than removing an engineering
detail, the paper's story and its evidence disagree - fix the story or the
method before a reviewer does it for you. Report ablations on more than one
dataset when results are close; single-dataset ablations invite the "tuned on
that set" read.

## Efficiency and scale reporting

For any method aimed at ranking, retrieval, or serving:

- Report inference latency per query/user at a stated batch size and hardware,
  plus index or memory footprint next to effectiveness numbers.
- Separate one-time costs (training, index build) from per-request costs.
- Scale claims need a scaling curve (data or corpus size vs cost/quality), not
  an adjective. "Web-scale" with a 100k-item experiment is a tells-table entry
  in `wsdm-writing-style` for a reason.

## Online and production evidence

A/B results strengthen a WSDM paper when framed correctly: they are
*attested* evidence of deployment value (traffic share, duration, metric
definitions, guardrails - the protocol requirements in `wsdm-reproducibility`),
not a substitute for reproducible offline comparison. The clean pattern pairs
them: offline tables establish the method ranking on inspectable data; the
online section shows the offline win survived serving reality. State
discrepancies between the two honestly - the offline-online gap is itself a
finding this community values.

## Pre-submission experiment audit

```text
[ ] Temporal (or justified) splits, documented, leakage checks run
[ ] Candidate-set regime stated and uniform across systems
[ ] Baselines: recent-strong + simple-heuristic, tuning parity stated
[ ] Significance: paired test, named unit, cutoff-matched claims
[ ] Ablation isolates the *named* mechanism, multi-dataset if close
[ ] Efficiency: latency/memory beside effectiveness for serving claims
[ ] Robustness slice: cold-start or tail reported, not just aggregate
[ ] Every number in the abstract traceable to a table
```

## Output format

```text
[Quadrants] effectiveness / validity / efficiency / robustness: covered or gap
[Protocol] split, candidate set, cutoffs, significance unit: <summary>
[Baselines] recency + simplicity + tuning parity: pass / additions needed
[Mechanism ablation] isolates claim: yes / story-evidence mismatch
[Online evidence] attested framing correct: yes / no / n-a
[Fix-first] the single highest-risk evaluation gap
```
