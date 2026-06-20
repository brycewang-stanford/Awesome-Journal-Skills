---
name: spq-workflow
description: Use as the entry point for any Social Psychology Quarterly (SPQ) manuscript. Routes to the right SPQ sub-skill based on where you are in the lifecycle and which sociological-social-psychology tradition (symbolic interaction, social structure and personality, group processes, status/affect, identity) and article type (Article vs. Note) fit. It dispatches; it does not draft content.
---

# SPQ Workflow Router (spq-workflow)

The orchestrator for a Social Psychology Quarterly submission. Figure out the stage, the **tradition**,
and the **article type**, then send the user to the matching skill. SPQ is the journal of **sociological
social psychology** — the router's first job is to make sure the paper connects **social structure or
process to the individual** (self, interaction, group), not that it is psychology with a survey attached.

## When to trigger

- Starting a new SPQ paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Deciding between a full **Article** (≤ 10,000 words) and a **Note** (≤ 5,000 words)
- Returning with a decision letter (route to `spq-rebuttal`)

## First question: which tradition and type?

| Situation | Tradition / type | Route to |
|-----------|------------------|----------|
| Meaning-making, self, interaction order, accounts | **Symbolic interaction** (often interview/observation) | normal pipeline; `spq-research-design` (interpretive) |
| Social structure / status shaping the self, well-being, attitudes | **Social structure and personality** (survey/secondary) | normal pipeline |
| Status, expectation states, exchange, legitimacy, justice | **Group processes** (usually experimental) | normal pipeline; `spq-research-design` (experiment) |
| Identity salience/verification, affect/emotion modeling | **Identity / affect** programs | `spq-theory-building` then design |
| One crisp contribution communicable briefly | **Note** (≤ 5,000 words) | normal pipeline, tighter scope |

> SPQ is interdisciplinary (sociologists and psychologists publish), but the through-line is always the
> **link between the individual and society**. If that link is missing, reframe (back to topic-selection).

## Routing map (stage → skill)

```text
Idea / fit?                       → spq-topic-selection
Where does it sit in the field?   → spq-literature-positioning
What's the social-psych argument? → spq-theory-building
Is the design defensible?         → spq-research-design
Are the analyses sound?           → spq-data-analysis
Are the exhibits clear?           → spq-tables-figures
Does it read for the field?       → spq-writing-style
Data / materials & ethics?        → spq-data-and-transparency
How will it be judged?            → spq-review-process
Ready to submit?                  → spq-submission
Got an R&R / decision?            → spq-rebuttal
```

## Default order

`topic-selection → literature-positioning → theory-building → research-design → data-analysis →
tables-figures → writing-style → data-and-transparency → review-process → submission → rebuttal`

Iterate: most papers loop theory ↔ design ↔ analysis several times before writing-style.

## Anti-patterns

- Treating SPQ like JPSP or Psychological Science — a study of individual cognition with no link to social structure or interaction is off-fit
- Treating SPQ like ASR/AJS — a macro-sociology paper with no social-psychological mechanism is off-fit
- Forcing an experimental template onto interpretive symbolic-interaction work (SPQ judges each tradition on its own terms)
- Treating data sharing as a gate — SPQ encourages but does not require it (see `spq-data-and-transparency`)


## Router pass for Social Psychology Quarterly

Run this as a concrete capability pass. First lock the social-psychological process, measurement, design, and boundary condition across groups or contexts; then test whether the manuscript addresses social-psychology reviewers who expect interaction, identity, group process, or status mechanisms grounded in sociological theory.

- **Primary move:** Run the pack as fit gate, evidence gate, writing gate, source-map gate, and output contract; stop when a gate lacks evidence.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against JPSP for psychology breadth, ASR/AJS for sociology theory stakes, Social Forces for broader empirical sociology; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` and name the live-check item that could change the upload plan.

## Output format

```
【Stage】idea / positioning / theory / design / analysis / exhibits / writing / data / review / submit / rebut
【Tradition】symbolic interaction / social structure & personality / group processes / identity / affect
【Type】Article (≤10,000) / Note (≤5,000)
【Route to】spq-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — sociological-social-psychology data + software by tradition
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official SPQ URLs behind every fact in this pack
