# Environmental Science & Technology Skills

<p align="center">
  <img src="assets/cover.svg" alt="Environmental Science & Technology cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-ES%26T-1b7a4b)](https://pubs.acs.org/journal/esthag)
[![Field](https://img.shields.io/badge/field-Environmental%20Science%20%26%20Engineering-1f6feb)](https://pubs.acs.org/page/esthag/about.html)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **Environmental Science & Technology (ES&T)** — the
flagship **environmental science and engineering** research journal of the **American Chemical Society
(ACS)**. ES&T aims to be **transformational and direction-setting**, publishing rigorous, robust work
for a multidisciplinary audience: environmental chemistry, environmental engineering, fate/transport/
transformation in natural and engineered systems, treatment and resource recovery, ecotoxicology and
environmental health, biogeochemical cycling, sustainability and energy, and the science–policy
interface.

This repository is opinionated. It is **not** a generic science-writing toolbox and it is **not** a
social-science pack repurposed for chemistry. It is an **ES&T-specific** stack built around the things
that actually decide an ES&T paper: a demonstrated claim of **environmental significance**, analytical
rigor with real **QA/QC**, closed **mass/energy balances**, a mandatory **TOC/abstract graphic**, a
**Supporting Information** file submitted alongside the manuscript, and a **data-availability**
statement backed by deposition in public databases.

---

## What Is ES&T, and Why a Dedicated Stack?

ES&T's constraints differ from a pure-chemistry journal or a general-science venue:

| Constraint            | ES&T                                                                          | Implication                                                       |
|-----------------------|-------------------------------------------------------------------------------|------------------------------------------------------------------|
| Premium on            | **Environmental significance** + direction-setting novelty                    | A clean lab result with no environmental relevance is off-fit    |
| Scope                 | Environmental **chemistry + engineering + tox/health + biogeochem + policy**  | The paper must reach a multidisciplinary audience                |
| Rigor                 | **QA/QC**, honest uncertainty, **closed mass balances**                       | Blanks, recoveries, LOD/LOQ, replicates are expected             |
| Publisher             | **American Chemical Society (ACS)**                                            | Submitted via the **ACS Publishing Center** / **ACS Paragon Plus** |
| Exhibits              | **Mandatory TOC/abstract graphic**; figures/tables may count as words         | Build the visual abstract; budget exhibit word-equivalents       |
| Transparency          | **Data-availability statement** + public-database deposition; **SI** alongside | Build the SI and data deposit as you go                          |
| Review                | Editor desk-screen (declines a large fraction), then ~3 expert reviewers      | Clear the editorial bar on significance before review            |
| Style                 | **ACS** numbered-citation style; SI units                                     | Not a generic author-date style                                  |
| Companion             | **ES&T Letters** for urgent, high-impact short results                        | Match urgency to venue                                           |

Volatile specifics (exact word limits and word-equivalents, submission-system name, blinding model,
current editor, metrics, any APC) change — items not directly confirmed are marked **待核实** in
[`resources/official-source-map.md`](resources/official-source-map.md).
**Verify on the official journal page.**

### Article types (word limits 待核实)

- **Research Article** — full original study (~7,000 words); requires a TOC graphic.
- **Critical Review** — comprehensive analytical synthesis (~10,000 words).
- **Feature** — accessible, magazine-style piece for the broad community (~5,000 words).
- **Perspective** — focused, forward-looking opinion/synthesis (~4,000 words).
- **Policy Analysis** — science/engineering at the **policy interface** (~7,000 words).
- **Viewpoint / Correspondence / Letter to the Editor** — short opinion / comment formats.
- **ES&T Letters** — the companion journal for the rapid disclosure of **urgent** results (Letter ≤3,000 words).

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/est-skills
/plugin install est-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/est-skills.git
cd est-skills

mkdir -p ~/.claude/skills && cp -R skills/est-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/est-* ~/.codex/skills/
```

### First Prompt

```
Use est-workflow to tell me which skill I should use next for my ES&T manuscript.
```

---

## Default Workflow

```text
est-topic-selection
        ▼
est-literature-positioning
        ▼
est-study-design
        ▼
est-data-analysis
        ▼
est-figures-and-tables
        ▼
est-reporting-and-reproducibility
        ▼
est-writing-style           (polish)
        ▼
est-cover-letter
        ▼
est-review-process
        ▼
est-submission
        ▼
est-revision-and-rebuttal
```

`est-workflow` is the router — it tells you which skill to use next based on where you are. If your
result is **urgent and high-impact** but short, route to `est-workflow` early to consider the
**ES&T Letters** companion journal instead of a full Research Article.

---

## Skills

| Skill                                | Purpose                                                                       |
|--------------------------------------|-------------------------------------------------------------------------------|
| `est-workflow`                       | Router — decides which sub-skill to invoke next; picks the article type       |
| `est-topic-selection`                | The environmental-significance test; fit and article-type choice              |
| `est-literature-positioning`         | State the knowledge gap; engage chemistry/engineering/tox/policy literatures  |
| `est-study-design`                   | Environmental relevance, controls, replication, mass balance, QA/QC by design |
| `est-data-analysis`                  | QA/QC reporting, censored-data stats, uncertainty, closed mass balances       |
| `est-figures-and-tables`             | Self-contained exhibits + the mandatory TOC/abstract graphic                  |
| `est-reporting-and-reproducibility`  | Supporting Information, data-availability statement, public-database deposit  |
| `est-writing-style`                  | ACS style; significance up front; fit the article-type word limit             |
| `est-cover-letter`                   | Editor pitch — significance, fit, ≥4 non-conflicted suggested reviewers       |
| `est-review-process`                 | Editor desk-screen, ~3 expert reviewers, decision flow, integrity checks      |
| `est-submission`                     | ACS Publishing Center preflight (type, TOC graphic, SI, data statement, ACS)  |
| `est-revision-and-rebuttal`          | Response-letter strategy for multiple reviewers + editor                      |

### Resources

- [`resources/external_tools.md`](resources/external_tools.md) — environmental data sources (EPA / PubChem / NIST / MassBank / GenBank), instruments and QA/QC, fate-transport models, and R / Python / reproducibility tooling
- [`resources/official-source-map.md`](resources/official-source-map.md) — official ACS / ES&T URLs behind every fact, with 待核实 markers on unverified items

---

## What This Repo Does Not Do

- It does not write a submittable manuscript for you
- It does not simulate any specific editor's or reviewer's taste
- It does not assert volatile metadata (exact word limits/word-equivalents, submission-system name, blinding model, editor, metrics, APC) — verify on the official page; unverified items are marked 待核实
- It does not decide whether your work has environmental significance — that is the researcher's call

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [Environmental Science & Technology (ACS Publications)](https://pubs.acs.org/journal/esthag) — journal home
- [ES&T Author Guidelines (ACS Researcher Resources)](https://researcher-resources.acs.org/publish/author_guidelines?coden=esthag) — article types, limits, policies

---

## License

MIT
