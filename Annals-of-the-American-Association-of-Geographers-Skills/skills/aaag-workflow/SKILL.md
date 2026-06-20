---
name: aaag-workflow
description: Use when starting or navigating any Annals of the American Association of Geographers (Annals of the AAG) manuscript and you need the entry point. Routes to the right sub-skill based on lifecycle stage and which of the journal's four areas (plus the cross-disciplinary track) the paper targets. It dispatches; it does not draft content.
---

# Annals of the AAG Workflow Router (aaag-workflow)

The orchestrator for an Annals submission. Figure out the stage and the **area**, then send the user
to the matching skill. The Annals is the **broad four-area flagship of the discipline** — the router's
first job is to make the paper legible as *geography*, not just as a domain study that happens to use
maps or coordinates.

## When to trigger

- Starting a new Annals paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Deciding which of the **four areas** (or the cross-disciplinary/General Geography track) the paper targets
- Choosing the **article type** (Article, Forum, Commentary) — they have different caps
- Returning with a decision letter (route to `aaag-rebuttal`)

## First question: which area?

The Annals routes manuscripts to a **subject editor by area**; the area you declare shapes the
reviewers and the bar. Pick the closest, or General Geography if the contribution is discipline-wide.

| Your work | Area | Watch for |
|-----------|------|-----------|
| Spatial analysis, GIScience, modeling, geocomputation | **Geographic Methods** | method must advance geographic inference, not just apply a tool |
| Social/cultural/economic/political/urban geography, often qualitative | **Human Geography** | engage geographic theory; not a sociology paper with a map |
| Coupled human-environment systems, political ecology, hazards, land change | **Nature and Society** | both sides (nature *and* society) must be theorized |
| Geomorphology, biogeography, climatology, remote sensing of the environment | **Physical Geography, Earth & Environmental Sciences** | rigor of an earth-science venue + geographic framing |
| Contribution spans areas / is discipline-wide | **General Geography (cross-disciplinary)** | say why all geographers should care |

## Article type (caps differ — see `aaag-submission`)

| Format | Scope | Cap (verify; 检索于 2026-06) |
|--------|-------|------------------------------|
| **Article** | full original study | **≤ 11,000 words** incl. abstract, refs, notes, tables, figure captions |
| **Forum** | curated multi-author debate | intro 2,500 + papers 5,000 each, **≤ 25,000 total** |
| **Commentary** | response/short intervention | **< 2,000 words** incl. references |

## Routing map (stage → skill)

```text
Area fit & framing?              → aaag-topic-selection
Where does it sit in geography?  → aaag-literature-positioning
What's the geographic argument?  → aaag-theory-building
Is the design defensible?        → aaag-research-design
Are the analyses sound?          → aaag-data-analysis
Are the maps/exhibits clear?     → aaag-tables-figures
Does it read as geography?       → aaag-writing-style
Spatial-data provenance/ethics?  → aaag-transparency-and-data
How will it be judged?           → aaag-review-process
Ready to submit?                 → aaag-submission
Got an R&R / decision?           → aaag-rebuttal
```

## Default order

`topic-selection → literature-positioning → theory-building → research-design → data-analysis →
tables-figures → writing-style → transparency-and-data → review-process → submission → rebuttal`

Iterate: most papers loop theory ↔ design ↔ analysis several times before writing-style.

## Geography fit check (run before routing onward)

| Check | Pass condition | Route if weak |
|-------|----------------|---------------|
| Geographic-ness | The space/place/scale/spatial-process is *constitutive* of the argument, not decorative. | `aaag-topic-selection` |
| Area | The paper clearly targets one of the four areas (or General Geography). | area table above |
| Method on own terms | Quantitative/spatial, GIScience, remote-sensing, or qualitative work is defended in its own tradition. | `aaag-research-design` |
| Spatial-data integrity | Projections, sources, and geoprivacy/human-subjects ethics have a plan. | `aaag-transparency-and-data` |

If "geographic-ness" fails — the paper would be unchanged if you deleted the geography — do not route
to writing-style; it needs a theory/fit repair (`aaag-topic-selection`).

## Anti-patterns

- Treating the Annals like a domain journal that "also takes maps" — the geography must be load-bearing
- Forcing a quantitative-spatial template onto qualitative human geography (each area is judged on its own terms)
- Picking the wrong area editor (a Nature-Society paper sent as pure Physical, or vice versa)
- Sending a 14,000-word draft to a journal that caps everything (incl. captions/notes) at 11,000

## Output format

```
【Stage】idea / positioning / theory / design / analysis / exhibits / writing / transparency / review / submit / rebut
【Area】Methods / Human / Nature-Society / Physical / General
【Type】Article / Forum / Commentary
【Route to】aaag-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — geographic data + GIS/remote-sensing/spatial software by area
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official Annals/AAG/Taylor & Francis URLs behind every fact in this pack
