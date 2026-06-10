---
name: ci-workflow
description: Use as the entry point for any Critical Inquiry (CI) essay. Routes to the right CI sub-skill based on where you are in the lifecycle and which format (Article, Critical Response, Review) fits. CI is an interdisciplinary journal of criticism and theory in the arts and humanities; the router's job is to keep the project pointed at a bold theoretical intervention with interdisciplinary stakes. It dispatches; it does not draft content.
---

# Critical Inquiry Workflow Router (ci-workflow)

The orchestrator for a *Critical Inquiry* submission. Figure out the stage and the **format**, then
send the user to the matching skill. CI is **interdisciplinary criticism and theory** — not a single
discipline's house organ — so the router's first job is to make sure the essay is built around a
**theoretical intervention** that matters across fields, not a competent reading with no stakes.

## When to trigger

- Starting a new CI essay and unsure where to begin
- Mid-project and unsure which skill applies next
- Deciding among the **three formats** (Article, Critical Response, Review)
- Returning with a decision letter (route to `ci-revision-and-response`)

## First question: which format?

| Situation | Format | Route to |
|-----------|--------|----------|
| Full original argument, interdisciplinary stakes | **Article** (≤ 9,500 words) | normal pipeline below |
| Reply to or debate with a published CI piece | **Critical Response** (≤ 3,000 words) | `ci-argument-and-intervention` + `ci-scholarly-positioning` |
| Short notice of a book/exhibition | **Review** (≤ 500 words) | `ci-writing-style` + `ci-submission` |
| A themed cluster of essays | **Special issue** (editor-proposed) | `ci-review-process` (proposal route) |

> The 9,500-word article cap **includes discursive notes and all bibliographical information** — plan
> the notes into the budget from the start (see `ci-writing-style`).

## Routing map (stage → skill)

```text
Is this a CI-shaped problem?       → ci-topic-selection
Whose conversation am I entering?  → ci-scholarly-positioning
What is the intervention?          → ci-argument-and-intervention
What objects does it read?         → ci-evidence-and-objects
Which theory, used how?            → ci-theory-and-method
How is the essay built?            → ci-structure-and-exposition
Does the prose earn the claim?     → ci-writing-style
Notes / images / Chicago style?    → ci-citation-and-style
How will it be judged?             → ci-review-process
Ready to submit?                   → ci-submission
Got a decision / revise request?   → ci-revision-and-response
```

## Default order

`topic-selection → scholarly-positioning → argument-and-intervention → evidence-and-objects →
theory-and-method → structure-and-exposition → writing-style → citation-and-style → review-process →
submission → revision-and-response`

Iterate: most essays loop argument ↔ objects ↔ theory several times before the prose settles.

## Anti-patterns

- Treating CI like a single-discipline journal — the intervention must travel across fields
- A survey or literature review with no claim of its own (CI wants an intervention, not a digest)
- Theory used as decoration rather than as an instrument that does work on an object
- Skipping image permissions and Chicago-note discipline until the end


## Router pass for Critical Inquiry

Treat this skill as an executable review pass, not a prose hint. First lock the object, theoretical stakes, interpretive turn, and permission/citation discipline; then judge whether the current manuscript answers the venue's real reader: humanities reviewers who expect a strong interpretive intervention rather than an empirical-results narrative.

- **Do the pass:** Run the pack as a sequence: fit gate, evidence gate, writing gate, source-map gate, and final output contract; stop when a gate lacks evidence.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against PMLA for literary-field reach, New Literary History for theory/history, Representations for historically grounded cultural analysis; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Stage】topic / positioning / intervention / objects / theory / structure / prose / citations / review / submit / revise
【Format】Article / Critical Response / Review / Special issue
【Route to】ci-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — archives, image and text sources, theory shelf, Chicago tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official CI URLs behind every fact in this pack
