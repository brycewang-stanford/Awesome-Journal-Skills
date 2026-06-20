---
name: bjps-workflow
description: Use as the entry point for any British Journal of Political Science (BJPS / BJPolS) manuscript. Routes to the right BJPS sub-skill based on lifecycle stage and which of the three formats (Research Article, Letter, Comment) fits. It dispatches; it does not draft content.
---

# BJPS Workflow Router (bjps-workflow)

The orchestrator for a British Journal of Political Science submission. Figure out the stage and the
**format**, then send the user to the matching skill. BJPS is a **broad, internationally-oriented
general** political-science journal (Cambridge University Press) that covers every subfield and
methodology — the router's first job is to confirm the paper has **wide interest** and is pitched
beyond a single subfield or national case.

## When to trigger

- Starting a new BJPS paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Deciding which of the **three formats** fits the paper
- Returning with a decision letter (route to `bjps-rebuttal`)

## First question: which format?

| Situation | Format | Route to |
|-----------|--------|----------|
| Full original study, broad interest | **Research Article** (~10,000 words; 待核实 exact cap) | normal pipeline below |
| One crisp, focused contribution | **Letter** (short article, ~4,000 words; 待核实) | normal pipeline, tighter scope |
| Critique / correction of a published BJPS piece | **Comment** | `bjps-literature-positioning` + `bjps-research-design` |

> A Letter is not a half-finished Article — it is a complete, decisive contribution at short length.
> Do not pad a Letter into an Article, or starve an Article into a Letter.

## Routing map (stage → skill)

```text
Idea / fit?                      → bjps-topic-selection
Where does it sit in the field?  → bjps-literature-positioning
What's the argument?             → bjps-theory-building
Is the design defensible?        → bjps-research-design
Are the analyses sound?          → bjps-data-analysis
Are the exhibits clear?          → bjps-tables-figures
Does it read for the field?      → bjps-writing-style
Replication data & transparency? → bjps-transparency-and-data
How will it be judged?           → bjps-review-process
Ready to submit?                 → bjps-submission
Got an R&R / decision?           → bjps-rebuttal
```

## Default order

`topic-selection → literature-positioning → theory-building → research-design → data-analysis →
tables-figures → writing-style → transparency-and-data → review-process → submission → rebuttal`

Iterate: most papers loop theory ↔ design ↔ analysis several times before writing-style.

## Wide-interest routing check

Before selecting the next skill, force a one-minute BJPS fit check:

| Check | Pass condition | Route if weak |
|-------|----------------|---------------|
| Interest | A scholar outside the author's subfield (or country specialism) can state why the question matters to political science generally. | `bjps-topic-selection` |
| Format | The manuscript clearly fits Research Article, Letter, or Comment. | format table above |
| Method pluralism | The method is defended on its own terms, not forced into a quantitative template; BJPS spans formal, quant, qual, and interpretive work. | `bjps-research-design` |
| Transparency | Replication data/code (or a qualitative-transparency / restricted-access plan) is mapped to the BJPolS Dataverse expectation. | `bjps-transparency-and-data` |

If the paper fails the interest check, do not route to writing-style. It needs a theory or fit repair —
BJPS reviewers reject competent single-country or single-subfield studies that never make a claim of
**general** political-science interest.

## Anti-patterns

- Treating BJPS like a national or subfield outlet — the contribution must travel beyond one case or specialism
- Forcing a quantitative template onto qualitative, formal, or interpretive work (BJPS judges each on its own terms)
- Confusing BJPS with its US generalist siblings (APSR, AJPS) or specialists (CPS, World Politics) — see README
- Deferring the replication package to acceptance — assemble it as you analyze

## Output format

```
【Stage】idea / positioning / theory / design / analysis / exhibits / writing / transparency / review / submit / rebut
【Format】Research Article / Letter / Comment
【Route to】bjps-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — political-science data + software by method
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official BJPS URLs behind every fact in this pack
