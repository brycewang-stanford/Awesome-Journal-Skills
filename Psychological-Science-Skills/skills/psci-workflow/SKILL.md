---
name: psci-workflow
description: Use when starting or navigating any Psychological Science manuscript and you are unsure which sub-skill applies. Use when choosing among manuscript types or returning with a decision letter. Routes by lifecycle stage and manuscript type (Research Article, Registered Report Stage 1/2, Registered Report with Existing Data, Commentary), and flags the journal's tight word format and open-science requirements. It dispatches; it does not draft content.
---

# Psychological Science Workflow Router (psci-workflow)

The orchestrator for a Psychological Science submission. The journal's two defining constraints are a
**very tight word format** and **strong open-science requirements** — the router makes sure both are
handled from the start, then sends the user to the matching skill.

## When to trigger

- Starting a new Psychological Science paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Choosing among manuscript types
- Returning with a decision letter (route to `psci-rebuttal`)

## First question: manuscript type

| Situation | Type | Route note |
|-----------|------|-----------|
| Completed empirical study | **Research Article** | main pipeline below; mind the 2,000-word format |
| Prospective design, no results yet | **Registered Report (Stage 1)** | go to `psci-study-design` + `psci-review-process` early |
| Stage-1 accepted, now have results | **Registered Report (Stage 2)** | `psci-data-analysis` → `psci-writing-style` |
| Confirmatory test on existing data | **Registered Report with Existing Data** | `psci-study-design` (declare data provenance) |
| Short critique/reply to a published paper | **Commentary / Reply** (≤ 1,000 words) | `psci-literature-positioning` |

> Short Reports and standalone Preregistered Direct Replications are **no longer accepted** — fit your
> replication/extension into a Research Article or a Registered Report.

## Routing map (stage → skill)

```text
Idea / fit?                       → psci-topic-selection
Where does it sit in the field?   → psci-literature-positioning
Theory + hypotheses?              → psci-theory-and-hypotheses
Design / power / preregistration? → psci-study-design
Analysis sound + disclosed?       → psci-data-analysis
Exhibits (APA, embedded)?         → psci-tables-figures
Fits the word format?             → psci-writing-style
Open data/materials + statement?  → psci-open-science-and-transparency
How will it be judged?            → psci-review-process
Ready to submit?                  → psci-submission
Got an R&R / decision?            → psci-rebuttal
```

## Default order

`topic-selection → literature-positioning → theory-and-hypotheses → study-design → data-analysis →
tables-figures → writing-style → open-science-and-transparency → review-process → submission → rebuttal`

For Registered Reports, the Stage 1 package (theory + design + analysis plan) is reviewed **before**
data — pull `study-design` and `review-process` forward.

## Worked micro-example — routing a live project (illustrative)

A team has two preregistered attention studies (N = 240; N = 300), open data, and an R2 asking for
power and a replication. The router walks them:

```
Type:    Research Article (results in hand, internal replication present).
Entry:   not idea-stage → skip topic-selection; they are at analysis/exhibits.
Route:   data-analysis (effect sizes + CIs + disclosure)
         → tables-figures (dot/CI figure, embedded)
         → writing-style (fit Intro+Discussion ≤ 2,000)
         → open-science-and-transparency (DOIs + Transparency Statement)
         → submission (preflight) ; on R&R → rebuttal.
Flag:    Transparency Statement must sit between Intro and Methods — verify
         current placement against the journal's submission guidelines.
```

## Stage-triage table (symptom → skill)

| What the author says | Stage | Route to |
|----------------------|-------|----------|
| "Is this even right for the journal?" | fit | `psci-topic-selection` |
| "My intro is 1,400 words and still growing" | format | `psci-writing-style` |
| "Reviewer says single underpowered study" | design/analysis | `psci-study-design` + `psci-data-analysis` |
| "Where does the Transparency Statement go?" | transparency | `psci-open-science-and-transparency` |
| "I have an R&R" | revision | `psci-rebuttal` |
| "Should I preregister before running?" | design | `psci-study-design` (consider RR Stage 1) |

## Routing pitfalls specific to this venue

- Sending a confirmatory-prospective project straight to `psci-data-analysis` instead of considering a
  Registered Report Stage 1 first — the route matters before data exist.
- Deferring `psci-open-science-and-transparency` to the end; deposits and DOIs should be built early so
  the Transparency Statement is drafted from live identifiers, not promised at acceptance.

## Anti-patterns

- Writing long, then trying to cut to 2,000 words — design for the format from the start
- Treating open data/materials as optional (they are required; exemptions are case-by-case and graded)
- Forgetting the Research Transparency Statement (it sits between Intro and Methods)
- Choosing a Registered Report after results exist

## Output format

```
【Stage】idea / positioning / theory / design / analysis / exhibits / writing / transparency / review / submit / rebut
【Type】Research Article / Registered Report S1 / S2 / RR-Existing-Data / Commentary
【Route to】psci-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — preregistration, repositories, power, effect-size tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official Psychological Science URLs behind every fact in this pack
