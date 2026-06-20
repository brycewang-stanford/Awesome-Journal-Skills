---
name: jru-literature-positioning
description: Use when staking a Journal of Risk and Uncertainty (JRU) manuscript's contribution against the expected-utility-and-alternatives literature. Positions the claim within risk/uncertainty scholarship; it does not invent evidence or citations.
---

# Literature Positioning (jru-literature-positioning)

## When to trigger

- The contribution is described as "new" but the relevant decision-theory or measurement literature is not engaged
- A referee is likely to say "this was settled by [the prospect-theory / ambiguity / VSL literature] decades ago"
- The paper sits between behavioral camps (EU loyalists vs. PT/RDU vs. ambiguity) and has not declared which conversation it joins
- Citations lean on textbooks and reviews rather than the primary representations the paper builds on

## The conversations JRU papers must locate themselves in

JRU readers hold a precise map of the field. Position the paper on it explicitly rather than against "the literature" generically:

- **Expected utility and its critiques** — vNM/Savage as the benchmark; the Allais and Ellsberg paradoxes as the canonical anomalies a contribution must respect or explain.
- **Non-EU under risk** — prospect theory and cumulative prospect theory (probability weighting, loss aversion, reference dependence); rank-dependent utility; disappointment/regret models. Say which functional family you adopt and why.
- **Uncertainty / ambiguity** — maxmin and α-MEU, smooth ambiguity, variational and multiplier preferences, source-dependent weighting. If the paper is about *ambiguity*, it must not be positioned only against *risk* models.
- **Measurement and elicitation** — the lineage of choice-list / multiple-price-list, BDM, and matching-probability methods, and the known biases each carries.
- **VSL and risk valuation** — hedonic-wage and stated-preference traditions; the publication-selection / meta-analysis debates that any new VSL estimate must engage.
- **Insurance and precaution** — demand-for-insurance puzzles, takeup under ambiguity, precautionary saving.

## How to stake the contribution

1. Name the **single conversation** the paper joins and the two or three primary papers it directly extends or contradicts (primary sources, not reviews).
2. State the gap as a property of a *primitive*: a representation that the existing models cannot generate, a measurement bias prior work conflated, an estimate prior work could not identify.
3. Distinguish **incremental within a paradigm** (a sharper estimate of probability weighting) from **cross-paradigm** (evidence that adjudicates EU vs. PT) — JRU values both, but they need different framing and different referees.
4. Pre-empt the "already known" objection by stating what is genuinely new relative to the closest prior result, in one sentence.
5. Hand off to `jru-theory-model` (if the contribution is a representation) or `jru-identification` (if it is a measurement/estimate).

## Citation discipline for a specialist readership

JRU referees are likely to be among the authors you cite, so the bibliography is read as a map of how well you know the field — not as a formality.

- **Cite the representation you use, in its original form.** If you fit cumulative prospect theory you owe the rank-dependent and sign-dependent foundations, not only a survey that mentions them.
- **Cite the elicitation lineage.** A choice-list or BDM design should cite the methodological papers that established and critiqued the device, so the referee knows you adopted it with eyes open.
- **Engage the inconvenient result.** If a prior paper found the opposite sign or a smaller weighting distortion, cite it and explain the difference (sample, stakes, design) — burying it invites a rejection on incomplete scholarship.
- **Avoid review-only citations** for load-bearing claims; a review can frame, but the contribution must be located against primary work.

## Worked vignette (illustrative)

A draft claims to be "the first to measure ambiguity aversion in insurance choices." A JRU referee immediately recalls the ambiguity-and-insurance literature and the smooth-ambiguity tradition. The repositioned paper drops the "first" framing and instead stakes a *primitive* claim: existing estimates conflate ambiguity attitude with pessimistic beliefs, and the paper's design separates them, sharpening the ambiguity index by an identified amount. The two closest prior estimates are cited with the delta from each stated in the introduction — turning a vulnerable novelty claim into a defensible contribution.

## Positioning across paradigms vs. within one

The framing changes sharply depending on the ambition:

- **Within a paradigm** (e.g., a sharper Prelec estimate, a cleaner VSL): position against the best prior *estimate*, lead with precision and identification, and let the contribution be "we measure X better, and here is why the old number was off."
- **Cross-paradigm** (evidence that adjudicates EU vs. CPT, or risk vs. ambiguity): position against both camps' canonical predictions, give each its fair test, and make the discriminating prediction the centerpiece — referees will be drawn from the camp you challenge.
- **Methodological** (a new elicitation that reveals a primitive prior devices distorted): position against the device literature, not the substantive literature, and show the old device's bias quantitatively.

A common failure is writing a within-paradigm paper with cross-paradigm rhetoric ("we overturn expected utility") that the evidence cannot support — calibrate the claim to the design.

## Checklist

- [ ] The paper declares which decision-theory conversation it joins (EU critique / non-EU risk / ambiguity / measurement / VSL / insurance)
- [ ] The two or three closest **primary** papers are cited and the delta from each is stated
- [ ] Ambiguity papers engage ambiguity models, not just risk models (and vice versa)
- [ ] A new VSL or insurance estimate engages the relevant meta-analytic / selection debate
- [ ] The contribution is framed as a property of a primitive, not as "a new context"
- [ ] No citation is asserted that has not been verified; uncertain ones marked 待核实

## Where the introduction makes the contribution land

The positioning is only as strong as where it sits in the paper:

- **The delta from the closest prior result belongs on page one**, in a sentence a referee can quote when recommending acceptance — not buried in a related-work section near the end.
- **Frame the gap as a question the field already cares about**, then show prior work could not answer it for a stated reason (no design to separate u from w; no variation to separate preferences from beliefs).
- **Acknowledge the strongest prior result fairly** before stating your advance; a generous reading of the predecessor makes your delta more credible, not less.

A contribution paragraph that names the conversation, the closest two papers, the gap, and the advance — in four sentences — is what a JRU editor scans for first.

## Anti-patterns

- Citing Kahneman–Tversky or Savage as a courtesy while the actual contribution floats free of any model
- Positioning an ambiguity paper as if Ellsberg and the smooth-ambiguity literature did not exist
- "First to study X in country Y" framing — context novelty is not a JRU contribution by itself
- Strawmanning EU: JRU referees include EU defenders who will punish a caricature
- Burying the delta-from-prior-work in the discussion section instead of the introduction

## Output format

```text
【Journal】Journal of Risk and Uncertainty
【Skill】jru-literature-positioning
【Verdict】well-positioned / re-anchor / under-cited
【Conversation joined】EU critique / non-EU risk / ambiguity / measurement / VSL / insurance
【Closest prior work】<2-3 primary papers> and the delta from each
【Incremental vs. cross-paradigm】which, and why JRU cares
【Source status】verified / 待核实 / not asserted
【Next skill】jru-theory-model OR jru-identification
```
