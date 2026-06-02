---
name: crim-workflow
description: Use as the entry point for any Criminology (ASC / Wiley) manuscript. Routes to the right crim sub-skill based on where you are in the lifecycle and whether the paper is a full Article or a Research Note. Criminology is theory-forward and interdisciplinary, so the router first checks that the paper makes a criminological contribution, not just reports a crime correlation. It dispatches; it does not draft content.
---

# Criminology Workflow Router (crim-workflow)

The orchestrator for a *Criminology* submission. Figure out the stage and the **article type**, then
send the user to the matching skill. *Criminology* is the **interdisciplinary flagship of the American
Society of Criminology** — the router's first job is to make sure the paper advances a **theoretical
or measurement contribution** about crime, not just a finding about a crime dataset.

## When to trigger

- Starting a new *Criminology* paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Deciding between a full **Article** and a **Research Note**
- Returning with a decision letter (route to `crim-rebuttal`)

## First question: which article type?

| Situation | Type | Route to |
|-----------|------|----------|
| Full original study advancing theory/measurement | **Article** | normal pipeline below |
| One focused, self-contained contribution | **Research Note** (待核实 cap) | normal pipeline, tighter scope |
| Re-examining / reproducing a published finding | replication-style study | `crim-research-design` + `crim-data-and-transparency` |
| Prospective design, data not yet collected | preregister first | `crim-data-and-transparency` (preregistration) early |

> If your design is prospective, lock the pre-analysis plan **before** you see outcomes — that is what
> protects against the "fishing" critique expert reviewers will raise.

## Routing map (stage → skill)

```text
Idea / fit?                       → crim-topic-selection
Where does it sit in the field?   → crim-literature-positioning
What's the theory / mechanism?    → crim-theory-building
Is the design defensible?         → crim-research-design
Are the analyses sound?           → crim-data-analysis
Are the exhibits clear?           → crim-tables-figures
Does it read for criminology?     → crim-writing-style
Data + transparency ready?        → crim-data-and-transparency
How will it be judged?            → crim-review-process
Ready to submit?                  → crim-submission
Got an R&R / decision?            → crim-rebuttal
```

## Default order

`topic-selection → literature-positioning → theory-building → research-design → data-analysis →
tables-figures → writing-style → data-and-transparency → review-process → submission → rebuttal`

Iterate: most criminology papers loop theory ↔ design ↔ analysis several times (e.g., refitting a
trajectory model or recidivism survival) before writing-style.

## Anti-patterns

- Treating *Criminology* as a place for a bare crime-data correlation with no theoretical payoff
- Forcing a quantitative template onto qualitative or ethnographic work (the journal is interdisciplinary)
- Choosing the Research Note type for a paper that needs a full Article's evidentiary load
- Leaving the data/transparency package until acceptance instead of building it as you go

## Output format

```
【Stage】idea / positioning / theory / design / analysis / exhibits / writing / transparency / review / submit / rebut
【Type】Article / Research Note / replication-style
【Route to】crim-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — crime data + criminology software by method
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official Criminology / ASC / Wiley URLs behind every fact in this pack
