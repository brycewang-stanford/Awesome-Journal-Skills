---
name: rje-workflow
description: Use when routing a RAND Journal of Economics (RJE) manuscript to the right rje-* skill across the industrial-organization lifecycle — from IO topic fit through structural or reduced-form identification, exhibit design, Wiley Research Exchange submission, the editor screen, and the two-referee response. Use this as the entry-point dispatcher when you are unsure which RJE specialist skill a task needs; it dispatches, it does not itself frame, estimate, or write.
---

# RJE Workflow Router (rje-workflow)

## When to trigger

- You are starting or mid-way through an RJE manuscript and want to know the next step
- You are unsure whether your applied-micro / IO project is an RJE fit at all
- You need to map a reviewer request back to the right specialist skill

## What RJE is (so the route is correct)

The RAND Journal of Economics (RJE), formerly the **Bell Journal of Economics**, is owned and sponsored by the **RAND Corporation** (Santa Monica) and published in partnership with **Wiley**. Its scope is deliberately narrow: **applied microeconomics centered on industrial organization** — regulated industries, antitrust/competition, regulation, market structure, firm strategy, and the economic analysis of organizations. It is widely regarded as the field's **flagship IO journal**. Both theoretical and empirical work is welcomed. This is *not* a general-interest or macro outlet, so route accordingly.

## The route

```text
rje-topic-selection          (Is this an IO question RJE wants?)
        ▼
rje-contribution-framing     (What is the one-sentence contribution?)
        ▼
rje-literature-positioning   (Stake it against the IO frontier)
        ▼
rje-identification-strategy  (Structural or reduced-form design)
        ▼
rje-data-analysis            (Estimate, diagnose, robustness)
        ▼
rje-tables-figures           (Exhibits under the RJE Style Guide)
        ▼
rje-writing-style            (House usage + author-date polish)
        ▼
rje-replication-and-data-policy (Package + supporting-info handling)
        ▼
rje-review-process           (Understand the editor screen + referees)
        ▼
rje-submission               (Page caps, abstract, fee, portal preflight)
        ▼
rje-rebuttal                 (Respond to the two referees + Editor)
```

## How to pick

- **No clear IO angle yet** → `rje-topic-selection`
- **Have results, fuzzy on the "so what"** → `rje-contribution-framing`
- **Design is the bottleneck** → `rje-identification-strategy`
- **About to press submit** → `rje-submission` (page caps are hard)
- **Got an R&R from the handling Editor** → `rje-rebuttal`

## Symptom-to-skill dispatch table

When a task or reviewer remark arrives mid-project, match the symptom to the specialist skill rather than guessing the stage.

| Symptom or request | Route to | Why |
|---|---|---|
| "Is this even an IO question for RJE?" | `rje-topic-selection` | Scope is deliberately narrow; screen fit first |
| "The intro reads like a methods exercise" | `rje-contribution-framing` | Make the IO advance legible by page 1 |
| "Referee says we miss the frontier" | `rje-literature-positioning` | Stake against the right IO strand |
| "Price is treated as exogenous" | `rje-identification-strategy` | Endogeneity is the central structural threat |
| "Counterfactual looks fragile" | `rje-data-analysis` | Bound it; validate against an episode |
| "Tables blow the 40-page cap" | `rje-tables-figures` | Triage exhibits to the appendix |
| "Subsections are numbered 2.1, 2.2" | `rje-writing-style` | RJE leaves subsections unnumbered |
| "What do we deposit for replication?" | `rje-replication-and-data-policy` | RJE hosts nothing; supporting info discouraged |
| "What happens after submit?" | `rje-review-process` | Editor screen then two anonymous referees |
| "Final checks before upload" | `rje-submission` | Page caps, abstract, fee, portal |
| "We got an R&R" | `rje-rebuttal` | Editor's letter is binding; respect caps |

## Worked routing vignette

Suppose a collaborator says: "Our hospital-merger article got an R&R; one referee disputes the bargaining model's identification and the Editor wants the welfare number bounded — and we are over the page cap." Route in order:

- **Editor's binding ask (bound the welfare number) and identification dispute** → `rje-rebuttal` to plan the response, drawing on `rje-identification-strategy` for the bargaining-identification defense and `rje-data-analysis` for the bounded counterfactual.
- **Over the page cap** → `rje-tables-figures` and `rje-submission` to triage exhibits into the appendix before resubmission.
- **House-style drift in the revision** → `rje-writing-style` for a final pass.

The router's job is to sequence these, not to perform any one of them.

## Lifecycle calibration anchors

- The lifecycle is roughly linear early (topic → framing → positioning → design → analysis → exhibits → style) but loops once an R&R arrives: rebuttal pulls back into identification, analysis, and exhibits before resubmission.
- The two hard external gates are the editor screen (clear it with a legible IO hook and page-cap discipline) and the two-referee read (clear it with credible identification and bounded counterfactuals).
- Treat these stages as a default ordering, not a rigid pipeline; an applied-theory IO article may compress the empirical skills and lean on framing, positioning, and writing-style. Confirm any process specifics against the journal's current author guidelines.

## Output format

```
【Stage】topic / framing / design / analysis / exhibits / style / package / submission / rebuttal
【RJE fit risk】on-scope IO? [Y/N/uncertain]
【Next skill】rje-...
【Why】one line
```
