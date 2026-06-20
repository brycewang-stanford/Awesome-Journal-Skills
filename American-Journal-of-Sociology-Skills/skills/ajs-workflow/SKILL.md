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
> contribution in its own right. Live-check current Comment length/eligibility in `ajs-submission`.

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

## Calibration anchors (what an AJS trajectory feels like)

Orienting heuristics, not editorial guarantees; confirm volatile specifics against the journal's current submission guidelines.

- **Long-form, theory-first.** AJS tolerates sustained argument that runs longer than the ASR norm; the router never pushes "trim to a cap," only "make every page earn its theoretical keep," and routes a competent-but-thin paper back to `ajs-theory-building` first.
- **Craftsmanship and patience.** AJS rewards a carefully built argument and a clean evidentiary trail, so the router prioritizes depth-of-construction skills over format skills; the realistic first-round outcome for a promising paper is a substantial R&R, not acceptance.

## Stage-to-symptom dispatch (route on the complaint, not the calendar)

| The author says… | Route to |
|------------------|----------|
| "Reviewer 2 called it atheoretical." | `ajs-theory-building` |
| "It feels too narrow for a flagship." | `ajs-topic-selection` |
| "They said I reinvented the wheel." | `ajs-literature-positioning` |
| "The design can't bear my claim." | `ajs-research-design` |
| "Robustness wall, no payoff." | `ajs-data-analysis` |
| "Desk-returned before review." | `ajs-review-process` then `ajs-submission` |

## Worked micro-example (illustrative numbers)

A comparative-historical study of why labor-incorporation regimes diverged across four Latin American states opens the router unsure where to begin. The empirics are rich but the contribution reads as "these four cases differed," so the router sends them to `ajs-topic-selection`, then `ajs-theory-building` to name the mechanism (an illustrative "elite splits during a critical juncture lock in durable incorporation patterns"), then `ajs-research-design` for most-different case selection, looping theory↔design twice before prose polish. At an illustrative 19,000 words the paper is long but not disqualified — provided every section advances the argument.

## Anti-patterns

- Treating AJS like a field journal — the contribution must be in dialogue with current sociology
- Submitting an "opinion" or current-events interpretation rather than original research (AJS prejects these)
- Assuming the ASA Style Guide applies — AJS uses its **own house style** (route to `ajs-writing-style`)
- Forgetting the **$30 submission fee** / sole-author grad-student waiver (route to `ajs-submission`)
- Leaning on a bare finding with no portable theoretical payoff
- Routing as if speed-to-acceptance were the goal; the AJS path optimizes depth, and a substantial R&R is a normal milestone

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
