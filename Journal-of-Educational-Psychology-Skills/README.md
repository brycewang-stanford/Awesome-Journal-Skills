# Journal of Educational Psychology Skills

<p align="center">
  <img src="assets/cover.svg" alt="Journal of Educational Psychology cover" width="200">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Journal%20of%20Educational%20Psychology-8a5a12)](https://www.apa.org/pubs/journals/edu)
[![Field](https://img.shields.io/badge/field-Educational%20Psychology-1f6feb)](https://www.apa.org/pubs/journals/edu)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at the **Journal of Educational Psychology** (JEP) — the
**American Psychological Association's flagship outlet for original, primary psychological research on
education**, founded in **1910** and published by the **APA** (8 issues/year). JEP publishes rigorous
psychological research on **learning and instruction across all ages and educational levels** —
motivation and engagement, achievement, reading/math/science learning, assessment, self-regulation, and
interventions in real educational settings (school, classroom, online).

This repository is opinionated. It is **not** a generic education-writing toolbox and it is **not** a
relabeled social-science pack. It is **JEP-specific**: an **educational-relevance + psychological-theory**
scope bar, **classroom/school designs** (cluster-randomized trials, nesting, cluster-level power,
measurement of learning constructs, ecological validity), **multilevel/SEM/growth analysis** with
educationally meaningful effect sizes, **masked review**, **APA 7th edition** within a **12,000-word**
format, and APA's transparency regime — a **Transparency and Openness** subsection, **JARS** reporting,
and encouraged preregistration.

---

## What Is the Journal of Educational Psychology, and Why a Dedicated Stack?

Its constraints differ from both a general-psychology journal and a long-format education journal:

| Constraint            | Journal of Educational Psychology                                              | Implication                                                       |
|-----------------------|--------------------------------------------------------------------------------|------------------------------------------------------------------|
| Scope                 | **Original, primary psychological research on learning/instruction**; occasional **exceptionally important** meta-analyses | Need a learning mechanism *and* an educational implication |
| Out of scope          | Reliability/validity studies of a single test/instrument                       | Measurement-only papers go elsewhere                            |
| Design                | Students **nested** in classes/schools; field trials, quasi-experiments, longitudinal | Power and analyze at the **level of randomization** |
| Analysis              | **Multilevel / SEM / growth** models; effect sizes + CIs; mechanism tests       | Single-level OLS on clustered data is a routine reject          |
| Length                | Generally **≤ 12,000 words** (excl. refs/tables/figures/appendices)             | Full-length, but earn it; not a survey                          |
| Abstract              | **≤ 250 words**                                                                 | Concise, content-bearing                                        |
| Style                 | **APA 7th edition**, double-spaced                                              | Effect sizes + CIs in reporting                                 |
| Review                | **Masked** (author + reviewer identities masked)                               | Scrub names, grant numbers, sites, first-person self-cites      |
| Publisher / portal    | **APA** / **Editorial Manager** (`editorialmanager.com/edu`)                    | No submission fee (free peer review)                            |
| Transparency          | **Transparency and Openness** subsection (data + materials + code + DOIs)       | Prepare deposits and identifiers early                          |
| Standards             | **JARS / JARS-REC**; **preregistration encouraged**; **Open Science Badges**    | Walk the reporting standards for your design                    |

Volatile specifics (editor, exact word/abstract numbers, transparency wording) change — items not directly
confirmed are marked **待核实** in
[`resources/official-source-map.md`](resources/official-source-map.md). **Official basis checked 2026-06;
verify on the official page.**

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/journal-of-educational-psychology-skills
/plugin install journal-of-educational-psychology-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/journal-of-educational-psychology-skills.git
cd journal-of-educational-psychology-skills

mkdir -p ~/.claude/skills && cp -R skills/jedpsych-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/jedpsych-* ~/.codex/skills/
```

### First Prompt

```
Use jedpsych-workflow to tell me which skill I should use next for my Journal of Educational Psychology manuscript.
```

---

## Default Workflow

```text
jedpsych-topic-selection
        ▼
jedpsych-theory-and-hypotheses
        ▼
jedpsych-literature-positioning
        ▼
jedpsych-study-design          (nesting + cluster-level power; preregister if prospective)
        ▼
jedpsych-data-analysis         (multilevel/SEM/growth; effect sizes + CIs; mechanism)
        ▼
jedpsych-tables-figures
        ▼
jedpsych-writing-style          (fit 12,000 words, APA 7th, masked)
        ▼
jedpsych-open-science-and-transparency
        ▼
jedpsych-review-process
        ▼
jedpsych-submission
        ▼
jedpsych-rebuttal
```

`jedpsych-workflow` is the router. For a **prospective cluster-randomized trial**, route to
`jedpsych-study-design` and `jedpsych-review-process` early — power for nesting and an analysis plan
belong *before* schools are recruited.

---

## Skills

| Skill                                  | Purpose                                                                       |
|----------------------------------------|-------------------------------------------------------------------------------|
| `jedpsych-workflow`                    | Router — decides which sub-skill to invoke next                               |
| `jedpsych-topic-selection`             | Educational-relevance + theory fit; choose the manuscript type                 |
| `jedpsych-theory-and-hypotheses`       | State the learning mechanism and confirmatory vs. exploratory hypotheses       |
| `jedpsych-literature-positioning`      | Position a precise advance against the closest prior work                      |
| `jedpsych-study-design`                | Nesting, cluster-level power, measurement of learning constructs, ecology      |
| `jedpsych-data-analysis`               | Multilevel/SEM/growth, effect sizes + CIs, mechanism, JARS disclosure         |
| `jedpsych-tables-figures`              | APA 7th exhibits for model results, mediation, and growth; anonymized          |
| `jedpsych-writing-style`               | APA 7th within the 12,000-word format; the 250-word abstract; masking          |
| `jedpsych-open-science-and-transparency` | Transparency and Openness subsection, JARS, preregistration, DOIs            |
| `jedpsych-review-process`              | Masked review; educational relevance, rigor, and transparency as factors       |
| `jedpsych-submission`                  | Editorial Manager preflight (format, masking, transparency, JARS)              |
| `jedpsych-rebuttal`                    | R&R response-letter strategy for multiple reviewers + handling editor          |

### Resources

- [`resources/external_tools.md`](resources/external_tools.md) — power for nested designs (PowerUpR/`simr`/Optimal Design), multilevel/SEM (`lme4`/`lavaan`/Mplus), preregistration (OSF/REES), repositories (OSF/ICPSR/Dataverse/Zenodo), JARS, `papaja`
- [`resources/code/`](resources/code/) — runnable R skeletons for cluster-design diagnostics, multilevel/growth models, mediation, and JARS-ready tables
- [`resources/official-source-map.md`](resources/official-source-map.md) — official APA URLs behind every fact, with 待核实 markers
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — a before→after JEP Introduction in house style (fictional)
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — real, web-verified JEP papers by method × topic, with a sibling-journal guard

---

## What This Repo Does Not Do

- It does not write a submittable manuscript for you
- It does not simulate any specific editor's or reviewer's taste
- It does not assert volatile metadata (current editor, exact word/abstract limits, transparency wording) — verify on the official page; unverified items are marked 待核实
- It does not decide whether your finding is educationally important and rigorous enough — that is the researcher's call

---

## Differences vs. Sibling Journals

| Journal | Owner | What it is | How JEP differs |
|---------|-------|------------|-----------------|
| **Journal of Educational Psychology (JEP)** | APA | **Primary psychological research** on learning/instruction | The APA educational-psychology flagship: theory + mechanism + rigorous nested design |
| American Educational Research Journal (AERJ) | AERA | Broad education research (incl. qualitative, policy, social context) | JEP is narrower: *psychological* research with a learning mechanism |
| Review of Educational Research (RER) | AERA | **Review/synthesis** only | JEP publishes primary research (meta-analyses only if exceptionally important) |
| Contemporary Educational Psychology (CEP) | Elsevier | Educational psychology, often measurement/scale development | JEP de-emphasizes single-instrument validation; mechanism-driven |
| Learning and Instruction | EARLI/Elsevier | Learning & instruction, strong European base | Overlapping scope; JEP is the APA flagship with APA house style |
| Psychological Science | APS/SAGE | Short, broad-interest empirical psychology | JEP is full-length and education-specific, not a short report |

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [Journal of Educational Psychology (APA)](https://www.apa.org/pubs/journals/edu) — owner, aims/scope, submission guidelines
- [APA Journal Article Reporting Standards (JARS)](https://apastyle.apa.org/jars) — required reporting standards

---

## License

MIT
