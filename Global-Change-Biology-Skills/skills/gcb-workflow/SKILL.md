---
name: gcb-workflow
description: Use as the entry point for any Global Change Biology (GCB) manuscript. Routes to the right GCB sub-skill based on where you are in the lifecycle and which article type (Primary Research Article, Technical Advance, Review / Research Review, Opinion / Perspective) fits. It dispatches; it does not draft content.
---

# GCB Workflow Router (gcb-workflow)

The orchestrator for a *Global Change Biology* submission. Figure out the stage and the **article
type**, then send the user to the matching skill. GCB publishes **mechanistic links between global
environmental change and biological systems** — the router's first job is to make sure the paper leads
with a **driver → biological-response mechanism** of broad relevance, not a local description or a
conservation-management plan.

## When to trigger

- Starting a new GCB paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Deciding which **article type** fits the contribution
- Returning with a decision letter (route to `gcb-revision-and-rebuttal`)

## First question: which article type?

| Situation | Article type | Route to |
|-----------|--------------|----------|
| Completed original study, broad global-change relevance | **Primary Research Article** | normal pipeline below |
| New tool / method / modelling approach | **Technical Advance** | `gcb-study-design` + `gcb-data-analysis` |
| Integrative synthesis of a literature | **Research Review** (open) / **GCB Review** (invited) | `gcb-literature-positioning` + `gcb-writing-style` |
| Argued position / forward-looking view | **Opinion** (~3,000–5,000 w) / **Perspective** (~1,500 w) | `gcb-topic-selection` + `gcb-writing-style` |

> GCB Reviews are **commissioned**; the **Research Reviews** section is open for unsolicited submission.
> Live-check the current article-type list and caps in the official Wiley guidance before submission.

## Routing map (stage → skill)

```text
Idea / global-change fit?        → gcb-topic-selection
Where does it sit in the field?  → gcb-literature-positioning
Is the design defensible?        → gcb-study-design
Are the analyses sound?          → gcb-data-analysis
Are the exhibits mechanistic?    → gcb-figures-and-tables
Data & code archived?            → gcb-reporting-and-data-policy
Does it read for GCB?            → gcb-writing-style
Cover letter for the editor?     → gcb-cover-letter
How will it be judged?           → gcb-review-process
Ready to submit?                 → gcb-submission
Got a decision / revision?       → gcb-revision-and-rebuttal
```

## Default order

`topic-selection → literature-positioning → study-design → data-analysis → figures-and-tables →
reporting-and-data-policy → writing-style → cover-letter → review-process → submission →
revision-and-rebuttal`

Iterate: most papers loop design ↔ analysis ↔ figures several times before writing-style.

## Symptom-to-skill dispatch

When a user arrives mid-stream with a complaint rather than a stage, route by symptom. Each row sends
the question to the sub-skill that owns the fix.

| User says | Underlying issue | Route to |
|-----------|------------------|----------|
| "Editor desk-rejected on scope" | Fit/significance framing | `gcb-topic-selection` then `gcb-cover-letter` |
| "Reviewer says it's correlative" | Mechanism not tested | `gcb-study-design` + `gcb-data-analysis` |
| "Can't scale plot to biome" | Uncertainty not propagated | `gcb-data-analysis` |
| "Graphical abstract rejected" | Non-mechanistic exhibit | `gcb-figures-and-tables` |
| "Data statement non-compliant" | Archiving gap | `gcb-reporting-and-data-policy` |

## Worked micro-example (illustrative)

A user returns with a major-revision letter on a remote-sensing carbon-flux paper. The router reads the
decisive comments: the mechanism is called correlative and the scaling lacks uncertainty. It dispatches
first to `gcb-data-analysis` to add an ensemble and partition uncertainty, then to `gcb-figures-and-tables`
to make the driver-response panel lead, then to `gcb-revision-and-rebuttal` to assemble the response. It
also confirms the Zenodo code archive is re-tagged via `gcb-reporting-and-data-policy`. The order is
driven by which comments the editor flagged as decisive, not by the default pipeline. Scenario is
illustrative.

## Routing pitfalls the orchestrator guards against

- Sending a scope-mismatched idea down the writing pipeline before fixing fit in topic selection.
- Treating archiving as a final step rather than staging it during analysis.
- Routing an invited-only review type as if it were open for submission.

## Anti-patterns

- Pitching a local case study with no global-change mechanism or broad relevance
- Confusing GCB with a conservation-practice journal (mechanism/ecosystems, not action plans)
- Submitting an unsolicited "GCB Review" (those are by invitation — use Research Reviews)
- Leaving data/code archiving until acceptance — deposit is a condition of publication

## Output format

```
【Stage】idea / positioning / design / analysis / exhibits / data-policy / writing / cover-letter / review / submit / revise
【Article type】Primary Research Article / Technical Advance / Research Review / Opinion / Perspective
【Route to】gcb-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — global-change data + software by method
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official GCB URLs behind every fact in this pack
