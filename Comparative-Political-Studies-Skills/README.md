# Comparative Political Studies Skills

<p align="center">
  <img src="assets/cover.svg" alt="Comparative Political Studies cover" width="200">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-CPS-23457a)](https://journals.sagepub.com/home/cps)
[![Field](https://img.shields.io/badge/field-Comparative%20Politics-1f6feb)](https://journals.sagepub.com/author-instructions/cps)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **Comparative Political Studies (CPS)** — a leading
**comparative-politics** journal published by **SAGE** since **1968**. CPS publishes methodological,
theoretical, and empirical articles in comparative politics: **democratization & regimes, political
institutions, political behavior & participation, ethnic politics & conflict, comparative political
economy, and parties & elections** — across countries and over time. It is methodologically pluralist:
large-N quantitative and causal-inference designs, formal theory, qualitative and comparative-historical
inference, and multi-method work are all welcome, each judged on its own terms.

This repository is opinionated. It is **not** a generic social-science writing toolbox and it is **not**
a general political-science pack repurposed for comparative work. It is a **CPS-specific** stack: a claim
with **comparative leverage** (across countries, subnational units, or time), an argument that **travels**
beyond one region, a design defended on its own methodological terms, **anonymized** preparation for SAGE
Track, and a **replication package deposited to the CPS Dataverse** that gates final acceptance for
quantitative papers.

**Official basis checked 2026-06.** Volatile specifics (current editors, exact caps, fees, policy
wording, portal) are marked **(检索于 2026-06；以官网为准)** or **待核实** and must be confirmed on the
official SAGE author page.

---

## What Is CPS, and Why a Dedicated Stack?

CPS's constraints differ from a general flagship or an IR journal:

| Constraint            | CPS                                                                          | Implication                                                       |
|-----------------------|-----------------------------------------------------------------------------|------------------------------------------------------------------|
| Scope                 | **Comparative politics** (cross-national and intra-national)                 | The paper must have comparative leverage, not be one snapshot     |
| Premium on            | A **portable mechanism** that travels across regions/regime types           | A single-case area study with no comparative claim is off-fit     |
| Methods               | Quantitative, qualitative, formal, experimental, multi-method — judged on own terms | Do not force one template onto every paper                |
| Publisher             | **SAGE Publications** (since 1968)                                           | Submitted via **SAGE Track (ScholarOne)**                         |
| Review model          | **Anonymous** peer review                                                    | Anonymize the manuscript; identifying info on a separate title page |
| Length                | Articles **max 11,000 words**; references, tables, figures **excluded**      | Spend space on exhibits; keep prose tight                        |
| Abstract              | **Unstructured, ~150 words**                                                 | Not a structured abstract                                        |
| Style                 | **APA-style author-date** references (SAGE house)                            | Not APSA/Chicago; in-text and list must agree                    |
| Identifiers           | **ORCID required for the submitting author**                                 | Link it in SAGE Track before submission                          |
| Transparency          | **CPS Dataverse** replication deposit; **data availability statement** required | Quantitative final acceptance is gated on the deposit         |
| Preregistration       | **Optional** anonymized pre-analysis plan as supplementary material          | Encouraged, not required; mark registered vs. exploratory        |

Items not directly confirmed are marked **待核实** in
[`resources/official-source-map.md`](resources/official-source-map.md). **Verify on the official page.**

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/comparative-political-studies-skills
/plugin install comparative-political-studies-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/comparative-political-studies-skills.git
cd comparative-political-studies-skills

mkdir -p ~/.claude/skills && cp -R skills/cps-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/cps-* ~/.codex/skills/
```

### First Prompt

```
Use cps-workflow to tell me which skill I should use next for my CPS manuscript.
```

---

## Default Workflow

```text
cps-topic-selection
        ▼
cps-literature-positioning
        ▼
cps-theory-building
        ▼
cps-research-design
        ▼
cps-data-analysis
        ▼
cps-tables-figures
        ▼
cps-writing-style          (polish)
        ▼
cps-transparency-and-data
        ▼
cps-review-process
        ▼
cps-submission
        ▼
cps-rebuttal
```

`cps-workflow` is the router — it tells you which skill to use next based on where you are. Its first job
is the **comparative-fit check**: if the paper has no comparative leverage or its claim does not travel,
it routes back to `cps-topic-selection` / `cps-research-design` before anything else.

---

## Skills

| Skill                          | Purpose                                                                       |
|--------------------------------|-------------------------------------------------------------------------------|
| `cps-workflow`                 | Router — confirms comparative fit, decides which sub-skill to invoke next      |
| `cps-topic-selection`          | Comparative leverage + travel; right venue vs. APSR/AJPS/WP/IO/BJPS            |
| `cps-literature-positioning`   | Locate the paper in a comparative debate; name the rival; cross-regional breadth |
| `cps-theory-building`          | Build a portable mechanism with scope conditions and distinguishing implications |
| `cps-research-design`          | Defend the design — cross-national panels, case comparison, experiments, multi-method |
| `cps-data-analysis`            | Comparative-data hazards, inference, robustness, theory-driven heterogeneity   |
| `cps-tables-figures`           | Self-contained, comparative-legible exhibits; SAGE production specs            |
| `cps-writing-style`            | CPS arc, 11,000-word limit, ~150-word abstract, APA author-date references     |
| `cps-transparency-and-data`    | CPS Dataverse package, data availability statement, qualitative transparency   |
| `cps-review-process`           | Desk screen, anonymous review, decision categories, what comparativists reward |
| `cps-submission`               | SAGE Track preflight (anonymization, word count, ORCID, abstract, DAS)         |
| `cps-rebuttal`                 | R&R response-letter strategy for multiple reviewers + editor                   |

### Resources

- [`resources/external_tools.md`](resources/external_tools.md) — comparative-politics data sources (V-Dem / Polity / CSES / Manifesto Project / QoG / ACLED / UCDP / Correlates of War) + R / Stata / Python and qualitative/CAQDAS tooling
- [`resources/official-source-map.md`](resources/official-source-map.md) — official SAGE / CPS URLs behind every fact, with 待核实 markers on unverified items
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — verified real CPS papers by subfield × method, with a sibling-journal do-not-misattribute list
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — a before→after CPS-style introduction (fictional teaching example)
- [`resources/code/`](resources/code/) — reproducible Stata + Python causal-inference skeleton (vendored 2026-06)

---

## What This Repo Does Not Do

- It does not write a submittable manuscript for you
- It does not simulate any specific editor's or reviewer's taste
- It does not assert volatile metadata (current editors and term, exact caps, fee/APC, policy wording) — verify on the official page; unverified items are marked 待核实
- It does not decide whether your question has genuine comparative leverage — that is the researcher's call

---

## Differences vs. Sibling Journals

| Journal | Scope | Why not the same as CPS |
|---------|-------|-------------------------|
| **APSR / AJPS** | General US political-science flagships | Pitch to the whole discipline; CPS wants the *comparative-politics* contribution |
| **World Politics / International Organization** | IR and IR-adjacent comparative | IR-first; CPS is domestic comparative politics first |
| **British Journal of Political Science** | Broad UK generalist | Generalist; CPS is the comparative specialist |
| **Comparative Politics (CUNY)** | Comparative politics, more qualitative-leaning | Different journal/publisher; CPS (SAGE) is methodologically pluralist |

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [Comparative Political Studies (SAGE)](https://journals.sagepub.com/home/cps) — publisher home
- [CPS Submission Guidelines](https://journals.sagepub.com/author-instructions/cps) — scope, length, style, data policy
- [CPS Dataverse](https://dataverse.harvard.edu/dataverse/cps) — replication materials repository

---

## License

MIT
