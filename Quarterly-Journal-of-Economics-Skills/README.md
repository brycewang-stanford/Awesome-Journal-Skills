# Quarterly Journal of Economics Skills

<p align="center">
  <img src="assets/cover.svg" alt="Quarterly Journal of Economics cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-QJE-7c1c2c)](https://academic.oup.com/qje)
[![Index](https://img.shields.io/badge/index-Top--5%20Economics-1f6feb)](https://academic.oup.com/qje)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at the **Quarterly Journal of Economics (QJE)** — the oldest English-language economics journal (since 1886), published by Oxford University Press, edited historically out of Harvard, and one of the discipline's **top-5** general-interest journals.

This repository is opinionated. It is **not** a generic economics-writing toolbox. It is a **QJE-specific** stack: a big conceptual idea backed by clean, credible empirics — especially empirical microeconomics (labor, public, development, behavioral, economic history, political economy) — with credible causal identification, an extensive online appendix, figure-forward exhibits, a reproducible replication package, and few-round R&R discipline.

---

## Why a Separate QJE Skill Stack?

QJE imposes constraints that differ materially from a methods journal (Econometrica) or a top field journal:

| Constraint              | QJE                                                              | Implication                                                  |
|-------------------------|------------------------------------------------------------------|--------------------------------------------------------------|
| Audience                | General-interest, all of economics                               | A specialist-only question is off-fit                        |
| Premium on              | A **big idea** + clean, credible empirics                        | Technique-first papers belong at Econometrica                |
| Hallmark                | Compelling question + credible identification + broad lesson     | A reduced-form coefficient with no lesson reads as a WP       |
| Identification bar      | RCT / staggered DID (modern estimators) / IV / RDD, well defended | OLS + controls is fast-desk-rejected                         |
| Theory                  | A conceptual frame matched to the question (often light)         | Gratuitous structural models are penalized                   |
| Robustness / appendix   | **Very extensive** online appendix expected                      | A thin appendix reads as an unfinished paper                 |
| Presentation            | Increasingly **figure-forward**                                  | The headline should often be one clean graph                 |
| References              | Author-date                                                      | Numbered/footnote styles read as off-template                |
| Process                 | Editorial Express; no submission fee; replication required       | Fast desk reject; few rounds with demanding referees          |
| Over-claiming           | Punished                                                         | Claims must not exceed what the design supports              |

Generic "scientific writing" or "econ writing" skill packs do not address these constraints. Volatile specifics (current editors, exact fee, deposit policy) change — **verify them on the official journal page**.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install qje-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/awesome-journal-skills.git
cd awesome-journal-skills/Quarterly-Journal-of-Economics-Skills

mkdir -p ~/.claude/skills && cp -R skills/qje-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/qje-* ~/.codex/skills/
```

### First Prompt

```
Use qje-workflow to tell me which skill I should use next for my QJE manuscript.
```

---

## Default Workflow

```text
qje-topic-selection
        ▼
qje-literature-positioning
        ▼
qje-identification
        ▼
qje-theory-model
        ▼
qje-robustness
        ▼
qje-tables-figures
        ▼
qje-writing-style        (polish)
        ▼
qje-replication-package
        ▼
qje-referee-strategy
        ▼
qje-submission
        ▼
qje-rebuttal
```

`qje-workflow` is the router — it tells you which skill to use next based on where you are.

---

## Skills

| Skill                        | Purpose                                                                 |
|------------------------------|-------------------------------------------------------------------------|
| `qje-workflow`               | Router — decides which sub-skill to invoke next                         |
| `qje-topic-selection`        | Big-question fit + the "broad lesson" bar                               |
| `qje-literature-positioning` | Stake the contribution against the frontier (no standalone survey)      |
| `qje-identification`         | Credible causal design (RCT / staggered DID / IV / RDD)                 |
| `qje-theory-model`           | A conceptual frame matched to the question                              |
| `qje-robustness`             | The extensive online appendix top-5 referees expect                     |
| `qje-tables-figures`         | Figure-forward exhibits, self-contained notes                           |
| `qje-writing-style`          | Make the big idea land for a general-interest reader                    |
| `qje-replication-package`    | Reproducible data + code deposit for accepted papers                    |
| `qje-referee-strategy`       | War-game referee objections before submitting                           |
| `qje-submission`             | Editorial Express preflight + manuscript template                       |
| `qje-rebuttal`               | Few-round R&R response-letter strategy                                  |

### Resources

- [`skills/qje-submission/templates/manuscript_template.md`](skills/qje-submission/templates/manuscript_template.md) — QJE manuscript skeleton (abstract, intro arc, design, exhibits, author-date references)
- [`skills/qje-submission/templates/checklist.md`](skills/qje-submission/templates/checklist.md) — 8-section pre-submission self-check
- [`resources/external_tools.md`](resources/external_tools.md) — data sources (IPUMS / Census FSRDC / Opportunity Insights / DHS) + Stata / R / Python packages for credible-design empirical micro

---

## Differences vs. Other Top-5 Stacks

| Dimension          | QJE                                  | Econometrica                  | JPE                                  |
|--------------------|--------------------------------------|-------------------------------|--------------------------------------|
| Lead with          | A big empirical-micro question       | A method / theorem            | A question (often model-led)         |
| Identification     | Natural experiment, figure-forward   | Estimator properties          | Identification + quantitative model  |
| Theory weight      | Often light, matched to question     | Central                       | Frequently heavy / structural        |
| House style        | Author-date, extensive appendix      | Theorem-proof rigor           | Author-date, varied                  |

---

## What This Repo Does Not Do

- It does not write a submittable manuscript for you
- It does not simulate any specific editor's or referee's taste
- It does not assert volatile metadata (current editors, exact fee, exact deposit rules) — verify on the official page
- It does not judge whether your "big idea" is genuinely original — that is the researcher's call

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [Economic-Research-Journal-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/Economic-Research-Journal-Skills) — 《经济研究》
- [Quarterly Journal of Economics (official)](https://academic.oup.com/qje) — Oxford University Press

---

## License

MIT
