---
name: poq-workflow
description: Use as the entry point for any Public Opinion Quarterly (POQ) manuscript. Routes to the right POQ sub-skill based on where you are in the lifecycle and which submission type (Original Article, Research Note, Polls in Context, Research Synthesis, Book Review) fits. It dispatches; it does not draft content.
---

# POQ Workflow Router (poq-workflow)

The orchestrator for a POQ submission. Figure out the stage and the **submission type**, then send the
user to the matching skill. POQ is the leading journal of **public opinion and survey methodology** —
the router's first job is to make sure the paper is framed as a **measurement/opinion contribution**
with survey error and **AAPOR-standard disclosure** taken seriously from the start.

## When to trigger

- Starting a new POQ paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Deciding which **submission type** fits the paper
- Returning with a decision letter (route to `poq-rebuttal`)

## First question: which submission type?

| Situation | Type | Route to |
|-----------|------|----------|
| Full study — opinion or methods contribution | **Original Article** (≤ 6,500 words text + notes) | normal pipeline below |
| Single finding, extension, or replication | **Research Note** (< 3,000 words) | normal pipeline, tighter scope |
| Short, timely read of current poll data | **Polls in Context** (≤ 2,500 words) | `poq-data-analysis` + `poq-writing-style` |
| Integrative review of a literature | **Research Synthesis** (≤ 6,500 words) | `poq-literature-positioning` + `poq-theory-and-hypotheses` |
| Brief assessment of a recent book | **Book Review** (~1,200 words) | `poq-writing-style` |

> Word caps count **text and notes**, excluding figures, tables, references, and appendices — so the
> AAPOR disclosure appendix does **not** eat your budget. Confirm the current caps (待核实 on section
> names).

## Routing map (stage → skill)

```text
Idea / fit?                          → poq-topic-selection
Where does it sit in the field?      → poq-literature-positioning
What's the argument/hypothesis?      → poq-theory-and-hypotheses
Is the survey design defensible?     → poq-survey-design-and-measurement
Are the analyses design-based?       → poq-data-analysis
Are the exhibits clear?              → poq-tables-figures
Does it read for POQ?                → poq-writing-style
Repro package + Appendix A?          → poq-transparency-and-data-policy
How will it be judged?               → poq-review-process
Ready to submit?                     → poq-submission
Got an R&R / decision?               → poq-rebuttal
```

## Default order

`topic-selection → literature-positioning → theory-and-hypotheses → survey-design-and-measurement →
data-analysis → tables-figures → writing-style → transparency-and-data-policy → review-process →
submission → rebuttal`

Iterate: most papers loop survey-design ↔ data-analysis several times before writing-style.

## Anti-patterns

- Treating POQ like a generic social-science venue — the survey-error and disclosure bar is specific
- Leaving AAPOR disclosure (response rate, sampling, weighting) until the end instead of building Appendix A as you go
- Padding a Research Note or Polls in Context toward Article length
- Skipping the replication package until acceptance — it is archived **before typesetting**


## Router pass for Public Opinion Quarterly

Run this as a concrete capability pass. First lock the public-opinion construct, sampling frame, mode effects, weighting/nonresponse plan, and trend or causal interpretation; then test whether the manuscript addresses survey and public-opinion reviewers who inspect measurement, sampling, mode, nonresponse, and inference about attitudes or behavior.

- **Primary move:** Run the pack as fit gate, evidence gate, writing gate, source-map gate, and output contract; stop when a gate lacks evidence.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against Political Analysis for methods-first work, Journal of Politics for political-science theory, Communication Research for media-effects framing; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Stage】idea / positioning / theory / survey-design / analysis / exhibits / writing / transparency / review / submit / rebut
【Type】Original Article / Research Note / Polls in Context / Research Synthesis / Book Review
【Route to】poq-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — survey data + methodology software by task
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official POQ / AAPOR URLs behind every fact in this pack
