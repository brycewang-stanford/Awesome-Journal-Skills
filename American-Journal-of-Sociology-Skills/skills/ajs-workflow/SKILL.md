---
name: ajs-workflow
description: Use as the entry point for any American Journal of Sociology (AJS) manuscript. Routes to the right AJS sub-skill based on where you are in the lifecycle and whether the piece is a research article, a Comment/Reply, or a book-review response. It dispatches; it does not draft content.
---

# AJS Workflow Router (ajs-workflow)

The orchestrator for an AJS submission. Figure out the stage and the **piece type**, then send the
user to the matching skill. AJS is the discipline's **oldest** journal — generalist sociology with a
premium on **theoretical ambition** and a distinctive **student-run, double-blind** review run out of
the University of Chicago Department of Sociology. The router's first job is to make sure the paper is
**in dialogue with current sociology** (AJS "prejects" papers that are not).

## When to trigger

- Starting a new AJS paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Deciding whether the piece is a **research article** or a **Comment/Reply** on a published AJS paper
- Returning with a decision letter (route to `ajs-rebuttal`)

## First question: which piece type?

| Situation | Type | Route to |
|-----------|------|----------|
| Full original sociological study | **Research article** | normal pipeline below |
| Engaging/critiquing a specific published AJS article | **Comment** (then author **Reply**) | `ajs-literature-positioning` + `ajs-rebuttal` |
| Reviewing a book | **Book review** (usually invited) | `ajs-writing-style` (out of scope for the article pipeline) |

> AJS has a long **Comment-and-Reply tradition**: a focused critique of a published finding can be a
> contribution in its own right. Confirm current Comment length/eligibility (待核实) in `ajs-submission`.

## Routing map (stage → skill)

```text
Idea / fit?                       → ajs-topic-selection
In dialogue with which lit?       → ajs-literature-positioning
What is the theoretical payoff?   → ajs-theory-building
Is the design defensible?         → ajs-research-design
Are the analyses sound?           → ajs-data-analysis
Are the exhibits clear?           → ajs-tables-figures
Does it read for sociology?       → ajs-writing-style
Data / transparency in order?     → ajs-data-and-transparency
How will it be judged?            → ajs-review-process
Ready to submit?                  → ajs-submission
Got an R&R / writing a Reply?     → ajs-rebuttal
```

## Default order

`topic-selection → literature-positioning → theory-building → research-design → data-analysis →
tables-figures → writing-style → data-and-transparency → review-process → submission → rebuttal`

Iterate: AJS papers typically loop theory ↔ design ↔ analysis several times before writing-style —
the theoretical contribution usually sharpens late.

## Anti-patterns

- Treating AJS like a field journal — the contribution must be in dialogue with current sociology
- Submitting an "opinion" or current-events interpretation rather than original research (AJS prejects these)
- Assuming the ASA Style Guide applies — AJS uses its **own house style** (route to `ajs-writing-style`)
- Forgetting the **$30 submission fee** / sole-author grad-student waiver (route to `ajs-submission`)
- Leaning on a bare finding with no portable theoretical payoff

## Output format

```
【Stage】idea / positioning / theory / design / analysis / exhibits / writing / transparency / review / submit / rebut
【Type】research article / Comment / Reply / book review
【Route to】ajs-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — sociology data + software by tradition
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official AJS URLs behind every fact in this pack
