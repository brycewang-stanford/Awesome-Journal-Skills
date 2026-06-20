# New Media & Society Skills

<p align="center">
  <img src="assets/cover.svg" alt="New Media & Society cover" width="200">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-NM%26S-2a2a6a)](https://journals.sagepub.com/home/nms)
[![Field](https://img.shields.io/badge/field-Digital%20Media%20%26%20Society-1f6feb)](https://journals.sagepub.com/home/nms)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **New Media & Society (NM&S)** — a leading
**interdisciplinary** journal on digital media, the internet, and society, published by **SAGE** since
**1999**. NM&S publishes work on platforms and datafication, digital inequality and the digital divide,
social media and online community, algorithms and AI in everyday life, digital labor, privacy and
surveillance, and the social, political, and cultural shaping of new media. It is **methodologically
pluralist and international**: qualitative interviews and digital ethnography, critical and theoretical
work, content and discourse analysis, computational methods, and mixed methods all appear in its pages.

This repository is opinionated. It is **not** a generic social-science writing toolbox and it is
**not** a quantitative communication-science pack relabeled. It is an **NM&S-specific** stack: a claim
that reaches new media and society *broadly*, a portable concept rather than a platform report, a design
defended on its own methodological terms, careful **research ethics for online and platform data**, a
properly **masked** manuscript inside the **~8,000-word target**, and submission through **Sage Track**
under **strictly anonymous (double-anonymized)** review.

---

## What Is NM&S, and Why a Dedicated Stack?

NM&S's constraints differ from a single-field or a quantitative-comm journal:

| Constraint        | NM&S                                                                                  | Implication                                                        |
|-------------------|---------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| Scope             | **Digital media, the internet, and society — interdisciplinary**                       | The paper must reach beyond one platform and one field            |
| Premium on        | A portable concept/mechanism + interdisciplinary significance                          | A platform case study with no travelling idea is off-fit          |
| Methods           | Qualitative, critical/theoretical, content/discourse, computational, mixed — judged on own terms | Don't force a regression template onto interpretive work |
| Publisher         | **SAGE** (since 1999; ISSN 1461-4448 / 1461-7315)                                      | Submitted via **Sage Track** (ScholarOne), `mc.manuscriptcentral.com/nms` |
| Review model      | **Strictly anonymous (double-anonymized)** — masked manuscript + separate title page    | You *may* self-cite, just not identifyingly                        |
| Length            | **~8,000-word target** — *all text incl. notes, references, tables, and charts*        | References and tables count; a few hundred over may mean no review |
| Abstract          | **~150 words**, unstructured; **≥4 keywords**                                          | Concise purpose + approach + findings                              |
| Referencing       | **SAGE Harvard** (author-date)                                                         | Specific house citation style                                     |
| Ethics & data     | **SAGE/COPE** ethics + data-availability norms; **online/platform-data ethics**        | Consent, anonymization, scraping & ToS matter — not a verified replication gate |

Volatile specifics (current editors and the 2026 editorial transition, exact word/abstract caps, ORCID,
APC, masking format) change — items not directly confirmed are marked **待核实** in
[`resources/official-source-map.md`](resources/official-source-map.md). **Verify on the official journal
page** (which may block automated tools).

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/new-media-and-society-skills
/plugin install new-media-and-society-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/new-media-and-society-skills.git
cd new-media-and-society-skills

mkdir -p ~/.claude/skills && cp -R skills/newms-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/newms-* ~/.codex/skills/
```

### First Prompt

```
Use newms-workflow to tell me which skill I should use next for my New Media & Society manuscript.
```

---

## Default Workflow

```text
newms-topic-selection
        ▼
newms-literature-positioning
        ▼
newms-theory-building
        ▼
newms-research-design
        ▼
newms-data-analysis
        ▼
newms-tables-figures
        ▼
newms-writing-style          (polish)
        ▼
newms-transparency-and-data
        ▼
newms-review-process
        ▼
newms-submission
        ▼
newms-rebuttal
```

`newms-workflow` is the router — it tells you which skill to use next based on where you are.

---

## Skills

| Skill                          | Purpose                                                                       |
|--------------------------------|-------------------------------------------------------------------------------|
| `newms-workflow`               | Router — decides which sub-skill to invoke next                               |
| `newms-topic-selection`        | Interdisciplinary fit; a portable concept, not a platform report             |
| `newms-literature-positioning` | Braid two-or-more literatures; name the gap as a disagreement                |
| `newms-theory-building`        | Build a portable concept/mechanism drawing on media & social theory          |
| `newms-research-design`        | Defend the design — interviews/ethnography, content/discourse, computational, mixed |
| `newms-data-analysis`          | Inference, reliability, validation, and analytic transparency by method      |
| `newms-tables-figures`         | Clear, self-contained, anonymized exhibits (they count toward the word target)|
| `newms-writing-style`          | Reach the field in ~8,000 words; SAGE Harvard; front-load the contribution    |
| `newms-transparency-and-data`  | Online/platform-data ethics, consent, anonymization, scraping/ToS, sharing   |
| `newms-review-process`         | Anonymous review, what interdisciplinary referees weigh, decisions           |
| `newms-submission`             | Sage Track preflight (~8,000 words, masking, abstract, keywords, ethics)      |
| `newms-rebuttal`               | R&R response-letter strategy for conflicting interdisciplinary reviewers       |

### Resources

- [`resources/external_tools.md`](resources/external_tools.md) — digital-media data sources + R / Python / CAQDAS / content-analysis / computational tooling by method
- [`resources/official-source-map.md`](resources/official-source-map.md) — official SAGE / NM&S URLs behind every fact, with 待核实 markers
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — a before→after NM&S introduction (fictional, house style)
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — real, web-verified NM&S papers by method × theme, with a sibling-journal guard

---

## What This Repo Does Not Do

- It does not write a submittable manuscript for you
- It does not simulate any specific editor's or reviewer's taste (note the 2026 editorial transition)
- It does not assert volatile metadata (current editors, exact caps, ORCID/APC, masking format) — verify on the official page; unverified items are marked 待核实
- It does not decide whether your question is of broad interdisciplinary significance — that is the researcher's call

---

## Differences vs. Sibling Journals

| Journal | Center of gravity | When to send your paper there instead |
|---------|-------------------|----------------------------------------|
| **New Media & Society** | **Broad interdisciplinary digital-media-and-society**, methodologically pluralist | the work is conceptually ambitious and reaches across fields |
| Journal of Communication / Communication Research | Quantitative US communication science | a comm-theory effect estimated quantitatively |
| Information, Communication & Society | Information, ICT, and policy mechanics | narrowly about ICT/information-society mechanics |
| Social Media + Society | Social-media-platform-specific empirical work | a platform study with little reach beyond it |

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [New Media & Society (SAGE)](https://journals.sagepub.com/home/nms) — publisher home
- [NM&S Submission Guidelines](https://journals.sagepub.com/author-instructions/nms) — author instructions (may block automated tools)

---

## License

MIT
