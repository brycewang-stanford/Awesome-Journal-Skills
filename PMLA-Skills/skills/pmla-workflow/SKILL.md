---
name: pmla-workflow
description: Use as the entry point for any PMLA (Publications of the Modern Language Association) manuscript. Routes to the right PMLA sub-skill based on where you are in the lifecycle and which venue fits — a regular blind-reviewed article or a special feature (Theories and Methodologies, The Changing Profession, Criticism in Translation, Little-known Documents). It dispatches; it does not draft content.
---

# PMLA Workflow Router (pmla-workflow)

The orchestrator for a PMLA submission. Figure out the stage and the **venue**, then send the user to
the matching skill. PMLA is the **generalist flagship of literary and language studies** — the
router's first job is to make sure the essay speaks to scholars and teachers of language and
literature broadly, not only to one period or school, and that it argues from **close reading**, not
from data.

## When to trigger

- Starting a new PMLA essay and unsure where to begin
- Mid-project and unsure which skill applies next
- Deciding between a **regular article** and a **special feature**
- Returning with a decision letter (route to `pmla-revision-and-response`)

## First question: which venue?

| Situation | Venue | Route to |
|-----------|-------|----------|
| Full original argument, broad interest | **Regular article** (6,000–9,000 words) | normal pipeline below |
| Timely comment on recent scholarship / a method | **Theories and Methodologies** (~3,500 words) | `pmla-theory-and-method` early |
| New or emerging field, state of the profession | **The Changing Profession** (~3,500 words) | `pmla-scholarly-positioning` early |
| A newly translated critical text | **Criticism in Translation** | `pmla-citation-and-style` (translation policy) |
| An archival find made available with commentary | **Little-known Documents** | `pmla-textual-evidence-and-close-reading` |

> Special features have their own caps and a proposal deadline (待核实 — confirm on the live page).
> If unsure, default to the regular-article pipeline.

## Routing map (stage → skill)

```text
Idea / fit?                        → pmla-topic-selection
Where does it sit in criticism?    → pmla-scholarly-positioning
What is the argument?              → pmla-argument-development
What is the textual evidence?      → pmla-textual-evidence-and-close-reading
What is the theoretical frame?     → pmla-theory-and-method
Is it well structured?             → pmla-structure-and-exposition
Does the prose carry it?           → pmla-writing-style
Is it in MLA style?                → pmla-citation-and-style
How will it be judged?             → pmla-review-process
Ready to submit?                   → pmla-submission
Got a decision / revise?           → pmla-revision-and-response
```

## Default order

`topic-selection → scholarly-positioning → argument-development → textual-evidence-and-close-reading →
theory-and-method → structure-and-exposition → writing-style → citation-and-style → review-process →
submission → revision-and-response`

Iterate: most essays loop argument ↔ close reading ↔ theory several times before the prose polish.

## Anti-patterns

- Treating PMLA like a narrow specialist journal — the essay must interest the whole membership
- Importing a social-science template (hypotheses, data, replication) onto a literary essay
- Leaving close reading thin because "the theory does the work" — at PMLA the text is the evidence
- Forgetting **MLA membership is required to submit** and the review is **anonymous**


## Router pass for PMLA

Run this as a concrete capability pass. First lock the object corpus, interpretive intervention, field conversation, and scholarly stakes; then test whether the manuscript addresses humanities reviewers who expect a field-crossing literary or language-studies intervention with careful textual evidence.

- **Primary move:** Run the pack as fit gate, evidence gate, writing gate, source-map gate, and output contract; stop when a gate lacks evidence.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against Critical Inquiry for theory-forward essays, New Literary History for literary theory/history, discipline journals for narrower archive work; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Stage】idea / positioning / argument / evidence / theory / structure / prose / style / review / submit / revise
【Venue】regular article / Theories and Methodologies / The Changing Profession / Criticism in Translation / Little-known Documents
【Route to】pmla-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — texts, archives, bibliography, MLA-style tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official PMLA URLs behind every fact in this pack
