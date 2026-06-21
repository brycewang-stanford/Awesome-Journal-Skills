# Manufacturing & Service Operations Management (M&SOM) Skills

<p align="center">
  <img src="assets/cover.svg" alt="Manufacturing & Service Operations Management cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-M%26SOM-0a3d62)](https://pubsonline.informs.org/journal/msom)
[![Publisher](https://img.shields.io/badge/publisher-INFORMS%20%7C%20MSOM%20Society-1f6feb)](https://msomsociety.org/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **Manufacturing & Service Operations Management (M&SOM)** — the premier *operations-management* journal, published by **INFORMS** and sponsored by the **MSOM Society**.

This repository is opinionated. It is **not** a generic "OR writing" toolbox. It is an **M&SOM-specific** stack built around M&SOM's defining gate: an **operations decision or problem must be central to the contribution**, executed at top-tier rigor — whether the work is **analytical/stochastic modeling** (optimization, queueing, stochastic models, game theory, revenue management) or **rigorous empirical OM / data-driven analytics**. It covers OM-centered topic selection, model and mechanism development, literature positioning, methodology and identification, analysis and replicability, contribution framing, INFORMS house-style exhibits and prose, the author-routed Department-Editor ScholarOne submission, the double-anonymous review process, and R&R rebuttals.

> Durable norms only. Editors, department rosters, portal payment prompts, and special-track dates move over time; check the official M&SOM submission-guidelines page, editorial-board page, and INFORMS style files before an actual submission.

---

## Why a Separate M&SOM Skill Stack?

M&SOM imposes constraints that differ materially from theory-only management journals or general OR venues:

| Constraint              | Manufacturing & Service Operations Management              | Implication                                                       |
|-------------------------|------------------------------------------------------------|-------------------------------------------------------------------|
| Discipline              | Operations management (manufacturing & services)           | An operations decision must be central, not a backdrop            |
| Core gate               | Operations-centrality + top-tier execution                 | Strong analytics/finance/marketing papers are desk-screened off-fit |
| Methodology             | Analytical/stochastic modeling **and** empirical OM        | The method must deliver an operational insight                    |
| Routing                 | Author-chosen **Department** + two preferred DEs           | Fit means matching the right department, not a generalist pool    |
| Review                  | **Double-anonymous**; DE → AE → referees                   | Strict anonymization; DE/AE priorities lead                       |
| Length                  | **32-page typeset cap** incl. references/tables/figures/appendices | Mechanically enforced on the official template; exhibits cost pages |
| Supplement              | **≤ 16-page** online supplement                            | Proofs and extra studies live here                                |
| Abstract                | **Structured, ≤ 300 words**, three required sections       | Managerial implications is a required section, not framing        |
| Style                   | INFORMS author-year (style file v1.6)                      | Not APA; reference ordering is specific                           |
| Replicability           | INFORMS data/code disclosure; licensed-data access instructions | Be ready to share/retain data; ship code for licensed sources  |

Generic "scientific writing" or "OR methods" packs do not address these constraints.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/msom-skills
/plugin install msom-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/msom-skills.git
cd msom-skills

mkdir -p ~/.claude/skills && cp -R skills/msom-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/msom-* ~/.codex/skills/
```

### First Prompt

```
Use msom-workflow to tell me which skill I should use next for my M&SOM manuscript.
```

---

## Default Workflow

```text
msom-topic-selection

        ▼
msom-theory-development
        ▼
msom-literature-positioning
        ▼
msom-methods
        ▼
msom-data-analysis
        ▼
msom-contribution-framing
        ▼
msom-tables-figures
        ▼
msom-writing-style        (polish)
        ▼
msom-submission
        ▼
msom-review-process
        ▼
msom-rebuttal
```

`msom-workflow` is the router — it tells you which skill to use next based on where you are.

---

## Skills

| Skill                         | Purpose                                                                       |
|-------------------------------|-------------------------------------------------------------------------------|
| `msom-workflow`               | Router — decides which sub-skill to invoke next                               |
| `msom-topic-selection`        | Operations-centrality gate + analytical-vs-empirical lane + Department fit    |
| `msom-theory-development`     | Analytical model / operational mechanism; structural results                  |
| `msom-literature-positioning` | Joining the OM conversation; routing to the right Department                   |
| `msom-methods`                | Matching solution/identification to the operations decision                   |
| `msom-data-analysis`          | Proofs + numerical studies; identified effects; INFORMS replicability policy  |
| `msom-contribution-framing`   | Explicit operational insight + M&SOM structured abstract                      |
| `msom-tables-figures`         | Policy/sensitivity and results exhibits in INFORMS style within the page cap  |
| `msom-writing-style`          | Lead with the insight; control notation; INFORMS author-year; 32-page cap     |
| `msom-submission`             | ScholarOne preflight: anonymization, template, Department routing, data/code  |
| `msom-review-process`         | Six-department routing, double-anonymous review, special tracks               |
| `msom-rebuttal`               | R&R revision around DE/AE priorities + point-by-point response                |

### Resources

- [`skills/msom-submission/templates/manuscript_template.md`](skills/msom-submission/templates/manuscript_template.md) — M&SOM manuscript skeleton
- [`skills/msom-submission/templates/checklist.md`](skills/msom-submission/templates/checklist.md) — pre-submission self-check
- [`resources/external_tools.md`](resources/external_tools.md) — OM modeling/solver tools (Gurobi / CPLEX / MOSEK / AMPL / Pyomo / JuMP), simulation (AnyLogic / SimPy), and empirical OM (Stata / R / Python causal-inference)
- [`resources/official-source-map.md`](resources/official-source-map.md) — official INFORMS/M&SOM URLs behind every fact (accessed 2026-06-20)

---

## Distinctive M&SOM Norms

- **Operations-centrality gate** — an operations decision/problem must be the primary contribution; otherwise-strong analytics/marketing/finance papers are desk-screened.
- **Author-routed six departments** — Manufacturing & Supply Chain Operations; Services, Platforms & Revenue Management; Environment, Health & Society; Operational Innovation; Analytics in OM; and a **Practice Platform**. You name two preferred Department Editors (with a Manufacturing-and-Supply-Chain first/second rule).
- **Practice & perspective tracks** — a dedicated Practice Platform plus **OM Forum** banner pieces institutionalize field-driven and thought-leadership OM.
- **Hard 32-page typeset cap** counting *everything*, plus a separate **16-page** online supplement — stricter and more mechanical than narrative word-limit journals.
- **Mandatory structured abstract** (Problem definition / Methodology-results / Managerial implications), ≤ 300 words, jargon-free.
- **Society-and-conference coupling** — sponsored by the MSOM Society and tied to the MSOM Conference, with the **OM Grand Challenges (2026)** conference-to-journal special-issue fast-track.

---

## Differences vs. Management Science / Operations Research / POM

| Dimension          | M&SOM                                  | Management Science          | Operations Research            | POM (POMS)                   |
|--------------------|----------------------------------------|-----------------------------|--------------------------------|------------------------------|
| Core contribution  | Operations decision is **central**     | Broad OR/management         | Method/model can be the point  | OM, broad                    |
| Methods            | Analytical **and** empirical OM        | Many, incl. OM department   | OR methodology                 | Analytical & empirical OM    |
| Publisher/society  | INFORMS / MSOM Society                  | INFORMS                     | INFORMS                        | POMS / Wiley                 |
| Regular submission fee | Not listed on M&SOM author guidelines; check ScholarOne payment screen | $79 fee (from Aug 2025) | INFORMS | Varies by journal |

If an operations decision is not the centerpiece, M&SOM is the wrong venue.

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — index of journal-specific skill packs

---

## License

MIT
