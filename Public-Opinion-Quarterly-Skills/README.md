# Public Opinion Quarterly Skills

<p align="center">
  <img src="assets/cover.svg" alt="Public Opinion Quarterly cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-POQ-5a3a8c)](https://academic.oup.com/poq)
[![Field](https://img.shields.io/badge/field-Public%20Opinion%20%26%20Survey%20Methodology-1f6feb)](https://academic.oup.com/poq/pages/About)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **Public Opinion Quarterly (POQ)** — the leading journal
of **public opinion and survey research**, **published since 1937**, published by **Oxford University
Press** as an **official journal of the American Association for Public Opinion Research (AAPOR)**. POQ
selectively publishes important and innovative work on **opinion and communication theory**, **analyses
of current public opinion**, and **methodological issues in survey validity** — questionnaire
construction, interviewing, sampling strategy, mode of administration, nonresponse, and weighting.

This repository is opinionated. It is **not** a generic social-science writing toolbox and it is
**not** an economics pack repurposed for surveys. It is a **POQ-specific** stack built on the spine of
**survey science**: a contribution framed in **Total Survey Error**, a design defensible on coverage /
sampling / nonresponse / measurement / mode / weighting, **AAPOR-standard methodological disclosure**
in an **Appendix A: Disclosure Elements**, **double-blind** preparation, and a **replication package**
deposited to **POQ's Dataverse on Harvard Dataverse** that reproduces every table and figure.

---

## What Is POQ, and Why a Dedicated Stack?

POQ's constraints differ from a general social-science journal or a pure methods journal:

| Constraint            | POQ                                                                           | Implication                                                       |
|-----------------------|-------------------------------------------------------------------------------|------------------------------------------------------------------|
| Scope                 | **Public opinion + survey methodology** (and communication, behavior)         | The paper must contribute to opinion or to survey validity       |
| Premium on            | **Survey rigor** framed in **Total Survey Error**                             | A naive survey analysis with no error framing is off-fit         |
| Disclosure            | **AAPOR-standard disclosure** in **Appendix A: Disclosure Elements**          | Report exact wording, sampling, weighting, and response rates    |
| Response rates        | Computed **per AAPOR Standard Definitions** (RR1–RR6), with the calculation shown | A bare percentage is not enough                              |
| Publisher / affiliate | **Oxford University Press** / **AAPOR**                                        | Submitted via **ScholarOne Manuscripts**                         |
| Review model          | **Double-blind**, typically 2–3 referees                                      | Anonymize the manuscript; the AE may request code/data in review |
| Length                | **Article ≤ 6,500**; **Note < 3,000**; **Polls in Context ≤ 2,500** words     | Caps count text + notes; figures/tables/appendices excluded      |
| Transparency          | **Replication package to POQ's Harvard Dataverse**, archived before typesetting | Build it as you go; it must reproduce every table and figure   |
| Data statement        | **Data Availability Statement** required in the endmatter                     | Plan the DAS and any embargo / restricted-data path              |

Volatile specifics (editors and term, exact caps, section names, fee/APC, embargo, policy wording)
change — items not directly confirmed are marked **待核实** in
[`resources/official-source-map.md`](resources/official-source-map.md).
**Verify on the official journal page.**

### Five submission types

- **Original Articles** — full studies, **≤ 6,500 words** of text and notes; the journal's main format.
- **Research Notes** — single findings, important extensions, or replications, **< 3,000 words**.
- **Polls in Context** — short, timely interpretation of current poll data, **≤ 2,500 words** (section
  naming — historical "The Polls — Trends / Review" vs. current "Poll Trends" / "Polls in Context" —
  is 待核实).
- **Research Syntheses** — integrative reviews of a literature, **≤ 6,500 words** (incl. notes).
- **Book Reviews** — brief assessments of a recent relevant book, **~1,200 words**.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/poq-skills
/plugin install poq-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/poq-skills.git
cd poq-skills

mkdir -p ~/.claude/skills && cp -R skills/poq-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/poq-* ~/.codex/skills/
```

### First Prompt

```
Use poq-workflow to tell me which skill I should use next for my POQ manuscript.
```

---

## Default Workflow

```text
poq-topic-selection
        ▼
poq-literature-positioning
        ▼
poq-theory-and-hypotheses
        ▼
poq-survey-design-and-measurement
        ▼
poq-data-analysis
        ▼
poq-tables-figures
        ▼
poq-writing-style          (polish)
        ▼
poq-transparency-and-data-policy
        ▼
poq-review-process
        ▼
poq-submission
        ▼
poq-rebuttal
```

`poq-workflow` is the router — it tells you which skill to use next based on where you are. Whatever
the submission type, route early to `poq-survey-design-and-measurement` to lock the **Total Survey
Error** framing and start the **Appendix A: Disclosure Elements** before you write — disclosure is a
gate, not an afterthought.

---

## Skills

| Skill                                | Purpose                                                                       |
|--------------------------------------|-------------------------------------------------------------------------------|
| `poq-workflow`                       | Router — decides which sub-skill to invoke next                               |
| `poq-topic-selection`                | Opinion vs. survey-validity contribution; pick the right submission type      |
| `poq-literature-positioning`         | Engage the opinion debate *and* the survey-methods lineage                    |
| `poq-theory-and-hypotheses`          | Constructs, mechanisms, and falsifiable hypotheses (substantive or methods)   |
| `poq-survey-design-and-measurement`  | Total Survey Error: coverage, sampling, nonresponse, measurement, mode, weighting |
| `poq-data-analysis`                  | Design-based inference (weights/strata/clusters), uncertainty, robustness     |
| `poq-tables-figures`                 | Self-contained exhibits with design-based uncertainty and base N              |
| `poq-writing-style`                  | Reach the POQ audience within the type cap; name the methodological move       |
| `poq-transparency-and-data-policy`   | Appendix A disclosure; POQ Dataverse replication package; Data Availability Statement |
| `poq-review-process`                 | Double-blind review, 2–3 referees, AAPOR-disclosure bar, AE code/data requests |
| `poq-submission`                     | ScholarOne preflight (anonymization, word cap, Appendix A, DAS, package)      |
| `poq-rebuttal`                       | R&R response-letter strategy for survey-methodologist referees + AE           |

### Resources

- [`resources/external_tools.md`](resources/external_tools.md) — survey data sources (ANES / GSS / CES / Pew / Eurobarometer / ESS) + complex-survey, weighting, measurement, and pretesting tooling
- [`resources/official-source-map.md`](resources/official-source-map.md) — official OUP / AAPOR URLs behind every fact, with 待核实 markers on unverified items

---

## What This Repo Does Not Do

- It does not write a submittable manuscript for you
- It does not simulate any specific editor's or referee's taste
- It does not assert volatile metadata (current editors and term, exact caps, section names, fee/APC, policy wording) — verify on the official page; unverified items are marked 待核实
- It does not decide whether your contribution is to opinion or to survey validity — that is the researcher's call

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [Public Opinion Quarterly (Oxford Academic)](https://academic.oup.com/poq) — publisher home
- [American Association for Public Opinion Research (AAPOR)](https://aapor.org/) — owner/affiliate, Transparency Initiative, Standard Definitions

---

## License

MIT
