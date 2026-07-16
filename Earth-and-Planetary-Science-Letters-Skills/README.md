# Earth and Planetary Science Letters Skills

<p align="center">
  <img src="assets/cover.svg" alt="Earth and Planetary Science Letters cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-EPSL-5b4a2f)](https://www.sciencedirect.com/journal/earth-and-planetary-science-letters)
[![Field](https://img.shields.io/badge/field-Solid--Earth%20%26%20Planetary%20Science-1f6feb)](https://www.sciencedirect.com/journal/earth-and-planetary-science-letters)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **Earth and Planetary Science Letters (EPSL)** —
Elsevier's flagship **letters journal for solid-Earth and planetary science** (founded 1966, ISSN
0012-821X). EPSL publishes **concise, high-significance Letters** on the physical, chemical and
mechanical processes of the Earth and other planets — including extrasolar ones — from deep interiors
to atmospheres, across geochemistry, geophysics, geochronology, geodynamics, petrology,
paleomagnetism, cosmochemistry, and planetary interiors.

This repository is opinionated. It is **not** a generic geoscience-writing toolbox, and it is **not**
another discipline's pack with the nouns swapped. It is an **EPSL-specific** stack built around what
actually decides an EPSL paper: the **letters format** (a main text capped near 6,500 words carrying
*one* decisive advance), a **process-level claim** rather than a regional case study, **full
analytical-uncertainty reporting** for isotope and geochronology data, **FAIR data deposition** in
the community's repositories (EarthChem, PANGAEA, IRIS/EarthScope, MagIC, NASA PDS), and framing
that reaches a **multi-disciplinary Earth-and-planets readership**.

---

## What Is EPSL, and Why a Dedicated Stack?

EPSL's constraints differ from both a specialist geoscience journal and a general-science venue:

| Constraint | EPSL | Implication |
|------------|------|-------------|
| Format | **Letters** — concise, ~6,500-word main text (re-check) | one decisive result; companion papers discouraged |
| Premium on | frontier, **process-level** insight | regional case studies without portable insight are desk-declined |
| Scope | physical/chemical/mechanical processes of **Earth and planets** (incl. extrasolar) | planetary work is in-scope, descriptive locality work is not |
| Readership | geochemists + geophysicists + geodynamicists + planetary scientists | referees typically span two sub-fields |
| Rigor | full uncertainty budgets, standards/blanks/decay constants, MSWD, resolution tests | an undefined ± draws a query |
| Data | data-availability statement + **FAIR repositories** (EarthChem, PANGAEA, IRIS, MagIC, PDS) | "available on request" is a red flag |
| Publisher / portal | Elsevier / **Editorial Manager** | Elsevier declarations: COI, CRediT, funding, AI use |
| Article types | Letters; **invited** Frontiers Papers; Comments/Replies | never self-select Frontiers |

Volatile specifics (the exact word cap, highlights requirement, reference formatting, editor roster,
any APC) change — such items are flagged **re-check** in
[`resources/official-source-map.md`](resources/official-source-map.md).
**Verify on the official journal pages.**

### Article types (details re-check on the official site)

- **Letter** — the standard type: a concise, high-significance original study (main text ≤ ~6,500 words).
- **Frontiers Paper** — field-spanning synthesis, **by editor invitation only**.
- **Comment / Reply** — formal exchange on a published EPSL paper.
- **Erratum / Corrigendum** — corrections.
- **Special-Issue papers** — per the issue's call.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/epsl-skills
/plugin install epsl-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/epsl-skills.git
cd epsl-skills

mkdir -p ~/.claude/skills && cp -R skills/epsl-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/epsl-* ~/.codex/skills/
```

### First Prompt

```
Use epsl-workflow to tell me which skill I should use next for my EPSL manuscript.
```

---

## Default Workflow

```text
epsl-topic-selection
        ▼
epsl-literature-positioning
        ▼
epsl-study-design
        ▼
epsl-data-analysis
        ▼
epsl-figures-and-tables
        ▼
epsl-reporting-and-reproducibility
        ▼
epsl-writing-style           (compress to letters format)
        ▼
epsl-cover-letter
        ▼
epsl-review-process
        ▼
epsl-submission
        ▼
epsl-revision-and-rebuttal
```

`epsl-workflow` is the router — it locates your stage and checks the result is letters-shaped before
anything is drafted. Geochronology and isotope projects typically loop design ↔ analysis until the
uncertainty budget closes.

---

## Skills

| Skill | Purpose |
|-------|---------|
| `epsl-workflow` | Router — checks letters fit, dispatches to the next skill |
| `epsl-topic-selection` | The process-level test; frontier-vs-incremental; fit or redirect |
| `epsl-literature-positioning` | Frame the gap across geochem/geophys/geochron/planetary literatures |
| `epsl-study-design` | Sample context, traceability, replication, discriminating designs, model falsifiability |
| `epsl-data-analysis` | Full uncertainty ladders, standards/blanks/constants, MSWD, resolution diagnostics |
| `epsl-figures-and-tables` | Few dense exhibits; context panels; uncertainty drawn; no rainbow colormaps |
| `epsl-reporting-and-reproducibility` | Supplement + FAIR deposit (EarthChem/PANGAEA/IRIS/MagIC/PDS/Zenodo) |
| `epsl-writing-style` | Letters compression; process-forward titles; cross-field legibility |
| `epsl-cover-letter` | The subject-editor pitch — advance, number, portability, clean reviewers |
| `epsl-review-process` | Desk screen + paired sub-field referees; harden before submitting |
| `epsl-submission` | Editorial Manager preflight (length, statements, declarations, files) |
| `epsl-revision-and-rebuttal` | Point-by-point strategy; route additions to the supplement, hold the cap |

### Resources

- [`resources/external_tools.md`](resources/external_tools.md) — FAIR repositories (EarthChem, PANGAEA, IRIS/EarthScope, MagIC, NASA PDS), GMT/PyGMT, GPlates, ObsPy, IsoplotR/ET_Redux/iolite, geodynamic and phase-equilibrium codes
- [`resources/official-source-map.md`](resources/official-source-map.md) — the official Elsevier/EPSL URLs behind every fact, checked 2026-07-16, with re-check flags
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — landmark EPSL papers by sub-field, each with a self-check question
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — a before→after abstract + introduction in EPSL house style

---

## What This Repo Does Not Do

- It does not write a submittable manuscript for you
- It does not simulate any specific editor's or reviewer's taste
- It does not assert volatile metadata (exact word cap, highlights rules, reference format details, editor roster, APC) — items it cannot pin are flagged re-check against [`resources/official-source-map.md`](resources/official-source-map.md)
- It does not decide whether your result moves a frontier — that judgment stays with the researcher

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — index of journal-specific skill packs
- [Earth and Planetary Science Letters (ScienceDirect)](https://www.sciencedirect.com/journal/earth-and-planetary-science-letters) — journal home
- [EPSL Guide for Authors](https://www.sciencedirect.com/journal/earth-and-planetary-science-letters/publish/guide-for-authors) — article types, length, policies

---

## License

MIT
