---
name: aerj-workflow
description: Use as the entry point for any American Educational Research Journal (AERJ) manuscript. Routes to the right AERJ sub-skill based on where you are in the lifecycle and which of the journal's two separately edited sections — Social and Institutional Analysis (SIA) or Teaching, Learning, and Human Development (TLHD) — fits the paper. It dispatches; it does not draft content.
---

# AERJ Workflow Router (aerj-workflow)

The orchestrator for an AERJ submission. Figure out the stage and the **section**, then send the user
to the matching skill. AERJ is a **field-wide generalist** journal organized into **two separately
edited sections** — the router's first job is to make sure the paper is pitched to the whole field and
routed to the right section.

## When to trigger

- Starting a new AERJ paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Deciding whether the paper belongs in **SIA** or **TLHD**
- Returning with a decision letter (route to `aerj-rebuttal`)

## First question: which section?

| Situation | Section | Then |
|-----------|---------|------|
| Policy, governance, equity, organizations, institutions | **Social and Institutional Analysis (SIA)** | normal pipeline below |
| Teaching, learning, instruction, human development | **Teaching, Learning, and Human Development (TLHD)** | normal pipeline below |
| Sits across both | name the **better-fit** section | say why in the cover letter |

> Both sections take quantitative, qualitative, and mixed-methods work. The section is about **topic
> and framing**, not method. Choosing wrong wastes a review cycle.

## Routing map (stage → skill)

```text
Idea / fit / section?            → aerj-topic-selection
Where does it sit in the field?  → aerj-literature-positioning
What frames the contribution?    → aerj-theory-and-framework
Is the design defensible?        → aerj-research-design
Are the analyses sound?          → aerj-data-analysis
Are the exhibits clear?          → aerj-tables-figures
Does it read for the field?      → aerj-writing-style
Reporting standards & data?      → aerj-transparency-and-data-policy
How will it be judged?           → aerj-review-process
Ready to submit?                 → aerj-submission
Got an R&R / decision?           → aerj-rebuttal
```

## Default order

`topic-selection → literature-positioning → theory-and-framework → research-design → data-analysis →
tables-figures → writing-style → transparency-and-data-policy → review-process → submission → rebuttal`

Iterate: most papers loop framework ↔ design ↔ analysis several times before writing-style.

## Anti-patterns

- Treating AERJ like a narrow specialty journal — the contribution must reach the whole field
- Confusing **section** with **method** (both sections take quant, qual, and mixed work)
- Forcing a quantitative template onto qualitative or mixed work (each is judged on its own terms)
- Skipping the reporting-standards / data step until acceptance

## Output format

```
【Stage】idea / positioning / framework / design / analysis / exhibits / writing / transparency / review / submit / rebut
【Section】SIA / TLHD (and why)
【Route to】aerj-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — education-research data + software by method
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official AERJ URLs behind every fact in this pack
