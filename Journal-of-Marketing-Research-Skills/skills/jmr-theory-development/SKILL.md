---
name: jmr-theory-development
description: Use when building the conceptual core of a Journal of Marketing Research (JMR) manuscript — deriving behavioral hypotheses with a testable process mechanism, or specifying the economic primitives and behavioral assumptions of a structural/econometric model. Adapts theory to JMR's two dominant genres without inflating into a managerial Journal-of-Marketing narrative.
---

# Theory & Mechanism Development (jmr-theory-development)

## When to trigger

- Hypotheses are descriptive ("A relates to B") with no underlying process
- A structural/econometric model lacks stated primitives, assumptions, or identifying logic
- Reviewers will ask "what is the mechanism?" or "why this functional form?"
- The conceptual section reads as a managerial story rather than a research argument

## JMR judges theory by genre

JMR welcomes a wide variety of approaches, so "theory development" means different things for its two dominant genres. Build the one that matches your paper.

### Behavioral papers — mechanism, not just prediction

- State the **psychological process** that produces the effect (e.g., a specific inference, motivation, or processing mode), not only the directional prediction.
- Derive hypotheses **a priori**; specify the **mediator** that carries the effect and the **moderator** that bounds it, with theoretical reasons each is the right one.
- Plan the **process evidence**: measured or manipulated mediation, moderation-of-process, or a process-by-moderation design — JMR reviewers expect the mechanism to be *tested*, not asserted.
- Identify the consumer/marketing phenomenon the mechanism explains; keep it a research contribution, not a list of managerial tips.

### Modeling / econometric papers — primitives and identification

- State the **economic and behavioral primitives**: utility/choice, the agent's information, the firm's problem, equilibrium concept (if any).
- Make **assumptions explicit** and justify functional-form and distributional choices; tie each to a marketing mechanism (e.g., heterogeneity, state dependence, learning).
- Spell out the **identification argument**: what variation in the data identifies each structural parameter, and what would break it.
- Connect the model to a substantive marketing question so the contribution is not "a model" but "what the model teaches about the market."

## The dual bar applies here

A mechanism with no substantive payoff, or a payoff with no credible mechanism/identification, fails JMR. The conceptual section must set up **both** what is learned **and** why the design will credibly show it.

## Anti-patterns

- HARKing — presenting post hoc patterns as a priori behavioral hypotheses.
- "Black-box" effects with no tested process in a behavioral paper.
- A structural model whose assumptions and identification are never stated.
- Letting the conceptual story drift into *Journal of Marketing* managerial framing.
- Over-claiming generalizability beyond what the mechanism or model supports.


## Theory pass for Journal of Marketing Research

Run this as a concrete capability pass. First lock the marketing construct, data or study design, inference threat, and managerial or consumer implication; then test whether the manuscript addresses marketing reviewers who expect measurement, experiments, consumer behavior, or empirical strategy to answer a marketing question.

- **Primary move:** Separate construct, mechanism, scope condition, and testable implication; refuse a theory section that only summarizes prior work.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against Marketing Science for quantitative modeling, Journal of Marketing for strategic managerial contribution, Journal of Consumer Research for consumer-theory depth; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```text
[Target] JMR
[Genre] behavioral / modeling-econometric
[Core claim] one sentence
[Behavioral] mechanism / mediator / moderator / process-evidence plan
[Modeling] primitives / assumptions / identification argument
[Dual bar] what is learned + why the design shows it
[Next skill] jmr-literature-positioning
```

## Resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md)
- [`../../resources/external_tools.md`](../../resources/external_tools.md)
