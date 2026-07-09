---
name: recsys-author-response
description: Use when drafting an ACM RecSys rebuttal during the author-response window, covering the short narrative RecSys allows, anonymity, anchoring answers to submitted evidence and the anonymous repository, the recurring objections about untuned baselines, leakage, and offline-online gaps, and Senior-PC-focused clarification.
---

# RecSys Author Response

Use this after RecSys reviews are released and the rebuttal window opens. RecSys runs a brief
author-response phase (2026: June 4-9) in which authors add a short narrative to clarify
misconceptions. Reopen the current instructions before drafting — the length and mechanics are
cycle-specific and the phase is short.

## Triage

- Answer concerns that move the decision: correctness, recommendation novelty, evaluation
  validity, reproducibility, and fit.
- Use **already-submitted** evidence — paper sections, tables, ablations, the appendix, and the
  anonymous repository. The rebuttal clarifies; it does not add a new experiment the reviewers
  cannot see.
- Keep the reply anonymous: no institution, platform, deployed-system name, or repository owner.
- Correct factual misreadings first, then address requested comparisons, tuning details, or
  uncertainty that the paper already supports.
- Do not paste new result tables the reviewers had no chance to vet; point to what exists.

## Drafting pattern

1. State the decision-critical correction or concession in the first line.
2. Point to the exact submitted evidence (table, figure, appendix section, repository path).
3. Explain the recommendation consequence — what it means for the ranking claim or deployment.
4. Promise a camera-ready wording fix only where it adds no unsupported new claim.

## Recommender-reviewer pushback patterns

| Pushback | What it signals | RecSys-ready fix |
|---|---|---|
| "Were the baselines tuned as hard as your method?" | The reviewer read the 2019 reproducibility literature | Point to the equal-budget tuning grid in the appendix and the per-baseline selected settings; never wave it off as "standard config" |
| "This is a random split on sequential data" | Suspected temporal leakage | Confirm the temporal/leave-one-last protocol and where it is stated, or concede and scope the claim |
| "Offline nDCG gains may not deploy" | The offline-online gap objection | Anchor to the off-policy estimate, the simulator, or an A/B result; if you have none, scope the claim to offline |
| "Metrics look sampled, not full-ranking" | Sampled-metric distortion suspected | State whether ranking is over the full item set and the cutoff, or report the full-ranking number |
| "Missing the obvious matrix-factorization baseline" | A weak-comparison gap | Anchor to the appendix comparison, or concede a camera-ready addition |

## Response micro-example

Reviewer objection: the Recall@20 gain probably vanishes against a properly tuned baseline.
Reply skeleton:

1. Concede the concern is the right one to raise.
2. Point to Appendix C, where every baseline is tuned on the same grid with the same budget, and
   the selected hyperparameters are listed.
3. Note the gain persists after tuning (Table 1) and the ablation (Table 2) isolates the
   mechanism.
4. Offer one camera-ready sentence making the equal-budget protocol explicit in the main text.

## Rebuttal calibration

- One decision-critical point per reviewer beats an exhaustive line-by-line reply; the Senior PC
  reads for whether the central evaluation objection was actually resolved.
- Reply early — RecSys rebuttal windows are short and a precise early narrative outweighs a late
  comprehensive one.
- Length and formatting norms vary by cycle; recheck the current author-response instructions
  before sending.

## Output format

```text
[Priority issue] <reviewer concern>
[Decision dimension] correctness / novelty / evaluation validity / reproducibility / fit
[Draft response] <RecSys-ready anonymous narrative>
[Evidence anchor] <table / figure / appendix / repository path>
[Forbidden content removed] <identity leaks, unseen new results, unsupported claims>
```
