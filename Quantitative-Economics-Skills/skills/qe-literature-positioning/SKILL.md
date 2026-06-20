---
name: qe-literature-positioning
description: Use to stake a Quantitative Economics (QE) manuscript's contribution against the frontier — what quantitative gap it closes relative to prior empirical, structural, and methodological work, and against its Econometric Society siblings. Positions the paper; it does not write a standalone literature survey.
---

# Literature Positioning (qe-literature-positioning)

## When to trigger

- The contribution relative to existing quantitative work is fuzzy or oversold
- You cannot name the two or three papers you are building on and the one you are beating
- A referee will ask "what is new here beyond [prior structural/empirical paper]?"
- You are unsure whether the positioning reads as QE rather than Econometrica or a field journal

## The QE positioning logic

QE referees — refereeing for the **Econometric Society's empirically/quantitatively oriented** journal — judge a paper on whether it **moves a quantitative question forward**, not on a literature tour. Positioning must answer three questions crisply:

1. **What did we not know quantitatively before this paper?** A parameter that was assumed rather than estimated; a counterfactual no prior design could run; a fact no prior data could measure; a method whose application changes a known answer.
2. **Whose shoulders are you standing on, and where do you depart?** Name the prior empirical design or structural model you extend, and the precise margin of departure (richer data, a relaxed assumption, a new identification result, a feasible computation).
3. **Why QE and not a sibling?** If the contribution is the *method itself*, the home is Econometrica; if it is *pure theory*, Theoretical Economics. QE positioning emphasizes the **quantitative answer to a substantive question** that the method makes possible.

## Positioning craft

- Integrate citations into the argument; do not write an isolated "Literature" wall. A short related-work paragraph plus contextual cites throughout is the QE norm.
- Be specific about the **delta**: "Prior work assumes X; we estimate it and find Y, which overturns Z" beats "we contribute to the literature on X."
- Distinguish **empirical**, **structural/computational**, and **methodological** strands, and say which one your contribution primarily advances.
- Reference work as it is **published, in a stable public archive (e.g., SSRN), or author-provided** — QE expects references that resolve to durable sources by final publication.

## Checklist

- [ ] The quantitative gap is stated in one sentence ("X was assumed/unmeasured; we estimate/measure it")
- [ ] Two or three load-bearing predecessors named, with the precise departure from each
- [ ] The one closest competing paper named and distinguished
- [ ] Empirical vs. structural vs. methodological strand of the contribution identified
- [ ] The "why QE, not Econometrica/TE" cut is implicit in the framing
- [ ] References resolve to published / stable-archive / author-provided sources
- [ ] No standalone survey section padding the contribution

## Anti-patterns

- A literature-dump section that lists everything and positions nothing
- "First to study X" claims that a prior structural or empirical paper already touched
- Hiding the closest competitor instead of distinguishing it head-on
- Positioning a method-first contribution as QE when Econometrica is the real home
- Citing only working papers when published or stable-archive versions exist

## Siblings and field journals: where the delta lands

| If the departure is mainly... | Natural home | QE positioning move |
|-------------------------------|------|---------------------|
| a new estimator/theorem | Econometrica / TE | foreground the quantity it newly enables |
| a counterfactual earlier designs did not deliver | QE | name the structural margin that makes it feasible |
| a measured object no prior data captured | QE | tie the fact to a question the field shares |

The desk-reject trap is the **incremental-delta** paper: a competent re-estimation of a known model on new data with no new quantity. Make the delta a number the field lacked.

## Worked vignette: positioning a trade-elasticity estimate (illustrative)

A paper re-estimates the trade elasticity using a tariff change as quasi-experimental variation. Weak positioning: "we contribute to the literature on trade elasticities." QE positioning names the delta: "Prior gravity estimates assume a single elasticity around 4; using firm-level tariff variation we find it ranges from 2 to 7 across sectors (illustrative), raising the welfare cost of a uniform tariff by about a third versus the homogeneous benchmark." Two predecessors are named (the gravity workhorse, the closest firm-level study), each with its margin of departure.

## Referee pushback and the positioning fix

- *"What is new beyond [prior structural paper]?"* → State the one-sentence delta as a quantity that paper did not deliver, not a topic overlap.
- *"This belongs at Econometrica — it is a method."* → Re-center on the substantive answer the method makes possible; demote the machinery.
- *"You ignore the closest competitor."* → Name it and distinguish on data, assumption, or quantity head-on, not by omission.

## Output format

```
【Quantitative gap】one sentence
【Building on】[2-3 papers + departure from each]
【Closest competitor】[paper] — distinguished how
【Contribution strand】empirical / structural / methodological
【QE vs. sibling】why not Econometrica / TE
【Next step】qe-contribution-framing
```
