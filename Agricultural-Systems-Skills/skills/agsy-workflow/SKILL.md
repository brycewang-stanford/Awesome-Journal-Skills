---
name: agsy-workflow
description: Use as the entry point for any Agricultural Systems (AgSy) manuscript. Routes to the right AgSy sub-skill based on where you are in the lifecycle and which article type (research paper, short communication, perspective, comment, review) fits. AgSy is a systems-science journal, so the router's first job is to confirm there is a real systems question — interactions, hierarchical levels, trade-offs — not a single-factor field trial. It dispatches; it does not draft content.
---

# Agricultural Systems Workflow Router (agsy-workflow)

The orchestrator for an Agricultural Systems submission. Figure out the stage and the **article type**,
then send the user to the matching skill. AgSy is defined by **interactions across components and
hierarchical levels** (field → farm → landscape → region → food system) — the router's first job is to
make sure the paper poses a genuine **systems** question, analyzed with **modelling and trade-offs**,
not a single-factor agronomic trial.

## When to trigger

- Starting a new AgSy paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Deciding which **article type** fits the work
- Returning with a decision letter (route to `agsy-revision-and-rebuttal`)

## First question: is this a systems paper, and which type?

| Situation | Article type | Route to |
|-----------|--------------|----------|
| Full systems study (interactions, modelling, trade-offs) | **Research paper** (~8,000 words) | normal pipeline below |
| One focused systems result | **Short communication** (~4,000 words) | normal pipeline, tighter scope |
| Forward-looking opinion on agricultural-systems science | **Perspective** (~2,000 words, rapid review) | `agsy-writing-style` + `agsy-impact-and-implications` |
| Short response to a published AgSy paper | **Comment** (~1,000 words) | `agsy-literature-positioning` + `agsy-writing-style` |
| Integrative synthesis of a systems literature | **Review** (verify scope) | `agsy-literature-positioning` + `agsy-systems-framing-and-modeling` |

> If the work is really a single-treatment field trial with no interactions, trade-offs, or model, it
> is **off-fit** — reframe it as a systems question or send it to a field-crops/agronomy journal.

## Routing map (stage → skill)

```text
Is it a real systems question?     → agsy-topic-selection
Where does it sit in the field?    → agsy-literature-positioning
System boundaries + the model?     → agsy-systems-framing-and-modeling
Is the model evaluated soundly?    → agsy-data-and-model-evaluation
Do exhibits show interactions?     → agsy-figures-and-tables
Does it read clearly?              → agsy-writing-style
Why does the result matter?        → agsy-impact-and-implications
Data + code + models shareable?    → agsy-reproducibility-and-data-policy
How will it be judged?             → agsy-review-process
Ready to submit?                   → agsy-submission
Got reviews / a decision?          → agsy-revision-and-rebuttal
```

## Default order

`topic-selection → literature-positioning → systems-framing-and-modeling → data-and-model-evaluation →
figures-and-tables → writing-style → impact-and-implications → reproducibility-and-data-policy →
review-process → submission → revision-and-rebuttal`

Iterate: most systems papers loop framing ↔ modelling ↔ evaluation several times before writing-style.

## Anti-patterns

- Treating AgSy like a field-trial agronomy journal — the contribution must be a systems analysis
- A model run with no description, calibration, or evaluation (a black box)
- Skipping the decision/impact step — AgSy wants relevance, not a methods demo
- Leaving data, code, and the model undocumented until acceptance

## Output format

```
【Stage】idea / positioning / framing / evaluation / exhibits / writing / impact / repro / review / submit / revise
【Article type】Research paper / Short communication / Perspective / Comment / Review
【Systems question?】real interactions/trade-offs? [Y/N]
【Route to】agsy-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — systems models + calibration/uncertainty software by scale
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official AgSy URLs behind every fact in this pack
