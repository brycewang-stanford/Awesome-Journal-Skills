---
name: jfqa-contribution-framing
description: Use when framing the contribution of a Journal of Financial and Quantitative Analysis (JFQA) paper — write the strict one-paragraph abstract of no more than 100 words and an introduction that states what is new in finance terms, so the quantitative contribution lands within JFQA's tight abstract cap and high selectivity.
---

# JFQA Contribution Framing (jfqa-contribution-framing)

Use this skill to state the contribution of a **JFQA** manuscript crisply — the journal is highly selective (prints **< 9%** of 1,000+ annual submissions) and imposes an unusually strict abstract limit.

## The 100-word abstract (hard constraint)

JFQA requires the abstract to be **one paragraph of no more than 100 words** — tighter than most finance/economics flagships. Make every word count:

- One sentence on the question and why it matters in finance.
- One or two sentences on the data/design (sample, identification).
- One or two sentences on the headline quantitative result, **with a number** (basis points, alpha, elasticity, magnitude per one-SD change).
- One sentence on the broader implication for the subfield.
- No citations, no equations, no filler. Stay at or under 100 words.

## The introduction contribution paragraph

- Lead with the question and the answer; do not bury the result.
- State the contribution against the closest rivals (see jfqa-literature-positioning).
- Make the **economic magnitude** explicit and the mechanism clear.
- Preview the design and the key exhibit.

## Anti-patterns

- An abstract over 100 words, or split into multiple paragraphs — a formatting strike before a reviewer even reads it.
- Vague claims ("we shed light on...") instead of a measured result.
- Over-claiming beyond what the design supports.
- Saving the contribution for the conclusion.

## JFQA contribution stress test

Before accepting the framing, force the abstract and first-page contribution paragraph to answer:

1. **Finance object**: return, risk, liquidity, capital structure, governance, intermediary behavior, or
   another finance quantity that JFQA readers recognize immediately.
2. **Design credibility**: the source of variation, model restriction, or quantitative method that makes
   the claim more than a finance correlation.
3. **Magnitude**: basis points, alpha, spread, elasticity, valuation effect, probability change, or another
   finance-scale number.
4. **Closest-rival delta**: the one paper a referee will cite and the precise way this paper changes the
   conclusion.

If the answer to item 3 is "statistically significant," the contribution is not yet JFQA-ready.

## Worked compression: a microstructure abstract at the cap

Hypothetical paper: an exchange-level tick-size reform and small-cap liquidity (all numbers illustrative). The first draft ran 127 words and opened with three sentences about electronic markets in general. The JFQA-ready version spends its budget like this:

- Question, ~15 words: does the reform change liquidity for the affected stocks, and through which channel?
- Design, ~25 words: the reform event, roughly 1,200 treated small-caps vs. matched controls, difference-in-differences on intraday quote data.
- Result with numbers, ~40 words: quoted spreads move 11.6 bps (14% of the pre-period mean); depth at the inside changes 22%; effects concentrate where the constraint binds.
- Implication, ~18 words: one sentence on what the elasticity means for tick-size policy.

Every surviving clause carries a finance object, a design cue, or a number. Motivation throat-clearing is the first thing cut, because the 100-word cap punishes it hardest.

## Magnitude phrasing by JFQA subfield

| Subfield | Headline-number form JFQA readers expect | Weak form to delete |
|---|---|---|
| Asset pricing | monthly alpha in bps; premium per one-SD of the characteristic; Sharpe change | "significant at the 1% level" |
| Corporate finance | pp change in leverage/investment/cash, scaled by the sample mean | "positively related to" |
| Microstructure | bps of spread; depth or price-impact change; % of daily volume | "liquidity improves" |
| Institutions/banking | pp change in lending or default probability; capital-ratio effect | "stability increases" |
| Derivatives | implied-vol points; hedging-error reduction; option-return spread | "evidence of mispricing" |

## Referee pushback on framing, with the JFQA repair

| Pushback heard at JFQA | What it signals | Repair |
|---|---|---|
| "The contribution is incremental" | closest-rival delta not quantified | state the number the paper changes and by how much |
| "Magnitudes seem small" | raw coefficient reported without a benchmark | scale by the mean, a one-SD move, or a dollar value |
| "Abstract oversells the design" | causal verbs without causal variation | downgrade verbs to what the design supports |
| "Unclear who cares" | no finance decision-maker named | tie the result to an investor, manager, or regulator choice |

## Output format

```
【Abstract】one paragraph, word count ≤ 100, states result + number
【Question】one sentence
【Contribution】vs. closest rivals, with magnitude
【Implication】for the finance subfield
【Next step】jfqa-tables-figures or jfqa-writing-style
```
