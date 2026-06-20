# Journal of Development Economics Skills

<p align="center">
  <img src="assets/cover.svg" alt="Journal of Development Economics cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-JDE-1b5e3f)](https://www.sciencedirect.com/journal/journal-of-development-economics)
[![Field](https://img.shields.io/badge/field-Development%20Economics-1f6feb)](https://www.sciencedirect.com/journal/journal-of-development-economics)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at the **Journal of Development Economics (JDE)** — the **leading field journal in development economics**, published by **Elsevier** and edited by Editors-in-Chief **A. Foster** and **K. Macours**. JDE publishes theoretical and empirical research on the economics of developing countries and the process of economic development.

This repository is opinionated. It is **not** a generic economics-writing toolbox. It is a **JDE-specific** stack for development economics: a first-order question about low- and middle-income economies, credible identification in messy field settings (RCT / DID / IV / RDD), welfare-relevant magnitudes, an extensive online appendix, and a **mandatory, review-stage-ready replication package** deposited to Mendeley Data.

---

## What Is JDE, and Why a Dedicated Stack?

JDE imposes constraints that differ from a top-5 general-interest journal or a methods journal:

| Constraint            | JDE                                                                          | Implication                                                       |
|-----------------------|------------------------------------------------------------------------------|------------------------------------------------------------------|
| Scope                 | Economics of developing countries / economic development                     | A generic micro result on LMIC data is off-fit                   |
| Premium on            | A **first-order development question** + credible identification             | Technique-first or descriptive-only papers struggle              |
| Identification        | RCT/field experiment, DID, IV, RDD — defended for field settings             | OLS + controls is not enough                                     |
| Publisher / portal    | **Elsevier**, via **Editorial Manager**                                      | Not OUP/Editorial Express; single-anonymized review              |
| Review model          | **Single-anonymized** (referees know the author)                             | Do not anonymize as double-blind                                 |
| Fee                   | **USD 50 non-refundable submission fee** for original manuscripts; optional OA APC after acceptance | Budget before filing; re-check the live payment screen           |
| Selectivity           | ~1,300 submissions/yr, ~1/4 reviewed, **~6-8% published**                    | A clean, complete, well-framed submission matters                |
| Replication           | Mandatory replication policy + Elsevier **Option C** data policy            | Build the package before you submit                              |
| Submission cap        | **≤ 3 papers per author per 12 months**                                      | Plan your submissions                                            |
| Distinctive routes    | Pre-results review (Registered Reports) + AER: Insights-style short-paper    | Choose the right track up front                                  |

The official ScienceDirect pages were refreshed on **2026-06-20** in [`resources/official-source-map.md`](resources/official-source-map.md). Re-check live pages before submission-ready advice because fees, editors, special issues, and policy wording can change.

### Three submission routes

- **Full-length (standard):** no fixed length limit; extensive online appendix expected.
- **Short-paper (limited-revision):** modeled on **AER: Insights** — ≤ 6,000 words, ≤ 5 exhibits, ≤ 20-page online appendix; refereed decisions generally in **6-8 weeks**, with a conditional-accept / reject structure.
- **Pre-results review (Registered Reports):** a **permanent** track (run with **BITSS**) — submit a Stage 1 proposal (hypotheses, procedures, statistical analysis plan, power analysis, pilot data) ≤ 60 pages with a ≤ 150-word abstract; get **in-principle acceptance before results are known**, then submit Stage 2.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/jde-skills
/plugin install jde-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/jde-skills.git
cd jde-skills

mkdir -p ~/.claude/skills && cp -R skills/jde-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/jde-* ~/.codex/skills/
```

### First Prompt

```
Use jde-workflow to tell me which skill I should use next for my JDE manuscript.
```

---

## Default Workflow

```text
jde-topic-selection
        ▼
jde-literature-positioning
        ▼
jde-contribution-framing
        ▼
jde-identification-strategy
        ▼
jde-data-analysis
        ▼
jde-tables-figures
        ▼
jde-writing-style          (polish)
        ▼
jde-replication-and-data-policy
        ▼
jde-review-process
        ▼
jde-submission
        ▼
jde-rebuttal
```

`jde-workflow` is the router — it tells you which skill to use next based on where you are. If your design is **prospective**, route to `jde-review-process` early to use the pre-results review track.

---

## Skills

| Skill                              | Purpose                                                                       |
|------------------------------------|-------------------------------------------------------------------------------|
| `jde-workflow`                     | Router — decides which sub-skill to invoke next                               |
| `jde-topic-selection`              | First-order development-question fit                                          |
| `jde-literature-positioning`       | Stake the contribution against the development frontier                       |
| `jde-contribution-framing`         | Make the development takeaway explicit and welfare-relevant                   |
| `jde-identification-strategy`      | Credible causal design (RCT / DID / IV / RDD) for field settings             |
| `jde-data-analysis`                | Estimation, heterogeneity, attrition, measurement, clustered inference        |
| `jde-tables-figures`               | Figure-forward exhibits with self-contained notes                            |
| `jde-writing-style`                | Land the question and policy stakes for a development audience               |
| `jde-replication-and-data-policy`  | Mandatory, review-ready data + code deposit (Mendeley Data)                  |
| `jde-review-process`               | Choose among full-length / short-paper / pre-results routes                  |
| `jde-submission`                   | Editorial Manager preflight                                                   |
| `jde-rebuttal`                     | R&R response-letter strategy (incl. single-round short-paper revision)       |

### Resources

- [`resources/external_tools.md`](resources/external_tools.md) — development data sources (LSMS / DHS / WDI / AEA RCT Registry) + Stata / R / Python packages for credible-design field work
- [`resources/official-source-map.md`](resources/official-source-map.md) — official JDE URLs behind current process facts, refreshed 2026-06-20

---

## What This Repo Does Not Do

- It does not write a submittable manuscript for you
- It does not simulate any specific editor's or referee's taste
- It does not freeze volatile metadata (fees, editors, APC, special issues, policy wording); re-check live pages before filing
- It does not judge whether your development question is genuinely first-order — that is the researcher's call

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [Journal of Development Economics (official)](https://www.sciencedirect.com/journal/journal-of-development-economics) — Elsevier / ScienceDirect
- [JDE pre-results review (BITSS)](https://www.bitss.org/publishing/jde/) — Registered Reports track

---

## License

MIT
