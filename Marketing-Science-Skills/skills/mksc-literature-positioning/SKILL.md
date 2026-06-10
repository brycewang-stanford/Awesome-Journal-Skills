---
name: mksc-literature-positioning
description: Use when positioning a Marketing Science manuscript in its literature — locating the contribution among structural and analytical modeling precedents and the relevant substantive stream (pricing, advertising/digital, channels/retail, branding, platforms, analytics), and disclosing self-overlap. Positions the paper; it does not state the headline contribution (mksc-contribution-framing).
---

# Literature Positioning (mksc-literature-positioning)

## When to trigger

- The intro reads as "no one has modeled X" (gap-spotting) rather than joining a modeling conversation
- You are unsure which precedent papers define your model's baseline
- Reviewers may say "this is a small extension of an existing model"
- You build on your own prior work and must disclose how this paper goes beyond it

## Position on two axes at once

A Marketing Science paper sits at the intersection of a **modeling lineage** and a **substantive stream**. Make both explicit.

1. **Modeling lineage.** Which model is your baseline — a BLP-style demand system, a dynamic discrete-choice model, a channel/Stackelberg pricing game, an auction or search model? State what you add to it (a new mechanism, richer dynamics, a novel identification strategy, a tractable closed form) and why prior models could not answer your question.
2. **Substantive stream.** Which marketing problem — pricing, advertising/digital and attribution, branding, distribution channels and retailing, platforms/two-sided markets, or marketing analytics/ML — does the paper speak to? Tie the model's payoff to that stream's open questions.

## From gap-spotting to a real contribution

Do not justify the paper by absence ("X has not been studied"). Justify it by **what the field gains**: a sharper mechanism, a counterfactual prior models could not compute, a relaxed assumption that overturns a known result, or a method others can reuse. The strongest framings show that a *natural* prior modeling choice gives the wrong answer, and your model corrects it.

## Self-overlap disclosure (required)

Marketing Science requires that if the submission builds on the authors' own published or under-review work, you **cite it and state how this paper's contribution goes beyond it**. Because regular review is double-anonymous, cite your own prior work in the neutral third person and keep the manuscript blinded (no "in our earlier paper").

## Checklist

- [ ] Baseline model(s) named; your delta to each is explicit
- [ ] Substantive stream identified and its open question stated
- [ ] Contribution framed as field gain, not absence of prior work
- [ ] Closest competing model addressed head-on (why it cannot answer this)
- [ ] Author self-overlap cited and differentiated; manuscript stays blinded

## Anti-patterns

- "No paper has done X" with no engagement of the nearest model.
- Citing a wall of references without naming the one baseline you extend.
- Hiding a close prior paper (your own or others') the editor will know.
- De-blinding via "our previous work" phrasing under double-anonymous review.


## Positioning pass for Marketing Science

Use this as a second-pass capability check. First lock the demand/supply mechanism, fit evidence, and counterfactual decision margin; then test whether the manuscript addresses quantitative marketing reviewers who read the model through the managerial counterfactual it makes possible.

- **Primary move:** Map incumbent conversation, unresolved tension, this manuscript's delta, and the sibling-venue omission a referee might notice.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against Journal of Marketing Research for empirical marketing breadth, Management Science for wider OR/MS reach, Quantitative Marketing and Economics for specialist modeling; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Modeling lineage】baseline model(s) + your delta
【Substantive stream】pricing/advertising/channels/platform/analytics + open question
【Contribution framing】field gain (not gap)
【Closest competitor】why it cannot answer this question
【Self-overlap】prior work cited + differentiated; blinding intact
【Next step】mksc-methods
```
