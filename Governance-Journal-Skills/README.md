# Governance Journal Skills

<p align="center">
  <img src="assets/cover.svg" alt="Governance: An International Journal of Policy, Administration, and Institutions cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Governance-14274e)](https://onlinelibrary.wiley.com/journal/14680491)
[![Field](https://img.shields.io/badge/field-Public%20Administration%20%26%20Political%20Science-1f6feb)](https://onlinelibrary.wiley.com/journal/14680491)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **Governance: An International Journal of Policy,
Administration, and Institutions** — published by **Wiley(-Blackwell)** in association with the
**International Political Science Association (IPSA) Research Committee 27 — Structure & Organization
of Government (SOG)**, founded in **1988**, quarterly (ISSN 0952-1895 print / 1468-0491 online).
*Governance* publishes theoretical and empirical scholarship on **executive politics, public policy,
public administration, and the organization of the state** — comparative and international
governance, regulatory governance, policy-making processes, bureaucratic and institutional reform,
governance networks, accountability, and the state itself. It welcomes quantitative, qualitative, and
comparative-historical work judged on its own terms.

This repository is opinionated. It is **not** a generic public-administration writing toolbox and it
is **not** an economics pack repurposed for policy studies. It is a **Governance-specific** stack: a
question of **comparative significance for policy, administration, and institutions**, an argument
that travels **across cases and systems**, a design defended on its own methodological terms,
**double-blind** preparation with a **separate title page**, and a **Data Availability Statement** that
states whether replication materials exist and how to reach them.

> **Official basis checked 2026-06** — facts here are drawn from the Wiley Online Library journal page,
> the journal's author guidelines, and IPSA SOG/RC27 sources. Volatile specifics (editors and term,
> exact word/abstract caps, submission portal, fees/APC, ORCID and reference-style detail) change;
> items not directly confirmed are marked **待核实** in
> [`resources/official-source-map.md`](resources/official-source-map.md). **Verify on the official
> journal page before relying on any of them.**

---

## What Is Governance, and Why a Separate Stack?

*Governance*'s constraints differ from a practitioner journal, a public-management-theory journal, or
a policy-analysis journal:

| Constraint            | Governance                                                                                   | Implication                                                              |
|-----------------------|----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| Scope                 | **Executive politics, public policy, public administration, the organization of the state**   | The paper must speak to comparative governance, not just one country/agency |
| Premium on            | **A clear, original intervention** that travels across cases and institutional settings        | A purely local administrative report or descriptive case is off-fit       |
| Methods               | Quantitative, qualitative, comparative-historical — any **rigorous** method making the point   | Match method to question; do not force one template                       |
| Publisher / owner     | **Wiley(-Blackwell)** / in association with **IPSA SOG (RC27)**                                | Submit via the **Wiley submission system** (检索于 2026-06；以官网为准)    |
| Review model          | **Double-blind**; **at least two referees** review anonymously                                 | Anonymize the manuscript; supply a **separate title page**                |
| Out of scope (hard)   | **Corporate governance**; typically **no literature reviews / bibliometric analyses**          | Do not pitch a corporate-governance or pure-review paper here             |
| Length                | **≤ 9,000 words excluding citations/bibliography** (official); abstract **~150 words**          | Put the word count on the title page; mind the cap from the first draft   |
| Transparency          | **Data Availability Statement required**; DOI-citable repository recommended                    | Write the statement honestly; deposit replication materials where you can |
| Pre-analysis plans    | An **anonymized pre-analysis plan may be supplied** as supplementary material                  | Use it to signal prospective, confirmatory design where relevant          |

> *Governance* requires a **Data Availability Statement**, but — unlike APSR's verified
> reproducibility gate — it is a **mandatory statement**, not a hard pre-publication reproduction check
> by the editorial office. Be honest about that distinction: build a clean replication package because
> it is good practice and DOI-citable deposit is recommended, not because the editors will re-run it as
> a condition of acceptance (检索于 2026-06；以官网为准).

The official author guidelines give the working word cap as **≤ 9,000 words** excluding
citations/bibliography. A third-party listing reports a much lower **3,000–5,000 words**; treat the
official 9,000 as the working cap and see the **待核实** note on the discrepancy in
[`resources/official-source-map.md`](resources/official-source-map.md).

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/governance-journal-skills
/plugin install governance-journal-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/governance-journal-skills.git
cd governance-journal-skills

mkdir -p ~/.claude/skills && cp -R skills/govern-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/govern-* ~/.codex/skills/
```

### First Prompt

```
Use govern-workflow to tell me which skill I should use next for my Governance manuscript.
```

---

## Default Workflow

```text
govern-topic-selection
        ▼
govern-literature-positioning
        ▼
govern-theory-building
        ▼
govern-research-design
        ▼
govern-data-analysis
        ▼
govern-tables-figures
        ▼
govern-writing-style          (polish)
        ▼
govern-transparency-and-data
        ▼
govern-review-process
        ▼
govern-submission
        ▼
govern-rebuttal
```

`govern-workflow` is the router — it tells you which skill to use next based on where you are. If your
design is **prospective and confirmatory**, route to `govern-transparency-and-data` early to draft an
**anonymized pre-analysis plan** as supplementary material; if your contribution is **comparative
across cases or systems**, lean on `govern-topic-selection` and `govern-literature-positioning` to make
the cross-case stake explicit before you draft.

---

## Skills

| Skill                           | Purpose                                                                              |
|---------------------------------|-------------------------------------------------------------------------------------|
| `govern-workflow`               | Router — decides which sub-skill to invoke next                                      |
| `govern-topic-selection`        | Comparative-governance fit; an original intervention that travels across cases       |
| `govern-literature-positioning` | Engage the policy / administration / institutions literatures Governance readers expect |
| `govern-theory-building`        | Build the argument about policy, administration, or the state into a contribution    |
| `govern-research-design`        | Defend the design — comparative cases, causal inference, QCA, mixed methods          |
| `govern-data-analysis`          | Analysis norms, uncertainty, robustness, cross-case and configurational triangulation |
| `govern-tables-figures`         | Clear, self-contained exhibits for a comparative-governance audience                 |
| `govern-writing-style`          | Reach a comparative policy/administration audience within the ~9,000-word cap        |
| `govern-transparency-and-data`  | Data Availability Statement; DOI-citable deposit; anonymized pre-analysis plan       |
| `govern-review-process`         | Double-blind review, desk screening, scope fit, decision categories                  |
| `govern-submission`             | Wiley-system preflight (anonymization, separate title page, word count, abstract)    |
| `govern-rebuttal`               | R&R response-letter strategy for multiple referees + editor                          |

### Resources

- [`resources/external_tools.md`](resources/external_tools.md) — comparative-governance data sources
  (V-Dem / Quality of Government / World Bank WGI / OECD / Comparative Agendas / ParlGov / Manifesto
  Project / SGI) plus R / Stata / Python, QCA/fsQCA tooling, and CAQDAS for qualitative work
- [`resources/official-source-map.md`](resources/official-source-map.md) — official Wiley / IPSA SOG
  URLs behind every fact, with 待核实 markers on unverified items

---

## Differences vs. Sibling Journals

*Governance* is easy to confuse with neighboring public-administration and policy journals. Pitch it as
the **comparative policy / administration / institutions** venue, and route off-fit work elsewhere.

| Journal                      | Owner / publisher                  | Distinctive niche                                                  |
|------------------------------|------------------------------------|-------------------------------------------------------------------|
| **Governance**               | IPSA SOG (RC27) / **Wiley**        | **Comparative & international** executive politics, policy, administration, institutions |
| **Public Administration Review (PAR)** | ASPA / Wiley             | US-centric, **practitioner-facing** public administration          |
| **JPART**                    | Oxford University Press            | **Public-administration theory** and organizational behavior      |
| **JPAM**                     | Wiley (for APPAM)                  | **Policy analysis** and program evaluation, often US policy        |
| **Regulation & Governance**  | **Wiley** (sibling)                | **Regulatory studies** and regulatory governance, cross-discipline |

---

## What This Repo Does Not Do

- It does not write a submittable manuscript for you
- It does not simulate any specific editor's or reviewer's taste
- It does not assert volatile metadata (current editors and term, exact word/abstract caps,
  submission portal, fee/APC, reference-style and ORCID specifics) — verify on the official page;
  unverified items are marked 待核实
- It does not decide whether your question is of comparative governance significance — that is the
  researcher's call
- It does **not** turn a corporate-governance paper or a stand-alone literature review into a fit for
  *Governance* — those are out of scope

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — index of journal-specific skill packs
- [Governance (Wiley Online Library)](https://onlinelibrary.wiley.com/journal/14680491) — publisher home, current issues, author guidelines
- [IPSA SOG (RC27) — Structure & Organization of Government](https://www.ipsa.org/) — the research committee in association with which *Governance* is published

---

## License

MIT
