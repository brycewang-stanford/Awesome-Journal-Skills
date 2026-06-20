---
name: agsy-review-process
description: Use to understand how Agricultural Systems (AgSy) evaluates a manuscript — single-anonymized peer review with a minimum of two reviewers and an editor decision, desk screening for fit and systems content, what reviewers weigh, and the rapid-review track for Perspectives. Sets expectations and shapes the paper to survive review; it does not contact editors.
---

# Review Process (agsy-review-process)

Knowing how AgSy screens and decides lets you pre-empt the failure modes before submitting. AgSy is
**single anonymized** (reviewers see the authors), screens for **fit and genuine systems content**, and
sends suitable papers to a **minimum of two expert reviewers**; the **editor** makes the decision.
Source-map process facts were refreshed from ScienceDirect on 2026-06-20; live-check them before a
real upload because review wording and submission links can change.

## When to trigger

- Before submitting, to stress-test against desk-rejection and reviewer concerns
- Deciding whether a piece fits the **Perspective** (rapid-review) track
- Interpreting a decision letter and setting expectations
- Understanding what systems reviewers are likely to weigh

## How AgSy review works

1. **Single anonymized.** Reviewers know the authors; authors do not know reviewers. There is no
   manuscript anonymization step (unlike a double-anonymous journal).
2. **Editor screening / desk decision.** Editors screen for **scope and fit** first — is this a
   **systems** paper (interactions, hierarchical levels, modelling, trade-offs), and does it have the
   substantive natural-science + interaction content AgSy requires? Single-factor field trials and
   black-box model demos are common desk rejections.
3. **External review.** Suitable submissions go to a **minimum of two** expert reviewers for
   independent assessment of scientific quality.
4. **Decision.** Accept / minor or major revision / reject — taken by the **journal's editors**.
5. **Perspective rapid review.** **Perspective** articles undergo a **rapid** review process for a short
   submission-to-publication time; authors should consult editors before submitting a Perspective where
   the Guide requires it.

## What systems reviewers weigh

- Is there a **real systems question** (interactions, trade-offs), or a dressed-up single-factor study?
- Is the **model described, justified, and calibrated**, with an **independent evaluation**?
- Are **sensitivity and uncertainty** characterized?
- Are **trade-offs** surfaced and the **decision relevance** clear?
- Are **data, code, and the model** shareable (Elsevier research-data policy)?

## Shape the paper to pass

- Make the systems question explicit up front (avoids a "not a systems paper" desk rejection).
- Describe and evaluate the model properly (avoids the "black box" reviewer objection).
- Surface trade-offs and decision relevance (avoids "no clear application").
- Have data/code/model deposit ready (avoids a late reproducibility hold).

## Desk-screen gate (what trips the early decision)

Before external review, the editor screens for fit and substance. Map your submission to the gate:

- *Systems content present?* If the only "interaction" is a treatment effect, it reads as a field trial
  — a common fit desk rejection.
- *Model assessable?* A black-box model (no version, calibration, or evaluation) cannot be reviewed and
  is screened out or returned.
- *Decision relevance visible?* If the "so what for a decision" is absent, expect "no clear application."
- *Track correct?* A full study in the Perspective slot, or a Perspective padded to a paper, is a
  type/length mismatch caught early.

## Referee pushback → the AgSy-specific fix

- *"This is a dressed-up single-factor study."* → Make the interaction and trade-off explicit up front
  (see `agsy-systems-framing-and-modeling`).
- *"The model is a black box."* → Describe, justify, and independently evaluate it before review.
- *"Where is the uncertainty?"* → Add sensitivity and uncertainty analysis to the conclusion-bearing
  outputs.

## Anti-patterns

- Submitting a single-factor field trial to a systems journal (fit desk rejection)
- A model with no calibration/evaluation, sensitivity, or uncertainty
- Expecting double-anonymous handling — AgSy is single anonymized
- Treating a Perspective as a full research paper (wrong track and length)


## Review-risk pass for Agricultural Systems

Run this as a concrete capability pass. First lock the system boundary, actor decision, model/data linkage, and sustainability or food-security tradeoff; then test whether the manuscript addresses agricultural-systems reviewers who expect crop, farm, value-chain, environment, and policy components to be connected rather than listed.

- **Primary move:** Turn likely reviewer objections into a ledger with response evidence, manuscript location, and the decision-maker who must be convinced first.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against Field Crops Research for plot-level agronomy, Global Food Security for policy synthesis, Agricultural Economics for economics-first work; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Fit check】genuine systems question (interactions/trade-offs)? [Y/N]
【Model rigor】described + calibrated + independently evaluated? [Y/N]
【Sensitivity/uncertainty】characterized? [Y/N]
【Decision relevance】trade-offs + application clear? [Y/N]
【Track】standard vs Perspective (rapid review)
【Realistic outcome】reject / major / minor / (rare) accept
【Next】agsy-submission (or agsy-revision-and-rebuttal if decided)
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — peer-review model, reviewer count, editor decision, rapid review for Perspectives
