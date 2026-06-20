---
name: eursr-workflow
description: Use when starting or routing any European Sociological Review (ESR) manuscript and unsure which skill applies. Routes to the right ESR sub-skill based on the lifecycle stage and the manuscript type (research Article ~8,000 words vs. Comment/Reply vs. Data Brief). It dispatches; it does not draft content.
---

# ESR Workflow Router (eursr-workflow)

The orchestrator for an ESR submission. ESR is the **flagship quantitative-sociology journal** of the
European Consortium for Sociological Research (ECSR), published by **Oxford University Press**. The
router's first job is to confirm the work is a **rigorous quantitative contribution** — usually
comparative and/or longitudinal — and to send the user to the matching skill for their stage.

## When to trigger

- Starting a new ESR paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Deciding among a full **Article**, a **Comment/Reply**, and a **Data Brief**
- Returning with a decision letter (route to `eursr-rebuttal`)

## First question: manuscript type

| Situation | Type | Note |
|-----------|------|------|
| Full quantitative study, comparative/longitudinal | **Article** (~8,000 words incl. endnotes + references) | the main pipeline below |
| Critique of / reply to a published ESR piece | **Comment/Reply** | tight scope; engage the original directly |
| Showcasing a data source for the community | **Data Brief** | describe design/sampling/content + sociological potential |

Then confirm the **method shape**, because design and analysis advice turn on it:
cross-national comparative · panel/longitudinal · multilevel · event-history · causal-inference ·
SEM/measurement.

## Routing map (stage → skill)

```text
Idea / fit?                          → eursr-topic-selection
Where does it sit in the field?      → eursr-literature-positioning
What's the theoretical argument?     → eursr-theory-building
Is the comparative/panel design sound? → eursr-research-design
Are the models defensible?           → eursr-data-analysis
Are the exhibits clear?              → eursr-tables-figures
Does it read in ESR house style?     → eursr-writing-style
Replication package + DAS ready?     → eursr-transparency-and-data
How will it be judged?               → eursr-review-process
Ready to submit?                     → eursr-submission
Got an R&R / decision?               → eursr-rebuttal
```

## Default order

`topic-selection → literature-positioning → theory-building → research-design → data-analysis →
tables-figures → writing-style → transparency-and-data → review-process → submission → rebuttal`

Iterate: comparative and multilevel papers loop theory ↔ design ↔ analysis as the cross-national
data dictate.

## Symptom-to-skill dispatch

ESR rewards a tight pairing of a portable sociological mechanism with a quantitative design that
defeats the leading confound. Most symptoms map cleanly to one sub-skill — use this lookup before
defaulting to the linear order.

| Symptom you arrive with | Likely root | Route to |
|--------------------------|-------------|----------|
| "A reader says it's just one-country description" | fit / comparative reach | eursr-topic-selection |
| "Reviewer says I missed the European literature" | cross-national positioning | eursr-literature-positioning |
| "It's called atheoretical / variable-driven" | no portable mechanism | eursr-theory-building |
| "Reviewer doubts the comparative or causal logic" | design | eursr-research-design |
| "They want robustness / the right level of clustering" | analysis | eursr-data-analysis |
| "An exhibit is unclear" | exhibits | eursr-tables-figures |
| "Over 8,000 words / reads heavy" | prose + length | eursr-writing-style |
| "Where is the replication package?" | transparency mandate | eursr-transparency-and-data |
| "What will reviewers want?" | expectations | eursr-review-process |
| "Submitting tomorrow" | preflight | eursr-submission |
| "Got an R&R" | response letter | eursr-rebuttal |

## Worked micro-example (illustrative routing)

A user arrives mid-project with a cross-national education study and a vague worry.

```
User: "I have ESS data for 20 countries and good multilevel models, but a colleague says it's
  'just a country-comparison, not an ESR contribution.'"
Router read: the worry is theoretical portability, not data → start at eursr-theory-building (name the
  macro–micro mechanism the country variation identifies), then eursr-literature-positioning (the live
  comparative debate), then eursr-research-design (what the cross-national variation lets you rule out).
Type: full quantitative study → Article (~8,000 words incl. references), not a Comment.
Then: eursr-data-analysis (multilevel SEs, country-level df) → eursr-tables-figures →
  eursr-transparency-and-data (replication package early, since the work is statistical).
```

The router resists the linear default and sends the comparative paper to theory and positioning first,
where its fit risk actually lives.

## Referee-stage pushback → which skill answers it

- *"One-country result dressed as comparative."* → eursr-topic-selection then eursr-research-design
  (what the cross-national contrast identifies).
- *"Country-level inference with too few clusters."* → eursr-data-analysis (degrees of freedom,
  appropriate SEs / Bayesian or design-based alternatives).
- *"Anonymity is broken."* → eursr-submission masking sweep before re-upload.

## Calibration anchors

- **Quantitative rigor on a portable mechanism is the gate.** ESR's first question is whether a
  defensible quantitative design carries a mechanism European sociology can use — route there when fit
  is in doubt.
- **Comparative/longitudinal data set the path.** Cross-national and panel designs loop theory ↔ design
  ↔ analysis; do not force them through a single linear pass.
- **Transparency is now load-bearing.** For statistical/computational work a replication package is
  required at conditional acceptance (submissions from 1 Jan 2025); plan it early, not at the end.

## Anti-patterns

- Treating ESR like a general or US-sociology journal — the target is rigorous European quantitative work
- Forcing a single-country descriptive paper into a comparative frame after the fact
- Padding a focused critique into an Article when a Comment/Reply fits
- Forgetting the Data Availability Statement and (for statistical work) the replication-package mandate

## Output format

```
【Stage】idea / positioning / theory / design / analysis / exhibits / writing / transparency / review / submit / rebut
【Type】Article / Comment-Reply / Data-Brief
【Method shape】comparative / panel / multilevel / event-history / causal / SEM
【Route to】eursr-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — European data (ESS / EU-SILC / SOEP / EVS) + software by method
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official ESR / OUP / ECSR URLs behind every fact in this pack
