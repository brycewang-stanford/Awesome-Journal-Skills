---
name: finman-topic-selection
description: Use when deciding whether a topic fits Financial Management (FM) and is worth aiming there — testing the question for general-interest finance relevance, topicality, and managerial/market payoff before the literature and design work begins. Sets the target; it does not run analysis or write the paper.
---

# Topic Selection (finman-topic-selection)

## When to trigger

- You have a finance result or idea and are unsure FM is the right home (vs. a specialist or a top-3 outlet)
- A coauthor asks "is this *general-interest* enough, or too niche, for FM?"
- The question feels technically sound but you cannot yet say why a practitioner or a non-specialist finance academic would care
- The topic feels dated — re-treading a settled debate rather than a live one

## The FM topic bar

FM is the FMA's **general-interest** finance journal, and its editors are unusually explicit about taste: they want "academic articles that people actually read," judged on **originality, rigor, timeliness, practical relevance, and quality**, with **less weight on trivial robustness** and real weight on whether the paper "provokes and furthers debate." Translated into a topic filter, an FM-worthy question is one a corporate-finance, asset-pricing, banking, *or* markets reader would all find interesting, that speaks to a decision a manager, investor, regulator, or trader actually faces, and that is **topical** — anchored to a current or emerging financial issue rather than a marginal extension of a 2008 debate. The journal also actively solicits work "from anywhere around the globe," so a clean non-US setting is an asset, not a liability, when the financial mechanism is general.

## Deciding whether the topic is FM-shaped

Run the question through four gates, in order. If it fails the first two, FM is probably the wrong target; if it fails the last two, the topic needs reframing before you proceed.

1. **General-interest gate.** Could you state the finding in one sentence to a finance seminar with no field specialists and have them care? If it only lands with, say, microstructure insiders, consider a specialist outlet — or recast the takeaway around the broader implication.
2. **Decision-relevance gate.** Name the agent whose decision changes if the result is true — a CFO setting payout, an investor pricing a factor, a regulator weighing a rule, a board designing pay. If no such agent exists, the "practical relevance" criterion is unmet.
3. **Topicality gate.** Tie the question to a live or emerging issue (a recent regulation, a new instrument, a market structure shift, a data-newly-available phenomenon). A timely hook is one of FM's five stated criteria.
4. **Originality gate.** State the *new* thing — a new fact, a new mechanism, a new identification of an old mechanism, or a clean answer to a genuinely open question. "We add controls to a known result" fails this gate at FM.

## Topic signals by FM subfield

FM is general-interest, so the same four gates apply across very different subfields — but the *shape* of an FM-worthy question differs by area. Use this to pressure-test the topic against its home subfield's FM bar.

| Subfield | An FM-shaped question looks like | A too-narrow / mis-targeted version |
|----------|----------------------------------|-------------------------------------|
| Corporate finance | a financing/investment/M&A decision affected by a live shock, with a managerial takeaway | a marginal re-test of pecking order on a new sample |
| Payout & capital structure | how a policy choice responds to a tax/regulatory change that separates competing theories | another determinants-of-leverage regression |
| Governance | a board/ownership mechanism with a credible source of variation and a board-relevant implication | a governance-index correlation with performance |
| Investments / asset pricing | a return pattern that speaks to a general debate (risk vs. mispricing) and survives costs | a factor zoo addition with no economic story |
| Banking / intermediation | an information/frictions mechanism that generalizes beyond banks | a bank-specific regulatory note |
| Markets / microstructure | a market-design or liquidity finding with implications a trader/regulator acts on | a venue-specific tick-size technicality |

## Checklist

- [ ] One-sentence claim is legible to a general finance audience, not only a subfield
- [ ] The decision-maker who would act on the result is named (manager / investor / regulator / board)
- [ ] The question is tied to a current or emerging financial issue (timeliness)
- [ ] The originality is stated as a specific new fact/mechanism/answer, not an incremental extension
- [ ] The setting (US or non-US) is justified by the generality of the mechanism, not convenience
- [ ] The topic fits the FM-shaped column for its subfield, not the too-narrow column
- [ ] You can articulate why this is FM and not a specialist sibling or a top-3 desk

## Anti-patterns

- A technically clean paper with no audience beyond one subfield — "rigorous but no one reads it"
- Pitching a marginal extension of a long-settled debate as if novelty came from the new sample
- Leading with method ("we apply estimator X") instead of the financial question and its stakes
- Treating a non-US setting as a defect to apologize for, rather than evidence of generality
- Assuming exotic data alone makes a topic FM-worthy without a decision-relevant payoff

## Worked vignette (illustrative)

A draft documents that firms in one country smooth dividends more after a 2023 tax change. As framed it reads like a country-specific note. The FM reframe: ask the general-interest question — *do payout commitments respond to tax-induced changes in the marginal investor's clientele, and what should a CFO infer about signaling vs. catering?* Now the decision-maker (the CFO setting payout policy), the topicality (a 2023 reform), and the originality (clean tax variation that separates two payout theories) are all explicit, and a non-US setting becomes the source of identification rather than a parochial limitation.

## Early routing decisions this stage settles

Topic selection is also where you decide, provisionally, two things that shape the whole pipeline:

- **Whether FM is the right target at all.** If the question fails the general-interest and decision-relevance gates, route the user honestly to a specialist sibling rather than forcing an FM pitch the editors will see through. Naming the correct home early saves a desk-reject and a fee.
- **Where the binding constraint will be.** A topic whose novelty is a *new fact* will live or die on measurement and framing; one whose novelty is a *causal claim about an old mechanism* will live or die on identification. Flag this so `finman-workflow` can route to the right next link instead of marching through every stage.

## Reframes that rescue a borderline topic

When a topic fails a gate, it is often salvageable by changing the question, not the data:

- **Fails general-interest** → lift the takeaway one level: from "X happens in industry Y" to the mechanism (information, frictions, incentives) that travels across industries.
- **Fails decision-relevance** → name the agent and the decision explicitly; if you cannot, the finding may be a measurement curiosity better suited elsewhere.
- **Fails timeliness** → re-anchor to a current shock, instrument, or newly available dataset that makes the old question live again.
- **Fails originality** → find the disagreement your result settles, or the fact no one has cleanly documented, rather than the marginal coefficient you add.
A topic that survives all four after reframing is genuinely FM-shaped; one that needs the data to do the persuading is not.

## Output format

```
【Journal】Financial Management
【Topic in one sentence】<general-interest finance claim>
【Decision-maker】<manager / investor / regulator / board who acts on it>
【Timeliness hook】<current or emerging issue it speaks to>
【Originality】<new fact / mechanism / identification / answer>
【FM vs. siblings】why FM and not JCF / JFQA / a top-3 desk
【Source status】verified / 待核实 / not asserted
【Next skill】finman-literature-positioning
```
