---
name: mksc-contribution-framing
description: Use when stating the headline contribution of a Marketing Science manuscript — naming the primary dimension (substantive marketing insight, modeling, methodology, data, or practice) and writing the contribution and managerial-implication paragraphs. Frames the contribution; it does not build the model (mksc-theory-development) or run the analysis (mksc-data-analysis).
---

# Contribution Framing (mksc-contribution-framing)

## When to trigger

- The results exist but the "so what" for marketing is thin or implicit
- You cannot say in one sentence what the field learns
- A reviewer calls the contribution "incremental" or "a methods exercise"
- You are deciding the Frontiers track, which rewards one dominant dimension

## Name the primary dimension

Marketing Science contributions fall on identifiable dimensions. State which one is primary, and let the others support it:

- **Substantive** — a new marketing insight or counterfactual answer (how a pricing/advertising/channel/platform decision should change, and why).
- **Modeling** — a new or sharper model that captures a marketing mechanism prior models missed.
- **Methodological** — a new estimator, identification strategy, or computational method others can reuse.
- **Data** — a novel dataset enabling questions that were previously infeasible (the Database track).
- **Practice** — a deployed solution with measurable impact (Practice Paper / Practice Prize, with a 500–1,000-word Impact Statement, single-blind).

Most regular papers lead on **substantive** or **modeling** and use methodology as support. **Frontiers** papers must make a major contribution on **one** primary dimension while meeting (relaxed) thresholds on the others — "different, but equal."

## Write the contribution explicitly

- **Intro contribution paragraph**: state the marketing question, the model, the answer (including the key counterfactual magnitude), and what the field now knows that it did not.
- **Discussion**: generalize beyond the specific data — boundary conditions, what the mechanism implies for other settings, and where the model would break.
- **Managerial implications**: translate the counterfactual into a decision a manager could act on, with honest scope. The INFORMS lineage rewards decision-relevant, quantified takeaways.

## Avoid the common downgrades

- A sophisticated model that answers no important marketing question reads as a technique demo.
- A correct estimate with no counterfactual leaves the "so what" unstated.
- Listing five "contributions" of equal weight dilutes the primary one.

## Checklist

- [ ] Primary dimension named (substantive / modeling / methodological / data / practice)
- [ ] One-sentence statement of what the field learns
- [ ] Intro paragraph ties question → model → answer → counterfactual magnitude
- [ ] Discussion gives boundary conditions and generalization
- [ ] Managerial implication is decision-relevant and quantified, with scope
- [ ] If Frontiers: one dominant dimension, others at relaxed threshold

## Anti-patterns

- "We contribute to the literature on X" with no specific learning.
- Equal-weight contribution lists that hide the real one.
- Method showcased with no marketing payoff.
- Managerial implications that restate results instead of prescribing a decision.


## Contribution pass for Marketing Science

Treat this skill as an executable review pass, not a prose hint. First lock the demand/supply mechanism, fit evidence, and counterfactual decision margin; then judge whether the current manuscript answers the venue's real reader: quantitative marketing reviewers who read the model through the managerial counterfactual it makes possible.

- **Do the pass:** Translate the result into who learns what, which mechanism changes, and which alternative explanation is ruled out; keep the contribution narrower than the evidence.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against Journal of Marketing Research for empirical marketing breadth, Management Science for wider OR/MS reach, Quantitative Marketing and Economics for specialist modeling; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Primary dimension】substantive / modeling / methodological / data / practice
【What the field learns】one sentence
【Intro contribution】question → model → answer → counterfactual magnitude
【Generalization】boundary conditions / scope
【Managerial implication】decision + quantified payoff
【Track】regular / Frontiers (one dominant dimension)
【Next step】mksc-tables-figures
```
