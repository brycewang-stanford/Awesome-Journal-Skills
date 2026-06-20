# Annals of the American Association of Geographers Skills

<p align="center">
  <img src="assets/cover.svg" alt="Annals of the AAG cover" width="200">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Annals%20of%20the%20AAG-1f6a4a)](https://www.tandfonline.com/journals/raag21)
[![Field](https://img.shields.io/badge/field-Geography-1f6feb)](https://www.aag.org/journal/annals-of-the-aag/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at the **Annals of the American Association of Geographers
(Annals of the AAG)** — the **flagship geography journal**, founded in **1911** (as the *Annals of the
Association of American Geographers*) and published by **Taylor & Francis (Routledge)** for the
**American Association of Geographers (AAG)**. The Annals publishes the best scholarship across the
**whole discipline of geography**, organized around **four areas** plus a cross-disciplinary track:
**Geographic Methods** (GIScience, spatial analysis, modeling); **Human Geography**; **Nature and
Society**; and **Physical Geography, Earth, and Environmental Sciences** — quantitative/spatial,
GIScience, remote-sensing, qualitative, and mixed-methods work alike.

This repository is opinionated. It is **not** a generic social-science writing toolbox and it is **not**
an economics or GIS-software pack repurposed for geography. It is an **Annals-specific** stack: a
question where **space, place, and scale are load-bearing**, an argument grounded in **geographic
theory** that speaks across the four areas, a design **defended on its own terms** (spatial
autocorrelation, MAUP/scale, validation, positionality), **maps held to cartographic standard**,
**double-anonymous** preparation, and **spatial-data provenance + geoprivacy** handled honestly.

---

## What Is the Annals, and Why a Dedicated Stack?

The Annals's constraints differ from a specialty geography journal or a methods journal:

| Constraint            | Annals of the AAG                                                              | Implication                                                       |
|-----------------------|-------------------------------------------------------------------------------|------------------------------------------------------------------|
| Scope                 | **Whole discipline**, structured in **four areas** + General Geography         | The paper must matter across geography, not one sub-field         |
| Premium on            | **Geographic significance** (space/place/scale load-bearing) + geographic theory | A "domain study with a map" is off-fit                         |
| Methods               | Spatial-quant, GIScience, remote-sensing, qualitative, mixed — judged on own terms | Do not force one template onto every paper                    |
| Publisher / owner     | **Taylor & Francis (Routledge)** / **AAG**                                     | Submitted via **ScholarOne Manuscripts**                         |
| Review model          | **Double-anonymous**; 1–3 referees (one editor/designate)                      | Anonymize the manuscript and study-site detail                   |
| Editors               | A **subject editor per area** + General + a **Cartography Editor**; four-year terms | Declare the area; it routes the editor and the bar          |
| Length                | **Article ≤ 11,000 words *including* abstract, refs, notes, tables, captions** | Budget the whole document, not just the body                     |
| Other formats         | **Forums** (≤ 25,000 total) and **Commentaries** (< 2,000)                     | Choose the right format up front                                 |
| Style                 | **Chicago Manual of Style** (author-date); 3–5 italicized keywords             | Not a generic style; keywords italicized & alphabetized          |
| Exhibits              | **Maps held to cartographic standard** (projection, classification, legend)    | A Cartography Editor reviews; figures count toward the cap       |
| Transparency          | Spatial-data **provenance + geoprivacy**; T&F data policy                      | Document sources/CRS/processing; mask sensitive locations        |

Volatile specifics (editors and terms, exact caps, abstract length, fee/APC, data-policy wording) change
— items not directly confirmed are marked **待核实** in
[`resources/official-source-map.md`](resources/official-source-map.md). **Official basis checked 2026-06.**
**Verify on the official journal page.**

### The four areas (declare one)

- **Geographic Methods** — GIScience, spatial analysis, modeling, geocomputation.
- **Human Geography** — social/cultural/economic/political/urban geography, often qualitative.
- **Nature and Society** — coupled human-environment systems, political ecology, hazards, land change.
- **Physical Geography, Earth & Environmental Sciences** — geomorphology, biogeography, climatology, remote sensing.
- **General Geography (cross-disciplinary)** — contributions that span the areas.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/annals-aag-skills
/plugin install annals-aag-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/annals-aag-skills.git
cd annals-aag-skills

mkdir -p ~/.claude/skills && cp -R skills/aaag-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/aaag-* ~/.codex/skills/
```

### First Prompt

```
Use aaag-workflow to tell me which skill I should use next for my Annals of the AAG manuscript.
```

---

## Default Workflow

```text
aaag-topic-selection
        ▼
aaag-literature-positioning
        ▼
aaag-theory-building
        ▼
aaag-research-design
        ▼
aaag-data-analysis
        ▼
aaag-tables-figures
        ▼
aaag-writing-style          (polish)
        ▼
aaag-transparency-and-data
        ▼
aaag-review-process
        ▼
aaag-submission
        ▼
aaag-rebuttal
```

`aaag-workflow` is the router — it tells you which skill to use next based on where you are and which of
the **four areas** your paper targets. Most papers loop theory ↔ design ↔ analysis several times before
writing-style.

---

## Skills

| Skill                            | Purpose                                                                       |
|----------------------------------|-------------------------------------------------------------------------------|
| `aaag-workflow`                  | Router — decides which sub-skill to invoke next; picks the area & article type |
| `aaag-topic-selection`           | Geographic-significance fit + area declaration (Methods/Human/Nature-Society/Physical/General) |
| `aaag-literature-positioning`    | Enter a geographic conversation across the area and the discipline             |
| `aaag-theory-building`           | Build a portable geographic argument (place, scale, space-time, environment-society) |
| `aaag-research-design`           | Defend the design — spatial/quant & GIS, remote-sensing/physical, qualitative, mixed |
| `aaag-data-analysis`             | Spatially honest analysis (autocorrelation, MAUP, validation), uncertainty, robustness |
| `aaag-tables-figures`            | Maps to cartographic standard; figures and tables within the inclusive cap     |
| `aaag-writing-style`             | Chicago author-date; 11,000-word inclusive cap; italicized keywords; reads as geography |
| `aaag-transparency-and-data`     | Spatial-data provenance, reproducibility, and geoprivacy / human-subjects ethics |
| `aaag-review-process`            | Double-anonymous review by area; decision categories; desk-reject triggers     |
| `aaag-submission`                | ScholarOne preflight (area/type, anonymization, word count, keywords, ORCID)   |
| `aaag-rebuttal`                  | Revision response to the subject editor + 1–3 cross-area referees              |

### Resources

- [`resources/external_tools.md`](resources/external_tools.md) — geographic data sources (Census/IPUMS/OSM/Landsat/Sentinel/DEMs/GBIF) + GIS / spatial-stats / remote-sensing / qualitative tooling
- [`resources/official-source-map.md`](resources/official-source-map.md) — official AAG / Taylor & Francis URLs behind every fact, with 待核实 markers on unverified items
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — real, web-verified Annals papers by area × method, with a sibling-journal guardrail
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — before→after Annals-style introduction (fictional, illustrative)

---

## Differences vs. Sibling Journals

| Journal | What it is | Use this pack instead when… |
|---------|------------|------------------------------|
| **Annals of the AAG** | AAG's **broad four-area flagship**, original research | …your geography is load-bearing and reaches across an area |
| *Progress in Human Geography* | review/agenda essays | …you are writing original empirical work, not a review |
| *Geographical Analysis* | formal spatial-analytic methods | …your Methods contribution is broader/more applied than GA |
| *IJGIS* | GIScience methods/algorithms | …the geographic question, not the algorithm, leads |
| *The Professional Geographer* / *Transactions of the IBG* | shorter AAG reports / UK flagship | …you want the AAG's broad full-length flagship |

---

## What This Repo Does Not Do

- It does not write a submittable manuscript for you
- It does not simulate any specific editor's or reviewer's taste
- It does not assert volatile metadata (current editors and terms, exact caps, fee/APC, policy wording) — verify on the official page; unverified items are marked 待核实
- It does not decide whether your geography is load-bearing or which area fits — that is the researcher's call

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [Annals of the AAG (Taylor & Francis Online)](https://www.tandfonline.com/journals/raag21) — publisher home
- [Annals of the AAG at the AAG](https://www.aag.org/journal/annals-of-the-aag/) — owner, areas, author guidelines

---

## License

MIT
