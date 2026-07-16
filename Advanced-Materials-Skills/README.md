# Advanced Materials Skills

<p align="center">
  <img src="assets/cover.svg" alt="Advanced Materials journal cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Advanced%20Materials-4a2c6b)](https://advanced.onlinelibrary.wiley.com/journal/15214095)
[![Index](https://img.shields.io/badge/publisher-Wiley--VCH-1f6feb)](https://www.wiley.com/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **Advanced Materials (Adv. Mater.)** — Wiley-VCH's flagship, very-high-impact materials-science journal, publishing weekly across **all** of materials science: materials chemistry, nanotechnology, energy materials (batteries, photovoltaics, catalysis), electronics and optoelectronics, and biomaterials.

This repository is opinionated. It is **not** a generic materials-writing toolbox. It is an **Adv. Mater.-specific** stack built around the journal's defining bar: a genuine **materials-science advance** — a new material, mechanism, or property, not incremental optimization — that is **rigorously characterized by multiple complementary techniques**, ideally carried through to a **device-level demonstration benchmarked against the state of the art**, and communicated with **cover-quality figures**.

---

## Why a Separate Adv. Mater. Skill Stack?

Advanced Materials imposes bars that differ materially from its excellent sibling journals in the Wiley "Advanced" portfolio (Advanced Functional Materials, Advanced Science, Small, Advanced Materials Interfaces):

| Constraint            | Advanced Materials                                              | Implication                                                          |
|-----------------------|----------------------------------------------------------------|----------------------------------------------------------------------|
| The gate              | Genuine advance **AND** broad impact (both required)           | Incremental optimization is rejected on impact grounds even if flawless |
| Audience              | All of materials science, not just your subfield               | The opening/abstract must read out-of-subfield                        |
| Characterization      | Multi-technique triangulation of structure→property claims     | A single XRD or one TEM image is not enough                           |
| Benchmarking          | Fair comparison to the best reported systems, in the paper     | A record number with no benchmark reads as unsupported                |
| Format                | Communication (~4 typeset pages) vs. Research Article (~10)    | Length is counted in typeset pages; figures count with text          |
| Communication abstract| The **opening paragraph serves as the abstract**              | The first paragraph must stand alone and sell the advance            |
| Figures               | Cover-quality, plus a required Table-of-Contents graphic       | Fig. 1 must convey the advance at a glance; the TOC graphic sells it  |
| Cover letter          | Must justify the advance + broad impact to the editor          | Omitting the broad-impact leg is the most common miss                 |
| Process               | Wiley editors + referees; selective, desk-triaged on impact    | May decline a correct paper on novelty/impact; transfer routes exist |

Generic "scientific writing" packs do not address the advance-vs-optimization gate, multi-technique triangulation, benchmarking discipline, or the Communication-vs-Article format.

> Volatile specifics (current article-type page limits, figure DPI/format, TOC-graphic spec, submission portal, APC, required declarations) change — always verify on the official Wiley Advanced Materials author page.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/advmat-skills
/plugin install advmat-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/advmat-skills.git
cd advmat-skills

mkdir -p ~/.claude/skills && cp -R skills/advmat-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/advmat-* ~/.codex/skills/
```

### First Prompt

```
Use advmat-workflow to tell me which skill I should use next for my Advanced Materials manuscript.
```

---

## Default Workflow

```text
advmat-scope-fit
        ▼
advmat-results-framing
        ▼
advmat-methods
        ▼
advmat-figures
        ▼
advmat-supplementary
        ▼
advmat-writing-style       (polish)
        ▼
advmat-length-management   (fit the article-type format)
        ▼
advmat-cover-letter
        ▼
advmat-submission
        ▼
advmat-referee-strategy
        ▼
advmat-revision
```

`advmat-workflow` is the router — it tells you which skill to use next based on where you are.

---

## Skills

| Skill                     | Purpose                                                                     |
|---------------------------|-----------------------------------------------------------------------------|
| `advmat-workflow`         | Router — decides which sub-skill to invoke next                             |
| `advmat-scope-fit`        | The advance + broad-impact gate; Adv. Mater. vs. AFM / Adv. Sci. / Small / AMI |
| `advmat-results-framing`  | One-advance narrative, structure→property→function chain, Communication opening-as-abstract |
| `advmat-methods`          | Multi-technique characterization, benchmarking, reproducibility; body vs. Experimental Section vs. SI |
| `advmat-figures`          | Cover-quality lead figure, multi-panel characterization figures, the TOC graphic |
| `advmat-supplementary`    | Partition extended data / full experimental detail to the SI; keep the paper stand-alone |
| `advmat-writing-style`    | Wiley house style, de-hyping, precise nomenclature/units, out-of-subfield readability |
| `advmat-length-management`| Fit the Communication (~4 pp) or Research Article (~10 pp) format; display items count with text |
| `advmat-cover-letter`     | Justify the advance + broad impact to the editor                            |
| `advmat-submission`       | Pre-submission preflight + Adv. Mater. template (article type, files, TOC, ORCID) |
| `advmat-referee-strategy` | Suggested / opposed referees; pre-empt characterization and benchmarking objections |
| `advmat-revision`         | Reviewer-report response, resubmission, and the Wiley transfer route         |

### Resources

- [`skills/advmat-submission/templates/manuscript_template.md`](skills/advmat-submission/templates/manuscript_template.md) — Adv. Mater. skeleton (title, abstract/opening, body, Experimental Section, figure/TOC budgeting, SI outline, cover letter)
- [`skills/advmat-submission/templates/checklist.md`](skills/advmat-submission/templates/checklist.md) — 10-section pre-submission self-check
- [`resources/external_tools.md`](resources/external_tools.md) — characterization-analysis software, the DFT/simulation stack (VASP, Quantum ESPRESSO, Materials Project, pymatgen), figure tools, and data repositories
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — web-verified landmark *Adv. Mater.* papers (MXenes, superhydrophobic surfaces, e-skin, carbon aerogels, AIE, ...) plus a venue-trap guardrail, for design positioning
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — annotated before→after of a Communication opening paragraph
- [`resources/official-source-map.md`](resources/official-source-map.md) — the official Wiley URLs behind the pack's facts, with a Checked date

---

## Differences vs. Sibling Advanced-Portfolio Journals

| Dimension          | Advanced Materials                    | Adv. Funct. Mater. / Adv. Sci. / Small / AMI |
|--------------------|---------------------------------------|-----------------------------------------------|
| The gate           | Genuine advance **+ broad impact**    | Rigor + a well-defined (often specialist) audience |
| Audience           | All of materials science              | The specific subfield / functional area       |
| Incremental result | Rejected on impact grounds            | Appropriate and welcome                        |
| Benchmarking       | Fair comparison to SOTA, in the paper | Expected, scaled to the venue                  |
| Format             | Communication or Research Article     | Article-type conventions per journal           |

If your result is solid but incremental or narrowly functional, `advmat-scope-fit` will recommend retargeting to a sibling journal rather than fighting the impact gate.

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [Advanced Materials](https://advanced.onlinelibrary.wiley.com/journal/15214095) — Official Wiley journal page
- [Wiley-VCH](https://www.wiley.com/) — Publisher

---

## License

MIT
