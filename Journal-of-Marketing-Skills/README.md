# Journal of Marketing (JM) Skills

<p align="center">
  <img src="assets/cover.svg" alt="Journal of Marketing cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-JM-b3122b)](https://www.ama.org/journal-of-marketing/)
[![Publisher](https://img.shields.io/badge/AMA%20%C2%B7%20SAGE-substantive-1f6feb)](https://www.ama.org/journal-of-marketing/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at the **Journal of Marketing (JM)** — the American Marketing Association's (AMA) premier *general-audience* journal for **substantive** marketing research, published by SAGE on behalf of the AMA.

This repository is opinionated. It is **not** a generic "marketing writing" toolbox. It is a **JM-specific** stack built around JM's defining bar: **the most impactful, thought-leading substantive research in the marketing discipline**, with genuine **managerial, policy, and societal relevance**. It covers substantive topic selection, theory grounded in real-world marketing phenomena, literature positioning, JM's "big tent" / **empirics-first** empirical methods, exact-statistics data analysis with JM Dataverse replication, managerial-relevance contribution framing, AMA house-style exhibits and prose, ScholarOne (Sage Track) submission, the double-anonymized review process, and multi-round R&R rebuttals.

> Durable norms only. Editor rosters, portal prompts, fee/OA language, and transparency workflows change — run the source-map live checks against the official JM/SAGE/AMA pages before upload.

---

## Why a Separate JM Skill Stack?

JM imposes constraints that differ materially from theory-driven, modeling-heavy, or pure-consumer-behavior marketing journals:

| Constraint              | Journal of Marketing                                                | Implication                                                       |
|-------------------------|---------------------------------------------------------------------|------------------------------------------------------------------|
| Core bar                | **Substantive** insight into important real-world marketing questions | Methodological novelty for its own sake is out of scope         |
| Dual mandate            | Scholarly **and** practical — managerial/policy/societal relevance required | Relevance is mandatory, not a courtesy paragraph              |
| Audience                | Scholars, educators, managers, policy makers, consumers, society     | A general-audience, "bridge" framing — not a niche-specialist read |
| Data stance             | "Big tent": experiments, field studies, surveys, interviews, observational, secondary; **empirics-first** welcomed | No single method is privileged; the phenomenon leads        |
| Anti-incrementalism     | Replicating theory or applying existing findings to a new context is rejected | "New context" alone is not a contribution                   |
| Methods role            | Methods serve the substantive question; "unnecessarily complex analyses" are pushed back on | Modeling-for-its-own-sake routes to Marketing Science / JMR  |
| Statistics reporting    | Actual p-values, standard errors, **and effect sizes** required      | "p < .05" thresholds are non-compliant                          |
| Length                  | Hard **50-page** limit inclusive of everything except web appendices | Tables, figures, references, print appendices all count         |
| Transparency            | Replication packet to **JM Dataverse** at conditional acceptance     | Data + code (or qualitative materials) Editor-accessible, reviewer-blind |
| Process                 | ScholarOne (Sage Track); double-anonymized; handling Editor decides  | Manuscripts must be fully anonymized                            |
| Fees                    | No fees payable to submit or publish in the subscription route; optional OA via Sage Choice may carry a fee | Budget only after checking the live SAGE/OA prompts |

Generic "scientific writing" or "social-science methods" packs do not address these constraints.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/jm-skills
/plugin install jm-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/jm-skills.git
cd jm-skills

mkdir -p ~/.claude/skills && cp -R skills/jm-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/jm-* ~/.codex/skills/
```

### First Prompt

```
Use jm-workflow to tell me which skill I should use next for my Journal of Marketing manuscript.
```

---

## Default Workflow

```text
jm-topic-selection
        ▼
jm-theory-development
        ▼
jm-literature-positioning
        ▼
jm-methods
        ▼
jm-data-analysis
        ▼
jm-contribution-framing
        ▼
jm-tables-figures
        ▼
jm-writing-style        (polish)
        ▼
jm-submission
        ▼
jm-review-process
        ▼
jm-rebuttal
```

`jm-workflow` is the router — it tells you which skill to use next based on where you are.

---

## Skills

| Skill                       | Purpose                                                                 |
|-----------------------------|-------------------------------------------------------------------------|
| `jm-workflow`               | Router — decides which sub-skill to invoke next                         |
| `jm-topic-selection`        | Substantive, managerially relevant question + JM fit test (vs. JMR / Marketing Science / JCR) |
| `jm-theory-development`     | Theory grounded in real-world marketing phenomena; empirics-first reasoning |
| `jm-literature-positioning` | Join the substantive conversation; avoid "new context" incrementalism   |
| `jm-methods`                | Match design (experiment / field / survey / secondary / qualitative) to the substantive question |
| `jm-data-analysis`          | Exact p-values, SEs, effect sizes; identification; JM Dataverse replication |
| `jm-contribution-framing`   | Explicit substantive + managerial/policy/societal contribution          |
| `jm-tables-figures`         | Result tables, managerial-takeaway exhibits, interaction plots in AMA style |
| `jm-writing-style`          | Front-loaded substantive argument, AMA author-date house style          |
| `jm-submission`             | ScholarOne (Sage Track) preflight: anonymization, 50-page format, files |
| `jm-review-process`         | How JM double-anonymized review/decisions work; reading a decision letter |
| `jm-rebuttal`               | Multi-round R&R revision and point-by-point response letter             |

### Resources

- [`resources/external_tools.md`](resources/external_tools.md) — marketing-research data (NielsenIQ / Circana / Prolific / Qualtrics / Sawtooth / field-experiment partners) and analysis software (R lavaan / PROCESS / Stata reghdfe / DiD / choice models)
- [`resources/official-source-map.md`](resources/official-source-map.md) — official AMA/SAGE/JM URLs behind every verified fact (accessed 2026-06-20) and live-check items

---

## Differences vs. JMR / Marketing Science / JCR

| Dimension          | Journal of Marketing                  | JMR                                   | Marketing Science                  | JCR                                |
|--------------------|---------------------------------------|---------------------------------------|------------------------------------|------------------------------------|
| Core contribution  | **Substantive** + managerial relevance | Methods-forward empirical rigor       | Analytical / quant modeling        | Interdisciplinary consumer theory  |
| Method emphasis    | "Big tent", empirics-first            | Measurement, models, methods          | Formal/game-theoretic & structural | Consumer-behavior experiments/theory |
| Audience           | Managers, policy, society + scholars  | Marketing researchers                 | Modelers, analysts                 | Consumer researchers (broad social science) |
| Owner / publisher  | AMA / SAGE                            | AMA / SAGE                            | INFORMS                            | Oxford UP / ACR                    |

If your paper is centered on a modeling or methods advance rather than a substantive marketing insight, target **Marketing Science** or **JMR**; if it is interdisciplinary consumer theory, target **JCR**.

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — index of journal-specific skill packs

---

## License

MIT
