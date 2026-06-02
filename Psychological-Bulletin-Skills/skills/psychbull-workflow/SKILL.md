---
name: psychbull-workflow
description: Use as the entry point for any Psychological Bulletin manuscript. Routes to the right psychbull sub-skill based on where you are in the research-synthesis lifecycle and which synthesis type (meta-analysis, systematic review, meta-review/meta-synthesis, qualitative review) fits. Psychological Bulletin publishes syntheses, not original studies — it dispatches; it does not draft content.
---

# Psychological Bulletin Workflow Router (psychbull-workflow)

The orchestrator for a Psychological Bulletin submission. Figure out the stage and the **synthesis
type**, then send the user to the matching skill. Psychological Bulletin publishes **research
syntheses — systematic reviews and meta-analyses — not original primary studies**, so the router's
first job is to confirm the project is a *synthesis of existing work*, not a new experiment or pure
theory.

## When to trigger

- Starting a new Psychological Bulletin review/meta-analysis and unsure where to begin
- Mid-project and unsure which skill applies next
- Deciding which **synthesis type** fits (meta-analysis vs. systematic vs. qualitative review)
- Returning with a decision letter (route to `psychbull-rebuttal`)

## First question: is this even a Bulletin paper, and which type?

| Situation | Synthesis type | Route to |
|-----------|----------------|----------|
| Many comparable studies with extractable effect sizes | **Meta-analysis** | full pipeline below |
| Large literature, appraisal needed but pooling uncertain | **Systematic review** (PRISMA) | pipeline, lighter on `meta-analysis-methods` |
| Synthesizing across prior reviews or qualitative findings | **Meta-review / meta-synthesis** | `topic-selection` + `theory-integration` |
| Database resists quantitative pooling | **Qualitative / narrative review** | `topic-selection` + `theory-integration` |
| New data / a new experiment | **Off-fit** — primary study | another APA empirical journal |
| Pure new theory | **Off-fit** | *Psychological Review* |

> If you have original data or a brand-new theory with no synthesis, stop: Psychological Bulletin is
> the wrong venue. It synthesizes what already exists.

## Routing map (stage → skill)

```text
Review-worthy / meta-analyzable?    → psychbull-topic-selection
How do I find all the studies?      → psychbull-literature-search-strategy
Which studies are in, and coded?    → psychbull-inclusion-and-coding
How do I pool the effects?          → psychbull-meta-analysis-methods
What moves the effect? Bias?        → psychbull-moderators-and-bias
What does it all mean theoretically?→ psychbull-theory-integration
Are the exhibits MARS-ready?        → psychbull-tables-figures
Does it read in APA 7th / MARS?     → psychbull-writing-style
Protocol, data, code transparent?   → psychbull-open-science-and-transparency
Ready to submit?                    → psychbull-submission
Got an R&R / decision?              → psychbull-rebuttal
```

## Default order

`topic-selection → literature-search-strategy → inclusion-and-coding → meta-analysis-methods →
moderators-and-bias → theory-integration → tables-figures → writing-style →
open-science-and-transparency → submission → rebuttal`

Iterate: most syntheses loop search ↔ coding ↔ analysis as new studies surface. Register the protocol
(`open-science-and-transparency`) **before** screening, even though it appears late in the default order.

## Anti-patterns

- Treating Psychological Bulletin like a primary-study journal — it publishes syntheses, not new data
- Sending original theory here instead of to *Psychological Review*
- Starting analysis before a documented, reproducible search (no PRISMA trail)
- Pooling without a protocol — preregister before screening

## Output format

```
【Stage】topic / search / coding / analysis / moderators-bias / theory / exhibits / writing / transparency / submit / rebut
【Synthesis type】meta-analysis / systematic / meta-review / qualitative (or OFF-FIT → which journal)
【Route to】psychbull-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — synthesis lifecycle tooling by stage
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official Psychological Bulletin URLs behind every fact in this pack
