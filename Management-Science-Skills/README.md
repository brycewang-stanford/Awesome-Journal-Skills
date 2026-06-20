# Management Science Skills

<p align="center">
  <img src="assets/cover.svg" alt="Management Science cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Management%20Science-1b3a6b)](https://pubsonline.informs.org/journal/mnsc)
[![Publisher](https://img.shields.io/badge/publisher-INFORMS-1b3a6b)](https://www.informs.org/)
[![Index](https://img.shields.io/badge/index-FT50%20%7C%20UTD24-1f6feb)](https://pubsonline.informs.org/journal/mnsc)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **Management Science** — the **INFORMS** flagship, established in **1954** by the precursor Institute of Management Sciences (TIMS).

This repository is opinionated. It is **not** a generic "management writing" toolbox. It is a **Management Science-specific** stack built around the journal's defining feature: it is deliberately **bimethodological**, placing rigorous **analytical/quantitative** modeling (operations research, optimization, stochastic processes, game and economic theory) **side by side** with **empirical** work (econometrics, lab/field experiments, behavioral studies, data science), across every functional business area — accounting, finance, marketing, operations, information systems, strategy, entrepreneurship, organizations, behavioral economics. Submissions are routed through a **Department / area-editor** structure, and the unifying bar is **rigor plus a decision-relevant contribution that travels across departments**.

> Durable norms only. The Editor-in-Chief, the submission fee, exact page limits, the department roster, and policies change — always verify on the official Management Science submission guidelines and the Code and Data Disclosure Policy pages on INFORMS PubsOnline.

---

## Why a Separate Management Science Skill Stack?

Management Science imposes constraints that differ materially from single-method or theory-only journals:

| Constraint              | Management Science                                                | Implication                                                       |
|-------------------------|------------------------------------------------------------------|------------------------------------------------------------------|
| Methodology             | **Bimethodological** — analytical modeling *and* empirical, equally | Pick the right lane; meet that lane's rigor bar                |
| Routing                 | **Department / area-editor** structure; the DE owns the desk screen | Wrong Department or wrong literature → wrong desk               |
| Core bar                | Rigor **plus** a decision-relevant insight that travels across departments | A correct model with no managerial reading is off-mission     |
| Fit                     | Must belong here vs **Operations Research / M&SOM / Marketing Science** | DE/AE first screen for department fit and merit                 |
| Review                  | **Double-anonymized**; AE recruits reviewers after initial screen | Anonymize fully; disclose proceedings versions anonymously       |
| Transparency            | **Code and Data Disclosure** + AsCollected project page | Build a regenerating replication package from day one         |
| Fee                     | **$79** per submission (Aug 1, 2025), member / low-income / honor waivers | Pay or claim a waiver; no justification needed for the honor waiver |
| Length                  | No initial limit; prefers **short, focused** papers; invited revisions capped | Tight notation and a lean main body; offload to the online appendix |
| Style                   | **Author-year** citations; 11-pt, 1-inch; abstract ≤ 250 words, 3–5 keywords | Configure the reference manager to name–date                  |

Generic "scientific writing" or "social-science methods" packs do not address these constraints.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/mgsci-skills
/plugin install mgsci-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/mgsci-skills.git
cd mgsci-skills

mkdir -p ~/.claude/skills && cp -R skills/mgsci-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/mgsci-* ~/.codex/skills/
```

### First Prompt

```
Use mgsci-workflow to tell me which skill I should use next for my Management Science manuscript.
```

---

## Default Workflow

```text
mgsci-topic-selection
        ▼
mgsci-theory-development
        ▼
mgsci-literature-positioning
        ▼
mgsci-methods
        ▼
mgsci-data-analysis
        ▼
mgsci-contribution-framing
        ▼
mgsci-tables-figures
        ▼
mgsci-writing-style        (polish)
        ▼
mgsci-submission
        ▼
mgsci-review-process
        ▼
mgsci-rebuttal
```

`mgsci-workflow` is the router — it tells you which skill to use next, and which Department lane (analytical vs empirical) you are in.

---

## Skills

| Skill                          | Purpose                                                                          |
|--------------------------------|----------------------------------------------------------------------------------|
| `mgsci-workflow`               | Router — decides which sub-skill to invoke next and which lane you are in         |
| `mgsci-topic-selection`        | Decision-relevance bar + Department fit (vs Operations Research / M&SOM / Marketing Science) |
| `mgsci-theory-development`     | Analytical model (assumptions → propositions → comparative statics) **or** a priori hypotheses |
| `mgsci-literature-positioning` | Joining the right Department's conversation; problematization; author-year citing |
| `mgsci-methods`                | Matching an analytical or empirical design to the question and the Department standard |
| `mgsci-data-analysis`          | Proofs + numerics **or** identification/estimation + robustness; disclosure package |
| `mgsci-contribution-framing`   | Decision-relevant insight that travels across departments; the fit case            |
| `mgsci-tables-figures`         | Comparative-statics figures / result tables; self-contained, notation-lean exhibits |
| `mgsci-writing-style`          | Front-loaded result, notation paired with intuition, author-year house style       |
| `mgsci-submission`             | ScholarOne seven-step preflight: anonymization, fee/waivers, disclosure package    |
| `mgsci-review-process`         | Department desk screen, high desk-reject, double-anonymized review, fit bar         |
| `mgsci-rebuttal`               | R&R revision and point-by-point response; page cap and disclosure update           |

### Resources

- [`resources/external_tools.md`](resources/external_tools.md) — analytical tooling (Gurobi / CPLEX / JuMP / Mathematica) and empirical tooling (Stata / R / Python / oTree / Prolific) plus the Data-and-Code-Disclosure package recipe
- [`resources/official-source-map.md`](resources/official-source-map.md) — official INFORMS/Management Science URLs behind current process facts (accessed 2026-06-20)

---

## Verified Facts (confirm current values)

- **Publisher / lineage:** INFORMS; established **1954** by the precursor Institute of Management Sciences (TIMS).
- **Editor-in-Chief:** Christoph H. Loch, term **Jan 1, 2024 – Dec 31, 2026**.
- **Portal:** ScholarOne Manuscripts at **mc.manuscriptcentral.com/mnsc**; seven-step upload.
- **Abstract:** ≤ **250 words**; **3–5 keywords**.
- **Style:** **author-year** in-text citations (e.g., Norman 1977); 11-pt, 1-inch margins; PDF preferred.
- **Length:** no formal initial limit; invited revisions ≤ **47 pages double-spaced** or **32 pages 1.5-spaced**, online appendix excluded.
- **Fee:** **$79** per original submission (effective Aug 1, 2025); INFORMS-member, low-/lower-middle-income-economy, and honor-based waivers.
- **Transparency:** **Code and Data Disclosure Policy** (effective June 1, 2019; revised April 20, 2026); authors provide an **AsCollected** project-page URL at submission, and accepted numerical/computational papers provide data, programs, and details sufficient to permit replication before production.

See [`resources/official-source-map.md`](resources/official-source-map.md) for the official INFORMS source trail.

---

## Differences vs. Sister INFORMS Journals

| Dimension          | Management Science                               | Operations Research          | M&SOM                          | Marketing Science            |
|--------------------|--------------------------------------------------|------------------------------|--------------------------------|------------------------------|
| Core contribution  | Decision-relevant insight that **travels across departments** | New OR method / theory       | Supply-chain & service ops     | Quantitative-marketing models |
| Methodology        | Analytical **and** empirical, side by side       | Predominantly analytical/OR  | Analytical + empirical ops     | Models of consumer/firm behavior |
| Best fit           | Cross-department managerial-science results      | Methodological OR advances   | Operations management focus    | Marketing focus              |

If the core contribution is a methodology with limited managerial reading, target **Operations Research**; if it is supply-chain/service operations, **M&SOM**; if it is quantitative marketing, **Marketing Science**.

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — index of journal-specific skill packs

---

## License

MIT
