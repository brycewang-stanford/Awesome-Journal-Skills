---
name: eer-referee-strategy
description: Use when anticipating the objections a European Economic Review (EER) referee will raise — under single-anonymized review across any field — and pre-empting them before submission. Maps likely pushback to fixes; it does not draft the response letter (use eer-rebuttal after a decision).
---

# Referee Strategy (eer-referee-strategy)

## When to trigger

- The paper is near-complete and you want to pre-empt predictable referee objections
- You are unsure who the likely referees are and what they will attack
- An editor desk-screen risk needs reducing (breadth/novelty/fit)
- Before submission, to convert anticipated objections into in-paper defenses

## The EER referee reality

EER review is **single-anonymized**: the referee sees who the authors are. The referee is typically an **expert in your exact design or field** and frequently **someone you cite**. Two gates precede them: an **editor desk-screen** (out-of-scope or low-novelty papers are rejected without review, and the **submission fee is non-refundable**), then **≥2 external referees** for an independent assessment (检索于 2026-06；以官网为准). The first decision is usually fast; the strategic move is to **pre-empt the predictable objections in the paper itself** so a referee has less to grab.

## Map objection → pre-emption

| Likely objection | Pre-emption (where it lives) |
|------------------|------------------------------|
| "Not general interest / too narrow" | breadth hook on page one (`eer-topic-selection`, `eer-writing-style`) |
| "Contribution is incremental / already known" | named frontier delta + concurrent-work distinction (`eer-literature-positioning`) |
| "Identification is not credible" | design-appropriate estimator + key-assumption defense (`eer-identification`) |
| "TWFE is biased here" | heterogeneity-robust DiD + flat leads (`eer-identification`) |
| "Exclusion restriction is assumed, not defended" | theory + institutions + falsification (`eer-identification`) |
| "Result is fragile / spec-dependent" | coefficient-stability battery (`eer-robustness`) |
| "Inference ignores clustering/dependence" | correct clustering + wild bootstrap / dependence-robust SEs (`eer-robustness`) |
| "Model is decorative" | model delivers the tested comparative static (`eer-theory-model`) |
| "Can't reproduce this" | replication package ready + data statement (`eer-replication-package`) |
| "Exhibits unreadable / stars instead of SEs" | one headline table with SEs (`eer-tables-figures`) |

## Strategy moves

1. **Pre-empt the top three objections in the paper**, not just the response letter — a referee who finds the answer already there has less to demand.
2. **Write for the cited referee**: be accurate and fair to the literature; do not dismiss the person likely refereeing you.
3. **Reduce desk-screen risk**: make breadth and novelty unmissable in the abstract and first paragraph.
4. **Pre-build the robustness/identification appendix** the obvious referee will ask for, and signal it in-text.
5. **Keep claims calibrated** — overclaiming is the fastest route to a hostile report.

## Checklist

- [ ] Top 3 likely objections listed, each with where it is pre-empted in the paper
- [ ] Breadth + novelty visible enough to survive the editor desk-screen
- [ ] Identification/robustness defenses already in the draft (not deferred to rebuttal)
- [ ] Literature treatment fair and accurate (referee may be a cited author)
- [ ] Claims calibrated to evidence; no overselling
- [ ] Replication materials ready to disarm a reproducibility objection

## Anti-patterns

- Assuming anonymity and writing dismissively about the likely referee's own work
- Saving every defense for the rebuttal instead of pre-empting in the paper
- Submitting a marginal-fit paper and losing the non-refundable fee to a desk reject
- Overclaiming and handing the referee an easy "the evidence does not support this"
- Ignoring an obvious robustness test the field referee will certainly request

## Worked vignette (illustrative)

A finance paper anticipates three objections: (1) "endogenous treatment" → adds an IV with a defended exclusion and a placebo; (2) "driven by the crisis years" → leave-out-period robustness in-text; (3) "incremental vs. paper X" → a sentence naming exactly how it relaxes X's key assumption. All three are answered *in the submitted paper*. When the report arrives, the referee's main asks are already addressed, shortening the R&R.

## Output format

```
【Likely referee profile】field/design expert; possibly cited author
【Top 3 objections】each + where pre-empted in the paper
【Desk-screen risk】breadth/novelty visible up front? [Y/N]
【Pre-built defenses】identification/robustness/replication ready? [Y/N]
【Claim calibration】matched to evidence? [Y/N]
【Next step】eer-submission (preflight) → eer-rebuttal (after decision)
```
