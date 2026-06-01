---
name: jole-topic-selection
description: Use when deciding whether a research question fits the Journal of Labor Economics (JOLE) — a general-interest labor-economics quarterly — and how to frame it so it matters to labor economists broadly, not just one niche. Tests fit; it does not run the analysis.
---

# Topic Selection (jole-topic-selection)

## When to trigger

- You have data or a result but are unsure it is a JOLE-fit labor question
- The question feels narrow ("so what for labor economics?" is unclear)
- You are choosing among several possible angles on the same dataset
- You need to decide between JOLE and a non-labor general-interest journal

## The JOLE scope bar

JOLE is a general-interest, peer-reviewed **quarterly** for **labor economics** — the study of behavior and outcomes in labor markets — and the official journal of the **Society of Labor Economists (SOLE)**. It publishes both **theoretical and applied/empirical** work. In-scope core topics:

- **Wages, earnings, and inequality** (returns to skill, wage structure, firm pay premia)
- **Employment and unemployment** (job search, matching, separations, labor demand)
- **Human capital and education** (schooling, training, returns, skill formation)
- **Labor supply and demand** (hours, participation, elasticities)
- **Household and family economics** (intra-household allocation, fertility, marriage and work)
- **Discrimination** (race, gender, taste-based vs. statistical)
- **Unions and labor-market institutions** (collective bargaining, minimum wages)
- **Migration and immigration** (labor-market effects, selection, assimilation)
- **Labor-market policy** (UI, EITC, employment protection, active labor-market programs)

The fit test is not "is this about workers?" but **"would a labor economist outside my subfield find the answer first-order?"** JOLE rewards a clean labor question with credible identification and a lesson that travels beyond the specific setting.

## Fit diagnostics

- **Labor-first, not labor-adjacent.** A finance or macro paper that mentions employment is usually a better fit elsewhere; a labor paper using a macro shock for identification can fit JOLE if the question is about the labor market.
- **General-interest within labor.** A result of interest only to one narrow literature (e.g., a parameter for a single program with no broader lesson) is off-fit; a field journal or specialty outlet may fit better.
- **Theory or empirics both welcome — but disciplined.** A theoretical labor paper needs a labor-economic payoff; an empirical one needs credible identification and replicable data (JOLE publishes empirical work only if data are documented and available).
- **Travels beyond the setting.** State the lesson a labor economist takes away even if they never study your exact country/policy/firm.

## Sharpening the question

1. Write the question in one sentence a labor economist in another subfield would care about.
2. Name the **margin** (wages? employment? hours? human capital? matching?) the paper moves.
3. Name the **identifying variation** that lets you answer it credibly (preview of jole-identification-strategy).
4. State the **broader labor lesson** in one sentence ("beyond this reform/firm/country").
5. Sanity-check against JOLE's word economy (~20,000 words) — a question that needs a 60-page treatment may be two papers.

## Checklist

- [ ] The question is squarely **labor economics**, not labor-adjacent
- [ ] It is **general-interest within labor**, not niche-only
- [ ] The margin (wages / employment / human capital / supply / etc.) is named
- [ ] A credible identifying variation exists (or a disciplined theoretical contribution)
- [ ] The empirical core is replicable (data documented and available)
- [ ] The broader labor lesson "beyond this setting" is statable in one sentence

## Anti-patterns

- A labor-adjacent paper (finance/macro/IO) dressed as labor with no labor question at its core
- A narrow program evaluation with no lesson beyond the program
- "It's about workers" as the entire fit argument
- An empirical question whose data could never be made available for replication
- A scope so large it cannot be argued within JOLE's word economy

## Output format

```
【Labor question】one sentence:
【Margin】wages / employment / human capital / supply / family / discrimination / institutions / migration
【Identifying variation】preview:
【General-interest within labor?】[Y/N] — why
【Broader labor lesson】one sentence:
【Verdict】JOLE-fit / refocus / try a field journal
【Next step】jole-literature-positioning
```
