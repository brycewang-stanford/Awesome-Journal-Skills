---
name: est-workflow
description: Use as the entry point for any Environmental Science & Technology (ES&T) manuscript. Routes to the right ES&T sub-skill based on where you are in the lifecycle and which article type (Research Article, Critical Review, Feature, Perspective, Policy Analysis, or the rapid companion ES&T Letters) fits. It dispatches; it does not draft content.
---

# ES&T Workflow Router (est-workflow)

The orchestrator for an ES&T submission. Figure out the stage and the **article type**, then send the
user to the matching skill. ES&T is a **multidisciplinary environmental science and engineering**
journal — the router's first job is to make sure the paper carries clear **environmental
significance**, not just a clean lab result.

## When to trigger

- Starting a new ES&T paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Deciding which article type fits, or whether to send urgent results to **ES&T Letters**
- Returning with a decision letter (route to `est-revision-and-rebuttal`)

## First question: which article type?

| Situation | Type | Route to |
|-----------|------|----------|
| Full original study | **Research Article** (~7,000 words; 待核实) | normal pipeline below |
| Urgent, high-impact result, short | **ES&T Letters** (Letter ≤3,000 words; separate journal) | tighten scope; `est-submission` |
| Comprehensive synthesis of a field | **Critical Review** (~10,000 words; 待核实) | `est-literature-positioning` + `est-writing-style` |
| Forward-looking opinion/synthesis | **Perspective** (~4,000 words; 待核实) | `est-literature-positioning` |
| Magazine-style accessible piece | **Feature** (~5,000 words; 待核实) | `est-writing-style` |
| Science–policy interface analysis | **Policy Analysis** (~7,000 words; 待核实) | `est-topic-selection` + `est-writing-style` |

> Word caps are volatile and figures/tables may count as word-equivalents — confirm on the live
> guidelines page (see 待核实 in `resources/official-source-map.md`).

## Routing map (stage → skill)

```text
Idea / environmental significance? → est-topic-selection
Where does it sit in the field?    → est-literature-positioning
Is the study design defensible?    → est-study-design
Are the analyses + QA/QC sound?    → est-data-analysis
Are the exhibits + TOC art clear?  → est-figures-and-tables
SI, data deposit, reproducibility? → est-reporting-and-reproducibility
Does it read in ACS style?         → est-writing-style
Cover letter to the editor?        → est-cover-letter
How will it be judged?             → est-review-process
Ready to submit?                   → est-submission
Got a decision / revision?         → est-revision-and-rebuttal
```

## Default order

`topic-selection → literature-positioning → study-design → data-analysis → figures-and-tables →
reporting-and-reproducibility → writing-style → cover-letter → review-process → submission →
revision-and-rebuttal`

Iterate: most papers loop design ↔ analysis ↔ QA/QC several times before writing-style.

## Anti-patterns

- Treating ES&T like a pure-chemistry or pure-engineering journal — the paper must show environmental relevance
- A clean method with no demonstrated significance for a real environmental system
- Choosing ES&T Letters for non-urgent work, or ES&T for a result better suited to a specialist venue
- Leaving the TOC graphic, SI, and data deposit to the last day

## Output format

```
【Stage】idea / positioning / design / analysis / exhibits / reproducibility / writing / cover-letter / review / submit / revise
【Type】Research Article / Critical Review / Feature / Perspective / Policy Analysis / ES&T Letters
【Route to】est-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — environmental data, instruments, and software by sub-area
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official ES&T URLs behind every fact in this pack
