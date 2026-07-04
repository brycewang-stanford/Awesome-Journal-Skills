---
name: jpe-workflow
description: Use when deciding which jpe-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a Journal of Political Economy (JPE) manuscript. Routes — it does not replace — the specialized skills.
---

# JPE Workflow Router (jpe-workflow)

## Overview

This is the router. It does not replace any specialized skill. It tells you **which jpe-* skill to use given where you are right now** in a Journal of Political Economy (JPE) submission.

Default assumption: unless the user says otherwise, treat the target as **JPE proper** (University of Chicago Press; lead editor Esteban Rossi-Hansberg). The same routing applies to the **2023-launched companion journals** — JPE Microeconomics (lead editor John List) and JPE Macroeconomics (lead editor Greg Kaplan) — but those are narrower in scope; flag that routing choice in `jpe-topic-selection`. Note two JPE-specific gates that shape the whole pipeline: a **non-refundable $250 / $125 submission fee** with a 3-referee-reports waiver, and a conditional accept that triggers the **JPE Data Editor** verifying a DCAS package deposited to the **JPE Dataverse**.

The single organizing question behind every JPE skill: **"What does economic theory predict here, and does the evidence bear it out?"** A Chicago referee will read the paper as an economic argument, not a regression table. Internal consistency of that argument is scrutinized harder than at most journals.

## When to trigger

- The user asks "what should I do next?" on a JPE-targeted paper
- A draft is handed over and the current bottleneck is unclear
- Work is bouncing between modeling, empirics, and writing with no clear order
- A JPE decision letter (reject / R&R) has arrived and the user needs to switch into response mode

## Routing table

| Current symptom                                                        | Next skill                  |
|------------------------------------------------------------------------|-----------------------------|
| Idea is a correlation in search of a question; no economic mechanism   | `jpe-topic-selection`       |
| Unsure whether the paper is "JPE-shaped" vs. a field journal           | `jpe-topic-selection`       |
| Lit review reads as a list; contribution not framed in Chicago author-date | `jpe-literature-positioning`|
| Empirics are OLS + controls; causal claim not defended                 | `jpe-identification`        |
| Reduced-form result has no model / mechanism behind it                 | `jpe-theory-model`          |
| Structural model present but identification of parameters is unclear   | `jpe-theory-model`          |
| Main result exists but rests on a single specification                 | `jpe-robustness`            |
| Tables overloaded; figures not carrying the economic story             | `jpe-tables-figures`        |
| Prose is verbose / hedged / not in JPE's spare analytical voice        | `jpe-writing-style`         |
| Conditionally accepted; need a DCAS package for the JPE Data Editor / JPE Dataverse | `jpe-replication-package` |
| Want to anticipate the price-theory / GE objections a referee will raise | `jpe-referee-strategy`    |
| Ready to submit; need Editorial Express preflight + $250/$125 fee/format check | `jpe-submission`     |
| Received an R&R; need to draft the response letter                     | `jpe-rebuttal`              |

## Default order

1. `jpe-topic-selection` — lock the economic question and the mechanism it tests
2. `jpe-literature-positioning` — situate the contribution in the economics literature (Chicago author-date)
3. `jpe-identification` — make the causal/empirical claim credible
4. `jpe-theory-model` — the model or mechanism that gives the result its economic meaning
5. `jpe-robustness` — kill the alternative explanations a referee will float
6. `jpe-tables-figures` — finalize main exhibits so each carries economic content
7. `jpe-writing-style` — tighten prose into JPE's analytical register (polish)
8. `jpe-referee-strategy` — pre-mortem the report you expect, patch holes
9. `jpe-replication-package` — assemble data/code to DCAS standard for the JPE Data Editor / JPE Dataverse
10. `jpe-submission` — Editorial Express preflight ($250/$125 fee, Chicago author-date format, single-blind)
11. `jpe-rebuttal` — after the R&R lands

