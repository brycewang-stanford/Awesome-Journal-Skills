# Molecular Cell Skills

<p align="center">
  <img src="assets/cover.svg" alt="Molecular Cell (Cell Press) cover card" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Molecular%20Cell%20(Cell%20Press)-6a1b2a)](https://www.cell.com/molecular-cell/home)
[![Scope](https://img.shields.io/badge/scope-mechanistic%20molecular%20biology-1f6feb)](https://www.cell.com/molecular-cell/home)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **Molecular Cell** (Mol. Cell, Cell Press) — the flagship journal for mechanistic molecular biology.

This pack is opinionated. It is **not** a generic "scientific writing" toolbox. It is a **Molecular Cell-specific** stack that encodes the journal's editorial bar — **a deep molecular mechanism, proven by multiple orthogonal approaches, with physiological relevance** — and the concrete conventions that follow: the single-mechanism Article within a ~7,000-word / ~7-display-item budget (or the ~4,000-word Short Article), **STAR Methods** with the **Key Resources Table** and **Resource Availability**, data/structure/code deposition (GEO/PDB/EMDB/PRIDE), the signature Cell Press **Highlights / eTOC blurb / Graphical Abstract** trio, the Summary, and — distinctively — the current Cell Press **numbered superscript reference style**.

---

## Why a Separate Molecular Cell Skill Stack?

Molecular Cell rewards a different thing than *Cell* or a broad field journal — **mechanistic depth over breadth** — and its conventions follow:

| Constraint                | Molecular Cell                                               | Implication                                                  |
|---------------------------|-------------------------------------------------------------|-------------------------------------------------------------|
| Editorial bar             | A **deep molecular mechanism** with orthogonal validation   | Descriptive / correlative or single-technique papers are **pre-review rejected** |
| Depth vs. breadth         | Mechanism to the residue/base/step, physiologically anchored | Broad-but-shallow stories belong at *Cell*; deep-but-narrow at Mol. Cell |
| Article structure         | Summary · Intro · Results · Discussion · **STAR Methods**    | A free-text Methods section is off-style                    |
| Length budget             | Article ~**7,000 words** / ~**7** display items; Short Article ~**4,000** | Comprehensiveness is not rewarded — tighten to the mechanism |
| Methods                   | **STAR Methods** + Key Resources Table + Resource Availability | Every antibody, plasmid, oligo, and purified protein needs source + identifier |
| Data & structures         | Deposited with accession/DOI; structures with maps/structure factors | "On request" is not acceptable for primary data           |
| References                | **Cell Press numbered** (superscript, order of appearance), full author lists | Author–date manuscripts must be **renumbered**            |
| Signature artifacts       | **Highlights**, **eTOC blurb**, **Graphical Abstract**      | Missing/weak artifacts hurt at every editorial stage        |
| Over-interpretation       | A top rejection reason; reviewers demand the mechanism be airtight | Conclusions (and structures) must not outrun the evidence |

Generic "scientific writing" packs do not encode these venue constraints.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install molcell-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/awesome-journal-skills.git
cd awesome-journal-skills/Molecular-Cell-Skills

mkdir -p ~/.claude/skills && cp -R skills/molcell-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/molcell-* ~/.codex/skills/
```

### First Prompt

```
Use molcell-workflow to tell me which skill I should use next for my manuscript targeted at Molecular Cell.
```

---

## Default Workflow

```text
molcell-fit            (clear the deep-mechanism + orthogonal-validation bar first)
        ▼
molcell-framing        (lock the single-mechanism arc: question → mechanism → physiological consequence)
        ▼
molcell-writing        (Article structure; ~7,000-word budget; STAR Methods, not free-text)
        ▼
molcell-figures        (display items within ~7; show the data; blot/structure/genomics integrity)
        ▼
molcell-star-methods   (Key Resources Table + Resource Availability + QSA)
        ▼
molcell-data           (GEO/PDB/EMDB/PRIDE deposition + availability statement)
        ▼
molcell-summary        (~150-word Summary — polish)
        ▼
molcell-highlights     (Highlights + eTOC blurb + Graphical Abstract — polish)
        ▼
molcell-citation       (Cell Press numbered references — polish)
        ▼
molcell-submission     (cover letter + preflight)
        ▼
molcell-rebuttal       (after review)
```

`molcell-workflow` is the router — it tells you which skill to use next based on where you are.

---

## Skills

| Skill                  | Purpose                                                                   |
|------------------------|---------------------------------------------------------------------------|
| `molcell-workflow`     | Router — decides which sub-skill to invoke next                            |
| `molcell-fit`          | Pre-review filter: deep mechanism + orthogonal validation; Cell Press venue routing |
| `molcell-framing`      | Lock the single-mechanism arc and a declarative title                     |
| `molcell-writing`      | Article structure; ~7,000-word / ~7-item budget; STAR Methods location    |
| `molcell-figures`      | Column sizing (85/114/174 mm), show-the-data, blot/structure/genomics integrity |
| `molcell-star-methods` | Key Resources Table + Resource Availability (3 subsections) + QSA          |
| `molcell-data`         | Deposition (GEO/PDB/EMDB/PRIDE/Mendeley Data), accessions, availability statement |
| `molcell-summary`      | ~150-word unstructured Summary, molecular mechanism named, quantified     |
| `molcell-highlights`   | Highlights (≤85 chars), eTOC blurb (~50 words), Graphical Abstract         |
| `molcell-citation`     | Cell Press **numbered** superscript references, order of appearance, full author lists |
| `molcell-submission`   | Full preflight checklist + manuscript/cover-letter templates              |
| `molcell-rebuttal`     | Decision triage, experiment prioritization, point-by-point response       |

### Resources

- [`skills/molcell-submission/templates/checklist.md`](skills/molcell-submission/templates/checklist.md) — full preflight checklist
- [`skills/molcell-submission/templates/manuscript_template.md`](skills/molcell-submission/templates/manuscript_template.md) — Molecular Cell manuscript skeleton (STAR Methods, KRT, eTOC blurb, Highlights, cover-letter scaffold)
- [`resources/external_tools.md`](resources/external_tools.md) — deposition repositories, STAR Methods/RRID standards, the molecular-biology stack, and Cell Press author pages
- [`resources/official-source-map.md`](resources/official-source-map.md) — official URLs + verified journal facts (checked 2026-07-16)
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — method × topic positioning with a sibling-confusion guard
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — annotated Summary + mechanistic opening

---

## Differences vs. Cell / Nature / Cell Press siblings

| Dimension          | Molecular Cell                        | Cell                              | Nature / Science                    |
|--------------------|---------------------------------------|-----------------------------------|-------------------------------------|
| Bar                | **Deep molecular mechanism** + orthogonal validation | Complete, broad, mechanistic story | Top-1% broad significance          |
| Depth vs. breadth  | Depth first; defined domain           | Breadth + depth                   | Breadth first                       |
| Abstract           | **Summary**, ~150 w, unstructured     | Summary, ≤150 w                   | Science ≤125 w + one-sentence summary |
| Methods            | **STAR Methods** + KRT                | STAR Methods + KRT                | Methods section / Supplementary     |
| References         | **Cell Press numbered** (superscript) | Cell Press numbered               | Science: numbered by appearance     |
| When to switch     | —                                     | Broad cross-field complete story  | If you want the widest audience     |

> Note: Molecular Cell (like other Cell Press journals) now uses a **numbered** superscript reference style. See the sibling [Cell-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/Cell-Skills) pack for the flagship, and [Cancer-Cell-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/Cancer-Cell-Skills) for molecular oncology.

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — index of journal-specific skill packs
- [Cell-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/Cell-Skills) · [Science-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/Science-Skills) · [PNAS-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/PNAS-Skills)

---

## Disclaimer

This is an independent, community-built skill pack. It is **not** affiliated with, endorsed by, or produced by Cell Press, Elsevier, or *Molecular Cell*. All targets (word counts, character limits, item limits, style rules) reflect publicly documented author guidelines at the time of writing — **always confirm against the current [Molecular Cell information for authors](https://www.cell.com/molecular-cell/information-for-authors) and [STAR Methods guidelines](https://www.cell.com/star-methods)** before submitting.

---

## License

MIT
