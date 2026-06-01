---
name: jmr-workflow
description: Use when deciding which jmr-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a Journal of Marketing Research (JMR) manuscript. Routes — it does not replace — the specialized skills, and classifies the paper as behavioral, modeling/econometric, or a methods contribution.
---

# Journal of Marketing Research Workflow (jmr-workflow)

## Overview

This is the router. It does not replace any specialized skill; it tells you **which jmr-* skill to use right now** for your JMR manuscript.

Default assumption: unless the user says otherwise, treat the target as JMR — the American Marketing Association's (AMA) methods- and modeling-forward flagship, published by SAGE. JMR covers the **full spectrum of marketing topics with an emphasis on methodological rigor** and welcomes a **wide variety of data and methodological approaches**. Its defining feature is methodological pluralism *within one journal*: lab and field **experiments** in consumer behavior sit alongside **econometric and structural/analytical marketing-science modeling**, plus dedicated **methods contributions**. JMR enforces a **dual bar** — a manuscript must clear *both* a methodological-rigor bar *and* a substantive/theoretical-contribution bar — which distinguishes it from the more managerial *Journal of Marketing*.

First routing question: **which genre is this paper?** Behavioral (experiments + process), modeling/econometric (causal identification or structural estimation), or a methods paper (a new estimator/measure). The genre determines how `jmr-theory-development`, `jmr-methods`, and `jmr-data-analysis` are applied.

> Editor transition: Rebecca Hamilton (Georgetown) is EIC through 30 June 2026; Raphael Thomadsen's incoming team (Washington University in St. Louis, 2026–2029) has processed new manuscripts since 1 April 2026 — authors submitting now are effectively handled by the incoming team. Verify the masthead at ama.org.

## When to trigger

- "What should I do next?" with a half-built JMR manuscript
- You have a result but are unsure whether the dual bar (rigor + substance) is met
- A reviewer pushes on identification, exact-statistics reporting, or "what do we learn?"
- You received a JMR decision letter and need to switch into response mode

## Routing table

| Current symptom                                                       | Next skill                  |
|-----------------------------------------------------------------------|-----------------------------|
| Idea is vague; unsure it is JMR-fit vs. JM / Marketing Science / JCR  | `jmr-topic-selection`       |
| Conceptual claim or model primitive is underspecified                 | `jmr-theory-development`    |
| Front end reads as a better application, not a contribution           | `jmr-literature-positioning`|
| Design/identification may not support the causal or structural claim  | `jmr-methods`               |
| Need exact p-values, SEs, effect sizes, the right estimator           | `jmr-data-analysis`         |
| Results exist but the dual "so what" is thin                          | `jmr-contribution-framing`  |
| Exhibits cluttered, or main-text vs. Web Appendix split is wrong      | `jmr-tables-figures`        |
| Prose buries the argument; abstract/style off AMA norms               | `jmr-writing-style`         |
| Ready to submit; need ScholarOne / 50-page / Web Appendix preflight   | `jmr-submission`            |
| Want to understand JMR's double-anonymized, two-review process        | `jmr-review-process`        |
| Received an R&R; need to plan and draft the response                  | `jmr-rebuttal`              |

## Default order

1. `jmr-topic-selection` → 2. `jmr-theory-development` → 3. `jmr-literature-positioning` → 4. `jmr-methods` → 5. `jmr-data-analysis` → 6. `jmr-contribution-framing` → 7. `jmr-tables-figures` → 8. `jmr-writing-style` → 9. `jmr-submission` → 10. `jmr-review-process` → 11. `jmr-rebuttal`

> `jmr-tables-figures` and `jmr-writing-style` are **late-stage polish**. Do not invoke them while identification, the model, or the contribution is still unsettled.

## Difference vs. JM / Marketing Science / JCR

- **JMR**: dual bar (rigor + substance); experiments **and** modeling in one venue; 50-page print limit + 'W'-prefixed Web Appendix; ScholarOne at mc.manuscriptcentral.com/ama_jmr.
- **Journal of Marketing**: managerial/substantive framing — manager-facing implications lead.
- **Marketing Science**: quantitative marketing science; analytical/structural models.
- **JCR**: consumer behavior, interdisciplinary, primarily behavioral experiments.

## Anti-patterns

- **Do not** treat JMR as single-genre — route behavioral and modeling papers differently.
- **Do not** let polish skills run before the dual bar is plausibly met.
- **Do not** let `jmr-rebuttal` draft a response before the manuscript is actually revised.

## Output format

```text
[Target] JMR
[Genre] behavioral / modeling-econometric / methods
[Stage] workflow
[Main bottleneck] rigor bar / substance bar / fit / process
[Next skill] jmr-...
[Live-rule checks] masthead, 50-page limit, Web Appendix, fees → verify
```

## Resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md)
- [`../../resources/external_tools.md`](../../resources/external_tools.md)
