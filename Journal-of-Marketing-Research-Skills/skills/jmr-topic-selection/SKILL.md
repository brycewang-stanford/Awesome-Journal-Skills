---
name: jmr-topic-selection
description: Use when testing whether a marketing question is a fit for the Journal of Marketing Research (JMR) — a methods-/modeling-forward AMA flagship — rather than the managerial Journal of Marketing, the analytical Marketing Science, or the consumer-theory JCR. Locks a question that can clear both JMR's rigor bar and its substantive-contribution bar.
---

# Topic Selection & JMR Fit (jmr-topic-selection)

## When to trigger

- You have a marketing idea but are unsure JMR is the right AMA/marketing venue
- A finding is managerially interesting but you are unsure it advances research
- You cannot tell whether the paper is behavioral, modeling/econometric, or methods
- A coauthor says "this might be a JM paper" or "this is really Marketing Science"

## The JMR fit test

JMR publishes the **full spectrum of marketing topics with an emphasis on methodological rigor** and welcomes a **wide variety of data and methodological approaches**. Fit at JMR is a **dual** test, not a topic test:

1. **Rigor bar** — Can the design credibly support the claim? (clean experimental identification, a defensible causal/econometric strategy, or a well-identified structural model.)
2. **Substance bar** — Do marketing researchers *learn something* — a new substantive insight about consumers, markets, or marketing actions, or a usable methodological advance? A flawless null with no insight does not clear it.

A JMR-fit topic clears **both**. A topic that is only managerially compelling but methodologically thin belongs at *Journal of Marketing*; a topic that is only a clever model with no marketing payoff belongs at *Marketing Science*.

## Classify the genre early

| Genre                     | Center of gravity                                          | Typical JMR home |
|---------------------------|------------------------------------------------------------|------------------|
| Behavioral                | Lab/field experiments, consumer psychology, process tests  | Yes              |
| Modeling / econometric    | Choice models, structural demand, causal field data        | Yes              |
| Methods contribution      | A new estimator, measure, or research procedure            | Yes              |

The genre sets which downstream skills do the heavy lifting (`jmr-methods`, `jmr-data-analysis`).

## Sister-journal triage

- **Journal of Marketing (JM)** — manager-facing, substantive framing; lighter on method. If the lead is "what should managers do," consider JM.
- **Marketing Science** — analytical/structural quantitative marketing; if the contribution is the model itself with no broad marketing-research insight, it may fit there.
- **Journal of Consumer Research (JCR)** — deep consumer-behavior theory, interdisciplinary; if the payoff is a consumer-psychology theory rather than a method-credible marketing finding, consider JCR.

## Pre-commitment checks

- A one-sentence research question naming the marketing phenomenon and the unit (consumer, firm, market).
- A stated genre and the matching identification/estimation plan.
- An explicit "what we learn" sentence — substantive, methodological, or both.
- Feasible data/stimuli that can survive the **exact-statistics** mandate (p-values to three digits, SEs, effect sizes) and **replication** disclosure.

## Anti-patterns

- Choosing a topic on managerial appeal alone (a JM signal, not JMR).
- A method showcase with no marketing payoff (a Marketing Science risk).
- Picking a question whose data can never support credible identification.
- Deferring the genre decision until methods — it should be set now.

## Output format

```text
[Target] JMR
[Question] one sentence
[Genre] behavioral / modeling-econometric / methods
[Rigor bar] can the design support the claim? ...
[Substance bar] what do researchers learn? ...
[Sister-journal risk] JM / Marketing Science / JCR → answer
[Next skill] jmr-theory-development
```

## Resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md)
- [`../../resources/external_tools.md`](../../resources/external_tools.md)
