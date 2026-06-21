# Conservation Biology Skills

<p align="center">
  <img src="assets/cover.svg" alt="Conservation Biology cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Conservation%20Biology-3f7d20)](https://conbio.onlinelibrary.wiley.com/journal/15231739)
[![Field](https://img.shields.io/badge/field-Conservation%20Science-1f6feb)](https://conbio.org/publications/conservation-biology/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **Conservation Biology** — the **flagship journal of the
Society for Conservation Biology (SCB)**, founded in **1987** and published by **Wiley**. Conservation
Biology publishes ground-breaking research, essays, and reviews that develop theory and methods, define
key problems, and propose solutions across the **social, ecological, and philosophical dimensions of
conserving biological diversity** — population and landscape ecology, extinction risk, protected-area
design, human-wildlife interactions, and conservation policy and practice, drawing on both the natural
and social sciences.

This repository is opinionated. It is **not** a generic ecology writing toolbox and it is **not** an
economics or methods pack repurposed for conservation. It is a **Conservation Biology-specific** stack:
a result with **direct, transferable implications for conserving biodiversity**, a design matched to the
ecological question (detection, scale, counterfactuals), **double-blind** preparation, a **data
availability statement** with shareable data/code archived where possible, and conservation
recommendations that **bridge science and practice** without over-claiming.

---

## What Is Conservation Biology, and Why a Dedicated Stack?

Conservation Biology's constraints differ from a general ecology journal or a methods journal:

| Constraint            | Conservation Biology                                                          | Implication                                                       |
|-----------------------|-------------------------------------------------------------------------------|------------------------------------------------------------------|
| Premium on            | **Direct conservation relevance** + novelty + transferability                 | A sound but inconsequential study is off-fit                     |
| Scope                 | Conserving **biological diversity** — ecology + practice + policy             | The result must inform a real conservation decision              |
| Methods               | Field ecology, modeling, synthesis, human dimensions — judged on own terms    | Match design to the question; don't force one template           |
| Publisher / owner     | **Wiley** / **Society for Conservation Biology (SCB)**                         | Submit via **ScholarOne Manuscript Central**, not Editorial Manager |
| Review model          | **Double-blind** (adopted 2014)                                               | Anonymize manuscript *and* author identities                     |
| Length                | Contributed Papers **7,000** in current Wiley listings; **abstract ≤ 300**     | Word count runs Abstract → Literature Cited (excludes tables)    |
| Exhibits              | About **one table/figure per four pages** of text                             | Every exhibit must earn its space; rest goes to SI               |
| Transparency          | **Data-availability statement**; shareable data/code deposit encouraged        | Build the package as you go; protect sensitive species data      |
| Sensitive data        | Mask precise locations of threatened / trafficked taxa                        | A map must not aid poaching or disturbance                       |

Use [`resources/official-source-map.md`](resources/official-source-map.md) for the source trail behind
these claims. The final upload-week check belongs on the live Wiley Instructions for Authors page,
especially for article-type availability, caps beyond Contributed Papers, declarations, and production
file prompts.

### Main article types

- **Contributed Papers** — full empirical study, IMRAD, broad relevance (current Wiley listings show
  7,000 words).
- **Research Notes** — focused or preliminary contributions.
- **Reviews** — comprehensive synthesis of a well-developed literature.
- **Essays** — forward-looking, evidence-grounded arguments on conservation issues.
- **Conservation Practice and Policy** — applied tools, policy, and management lessons.
- **Comments / Diversity / Letters** — short formats (no abstract). Registered Reports where offered.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/conbio-skills
/plugin install conbio-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/conbio-skills.git
cd conbio-skills

mkdir -p ~/.claude/skills && cp -R skills/conbio-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/conbio-* ~/.codex/skills/
```

### First Prompt

```
Use conbio-workflow to tell me which skill I should use next for my Conservation Biology manuscript.
```

---

## Default Workflow

```text
conbio-topic-selection
        ▼
conbio-literature-positioning
        ▼
conbio-study-design
        ▼
conbio-data-analysis
        ▼
conbio-figures-and-tables
        ▼
conbio-reporting-and-data-policy
        ▼
conbio-writing-style          (polish)
        ▼
conbio-conservation-relevance-and-implications
        ▼
conbio-review-process
        ▼
conbio-submission
        ▼
conbio-revision-and-rebuttal
```

`conbio-workflow` is the router — it tells you which skill to use next based on where you are. If your
design is **prospective**, route to `conbio-review-process` early to consider the **Registered Reports**
track; most papers loop design ↔ analysis ↔ conservation relevance before final writing.

---

## Skills

| Skill                                            | Purpose                                                                       |
|--------------------------------------------------|-------------------------------------------------------------------------------|
| `conbio-workflow`                                | Router — decides which sub-skill to invoke next                               |
| `conbio-topic-selection`                         | Conservation-relevance fit; novelty + transferability; pick the article type  |
| `conbio-literature-positioning`                  | Engage the conservation literatures; state the gap precisely                  |
| `conbio-study-design`                            | Defend the design — detection, scale, counterfactuals, modeling, synthesis    |
| `conbio-data-analysis`                           | Appropriate models, honest uncertainty, robustness, reproducibility           |
| `conbio-figures-and-tables`                      | Self-contained, accessible exhibits and maps; mask sensitive locations        |
| `conbio-reporting-and-data-policy`               | Data-availability statement + shareable data/code archive; restricted data     |
| `conbio-writing-style`                           | Journal Style Guide; accessible prose within the per-type word cap            |
| `conbio-conservation-relevance-and-implications` | Sharpen the so-what; actionable, transferable recommendations                 |
| `conbio-review-process`                          | Double-blind review, editorial screening, decision categories, Registered Reports |
| `conbio-submission`                              | ScholarOne preflight (anonymization, caps, Style Guide, data statement)       |
| `conbio-revision-and-rebuttal`                   | Response-letter strategy for multiple reviewers + handling editor             |

### Resources

- [`resources/external_tools.md`](resources/external_tools.md) — conservation data sources (GBIF / IUCN Red List / WDPA / Movebank / Global Forest Watch) + R / Python / GIS and synthesis tooling
- [`resources/official-source-map.md`](resources/official-source-map.md) — official Wiley / SCB URLs behind every journal-specific fact and upload-week live-check boundary

---

## What This Repo Does Not Do

- It does not write a submittable manuscript for you
- It does not simulate any specific editor's or reviewer's taste
- It does not freeze upload-week metadata such as article-type availability, all per-type caps, file prompts, or masthead details; check the official page before submission
- It does not decide whether your result has genuine conservation relevance — that is the researcher's call

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [Conservation Biology (Wiley Online Library)](https://conbio.onlinelibrary.wiley.com/journal/15231739) — publisher home
- [Conservation Biology at SCB](https://conbio.org/publications/conservation-biology/) — owner society, journal information

---

## License

MIT
