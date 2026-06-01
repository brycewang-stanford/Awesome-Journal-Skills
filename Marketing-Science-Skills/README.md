# Marketing Science Skills

<p align="center">
  <img src="assets/cover.svg" alt="Marketing Science cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Marketing%20Science-1b3a6b)](https://pubsonline.informs.org/journal/mksc)
[![Publisher](https://img.shields.io/badge/INFORMS-ISMS-1f6feb)](https://pubsonline.informs.org/journal/mksc)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **Marketing Science** — the flagship *quantitative-marketing* journal of the **INFORMS Society for Marketing Science (ISMS)**, published by INFORMS.

This repository is opinionated. It is **not** a generic "marketing writing" toolbox, and it is **not** a consumer-behavior (JCR-style) experiments pack. It is a **Marketing Science-specific** stack built around the journal's defining bar: work that **answers an important marketing question using mathematical modeling**. The dominant published genres are **structural econometric models** and **analytical (game-theoretic) models**; econometrics, statistics, machine learning, surveys, and experiments are welcome only when rigorously tied to a formal model. It covers modeling-driven topic selection, model and identification development, literature positioning, structural/analytical methods, estimation and counterfactual analysis, contribution framing, INFORMS house-style exhibits and prose, ScholarOne submission, the double-anonymous review process, and multi-round R&R rebuttals.

> Durable norms only. Editors, fees, exact word limits, and policies change — always verify on the official Marketing Science submission pages, the Replication and Disclosure Policy, and the INFORMS Author Portal.

---

## Why a Separate Marketing Science Skill Stack?

Marketing Science imposes constraints that differ materially from behavior-first marketing journals (e.g., JCR) and from archival accounting/finance journals:

| Constraint              | Marketing Science                                                  | Implication                                                    |
|-------------------------|--------------------------------------------------------------------|----------------------------------------------------------------|
| Discipline              | Quantitative marketing (INFORMS / ISMS), not a marketing-association journal | OR/analytics lineage; formal-model rigor is the bar     |
| Core bar                | Answer an important marketing question **using mathematical modeling** | Pure conceptual or scale-validation papers are off-fit     |
| Dominant genres         | Structural econometrics; analytical / game-theoretic models        | Even empirical/behavioral work must connect to a formal model  |
| Identification          | Demand/supply structure, equilibrium, instruments, exclusion logic | "Reduced-form correlation, no model" reads as off-venue        |
| Analysis                | GMM/MLE/SMM estimation, counterfactuals, comparative statics       | A regression table without a model or policy experiment is thin |
| Review                  | **Double-anonymous**; strict author-blinding for regular submissions | Single-blind habits from economics outlets do not apply      |
| Transparency            | Mandatory **data + estimation code** deposit on acceptance         | Plan replication-ready code from day one                       |
| Format                  | INFORMS style; author-year cites; LaTeX/Word; succinct main text   | Verify current limits; Frontiers is a strict 6,000-word cap    |
| Process                 | ScholarOne; Senior-Editor / Associate-Editor routing; multi-round R&R | First-round accepts are essentially unheard of              |

Generic "scientific writing," consumer-behavior, or "social-science methods" packs do not address these constraints.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/mksc-skills
/plugin install mksc-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/mksc-skills.git
cd mksc-skills

mkdir -p ~/.claude/skills && cp -R skills/mksc-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/mksc-* ~/.codex/skills/
```

### First Prompt

```
Use mksc-workflow to tell me which skill I should use next for my Marketing Science manuscript.
```

---

## Default Workflow

```text
mksc-topic-selection
        ▼
mksc-theory-development      (model + identification)
        ▼
mksc-literature-positioning
        ▼
mksc-methods                 (structural / analytical)
        ▼
mksc-data-analysis           (estimation + counterfactuals)
        ▼
mksc-contribution-framing
        ▼
mksc-tables-figures
        ▼
mksc-writing-style           (polish)
        ▼
mksc-submission
        ▼
mksc-review-process
        ▼
mksc-rebuttal
```

`mksc-workflow` is the router — it tells you which skill to use next based on where you are.

---

## Skills

| Skill                        | Purpose                                                                            |
|------------------------------|------------------------------------------------------------------------------------|
| `mksc-workflow`              | Router — decides which sub-skill to invoke next                                     |
| `mksc-topic-selection`       | Modeling-driven question + Marketing Science fit test (vs. JCR/JMR/Management Science) |
| `mksc-theory-development`    | Build the analytical/structural model; identification and equilibrium logic        |
| `mksc-literature-positioning`| Join a modeling conversation; position vs. structural/analytical precedents         |
| `mksc-methods`               | Choose structural vs. analytical vs. causal-ML approach; specify the estimable model |
| `mksc-data-analysis`         | Estimation (GMM/MLE/SMM/Bayes), model fit, counterfactuals, robustness              |
| `mksc-contribution-framing`  | Explicit substantive + methodological/modeling contribution statement              |
| `mksc-tables-figures`        | Estimates, fit, comparative statics, and counterfactual exhibits in INFORMS style  |
| `mksc-writing-style`         | Front-loaded model intuition, INFORMS author-year style, succinct prose            |
| `mksc-submission`            | ScholarOne preflight; blinding, format, replication package, track choice          |
| `mksc-review-process`        | How double-anonymous SE/AE review and decisions work; reading a decision letter    |
| `mksc-rebuttal`              | Multi-round R&R revision and point-by-point response letter                         |

### Resources

- [`resources/external_tools.md`](resources/external_tools.md) — quantitative-marketing data sources (NielsenIQ/Kilts, Circana/IRI, scanner & clickstream, Compustat/CRSP) and modeling/estimation software (pyBLP, MATLAB/Julia, Stan/PyMC, Gurobi, econml)
- [`resources/official-source-map.md`](resources/official-source-map.md) — every venue fact mapped to an official INFORMS URL (accessed 2026-06-01); unverified items flagged 待核实

---

## Differences vs. JCR / JMR / Management Science

| Dimension          | Marketing Science                       | JCR                              | JMR                                  | Management Science                   |
|--------------------|------------------------------------------|----------------------------------|--------------------------------------|--------------------------------------|
| Core contribution  | Marketing question via **mathematical modeling** | Consumer-behavior theory      | Broad (modeling + behavioral + methods) | OR/management science, multi-area    |
| Signature methods  | Structural econometrics; analytical/game theory | Lab/field experiments        | Mixed (modeling and experiments)     | Optimization, stochastic models, econometrics |
| Editorial structure| Senior Editors + Associate Editors       | Area/associate editors           | Area editors                         | Standing **departmental Area Editors** |
| Publisher          | INFORMS / ISMS                           | Oxford UP / ACR                  | American Marketing Association       | INFORMS                              |
| Best fit           | Modeling-core pricing/advertising/channels/analytics | Conceptual consumer psychology | Quant or behavioral marketing       | General management-science modeling  |

If your contribution is a consumer-psychology experiment with no formal model, JCR is the better fit; if it is general management science, target Management Science.

---

## Distinctive Marketing Science Norms

- **Modeling core with methodological pluralism** — empirical or behavioral contributions must connect to or advance a mathematical/quantitative model; structural and analytical work dominate.
- **Frontiers in Marketing Science** — a shorter, Science-like, faster-review track capped strictly at **6,000 words** (everything included), rewarding a major contribution on one primary dimension.
- **Mandatory replication deposit** — data and estimation code on acceptance, under the journal's field-leading Replication and Disclosure Policy.
- **Double-anonymous review** with strict author-blinding for regular submissions; single-blind only for Practice/Science-to-Practice tracks.
- **Specialized tracks** — Database papers, Practice Papers/Practice Prize (with a 500–1,000-word Impact Statement), and Science-to-Practice — reflecting the INFORMS analytics/practice orientation.

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — index of journal-specific skill packs

---

## License

MIT
