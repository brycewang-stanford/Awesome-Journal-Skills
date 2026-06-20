# Population and Development Review Skills

<p align="center">
  <img src="assets/cover.svg" alt="Population and Development Review cover" width="200">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-PDR-5a2a4a)](https://onlinelibrary.wiley.com/journal/17284457)
[![Field](https://img.shields.io/badge/field-Demography%20%2B%20Development-1f6feb)](https://popcouncil.org/population-and-development-review-journal/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **Population and Development Review (PDR)** — the quarterly
journal published by **Wiley** on behalf of the **Population Council**, founded in **1975**, at the
**intersection of demography and development**. PDR advances knowledge of the relationships between
**population and social, economic, and environmental change**, and provides a forum for **public policy**
on those relationships: fertility and family change, mortality and health, migration and urbanization,
ageing and population structure, and population and environment/climate. It publishes **empirical
demography**, **formal demography**, and the substantial **synthetic/conceptual essays** it is famous for.

This repository is opinionated. It is **not** a generic social-science writing toolbox, and it is **not**
a methods-forward demography pack repurposed for development. It is a **PDR-specific** stack: a genuine
**population-and-development** question of broad interest, an argument that speaks **across fields** (an
economist or an environmental scholar should care about your fertility paper), a design defended on
**demographic** terms with its **development meaning** made explicit, **double-anonymized** preparation,
and a **data availability statement** with **reproducible code** deposited in a FAIR repository.

---

## What Is PDR, and Why a Dedicated Stack?

PDR's constraints differ from a methods-forward demography or a development-economics journal:

| Constraint            | Population and Development Review                                                          | Implication                                                          |
|-----------------------|-------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Scope                 | **Population ↔ development** — fertility, mortality, migration, ageing, **environment**, policy | The paper must connect a population process to development, not just use the data |
| Premium on            | **Broad interest** + a clear contribution, incl. **synthetic/conceptual essays**          | A narrow estimate, or a pure framework with no payoff, is off-fit    |
| Methods               | Life tables, decomposition, event history, APC, projections, causal — **plus** conceptual synthesis | Pick the method that answers the population-and-development question |
| Publisher / owner     | **Wiley** (publisher) / **Population Council** (owner); founded **1975**                   | Submitted via **ScholarOne**; APA-style house referencing           |
| Review model          | **Double-anonymized** (≥2 referees), editorial/committee screen first, ~3-month decision   | Remove all co-author identifiers; reviewers and authors anonymous    |
| Submission format     | **Free Format** first round — references in any consistent style; APA applied at revision  | Don't over-format the first submission; keep it consistent           |
| Fees                  | **No author fees** — no submission fee, **no APC** under the standard model                | Budget nothing; an Online Open choice may carry a separate Wiley APC |
| Length                | Research Articles typically **~8,000–10,000 words**; Notes & Commentary short             | Treat as norms; confirm any portal cap on the author page           |
| Transparency          | **Data availability statement** + persistent IDs; ORCID; reproducible code                 | PDR hosts no repository — you deposit in a FAIR one                  |

Volatile specifics (current editors, exact abstract/length caps, portal link, fee/Online Open options,
policy wording) change — items not directly confirmed are marked **待核实** in
[`resources/official-source-map.md`](resources/official-source-map.md). **Verify on the official journal
page.**

### Article types

- **Research Article** — full original study or substantial synthetic essay; typically **~8,000–10,000 words**.
- **Notes & Commentary** — short, focused argument or response on a current population question.
- **Data & Perspectives** — a new dataset, indicator, or interpretation of population statistics.
- **Archives** — archival population documents or official-agency texts, with framing.
- **Book Review** — evaluative review of a population/development book (usually invited).

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/population-and-development-review-skills
/plugin install population-and-development-review-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/population-and-development-review-skills.git
cd population-and-development-review-skills

mkdir -p ~/.claude/skills && cp -R skills/popdevr-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/popdevr-* ~/.codex/skills/
```

### First Prompt

```
Use popdevr-workflow to tell me which skill I should use next for my PDR manuscript.
```

---

## Default Workflow

```text
popdevr-topic-selection
        ▼
popdevr-literature-positioning
        ▼
popdevr-theory-building
        ▼
popdevr-research-design
        ▼
popdevr-data-analysis
        ▼
popdevr-tables-figures
        ▼
popdevr-writing-style          (polish)
        ▼
popdevr-transparency-and-data
        ▼
popdevr-review-process
        ▼
popdevr-submission
        ▼
popdevr-rebuttal
```

`popdevr-workflow` is the router — it tells you which skill to use next based on where you are. Empirical
PDR papers loop **theory ↔ design ↔ analysis** as the population-and-development argument sharpens; a
synthetic essay loops **literature-positioning ↔ theory-building ↔ writing-style**, since its
contribution is the framework, not a new estimate.

---

## Skills

| Skill                          | Purpose                                                                          |
|--------------------------------|----------------------------------------------------------------------------------|
| `popdevr-workflow`             | Router — decides which sub-skill to invoke next                                  |
| `popdevr-topic-selection`      | Population-and-development fit and broad interest; pick the right article type   |
| `popdevr-literature-positioning` | Engage population science *and* the development debate; stake the contribution |
| `popdevr-theory-building`      | Build the mechanism, sharpened estimate, or synthetic framework into a contribution |
| `popdevr-research-design`      | Choose and defend the method (life table, decomposition, EHA, APC, projection)   |
| `popdevr-data-analysis`        | Rate/exposure construction, uncertainty, comparability, development meaning      |
| `popdevr-tables-figures`       | Pyramids, age schedules, survival curves, projection fans, comparative exhibits  |
| `popdevr-writing-style`        | Lucid essayistic prose; abstract/keywords; Free Format; APA at revision          |
| `popdevr-transparency-and-data` | Data availability statement, FAIR deposit, DHS/census licensing, ORCID          |
| `popdevr-review-process`       | Editorial screen, double-anonymized review, ~3-month decision                    |
| `popdevr-submission`           | ScholarOne preflight (anonymization, Free Format, data statement, no fees)       |
| `popdevr-rebuttal`             | R&R response strategy for cross-field referees + the deciding editor             |

### Resources

- [`resources/external_tools.md`](resources/external_tools.md) — population + development data sources (HMD / HFD / WPP / IPUMS / DHS / WDI) + R / Stata / Python packages (life tables, decomposition, survival, APC, projections)
- [`resources/official-source-map.md`](resources/official-source-map.md) — official Wiley / Population Council URLs behind every fact, with 待核实 markers on unverified items
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — a fictional PDR-style introduction (before → after)
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — real, web-verified PDR papers by topic × contribution, with a sibling-journal guard
- [`resources/code/`](resources/code/) — reproducible Stata + Python causal-inference skeleton (vendored, venue-neutral)

---

## What This Repo Does Not Do

- It does not write a submittable manuscript for you
- It does not simulate any specific editor's or reviewer's taste
- It does not assert volatile metadata (current editors, exact caps, portal link, fee/Online Open options, policy wording) — verify on the official page; unverified items are marked 待核实
- It does not decide whether your question is of broad population-and-development interest — that is the researcher's call
- It does not assume a Wiley APC applies — under the standard model PDR has no author fees

---

## Differences vs. Sibling Journals

| Journal | Owner / publisher | Distinctive demand | This pack's stance |
|---------|-------------------|--------------------|--------------------|
| **Population and Development Review (PDR)** | Population Council / Wiley | Population ↔ development + policy; **synthetic essays**; broad interest | Connect a population process to development; honor the essay tradition |
| Demography | PAA / Duke UP | Methods-forward population science; double-blind; S2O | Use `Demography-Skills` for a pure population-science estimate |
| Population Studies | Population Investigation Committee / T&F | Formal & empirical demography, methods rigor | Re-route if the contribution is methodological, not development-facing |
| Population Research and Policy Review | Springer | Applied population policy | Re-route if it is applied policy with no broad population-and-development argument |
| Studies in Family Planning | Population Council / Wiley | Reproductive health programs and evaluation | Re-route if the focus is program/intervention, not the population–development link |

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [PDR on Wiley Online Library](https://onlinelibrary.wiley.com/journal/17284457) — publisher home, current issues, author guidelines
- [PDR at the Population Council](https://popcouncil.org/population-and-development-review-journal/) — owner, scope, editorial oversight
- [PDR on JSTOR](https://www.jstor.org/journal/popudeverevi) — archive back to 1975

---

## License

MIT
