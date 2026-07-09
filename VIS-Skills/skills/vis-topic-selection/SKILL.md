---
name: vis-topic-selection
description: Use when deciding whether a project belongs at IEEE VIS or should be routed to EuroVis, PacificVis, CHI, a graphics venue, or the IEEE TVCG journal track, and when choosing among the six VIS areas (Theoretical & Empirical, Applications, Systems & Rendering, Representations & Interaction, Data Transformations, Analytics & Decisions) by contribution type and evidence maturity.
---

# VIS Topic Selection

Decide the venue and the area before drafting. IEEE VIS is the flagship of the visualization
community, and since 2021 it is a **single unified conference** whose full papers are **IEEE TVCG
journal articles** across **six areas**. Two routing questions matter: **is this a visualization
paper at all** (versus HCI, graphics, or ML), and **which of the six areas** is its primary home.
A technically strong paper whose real lesson is about a model, a rendering primitive, or an
interaction unrelated to seeing data is respected and then rejected as out of scope.

## Is it a visualization paper?

VIS rewards contributions about **how people visually represent, interact with, and reason about
data**. The test: if you removed the *visual-representation-and-task* core, is there still a paper?
If the contribution is a machine-learning model whose visualization is incidental, or a rendering
technique with no data-analysis task, or an interaction study with no visual-encoding question, a
sibling venue fits better. If the heart is the encoding, the perception, the analytic workflow, or
the visualization system, it is a VIS paper.

## Choosing among the six areas (the primary-area decision)

| Your contribution's center | Primary area |
|---|---|
| Theory, models, or empirical/perceptual studies establishing visualization foundations | **Theoretical & Empirical** |
| An application or design study solving a real domain problem with visualization | **Applications** |
| Building visualization systems, rendering algorithms, or alternate I/O modalities | **Systems & Rendering** |
| Designing visual representations and interaction techniques for data/users/tasks | **Representations & Interaction** |
| Algorithms that transform data to enable effective visual mapping | **Data Transformations** |
| Integrated human-machine analytic workflows, decision support, ML-in-the-loop | **Analytics & Decisions** |

Your primary area determines the Area Paper Chair and the reviewer pool, so choose the area whose
community will best appreciate the contribution — not merely the one that mentions your keywords.
When a paper spans two areas, pick the one carrying the **primary** contribution and use keywords to
signal the secondary.

## Sibling-venue routing table

| Signal in your project | Better home | Why |
|---|---|---|
| Core visualization contribution, evidence ready, next VIS deadline works | **IEEE VIS** | The flagship; TVCG journal publication across the six areas |
| Equally strong but the European cycle lands sooner, or the topic skews European | **EuroVis / CGF** | Sibling visualization venue; different calendar, Computer Graphics Forum publication |
| Regional fit or the Pacific cycle is nearer | **PacificVis** | Sibling regional visualization venue |
| The heart is interaction/usability with no visual-encoding question | **CHI / UIST** | HCI venues; the contribution is interaction, not visualization |
| The heart is rendering/geometry with no data-analysis task | **SIGGRAPH / graphics venue** | Graphics contribution, not visualization |
| The study is too long/nuanced for the 9-page budget, or you want a journal-first path | **IEEE TVCG (journal track)** | The same journal, entered directly rather than through the VIS call |

## Contribution shapes VIS rewards

- **New visual encoding or interaction technique** — a representation or interaction that lets people
  do an analysis task better, justified perceptually and evaluated (the UpSet lineage).
- **System / toolkit** — an integration that changes how visualizations are built or used, shown in
  real use (the D3 lineage).
- **Perceptual / empirical study** — a controlled result about how people read visualizations that
  changes design practice (the "what makes a visualization memorable?" lineage).
- **Design study** — a real domain problem solved with visualization and reflected into transferable
  lessons (the design-study-methodology lineage).
- **Model / theory / methodology** — a framework that improves how the field designs or evaluates
  (the nested-model lineage) — the "foundations" the venue is built on.

## The remove-the-visualization and re-label tests

Two quick tests sharpen a borderline verdict:

- **Remove-the-visualization test:** if you deleted the visual-representation-and-task core, is there
  still a contribution? If the model or the renderer is the whole paper, route to ML or graphics.
- **Re-label test:** could this be submitted to CHI or SIGGRAPH unchanged and read as native there?
  If its heart is interaction usability or rendering, route accordingly; VIS rewards the
  data-representation-and-reasoning framing.

## Evidence maturity, without the ladder cliché

Fit is necessary but not sufficient: the same idea sits at different doors depending on how far the
evidence has come. An encoding idea with a sketch but no study is a poster or short paper; a system
demonstrated only on data you chose needs a real study or expert use before the full-paper track; a
study too deep for the 9-page budget may belong in the TVCG journal track first. Submitting one step
early earns a "promising, but..." and costs a full annual cycle.

## Decision procedure

```text
[Is-it-VIS] remove the visual-representation-and-task core -> still a paper? no => VIS; yes => reroute
[Contribution type] technique / system / perceptual-study / design-study / model
[Primary area] map the contribution's center to one of the six areas
[Sibling check] interaction-only -> CHI/UIST; rendering-only -> SIGGRAPH; European/Pacific cycle -> EuroVis/PacificVis
[Length check] too long for 9+2? -> consider the TVCG journal track
[Verdict] IEEE VIS (area X) / sibling venue / journal-first, with a one-line reason
```

Run this before the writing skills; a wrong venue or area decision wastes every later step. When the
verdict is VIS, continue with `vis-workflow` for the calendar and `vis-writing-style` for the paper
shape.