> `jpe-writing-style` is a **late polish** stage. Do not chase prose before the identification and the model are sound. `jpe-theory-model` and `jpe-identification` often iterate together — for JPE the model frequently disciplines the empirical specification, not the reverse.

## Decision heuristics

- "I have a clean causal effect but no story for *why*" → `jpe-theory-model` (a bare effect is not a JPE paper)
- "I have a model but the empirics are an afterthought" → `jpe-identification`
- "My intro cites everyone but never says what economics learns" → `jpe-literature-positioning`
- "DID uses TWFE with staggered timing and I haven't addressed heterogeneity bias" → `jpe-identification`
- "All my evidence is one regression" → `jpe-robustness`
- "A referee will say this ignores general equilibrium / selection / incentives" → `jpe-referee-strategy`
- "Submitting tomorrow" → `jpe-submission`
- "Got three referee reports" → `jpe-rebuttal`

## Pipeline status manifest

Track where the manuscript actually is before asking "what next?". Keep this block at the top of the project notes and update it after every working session; the first `blocked` or `todo` row is the skill to invoke.

```yaml
jpe_pipeline:
  target: JPE proper          # or: JPE Micro | JPE Macro — decide in jpe-topic-selection
  stages:
    - {skill: jpe-topic-selection,        status: done,    gate: "economic question + mechanism locked"}
    - {skill: jpe-literature-positioning, status: done,    gate: "contribution stated in Chicago author-date frame"}
    - {skill: jpe-identification,         status: blocked, gate: "causal claim defensible to a Chicago referee"}
    - {skill: jpe-theory-model,           status: todo,    gate: "model disciplines the empirical specification"}
    - {skill: jpe-robustness,             status: todo,    gate: "alternative explanations killed, not just noted"}
    - {skill: jpe-tables-figures,         status: todo,    gate: "each exhibit carries economic content"}
    - {skill: jpe-writing-style,          status: todo,    gate: "spare analytical register throughout"}
    - {skill: jpe-referee-strategy,       status: todo,    gate: "price-theory / GE objections pre-answered"}
    - {skill: jpe-replication-package,    status: todo,    gate: "DCAS package ready for JPE Dataverse deposit"}
    - {skill: jpe-submission,             status: todo,    gate: "Editorial Express preflight; $250/$125 fee cleared"}
    - {skill: jpe-rebuttal,               status: n/a,     gate: "activates only after an R&R decision"}
  rule: "route to the first stage whose status is blocked or todo; never polish downstream of a blocked gate"
```

## Differences vs. QJE / Econometrica / REStud stacks

JPE sits among the top-five but has a distinct house taste:

- **JPE**: premium on a tight economic *mechanism* and price-theoretic reasoning; reduced-form and structural both welcome, but the result must mean something for economic theory.
- **QJE**: prizes a striking, important question and a clean natural experiment; mechanism valued but identification often leads.
- **Econometrica**: methodological / theoretical novelty and formal rigor lead; pure applied work needs a method or theory contribution.
- **REStud**: technical depth with a younger-frontier slant; theory and structural empirics both core.

If the paper is methodological with no economic application, Econometrica may fit better. If it is an atheoretical policy evaluation, reconsider the framing in `jpe-topic-selection` before targeting JPE. And unlike its peers, JPE offers an in-house routing choice between the flagship and the JPE Micro / JPE Macro companions — use it deliberately.

## Anti-patterns

- **Do not** skip `jpe-theory-model` and present a reduced-form correlation as a finished JPE paper — referees ask "what is the economics?"
- **Do not** let `jpe-tables-figures` polish exhibits while the identification is still contested
- **Do not** let `jpe-rebuttal` draft a response letter before the manuscript itself has been revised
- **Do not** treat `jpe-submission` as the first stop; preflight is worthless if the economic argument is not yet sound
- **Do not** defer reproducible code to post-accept; the JPE Data Editor verifies the package before publication
