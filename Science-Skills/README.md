# Science Skills

<p align="center">
  <img src="assets/cover.png" alt="Science (AAAS) cover card" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Science%20(AAAS)-b1141c)](https://www.science.org/journal/science)
[![Scope](https://img.shields.io/badge/scope-multidisciplinary-1f6feb)](https://www.science.org/journal/science)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **Science** (AAAS) — the flagship multidisciplinary research journal.

This pack is opinionated. It is **not** a generic "scientific writing" toolbox. It is a **Science-specific** stack that encodes the journal's editorial bar — **broad significance and general interest** — and the concrete conventions that follow from it: the standard vs extended Research Article budgets, the one-sentence summary and ≤125-word abstract, display-item budgets, statistics and reproducibility reporting, mandatory data/code/materials deposition, Science numbered-reference style, and a significance-forward cover letter.

---

## Why a Separate Science Skill Stack?

Science imposes constraints that differ materially from field journals — and from Nature:

| Constraint                | Science                                                       | Implication                                                  |
|---------------------------|--------------------------------------------------------------|-------------------------------------------------------------|
| Editorial bar             | Broad significance + general interest across disciplines      | Most papers are **desk-rejected without review** if specialist |
| Formats                   | Research Article ≤3,000 w, 3–5 items (extended online ≤6,000 w, ≤6) | Wrong format or over length signals inexperience             |
| One-sentence summary      | Required, ≤ ~125 characters, not the title                    | A missing/weak summary hurts at triage                       |
| Abstract                  | ≤ ~125 words, single paragraph, no subheadings, quantified    | Long structured abstracts are off-style                     |
| Methods location          | In **Supplementary Materials** for Research Articles          | Methods in the body bloats the main text                    |
| References                | Numbered, in order of appearance, **one continuous list (incl. SM)**, full author lists | Author–date / Nature style must be converted        |
| Data & code               | Deposited with accession/DOI; "on request" not acceptable     | No accession numbers = not submission-ready                 |
| Over-claiming             | A top rejection reason post-review                            | Conclusions must not outrun the evidence                    |

Generic "scientific writing" packs do not encode these venue constraints.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install science-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/awesome-journal-skills.git
cd awesome-journal-skills/Science-Skills

mkdir -p ~/.claude/skills && cp -R skills/sci-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/sci-* ~/.codex/skills/
```

### First Prompt

```
Use sci-workflow to tell me which skill I should use next for my manuscript targeted at Science.
```

---

## Default Workflow

```text
sci-fit            (clear the broad-significance bar first)
        ▼
sci-framing        (lock the advance + why-now)
        ▼
sci-writing        (standard vs extended Research Article; hold length)
        ▼
sci-figures        (display items within budget)
        ▼
sci-statistics     (rigor + reproducibility)
        ▼
sci-data           (data / code / materials availability)
        ▼
sci-abstract       (one-sentence summary + ≤125-word abstract — polish)
        ▼
sci-citation       (Science numbered style — polish)
        ▼
sci-cover-letter   (significance-forward editor pitch)
        ▼
sci-submission     (preflight)
        ▼
sci-rebuttal       (after review)
```

`sci-workflow` is the router — it tells you which skill to use next based on where you are.

---

## Skills

| Skill              | Purpose                                                                 |
|--------------------|-------------------------------------------------------------------------|
| `sci-workflow`     | Router — decides which sub-skill to invoke next                          |
| `sci-fit`          | Desk-reject filter: broad significance / general interest; venue routing |
| `sci-framing`      | Lock the one-sentence advance, the "why now", and a declarative title    |
| `sci-abstract`     | One-sentence summary (≤125 chars) + ≤125-word abstract                   |
| `sci-writing`      | Standard vs extended Research Article; length budgets; Methods → Supplementary |
| `sci-figures`      | Item budget, column sizing, ≥6 pt fonts, show-the-data, colorblind-safe   |
| `sci-statistics`   | Effect size + CI + n + test; replication; randomization; reproducibility  |
| `sci-data`         | Repository deposition, accession/DOI, availability statement, materials   |
| `sci-citation`     | Science numbered style, order of appearance, one continuous list          |
| `sci-cover-letter` | Significance-forward, editor-facing pitch                                 |
| `sci-submission`   | Full preflight checklist + templates                                      |
| `sci-rebuttal`     | Decision triage, experiment prioritization, point-by-point response       |

### Resources

- [`skills/sci-submission/templates/checklist.md`](skills/sci-submission/templates/checklist.md) — full preflight checklist
- [`skills/sci-submission/templates/cover_letter_template.md`](skills/sci-submission/templates/cover_letter_template.md) — significance-forward cover-letter scaffold
- [`resources/external_tools.md`](resources/external_tools.md) — deposition repositories, reporting standards, figure/stats tooling, and key Science author pages

---

## Differences vs. Nature / Science Advances / PNAS

| Dimension          | Science                          | Nature                            | Science Advances / PNAS            |
|--------------------|----------------------------------|-----------------------------------|------------------------------------|
| Bar                | Top-1% broad significance        | Top-1% broad significance         | Broad but more accepting           |
| Signature artifact | One-sentence summary             | Summary paragraph                 | PNAS: 120-word significance statement |
| References         | Numbered, order of appearance    | Different numbered convention     | Own styles                          |
| Methods            | Supplementary (Research Articles) | Methods section conventions       | Varies                              |
| When to switch     | —                                | Re-style before transfer          | If not top-1% general interest      |

For Nature, see the curated [nature-skills](https://github.com/Yuan1z0825/nature-skills). For PNAS, NEJM, Lancet, and Cell, see the sibling packs in [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills).

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — index of journal-specific skill packs
- [Cell-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/Cell-Skills) · [PNAS-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/PNAS-Skills) · [NEJM-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/NEJM-Skills) · [Lancet-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/Lancet-Skills)

---

## Disclaimer

This is an independent, community-built skill pack. It is **not** affiliated with, endorsed by, or produced by AAAS or *Science*. All targets (word counts, item limits, style rules) reflect publicly documented author guidelines at the time of writing — **always confirm against the current [Science Author Guidelines](https://www.science.org/content/page/science-information-authors)** before submitting.

---

## License

MIT
