---
name: journal-of-labor-economics
description: Use when targeting Journal of Labor Economics (JOLE) or deciding whether a labor-economics manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Journal of Labor Economics (journal-of-labor-economics)

## Journal positioning

The Journal of Labor Economics (JOLE) is a field flagship for labor economics, publishing the most consequential work on wages, employment, human capital, and the transition from education to work. The paper that wins here pairs a real labor question with microdata and a credible identification strategy that other labor economists will trust. The readership is labor economists, so the contribution must advance how the field understands a labor-market mechanism — not simply estimate a familiar parameter in a new dataset.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the publisher's own site or submission system.

## When to trigger

- The author names JOLE (or a top labor field outlet) as the target venue.
- A labor paper has microdata and an identification strategy and the author is choosing between JOLE and a general or applied-micro venue.
- An applied-micro or education paper needs re-framing so the labor-market mechanism, not the dataset, is the contribution.
- The author needs JOLE's desk-reject risks and a credible labor/applied-micro alternative list before submitting.

## Scope & topic fit

- Wage determination, returns to skill, the wage structure, and earnings dynamics.
- Employment, unemployment, labor supply and demand, job search and matching, and labor-market frictions.
- Human capital, education-to-work transitions, training, and the economics of education tied to labor outcomes.
- Discrimination, immigration, family and labor, firms and workers (matched employer-employee), and labor-market institutions, when the question is genuinely about the labor market.

## Method & evidence bar

- Credible identification on microdata is the desk filter: quasi-experiments, policy variation, RDD, IV with a defensible exclusion, modern DiD estimators, or structural labor models with identified parameters.
- Naive TWFE on staggered treatment, weak instruments, and selection left unaddressed are treated as fatal; inference must match current standards.
- Structural labor work needs clearly stated assumptions and identified structural parameters, with the economics of the mechanism made transparent.
- Robustness, mechanism evidence, and attention to external validity are expected beyond a single headline coefficient.

## Structure & house style

- The introduction states the labor question, the identification strategy, the mechanism, and the headline magnitude, and says why it matters for labor economics broadly.
- Make the contribution explicit against the closest recent labor work; "first to study X with dataset Y" is not a contribution.
- The journal uses an unstructured abstract and JEL codes; an online appendix carries robustness, additional specifications, and data construction.
- Exhibits report economic magnitudes and the identifying variation clearly; the central result should be legible from one table or figure.

## Official-submission checklist

- Search the live site for "Journal of Labor Economics submission guidelines / instructions for authors" and follow the current University of Chicago Press / SOLE version, not a third-party broker's copy.
- Re-check formatting, abstract/JEL codes, reference style, anonymization expectations, the online-appendix policy, and the data & code availability requirements.
- Re-check the current replication/data-deposit expectation and any society-membership or submission routes on the editorial system.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating why a labor economist should change their view of a labor-market mechanism because of this paper.
- [ ] The contribution is stated as identification / mechanism / measurement, not as a significant coefficient.
- [ ] The introduction positions the paper against the current labor frontier on this question.
- [ ] Identification is credible on microdata; DiD/IV/RDD/structural choices are state-of-the-art and inference is correct.
- [ ] Data construction is documented and the replication package is ready.

## Common desk-reject triggers

- A familiar labor parameter re-estimated in a new dataset with no methodological or conceptual advance.
- Identification the field no longer accepts (naive TWFE on staggered adoption, weak IV, unaddressed selection).
- A correlation between labor outcomes with no source of exogenous variation and no mechanism.
- A paper that is really education, public, or development economics framed as labor.

## Re-routing decision

- General-interest labor at top-5 ambition → `american-economic-review` or `aej-applied-economics`; broad applied micro → `review-of-economics-and-statistics` or `journal-of-human-resources`.
- Taxation, transfers, and social insurance with labor outcomes → `journal-of-public-economics`.
- Labor in low/middle-income settings → `journal-of-development-economics`; labor theory/search mechanism → `journal-of-economic-theory`.
- Health-and-labor → `journal-of-health-economics`; macro-labor at the aggregate level → `journal-of-monetary-economics`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Journal of Labor Economics
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the identification on microdata clear this venue's bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / JEL / anonymization / online appendix / replication>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
