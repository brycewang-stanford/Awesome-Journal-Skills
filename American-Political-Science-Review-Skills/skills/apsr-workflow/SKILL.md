---
name: apsr-workflow
description: Use as the entry point for any American Political Science Review (APSR) manuscript. Routes to the right APSR sub-skill based on where you are in the lifecycle and which of the five tracks (Regular Article, Research Note, Replication/Reappraisal, Synthesis, Registered Report) fits. It dispatches; it does not draft content.
---

# APSR Workflow Router (apsr-workflow)

The orchestrator for an APSR submission. Figure out the stage and the **track**, then send the user
to the matching skill. APSR is a **discipline-wide generalist** journal — the router's first job is to
make sure the paper is pitched to the whole discipline, not just a subfield.

## When to trigger

- Starting a new APSR paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Deciding which of the **five tracks** fits the paper
- Returning with a decision letter (route to `apsr-rebuttal`)

## First question: which track?

| Situation | Track | Route to |
|-----------|-------|----------|
| Full original study, broad significance | **Regular Article** (< 11,000 words) | normal pipeline below |
| Focused single contribution | **Research Note** (< 7,000 words) | normal pipeline, tighter scope |
| Re-running / reassessing a published finding | **Replications and Reappraisals** | `apsr-research-design` + `apsr-transparency-and-data-policy` |
| Consolidating a literature or debate | **Synthesis** | `apsr-literature-positioning` + `apsr-theory-building` |
| Design finished, data **not yet collected/analyzed** | **Registered Report** | `apsr-review-process` (Stage 1) early |

> If the design is prospective, decide on Registered Reports **before** collecting data — that is the
> whole point of the track.

## Routing map (stage → skill)

```text
Idea / fit?                      → apsr-topic-selection
Where does it sit in the field?  → apsr-literature-positioning
What's the argument?             → apsr-theory-building
Is the design defensible?        → apsr-research-design
Are the analyses sound?          → apsr-data-analysis
Are the exhibits clear?          → apsr-tables-figures
Does it read for the discipline? → apsr-writing-style
Repro package & transparency?    → apsr-transparency-and-data-policy
How will it be judged?           → apsr-review-process
Ready to submit?                 → apsr-submission
Got an R&R / decision?           → apsr-rebuttal
```

## Default order

`topic-selection → literature-positioning → theory-building → research-design → data-analysis →
tables-figures → writing-style → transparency-and-data-policy → review-process → submission → rebuttal`

Iterate: most papers loop theory ↔ design ↔ analysis several times before writing-style.

## Discipline-wide routing check

Before selecting the next skill, force a one-minute APSR fit check:

| Check | Pass condition | Route if weak |
|-------|----------------|---------------|
| Audience | A reader outside the author's subfield can state why the question matters to political science. | `apsr-topic-selection` |
| Track | The manuscript clearly fits Regular Article, Research Note, Replication/Reappraisal, Synthesis, or Registered Report. | track table above |
| Method pluralism | The chosen method is defended on its own terms rather than forced into a quantitative template. | `apsr-research-design` |
| Transparency | Data, code, qualitative evidence, formal proof, or interpretive materials have an explicit verification plan. | `apsr-transparency-and-data-policy` |

If the paper fails the audience check, do not route to writing-style. It needs a theory or fit repair,
because APSR reviewers reject well-executed subfield papers that never become discipline-wide claims.

## Anti-patterns

- Treating APSR like a subfield journal — the contribution must reach the whole discipline
- Forcing a quantitative template onto qualitative, formal, or interpretive work (APSR judges each on its own terms)
- Choosing Registered Reports *after* seeing results (impossible — Stage 1 precedes data)
- Skipping the reproducibility package until acceptance — it is verified by the editorial office

## Output format

```
【Stage】idea / positioning / theory / design / analysis / exhibits / writing / transparency / review / submit / rebut
【Track】Regular Article / Research Note / Replication / Synthesis / Registered Report
【Route to】apsr-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — political-science data + software by method
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official APSR URLs behind every fact in this pack
