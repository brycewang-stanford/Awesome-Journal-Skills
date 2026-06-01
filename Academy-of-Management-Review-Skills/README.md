# Academy of Management Review (AMR) Skills

<p align="center">
  <img src="assets/cover.svg" alt="Academy of Management Review journal cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Academy%20of%20Management%20Review-14635a)](https://aom.org/research/journals/review)
[![Index](https://img.shields.io/badge/index-Academy%20of%20Management-1f6feb)](https://aom.org/research/journals/review)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at the **Academy of Management Review (AMR)** — the Academy of Management's premier **theory** journal. AMR publishes conceptual articles that **build new theory**; it contains **no datasets, no hypothesis tests, and no results sections**.

This repository is opinionated. It is **not** a generic management-writing toolbox and it is **not** an empirical-management stack. It is an **AMR-specific, theory-building** stack covering theoretical-puzzle framing, conversation positioning, construct and proposition development, argument-logic stress-testing, contribution differentiation, conceptual figures, AOM house style, ScholarOne submission, and the developmental multi-round review.

---

## Why a Separate AMR Skill Stack?

AMR imposes constraints that differ materially from empirical management journals (AMJ / ASQ / SMJ):

| Constraint                | Academy of Management Review                                  | Implication                                                  |
|---------------------------|----------------------------------------------------------------|--------------------------------------------------------------|
| Deliverable               | New **theory** (constructs / process model / reconceptualization) | A study with data is off-fit; route it to AMJ / ASQ / SMJ    |
| Data                      | **None** — no samples, measures, estimation, or results        | There is no methods or results section at all                |
| Core unit                 | **Propositions** (theoretical claims), each earned by argument | Not hypotheses tested against a sample                       |
| Hallmark                  | "Challenge **and** extend" an existing theoretical conversation | Pure critique or pure summary both fail                      |
| Rigor standard            | **Logical soundness** of the argument                          | Logic plays the role statistics play at empirical journals   |
| Constructs                | Defined, domain-bounded, distinct from neighbors               | A relabeled construct is a desk-reject signal                |
| Boundary conditions       | Stated as part of the theory                                   | Treated as contribution, not as a disclaimer                 |
| Contribution              | Differentiated "before → after"; what scholars can now explain | "Not differentiated from prior work" is the top reject reason |
| Figures                   | Conceptual: process models, typologies, multi-level frameworks | No data plots — every box a construct, every arrow earned    |
| Review                    | Double-anonymous, **developmental**, multi-round (ScholarOne)  | Multiple rounds are normal; the bar rises across rounds      |

Generic "scientific writing" or empirical-management skill packs do not address these constraints.

> Accuracy note: AMR's editorial team and exact length / abstract limits change over time. AOM currently says it does not charge submission fees, but you should still verify all portal-stage specifics on the official AMR / Academy of Management author page before submitting.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/amr-skills
/plugin install amr-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/amr-skills.git
cd amr-skills

mkdir -p ~/.claude/skills && cp -R skills/amr-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/amr-* ~/.codex/skills/
```

### First Prompt

```
Use amr-workflow to tell me which skill I should use next for my Academy of Management Review manuscript.
```

---

## Default Workflow

```text
amr-topic-selection
        ▼
amr-literature-positioning
        ▼
amr-theory-development
        ▼
amr-methods                (theory-construction craft)
        ▼
amr-data-analysis          (argument-logic stress test)
        ▼
amr-contribution-framing
        ▼
amr-tables-figures         (conceptual model / propositions table)
        ▼
amr-writing-style          (polish)
        ▼
amr-submission
        ▼
amr-review-process
        ▼
amr-rebuttal
```

`amr-workflow` is the router — it tells you which skill to use next based on where you are.

---

## Skills

| Skill                       | Purpose                                                                 |
|-----------------------------|-------------------------------------------------------------------------|
| `amr-workflow`              | Router — decides which sub-skill to invoke next                         |
| `amr-topic-selection`       | Is there a real theoretical puzzle, and is it AMR-fit (not empirical)?  |
| `amr-theory-development`    | Build constructs, relationships, propositions, and boundary conditions  |
| `amr-literature-positioning`| Pick the conversation; "challenge and extend" it (no review-essays)     |
| `amr-methods`               | Theory-CONSTRUCTION craft — construct domains, mechanisms (no data)     |
| `amr-data-analysis`         | ARGUMENT development — logic checks, counterfactuals, rivals (no data)  |
| `amr-contribution-framing`  | Differentiate the new theory; state the "before → after"                |
| `amr-tables-figures`        | Conceptual figures — process models, typologies, propositions tables    |
| `amr-writing-style`         | AOM house style; argument-driven prose (polish)                         |
| `amr-submission`            | ScholarOne preflight + manuscript template (format, anonymization, ethics) |
| `amr-review-process`        | Understand the developmental, multi-round review and decision letters   |
| `amr-rebuttal`              | R&R response document that shows the theory was genuinely strengthened  |

### Resources

- [`skills/amr-submission/templates/manuscript_template.md`](skills/amr-submission/templates/manuscript_template.md) — AMR conceptual-article skeleton (puzzle intro, theory development, propositions, conceptual model, discussion)
- [`skills/amr-submission/templates/checklist.md`](skills/amr-submission/templates/checklist.md) — 8-section pre-submission self-check (scope / format / anonymization / abstract / theory / figures / references / ethics & portal)
- [`resources/external_tools.md`](resources/external_tools.md) — Theory-building tools (citation mapping, reference managers, conceptual-diagram software, argument-logic aids)

---

## Differences vs. Empirical-Management Skill Stacks (AMJ / ASQ / SMJ)

| Dimension          | Academy of Management Review     | AMJ / ASQ / SMJ (empirical)        |
|--------------------|----------------------------------|------------------------------------|
| Deliverable        | New theory                       | Theory **tested** with data        |
| Data               | None                             | Samples, measures, estimation      |
| Core unit          | Propositions (argued)            | Hypotheses (tested)                |
| Rigor standard     | Logical soundness                | Statistical / empirical rigor      |
| Figures            | Conceptual models, typologies    | Data plots, results tables         |
| Methods section    | None (theory-construction craft) | Required (research design)         |

If your project has data, an empirical-management stack fits better — AMR builds the theory those journals later test.

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [Economic-Research-Journal-Skills](https://github.com/brycewang-stanford/economic-research-skills) — 《经济研究》

---

## License

MIT
