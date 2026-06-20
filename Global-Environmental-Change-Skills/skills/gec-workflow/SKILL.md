---
name: gec-workflow
description: Use as the entry point for any Global Environmental Change (GEC) manuscript. Routes to the right GEC sub-skill based on where you are in the lifecycle and whether the paper fits a Research Article or a shorter format. GEC is interdisciplinary and social-science-leading; the router's first job is to make sure the human and policy dimensions are front and centre. It dispatches; it does not draft content.
---

# GEC Workflow Router (gec-workflow)

The orchestrator for a *Global Environmental Change* submission. Figure out the stage and the **format**,
then send the user to the matching skill. GEC publishes work on the **human and policy dimensions** of
global environmental change — so the router's first job is to confirm the paper has a **significant
social-science component** and a real-world / policy payoff, not just an environmental result.

## When to trigger

- Starting a new GEC paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Deciding whether the work fits a full **Research Article** or a shorter format
- Returning with a decision letter (route to `gec-revision-and-rebuttal`)

## First question: which format?

| Situation | Format | Route to |
|-----------|--------|----------|
| Full original study, broad significance | **Research Article** (up to 8,000 words) | normal pipeline below |
| Distinctive viewpoint / agenda-setting argument | **Perspective** (up to 3,000 words) | `gec-conceptual-framework` + `gec-writing-style` |
| Integrative synthesis needing methods/data analysis | Usually **Research Article** | `gec-literature-positioning` + `gec-conceptual-framework` |
| Prospective design, data not yet collected | plan transparency early | `gec-research-design` + `gec-review-process` |

> The 8,000-word and 3,000-word caps were refreshed from the official Guide on 2026-06-20. Re-check the
> live Guide before filing, especially for special issue instructions.

## Routing map (stage → skill)

```text
Idea / fit?                        → gec-topic-selection
Where does it sit in the field?    → gec-literature-positioning
What is the framework?             → gec-conceptual-framework
Is the design defensible?          → gec-research-design
Are the analyses sound?            → gec-data-analysis
Are the exhibits clear?            → gec-figures-and-tables
Does it read for a broad audience? → gec-writing-style
So what for policy / practice?     → gec-policy-relevance-and-implications
How will it be judged?             → gec-review-process
Ready to submit?                   → gec-submission
Got an R&R / decision?             → gec-revision-and-rebuttal
```

## Default order

`topic-selection → literature-positioning → conceptual-framework → research-design → data-analysis →
figures-and-tables → writing-style → policy-relevance-and-implications → review-process → submission →
revision-and-rebuttal`

Iterate: most papers loop framework ↔ design ↔ analysis several times before writing-style.

## Anti-patterns

- Treating GEC as a natural-science venue — the human / policy dimension must lead
- Skipping the conceptual framework and presenting results with no organizing lens
- Forcing one method template onto every paper (GEC welcomes quantitative, qualitative, and mixed work)
- Leaving policy relevance as an afterthought rather than a designed-in contribution

## Output format

```
【Stage】idea / positioning / framework / design / analysis / exhibits / writing / policy / review / submit / revise
【Format】Research Article / Perspective / Review / other
【Route to】gec-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — data sources + software by method
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official GEC URLs behind every fact in this pack
