---
name: rje-workflow
description: Router for The RAND Journal of Economics (RJE) manuscript lifecycle — decides which rje-* skill to use next for an industrial-organization paper, from IO topic fit through Wiley Research Exchange submission and referee response. Start here when unsure.
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

## Output format

```
【Stage】topic / framing / design / analysis / exhibits / style / package / submission / rebuttal
【RJE fit risk】on-scope IO? [Y/N/uncertain]
【Next skill】rje-...
【Why】one line
```
