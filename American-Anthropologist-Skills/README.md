# American Anthropologist Skills

<p align="center">
  <img src="assets/cover.svg" alt="American Anthropologist cover" width="200">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-American%20Anthropologist-7a4a1a)](https://anthrosource.onlinelibrary.wiley.com/journal/15481433)
[![Field](https://img.shields.io/badge/field-Anthropology-1f6feb)](https://www.americananthro.org/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **American Anthropologist (AA)** — the **flagship
four-field journal of the American Anthropological Association (AAA)**, founded in **1888** and published
by **Wiley**. AA publishes the best scholarship across the **whole of anthropology**: **sociocultural
anthropology, archaeology, biological/physical anthropology, and linguistic anthropology**, together
with **reflexive and public anthropology**. The journal is predominantly **ethnographic and
qualitative**, but it also publishes material/archaeological and quantitative biological work — and it
is distinctively strong on **theory, reflexivity, ethics, and writing**.

This repository is opinionated. It is **not** a generic social-science writing toolbox and it is **not**
an econometrics pack repurposed for anthropology. It is an **AA-specific** stack: a contribution of
**four-field significance**, an argument that speaks **past its own subfield**, **ethnographic and
qualitative inference treated as first-class**, **reflexivity and positionality** made explicit,
**anonymous** preparation, and — at the center — **research ethics and accountability**: informed
consent, anonymization, protection of vulnerable communities, and heritage/repatriation obligations
under the AAA *Principles of Professional Responsibility* and an **ethics of care**.

---

## What Is AA, and Why a Dedicated Stack?

AA's constraints differ from a single-subfield journal or a quantitative social-science venue:

| Constraint            | American Anthropologist                                                          | Implication                                                       |
|-----------------------|---------------------------------------------------------------------------------|------------------------------------------------------------------|
| Scope                 | **Four fields** of anthropology + reflexive/public                              | The paper must matter beyond its subfield                        |
| Premium on            | **Four-field significance** + a portable concept, with reflexivity              | A narrow, subfield-only description is off-fit                    |
| Methods               | **Ethnographic/qualitative first-class**; also material, lab, computational     | Do not force ethnography into a hypothesis-test template          |
| Publisher / owner     | **Wiley** / **AAA**                                                             | Submitted via **Research Exchange** (since Apr 2025)             |
| Review model          | **Anonymous** peer review under an **ethics of care**                            | Anonymize manuscript **and file name**; separate title page      |
| Fee                   | **No submission or publication fee**                                            | Do not budget a fee (OnlineOpen APC only if going open access)    |
| Length                | Research Articles **≤ 8,000 words**; **abstract 200**; shorter sections vary     | Counts include figures, tables, references, notes                |
| Style                 | **Chicago author-date**; **free-format** accepted; DOIs in references            | Not a rigid template at first submission; ORCID per Wiley         |
| Ethics                | **Consent, anonymization, heritage/repatriation, accountability** are central   | Ethics is designed in, and gates publication                     |
| Distinctive sections  | Vital Topics Forums · World / Public / Multimodal Anthropologies · Review Essays | Choose the right section up front                                |

> **Official basis checked 2026-06-20** — facts are anchored to the AA editorial site, AAA ethics and
> news pages, AnthroSource/Wiley, and Wiley's Author Compliance Tool. Live Research Exchange prompts,
> APCs, and editorial rosters can change; verify those at upload or acceptance.

### Sections at a glance

- **Research Articles** — full studies, **≤ 8,000 words** (extendable to ~10,500 on acceptance).
- **Vital Topics Forums** — curated multi-author debates on pressing issues (often invited/proposed).
- **World Anthropologies** — anthropology produced beyond the Anglophone center; decenters the canon.
- **Public Anthropologies** — engaged, activist, publicly-facing scholarship.
- **Multimodal Anthropologies** — image/sound/film as argument, treated as scholarship in its own right.
- **Essays / Commentaries / Interviews / Review Essays / Book Reviews** — shorter formats with their own caps.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/american-anthropologist-skills
/plugin install american-anthropologist-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/american-anthropologist-skills.git
cd american-anthropologist-skills

mkdir -p ~/.claude/skills && cp -R skills/amanthro-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/amanthro-* ~/.codex/skills/
```

### First Prompt

```
Use amanthro-workflow to tell me which skill I should use next for my American Anthropologist manuscript.
```

---

## Default Workflow

```text
amanthro-topic-selection
        ▼
amanthro-literature-positioning
        ▼
amanthro-theory-building
        ▼
amanthro-research-design
        ▼
amanthro-data-analysis
        ▼
amanthro-tables-figures
        ▼
amanthro-writing-style          (polish)
        ▼
amanthro-transparency-and-data  (ethics & accountability — also run EARLY)
        ▼
amanthro-review-process
        ▼
amanthro-submission
        ▼
amanthro-rebuttal
```

`amanthro-workflow` is the router — it tells you which skill to use next based on your stage, subfield,
and section. The **ethics-and-accountability** skill (`amanthro-transparency-and-data`) should run
**early** as well as before submission: consent, anonymization, and heritage obligations are design
decisions, not final-step checks.

---

## Skills

| Skill                              | Purpose                                                                       |
|------------------------------------|-------------------------------------------------------------------------------|
| `amanthro-workflow`                | Router — decides which sub-skill to invoke next (by stage, subfield, section)  |
| `amanthro-topic-selection`         | Four-field fit across anthropology; pick the right section                     |
| `amanthro-literature-positioning`  | Speak past your subfield; decenter the canon; citational politics             |
| `amanthro-theory-building`         | Build a portable concept + reflexive argument (ethnographic to biological)     |
| `amanthro-research-design`         | Defend the design — fieldwork, archival/material, lab/quant, multimodal        |
| `amanthro-data-analysis`           | Disciplined interpretation; honest evidence; quant rigor for bio/archaeology   |
| `amanthro-tables-figures`          | Ethnographic + multimodal exhibits: consent, permissions, alt text            |
| `amanthro-writing-style`           | Chicago author-date; reach four fields; care-ful, inclusive language           |
| `amanthro-transparency-and-data`   | Ethics & accountability: consent, anonymization, heritage/repatriation         |
| `amanthro-review-process`          | Anonymous review, ethics of care, screening, sections, decision categories     |
| `amanthro-submission`              | Research Exchange preflight (anonymization, caps, ethics statement, ORCID)      |
| `amanthro-rebuttal`                | R&R response-letter strategy for cross-subfield reviewers + editor             |

### Resources

- [`resources/external_tools.md`](resources/external_tools.md) — anthropology data sources, archives, and software (CAQDAS, transcription, GIS, lab/quant) by subfield
- [`resources/official-source-map.md`](resources/official-source-map.md) — official AA / AAA / Wiley URLs behind every fact and live-check guardrail
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — before→after AA-style introduction (fictional)
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — real, web-verified AA papers by subfield × method, with a sibling-journal guard

---

## Differences vs. Sibling Journals

| Journal                    | Scope / format                                                   | This pack's guard |
|----------------------------|-----------------------------------------------------------------|-------------------|
| **American Anthropologist (AA)** | **Four-field AAA flagship**; ethnographic + material + bio + linguistic | The target of this pack |
| *American Ethnologist* (AE) | Sociocultural ethnography (AAA/AES)                              | AA is broader four-field, not AE's sociocultural focus |
| *Cultural Anthropology* (CA)| Sociocultural, theory-forward (SCA), often open access           | AA is four-field, not CA's sociocultural-only remit |
| *Current Anthropology*      | Four-field but with the distinctive **CA✩ comments-and-reply** format (Wenner-Gren/Chicago) | AA has no CA✩ format; do not confuse the two |

---

## What This Repo Does Not Do

- It does not write a submittable manuscript for you
- It does not simulate any specific editor's or reviewer's taste
- It does not grant ethics waivers or replace IRB/community review
- It does not hard-code volatile metadata beyond sourced facts; verify Research Exchange prompts, APCs, and masthead changes on the live pages

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [American Anthropologist (Wiley Online Library)](https://anthrosource.onlinelibrary.wiley.com/journal/15481433) — publisher home
- [American Anthropologist editorial site](https://www.americananthropologist.org/) — sections, how-to-submit, editorial policies
- [American Anthropological Association](https://www.americananthro.org/) — owner; ethics principles

---

## License

MIT
