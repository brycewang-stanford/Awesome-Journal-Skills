---
name: io-workflow
description: Use as the entry point for any International Organization (IO) manuscript. Routes to the right IO sub-skill based on where you are in the lifecycle and which article type (Research Article, Research Note, Essay) fits. IO is the IR-specialist flagship, so the router's first job is to confirm the paper is an international-relations contribution, not a domestic-politics paper with an international label. It dispatches; it does not draft content.
---

# IO Workflow Router (io-workflow)

The orchestrator for an *International Organization* submission. Figure out the stage and the **article
type**, then send the user to the matching skill. IO is the **leading journal of international
relations** — the router's first job is to make sure the **international or cross-border phenomenon is a
major cause or effect**, and that the paper offers a **generalizable theory** of international politics.

## When to trigger

- Starting a new IO paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Deciding among **Research Article / Research Note / Essay**
- Returning with a decision letter (route to `io-rebuttal`)

## First question: is it really an IR paper, and which type?

| Situation | Article type | Route to |
|-----------|--------------|----------|
| Full original IR study, generalizable theory | **Research Article** (≤ 14,000 words) | normal pipeline below |
| Focused single IR contribution | **Research Note** (≤ 8,000 words) | normal pipeline, tighter scope |
| Conceptual / agenda-setting / debate piece | **Essay** (≤ 10,000 words) | `io-theory-building` + `io-literature-positioning` |
| International phenomenon is only backdrop | (off-fit) | back to `io-topic-selection` — re-center the international level |

> If the international or cross-border phenomenon is not a **major cause or effect**, the paper is not
> yet an IO paper — fix that before anything else.

## Routing map (stage → skill)

```text
IR fit / theory worth it?         → io-topic-selection
Where does it sit in IR debates?  → io-literature-positioning
What's the IR theory?             → io-theory-building
Is the international design sound? → io-research-design
Are the analyses sound?           → io-data-analysis
Are the exhibits clear?           → io-tables-figures
Does it read for IR scholars?     → io-writing-style
Repro package + DAS verifiable?   → io-transparency-and-data-policy
How will it be judged?            → io-review-process
Ready to submit?                  → io-submission
Got an R&R / decision?            → io-rebuttal
```

## Default order

`topic-selection → literature-positioning → theory-building → research-design → data-analysis →
tables-figures → writing-style → transparency-and-data-policy → review-process → submission → rebuttal`

Iterate: IR papers usually loop theory ↔ design ↔ analysis several times before writing-style.

## Anti-patterns

- Treating IO like a generalist political-science journal (APSR/AJPS/JOP) — IO wants an **IR** theory, not a domestic-politics result with international data attached
- Leading with data when the contribution should be **generalizable theory** about international politics
- Leaving the reproducibility package and Data Availability Statement until acceptance — IO **verifies results and formal proofs before final acceptance**
- Sending a domestic-comparative paper where the cross-border mechanism is incidental

## Output format

```
【Stage】idea / positioning / theory / design / analysis / exhibits / writing / transparency / review / submit / rebut
【Article type】Research Article / Research Note / Essay
【IR fit】international phenomenon = major cause/effect? [Y/N]
【Route to】io-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — IR data sources + software by method
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official IO URLs behind every fact in this pack
