---
name: epsl-workflow
description: Use when starting or resuming any Earth and Planetary Science Letters (EPSL) manuscript and you need the entry point. Routes to the right EPSL sub-skill based on lifecycle stage and on whether the work matches the letters format (a concise, high-significance Letter; an invited Frontiers Paper; or a Comment/Reply). It dispatches; it does not draft content.
---

# EPSL Workflow Router (epsl-workflow)

The dispatcher for an EPSL submission. EPSL is Elsevier's flagship **letters journal for solid-Earth
and planetary science** (founded 1966, ISSN 0012-821X): it wants a **concise Letter carrying one
decisive, process-level advance** about the physical, chemical or mechanical workings of the Earth or
another planet. The router's first job is therefore double: locate the stage, and confirm the result
is a *Letter* — not a data report, not a regional case study, not two papers stapled together.

## When to trigger

- Starting an EPSL manuscript and unsure where to begin
- Mid-project and unsure which skill applies next
- Unsure whether the work is letters-shaped or belongs at a specialist journal
- Returning with a decision letter (route to `epsl-revision-and-rebuttal`)

## First question: is this a Letter?

| Situation | Verdict | Route to |
|-----------|---------|----------|
| One decisive advance on a process of Earth/planetary interiors, surfaces, or atmospheres | Letter — proceed | pipeline below |
| Solid dataset, insight local to one region or one analyte | not yet letters-shaped | `epsl-topic-selection` to reframe or redirect |
| Two intertwined results needing two manuscripts | companion papers are discouraged at EPSL | merge to one Letter or split venues |
| Field-wide synthesis | **Frontiers Paper** — by editor invitation only | do not self-select; query first |
| Dispute with a published EPSL paper | Comment / Reply | `epsl-review-process` for etiquette |

> Length is policed: the main text (introduction through conclusions) is capped near 6,500 words —
> re-check the exact figure on the official Guide for Authors before trusting it.

## Routing map (stage → skill)

```text
Does the idea clear the frontier bar?      → epsl-topic-selection
Which literatures must the gap engage?     → epsl-literature-positioning
Will the sampling/analytical plan hold?    → epsl-study-design
Are uncertainties fully propagated?        → epsl-data-analysis
Do the exhibits work for four sub-fields?  → epsl-figures-and-tables
Data deposited FAIR, methods transparent?  → epsl-reporting-and-reproducibility
Does it read like a Letter?                → epsl-writing-style
Pitching the handling editor?              → epsl-cover-letter
How will it be judged?                     → epsl-review-process
Ready for Editorial Manager?               → epsl-submission
Decision letter arrived?                   → epsl-revision-and-rebuttal
```

## Default order

`topic-selection → literature-positioning → study-design → data-analysis → figures-and-tables →
reporting-and-reproducibility → writing-style → cover-letter → review-process → submission →
revision-and-rebuttal`

Expect loops: geochronology and isotope work cycles design ↔ analysis until the uncertainty budget
closes; modeling work cycles design ↔ figures until the resolution tests convince.

## Symptom → skill quick-routing

| User says | Underlying EPSL risk | Route to |
|-----------|----------------------|----------|
| "Is this significant enough for EPSL?" | frontier-vs-incremental desk screen | `epsl-topic-selection` |
| "The editor called it a regional study" | no process-level takeaway | `epsl-topic-selection`, `epsl-literature-positioning` |
| "Reviewer wants the full error budget" | analytical-transparency gap | `epsl-data-analysis` |
| "Where do I put 400 zircon analyses?" | data table belongs in repository/supplement | `epsl-reporting-and-reproducibility` |
| "I'm 2,000 words over" | letters-format cap | `epsl-writing-style` |
| "Which repository counts as FAIR?" | data-availability mandate | `epsl-reporting-and-reproducibility` |
| "Got a major revision" | rebuttal strategy | `epsl-revision-and-rebuttal` |

## Worked micro-example (illustrative — routing a subduction-zone water paper)

A user arrives: "I have B isotopes and seismic velocities suggesting slab fluids reach the deep
arc — where do I start?" The router's pass (illustrative):

1. **Frontier check** → `epsl-topic-selection`: the claim generalizes (how water leaves slabs), so it
   clears the process bar; confirm Letter shape, one advance.
2. **Positioning** → `epsl-literature-positioning`: the gap must engage geochemists *and*
   seismologists, or one of the two reviewers will call it naive.
3. **Design/analysis loop** → `epsl-study-design` ↔ `epsl-data-analysis`: reference materials, blanks,
   2σ external reproducibility, and the velocity-model resolution test.
4. **Exhibits + deposit** → `epsl-figures-and-tables`, `epsl-reporting-and-reproducibility`: one
   cross-section figure carrying the argument; data to EarthChem, waveform products via IRIS/EarthScope.
5. **Write → pitch → submit** → `epsl-writing-style` → `epsl-cover-letter` → `epsl-submission`.

The router's standing job: surface the two gates the editors weigh first — process-level significance
and analytical transparency — before any prose is written.

## Anti-patterns

- Treating EPSL as a general geoscience outlet — a sound regional dataset with no process insight is the classic desk decline
- Planning companion papers; EPSL explicitly discourages them
- Self-selecting "Frontiers Paper" without an editor's invitation
- Discovering the ~6,500-word main-text cap after the draft is 9,000 words
- Leaving data deposition and the methods supplement until submission week

## Output format

```
【Stage】idea / positioning / design / analysis / exhibits / reproducibility / writing / cover-letter / review / submit / revise
【Format check】Letter / invited Frontiers / Comment-Reply / not letters-shaped
【Route to】epsl-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — geochemistry, geophysics, and geochronology tooling by sub-field
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official Elsevier/EPSL URLs behind every fact in this pack
