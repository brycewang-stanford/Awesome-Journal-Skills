# Journal of Business Venturing (JBV) Skills

<p align="center">
  <img src="assets/cover.svg" alt="Journal of Business Venturing cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-JBV-b8460e)](https://www.sciencedirect.com/journal/journal-of-business-venturing)
[![Index](https://img.shields.io/badge/index-FT50%20%7C%20SSCI-1f6feb)](https://www.sciencedirect.com/journal/journal-of-business-venturing)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at the **Journal of Business Venturing (JBV)** — an FT50 flagship in **entrepreneurship and new venture creation**, published by **Elsevier** (print ISSN 0883-9026, online ISSN 1873-2003). Current ScienceDirect metadata lists **Sophie Bacq** and **Simon Parker** as Co-Editors-in-Chief.

This repository is opinionated. It is **not** a generic "management writing" toolbox. It is a **JBV-specific** stack built around JBV's defining bar: a paper must illuminate the **entrepreneurial phenomenon in its myriad of forms** and make a clear theoretical contribution to entrepreneurship — entrepreneurship must be *central*, not an incidental empirical setting. It covers phenomenon-driven topic selection, multidisciplinary theory development (economics, psychology, sociology), literature positioning in the entrepreneurship conversation, methodologically pluralistic design and analysis (econometrics on novel venture datasets, experiments, qualitative process work, mixed methods), theoretical-contribution framing, Elsevier house-style exhibits and prose, Editorial Manager submission under double-anonymized review, area-editor review routing, and R&R rebuttals.

> Durable norms only. Editors, area-editor domains, APCs, metrics, and policies change — always verify on the official JBV Guide for Authors (ScienceDirect), editorial-board page, open-access page, and Editorial Manager portal. `resources/official-source-map.md` was refreshed on 2026-06-20.

---

## Why a Separate JBV Skill Stack?

JBV imposes constraints that differ materially from general management or economics journals:

| Constraint              | Journal of Business Venturing                                       | Implication                                                       |
|-------------------------|--------------------------------------------------------------------|------------------------------------------------------------------|
| Domain                  | Entrepreneurship / new venture creation must be **central**        | A well-identified org study with no entrepreneurial core is off-fit |
| Disciplinary lens       | Self-consciously **multidisciplinary** (econ, psych, sociology)    | Breadth of lens is an expectation, not a bonus                   |
| Contribution mode       | Welcomes "theories, **narratives, and interpretations**"           | Not only the strict hypothetico-deductive template               |
| Methodology             | Pluralistic but **theory-first** — method must serve the question  | Method showcased without theory advance is desk-reject risk      |
| Routing                 | **Area editors / handling editors** under the Co-EICs shape review | Fit with the relevant domain shapes routing and outcome          |
| Review                  | **Double-anonymized**; minimum two reviewers                       | Anonymize fully (no names, affiliations, acknowledgements)       |
| Submission              | Elsevier **Editorial Manager**; flexible references at submission  | Separate title page + anonymized manuscript; co-submit Data in Brief/MethodsX |
| Declarations            | Competing-interest **and** generative-AI disclosure required       | Both mandatory at submission                                     |
| Data                    | Elsevier **Option C** research-data policy                         | Deposit/cite/link data or explain why data cannot be shared      |

Generic "scientific writing" or "social-science methods" packs do not address these constraints.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/jbv-skills
/plugin install jbv-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/jbv-skills.git
cd jbv-skills

mkdir -p ~/.claude/skills && cp -R skills/jbv-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/jbv-* ~/.codex/skills/
```

### First Prompt

```
Use jbv-workflow to tell me which skill I should use next for my JBV manuscript.
```

---

## Default Workflow

```text
jbv-topic-selection
        ▼
jbv-theory-development
        ▼
jbv-literature-positioning
        ▼
jbv-methods
        ▼
jbv-data-analysis
        ▼
jbv-contribution-framing
        ▼
jbv-tables-figures
        ▼
jbv-writing-style        (polish)
        ▼
jbv-submission
        ▼
jbv-review-process
        ▼
jbv-rebuttal
```

`jbv-workflow` is the router — it tells you which skill to use next based on where you are.

---

## Skills

| Skill                       | Purpose                                                                       |
|-----------------------------|-------------------------------------------------------------------------------|
| `jbv-workflow`              | Router — decides which sub-skill to invoke next                               |
| `jbv-topic-selection`       | Phenomenon-driven entrepreneurship question + JBV fit test (vs. general mgmt) |
| `jbv-theory-development`    | Multidisciplinary mechanism (econ/psych/sociology); narratives welcome        |
| `jbv-literature-positioning`| Joining the entrepreneurship conversation; problematization over gap-spotting |
| `jbv-methods`               | Matching design (venture panel/experiment/qualitative/mixed) to the question  |
| `jbv-data-analysis`         | Survival/selection/panel estimators, attrition, endogeneity, robustness       |
| `jbv-contribution-framing`  | Explicit contribution to entrepreneurship theory + boundary conditions        |
| `jbv-tables-figures`        | Venture-data tables, process models, interaction plots in Elsevier style      |
| `jbv-writing-style`         | Phenomenon-forward argument, active voice, Elsevier reference style           |
| `jbv-submission`            | Editorial Manager preflight + anonymization, declarations, co-submission      |
| `jbv-review-process`        | How JBV area-editor review/decisions work; reading a decision letter          |
| `jbv-rebuttal`              | Multi-round R&R revision and point-by-point response letter                   |

### Resources

- [`resources/official-source-map.md`](resources/official-source-map.md) — every used fact + official URL + accessed date; refreshed 2026-06-20
- [`resources/external_tools.md`](resources/external_tools.md) — entrepreneurship data sources (GEM / PSED / Kauffman / PitchBook / Crunchbase / Kickstarter) and analysis software (Stata survival/panel, R `fixest`/`survival`, NVivo, fsQCA, G*Power)

---

## What Makes JBV Distinctive

- **Phenomenon-driven mandate** — the paper must illuminate the entrepreneurial phenomenon; entrepreneurship is the contribution, not the setting. This separates JBV from general management journals that accept any well-identified organizational study.
- **Multidisciplinary by design** — grounded in economics, psychology, and sociology, and welcoming anthropology, geography, history, and multiple functional areas.
- **Area-editor / handling-editor routing** — manuscripts are routed under the current Co-Editors-in-Chief; fit with the relevant entrepreneurship domain matters.
- **Theories, narratives, and interpretations** — JBV elevates interesting narrative and interpretive theorizing alongside hypothesis-testing.
- **FT50 / discipline-defining flagship** — a high theory bar; off-topic or insufficiently theorized work is commonly desk-rejected.
- **Built-in co-submission** — Data in Brief / MethodsX artifacts attach in the Editorial Manager workflow.

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — index of journal-specific skill packs
- Academy-of-Management-Journal-Skills — AMJ (premier *empirical* management journal)

---

## License

MIT
