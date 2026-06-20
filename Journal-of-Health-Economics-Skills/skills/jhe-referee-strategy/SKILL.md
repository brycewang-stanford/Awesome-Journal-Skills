---
name: jhe-referee-strategy
description: Use when pre-morteming a Journal of Health Economics (JHE) manuscript against the objections its health-economist referees raise before submission. Anticipates and disarms likely pushback; it does not draft the response letter after a decision (jhe-rebuttal) or run the submission preflight.
---

# Referee Strategy (jhe-referee-strategy)

## When to trigger

- The paper is near-final and you want to find the objections before a referee does
- You suspect a specific weakness (selection, concurrent policy, overclaiming) a health economist will name
- You are choosing what to put in the main text versus the appendix to pre-empt pushback
- You want to write the introduction so it answers the first question a JHE referee will ask

## Who reviews at JHE and how

Review is **single-anonymized** (referees know the authors; you do not know them) and suitable papers typically go to **at least two reviewers** for independent expert assessment (检索于 2026-06；以官网为准). The referees are **health economists** — they hold the field's canonical results and the institutional facts of the program/market you study. The implication for strategy: you cannot hide behind anonymity, and you cannot bluff institutions. Anticipate the *health-econ-specific* objection, not the generic one, and answer it in the paper before it is asked.

## The JHE referee pre-mortem (objections in the order they arrive)

| Likely objection | Pre-empt by |
|------------------|-------------|
| "This is selection, not the effect you claim" | model/bound the selection; show take-up vs. crowd-out vs. moral hazard separately |
| "Your policy variation is confounded by a concurrent reform" | placebo on ineligible group/period; rule out simultaneous reforms explicitly in the institutional section |
| "Staggered DiD here is biased" | heterogeneity-robust estimator + event-study leads + honest-DID bound already in the main text |
| "A coverage/utilization effect is not a welfare effect" | add the demand-and-cost model that maps utilization to welfare; do not overclaim |
| "Health spending is skewed; OLS is wrong" | defended two-part/GLM estimator with the zero mass shown |
| "Few states; your SEs are too small" | wild-cluster bootstrap / randomization inference, clustering at the policy level |
| "This belongs in AJHE / Health Economics / JPubE" | sharpen the health-econ contribution and the boundary in the intro |
| "Your data cannot be reproduced" | honest DAS + shared code + access path (jhe-replication-package) |

## How to use the pre-mortem

1. **Rank the objections by how fatal they are**, and put the defense to the top one or two in the **main text**, not the appendix.
2. **Write the introduction to answer the first objection** — if selection is the obvious worry, the intro should already gesture at how you handle it.
3. **Pre-place the diagnostic exhibit.** If a referee will ask for an event-study or a placebo, it should already be Figure 2.
4. **Name the sibling-journal reroute risk** and disarm it with the contribution framing, so no referee suggests "send it elsewhere."
5. **Suggest referees thoughtfully** if the system allows: experts who know the institution will judge the design fairly; avoid only methodologists who will miss the health-policy stakes.

## Checklist

- [ ] The two most fatal objections are identified and answered in the main text
- [ ] Selection and concurrent-policy threats are pre-empted, not left for the referee
- [ ] Staggered-bias and few-cluster inference are handled before submission
- [ ] Welfare claims are matched to what the design identifies (no overreach to invite the obvious objection)
- [ ] The sibling-journal reroute risk is disarmed by the contribution framing
- [ ] The introduction answers the first question a health economist will ask
- [ ] Reproducibility objection pre-empted with an honest DAS and shared code
- [ ] Suggested referees (if allowed) know the institution, not only the method

## Handoff boundary

This skill is a pre-submission pre-mortem; it anticipates objections and decides what to pre-place where. It is not the post-decision response letter (`jhe-rebuttal`) and it does not run the analysis that answers an objection — route a flagged gap to `jhe-identification`, `jhe-robustness`, or `jhe-theory-model` first, then come back to decide placement. When the pre-mortem is clean and the defenses are in the main text, hand off to `jhe-submission`.

## Anti-patterns

- Burying the defense to the most likely objection in an appendix a referee may not reach
- Pre-empting generic econometric worries while ignoring the health-econ-specific one (selection, institutions)
- Overclaiming welfare and then hoping no referee notices
- Ignoring the few-state inference problem until a referee forces it
- Treating single-anonymized review as if institutions could be glossed over

## Main-text vs. appendix: what to pre-place where

The single highest-leverage referee-strategy decision is **what earns a place in the main text**. Put in the main text anything a referee needs to *believe the design*; demote to the appendix anything that merely reassures. At JHE that means: the heterogeneity-robust estimate, the key placebo/falsification, the selection bound, and the headline distribution figure belong in the body — the controls sweep, alternative bandwidths, and secondary outcomes go to the online appendix. A defense a referee cannot find is a defense that does not exist.

## Reading two referees who disagree

With ≥2 health-economist reviewers, disagreement is common and is **not yours to adjudicate by majority** — the editor's letter does that. When you anticipate conflict (one wants a structural model, one wants reduced-form transparency), prepare a framing that serves both: a reduced-form headline with a model in support, each labeled for what it identifies. Pre-empting the conflict in the paper's structure is better than trying to win it in the response letter later.

## Worked vignette (illustrative)

Before submitting a hospital-payment-reform paper, the pre-mortem flags the two fatal objections: patient selection (sicker patients sort to reformed hospitals) and a concurrent quality-reporting mandate. Rather than wait, the authors move the selection bound (Oster δ) and the placebo on the unreformed service line into the main text as Table 3 and Figure 2, add a paragraph in the institutional section ruling out the simultaneous mandate by timing, and frame the contribution as a provider-incentive result (not a generic policy evaluation) to forestall a "send to AJHE" suggestion. The first referee's likely two questions are answered before they are asked.

## Output format

```text
【Journal】Journal of Health Economics
【Skill】jhe-referee-strategy
【Review model】single-anonymized; ≥2 reviewers (检索于 2026-06；以官网为准)
【Top objections (ranked)】1) ... 2) ... 3) ...
【Pre-empts in main text】[which defense goes where]
【Welfare/scope discipline】claim matched to design? [Y/N]
【Reroute risk disarmed】vs. AJHE / Health Economics / JPubE? [Y/N]
【Next skill】jhe-submission
```

## A quick self-test before you stop

Read your own introduction as the harshest health economist you know. If you can name the objection you would raise and it is not answered by the end of the paper's main text, the pre-mortem is not finished. The goal is that the first two questions a referee writes are questions you have already answered in figures and tables they can find — not questions you are hoping they will not ask.
