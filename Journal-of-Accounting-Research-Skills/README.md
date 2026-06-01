# Journal of Accounting Research (JAR) Skills

<p align="center">
  <img src="assets/cover.svg" alt="Journal of Accounting Research cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-JAR-7a0019)](https://www.chicagobooth.edu/research/chookaszian/journal-of-accounting-research)
[![Index](https://img.shields.io/badge/index-FT50%20%7C%20SSCI-1f6feb)](https://www.chicagobooth.edu/research/chookaszian/journal-of-accounting-research)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at the **Journal of Accounting Research (JAR)** — one of the "top three" accounting journals, sponsored by the **Chookaszian Accounting Research Center at the University of Chicago Booth School of Business** and published with Wiley-Blackwell.

This repository is opinionated. It is **not** a generic "accounting writing" toolbox. It is a **JAR-specific** stack built around JAR's defining identity: rigorous **empirical-archival capital-markets** research in the **Ball-Brown** lineage, judged on **credible identification** and an economic story about how accounting information is produced, disclosed, audited, and used. It covers question selection and JAR fit, economics-based theory and signed predictions, literature positioning, identification-driven design, large-sample archival analysis (clustering, endogeneity, construct measurement, robustness), contribution framing, JAR house-style exhibits and prose, the Wiley Research Exchange submission and tiered-fee gate, the double-anonymized editor-panel review, and R&R rebuttals.

> Durable norms only. Editors, fees, exact limits, the conference theme, and policies change — always verify on the official Chookaszian Center JAR pages and the Wiley author guidelines.

---

## Why a Separate JAR Skill Stack?

JAR imposes constraints that differ materially from theory-only or management journals:

| Constraint              | Journal of Accounting Research                              | Implication                                                  |
|-------------------------|------------------------------------------------------------|--------------------------------------------------------------|
| Discipline              | Empirical accounting (capital markets, disclosure, audit, tax) | Pure-finance or pure-methods papers are off-fit           |
| Core bar                | Credible **identification** + an economic story            | A panel regression with no identifying variation reads as correlation |
| Theory                  | Economics-based mechanism (information / agency / disclosure) | Psychology-style construct chains do not fit                |
| Design                  | Archival natural experiments, RD, IV, event studies (also experiments/analytical/field) | The design must actually identify the effect |
| Inference               | Clustering matched to the design (firm / firm×year)        | Robust SEs on panel data get flagged                         |
| Reproducibility         | **Mandatory** data-and-code sharing (posted & hosted)      | "Code on request" is not acceptable; build the package early |
| Submission gate         | **Tiered fee** ($750/$500/$50), paid within one week       | Budget the fee; lower tier needs all authors in Tier 2/3     |
| Volume cap              | At most **four new papers / author / two years**           | Choose which projects to send                                |
| Process                 | Senior-Editor panel; double-anonymized; multi-round R&R    | No single EIC; first-round accepts are unheard of            |
| Distinctive tracks      | **Ray Ball Annual Conference** (June issue); **Registered Reports** | Extra paths with their own rules                       |

Generic "scientific writing" or "social-science methods" packs do not address these constraints.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/jar-skills
/plugin install jar-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/jar-skills.git
cd jar-skills

mkdir -p ~/.claude/skills && cp -R skills/jar-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/jar-* ~/.codex/skills/
```

### First Prompt

```
Use jar-workflow to tell me which skill I should use next for my JAR manuscript.
```

---

## Default Workflow

```text
jar-topic-selection
        ▼
jar-theory-development
        ▼
jar-literature-positioning
        ▼
jar-methods
        ▼
jar-data-analysis
        ▼
jar-contribution-framing
        ▼
jar-tables-figures
        ▼
jar-writing-style        (polish)
        ▼
jar-submission
        ▼
jar-review-process
        ▼
jar-rebuttal
```

`jar-workflow` is the router — it tells you which skill to use next based on where you are.

---

## Skills

| Skill                       | Purpose                                                                 |
|-----------------------------|-------------------------------------------------------------------------|
| `jar-workflow`              | Router — decides which sub-skill to invoke next                         |
| `jar-topic-selection`       | Accounting question + credible setting + JAR fit (vs. TAR/JAE/RAST/CAR) |
| `jar-theory-development`    | Economics-based mechanism; signed, falsifiable predictions              |
| `jar-literature-positioning`| Joining the accounting conversation; marginal contribution              |
| `jar-methods`               | Identification strategy (archival NE / RD / IV / event study / experiment) |
| `jar-data-analysis`         | SE clustering, endogeneity execution, construct measurement, robustness |
| `jar-contribution-framing`  | Explicit contribution to accounting knowledge + economic magnitude       |
| `jar-tables-figures`        | Sample/descriptive/results/identification exhibits in JAR house style    |
| `jar-writing-style`         | Design-forward, economically literate prose; JAR author-date style       |
| `jar-submission`            | Research Exchange preflight: anonymization, tiered fee, data-and-code     |
| `jar-review-process`        | Editor-panel review, fee/desk gates, Ray Ball & Registered Reports tracks |
| `jar-rebuttal`              | Multi-round R&R revision and point-by-point response letter             |

### Resources

- [`resources/external_tools.md`](resources/external_tools.md) — empirical-accounting data sources (Compustat / CRSP / I/B/E/S / Audit Analytics / EDGAR) and analysis software (Stata `reghdfe`/`csdid`/`rdrobust`, R `fixest`, SAS, WRDS)
- [`resources/official-source-map.md`](resources/official-source-map.md) — official JAR / Chookaszian Center / Wiley URLs behind every verified fact (accessed 2026-06-01); unverified items flagged 待核实

---

## What Makes JAR Distinctive

- **Empirical-archival capital-markets identity** (the Ball-Brown lineage) — identification and economic magnitude weigh as heavily as a sound regression.
- **Mandatory data-and-code sharing** — JAR actually **requires and hosts** datasheets/code, unlike top peers that merely encourage it.
- **Tiered, country-based submission fee** ($750/$500/$50), due within one week of submission.
- **Senior-Editor panel** (no single editor-in-chief) running double-anonymized review.
- **Ray Ball JAR Annual Conference** with a dedicated (historically June) conference issue.
- **Registered Reports** — pre-registered, two-stage, outcome-independent in-principle acceptance.

---

## Differences vs. TAR / JAE / RAST / CAR

| Dimension          | JAR                               | TAR                          | JAE                                | RAST / CAR                   |
|--------------------|-----------------------------------|------------------------------|------------------------------------|------------------------------|
| Sponsor/publisher  | Chicago Booth (Chookaszian) / Wiley | American Accounting Assn.   | Elsevier                           | Springer / Wiley             |
| Signature identity | Empirical-archival capital markets | Broad, all accounting fields | Positive contracting/disclosure economics | Broad empirical accounting |
| Data/code policy   | **Required & hosted**             | No equivalent mandate        | **Encouraged**                     | Varies                       |
| Distinctive tracks | Ray Ball Conference; Registered Reports | —                       | —                                  | —                            |

If your paper is purely a methods contribution with no accounting question, or has no identification leverage, JAR is likely the wrong venue.

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — index of journal-specific skill packs

---

## License

MIT
