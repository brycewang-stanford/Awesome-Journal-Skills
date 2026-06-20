---
name: jbes-literature-positioning
description: Use when positioning a Journal of Business & Economic Statistics (JBES) methods paper against prior econometric and statistical methods. Stakes what is new relative to the existing toolkit; it does not write a standalone literature survey.
---

# Literature Positioning (jbes-literature-positioning)

## When to trigger

- A referee will ask "how is this different from method X already in the literature?"
- The contribution relative to the closest existing estimator/test/algorithm is fuzzy
- You are unsure whether your improvement is incremental or genuinely new
- You need to map your method onto the right strand (time series, panel, GMM, ML, Bayesian, etc.)

## Why positioning is the methods-paper crux at JBES

JBES referees are method experts: they judge a paper first by **what it adds to the existing toolkit**. Because the journal explicitly welcomes **adaptation of methods from machine learning and data science** alongside classical econometrics, your closest competitors may live in **two literatures at once** — the statistics/ML method you adapt *and* the econometric problem you apply it to. Position against **both**. The contribution must be stated as a delta against named prior methods, not as a freestanding survey: which assumptions you relax, which rates you improve, which computational barrier you remove, or which empirical setting prior methods cannot handle.

## Positioning protocol

1. **Name the incumbents.** List the 3–6 methods a referee would consider state of the art for your problem (estimator, test, or algorithm — with citations).
2. **State your delta per incumbent.** For each: weaker assumptions? better asymptotics/rates? valid under dependence/heavy tails/high dimension where they are not? faster/feasible at scale? Honest deltas only.
3. **Locate the strand.** Place the paper in its method family (e.g., HAC inference, GMM, factor models, quantile methods, debiased ML, Bayesian computation) so referees from that strand recognize the lineage.
4. **Bridge to the application.** Tie the methodological delta to the empirical payoff: the new method changes a substantive conclusion or makes a previously infeasible analysis feasible.
5. **Concede gracefully.** Where an incumbent dominates (simpler, or better in a regime you do not target), say so; over-claiming invites a hostile report.

## Checklist

- [ ] 3–6 closest prior methods named and cited
- [ ] A concrete delta stated against each (assumptions / rates / robustness / computation)
- [ ] Both the statistics/ML side and the econometrics side covered if you adapt across fields
- [ ] The method family / strand is explicit
- [ ] The positioning connects to the empirical payoff, not just abstract properties
- [ ] Limitations vs. incumbents conceded honestly

## Anti-patterns

- A chronological survey ("Smith (1990) did..., Jones (1995) did...") with no delta
- Comparing only to a strawman or to outdated methods, ignoring the current frontier
- Claiming novelty against econometrics while missing the identical idea in the statistics/ML literature (or vice versa)
- Vague superiority ("our method performs better") with no stated dimension of improvement
- Hiding the regime where an existing method still wins

## Worked vignette: positioning a debiased-ML estimator across two literatures

A hypothetical JBES paper adapts double/debiased machine learning to estimate a heterogeneous treatment effect of credit-score thresholds on default, using bank loan-level data (figures **illustrative**). Because the idea lives in two literatures at once, the positioning must hit both. On the statistics/ML side the closest prior work is cross-fitted DML and causal forests; the delta is a dependence-robust cross-fitting scheme valid under the within-branch clustering of loan data, which iid DML ignores. On the econometrics side the incumbents are series/sieve semiparametric estimators; the delta is an illustrative 30% RMSE reduction at the same nominal coverage when nuisance dimension is high. The paper concedes that plain DML still wins under independence and low nuisance dimension — naming where an incumbent dominates pre-empts a hostile report. The delta then ties to the application: it changes which credit-score band shows the largest effect.

## Referee-pushback patterns on positioning (venue-specific fixes)

| JBES referee objection | Fix this skill enforces |
|----|----|
| "This already exists in the statistics/ML literature." | Position against both fields; name the ML method you adapt and the econometric incumbent |
| "A chronological survey, not a delta." | Replace the timeline with a per-incumbent statement of assumptions/rates/robustness improved |
| "Vague claim that the method performs better." | State the dimension and magnitude of improvement against a named incumbent |

Calibration anchor (hedged): JBES welcomes machine-learning and data-science adaptations, so your
nearest competitor often sits **outside** econometrics — missing the identical idea in statistics/ML
invites the sharpest rejection.

## Output format

```
【Incumbents】[3–6 prior methods + citations]
【Delta per incumbent】method → what you improve (assumptions/rates/robustness/computation)
【Strand】method family this paper joins
【Cross-field check】statistics/ML side AND econometrics side covered? [Y/N]
【Empirical payoff】how the delta changes a substantive result
【Conceded】where incumbents still win: ...
【Next step】jbes-contribution-framing
```
