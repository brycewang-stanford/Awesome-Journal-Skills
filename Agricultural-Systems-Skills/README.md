# Agricultural Systems Skills

<p align="center">
  <img src="assets/cover.svg" alt="Agricultural Systems cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Agricultural%20Systems-6b5a2e)](https://www.sciencedirect.com/journal/agricultural-systems)
[![Field](https://img.shields.io/badge/field-Systems%20Analysis-3f7d3a)](https://www.sciencedirect.com/journal/agricultural-systems/about/aims-and-scope)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **Agricultural Systems (AgSy)** — an international journal
for the **systems analysis of agricultural systems**, published by **Elsevier** (ISSN 0308-521X print /
1873-2267 online). Agricultural Systems is, by its own definition, a journal
about **interactions**: among the components of agricultural systems, among hierarchical levels
(field → farm → landscape → region → food system), between agricultural and other land-use systems, and
between agricultural systems and their **natural, social, and economic environments**.

This repository is opinionated. It is **not** a generic agronomy writing toolbox and it is **not** a
field-trial pack repurposed for systems work. It is an **AgSy-specific** stack centered on what makes the
journal distinctive: a genuine **systems question** (interactions, trade-offs, emergent behavior), a
**model described, calibrated, and evaluated** with honest uncertainty, **whole-farm to food-system**
boundaries, and a clear link to a **decision** — design, management, or policy. A single-factor field
trial, however clean, is **off-fit** here unless it is embedded in a systems analysis.

---

## What Is Agricultural Systems, and Why a Dedicated Stack?

AgSy's constraints differ from a field-trial agronomy journal or a generic methods journal:

| Constraint            | Agricultural Systems                                                                  | Implication                                                          |
|-----------------------|----------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| Core object           | **Interactions** across components and hierarchical levels                            | A single-factor result is off-fit unless embedded in a system        |
| Premium on            | **Whole-farm / landscape / food-system** scope + integrated **modelling**             | Pure plot-level agronomy belongs in a field-crops journal            |
| Methods               | Conceptual + empirical + **dynamic / bio-economic modelling**, trade-off analysis      | Describe, calibrate, and **evaluate** the model; report uncertainty  |
| Publisher             | **Elsevier** (ISSN 0308-521X print / 1873-2267 online)                                | Use the current **Submit your article** / Editorial Manager path     |
| Review model          | **Single anonymized**; minimum two reviewers; editor decides                          | Author identity is visible; argue to expert systems reviewers        |
| Length                | Research paper **~8,000 words** (short comm. ~4,000; perspective ~2,000; comment ~1,000) | No hard cap, but stay near the guideline                          |
| Abstract / front      | **Abstract ≤ 250 words** + **Highlights** + **graphical abstract**                    | Prepare all three at submission                                      |
| Declarations          | **CRediT** roles + **declaration of competing interest** + funding / AI disclosures   | Add them up front                                                    |
| Data / code / models  | **Deposit, cite, and link research data** or explain why sharing is not possible      | Elsevier treats code and models as research data — build it as you go |

The current source map was refreshed from live ScienceDirect / Elsevier pages on **2026-06-20**.
Volatile specifics still need a final live check before a real upload, especially editors, APC,
submission-system URL, graphical-abstract specs, and article-type consultation rules.

### Article types

- **Research paper** — the main format; full systems study, **~8,000 words** recommended (no hard cap).
- **Short communication** — a focused contribution, **~4,000 words**.
- **Perspective** — a forward-looking opinion piece, **~2,000 words**, under **rapid review**.
- **Comment** — a short response to published work, **~1,000 words**.
- **Review article** — usually method-application focused rather than descriptive synthesis; consult the
  editors first where the guide requires pre-submission advice.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/agsy-skills
/plugin install agsy-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/agsy-skills.git
cd agsy-skills

mkdir -p ~/.claude/skills && cp -R skills/agsy-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/agsy-* ~/.codex/skills/
```

### First Prompt

```
Use agsy-workflow to tell me which skill I should use next for my Agricultural Systems manuscript.
```

---

## Default Workflow

```text
agsy-topic-selection
        ▼
agsy-literature-positioning
        ▼
agsy-systems-framing-and-modeling
        ▼
agsy-data-and-model-evaluation
        ▼
agsy-figures-and-tables
        ▼
agsy-writing-style          (polish)
        ▼
agsy-impact-and-implications
        ▼
agsy-reproducibility-and-data-policy
        ▼
agsy-review-process
        ▼
agsy-submission
        ▼
agsy-revision-and-rebuttal
```

`agsy-workflow` is the router — it tells you which skill to use next based on where you are. Most
systems papers loop **framing ↔ modelling ↔ evaluation** several times before writing, and the
**impact / decision-relevance** step is what separates an AgSy paper from a methods demo. If your model
is the contribution, spend most of your time in `agsy-systems-framing-and-modeling` and
`agsy-data-and-model-evaluation`.

---

## Skills

| Skill                                  | Purpose                                                                          |
|----------------------------------------|----------------------------------------------------------------------------------|
| `agsy-workflow`                        | Router — decides which sub-skill to invoke next                                  |
| `agsy-topic-selection`                 | Is this a real systems question? Pick scope, scale, and article type             |
| `agsy-literature-positioning`          | Position across systems / modelling / food-system literatures, not one subfield  |
| `agsy-systems-framing-and-modeling`    | System boundaries, components, feedbacks; model choice, description, calibration  |
| `agsy-data-and-model-evaluation`       | Evaluation metrics, sensitivity, uncertainty, trade-off and scenario analysis    |
| `agsy-figures-and-tables`              | Exhibits for interactions, dynamics, trade-offs, and observed-vs-simulated fit   |
| `agsy-reproducibility-and-data-policy` | Deposit data, code, and models; model-description standards; exemptions          |
| `agsy-writing-style`                   | Clear scientific prose; abstract ≤ 250, Highlights, graphical abstract           |
| `agsy-impact-and-implications`         | Decision / management / policy relevance — why the systems result matters        |
| `agsy-review-process`                  | Single-anonymized review, desk screening, reviewer expectations, decision types  |
| `agsy-submission`                      | Editorial Manager preflight (article type, abstract, declarations, data, files) |
| `agsy-revision-and-rebuttal`           | Response-letter strategy for multiple reviewers + editor                         |

### Resources

- [`resources/external_tools.md`](resources/external_tools.md) — systems models (APSIM / DSSAT / STICS / DNDC), whole-farm & bio-economic models, ABM / integrated-assessment tools, calibration / sensitivity / uncertainty packages, and food-system data sources (FAOSTAT / GYGA / FADN)
- [`resources/official-source-map.md`](resources/official-source-map.md) — official Elsevier / ScienceDirect URLs behind every journal fact used by this pack

---

## What This Repo Does Not Do

- It does not write a submittable manuscript for you
- It does not build, calibrate, or run your simulation model — it tells you what reviewers expect of it
- It does not turn a single-factor field trial into a systems paper; the systems question must be real
- It does not freeze volatile metadata (current editors, fees, URLs, or rule wording) — live-check the official page before a real upload
- It does not decide whether your question is a genuine systems question — that is the researcher's call

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [Agricultural Systems (ScienceDirect)](https://www.sciencedirect.com/journal/agricultural-systems) — publisher home
- [Agricultural Systems — Guide for Authors](https://www.sciencedirect.com/journal/agricultural-systems/publish/guide-for-authors) — article types, abstract, declarations, data policy

---

## License

MIT
