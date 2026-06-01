# Journal of Operations Management (JOM) Skills

<p align="center">
  <img src="assets/cover.svg" alt="Journal of Operations Management cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-JOM-0b3d62)](https://www.ascm.org/making-an-impact/research/journal-operations-management/jom/)
[![Index](https://img.shields.io/badge/index-FT50-1f6feb)](https://en.wikipedia.org/wiki/Journal_of_Operations_Management)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at the **Journal of Operations Management (JOM)** — the flagship outlet for *original, empirical* operations and supply chain management research, published by **Wiley on behalf of the Association for Supply Chain Management (ASCM, formerly APICS)**.

This repository is opinionated. It is **not** a generic "operations" or "supply-chain writing" toolbox, and it is **not** for analytical OR/optimization work. It is a **JOM-specific** stack built around JOM's defining bar: an *empirical* study where **operations are at the heart of the research question, not just in the context** — "it is the observation that renders the research empirical." It covers operations-centered topic selection, a priori OM theory development, literature positioning against the OM/SCM conversation, empirical design (survey, archival/secondary, field, case, experimental, and intervention-based), data analysis and validity, dual academic-and-practical contribution framing, APA-style exhibits and prose, the Department-routed cover-letter and checklist submission via Wiley ReX, the asymmetric double-anonymous review process, and multi-round R&R rebuttals.

> Durable norms only. Co-Editors-in-Chief, the Department roster, fees, the APC, the abstract limit, and exact length rules change — always verify on the official ASCM/JOM page, the Wiley JOM Author Guidelines, and the current author-resource pages. Items not confirmed on an authoritative page are flagged **待核实** in [`resources/official-source-map.md`](resources/official-source-map.md).

---

## Why a Separate JOM Skill Stack?

JOM imposes constraints that differ materially from analytical OM journals and generic management/economics outlets:

| Constraint              | Journal of Operations Management                                | Implication                                                       |
|-------------------------|-----------------------------------------------------------------|-------------------------------------------------------------------|
| Discipline              | Empirical operations & supply chain management                  | Operations must be the *heart* of the question, not the setting   |
| Empirical mandate       | Observation-grounded research only                              | **No purely analytical models or optimization** (→ OR/IE/analytical OM journals) |
| Methods                 | Survey, archival/secondary, field, case, experiment, **intervention-based** | The design must observe at the claimed operational level   |
| Theory                  | Empirical strength **and** a meaningful OM theory contribution   | A phenomenon-only "tech report" is rejected                       |
| Validity                | Measurement validity, CMB remedies, endogeneity, method check    | A dedicated **Empirical Research Methods** Department screens incoming work |
| Routing                 | One of **12 Departments**; name 2 (one preferred) in the cover letter | Misrouted framing reads as off-fit                          |
| Cover letter            | Recommend **≥3 Associate Editors and ≥3 ERB reviewers**, conflict-free | Unusually prescriptive — must be done                       |
| Review                  | **Asymmetric** double-anonymous (EICs/DEs see identity; reviewers/AEs do not) | Anonymize the manuscript fully                          |
| Format                  | ~40 pages; double-spaced, single-column, 12-pt; **APA**; checklist required | Over-long manuscripts are returned for streamlining        |
| Integrity               | iThenticate/CrossCheck; single source <~1%, overall <15% (else justify) | Stricter than a single global threshold                     |
| Audience                | Academics **and** ASCM practitioners                            | Practical relevance must be concrete and operational              |

Generic "scientific writing", "social-science methods", or analytical-OM packs do not address these constraints.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/jom-skills
/plugin install jom-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/jom-skills.git
cd jom-skills

mkdir -p ~/.claude/skills && cp -R skills/jom-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/jom-* ~/.codex/skills/
```

### First Prompt

```
Use jom-workflow to tell me which skill I should use next for my JOM manuscript.
```

---

## Default Workflow

```text
jom-topic-selection
        ▼
jom-theory-development
        ▼
jom-literature-positioning
        ▼
jom-methods
        ▼
jom-data-analysis
        ▼
jom-contribution-framing
        ▼
jom-tables-figures
        ▼
jom-writing-style        (polish)
        ▼
jom-submission
        ▼
jom-review-process
        ▼
jom-rebuttal
```

`jom-workflow` is the router — it tells you which skill to use next based on where you are.

---

## Skills

| Skill                       | Purpose                                                                       |
|-----------------------------|-------------------------------------------------------------------------------|
| `jom-workflow`              | Router — decides which sub-skill to invoke next                               |
| `jom-topic-selection`       | Operations-as-heart + empirical fit test; choose among the 12 Departments     |
| `jom-theory-development`    | A priori OM mechanisms (operational/behavioral/organizational) and hypotheses |
| `jom-literature-positioning`| Joining the OM/SCM conversation; distinguishing from analytical OM            |
| `jom-methods`               | Matching survey/archival/field/case/experiment/IBR to the operations question |
| `jom-data-analysis`         | Measurement, CMB, endogeneity, SEM/HLM/panel/count/survival; method-check ready |
| `jom-contribution-framing`  | Dual academic-and-practical contribution with operations at the center         |
| `jom-tables-figures`        | Descriptive/correlation/result tables, interaction & process figures (APA)     |
| `jom-writing-style`         | Front-loaded operations argument, dual audience, APA, length & similarity rules |
| `jom-submission`            | Wiley ReX preflight: Departments, cover-letter protocol, checklist, anonymization |
| `jom-review-process`        | Department routing, asymmetric double-anonymous review, the method check        |
| `jom-rebuttal`              | Multi-round R&R revision and point-by-point response letter                     |

### Resources

- [`skills/jom-submission/templates/cover_letter_template.md`](skills/jom-submission/templates/cover_letter_template.md) — JOM cover letter with the Department + reviewer-recommendation + disclosure protocol
- [`skills/jom-submission/templates/checklist.md`](skills/jom-submission/templates/checklist.md) — 10-section pre-submission self-check (the required checklist)
- [`resources/external_tools.md`](resources/external_tools.md) — empirical-OM data sources (Compustat / Panjiva / FactSet Revere / Qualtrics / Prolific / IMSS-GMRG-HPM) and analysis software (Mplus / R lavaan / Stata reghdfe & csdid / NVivo)
- [`resources/official-source-map.md`](resources/official-source-map.md) — every venue fact with its official URL and accessed date; unverified items flagged **待核实**

---

## What JOM Does NOT Publish

JOM explicitly does **not** publish purely analytical models or optimization techniques — "these belong in operations research, industrial engineering, or analytical OM journals."

| If your paper is...                                  | Target instead                                          |
|------------------------------------------------------|---------------------------------------------------------|
| A pure optimization / queueing / analytical model    | *Operations Research*, *M&SOM*, *Management Science* (OM) |
| A simulation with no empirical observation           | Analytical/IE venues                                    |
| Empirical OM with operations at the heart + theory   | **Journal of Operations Management** ✅                  |

If there is no **observation** anchoring the study, JOM is not the venue.

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — index of journal-specific skill packs

---

## License

MIT
