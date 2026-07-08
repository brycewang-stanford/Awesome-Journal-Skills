---
name: usenixsec-experiments
description: Use when designing or auditing the evaluation of a USENIX Security Symposium paper — building threat-model-faithful experiments, adaptive-attacker analysis for defenses, false-positive and vantage-point rigor for detection and measurement, ethical experimentation on live systems, and honest baselines.
---

# USENIX Security Experiments

The evaluation is where USENIX Security papers are won or lost, and the committee
reads it as an adversary would: looking for the experiment you did not run because
it would have hurt. This skill audits security evaluations against the venue's
specific rigor bars. It pairs with `usenixsec-reproducibility` (making runs
regenerable) and `usenixsec-writing-style` (reporting them).

## Match the experiment to the claim type

| Claim type | The experiment reviewers demand | The usual gap |
|---|---|---|
| Attack | End-to-end demonstration on a realistic target, success rate over trials | Works only in a toy setup; success rate is one lucky run |
| Defense | **Adaptive** attacker who knows the defense, plus overhead | Evaluated only against the original, non-adaptive attack |
| Detection | Detection rate **and** false-positive rate on realistic base rates | FPR measured on a clean dataset, not deployment traffic |
| Measurement | Cross-vantage / cross-time validity of the finding | Single vantage, single snapshot, over-generalized |
| System/protocol | Correctness + performance vs a credible baseline | Baseline is a strawman or an unoptimized reimplementation |

The recurring failure is the **non-adaptive defense evaluation**. A defense that
stops the attack it was designed against proves little; reviewers want the attacker
who adapts to the defense, and its absence is the single most common reason a
technically sound defense paper is rejected here.

## The base-rate discipline for detection

Detection and classification results live or die on realistic base rates. A 99%
detection rate with a 1% false-positive rate is useless at internet scale where
benign events outnumber malicious ones a million to one. Report:

- TPR and FPR separately, never a single "accuracy" that hides class imbalance.
- The base rate of the deployment you claim, and the resulting precision at that
  base rate (the base-rate fallacy is a named reviewer objection).
- ROC/PR behavior across thresholds, not one operating point chosen after the fact.

```python
# Precision at deployment base rate — the number a security reviewer recomputes
def precision_at_base_rate(tpr, fpr, base_rate):
    tp = tpr * base_rate
    fp = fpr * (1 - base_rate)
    return tp / (tp + fp) if (tp + fp) else float("nan")

# 99% TPR, 1% FPR sounds great; at 1-in-100k malicious it is nearly worthless:
print(precision_at_base_rate(0.99, 0.01, 1e-5))   # ~0.00099
```

## Statistical honesty for stochastic security results

Fuzzing, randomized attacks, timing side channels, and ML pipelines are all
nondeterministic. The venue expects distributions, not anecdotes:

- Repeat campaigns; report count, median, and dispersion (IQR or CI), not a max.
- For "our fuzzer finds more bugs," control the compute budget and report
  bug-discovery over time across seeds, with a rank test for significance.
- Timing/side-channel claims need enough traces to bound noise, and the analysis
  should survive a skeptic recomputing the statistic from released traces.

## Experimenting on live systems, ethically

Much USENIX Security evaluation touches real networks, real users, or real
devices. The evaluation design and the Ethical Considerations appendix must agree:

1. **Scanning/measurement**: rate-limit, honor opt-out and blocklists, use
   dedicated hosts with informative reverse DNS and a project page. Report these
   controls in the methodology, not only the appendix.
2. **Human subjects**: IRB approval or a documented equivalent; if the work would
   need IRB elsewhere and you lack one, say so and describe your safeguards — the
   ethics guidelines call for exactly this.
3. **Vulnerability testing**: prefer owned or authorized targets; for
   found-in-the-wild flaws, disclose before publishing and state the timeline.
4. **Data handling**: minimize collection, protect any PII, and delete per the
   stated plan. A reviewer who spots avoidable harm can sink the paper on ethics
   alone, independent of the science.

## Baselines and ablations that hold up

- Compare against the **state of the art**, reimplemented faithfully or run from
  released artifacts; a beaten strawman invites a reject.
- Ablate the components you claim matter — a "our key insight is X" claim needs the
  variant without X.
- Include the honest negative space: regimes where the attack fails or the defense
  is too costly. Reviewers here read omission as concealment.

## Pre-submission evaluation audit

1. Every claim mapped to an experiment; every experiment to a threat-model
   assumption it respects.
2. Defenses: adaptive-attacker experiment present and genuinely adaptive.
3. Detection: FPR at realistic base rate, precision computed.
4. Stochastic results: repetitions and dispersion reported.
5. Live-system work: ethical controls in both methodology and appendix.
6. Baselines current; ablations cover the claimed-critical parts.

## Reverify each cycle

- Any evaluation-reporting checklist the current CFP adds (待核实 for '27).
- Current ethics-guidelines wording on live experiments and human subjects.

## Output format

```text
[Claim-experiment map] each claim → experiment → threat-model consistency
[Adaptive check] defense evaluated against an adaptive attacker: yes/no
[Base-rate check] FPR + precision at deployment base rate reported: yes/no
[Statistics] repetitions + dispersion for stochastic results
[Ethics] live-system controls in methodology and appendix aligned
[Gaps] ordered fix list before submission
```
