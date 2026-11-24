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
| Full original study | **Research Article** (7,000 words) | normal pipeline below |
| Urgent, high-impact result, short | **ES&T Letters** (Letter ≤3,000 words; separate journal) | tighten scope; `est-submission` |
| Comprehensive synthesis of a field | **Review** (10,000 words) | `est-literature-positioning` + `est-writing-style` |
| Forward-looking opinion/synthesis | **Perspective** (4,000 words) | `est-literature-positioning` |
| Magazine-style accessible piece | **Feature** (5,000 words) | `est-writing-style` |
| Science–policy interface analysis | **Policy Analysis** (7,000 words) | `est-topic-selection` + `est-writing-style` |

> Word caps re-verified 2026-11-24; the count covers abstract + main text + figure/table captions
> (references, tables and graphics excluded). Re-confirm on the live guidelines page before upload.

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

## Symptom → skill quick-routing

When a user arrives mid-stream with a specific complaint, route by symptom rather than walking the
whole pipeline. Each symptom carries the ES&T-specific failure mode it signals:

| User says | Underlying ES&T risk | Route to |
|-----------|----------------------|----------|
| "Is this significant enough?" | desk-decline on significance | `est-topic-selection` |
| "A reviewer said it's not novel" | incremental-occurrence framing | `est-literature-positioning` |
| "Reviewer wants more controls/QA-QC" | analytical-rigor gap | `est-study-design`, `est-data-analysis` |
| "Mass balance doesn't close" | unaccounted-fraction objection | `est-data-analysis` |
| "Do I need a TOC graphic?" | incomplete-submission gate | `est-figures-and-tables` |
| "Where do I deposit the data?" | data-availability mandate | `est-reporting-and-reproducibility` |
| "Got a major revision" | response-letter strategy | `est-revision-and-rebuttal` |

## Worked micro-example (illustrative — routing a PFAS-fate manuscript)

A user starts: "I have river PFAS data showing a precursor converting to PFHxA — where do I begin?"
The router's pass (illustrative):

1. **Significance check** → `est-topic-selection`: reframe from occurrence to "surveys under-count
   persistent burden," confirming Research-Article fit.
2. **Positioning** → `est-literature-positioning`: engage the fate, analytical, and tox literatures so
   novelty is mechanistic, not "another dataset."
3. **Design/analysis loop** → `est-study-design` ↔ `est-data-analysis`: lock the abiotic control, mass
   balance, and QA/QC; handle the censored values with ROS.
4. **Exhibits + SI** → `est-figures-and-tables`, `est-reporting-and-reproducibility`: build a concept
   TOC graphic and deposit data/spectra/code.
5. **Write → cover → submit** → `est-writing-style` → `est-cover-letter` → `est-submission`.

The router's standing job: surface the environmental-significance and QA/QC gates *early*, because
those are what the desk editor and the ~three reviewers weigh first.

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
