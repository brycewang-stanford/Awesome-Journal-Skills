# Progress in Human Geography Skills

<p align="center">
  <img src="assets/cover.svg" alt="Progress in Human Geography cover" width="200">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Progress%20in%20Human%20Geography-29405c)](https://journals.sagepub.com/home/phg)
[![Field](https://img.shields.io/badge/field-Human%20Geography-1f6feb)](https://journals.sagepub.com/home/phg)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **Progress in Human Geography (PiHG)** — the discipline's
**leading review and theory journal**, founded in **1977** (originally at Edward Arnold) and published by
**SAGE**. PiHG is not an outlet for original empirical work: it publishes **critical, agenda-setting
review essays**, commissioned **Progress Reports** that survey a sub-field's recent work, the annual
**Progress in Human Geography Lecture**, and shorter interventions across economic, political, social,
cultural, urban, feminist, and more-than-human geographies. Review is **double-anonymous** via **SAGE
Track**.

This repository is opinionated. It is **not** a generic writing toolbox and it is **not** an empirical
paper pack repurposed for a review journal. It is a **PiHG-specific** stack built for the **review-essay
genre**: a **genuinely synthetic** contribution (not new data or a single case), **command of a large and
contested literature**, **critical-theoretical sophistication**, **conceptual clarity**, and a
**forward-looking intervention** that tells the field where to go next. If your manuscript's core is a
dataset and a finding, this is the wrong journal — and this is the wrong pack.

---

## What Is PiHG, and Why a Dedicated Stack?

PiHG's constraints differ sharply from an empirical human-geography journal:

| Constraint            | Progress in Human Geography                                                     | Implication                                                       |
|-----------------------|--------------------------------------------------------------------------------|------------------------------------------------------------------|
| What it publishes     | **Critical reviews, theory, and agenda-setting essays** — not empirical results | A "study with findings" is off-fit; lead with an argument, not data |
| Premium on            | A **synthetic, forward-looking contribution** that re-orders a literature       | Summary is not enough; you must argue and intervene              |
| Distinctive genres    | **Review articles**, commissioned **Progress Reports**, the **PiHG Lecture**    | Know which genre you are writing; Progress Reports are invited    |
| Publisher / owner     | **SAGE** (since 1977; originally Edward Arnold)                                  | Submitted via **SAGE Track** (ScholarOne-based)                  |
| Review model          | **Double-anonymous** peer review                                                | Anonymize the manuscript and neutralize self-citation            |
| Length                | Review article **4,000–8,000 words**, incl. endnotes, **excl. bibliography**    | Budget the argument tightly; the cap is short for a review       |
| Abstract & keywords   | **Unstructured abstract ~100 words**; **minimum 5 keywords**                    | State the intervention, not just the topic, in ~100 words        |
| Style                 | **SAGE Harvard** author–date referencing                                        | Not Chicago; consistent Harvard throughout                       |
| Exhibits              | **Conceptual** tables/diagrams (typologies, framework maps) — rarely data       | Figures do synthesis work, not report results                    |
| Ethics                | **COPE** member; ORCID; SAGE research-integrity and AI-use policies             | Disclose per policy; declare positionality where relevant        |

Volatile specifics (current editors, exact caps and abstract length, fee/OA options, policy wording)
change — items not directly confirmed are marked **待核实** in
[`resources/official-source-map.md`](resources/official-source-map.md). **Official basis checked
2026-07-16. Verify on the official journal page.**

### The core test (run before anything else)

**PiHG rewards a contribution you cannot get from data.** If a reader asks "what did you find?", you are
writing for the wrong journal. If they ask "how should the field now think about this, and what should it
do next?", you are in the right place — and the rest of this stack helps you make that case.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/phg-skills
/plugin install phg-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/phg-skills.git
cd phg-skills

mkdir -p ~/.claude/skills && cp -R skills/phg-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/phg-* ~/.codex/skills/
```

### First Prompt

```
Use phg-workflow to tell me which skill I should use next for my Progress in Human Geography review essay.
```

---

## Default Workflow

```text
phg-topic-selection
        ▼
phg-theory-building
        ▼
phg-literature-positioning
        ▼
phg-argument-synthesis
        ▼
phg-critical-intervention
        ▼
phg-contribution-framing
        ▼
phg-tables-figures
        ▼
phg-writing-style          (polish)
        ▼
phg-submission
        ▼
phg-review-process
        ▼
phg-rebuttal
```

`phg-workflow` is the router — it tells you which skill to use next based on where you are and whether you
are writing a free-standing **review article** or a commissioned **Progress Report**. Most essays loop
theory ↔ synthesis ↔ intervention several times before writing-style.

---

## Skills

| Skill                          | Purpose                                                                       |
|--------------------------------|-------------------------------------------------------------------------------|
| `phg-workflow`                 | Router — decides which sub-skill to invoke next; picks review article vs. Progress Report |
| `phg-topic-selection`          | Is the topic *review-worthy*? A live, contested literature with stakes, not a gap-filling study |
| `phg-theory-building`          | Build the conceptual apparatus that organizes the review and carries the argument |
| `phg-literature-positioning`   | Map and enter a large, contested literature; define the corpus and its debates |
| `phg-argument-synthesis`       | Turn many sources into one cumulative argument — synthesize, do not annotate    |
| `phg-critical-intervention`    | Make the critical move: name what the field misses and re-order the debate      |
| `phg-contribution-framing`     | Frame a portable, forward-looking agenda — the "so what / what next" for the field |
| `phg-tables-figures`           | Conceptual exhibits: typologies, framework diagrams, synthesis tables (not data) |
| `phg-writing-style`            | PiHG voice; SAGE Harvard; the 8,000-word inclusive cap; ~100-word abstract; 5+ keywords |
| `phg-submission`               | SAGE Track preflight (genre, anonymization, length, abstract, keywords, ORCID) |
| `phg-review-process`           | Double-anonymous review; decision categories; desk-reject triggers for reviews  |
| `phg-rebuttal`                 | Revision response to the editor and referees, strengthening the intervention    |

### Resources

- [`resources/external_tools.md`](resources/external_tools.md) — systematic-review and bibliometric tooling (Zotero, Scopus/Web of Science, VOSviewer/CiteSpace, PRISMA, CAQDAS for qualitative synthesis)
- [`resources/official-source-map.md`](resources/official-source-map.md) — official SAGE / PiHG URLs behind every fact, with 待核实 markers on unverified items
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — landmark human-geography theorists and review/theory works to benchmark the review-essay mode, with a genre guardrail
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — before→after PiHG review-essay introduction (illustrative)

---

## Differences vs. Sibling Journals

| Journal | What it is | Use this pack instead when… |
|---------|------------|------------------------------|
| **Progress in Human Geography** | Discipline's **review/theory flagship**; agenda-setting essays | …you are writing a synthetic, forward-looking review, not reporting data |
| *Annals of the AAG* / *Transactions of the IBG* | broad **empirical** flagships | …your paper's core is an argument about a literature, not a study |
| *Environment and Planning A/D* | theory-heavy **empirical** and conceptual papers | …you are surveying and re-ordering a field, not advancing one case |
| *Geoforum* / *Antipode* | critical **empirical** and theoretical interventions | …the contribution is a state-of-the-art review with an agenda |
| *Progress in Physical Geography* | the physical-geography sibling review journal | …your field is human geography |

---

## What This Repo Does Not Do

- It does not write a submittable review essay for you
- It does not simulate any specific editor's or reviewer's taste
- It does not assert volatile metadata (current editors, exact caps, fee/OA, policy wording) — verify on the official page; unverified items are marked 待核实
- It does not decide whether your topic is review-worthy or whether your intervention is genuinely new — that is the researcher's call

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [Progress in Human Geography (SAGE Journals)](https://journals.sagepub.com/home/phg) — journal home
- [PiHG Submission Guidelines](https://journals.sagepub.com/author-instructions/phg) — author instructions

---

## License

MIT
