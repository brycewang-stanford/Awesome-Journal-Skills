---
name: jmr-contribution-framing
description: Use when turning results into an explicit contribution statement for a Journal of Marketing Research (JMR) manuscript — clearing JMR's dual bar by stating both the substantive/theoretical insight and, where relevant, the methodological advance. Frames why marketing researchers should care because the design is credible.
---

# Contribution Framing (jmr-contribution-framing)

## When to trigger

- Results exist but the "so what for marketing research" is thin or implicit
- A reviewer says the contribution is "incremental" or "an application"
- You are unsure whether to lead with the substantive insight or the method
- The discussion restates results instead of stating what was learned

## Clear JMR's dual bar explicitly

JMR is the AMA's methods-forward flagship, and it judges papers on **two** contributions at once. State both, in the introduction and the discussion:

1. **Substantive / theoretical** — What do we now know about consumers, markets, or marketing actions that we did not before? What belief is changed, qualified, or newly established?
2. **Methodological credibility / advance** — Why is this believable? Either the design credibly identifies the effect (so the substantive claim is trustworthy), or the paper itself contributes a new method/measure that other researchers can reuse.

A paper that nails one bar but not the other is the canonical JMR reject: a credible-but-uninteresting result, or an interesting-but-unidentified claim.

## Lead with the right bar for your genre

- **Behavioral** — lead with the substantive insight and the *mechanism*; the credibility comes from the converging experiments and tested process.
- **Modeling / econometric** — lead with the substantive market insight the model/identification delivers; if the estimator or identification is itself novel, frame that as a secondary methodological contribution.
- **Methods paper** — the method *is* the primary contribution; show it solves a real marketing-research problem better than existing tools (with an application that demonstrates payoff).

## Write the contribution sentences

- A one-sentence **substantive** claim: "We show that [X] changes [marketing outcome] because [mechanism / market force]."
- A one-sentence **credibility/method** claim: "This is credible because [identification / converging designs]" or "We introduce [method] that lets researchers [do something previously infeasible]."
- A **boundary** sentence: where the effect holds and where it does not — JMR rewards honest scope over over-claiming.

## Contrast with the sister journals

If the only contribution is managerial implications, reviewers will ask why this is not a *Journal of Marketing* paper; if it is only a model with no marketing payoff, why not *Marketing Science*. Pre-empt this by stating the **research** (not just managerial) advance.

## Anti-patterns

- Discussion that summarizes findings instead of naming the contribution.
- Claiming a methodological contribution that is really a routine application.
- Managerial-implications-as-contribution (a *Journal of Marketing* signal).
- Over-generalizing beyond the design's identified scope.


## Contribution pass for Journal of Marketing Research

Run this as a concrete capability pass. First lock the marketing construct, data or study design, inference threat, and managerial or consumer implication; then test whether the manuscript addresses marketing reviewers who expect measurement, experiments, consumer behavior, or empirical strategy to answer a marketing question.

- **Primary move:** Translate the result into who learns what, which mechanism changes, and which alternative explanation is ruled out; keep the claim narrower than the evidence.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against Marketing Science for quantitative modeling, Journal of Marketing for strategic managerial contribution, Journal of Consumer Research for consumer-theory depth; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```text
[Target] JMR
[Genre] behavioral / modeling-econometric / methods
[Substantive claim] one sentence
[Credibility/method claim] one sentence
[Boundary] where it holds / fails
[Dual bar] both cleared? gaps ...
[Next skill] jmr-tables-figures
```

## Resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md)
- [`../../resources/external_tools.md`](../../resources/external_tools.md)
