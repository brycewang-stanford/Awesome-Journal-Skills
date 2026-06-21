# Cognitive Psychology Skills

<p align="center">
  <img src="assets/cover.svg" alt="Cognitive Psychology cover" width="200">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Cognitive%20Psychology-6a2a6a)](https://www.sciencedirect.com/journal/cognitive-psychology)
[![Field](https://img.shields.io/badge/field-Cognitive%20Science-1f6feb)](https://www.sciencedirect.com/journal/cognitive-psychology)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **Cognitive Psychology** (Elsevier) — a leading journal
of **cognitive science**, covering attention, perception, memory, learning, language, categorization,
reasoning, problem-solving, and judgment and decision-making. Cognitive Psychology is distinctive for
publishing **longer, integrative, model-driven** papers: it favors **multi-experiment programs that
combine tightly controlled cognitive experiments with formal computational or mathematical modeling**,
developing and testing theories of cognition through the experiment-to-model-fit loop.

This repository is opinionated. It is **not** a generic psychology-writing toolbox and it is **not** a
relabeled short-report pack. It is **Cognitive Psychology-specific**: a contribution shape built around
a **formal model that is fit and compared**, a **multi-experiment program** where each study adds
inference, **model comparison with parameter/model recovery**, and **reproducible model code** deposited
alongside the data. Submission is via **Elsevier Editorial Manager**.

---

## What Is Cognitive Psychology, and Why a Dedicated Stack?

Its constraints differ sharply from a short-report or a purely empirical social-science journal:

| Constraint            | Cognitive Psychology                                                            | Implication                                                       |
|-----------------------|--------------------------------------------------------------------------------|------------------------------------------------------------------|
| Contribution shape    | **Longer, integrative, model-driven** article (multi-experiment + formal model) | A single isolated effect is the wrong shape                       |
| Theory                | A **formal/computational model** with interpretable parameters                  | Verbal-only theory or "just a curve fit" is punished             |
| Design                | Experiments engineered to **discriminate competing models**                     | A design both rivals predict equally wastes the experiment       |
| Analysis              | **Model fitting + comparison** (AIC/BIC/Bayes factors) + **recovery**           | A single fit with no rival/recovery is not persuasive            |
| Hierarchy             | **(G)LMMs / hierarchical Bayesian** over crossed subject/item variance          | Aggregating to cell means inflates false positives               |
| Exhibits              | Figures **overlay model fit on data**; a model-comparison table                 | Bars of means hide what the venue cares about                    |
| Publisher / portal    | **Elsevier** / **Editorial Manager**                                            | Complete the Elsevier research-data + competing-interest declarations |
| Open science          | Share **data + model/analysis code + materials**; fits regenerate from code     | Code transparency is the venue-specific must                      |

Volatile specifics (current editor, review model, length guidance, abstract limit, data/code policy
wording, accepted article types) change — items not directly confirmed are marked **待核实** in
[`resources/official-source-map.md`](resources/official-source-map.md). **Verify on the official page.**

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/cognitive-psychology-skills
/plugin install cognitive-psychology-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/cognitive-psychology-skills.git
cd cognitive-psychology-skills

mkdir -p ~/.claude/skills && cp -R skills/cogpsych-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/cogpsych-* ~/.codex/skills/
```

### First Prompt

```
Use cogpsych-workflow to tell me which skill I should use next for my Cognitive Psychology manuscript.
```

---

## Default Workflow

```text
cogpsych-topic-selection
        ▼
cogpsych-theory-and-hypotheses    (formalize the model + rival first)
        ▼
cogpsych-literature-positioning
        ▼
cogpsych-study-design             (design experiments to discriminate models)
        ▼
cogpsych-data-analysis            (fit + compare + recover)
        ▼
cogpsych-tables-figures           (overlay model fit on data)
        ▼
cogpsych-writing-style            (integrate the program into one argument)
        ▼
cogpsych-open-science-and-transparency
        ▼
cogpsych-review-process
        ▼
cogpsych-submission
        ▼
cogpsych-rebuttal
```

`cogpsych-workflow` is the router. Because the **model is the contribution**, formalize theory before
positioning, and co-design experiments with the model — iterate `cogpsych-theory-and-hypotheses` ↔
`cogpsych-study-design`.

---

## Skills

| Skill                                    | Purpose                                                                      |
|------------------------------------------|------------------------------------------------------------------------------|
| `cogpsych-workflow`                      | Router — decides which sub-skill to invoke next                              |
| `cogpsych-topic-selection`               | Model-driven fit; multi-experiment vs. experiment-plus-model vs. review      |
| `cogpsych-theory-and-hypotheses`         | Formalize the model + rival; derive the discriminating prediction           |
| `cogpsych-literature-positioning`        | Position against rival models, not a chronology                             |
| `cogpsych-study-design`                  | Confound control, counterbalancing, power for the critical contrast          |
| `cogpsych-data-analysis`                 | Model fitting + comparison (AIC/BIC/BF) + recovery; mixed/hierarchical       |
| `cogpsych-tables-figures`                | Exhibits that overlay model fit on data; the comparison table               |
| `cogpsych-writing-style`                 | Weave a multi-experiment program + model into one argument                   |
| `cogpsych-open-science-and-transparency` | Open data + model/analysis code + materials; reproducible fits, DOIs         |
| `cogpsych-review-process`                | Editorial triage + expert modeling scrutiny; revision cycles                |
| `cogpsych-submission`                    | Editorial Manager preflight (shape, modeling, code, declarations)           |
| `cogpsych-rebuttal`                      | Revision response strategy for added experiments/model comparisons           |

### Resources

- [`resources/external_tools.md`](resources/external_tools.md) — modeling frameworks (Stan/JAGS/PyMC), model comparison (`loo`, Bayes factors), mixed models (`lme4`/`brms`), repositories (OSF/Mendeley Data/Zenodo), reproducibility tooling
- [`resources/official-source-map.md`](resources/official-source-map.md) — official Elsevier / ScienceDirect URLs behind every fact, with 待核实 markers
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — a before→after Introduction in the journal's model-driven house style (fictional)
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — real, web-verified _Cognitive Psychology_ papers by topic × method, with a sibling-journal omission guard

---

## Differences vs. Sibling Journals

| Journal | What it wants | How this pack differs |
|---------|---------------|------------------------|
| **Cognitive Psychology** (this pack) | Long, integrative, **model-driven** multi-experiment programs | Centered on the experiment-to-model-fit loop, model comparison + recovery, code transparency |
| **Cognition** (Elsevier) | Broader, more effect-/phenomenon-led cognitive science | Cognition takes shorter, phenomenon-first papers; bring the model-driven program here |
| **JEP: General** (APA) | High-impact experimental cognition | Cognitive Psychology leans harder into formal modeling + the multi-experiment program |
| **Psychological Science** (APS/SAGE) | Short, single-finding reports (≤ 2,000-word core) | Opposite length/ambition; one effect is wrong-shape here |
| **Journal of Memory and Language** (Elsevier) | Narrower-scope memory/language work | Bring the integrative, model-driven contribution to Cognitive Psychology |

---

## What This Repo Does Not Do

- It does not write a submittable manuscript for you
- It does not simulate any specific editor's or reviewer's taste
- It does not assert volatile metadata (current editor, review model, length guidance, data/code policy wording) — verify on the official page; unverified items are marked 待核实
- It does not decide whether your model is a genuine theoretical advance — that is the researcher's call

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [Cognitive Psychology (Elsevier / ScienceDirect)](https://www.sciencedirect.com/journal/cognitive-psychology) — scope, guide for authors, submission
- [Cognitive Psychology — Guide for Authors](https://www.sciencedirect.com/journal/cognitive-psychology/publish/guide-for-authors) — submission, data/code policy, declarations

---

## License

MIT
