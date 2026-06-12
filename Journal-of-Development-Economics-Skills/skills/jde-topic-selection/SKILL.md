---
name: jde-topic-selection
description: Use when judging whether a research question fits the Journal of Development Economics (JDE) — a first-order question about low- and middle-income economies and the process of economic development. Tests topic fit before identification or drafting begins.
---

# Topic Selection (jde-topic-selection)

## When to trigger

- You have data or a setting but are unsure it is a *development* question
- The question is interesting but the developing-country stakes are unclear
- You are weighing whether the work fits JDE versus a general-interest or a regional journal
- You are deciding whether to run the project as a prospective, pre-results-reviewed design

## The JDE fit bar

JDE is the **leading field journal in development economics**, published by Elsevier. It publishes theoretical and empirical research on the **economics of developing countries and the process of economic development** — poverty, growth, institutions, trade and development, health, education, labor, agriculture, credit and finance, and the microeconomics and macroeconomics of low- and middle-income economies. A question fits when:

- The **economic agent or economy is developing** (a household, firm, market, or government in an LMIC), and the mechanism is genuinely about development, not a generic micro result that happens to use developing-country data.
- It is **first-order**: it speaks to welfare, growth, or policy for poor populations, not a marginal refinement of a within-subfield debate.
- It travels: a smart development economist outside your exact subfield should care about the *answer*.

Because JDE is highly selective — roughly **1,300 submissions a year**, only about a quarter sent for review, ~**6-8%** accepted — a marginal or purely descriptive question rarely survives. The question, not the technique, has to carry the paper.

## Decision shortcuts

- "It's a clean micro result but the setting is incidental" → likely off-fit; sharpen the development mechanism or retarget.
- "It's a field experiment with a clear policy lesson for poor households" → strong fit; consider the **pre-results review** track so the design is locked before results.
- "It's a short, single-result paper" → consider the **AER: Insights-style short-paper** track.
- "It's a theory paper on development dynamics" → fits; JDE publishes theory, not only RCTs.

## Fit-screen table (illustrative verdicts)

| Candidate question                                                        | JDE fit  | Why                                                       |
|---------------------------------------------------------------------------|----------|-----------------------------------------------------------|
| RCT of a school-meals program on learning in a low-income country         | Strong   | First-order welfare stake, credible design, policy lever  |
| Microfinance access and firm investment in an LMIC, quasi-experimental    | Strong   | Credit-market friction, development mechanism is the point |
| Asset-pricing anomaly tested on an emerging-market exchange               | Weak     | Finance question wearing LMIC data; setting is incidental |

## Worked fit call (illustrative)

A team has administrative data on a rural electrification rollout and wonders if it is a JDE paper.

- **Off-fit version:** "Does electricity access correlate with nighttime light intensity?" — descriptive, no welfare stake, no identification.
- **On-fit version:** "Did staggered grid expansion raise non-farm enterprise formation and household earnings?" — a first-order question with a quasi-experimental design (rollout timing) and a clear policy lever; route to `jde-identification-strategy` next.

## Referee fit pushback

- *"This is a general micro result that happens to use developing-country data."* → relocate the contribution to the development mechanism, or retarget honestly. Novelty of site alone is never the contribution; the *answer* must matter for poor populations.

## Anti-patterns

- A general labor/IO/macro paper wearing a developing-country dataset as a costume
- A descriptive correlation with no welfare or policy stake for poor populations
- Over-claiming external validity from one site without saying what the result teaches development broadly
- Treating JDE as a fallback for a paper that failed a top-5 desk — fit must be genuine


## Fit pass for Journal of Development Economics

Treat this skill as an executable review pass, not a prose hint. First lock the development constraint, identification, welfare or distribution margin, and implementation context; then judge whether the current manuscript answers the venue's real reader: development economists who expect a development mechanism, credible design, and policy-relevant external validity.

- **Do the pass:** Score the manuscript on venue fit, novelty, evidence readiness, and audience ownership; reject a prestige-only target when a sibling venue owns the contribution more directly.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against World Development for broader policy audience, JPubE for fiscal/public-finance mechanisms, AER/AEJ Applied for field-wide reach; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Development question】one sentence
【Why it is first-order for LMICs】...
【Travels beyond the subfield?】[Y/N + why]
【Suggested route】full-length / short-paper / pre-results review
【Next step】jde-literature-positioning
```
