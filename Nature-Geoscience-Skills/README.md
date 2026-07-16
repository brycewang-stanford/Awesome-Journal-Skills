# Nature Geoscience Skills

<p align="center">
  <img src="assets/cover.svg" alt="Nature Geoscience journal cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Nature%20Geoscience-1d4e40)](https://www.nature.com/ngeo/)
[![Index](https://img.shields.io/badge/publisher-Nature%20Portfolio-1f6feb)](https://www.nature.com/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **Nature Geoscience (Nat. Geosci.)** — the Nature Portfolio's Earth-science flagship, publishing broad-interest advances across the **solid Earth, atmosphere, oceans, cryosphere, climate, and planetary science**.

This repository is opinionated. It is **not** a generic Earth-science writing toolbox. It is a **Nature-Geoscience-specific** stack built around the journal's defining constraint: a result must be a **broad, cross-disciplinary Earth-system advance**, grounded in **quantitative evidence with quantified uncertainty**, communicated **accessibly to non-specialists** inside the strict Nature Article container, with reproducible detail pushed to the online **Methods** and **Supplementary Information**.

---

## Why a Separate Nature Geoscience Skill Stack?

Nature Geoscience imposes constraints that differ materially from community Earth-science journals (JGR, GRL, Climate Dynamics) and even from its sister *Communications Earth & Environment*:

| Constraint            | Nature Geoscience                                                | Implication                                                          |
|-----------------------|-----------------------------------------------------------------|----------------------------------------------------------------------|
| The gate              | Broad Earth-system advance **AND** cross-disciplinary interest  | A rigorous but regional/incremental result is declined on interest grounds |
| Triage                | In-house editors desk-reject most submissions **before review** | The cover letter's breadth case is decisive; there is **no presub route** |
| Audience              | All Earth scientists, not just your subfield                    | Manuscripts are edited to be accessible to non-specialists          |
| Evidence bar          | Quantitative data / data-validated models, with uncertainty     | Model-only or uncertainty-free results are desk-rejected             |
| Length                | Article ~3,000 words; abstract ~200 words (verify)              | Ruthless partitioning to online Methods and SI                       |
| Display items         | 4–6 figures/tables (verify)                                     | Fig. 1 must carry the advance and its uncertainty at a glance        |
| Structure             | Separate online **Methods**; **"Here we show"** abstract        | The reproducible protocol lives outside the word count               |
| Compliance            | Reporting Summary + data + code availability                    | These gate **acceptance**, not just submission                       |
| Review                | Single-blind default; **double-blind opt-in**                   | Anonymise if you opt in                                              |

Generic "scientific writing" packs do not address the broad-interest desk-triage, the no-presub cover-letter burden, the online-Methods split, or the Reporting-Summary and data/code-availability gates.

> Volatile specifics (current word/display-item/reference limits, content types, Reporting Summary, portal, APC) change — always verify on the official Nature Geoscience author pages.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/ngeo-skills
/plugin install ngeo-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/ngeo-skills.git
cd ngeo-skills

mkdir -p ~/.claude/skills && cp -R skills/ngeo-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/ngeo-* ~/.codex/skills/
```

### First Prompt

```
Use ngeo-workflow to tell me which skill I should use next for my Nature Geoscience manuscript.
```

---

## Default Workflow

```text
ngeo-scope-fit
        ▼
ngeo-results-framing
        ▼
ngeo-methods
        ▼
ngeo-figures
        ▼
ngeo-supplementary
        ▼
ngeo-writing-style        (polish)
        ▼
ngeo-length-management    (fit the Article container)
        ▼
ngeo-cover-letter
        ▼
ngeo-submission
        ▼
ngeo-referee-strategy
        ▼
ngeo-revision
```

`ngeo-workflow` is the router — it tells you which skill to use next based on where you are.

---

## Skills

| Skill                     | Purpose                                                                     |
|---------------------------|-----------------------------------------------------------------------------|
| `ngeo-workflow`           | Router — decides which sub-skill to invoke next                             |
| `ngeo-scope-fit`          | The broad-interest Earth-system gate; Nat. Geosci. vs. community journals    |
| `ngeo-results-framing`    | One-advance narrative, the "Here we show" abstract, finding-first opening    |
| `ngeo-methods`            | Online Methods that grounds every claim in data + quantified uncertainty     |
| `ngeo-figures`            | 4–6 display items; lead figure carries the advance and its uncertainty       |
| `ngeo-supplementary`      | Partition extended data to SI; keep the main text self-contained            |
| `ngeo-writing-style`      | Nature house style, non-specialist accessibility, calibrated claims          |
| `ngeo-length-management`  | Fit ~3,000 words + 4–6 display items + ~50 references                        |
| `ngeo-cover-letter`       | Argue broad interest to the in-house editor (no presub route)               |
| `ngeo-submission`         | Preflight + Reporting Summary, data/code availability, Editorial Manager     |
| `ngeo-referee-strategy`   | Suggested / excluded referees; pre-empt breadth + grounding objections       |
| `ngeo-revision`           | Point-by-point response, resubmission, and the Nature Portfolio appeal route  |

### Resources

- [`skills/ngeo-submission/templates/manuscript_template.md`](skills/ngeo-submission/templates/manuscript_template.md) — Article skeleton ("Here we show" abstract, main text, online Methods, availability statements, SI, cover letter)
- [`skills/ngeo-submission/templates/checklist.md`](skills/ngeo-submission/templates/checklist.md) — 10-section pre-submission self-check
- [`resources/external_tools.md`](resources/external_tools.md) — reanalysis/satellite/proxy data, CMIP output, repositories (PANGAEA/Zenodo), and the geospatial software stack
- [`resources/official-source-map.md`](resources/official-source-map.md) — the real official URLs behind every fact, with checked dates
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — well-known Earth-system advances by subfield × evidence type
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — annotated before→after Nature Geoscience abstract + opening

---

## Differences vs. Community Earth-Science Journals

| Dimension           | Nature Geoscience                    | JGR / GRL / community + CEE          |
|---------------------|--------------------------------------|--------------------------------------|
| The gate            | Broad advance **+ cross-disciplinary interest** | Rigor + subfield relevance    |
| Triage              | Editor desk-reject before review     | Usually all sound work reviewed      |
| Audience            | All Earth scientists                  | The specific subfield                |
| Length              | Article ~3,000 words; strict          | Generous; full archival treatment    |
| Methods             | Separate online Methods               | Methods in the body                  |
| Regional/incremental| Declined on interest grounds          | Appropriate and welcome              |

If your result is solid but regional or incremental, `ngeo-scope-fit` will recommend retargeting to a community journal or *Communications Earth & Environment* rather than fighting the broad-interest gate.

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [Nature Geoscience](https://www.nature.com/ngeo/) — Official Nature Portfolio journal page
- [Nature Portfolio](https://www.nature.com/) — Publisher

---

## License

MIT
