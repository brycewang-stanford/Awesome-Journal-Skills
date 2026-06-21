# Developmental Psychology Skills

<p align="center">
  <img src="assets/cover.svg" alt="Developmental Psychology cover" width="200">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Developmental%20Psychology-1a6a5a)](https://www.apa.org/pubs/journals/dev/)
[![Field](https://img.shields.io/badge/field-Lifespan%20Development-1f6feb)](https://www.apa.org/pubs/journals/dev/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **Developmental Psychology** — the **American Psychological
Association (APA)** journal for empirical work on **human development across the life span**: infancy,
childhood, adolescence, adulthood, and aging; cognitive, social, emotional, and biological development.
The journal's defining demand is a credible claim about **developmental change** — age effects,
within-person change, or trajectories — and the contribution must **advance theory about development**.

This repository is opinionated. It is **not** a generic psychology-writing toolbox and it is **not** a
relabeled social-science pack. It is **Developmental Psychology-specific**: developmental-change designs
(cross-sectional, longitudinal/cohort, accelerated, micro-genetic, experiment), the field's hard problems
(**age vs. cohort confounds, attrition, measurement invariance across ages, ethics with minors**),
change-modeling analysis (**growth-curve / multilevel / SEM, mediation/moderation**), **APA 7th edition +
JARS** reporting, the required **Public Significance Statement**, and the journal's **Transparency and
Openness Promotion (TOP)** open-science commitments.

**Official basis checked 2026-06.** Volatile specifics (editor, length tiers, abstract ceiling,
masked-review and TOP wording) are marked **待核实** in
[`resources/official-source-map.md`](resources/official-source-map.md). **Verify on the official page.**

---

## What Is Developmental Psychology, and Why a Dedicated Stack?

Its constraints differ sharply from a general empirical-psychology or a social-science journal:

| Constraint            | Developmental Psychology                                                        | Implication                                                       |
|-----------------------|--------------------------------------------------------------------------------|------------------------------------------------------------------|
| Core claim            | **Developmental change** — age effects, within-person change, trajectories       | A single-age correlation is not a fit                            |
| Designs               | Cross-sectional, **longitudinal/cohort**, accelerated, micro-genetic, experiment | Match the design to the change claim                             |
| Hard problems         | **Age vs. cohort**, **attrition**, **measurement invariance** across ages       | Test invariance before interpreting change                      |
| Analysis              | **Growth-curve / multilevel / SEM**, mediation/moderation, FIML/MI for attrition | Model change, don't snapshot it                                  |
| Reporting             | **APA 7th edition + JARS** (JARS-Quant / JARS-Qual / MARS)                       | Effect sizes + CIs; full disclosure                             |
| Front matter          | **Public Significance Statement** (2–3 sentences, ~30–70 words)                  | Lay-accessible relevance, no overclaim                          |
| Length                | Tiered: ~4,500 (brief) / ~10,500 (larger) / ~15,000 (multi-study/longitudinal)  | Pick the right tier (检索于 2026-06；以官网为准)                 |
| Ethics                | Consent **+ child assent**; vulnerable-population protections                    | Age-appropriate measures and data handling                      |
| Publisher / portal    | **APA** / **Editorial Manager** (`editorialmanager.com/dvl`); **masked review** | Anonymize the manuscript and the shared links                   |
| Transparency          | **TOP** — data-availability statement, DOIs, preregistration, sample-size justification | Plan deposits early; share minors' data via permission archives |

Developmental Psychology is the **broad APA lifespan-development** journal — distinct from **Child
Development** (SRCD), **Developmental Science**, and **JPSP**. Unverified items are marked **待核实** in
[`resources/official-source-map.md`](resources/official-source-map.md).

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/developmental-psychology-skills
/plugin install developmental-psychology-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/developmental-psychology-skills.git
cd developmental-psychology-skills

mkdir -p ~/.claude/skills && cp -R skills/devpsych-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/devpsych-* ~/.codex/skills/
```

### First Prompt

```
Use devpsych-workflow to tell me which skill I should use next for my Developmental Psychology manuscript.
```

---

## Default Workflow

```text
devpsych-topic-selection
        ▼
devpsych-theory-and-hypotheses
        ▼
devpsych-literature-positioning
        ▼
devpsych-study-design          (preregister + plan invariance/attrition here)
        ▼
devpsych-data-analysis
        ▼
devpsych-tables-figures
        ▼
devpsych-writing-style          (APA 7th + Public Significance Statement)
        ▼
devpsych-open-science-and-transparency
        ▼
devpsych-review-process
        ▼
devpsych-submission
        ▼
devpsych-rebuttal
```

`devpsych-workflow` is the router. If your design is **prospective and confirmatory**, route to
`devpsych-study-design` and `devpsych-open-science-and-transparency` early so a preregistration and a
sample-size justification exist before data collection.

---

## Skills

| Skill                                    | Purpose                                                                       |
|------------------------------------------|-------------------------------------------------------------------------------|
| `devpsych-workflow`                      | Router — decides which sub-skill to invoke next                               |
| `devpsych-topic-selection`               | Fit test: is the contribution about developmental change? Length tier         |
| `devpsych-theory-and-hypotheses`         | Developmental theory + age-graded, directional hypotheses; confirmatory split |
| `devpsych-literature-positioning`        | Stake a developmental gap (change/age/mechanism) and the contribution         |
| `devpsych-study-design`                  | Age vs. cohort, attrition, measurement invariance, power, ethics with minors  |
| `devpsych-data-analysis`                 | Growth-curve/multilevel/SEM, invariance, mediation/moderation, effect sizes   |
| `devpsych-tables-figures`                | APA 7th exhibits that show change over age (trajectories, CIs)                 |
| `devpsych-writing-style`                 | APA 7th + JARS; length tiers; the Public Significance Statement                |
| `devpsych-open-science-and-transparency` | TOP: data-availability statement, DOIs, preregistration, minors' data         |
| `devpsych-review-process`                | Masked review; developmental-credibility and transparency as graded factors   |
| `devpsych-submission`                    | Editorial Manager preflight (tier, abstract, masking, invariance, TOP)        |
| `devpsych-rebuttal`                      | R&R response-letter strategy (invariance/attrition/disclosure requests)       |

### Resources

- [`resources/external_tools.md`](resources/external_tools.md) — preregistration (OSF), repositories (OSF/ICPSR/Databrary/Dataverse/Zenodo), developmental data archives, power simulation, growth/SEM/invariance/missing-data packages, `papaja`
- [`resources/official-source-map.md`](resources/official-source-map.md) — official APA URLs behind every fact, with 待核实 markers
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — a before→after Developmental Psychology Introduction (fictional)
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — verified Developmental Psychology papers by method × developmental domain

---

## Differences vs. Sibling Journals

| Dimension          | Developmental Psychology (APA)          | Child Development (SRCD)            | Developmental Science (Wiley)        | JPSP (APA)                       |
|--------------------|-----------------------------------------|------------------------------------|--------------------------------------|----------------------------------|
| Core remit         | Broad **lifespan** development          | Society flagship, **childhood**     | Often **infant/cognitive mechanism** | Personality / social processes   |
| Defining claim     | Developmental **change** + theory       | Child development + theory          | Mechanism of development             | Not a developmental-change claim |
| Typical format     | Tiered reports (brief→multi-study)      | Full empirical articles             | Often **brief**, fast                | Long empirical articles          |
| Best fit when      | Lifespan change, broad theory advance   | Child-focused, society-facing       | Short mechanism-focused finding      | Process not centered on age      |

---

## What This Repo Does Not Do

- It does not write a submittable manuscript for you
- It does not simulate any specific editor's or reviewer's taste
- It does not assert volatile metadata (current editor, exact length tiers, TOP wording) — verify on the official page; unverified items are marked 待核实
- It does not decide whether your finding is a credible developmental advance — that is the researcher's call

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [Developmental Psychology (APA)](https://www.apa.org/pubs/journals/dev/) — scope, submission guidelines, open-science policy
- [APA JARS](https://apastyle.apa.org/jars) — Journal Article Reporting Standards

---

## License

MIT
