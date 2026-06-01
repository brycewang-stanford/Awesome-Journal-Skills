# MIS Quarterly (MISQ) Skills

<p align="center">
  <img src="assets/cover.svg" alt="MIS Quarterly cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-MISQ-7a1f2b)](https://misq.umn.edu/)
[![Index](https://img.shields.io/badge/index-AIS%20Senior%20Scholars'%20Basket-1f6feb)](https://misq.umn.edu/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **MIS Quarterly (Management Information Systems Quarterly, MISQ)** — a leading *information systems* journal, published by the MIS Research Center (MISRC) at the Carlson School of Management, University of Minnesota, and an official journal of the **Association for Information Systems (AIS)**. It appears quarterly (March, June, September, December).

This repository is opinionated. It is **not** a generic "tech writing" or "social-science methods" toolbox. It is a **MISQ-specific** stack built around MISQ's defining trait: it is **pluralistic across four IS research traditions — behavioral, design science, economics, and organizational** — and rewards a rigorous theory contribution within any of them, including cross-tradition blends. Crucially, MISQ is the canonical home of **IS design science research** (the Hevner et al. 2004 lineage), a contribution mode absent from most behavioral-only top journals. The stack covers tradition-aware topic selection, theory/design-theory development, literature positioning, genre-matched design and analysis, contribution framing, page-limit-aware exhibits and prose, ScholarOne submission with a pluralistic transparency commitment, the Senior-Editor/Associate-Editor double-anonymous review process, and multi-round revision.

> Durable norms only. Editors, fees, exact page limits, the abstract format, and policies change — always verify on the official MISQ submission/instructions pages and the current MISQ Style Guide.

---

## Why a Separate MISQ Skill Stack?

MISQ imposes constraints that differ materially from management, economics, or CS journals:

| Constraint              | MIS Quarterly                                                       | Implication                                                       |
|-------------------------|---------------------------------------------------------------------|------------------------------------------------------------------|
| Discipline              | Information systems — the IT artifact must be central               | Management/economics/CS papers with incidental IT are off-fit    |
| Paradigm                | **Pluralistic**: behavioral, design science, economics, organizational | Pick the tradition; it sets the category, method, and contribution |
| Distinctive genre       | First-class **Design Science** track (Hevner et al. 2004)          | Build *and evaluate* an IT artifact; design principles are the contribution |
| Length                  | **Page** limits that count **everything** (text, tables, figures, refs, appendices) | Over-length manuscripts are returned; supplements discouraged    |
| Categories              | Research Article (50 pp), Research Notes (~half), Theory Development (55 pp), Theory-Generative Research Synthesis (65 pp), Issues & Opinions, Design Science | Self-select the genre up front |
| Transparency            | Pluralistic, genre-appropriate commitment uploaded at submission    | Procedures/code sufficient for replication; not one mandated standard |
| Review                  | **Double-anonymous**; SE + AE then external reviewers; **SE owns the decision** | No identifying info in the manuscript; multi-round revision normal |
| Service                 | By submitting, authors agree to review up to **three papers/year**  | A reciprocal obligation                                          |
| Style                   | MISQ Style Guide; APA 7th; in-text citation **leads with the information, not the author** | Configure your reference manager accordingly |

Generic "scientific writing" or "social-science methods" packs do not address these constraints.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/misq-skills
/plugin install misq-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/misq-skills.git
cd misq-skills

mkdir -p ~/.claude/skills && cp -R skills/misq-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/misq-* ~/.codex/skills/
```

### First Prompt

```
Use misq-workflow to tell me which skill I should use next for my MIS Quarterly manuscript.
```

---

## Default Workflow

```text
misq-topic-selection        (name the IS tradition + category)
        ▼
misq-theory-development      (mechanism / design theory / economic model)
        ▼
misq-literature-positioning
        ▼
misq-methods
        ▼
misq-data-analysis           (+ transparency materials)
        ▼
misq-contribution-framing
        ▼
misq-tables-figures
        ▼
misq-writing-style           (polish)
        ▼
misq-submission              (ScholarOne + transparency commitment)
        ▼
misq-review-process
        ▼
misq-rebuttal
```

`misq-workflow` is the router — it first helps you name which of the four IS traditions your paper lives in, then tells you which skill to use next.

---

## Skills

| Skill                          | Purpose                                                                            |
|--------------------------------|------------------------------------------------------------------------------------|
| `misq-workflow`                | Router — names the IS tradition and decides which sub-skill to invoke next          |
| `misq-topic-selection`         | IS-question fit; choose tradition (behavioral/design/economics/org) + category      |
| `misq-theory-development`      | Mechanism, design theory + design principles, economic model, or process theory     |
| `misq-literature-positioning`  | Join the IS conversation; keep the IT artifact central; vs. ISR/JMIS/JAIS           |
| `misq-methods`                 | Match design or build-and-evaluate strategy to the claim and tradition              |
| `misq-data-analysis`           | SEM/CMB, causal identification, artifact evaluation, qualitative traceability, transparency |
| `misq-contribution-framing`    | State the contribution in the tradition's currency; theory **and** practice         |
| `misq-tables-figures`          | Tradition-specific exhibits sized to the page limit (which counts them)             |
| `misq-writing-style`           | Front-loaded argument, interdisciplinary readability, APA 7 / MISQ style            |
| `misq-submission`              | ScholarOne preflight: Word file, anonymity, category/page cap, transparency commitment |
| `misq-review-process`          | The SE/AE double-anonymous process; reading a decision letter                       |
| `misq-rebuttal`                | Multi-round revision and point-by-point response, SE-letter-first                   |

### Resources

- [`resources/official-source-map.md`](resources/official-source-map.md) — every MISQ fact with its official URL, accessed 2026-06-01, with unverified items marked 待核实
- [`resources/external_tools.md`](resources/external_tools.md) — IS research tools by tradition (platform/digital-trace data, PLS/CB-SEM, causal econometrics, design-science build/evaluate stacks)

---

## The Four IS Traditions (and how the stack adapts)

| Tradition         | The paper's job                                              | Signature method/exhibit                          |
|-------------------|-------------------------------------------------------------|---------------------------------------------------|
| **Behavioral**    | Explain/predict IT adoption, use, and impact                | Experiment/survey; PLS/CB-SEM, CMB remedies       |
| **Design science**| Build **and evaluate** a novel, useful IT artifact          | Build-and-evaluate vs. baselines; design principles |
| **Economics of IS**| Identify causal/economic effects of IT                     | Natural experiment / DiD / IV / RD; robustness     |
| **Organizational**| Theorize IT in organizational and social context            | Case/qualitative; Gioia-style data structure       |

If your paper has no central IT artifact and the technology is interchangeable, MISQ is likely the wrong venue.

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — index of journal-specific skill packs

---

## License

MIT
