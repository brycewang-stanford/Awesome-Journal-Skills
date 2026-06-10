---
name: mksc-topic-selection
description: Use when choosing or sharpening the research question for a Marketing Science manuscript — testing whether a marketing problem is important AND admits a formal model (structural or analytical), and whether Marketing Science (not JCR/JMR/Management Science) is the right venue.
---

# Topic Selection & Venue Fit (mksc-topic-selection)

## When to trigger

- You have a marketing phenomenon (pricing, advertising/digital, branding, channels/retail, platforms, analytics) but no modeling angle
- You are unsure whether the question is "important" by Marketing Science standards
- You have a finding but it is a reduced-form correlation with no model
- You cannot decide between Marketing Science, JCR, JMR, or Management Science

## The two-part fit test

Marketing Science publishes "articles that answer **important research questions in marketing using mathematical modeling**." A topic must pass both gates:

1. **Substantive importance.** A real marketing decision or market phenomenon — how firms price, advertise, design assortments, or how consumers and markets respond — that managers or the field care about.
2. **Modelability.** It can be framed as an analytical (game-theoretic) model of strategic interaction, OR a structural econometric model of demand/supply that is estimable and yields counterfactuals. If neither fits, MKSC is likely the wrong venue.

A strong MKSC topic usually implies a **counterfactual or policy question** — "what happens to prices, share, or welfare if the firm/platform changes X?" — that only a model can answer.

## Pick the genre the question implies

- **Analytical** when the insight is about strategic interaction and you want clean comparative statics (channel conflict, competitive pricing, information/targeting design).
- **Structural** when you need quantitative magnitudes and counterfactuals from data (demand estimation, dynamic discrete choice, auctions, search).
- A **Frontiers** topic is timely and high-impact with one dominant contribution dimension — scope it to a 6,000-word total story.

## Venue contrast

- **JCR** — consumer-psychology theory and experiments with no formal model. If that is your paper, target JCR.
- **JMR** — broader, methods-forward marketing (modeling or behavioral); MKSC is narrower on the modeling core.
- **Management Science** — general management science; if the contribution is not specifically a marketing decision, it may belong there.

## Checklist

- [ ] Question is an important marketing decision/market phenomenon, in one sentence
- [ ] It admits a formal model (analytical or structural), not just a regression
- [ ] There is a clear counterfactual/policy payoff a model can deliver
- [ ] Genre (analytical / structural / Frontiers) chosen deliberately
- [ ] Venue confirmed vs. JCR / JMR / Management Science

## Anti-patterns

- A correlation in search of a story, with no model.
- A pure consumer-psychology effect dressed up as quantitative marketing.
- "Important to a manager" but no tractable model — or an elegant model answering no real marketing question.


## Fit pass for Marketing Science

Treat this skill as an executable review pass, not a prose hint. First lock the demand/supply mechanism, fit evidence, and counterfactual decision margin; then judge whether the current manuscript answers the venue's real reader: quantitative marketing reviewers who read the model through the managerial counterfactual it makes possible.

- **Do the pass:** Score the manuscript on venue fit, novelty, evidence readiness, and audience ownership; reject a prestige-only target when a sibling venue owns the contribution more directly.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against Journal of Marketing Research for empirical marketing breadth, Management Science for wider OR/MS reach, Quantitative Marketing and Economics for specialist modeling; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Question】one-sentence marketing question
【Importance】why the field/manager cares
【Modelability】analytical / structural / unclear; counterfactual payoff
【Genre】analytical / structural / Frontiers
【Venue】Marketing Science vs JCR/JMR/MgmtSci — fit verdict
【Next step】mksc-theory-development
```
