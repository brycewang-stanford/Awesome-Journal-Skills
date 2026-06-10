---
name: rje-literature-positioning
description: Use to position a manuscript against the industrial-organization frontier for The RAND Journal of Economics (RJE) — staking the contribution against prior IO work without a standalone survey, and citing in the RJE author-date style (no page numbers, no issue numbers). Positioning, not a literature review.
---

# Literature Positioning (rje-literature-positioning)

## When to trigger

- The related-work section reads like a survey instead of a positioning argument
- You are unsure which IO literatures your article must engage
- You need citations to conform to the RJE Style Guide

## Positioning at the IO flagship

RJE is the **flagship industrial-organization journal** (formerly the Bell Journal of Economics), so referees are IO insiders who know the canon and the current frontier. Positioning must show **exactly what your article adds to the IO conversation** — a new structural method, new estimates for a market, a new mechanism, or a theoretical result — not summarize the field. Engage the **specific strand** your contribution touches:

- **Demand & differentiation:** discrete-choice / random-coefficients (BLP-style) demand and its descendants.
- **Supply, conduct & market power:** oligopoly pricing, conduct testing, pass-through, markups.
- **Entry, exit & dynamics:** static and dynamic entry/investment games.
- **Regulation & antitrust:** merger analysis, regulated-industry studies, market design.
- **Organizations & contracts:** vertical relationships, incentives, firm boundaries.
- **Auctions & mechanisms** where competition is the object.

For each relevant strand, name the **closest prior articles**, state what they established, and pinpoint the **gap your work closes**. Distinguish a **method** contribution (you estimate something previously hard to identify) from a **substantive** one (you answer a market/policy question prior tools could not).

## Citation form (RJE Style Guide)

- Author-date in-text, **name and year only, no page numbers** (e.g., "Berry, Levinsohn and Pakes, 1995").
- Reference list alphabetical, unnumbered, **no issue numbers** in journal citations.
- Avoid numbered or footnote-style citations.

## Strand-targeting grid (find the conversation your article must enter)

Pick the strand your contribution actually touches, then identify the anchor literature referees will expect you to engage. Engaging the wrong strand reads as not knowing the field.

| Your object | IO strand to engage | What referees expect you to cite |
|---|---|---|
| Estimated demand elasticities | Discrete-choice / random-coefficients demand | The BLP lineage and its differentiation-instrument descendants |
| Markups / market power | Conduct, pass-through, the production-function markup debate | Both the structural-IO and the recent markup-measurement strands |
| Entry / market structure | Static and dynamic entry games | The entry-game and dynamic-oligopoly estimation lineage |
| Merger effects | Merger simulation and retrospectives | Both the simulation method and the ex-post retrospective evidence |
| Platform / two-sided pricing | Two-sided markets and network effects | The platform-competition and attention-market literatures |
| Vertical contracts | Vertical relations, foreclosure, bargaining | The vertical-restraints and Nash-in-Nash bargaining strands |

## Worked vignette: positioning a platform-pricing article

Suppose your article estimates how a food-delivery platform's commission structure affects restaurant entry and consumer prices. Positioning moves, not a survey:

- **Strand**: two-sided markets — you extend platform-pricing theory to an empirical setting with estimated cross-side externalities.
- **Closest prior work**: name the two or three articles that estimated platform demand or set platform-pricing theory, state what each established (e.g., the cross-group externality logic, or prior empirical platform demand estimates), and pinpoint the gap.
- **Gap closed (one sentence)**: "Prior work characterized optimal platform pricing theoretically or estimated one side's demand; we jointly estimate both sides' responses and quantify the welfare split of a commission change."
- **Contribution type**: substantive-empirical with a method wrinkle (joint two-sided estimation), not a pure theory result.

## Referee-pushback patterns and the venue fix

- **"You cite the canon but miss the current frontier."** Fix: add the most recent IO articles on your exact mechanism; referees are insiders who track the working-paper frontier (NBER IO, antitrust-relevant work).
- **"Your 'gap' was already closed by [recent article]."** Fix: read forward-citations of your anchor papers; restate the gap as the residual your article uniquely closes.
- **"This reads as a survey, not a stake."** Fix: convert each paragraph from "X did A, Y did B" into "relative to X and Y, this article adds Z."
- **"You claim novelty against a literature you do not engage."** Fix: cite and characterize the closest competitor honestly, then differentiate on method, market, or mechanism.

## Anti-patterns

- A chronological survey with no claim about your marginal contribution
- Citing general-econ landmarks while ignoring the specific IO strand you extend
- Page numbers in in-text cites or issue numbers in references (off RJE style)
- Claiming novelty against a literature you have not actually engaged

## Output format

```
【Strands engaged】[demand / conduct / entry-dynamics / regulation / organizations / auctions]
【Closest prior work】[3-6 articles, author-date]
【Gap closed】one sentence
【Contribution type】method / substantive / theoretical
【Citation style】author-date, no page/issue numbers? [Y/N]
【Next step】rje-identification-strategy
```
