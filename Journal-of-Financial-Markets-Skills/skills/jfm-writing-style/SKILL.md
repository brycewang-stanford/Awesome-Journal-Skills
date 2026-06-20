---
name: jfm-writing-style
description: Use when the prose, intro, and abstract are the bottleneck for a Journal of Financial Markets (JFM) manuscript — making the trading mechanism land for microstructure insiders. Late-stage polish; it does not invent evidence or citations.
---

# Writing Style (jfm-writing-style)

## When to trigger

- The mechanism, design, and exhibits are stable and it is time to write the intro and abstract (not before)
- The abstract describes data and methods but never states the microstructure result
- The intro reads like a broad-finance paper and does not signal "this is microstructure" in the first paragraph
- Institutional detail (market rules, order types, venue mechanics) is vague where precision is the JFM currency
- A coauthor's draft over-claims generality JFM referees will not grant

## The JFM voice

JFM prose is **precise about market mechanics and disciplined about claims**. The reader is a microstructure specialist who wants the institutional detail right and the mechanism stated plainly. Three habits define the house style:

1. **Lead with the trading-process mechanism, fast.** The first paragraph should name the market object (spread, depth, order flow, price discovery) and the economic force. A JFM intro that buries the mechanism behind two paragraphs of general-finance throat-clearing reads as mis-targeted.
2. **Get the institutions exactly right.** Name the venue, the matching/priority rule, the order types, the tick size, the relevant regulation. Microstructure referees notice when "the exchange" is used where the actual mechanism matters. This precision *is* the contribution's credibility.
3. **Claim only what the design supports.** Prefer "spreads narrow by X bps for treated stocks" to "liquidity improves." State economic magnitude in market terms (bps, depth, impact), not just statistical significance.

## Writing the intro and abstract

**Abstract:** in ~4-6 sentences — (1) the market question, (2) the data/setting in microstructure terms, (3) the identifying variation, (4) the *result with a magnitude in market units*, (5) the mechanism it implies, (6) one sentence of contribution. Confirm the exact abstract word limit on the guide for authors (检索于 2026-06；以官网为准 — 待核实).

**Intro (the funnel):** (1) the market phenomenon and why how-it-trades matters; (2) what we do and find, in one tight paragraph with the headline magnitude; (3) the identifying variation / measurement advance; (4) placement vs. the microstructure lineage (one paragraph, not a survey); (5) why JFM and not a broad-finance frame — the specialist depth. Keep the contribution sentence verbatim-consistent with the abstract and the title.

**Throughout:** define each liquidity measure on first use; keep units consistent with the exhibits; resist the passive "it is found that."

## Before / after (illustrative)

*Before (broad-finance framing):* "We examine the relationship between trading activity and asset prices using a large dataset of intraday transactions and find economically and statistically significant effects." This could be any finance paper; it states no mechanism and no magnitude.

*After (JFM voice):* "When a stock joins the pilot's wider-tick group, effective spreads widen by 12 bps and quoted depth at the touch nearly doubles, while the permanent (adverse-selection) component is unchanged — implying the wider tick raises liquidity-supply rents without altering information asymmetry." It names the shock, the market objects, the magnitudes in market units, and the mechanism it identifies. That is the sentence a microstructure editor wants in paragraph one.

## The mechanism sentence

Every JFM paper should have one sentence a reader could quote as "what this paper shows about how markets work." It names the cause, the market object, the magnitude, and the channel: "A wider tick raises liquidity-supplier rents — depth doubles while the adverse-selection component is flat — so the cost falls on uninformed traders." Draft this sentence early and let it discipline the whole paper; if you cannot write it cleanly, the contribution is not yet sharp. It should appear (in some form) in the abstract, the intro, and the conclusion, keeping the paper anchored to a single mechanism rather than a list of correlations.

## House-style details that signal fluency

- Use the field's terms precisely: *effective* vs. *quoted* spread, *permanent* vs. *temporary* impact, *adverse selection* vs. *inventory* cost, *lit* vs. *dark*, *maker-taker*. Loose usage reads as an outsider.
- Report magnitudes in the unit a trader thinks in (bps, cents, shares, microseconds), and benchmark against the average (a 2-bps effect on a 5-bps spread is large; on a 200-bps spread it is noise).
- Name dates and rules ("after Reg NMS, effective October 2007") rather than vague time references.
- Keep the active voice and a single, consistent label for each measure throughout.

## Pruning the broad-finance throat-clearing

A common drag on microstructure intros is two opening paragraphs of general motivation ("financial markets are central to the economy…") before the specific question appears. A microstructure editor wants the trading-process question and the headline in the first half-page. Cut generic scene-setting to one or two sentences and move quickly to the market mechanism, the setting, and what you find. The same discipline applies to the literature review: place the paper in its sub-field in a tight paragraph rather than surveying. Density and specificity read as expertise; broad preamble reads as a paper hedging about whether it really belongs at JFM.

## Checklist

- [ ] First paragraph names the trading-process object and the economic force
- [ ] Abstract states the result with a magnitude in market units, not just significance
- [ ] Institutional detail (venue, rules, order types, tick size, regulation) is exact, not generic
- [ ] Claims are sized in bps/depth/impact and bounded by the design
- [ ] The microstructure lineage is placed in the intro without a full literature survey
- [ ] One sentence says why JFM, not a broad-finance journal
- [ ] Contribution sentence is consistent across title, abstract, and intro

## Calibrating claims to a skeptical specialist

Microstructure referees are unusually quick to flag over-claiming because they know how many ways a liquidity result can be an artifact. Match the verb to the evidence: a clean randomized shock supports "causes"; a panel regression supports "is associated with"; a heterogeneity pattern supports "consistent with [mechanism]," not "proves." Name the channel only when the design isolates it — "spreads narrow because adverse selection falls" requires showing the adverse-selection component moved, not just the total spread. State scope honestly: a result on large-cap U.S. equities is not a claim about all markets. This disciplined register reads as competence to a specialist, whereas sweeping language reads as naivety and invites a harsher review.

## Anti-patterns

- An abstract that lists data and methods but never states the microstructure finding
- Generic institutional descriptions ("trades happen on the exchange") where the mechanism matters
- Over-claiming "liquidity improves" without magnitude or sign of the channel
- A broad-finance intro framing that hides the microstructure cut
- Significance-driven prose ("highly significant") instead of economic magnitude
- Polishing prose before the mechanism, measurement, and identification are settled

## Sequencing the write so the mechanism survives editing

Write in the order that protects the contribution. First lock the **results section** prose around the stable exhibits, stating each magnitude in market units. Then write the **mechanism / interpretation** paragraphs that connect the numbers to the trading-process force, since that is what a microstructure editor evaluates. Only then write the **intro**, reverse-engineered from the results so the headline magnitude in paragraph two matches the tables exactly. Write the **abstract last**, distilled from the finished intro. This order prevents the common failure where a beautifully written intro promises a sharper or broader result than the exhibits deliver — a gap microstructure referees notice immediately and read as over-claiming.

## Output format

```text
【Journal】Journal of Financial Markets (JFM)
【Skill】jfm-writing-style
【Mechanism in para 1】trading-process object named early? [Y/N]
【Abstract】result + market-unit magnitude stated? [Y/N]
【Institutions】venue/rules/order-types/tick exact? [Y/N]
【Claim discipline】sized in bps/depth/impact, design-bounded? [Y/N]
【Why JFM line】present in intro? [Y/N]
【Source status】abstract limit / style verified or 待核实
【Next skill】jfm-submission
```
