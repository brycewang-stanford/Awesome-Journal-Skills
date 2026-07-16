---
name: ngeo-workflow
description: Use when deciding which ngeo-* sub-skill to invoke next, or when sequencing manuscript work from scope-fit through revision for a Nature Geoscience (Nat. Geosci.) manuscript. Routes — does not replace — the specialized skills.
---

# Nature Geoscience Workflow (ngeo-workflow)

## Overview

This is the router. It does not do any one stage's work; it tells you **which ngeo-* skill to use at your current stage** and in what order.

Default assumption: unless the user says otherwise, the target is **Nature Geoscience** — a Nature Portfolio flagship that publishes Earth-system advances of broad, cross-disciplinary interest across the solid Earth, atmosphere, oceans, cryosphere, climate, and planetary science. The winning manuscript is not the most thorough regional case study; it is the one whose quantitative result changes how the wider Earth-science community understands a process. If the work is a solid but locally-scoped or specialist advance, its home is a community journal (JGR, GRL, Climate of the Past, EGU/AGU titles, or *Nature Communications* / *Communications Earth & Environment*), and `ngeo-scope-fit` will say so.

## When to trigger

- User asks "what should I do next?" on an Earth-science manuscript
- User drops a draft and needs the current bottleneck diagnosed
- User is unsure whether the result is "Nature Geoscience-worthy" or belongs in a community journal
- The Article is over the 3,000-word limit and material must be re-partitioned into Methods / Supplementary
- User received a Nature Portfolio editor or referee decision and needs to switch into response mode

## Routing table

| Current symptom                                                            | Next skill                |
|----------------------------------------------------------------------------|---------------------------|
| Unsure if the result is broad / important enough for Nat. Geosci.          | `ngeo-scope-fit`          |
| Result is real but the "why the whole field cares" is unclear              | `ngeo-results-framing`    |
| Methods sprawl into the main text; unsure what goes to online Methods      | `ngeo-methods`            |
| Figures too dense / lead figure does not show the Earth-system advance     | `ngeo-figures`            |
| Main text depends on Supplementary Information to be understood            | `ngeo-supplementary`      |
| Prose is wordy, jargon-heavy, or not accessible to non-specialists         | `ngeo-writing-style`      |
| Over the 3,000-word / display-item / reference limit                       | `ngeo-length-management`  |
| Need a cover letter arguing broad interest to the diverse readership       | `ngeo-cover-letter`       |
| Ready to submit; need format / files / reporting-summary preflight         | `ngeo-submission`         |
| Choosing suggested/excluded referees; anticipating objections              | `ngeo-referee-strategy`   |
| Received referee reports or an editor decision; need to respond            | `ngeo-revision`           |

## Default order

1. `ngeo-scope-fit` — settle the broad-interest Earth-system gate first; redirect to a community journal if it fails
2. `ngeo-results-framing` — lock the single headline advance and its "Here we show" statement
3. `ngeo-methods` — build the online Methods section that grounds every quantitative claim in data or model diagnostics
4. `ngeo-figures` — design a lead figure that carries the Earth-system result and its uncertainty
5. `ngeo-supplementary` — partition extended data, model output, and derivations to SI; keep the main text self-contained
6. `ngeo-writing-style` — Nature house style, "accessible to non-specialists," calibrated claims
7. `ngeo-length-management` — fit the 3,000-word Article budget and 4–6 display-item ceiling (do this AFTER content is stable)
8. `ngeo-cover-letter` — argue broad interest to the in-house editor who triages before review
9. `ngeo-submission` — final preflight (Editorial Manager files, reporting summary, data/code availability)
10. `ngeo-referee-strategy` — suggested / excluded referees; pre-empt likely objections
11. `ngeo-revision` — after the referee reports arrive

> `ngeo-writing-style` and `ngeo-length-management` are **late polish stages**. Do not trim to 3,000 words before the headline advance, Methods, and figures are stable, or you will cut the wrong material.

## Decision heuristics

- "Reviewer 2 will say 'this is a regional study, why not JGR?'" → `ngeo-scope-fit`
- "I can state my measurement but not what it changes about the Earth system" → `ngeo-results-framing`
- "My Methods are three pages of instrument and model detail" → `ngeo-methods`
- "My lead figure is a six-panel map grid with a 12-line caption" → `ngeo-figures`
- "You can't read the main text without the Supplementary" → `ngeo-supplementary`
- "I'm 800 words over and have seven figures" → `ngeo-length-management`
- "The editor needs to see why this is cross-disciplinary" → `ngeo-cover-letter`
- "Submitting tonight; is the Reporting Summary done?" → `ngeo-submission`
- "Who should I suggest as a referee?" → `ngeo-referee-strategy`
- "Three referee reports just landed" → `ngeo-revision`

## Manuscript status board

Readiness is a two-column question: is the *content* settled, and does it *fit the Nature Article container*? Fill this board before invoking `ngeo-submission`; any cell still marked OPEN routes you back to the named skill.

```text
NATURE GEOSCIENCE STATUS BOARD             verdict   owner skill
=========================================  ========  =====================
GATE  broad Earth-system interest +        OPEN      ngeo-scope-fit
      quantitative advance (fails →
      retarget community journal)
CLAIM one headline advance, framed as      OPEN      ngeo-results-framing
      "Here we show ..." for the field
METH  online Methods grounds every claim   OPEN      ngeo-methods
      in data / model diagnostics + error
FIG   lead figure = the advance + its      OPEN      ngeo-figures
      uncertainty, map/section legible
SI    main text self-contained; SI holds   OPEN      ngeo-supplementary
      extended data / model output only
STYLE accessible to non-specialists,       OPEN      ngeo-writing-style
      claims calibrated to evidence
FIT   inside 3,000 words + 4-6 display      OPEN      ngeo-length-management
      items + ~50 refs
CASE  cover letter argues broad interest   OPEN      ngeo-cover-letter
DATA  data + code availability + Reporting  OPEN      ngeo-submission
      Summary complete
REFS  suggested / excluded referees named  OPEN      ngeo-referee-strategy
-----------------------------------------  --------  ---------------------
all rows CLOSED → ngeo-submission preflight → submit on Editorial Manager
referee reports arrive → ngeo-revision
```

## Differences vs. community Earth-science journals

Nature Geoscience and community titles (JGR, GRL, Climate Dynamics, *Communications Earth & Environment*) share peer-review rigor but differ on the **gate**:

- **Nature Geoscience**: a broad, cross-disciplinary Earth-system advance, editor-triaged for general interest before review. A rigorous but regionally-scoped or incremental result is declined without review on interest grounds.
- **Community journals**: thorough, specialist-appropriate, archival; regional and incremental advances are welcome and length is generous.

If `ngeo-scope-fit` returns a "specialist / regional" verdict, retarget rather than fighting the broad-interest bar.

## Anti-patterns

- **Do not** skip `ngeo-scope-fit` — Nature editors desk-reject the majority of submissions before review on interest grounds; a wrong-venue manuscript wastes a cycle
- **Do not** run `ngeo-length-management` before content is stable — you will cut load-bearing evidence or uncertainty
- **Do not** let the Supplementary Information become a dump the main text silently depends on
- **Do not** treat data/code availability and the Reporting Summary as afterthoughts — they gate acceptance, not just submission

> Durable norms only. Verify current word/display-item/reference limits, content types, formats, and policies on the official Nature Geoscience author pages (Checked: 2026-07-16).
