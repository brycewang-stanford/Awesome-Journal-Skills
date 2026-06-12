---
name: mgsci-contribution-framing
description: Use when writing the explicit contribution statement for a Management Science (INFORMS) manuscript — turning an analytical result or empirical finding into a decision-relevant insight that travels across departments, and showing why it belongs in Management Science rather than a sister INFORMS journal. It frames the "so what"; it does not run the analysis (mgsci-data-analysis) or position the literature (mgsci-literature-positioning).
---

# Contribution Framing (mgsci-contribution-framing)

## When to trigger

- Results exist but the "so what for management decisions" is implicit or thin
- A Department Editor or reviewer questioned the magnitude or the fit of the contribution
- The paper reads as a correct model or a clean finding with no generalizable insight
- You need the contribution sentences for the intro and the discussion

## The Management Science contribution test

Management Science's unifying bar is **rigor plus a demonstrated contribution to management/business decision-making that travels across departments**. A correct proof or a clean estimate is necessary but not sufficient — the paper must say, in plain words, **what decision-relevant insight is now available that was not before**, and why it matters beyond a single niche.

Write the contribution on three axes:

1. **What is new.** The specific result — a new optimal policy / equilibrium property / identified causal effect / mechanism — stated as a claim, not a topic.
2. **Why it is decision-relevant.** Which managerial or policy decision changes, and in which direction, because of it. This is the "managerial science" core; an insight no decision-maker would act on is off-mission.
3. **Why it travels.** What a reader in a *different* Department learns from it. Cross-department reach is what distinguishes a Management Science contribution from one better suited to a focused sister journal.

## Make the fit case explicit

Because ambiguous-fit papers are discussed across the editorial team and many are redirected, frame the contribution so the home **Department** is obvious *and* the cross-department payoff is stated. If your result speaks to operations *and* finance, or to a behavioral mechanism *and* a market outcome, say so — that breadth is the argument for Management Science over Operations Research, M&SOM, or Marketing Science.

## Calibrate magnitude honestly

- **Analytical:** state the insight the comparative statics deliver, and be candid about the assumptions it rests on.
- **Empirical:** report effect sizes and practical magnitude, not just significance; discuss what would and would not generalize.
- Avoid overclaiming; a precisely bounded contribution is more credible than an inflated one.

## Anti-patterns

- A discussion that restates results without naming a decision that changes.
- "Contribution" framed only as filling a gap, with no insight that travels.
- Overclaiming generality the model or data cannot support.
- Burying the contribution sentence so the editor has to guess the Department and the payoff.


## Department-fit worked call (illustrative)

A draft estimates how algorithmic work-assignment on a gig platform changes courier retention, using a platform policy change for identification.

- **Weak framing:** "We study gig platforms and retention." No Department, no decision, no insight that travels.
- **Management Science framing:** "Exposing couriers to algorithmic reassignment raises 90-day attrition by ~6 percentage points (illustrative); the mechanism is perceived loss of control, and the lever is how much schedule autonomy the platform concedes." This names a decision (autonomy in algorithmic management), a mechanism that travels beyond couriers, and a clear home — a Behavioral Economics/Operations or Information Systems Department, not a pure-methods venue.
- **Routing test:** if the contribution is really the estimator, re-route to Operations Research; if it is the platform-design tradeoff, Management Science owns it.

## Contribution pass for Management Science

Run this as a concrete capability pass. First lock the decision problem, formal or empirical engine, managerial lever, and generality claim; then test whether the manuscript addresses OR/MS reviewers who expect a generalizable decision model, credible empirical leverage, or algorithmic insight with managerial consequence.

- **Primary move:** Translate the result into who learns what, which mechanism changes, and which alternative explanation is ruled out; keep the claim narrower than the evidence.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against Operations Research for method-first optimization, Marketing Science for marketing models, Organization Science for organization-theory mechanisms; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【What is new】one-sentence claim ...
【Decision relevance】which decision changes, direction ...
【Cross-department travel】who else learns from it ...
【Fit case】home Department + why Mgmt Sci over sister journal
【Magnitude】effect size / comparative-statics insight, honestly bounded
【Next step】mgsci-tables-figures or mgsci-writing-style
```
