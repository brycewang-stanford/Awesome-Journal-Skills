# Journal of Marketing Research (JMR) Skills

<p align="center">
  <img src="assets/cover.svg" alt="Journal of Marketing Research cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-JMR-9b1b30)](https://www.ama.org/journal-of-marketing-research/)
[![Index](https://img.shields.io/badge/index-FT50%20%7C%20UTD24-1f6feb)](https://www.ama.org/journal-of-marketing-research/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at the **Journal of Marketing Research (JMR)** — the American Marketing Association's (AMA) methods- and modeling-forward flagship, published by SAGE.

This repository is opinionated. It is **not** a generic "marketing writing" toolbox. It is a **JMR-specific** stack built around JMR's defining identity: a **dual bar** that demands both methodological rigor *and* a substantive/theoretical contribution, across a journal that deliberately spans **behavioral experiments** (lab and field) and **econometric/structural marketing-science modeling** in one venue. It covers topic selection, theory development, literature positioning, identification-aware design and analysis, exact-statistics reporting, contribution framing, AMA/SAGE house-style exhibits, the **50-page page limit** with its **'W'-prefixed Web Appendix**, ScholarOne submission, the **double-anonymized** review process, and multi-round R&R rebuttals.

> Durable norms only. Editors, fees, the exact page limit, and policies change — always verify on the SAGE author instructions and the AMA submission-guidelines page. **Editor transition:** Rebecca Hamilton (Georgetown) is EIC through 30 June 2026; Raphael Thomadsen's incoming team (Washington University in St. Louis, 2026–2029) has processed new manuscripts since 1 April 2026.

---

## Why a Separate JMR Skill Stack?

JMR imposes constraints that differ materially from theory-only management journals or archival accounting/finance journals:

| Constraint              | Journal of Marketing Research                                            | Implication                                                       |
|-------------------------|--------------------------------------------------------------------------|------------------------------------------------------------------|
| Discipline              | Full spectrum of marketing, methods- and modeling-forward                | Purely managerial framing belongs at *Journal of Marketing*       |
| Methodological span     | Behavioral experiments **and** econometric/structural modeling in one venue | The stack must serve both genres, not one                      |
| Core bar                | **Dual bar**: methodological rigor **and** substantive/theoretical contribution | Clever method with no insight, or insight with weak ID, fails |
| Statistics reporting    | **Exact p-values (3 digits), standard errors, effect sizes** mandated     | Asterisks / "p<.05" / no SEs are non-conforming                  |
| Length                  | **50-page** all-inclusive print limit (Web Appendix excluded)             | Push supplementary analyses into the unlimited Web Appendix       |
| Web Appendix            | First-class artifact: separate PDF, **'W'-prefixed** tables/figures        | Replication-enabling material lives there, labeled "Table W1"      |
| Transparency            | AMA Research Transparency Policy; **Data Availability Statement** on title page | Be ready to share code, instruments, materials on request     |
| Review                  | **Double-anonymized**; two independent reviews to reach Revise/Accept      | Anonymize fully; first-round accepts are essentially unheard of   |
| Citation style          | **AMA author-year** ("Thorelli 1960"), no reference cap                    | Not APA-numeric; configure your reference manager to AMA          |

Generic "scientific writing" or "social-science methods" packs do not address these constraints.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/jmr-skills
/plugin install jmr-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/jmr-skills.git
cd jmr-skills

mkdir -p ~/.claude/skills && cp -R skills/jmr-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/jmr-* ~/.codex/skills/
```

### First Prompt

```
Use jmr-workflow to tell me which skill I should use next for my JMR manuscript.
```

---

## Default Workflow

```text
jmr-topic-selection
        ▼
jmr-theory-development
        ▼
jmr-literature-positioning
        ▼
jmr-methods
        ▼
jmr-data-analysis
        ▼
jmr-contribution-framing
        ▼
jmr-tables-figures
        ▼
jmr-writing-style        (polish)
        ▼
jmr-submission
        ▼
jmr-review-process
        ▼
jmr-rebuttal
```

`jmr-workflow` is the router — it tells you which skill to use next based on where you are, and on whether your paper is a **behavioral**, **modeling/econometric**, or **methods** contribution.

---

## Skills

| Skill                        | Purpose                                                                            |
|------------------------------|------------------------------------------------------------------------------------|
| `jmr-workflow`               | Router — decides which sub-skill to invoke next; classifies behavioral vs. modeling vs. methods |
| `jmr-topic-selection`        | Marketing question + JMR fit test (vs. *Journal of Marketing* / *Marketing Science* / *JCR*) |
| `jmr-theory-development`     | Behavioral hypotheses with process evidence, or a modeling primitive / econometric mechanism |
| `jmr-literature-positioning` | Joining the marketing conversation; positioning across behavioral and modeling streams |
| `jmr-methods`                | Experimental design (lab/field) or identification strategy (IV/DiD/structural) matched to the claim |
| `jmr-data-analysis`          | Exact p-values, standard errors, effect sizes; the right estimator; replication-ready analysis |
| `jmr-contribution-framing`   | Clearing the dual bar — substantive insight plus methodological contribution        |
| `jmr-tables-figures`         | AMA-style exhibits; main-text vs. 'W'-prefixed Web Appendix tables/figures          |
| `jmr-writing-style`          | Third-person abstract, AMA author-year style, exact-statistics prose conventions    |
| `jmr-submission`             | ScholarOne preflight: 50-page limit, Web Appendix PDF, Data Availability Statement, anonymization |
| `jmr-review-process`         | How JMR's double-anonymized, Coeditor-routed, two-review process works              |
| `jmr-rebuttal`               | Multi-round R&R revision and point-by-point response letter                         |

### Resources

- [`skills/jmr-submission/templates/checklist.md`](skills/jmr-submission/templates/checklist.md) — pre-submission self-check (50-page limit, Web Appendix, exact statistics, anonymization)
- [`resources/external_tools.md`](resources/external_tools.md) — behavioral tools (Qualtrics / Prolific / PROCESS / G*Power) and modeling tools (NielsenIQ-IRI scanner data / Stata reghdfe / R bayesm / Stan / BLP-style demand)
- [`resources/official-source-map.md`](resources/official-source-map.md) — official AMA/SAGE URLs behind every verified fact (accessed 2026-06-01)

---

## Differences vs. *Journal of Marketing* / *Marketing Science* / *JCR*

| Dimension          | JMR                                       | Journal of Marketing (JM)     | Marketing Science            | Journal of Consumer Research (JCR) |
|--------------------|-------------------------------------------|-------------------------------|------------------------------|------------------------------------|
| Framing            | Methods- and modeling-forward             | Managerial / substantive      | Quantitative marketing science | Consumer behavior, interdisciplinary |
| Methods            | Experiments **and** modeling in one venue | Often empirical + managerial  | Modeling / analytical / econometric | Primarily behavioral experiments |
| Core bar           | Dual: rigor **and** substantive insight   | Managerial relevance + theory | Modeling contribution         | Consumer insight + theory          |
| Best fit           | Rigorous marketing findings or methods    | Manager-facing implications   | Structural / analytical models | Deep consumer-behavior theory      |

If your paper is purely manager-facing with light method, consider *Journal of Marketing*; a pure analytical model may fit *Marketing Science*; a deep consumer-psychology paper may fit *JCR*.

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — index of journal-specific skill packs
- [Academy-of-Management-Journal-Skills](https://github.com/brycewang-stanford) — Academy of Management Journal (AMJ)

---

## License

MIT
