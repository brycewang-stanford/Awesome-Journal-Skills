---
name: jhe-writing-style
description: Use when the prose of a Journal of Health Economics (JHE) manuscript buries the question or the policy stakes — abstract, introduction, and the institutional setup. Shapes the writing so a health economist sees the contribution fast; it does not establish results or build exhibits.
---

# Writing Style (jhe-writing-style)

## When to trigger

- The abstract states what you did but not what is new for health economics or why a policymaker should care
- The introduction takes a page to reach the question
- The institutional setup is missing, so the reader cannot judge whether the variation is credible
- The paper reads as generic applied micro and could be about any market, not health

## The JHE voice

JHE prose is **policy-relevant causal writing with institutional grounding**. The reader is a health economist who wants three things fast: the health-system question, the credible estimate, and the policy or welfare lesson. The house voice is precise and institutionally literate — it names the program, the payment rule, the market — not breezy and not a methods showcase. Because review is single-anonymized, you write as an identified author to a specialist audience; the goal is to make the contribution and its institutional credibility obvious, not to obscure scope.

## Where the writing must work hardest

### Abstract (1–7 keywords required; abstract length 待核实 — re-check the guide)
- Sentence 1: the health-economics question and why it matters now.
- Sentence 2: the setting and source of variation (name the program/market).
- Sentence 3: the headline estimate with its sign and magnitude.
- Sentence 4: the mechanism / interpretation.
- Sentence 5: the policy or welfare implication. Avoid jargon a policy reader cannot parse.

### Introduction (the funnel)
1. **Open on the policy/health stake**, not the literature.
2. **State the question** in one sentence by the end of paragraph one or two.
3. **Name the setting and identifying variation** early — JHE readers judge credibility from institutions.
4. **State the headline result with its number** in the intro; do not make readers wait.
5. **Three-part contribution**: what is new empirically, what is new for the mechanism, what it means for policy.
6. **Roadmap** kept short.

### Institutional section (a JHE signature)
Devote real space to how the program/market actually works — eligibility, payment, timing, the rule that generates your variation. This is not throat-clearing; it is where a health economist decides whether to believe the design.

## Calibrating the policy claim in prose

JHE prose lives or dies on **scope discipline** — claiming exactly what the design identifies, in words. The most common overreach is treating utilization or coverage language as welfare language. Write the verb that matches the estimand: a coverage expansion "raised take-up," "shifted who pays," or "increased preventive visits" — it "improved welfare" only if a model says so. Magnitudes should be in **policy-legible units**: percentage-point changes in coverage, dollars of spending, lives or QALYs only if estimated. Avoid the two extremes JHE referees dislike — breathless overclaiming and hedged mush that never states a number.

## Reporting conventions that signal a health economist wrote this

- Report **standard errors with clustering**, not just stars; name the clustering level in prose when it matters for inference.
- Quote effects **relative to a base** ("a 4.1pp rise from a 62% baseline"), since health economists read magnitudes against utilization/coverage rates.
- Handle **skewed spending** honestly in the text — note the estimator and that the mean can understate tail effects.
- Use the field's vocabulary precisely: moral hazard, adverse vs. advantageous selection, take-up, crowd-out, intensive vs. extensive margin — misusing these signals an outsider.
- Define program-specific acronyms on first use (DRG, ACO, FFS, DUA) — JHE is international, and not every reader shares the US institutional shorthand.

## Checklist

- [ ] Abstract states question, variation, magnitude, mechanism, and policy lesson in plain language
- [ ] 1–7 English keywords selected (检索于 2026-06；以官网为准)
- [ ] Introduction reaches the question within the first page
- [ ] The headline number appears in the introduction, not only in Section 5
- [ ] The institutional setting is described concretely enough to judge the variation
- [ ] Contribution stated as empirical + mechanism + policy, not "we extend the literature"
- [ ] Prose names the health-system specifics; it could not be about a generic market

## Anti-patterns

- Burying the institutional setup so deep that the design's credibility never registers
- An abstract that lists methods but never states the policy lesson
- An introduction that opens on a literature gap instead of the health/policy stake
- Hiding the headline estimate until the results section
- Skimping on the institutional section so referees cannot judge the design
- Generic applied-micro prose with the health setting interchangeable
- Overclaiming welfare in the abstract when the design identifies only a coverage/utilization effect

## Worked vignette (illustrative)

A draft opens: "A large literature studies insurance and utilization. We contribute to it." A health economist learns nothing. The JHE rewrite opens on the stake — "Whether expanding public coverage raises *appropriate* care or merely shifts who pays is central to Medicaid policy" — states the question, names the staggered state expansions as the variation in sentence three, and gives the number: "Take-up rose 4.1pp (s.e. 1.0), concentrated in preventive visits, with no detectable change in inpatient intensity." The contribution is then empirical (identified take-up by margin), mechanistic (preventive vs. acute), and policy (which margin the expansion actually moved). The reader knows in one paragraph what the paper is and why it matters.

## Output format

```text
【Journal】Journal of Health Economics
【Skill】jhe-writing-style
【Abstract】question + variation + magnitude + mechanism + policy? [Y/N]
【Intro funnel】question by page 1; headline number in intro? [Y/N]
【Institutional section】setting concrete enough to judge the design? [Y/N]
【Contribution】empirical + mechanism + policy stated? [Y/N]
【Voice】institutionally literate, not generic applied micro? [Y/N]
【Next skill】jhe-replication-package
```

## Handoff boundary

This is a late-stage polish; it makes the settled result land, it does not change the science. Do not rewrite the introduction before identification, the headline estimate, and the exhibits have stabilized — prose written around a moving number has to be redone. When the abstract and intro carry the question, the number, and the policy lesson cleanly, hand off to `jhe-replication-package` to assemble the deposit and Data Availability Statement.
