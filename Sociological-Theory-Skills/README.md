# Sociological Theory (ST) Skills

<p align="center">
  <img src="assets/cover.svg" alt="Sociological Theory journal cover" width="200">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Sociological%20Theory-2a2a6a)](https://journals.sagepub.com/home/stx)
[![Index](https://img.shields.io/badge/index-ASA%20·%20SAGE-1f6feb)](https://www.asanet.org/publications/journals/sociological-theory-2/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **Sociological Theory (ST)** — the **American Sociological Association's (ASA) dedicated theory journal**, published by SAGE. ST publishes conceptual work that **advances sociological theory**: new substantive theories, history of theory, metatheory, formal theory construction, and synthetic contributions. It contains **no hypothesis tests, no estimation, and no results sections** — data, when present at all, is **illustrative**, never a test.

This repository is opinionated. It is **not** a generic sociology-writing toolbox and it is **not** an empirical-sociology stack. It is an **ST-specific, theory-construction** stack covering theoretical-problem framing, tradition positioning, concept and proposition construction, argument validity, boundary conditions, conceptual exhibits, ASA house style, Manuscript Central submission, and the double-anonymous review.

> Official basis checked 2026-06. Volatile specifics (editorial team, exact length/abstract limits, processing fee, ASA Style edition, portal URL) change; verify on the official ST / SAGE author page before submitting.

---

## Why a Separate ST Skill Stack?

ST imposes constraints that differ materially from empirical sociology journals (ASR / AJS):

| Constraint            | Sociological Theory                                            | Implication                                                  |
|-----------------------|---------------------------------------------------------------|--------------------------------------------------------------|
| Deliverable           | A **conceptual advance** (new theory / mechanism / typology / re-read tradition) | A study with a finding is off-fit; route it to ASR / AJS    |
| Data                  | **Illustrative only** — no samples, measures, estimation, results | There is no methods or results section                      |
| Core unit             | **Propositions** (theoretical claims), each earned by argument | Not hypotheses tested against a sample                       |
| Rigor standard        | **Logical soundness & internal consistency**                  | Logic plays the role statistics play at empirical journals   |
| Concepts              | Defined, bounded by extension, distinct from neighbors        | A relabeled concept is a desk-reject signal                  |
| Tradition             | Intervene in a live conversation (field theory, pragmatism, mechanisms, cultural, systems, relational) | Freestanding speculation fails                  |
| Boundary conditions   | Stated as part of the theory                                  | Treated as contribution, not as a disclaimer                 |
| Contribution          | Differentiated "before → after"; what theory can now *see*    | "Not differentiated from existing theory" is the top reject reason |
| Figures               | Conceptual: mechanism diagrams, typologies, process models    | No data plots — every box a concept, every arrow earned      |
| Length                | Max ~14,500 words **inclusive of footnotes, references, tables, figures, appendices** (verify) | References and footnotes are inside the cap     |
| Review                | Double-anonymous, multi-round (Manuscript Central)            | Multiple rounds are normal; the bar rises across rounds      |

Generic "scientific writing" or empirical-sociology skill packs do not address these constraints.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/sociological-theory-skills
/plugin install sociological-theory-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/sociological-theory-skills.git
cd sociological-theory-skills

mkdir -p ~/.claude/skills && cp -R skills/soctheory-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/soctheory-* ~/.codex/skills/
```

### First Prompt

```
Use soctheory-workflow to tell me which skill I should use next for my Sociological Theory manuscript.
```

---

## Default Workflow

```text
soctheory-topic-selection
        ▼
soctheory-literature-positioning
        ▼
soctheory-theory-construction
        ▼
soctheory-argument-development     (validity + rivals)
        ▼
soctheory-boundary-conditions      (scope / domain / non-claims)
        ▼
soctheory-conceptual-exhibits      (typology / mechanism diagram)
        ▼
soctheory-contribution-framing
        ▼
soctheory-writing-style            (polish)
        ▼
soctheory-submission
        ▼
soctheory-review-process
        ▼
soctheory-rebuttal
```

`soctheory-workflow` is the router — it tells you which skill to use next based on where you are.

---

## Skills

| Skill                            | Purpose                                                                 |
|----------------------------------|-------------------------------------------------------------------------|
| `soctheory-workflow`             | Router — decides which sub-skill to invoke next                          |
| `soctheory-topic-selection`      | Is there a real theoretical problem, and is it ST-fit (not empirical)?   |
| `soctheory-theory-construction`  | Build concepts, mechanisms, internally consistent propositions           |
| `soctheory-literature-positioning`| Pick the tradition; extend / challenge / reconstruct / synthesize       |
| `soctheory-argument-development`  | Argument validity — warrants, rival theories, counter-cases (no data)   |
| `soctheory-boundary-conditions`  | Scope, domain, and what the theory does NOT claim                        |
| `soctheory-conceptual-exhibits`  | Conceptual figures — typologies, mechanism diagrams (never data plots)   |
| `soctheory-writing-style`        | ASA house style; argument-driven prose; the inclusive length cap (polish)|
| `soctheory-contribution-framing` | Name the new way of seeing; state the "before → after"                   |
| `soctheory-review-process`       | Understand the double-anonymous, multi-round review and decision letters |
| `soctheory-submission`           | Manuscript Central preflight (format, masking, ASA style, fee, ethics)   |
| `soctheory-rebuttal`             | R&R response document that shows the theory was genuinely strengthened   |

### Resources

- [`skills/soctheory-submission/templates/checklist.md`](skills/soctheory-submission/templates/checklist.md) — 8-section pre-submission self-check (scope / format / masking / abstract / theory / figures / references / ethics & portal)
- [`resources/external_tools.md`](resources/external_tools.md) — Theory-building tools (citation mapping, reference managers, conceptual-diagram software, argument-logic aids)
- [`resources/official-source-map.md`](resources/official-source-map.md) — ST scope, submission mechanics, length/fee facts, and a "still unverified" list
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — web-verified ST theory papers, with a sibling-journal misattribution guard
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — a fictional ST-style theory introduction (before → after)

---

## Differences vs. Empirical-Sociology & Sibling Theory Venues

| Dimension          | Sociological Theory              | ASR / AJS (empirical)              | Theory and Society / EJST       |
|--------------------|----------------------------------|------------------------------------|---------------------------------|
| Deliverable        | Conceptual advance               | Theory **tested/demonstrated** with data | Theory (T&S: historical-comparative; EJST: continental) |
| Data               | Illustrative only                | Samples, measures, estimation      | T&S often historical evidence   |
| Core unit          | Propositions (argued)            | Hypotheses (tested)                | Essay / historical argument     |
| Rigor standard     | Logical soundness                | Statistical / empirical rigor      | Interpretive / historical       |
| Figures            | Conceptual models, typologies    | Data plots, results tables         | Mostly prose                    |

If your project has a finding to demonstrate in data, an empirical-sociology stack fits better — ST builds the theory those journals later examine. ST is also distinct from *Theory and Society*, the *European Journal of Social Theory*, and *Sociological Methodology*: it is the ASA's analytically pluralist flagship for theory proper.

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [Academy-of-Management-Review-Skills](https://github.com/brycewang-stanford/amr-skills) — AMR, a theory-only management journal

---

## License

MIT
