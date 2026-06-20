# Global Environmental Change Skills

<p align="center">
  <img src="assets/cover.svg" alt="Global Environmental Change cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-GEC-0f6f8c)](https://www.sciencedirect.com/journal/global-environmental-change)
[![Field](https://img.shields.io/badge/field-Human%20Dimensions-1f6feb)](https://www.sciencedirect.com/journal/global-environmental-change)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **Global Environmental Change (GEC)** — the leading
international journal on the **human and policy dimensions** of global environmental change, founded in
**1990** and published by **Elsevier** (ISSN 0959-3780). GEC publishes theoretically and empirically
rigorous work on the **social drivers and consequences** of environmental change and on the
**governance, policy, and behavioral processes** that address it: climate adaptation, vulnerability,
environmental governance, socio-ecological systems, sustainability transitions, food and water systems,
land use, oceans and coasts, and urban change — quantitative, qualitative, and mixed-methods alike.

This repository is opinionated. It is **not** a generic social-science writing toolbox and it is **not**
a natural-science pack with a policy sentence bolted on. It is a **GEC-specific** stack: a question with
a **significant social-science component**, a **clear conceptual framework**, **interdisciplinary rigor**
defended on each method's own terms, **real-world and policy implications** grounded in the evidence, and
a transparent, reproducible record prepared with a **Data Availability Statement**.

---

## What Is GEC, and Why a Dedicated Stack?

GEC's constraints differ from a disciplinary social-science journal or a natural-science venue:

| Constraint            | GEC                                                                            | Implication                                                       |
|-----------------------|--------------------------------------------------------------------------------|-------------------------------------------------------------------|
| Scope                 | **Human and policy dimensions** of global environmental change                 | A biophysical result alone is off-fit                             |
| Premium on            | A **significant social-science component** + societal/policy significance      | Lead with the human dimension, not a hazard trend                 |
| Methods               | Quantitative, qualitative, mixed — judged on their own terms                   | Match method to question; state mixed-methods integration         |
| Publisher             | **Elsevier** (ISSN 0959-3780 / 1872-9495)                                      | Submitted through Elsevier's online submission system             |
| Review model          | **Double-anonymized**; typically at least two expert reviewers                 | Separate title page from an anonymized manuscript                 |
| Length                | Research Articles **up to 8,000 words**; Perspectives **up to 3,000 words**; **abstract ≤250** | Cut method minutiae to supplementary material                     |
| Highlights            | Required: **3-5 bullets, ≤85 characters each**, separate editable file         | Draft them as a shop window for the contribution                  |
| Framework             | Theoretically rigorous; the framework must **do work**                         | No atheoretical, purely descriptive papers                        |
| Transparency          | Elsevier **Option C** research-data policy; **Data Availability Statement**     | Deposit/cite/link data, or explain why sharing is impossible      |
| Significance          | Multi-scale: local processes with **global / cross-scale consequences**        | Connect your case to scales beyond the local                      |

The official ScienceDirect pages were refreshed on **2026-06-20** in
[`resources/official-source-map.md`](resources/official-source-map.md). Re-check live pages before
submission-ready advice because APCs, editors, special calls, and policy wording can change.

### What GEC looks for

- **A human/policy contribution** — the social drivers, consequences, or governance of environmental change.
- **A conceptual framework that does work** — generating the question and structuring the analysis.
- **Interdisciplinary rigor** — quantitative, qualitative, or mixed methods, each done well.
- **Real-world relevance** — implications grounded in the evidence, specific about actors and levers.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/gec-skills
/plugin install gec-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/gec-skills.git
cd gec-skills

mkdir -p ~/.claude/skills && cp -R skills/gec-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/gec-* ~/.codex/skills/
```

### First Prompt

```
Use gec-workflow to tell me which skill I should use next for my Global Environmental Change manuscript.
```

---

## Default Workflow

```text
gec-topic-selection
        ▼
gec-literature-positioning
        ▼
gec-conceptual-framework
        ▼
gec-research-design
        ▼
gec-data-analysis
        ▼
gec-figures-and-tables
        ▼
gec-writing-style          (polish)
        ▼
gec-policy-relevance-and-implications
        ▼
gec-review-process
        ▼
gec-submission
        ▼
gec-revision-and-rebuttal
```

`gec-workflow` is the router — it tells you which skill to use next based on where you are. Its first
job is to confirm the paper has a **significant social-science component** and a real policy payoff; most
papers loop **framework ↔ design ↔ analysis** several times before writing-style.

---

## Skills

| Skill                                      | Purpose                                                                       |
|--------------------------------------------|-------------------------------------------------------------------------------|
| `gec-workflow`                             | Router — decides which sub-skill to invoke next                               |
| `gec-topic-selection`                      | Human/policy fit and significance; pick the right article format              |
| `gec-literature-positioning`               | Engage multiple literatures; position at their interdisciplinary intersection |
| `gec-conceptual-framework`                 | Build a framework that generates the question and structures the analysis     |
| `gec-research-design`                      | Defend the design — causal inference, case work, experiments, mixed methods   |
| `gec-data-analysis`                        | Analysis norms, uncertainty, robustness, qualitative and mixed integration    |
| `gec-figures-and-tables`                   | Self-contained, accessible exhibits and the required Highlights               |
| `gec-writing-style`                        | Rigor that reads across disciplines, within the word and abstract caps        |
| `gec-policy-relevance-and-implications`    | Real-world implications: actors, levers, scope, equity, uncertainty           |
| `gec-review-process`                       | Double-anonymized review, scope/social-science screening, decision categories |
| `gec-submission`                           | Elsevier submission preflight (anonymization, caps, Highlights, data statement) |
| `gec-revision-and-rebuttal`                | Response-letter strategy for interdisciplinary reviewers + editor             |

### Resources

- [`resources/external_tools.md`](resources/external_tools.md) — environmental-change data sources (IPCC / ND-GAIN / FAOSTAT / WVS / Global Forest Watch) + R / Stata / Python and qualitative/CAQDAS and systems tooling
- [`resources/official-source-map.md`](resources/official-source-map.md) — official Elsevier / ScienceDirect URLs behind current process facts, refreshed 2026-06-20

---

## What This Repo Does Not Do

- It does not write a submittable manuscript for you
- It does not simulate any specific editor's or reviewer's taste
- It does not freeze volatile metadata (APC, editors, special calls, policy wording); re-check live pages before filing
- It does not decide whether your question has a genuine human-dimensions contribution — that is the researcher's call

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [Global Environmental Change (ScienceDirect)](https://www.sciencedirect.com/journal/global-environmental-change) — publisher home, aims and scope
- [Guide for Authors](https://www.sciencedirect.com/journal/global-environmental-change/publish/guide-for-authors) — article types, caps, Highlights, data policy

---

## License

MIT
