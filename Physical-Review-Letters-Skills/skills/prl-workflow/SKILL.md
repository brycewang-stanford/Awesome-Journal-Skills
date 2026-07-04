---
name: prl-workflow
description: Use when deciding which prl-* sub-skill to invoke next, or when sequencing manuscript work from scope-fit through revision for a Physical Review Letters (PRL) manuscript. Routes — does not replace — the specialized skills.
---

# Physical Review Letters Workflow (prl-workflow)

## Overview

This is the router. It does not replace any specialized skill; it tells you **which prl-* skill to use at your current stage**.

Default assumption: unless the user says otherwise, the target is **Physical Review Letters (PRL)** — a short, high-impact Letter that must clear the *importance + broad interest* gate and fit the strict deductible length limit, with detail pushed to Supplemental Material. If the work is a solid but incremental or specialist advance, the right home is **Physical Review A–E** or **Physical Review Research**, and `prl-scope-fit` will say so.

## When to trigger

- User asks "what should I do next?" on a physics Letter
- User drops a draft and needs the current bottleneck diagnosed
- User is unsure whether the result is "PRL-worthy" or belongs in a specialized PR journal
- The Letter is over the length limit and detail must be re-partitioned
- User received an APS referee report and needs to switch into response mode

## Routing table

| Current symptom                                                       | Next skill              |
|-----------------------------------------------------------------------|-------------------------|
| Unsure if the result is important / broad enough for PRL              | `prl-scope-fit`         |
| Result is real but the "why it matters to all physicists" is unclear  | `prl-results-framing`   |
| Methods sprawl into the Letter; can't tell what to keep vs. move      | `prl-methods`           |
| Figures too dense / lead figure doesn't show the central result       | `prl-figures`           |
| Letter doesn't stand alone; reader needs the SM to follow it          | `prl-supplementary`     |
| Prose is wordy, hedged, jargon-heavy, or not APS house style          | `prl-writing-style`     |
| Over the length / figure / equation / reference limit                 | `prl-length-management` |
| Need a cover letter that justifies importance + broad interest        | `prl-cover-letter`      |
| Ready to submit; need format / file / metadata preflight              | `prl-submission`        |
| Choosing suggested/opposed referees; anticipating objections          | `prl-referee-strategy`  |
| Received a referee report or editor decision; need to respond         | `prl-revision`          |

## Default order

1. `prl-scope-fit` — settle the importance + broad-interest gate first; redirect to PR A–E / PR Research if it fails
2. `prl-results-framing` — lock the single central claim and its broad significance
3. `prl-methods` — keep only what a physicist needs to trust the result; the rest goes to SM
4. `prl-figures` — design the lead figure to convey the central result at a glance
5. `prl-supplementary` — partition derivations / extended data into SM; the Letter must stand alone
6. `prl-writing-style` — APS house style, concision, defined notation
7. `prl-length-management` — fit the deductible limit; trim ruthlessly (do this AFTER content is stable)
8. `prl-cover-letter` — argue the importance + broad-interest case to the editors
9. `prl-submission` — final preflight (format, files, classification, metadata)
10. `prl-referee-strategy` — suggested / opposed referees; pre-empt likely objections
11. `prl-revision` — after the referee reports arrive

> `prl-writing-style` and `prl-length-management` are **late polish stages**. Do not trim to the limit before the central claim and figures are stable, or you will cut the wrong material.

## Decision heuristics

- "Reviewer 2 will say 'why not Phys. Rev. B?'" → `prl-scope-fit`
- "I can state the result but not why anyone outside my subfield cares" → `prl-results-framing`
- "My Methods section is three paragraphs of apparatus detail" → `prl-methods`
- "My lead figure has six panels and a 9-line caption" → `prl-figures`
- "You can't understand Fig. 2 without reading the SM" → `prl-supplementary`
- "I'm 600 words over and figures count against me" → `prl-length-management`
- "The editor needs to be told why this is broad-interest" → `prl-cover-letter`
- "Submitting tonight" → `prl-submission`
- "Who should I suggest as a referee?" → `prl-referee-strategy`
- "Three referee reports just landed" → `prl-revision`

## Letter status board

A Letter's readiness is a two-column question: is the *content* settled, and does it *fit the container*? Fill this board before invoking `prl-submission`; any cell still marked OPEN routes you back to the named skill.

```text
PRL STATUS BOARD                          verdict   owner skill
========================================  ========  =====================
GATE  importance + broad interest         OPEN      prl-scope-fit
      (fails → retarget PR A–E / PRR)
CLAIM one central result, stated for      OPEN      prl-results-framing
      physicists outside the subfield
BODY  methods trimmed to what earns       OPEN      prl-methods
      trust; remainder moved to SM
FIG   lead figure = central result        OPEN      prl-figures
      at a glance
SM    Letter stands alone; SM holds       OPEN      prl-supplementary
      derivations / extended data only
STYLE APS house style, notation defined   OPEN      prl-writing-style
FIT   inside the deductible length        OPEN      prl-length-management
      limit (figures/equations count)
CASE  cover letter argues importance      OPEN      prl-cover-letter
REFS  suggested / opposed referees named  OPEN      prl-referee-strategy
----------------------------------------  --------  ---------------------
all rows CLOSED → prl-submission preflight → submit
referee report arrives → prl-revision
```

## Differences vs. specialized Physical Review journals

PRL and Phys. Rev. A–E / PR Research share APS production and rigor standards but differ on the **gate**:

- **PRL**: importance + broad interest, communicated concisely. A correct-but-incremental result is rejected on breadth grounds even if flawless.
- **PR A–E / PR Research**: thorough, archival, specialist-appropriate; length is generous and full methods belong in the body.

If `prl-scope-fit` returns a "specialist" verdict, retarget to the appropriate PR journal rather than fighting the breadth gate.

## Anti-patterns

- **Do not** skip `prl-scope-fit` — editors triage on importance/breadth first; a wrong-venue Letter wastes a submission cycle
- **Do not** run `prl-length-management` before content is stable — you will cut load-bearing material
- **Do not** let `prl-supplementary` become a dumping ground that the Letter silently depends on
- **Do not** draft `prl-revision` responses before you have actually changed the manuscript

> Durable norms only. Verify current word/figure/reference limits, formats, and policies on the official APS / PRL author page.
