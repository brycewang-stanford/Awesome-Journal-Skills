---
name: imfer-referee-strategy
description: Use when anticipating the objections a dual academic/policy IMF Economic Review (IMFER) referee will raise, so a manuscript pre-empts them before submission or addresses them in revision. Plans the defense; it does not draft the response letter (imfer-rebuttal) or run the submission preflight (imfer-submission).
---

# Referee Strategy (imfer-referee-strategy)

## When to trigger

- The paper is near submission and you want to stress-test it against the referees it will draw
- You must decide which robustness/identification checks to run *before* submitting vs. hold in reserve
- An R&R arrived and you must map referee concerns to concrete responses
- You want to understand how IMFER's double-blind, dual-audience review shapes strategy

## How IMFER review works (plan around it)

IMFER uses **double-blind review** through Editorial Manager (anonymize the main file and self-citations) (检索于 2026-06；以官网为准). The distinctive feature is the **referee pool**: typically one frontier international-macro researcher *and* readers attuned to **policy relevance and IMF-program realism**. The modal report attacks (1) the **credibility of the cross-country / policy-surprise design**, then (2) **country composition and external validity**, then (3) **whether the policy implication is actually warranted**. A clean estimate with an over-reached or under-developed policy claim is a common rejection. Plan to **pre-empt the predictable objections in the paper** and reserve the letter for genuinely new asks.

| Referee objection (by type) | Pre-emption to build in now |
|-----------------------------|-----------------------------|
| "TWFE is biased under staggered policy adoption" | heterogeneity-robust estimator + clean event-study leads already in the paper |
| "Driven by a few countries / one region" | leave-one-country-out and drop-dominant in the main paper |
| "This is the global financial cycle, not your variable" | global-cycle / US-shock control shown to leave the result intact |
| "Policy is endogenous to the crisis" | external instrument / narrative timing + selection-into-program defense |
| "Spillovers violate SUTVA across borders" | explicit interference assumption or a network/spatial design |
| "Inference ignores cross-country dependence" | Driscoll–Kraay / two-way clustering; wild-cluster for few countries |
| "Effect ≠ the policy-relevant magnitude" | estimand stated; magnitude in policy units; scope of the implication bounded |
| "The policy implication overreaches the evidence" | implication explicitly bounded to what the design supports |
| "Not reproducible / restricted data" | package built with access instructions (`imfer-replication-package`) |
| "External validity beyond this sample?" | estimand + scope stated; the regime where the result transfers is named |

### Triaging which checks to run before vs. after
Not every conceivable check belongs in the submitted paper. Run *before submission* the checks a referee is near-certain to demand — the country-composition tests, the global-cycle control, the modern staggered-DID estimator, the cross-country-robust inference — because their absence reads as a hole. Hold *in reserve* the secondary perturbations (alternative deflators, additional subsamples, a placebo or two) that you can deploy in the response letter if asked, so the submitted paper stays readable. The judgment call is the boundary: anything an IMFER referee would consider a *threat to the headline* goes in now; anything that is merely a "would be nice" can wait. Putting reserve checks in an online appendix you reference is the safe middle path.

## Strategy craft

1. **War-game the design.** For each identifying assumption, write the sentence a hostile referee would use; if you cannot answer it in one paragraph + one exhibit, fix it before submission.
2. **War-game the policy claim.** IMFER's distinctive risk is the *policy* referee: state exactly what the finding licenses and what it does not.
3. **Lead with composition.** Put leave-one-country-out and the global-cycle control in the main paper — these are the first things an IMFER referee checks.
4. **Pre-empt, do not hide** the obvious weakness; referees punish papers that ignore the elephant.
5. **Make reproducibility visible** so the restricted-data concern is defused before it is raised.

## Checklist

- [ ] Main file and self-citations anonymized for double-blind review
- [ ] Each identifying assumption has a hostile-referee sentence and a one-paragraph+one-exhibit answer
- [ ] Country-composition checks (leave-one-out, drop-dominant) in the main paper
- [ ] Global financial cycle / common-shock confound pre-empted
- [ ] Policy-endogeneity and selection-into-program addressed
- [ ] Decisive checks placed in the main paper; reserve checks held for the letter or online appendix
- [ ] Estimand + policy magnitude + scope of the implication stated to pre-empt the policy referee
- [ ] The policy claim is bounded to what the evidence supports (no overreach)
- [ ] External validity / transfer regime named to pre-empt the guaranteed scope question
- [ ] Reproducibility package referenced so restricted-data suspicion is defused

## Anti-patterns

- Ignoring the obvious design weakness and hoping no referee notices
- Leaving identifiers/self-citations that break double-blind anonymity
- Over-reaching the policy implication — the fastest way to lose the policy referee
- No country-composition checks when one economy obviously dominates
- Treating the global financial cycle as someone else's problem
- Leaving the replication package as an acceptance-time afterthought
- Writing for the academic referee only and forgetting the paper will also be read for program realism
- Dumping every reserve check into the main text so the paper becomes unreadable
- Assuming an international-macro referee will not notice mis-specified cross-country inference

## Worked vignette (illustrative)

Before submitting a debt-spillover paper, the team war-games both tracks. The academic sentence: "Your event windows overlap the GFC, so you are picking up the global shock." Pre-emption: drop the GFC window and add a global-cycle control in the main paper. The policy sentence: "You claim restructurings should be faster, but your sample is all post-default — survivorship." Pre-emption: re-scope the implication to defaulting countries and add a selection-into-default note. Each objection gets one paragraph plus one exhibit *in the paper*, so the actual reports raise only genuinely new points.

## Referee pushback mapped to the pre-emption

- *"This is the global financial cycle, not your variable."* → Show the global-cycle control and the dropped-crisis window in the main text before a referee asks.
- *"The policy claim overreaches."* → State the estimand and bound the implication to the regime the design covers.
- *"Restricted data — can this be reproduced?"* → Reference the built package with access instructions so the suspicion never forms.

## Output format

```text
【Journal】IMF Economic Review
【Skill】imfer-referee-strategy
【Anonymization】main file + self-cites blinded? [Y/N]
【Design objection map】per assumption: [objection → pre-emption in paper]
【Composition checks】leave-one-out / drop-dominant in main paper? [Y/N]
【Common-shock】global-cycle control shown? [Y/N]
【Policy claim】estimand + magnitude stated; implication bounded? [Y/N]
【Reproducibility visible】package referenced? [Y/N]
【Next step】imfer-submission
```
