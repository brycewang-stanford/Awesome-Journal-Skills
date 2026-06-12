---
name: fcr-workflow
description: Use as the entry point for any Field Crops Research (FCR) manuscript. Routes to the right FCR sub-skill based on where you are in the lifecycle and which article type (Original Research Paper, Review, Short Communication, Opinion, Loomis Review) fits. It checks scope-fit first — FCR rejects controlled-environment-only and single-site single-season work — then dispatches; it does not draft content.
---

# FCR Workflow Router (fcr-workflow)

The orchestrator for a Field Crops Research submission. Figure out the stage and the **article type**,
then send the user to the matching skill. FCR is an **empirical field-agronomy** journal — the
router's first job is a **scope gate**: is this genuine field-based research with **multi-season
and/or multi-environment** relevance? If not, fix that before anything else.

## When to trigger

- Starting a new FCR paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Deciding which **article type** fits the work
- Returning with a decision letter (route to `fcr-revision-and-rebuttal`)

## Scope gate (ask first, every time)

| Question | If "no" |
|----------|---------|
| Is it **field-based** (not greenhouse/pot/root-restricting only)? | Likely out of scope → `fcr-topic-selection` |
| Does it have **≥ 2 seasons and/or multiple environments**? | Redesign or reframe → `fcr-experimental-design` |
| Is the crop a **field crop** (not horticultural/woody-perennial/non-cultivated)? | Out of scope → `fcr-topic-selection` |
| Is it more than **corroborative / descriptive / local**? | Sharpen the contribution → `fcr-topic-selection` |

## First question: which article type?

| Situation | Article type | Route to |
|-----------|--------------|----------|
| Full original field/modelling study | **Original Research Paper** | normal pipeline below |
| Concise, complete, focused study | **Short Communication** | normal pipeline, tighter scope |
| Critical synthesis of a topic | **Review** (usually invited; propose first) | `fcr-literature-positioning` + `fcr-topic-selection` |
| Perspective / position piece | **Opinion Paper** | `fcr-topic-selection` + `fcr-writing-style` |
| Invited major review | **Loomis Review** (by invitation) | `fcr-literature-positioning` |

## Routing map (stage → skill)

```text
Idea / scope fit?               → fcr-topic-selection
Where does it sit in the field? → fcr-literature-positioning
Is the design defensible?       → fcr-experimental-design
Are the analyses sound?         → fcr-data-analysis
Are the exhibits clear?         → fcr-figures-and-tables
Data availability & reporting?  → fcr-reporting-and-data-policy
Does it read for agronomists?   → fcr-writing-style
Need a cover letter?            → fcr-cover-letter
How will it be judged?          → fcr-review-process
Ready to submit?                → fcr-submission
Got a decision / revision?      → fcr-revision-and-rebuttal
```

## Default order

`topic-selection → literature-positioning → experimental-design → data-analysis → figures-and-tables →
reporting-and-data-policy → writing-style → cover-letter → review-process → submission →
revision-and-rebuttal`

Iterate: most papers loop design ↔ analysis ↔ figures several times before writing-style.

## Desk-reject triage table (route before you draft)

The Editors-in-Chief screen for scope before a manuscript reaches reviewers; most fast rejections are predictable. Catch them here and route to the repair skill instead of polishing prose on a paper that cannot pass the gate.

| Symptom an editor sees | FCR-specific risk | Route to |
|------------------------|-------------------|----------|
| Pot/greenhouse trial is the only evidence | Out of scope (controlled-environment exclusion) | `fcr-topic-selection` |
| One site × one season, no environment spread | Fails the ≥2-seasons/-environments expectation | `fcr-experimental-design` |
| Tomato, grapevine, turfgrass, or medicinal species | Wrong journal (horticultural/woody-perennial exclusion) | `fcr-topic-selection` |
| "First measurement of trait X in region Y" | Local/descriptive, not general insight | `fcr-literature-positioning` |
| ANOVA on pooled plots, blocking ignored | Statistics do not match the trial structure | `fcr-data-analysis` |
| Yields reported, no link to a biophysical process | Weak agronomic significance | `fcr-literature-positioning` |

## Worked routing vignette (illustrative)

*Illustrative scenario, numbers chosen to demonstrate the gate — not real data.* A team has a new
drought-tolerant maize hybrid yielding 8.4 t ha⁻¹ versus a 7.1 t ha⁻¹ check, measured at **one farm in
one season**. They ask where to begin a manuscript. The router runs the scope gate: field-based (pass),
field crop (pass), but **one site-year fails the multi-environment expectation** and the 1.3 t ha⁻¹
margin sits at a single point in the G×E space. Verdict: do **not** enter the drafting pipeline yet —
route to `fcr-experimental-design` to add seasons/sites (e.g., 2 seasons × 4 environments) so the
hybrid advantage can be shown to hold across environments, then resume the default order. Routing a
half-evidenced paper into writing-style first is the classic wasted cycle.

## Anti-patterns

- Skipping the scope gate and investing in controlled-environment-only or single-site data
- Treating one season at one site as enough (FCR expects multi-season/-environment relevance)
- Forcing a Review/Opinion frame onto what is really an Original Research Paper
- Leaving the data-availability statement and highlights to the last minute
- Polishing format on a paper whose G×E×M evidence cannot yet support a general yield claim

## Output format

```
【Scope gate】field-based? multi-environment? field crop? more than local? [pass/fix]
【Stage】idea / positioning / design / analysis / exhibits / reporting / writing / cover / review / submit / revise
【Article type】Original Research / Short Communication / Review / Opinion / Loomis Review
【Route to】fcr-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — agronomy data + software by method
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official FCR URLs behind every fact in this pack
