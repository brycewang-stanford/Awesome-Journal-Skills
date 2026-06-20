# Global Change Biology Skills

<p align="center">
  <img src="assets/cover.svg" alt="Global Change Biology cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-GCB-0e8a8a)](https://onlinelibrary.wiley.com/journal/13652486)
[![Field](https://img.shields.io/badge/field-Global%20Change%20Biology-1f6feb)](https://onlinelibrary.wiley.com/page/journal/13652486/homepage/productinformation.html)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **Global Change Biology (GCB)** — the leading journal on
the **impacts of global environmental change on biological systems**, **first published in 1995** and
published by **Wiley**. GCB exists to advance understanding of the interface between **global
environmental change** (climate warming, rising CO2 and tropospheric ozone, nitrogen deposition,
land-use change, ocean change) and **biological systems** — at any level of organization from
**molecular to biome**, in **aquatic or terrestrial**, **managed or natural** environments, including
both biological responses **and** feedbacks to change.

This repository is opinionated. It is **not** a generic ecology writing toolbox, and it is deliberately
**distinct from a conservation-practice pack**: GCB is about **global-change mechanisms and ecosystem
processes** — the causal link between a **driver** of global change and a **biological response** — not
conservation action plans or management prescriptions. A GCB paper leads with a **mechanism of broad
relevance**, defends its **scale and uncertainty**, carries a **graphical abstract** of the
driver-to-response link, and **archives data and code with a DOI** as a condition of publication.

---

## What Is GCB, and Why a Dedicated Stack?

GCB's constraints differ from a regional ecology journal or a conservation journal:

| Constraint            | GCB                                                                            | Implication                                                       |
|-----------------------|--------------------------------------------------------------------------------|-------------------------------------------------------------------|
| Scope                 | **Global environmental change × biological systems** (molecular → biome)       | Need a global-change driver and a biological response/feedback    |
| Premium on            | **Mechanism + broad relevance**, not local description                         | A single-site result with no mechanism is off-fit                 |
| Distinct from         | **Conservation practice** (action/management)                                  | GCB wants mechanism/ecosystems, not conservation prescriptions    |
| Publisher             | **Wiley**                                                                       | Submitted via **ScholarOne / Manuscript Central**, not Editorial Manager |
| Review model          | Editor-mediated expert review; live-check current anonymity/transparent-review options | Pre-empt expert concerns and data-access requests      |
| Length                | Research articles currently route to an **up to 8,000-word** main-body cap     | Confirm the current cap by article type before upload             |
| Abstract              | **300-word limit**; **6–10 keywords or phrases**                               | State aim, approach, quantified result, conclusion                |
| Graphical abstract    | **Required** — depicts the driver-to-response mechanism                        | Not a site map or phylogeny                                       |
| Data & code           | **Archived in a public repo with a DOI** as a condition of publication         | **"Available on request" is not accepted** — deposit before publication |

Volatile specifics (exact caps, accepted article types, fee/APC, policy wording, review model) change.
[`resources/official-source-map.md`](resources/official-source-map.md) now routes each operational fact
to Wiley, ScholarOne, or a DOI-capable repository source; live-check the official Wiley pages in a
browser immediately before upload.

### Article types

- **Primary Research Articles** — completed original studies with a global-change mechanism.
- **Technical Advances** — new tools, methods, or modelling approaches for global-change biology.
- **Reviews / Research Reviews** — integrative syntheses; **GCB Reviews are by invitation**, while the
  **Research Reviews** section is open for unsolicited submission.
- **Opinions / Perspectives** — argued, forward-looking pieces; live-check the current word caps and
  eligibility before choosing this route.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/gcb-skills
/plugin install gcb-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/gcb-skills.git
cd gcb-skills

mkdir -p ~/.claude/skills && cp -R skills/gcb-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/gcb-* ~/.codex/skills/
```

### First Prompt

```
Use gcb-workflow to tell me which skill I should use next for my Global Change Biology manuscript.
```

---

## Default Workflow

```text
gcb-topic-selection
        ▼
gcb-literature-positioning
        ▼
gcb-study-design
        ▼
gcb-data-analysis
        ▼
gcb-figures-and-tables
        ▼
gcb-reporting-and-data-policy
        ▼
gcb-writing-style           (polish)
        ▼
gcb-cover-letter
        ▼
gcb-review-process
        ▼
gcb-submission
        ▼
gcb-revision-and-rebuttal
```

`gcb-workflow` is the router — it tells you which skill to use next based on where you are and which
**article type** fits. If your contribution is a **method/tool**, route to `gcb-study-design` as a
**Technical Advance**; if it is a **synthesis**, route to `gcb-literature-positioning` for a **Research
Review** (GCB Reviews are commissioned).

---

## Skills

| Skill                            | Purpose                                                                       |
|----------------------------------|-------------------------------------------------------------------------------|
| `gcb-workflow`                   | Router — decides which sub-skill to invoke next; picks the article type        |
| `gcb-topic-selection`            | Global-change fit test: driver → response, mechanism, broad relevance          |
| `gcb-literature-positioning`     | Position across ecology/biogeochemistry/Earth-system literatures               |
| `gcb-study-design`               | Experiments, gradients/observation, and modelling — scale, replication, realism|
| `gcb-data-analysis`              | Mixed models, meta-analysis, model evaluation, honest uncertainty              |
| `gcb-figures-and-tables`         | Mechanism-first exhibits + the required graphical abstract                     |
| `gcb-reporting-and-data-policy`  | DOI data/code archiving; data availability statement; sensitive-data path      |
| `gcb-writing-style`              | Mechanism + significance up front; quantified, accessible, within caps         |
| `gcb-cover-letter`               | Editor-facing scope-fit + advance in a focused letter                          |
| `gcb-review-process`             | Desk screening, expert 2–3-reviewer review, decision categories                |
| `gcb-submission`                 | ScholarOne preflight (article type, abstract, graphical abstract, data)        |
| `gcb-revision-and-rebuttal`      | Point-by-point response defending mechanism, scale, and uncertainty            |

### Resources

- [`resources/external_tools.md`](resources/external_tools.md) — global-change data sources (ERA5 / CMIP6 / FLUXNET / MODIS / GBIF / TRY) + R / Python / process-model and meta-analysis tooling, and DOI repositories (Dryad / Zenodo / PANGAEA)
- [`resources/official-source-map.md`](resources/official-source-map.md) — official Wiley / GCB URLs behind every fact, plus live-check notes for volatile items

---

## What This Repo Does Not Do

- It does not write a submittable manuscript for you
- It does not simulate any specific editor's or reviewer's taste
- It does not assert volatile metadata (exact caps, article types, fee/APC, policy wording, review model) without an official-source route; live-check those items on the official page before submission
- It does not turn a conservation-management or local-description paper into a global-change mechanism — that is the researcher's science

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [Global Change Biology (Wiley Online Library)](https://onlinelibrary.wiley.com/journal/13652486) — publisher home
- [GCB author guidelines](https://onlinelibrary.wiley.com/page/journal/13652486/homepage/forauthors.html) — submission guidelines and policies
- [ScholarOne / Manuscript Central](https://mc.manuscriptcentral.com/gcb) — submission portal

---

## License

MIT
