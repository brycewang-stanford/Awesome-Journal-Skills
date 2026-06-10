---
name: demog-workflow
description: Use as the entry point for any Demography (PAA / Duke University Press) manuscript. Routes to the right Demography sub-skill based on where you are in the lifecycle and which article type (Research Article, Research Note, Commentary) fits. It dispatches; it does not draft content.
---

# Demography Workflow Router (demog-workflow)

The orchestrator for a *Demography* submission. Figure out the stage and the **article type**, then
send the user to the matching skill. Demography is the **multidisciplinary flagship of the Population
Association of America** — the router's first job is to confirm the paper poses a genuine
**population-science** question (how populations change, or why, and with what consequences), not a
study that merely uses demographic data in passing.

## When to trigger

- Starting a new Demography paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Deciding which **article type** fits (Article vs. Note vs. Commentary)
- Returning with a decision letter (route to `demog-rebuttal`)

## First question: which article type?

| Situation | Type | Route to |
|-----------|------|----------|
| Full original population study | **Research Article** (<= 8,000 words) | normal pipeline below |
| One focused, self-contained contribution | **Research Note** (<= 4,000 words) | normal pipeline, tighter scope |
| Short response/perspective on published work or a debate | **Commentary** (<= 2,000 words) | `demog-literature-positioning` + `demog-writing-style` |

> Word caps are **main-text** counts (exclude abstract, keywords, footnotes, acknowledgments). Confirm
> current caps on the official page (see 待核实).

## Routing map (stage -> skill)

```text
Idea / fit?                       -> demog-topic-selection
Where does it sit in the field?   -> demog-literature-positioning
What's the argument/mechanism?    -> demog-theory-building
Is the demographic design sound?  -> demog-research-design
Are the analyses sound?           -> demog-data-analysis
Are the exhibits clear?           -> demog-tables-figures
Does it read for population sci.? -> demog-writing-style
Data statement & repro package?   -> demog-data-and-reproducibility
How will it be judged?            -> demog-review-process
Ready to submit (ScholarOne)?     -> demog-submission
Got an R&R / decision?            -> demog-rebuttal
```

## Default order

`topic-selection -> literature-positioning -> theory-building -> research-design -> data-analysis ->
tables-figures -> writing-style -> data-and-reproducibility -> review-process -> submission -> rebuttal`

Iterate: most demographic papers loop theory <-> design <-> analysis several times (e.g., choosing
among life-table, decomposition, event-history, or APC framings) before writing-style.

## Anti-patterns

- Treating Demography like a generic applied-stats venue — the question must be about population change
- Forcing one demographic method (e.g., a regression) when the question calls for a life table, a
  decomposition, or an event-history model
- Calling the $1,000 editorial-management fee an open-access charge (Demography is free to read via S2O)
- Leaving the data availability statement until acceptance — build it as you go


## Router pass for Demography

Run this as a concrete capability pass. First lock the demographic process, data source, time scale, selection/migration/mortality issue, and uncertainty; then test whether the manuscript addresses population-science reviewers who inspect demographic process, measurement, cohort/period logic, and population validity.

- **Primary move:** Run the pack as fit gate, evidence gate, writing gate, source-map gate, and output contract; stop when a gate lacks evidence.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against Population and Development Review for policy synthesis, JMF for family process, Social Forces for broader sociology; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Stage】idea / positioning / theory / design / analysis / exhibits / writing / data / review / submit / rebut
【Type】Research Article / Research Note / Commentary
【Route to】demog-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — population data + demographic software by method
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official Demography URLs behind every fact in this pack
