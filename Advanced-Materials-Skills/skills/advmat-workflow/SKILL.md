---
name: advmat-workflow
description: Use when deciding which advmat-* sub-skill to invoke next, or when sequencing manuscript work from scope-fit through revision for an Advanced Materials (Adv. Mater.) manuscript. Routes — does not replace — the specialized skills.
---

# Advanced Materials Workflow (advmat-workflow)

## Overview

This is the router. It does not do the work of any specialized skill; it names **which advmat-* skill fits your current stage** and hands off.

Default assumption: unless told otherwise, the target is **Advanced Materials (Adv. Mater.)** — Wiley-VCH's flagship materials-science journal. The defining bar is a genuine **materials-science advance** (a new material, mechanism, or property — not an incremental improvement) that is **rigorously characterized by multiple complementary techniques**, ideally carried through to a **device-level demonstration benchmarked against the state of the art**, and communicated with **cover-quality figures**. If the work is solid but incremental or narrowly functional, its home is more likely **Advanced Functional Materials**, **Advanced Science**, **Small**, or **Advanced Materials Interfaces**, and `advmat-scope-fit` will say so.

## When to trigger

- User asks "what should I do next?" on a materials manuscript
- User drops a draft and needs the current bottleneck diagnosed
- User is unsure whether the result is "Adv. Mater.-worthy" or belongs in a sibling Advanced-portfolio journal
- The manuscript is over the Communication/Article length format and content must be re-partitioned
- User received a Wiley reviewer report and needs to switch into response mode

## Routing table

| Current symptom                                                        | Next skill                |
|------------------------------------------------------------------------|---------------------------|
| Unsure if the advance is novel / broad enough for Adv. Mater.          | `advmat-scope-fit`        |
| Result is real but the "why this is an advance" is unclear             | `advmat-results-framing`  |
| Characterization is thin, or the experimental section sprawls          | `advmat-methods`          |
| Figures are dense; no cover-quality lead figure or TOC graphic         | `advmat-figures`          |
| Manuscript leans on the SI; reader can't follow without it             | `advmat-supplementary`    |
| Prose is wordy, hedged, or not Wiley house style                       | `advmat-writing-style`    |
| Over the Communication (~4 pp) or Article (~10 pp) format budget       | `advmat-length-management`|
| Need a cover letter that argues advance + broad impact                 | `advmat-cover-letter`     |
| Ready to submit; need format / file / metadata preflight               | `advmat-submission`       |
| Choosing suggested/opposed referees; anticipating objections           | `advmat-referee-strategy` |
| Received a reviewer report or editor decision; need to respond         | `advmat-revision`         |

## Default order

1. `advmat-scope-fit` — settle the advance + broad-impact gate first; redirect to a sibling journal if it fails
2. `advmat-results-framing` — lock the single central advance and its significance
3. `advmat-methods` — make the multi-technique characterization airtight; full experimental detail to the SI
4. `advmat-figures` — design the lead figure and the TOC graphic to convey the advance at a glance
5. `advmat-supplementary` — partition extended data / methods into Supporting Information; the paper must stand alone
6. `advmat-writing-style` — Wiley house style, concision, defined nomenclature and units
7. `advmat-length-management` — fit the Communication or Article format (display items and words counted together)
8. `advmat-cover-letter` — argue the advance + broad-impact case to the editors
9. `advmat-submission` — final preflight (format, files, article type, ORCID, TOC graphic)
10. `advmat-referee-strategy` — suggested / opposed referees; pre-empt the characterization / benchmarking objections
11. `advmat-revision` — after the reviewer reports arrive

> `advmat-writing-style` and `advmat-length-management` are **late polish stages**. Do not trim to the page format before the central advance, characterization, and figures are stable, or you will cut load-bearing evidence.

## Decision heuristics

- "Reviewer 2 will ask 'why not Adv. Funct. Mater.?'" → `advmat-scope-fit`
- "I can state the material but not why it is a genuine advance" → `advmat-results-framing`
- "A referee will say the phase assignment isn't proven" → `advmat-methods`
- "My lead figure has ten panels and no single takeaway" → `advmat-figures`
- "You can't judge the material without reading the SI" → `advmat-supplementary`
- "I'm over the page limit and every figure is huge" → `advmat-length-management`
- "The editor needs to be told why this matters beyond my subfield" → `advmat-cover-letter`
- "Submitting tonight" → `advmat-submission`
- "Who should I suggest as a referee?" → `advmat-referee-strategy`
- "Three reviewer reports just landed" → `advmat-revision`

## Manuscript status board

Readiness is a two-column question: is the *science* settled, and does it *fit the format*? Fill this board before invoking `advmat-submission`; any cell still marked OPEN routes you back to the named skill.

```text
ADV. MATER. STATUS BOARD                  verdict   owner skill
========================================  ========  =====================
GATE  materials advance + broad impact    OPEN      advmat-scope-fit
      (fails → retarget AFM / Adv.Sci.)
ADVANCE one central new material /        OPEN      advmat-results-framing
      mechanism / property, stated plainly
CHAR  multi-technique characterization     OPEN      advmat-methods
      proves structure→property claim
FIG   lead figure + TOC graphic =          OPEN      advmat-figures
      the advance at a glance
SI    paper stands alone; SI holds         OPEN      advmat-supplementary
      extended data / full experimental
STYLE Wiley house style, units defined     OPEN      advmat-writing-style
FIT   inside Communication / Article        OPEN      advmat-length-management
      format (display items counted)
CASE  cover letter argues advance+impact    OPEN      advmat-cover-letter
REFS  suggested / opposed referees named    OPEN      advmat-referee-strategy
----------------------------------------  --------  ---------------------
all rows CLOSED → advmat-submission preflight → submit
reviewer report arrives → advmat-revision
```

## Differences vs. sibling Advanced-portfolio journals

Advanced Materials shares Wiley-VCH production and rigor standards with Advanced Functional Materials, Advanced Science, Small, and Advanced Materials Interfaces, but differs on the **gate**:

- **Adv. Mater.**: a broadly significant materials advance — a new material, mechanism, or property that reshapes how a field thinks. Incremental optimization is declined on impact grounds even when flawless.
- **AFM / Small / Adv. Sci. / AMI**: excellent, rigorous, but appropriately specialist or incremental work with a well-defined audience.

If `advmat-scope-fit` returns a "specialist / incremental" verdict, retarget rather than fighting the impact gate.

## Anti-patterns

- **Do not** skip `advmat-scope-fit` — editors triage on advance/impact first; a wrong-venue paper burns a submission cycle
- **Do not** run `advmat-length-management` before the science is stable — you will cut characterization the referees need
- **Do not** let the Supporting Information become the place where the real evidence hides
- **Do not** draft `advmat-revision` responses before you have actually changed the manuscript and added the requested data

> Durable norms only. Verify current word/page limits, article types, formats, and policies on the official Wiley Advanced Materials author page.
