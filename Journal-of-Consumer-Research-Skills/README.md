# Journal of Consumer Research (JCR) Skills

<p align="center">
  <img src="assets/cover.svg" alt="Journal of Consumer Research cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-JCR-7a1f2b)](https://consumerresearcher.com/about)
[![Publisher](https://img.shields.io/badge/publisher-Oxford%20University%20Press-1f6feb)](https://academic.oup.com/jcr)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at the **Journal of Consumer Research (JCR)** — the multi-disciplinary flagship of consumer behavior research, published by Oxford University Press (OUP) for Journal of Consumer Research, Inc.

This repository is opinionated. It is **not** a generic "marketing writing" toolbox. It is a **JCR-specific** stack built around JCR's defining bar: a clear **conceptual contribution** that *advances, deepens, or repudiates* existing theory about consumption, supported by appropriate empirical evidence. It covers consumer-behavior topic selection, interdisciplinary theory development, literature positioning across psychology/anthropology/sociology/economics, multi-study experimental and Consumer Culture Theory (CCT) designs, process evidence and trustworthiness, the conceptual-contribution statement, Chicago house-style exhibits and prose, ScholarOne submission, double-anonymized review, and multi-round R&R rebuttals.

> Durable norms only. Editors, fees, exact limits, and policies change — always verify on consumerresearcher.com and the OUP JCR instructions. Facts in this pack were accessed **2026-06-01**; see [`resources/official-source-map.md`](resources/official-source-map.md). Unverified items are marked **待核实**.

---

## Why a Separate JCR Skill Stack?

JCR imposes constraints that differ materially from other marketing/behavioral journals:

| Constraint              | Journal of Consumer Research                                      | Implication                                                       |
|-------------------------|------------------------------------------------------------------|------------------------------------------------------------------|
| Discipline              | Multi-disciplinary consumer **behavior** (psych/anthro/soc/econ) | Pure modeling, strategy, or managerial papers are off-fit        |
| Core bar                | A **conceptual contribution** about consumption                   | A robust effect with no theory advance reads as a tech report    |
| Two genres              | Multi-study **experiments** *and* interpretive **CCT** work       | Ethnography and lab experiments compete on equal footing         |
| Required gate           | 300-word **Consumer Relevance and Contribution Statement**        | A JCR-specific statement, distinct from the 200-word abstract    |
| Length                  | **60 double-spaced pages**, tables/figures **embedded and counted** | A page cap, not a word cap; a 40 MB web appendix holds overflow |
| Transparency            | Step-6 **Data Collection Statement**, approved repositories, code  | Required at invited revision; 7-year data retention              |
| Style                   | **Chicago Manual of Style** (not APA); Word                       | Configure references to Chicago, not APA                         |
| Review                  | **Double-anonymized**; ScholarOne; developmental, multi-round     | First-round accepts are essentially unheard of                   |
| Fees                    | **No** submission or publication fee (subscription under OUP)     | Only optional open-access and color-print charges                |

Generic "scientific writing" or "marketing methods" packs do not address these constraints.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/jcr-skills
/plugin install jcr-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/jcr-skills.git
cd jcr-skills

mkdir -p ~/.claude/skills && cp -R skills/jcr-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/jcr-* ~/.codex/skills/
```

### First Prompt

```
Use jcr-workflow to tell me which skill I should use next for my JCR manuscript.
```

---

## Default Workflow

```text
jcr-topic-selection
        ▼
jcr-theory-development
        ▼
jcr-literature-positioning
        ▼
jcr-methods
        ▼
jcr-data-analysis
        ▼
jcr-contribution-framing
        ▼
jcr-tables-figures
        ▼
jcr-writing-style        (polish)
        ▼
jcr-submission
        ▼
jcr-review-process
        ▼
jcr-rebuttal
```

`jcr-workflow` is the router — it tells you which skill to use next based on where you are.

---

## Skills

| Skill                        | Purpose                                                                       |
|------------------------------|-------------------------------------------------------------------------------|
| `jcr-workflow`               | Router — decides which sub-skill to invoke next                               |
| `jcr-topic-selection`        | Consumer-behavior question + JCR fit test (vs. JCP/JMR/JM)                     |
| `jcr-theory-development`     | Psychological process & hypotheses (experiments) or grounded theory (CCT)     |
| `jcr-literature-positioning` | Joining an interdisciplinary conversation; problematization over gap-spotting |
| `jcr-methods`                | Multi-study experiments, CCT fieldwork, mixed designs, Registered Reports     |
| `jcr-data-analysis`          | Process evidence (mediation/moderation, spotlight), CCT trustworthiness       |
| `jcr-contribution-framing`   | Conceptual contribution + the 300-word Consumer Relevance Statement           |
| `jcr-tables-figures`         | Study tables, process figures, interaction/spotlight plots in Chicago style   |
| `jcr-writing-style`          | Front-loaded, interdisciplinary prose; Chicago house style; anonymization     |
| `jcr-submission`             | ScholarOne preflight: anonymization, 60-page cap, Data Collection Statement   |
| `jcr-review-process`         | How JCR double-anonymized review/decisions work; reading a decision letter    |
| `jcr-rebuttal`               | Multi-round R&R revision and point-by-point response letter                   |

### Resources

- [`resources/external_tools.md`](resources/external_tools.md) — participant sourcing (Prolific/CloudResearch/Qualtrics), analysis (R/PROCESS/spotlight), CCT tools (NVivo/ATLAS.ti), and JCR-approved repositories (OSF/Harvard Dataverse/QDR/ResearchBox)
- [`resources/official-source-map.md`](resources/official-source-map.md) — official JCR/OUP URLs behind every verified fact (accessed 2026-06-01)

---

## Differences vs. JCP / JMR / JM

| Dimension          | JCR                                  | JCP                          | JMR                                | JM                           |
|--------------------|--------------------------------------|------------------------------|------------------------------------|------------------------------|
| Scope              | Consumer **behavior**, interdisciplinary | Consumer **psychology**     | Broad marketing research           | Broad marketing, managerial  |
| Core contribution  | Conceptual theory about consumption  | Psychological process        | Methods/substantive marketing      | Managerial + substantive     |
| Signature methods  | Multi-study experiments **+ CCT**    | Behavioral experiments       | Experiments, modeling, surveys     | Mixed, including modeling     |
| Default style      | **Chicago** Manual of Style          | APA-leaning                  | journal-specific                   | journal-specific             |

If your paper is an analytical-modeling, strategy, or managerial marketing contribution with no real consumer-theory advance, target **JMR / JM / Marketing Science**, not JCR. A purely psychological process paper may fit **JCP**.

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — index of journal-specific skill packs

---

## License

MIT
