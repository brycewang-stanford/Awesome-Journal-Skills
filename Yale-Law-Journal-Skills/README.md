# Yale Law Journal Skills

<p align="center">
  <img src="assets/cover.svg" alt="The Yale Law Journal cover" width="200">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-YLJ-16335c)](https://yalelawjournal.org/)
[![Field](https://img.shields.io/badge/field-Law-1f6feb)](https://law.yale.edu/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for legal scholarship targeted at **The Yale Law Journal (YLJ)** — the **student-edited
flagship law review of Yale Law School**, one of the most-cited legal publications in the United States.
YLJ is a **generalist** review: it publishes **Articles, Essays, Features, and book reviews** by
professional legal scholars, **student-written Notes and Comments**, and the online **YLJ Forum**.

This repository is opinionated. It is **not** a generic academic-writing toolbox and **not** a
peer-review pack repurposed for law. A student-edited law review works differently from a peer-reviewed
journal: authors submit a **near-final, heavily-footnoted, Bluebook-compliant** manuscript; **student
editors** evaluate it **anonymized** and, on acceptance, run an intensive edit and **source-pull** that
verifies every footnote by hand. This stack encodes that reality — the **preemption check**, the
**doctrine→theory→normative** argument arc, the **Bluebook footnote apparatus**, **YLJ's own submission
portal** (not Scholastica), and the **expedite** rules that diverge from the rest of the market.

---

## What Is YLJ, and Why a Dedicated Stack?

YLJ's constraints differ from a peer-reviewed journal and even from other law reviews:

| Constraint | YLJ | Implication |
|---|---|---|
| Editing model | **Student-edited** (Yale Law School); **not peer-reviewed** | Submit a finished article, not a draft to co-develop |
| Scope | **Generalist** legal scholarship | The claim must reach the whole profession, not one niche |
| Review | **Anonymized** (Articles & Essays Committee) | Remove all identity/prestige cues; reputation is invisible |
| Submission portal | **YLJ's own online system** — **not Scholastica/ExpressO** | Submit/expedite YLJ through its portal; multi-submit elsewhere via Scholastica |
| Expedite | **No competitive advantage** at YLJ | An outside offer does not move you up the queue |
| House style | **Bluebook** + the Journal's own citation requirements | Pinpoint cites; quotations marked; complete apparatus at submission |
| Verification | **Source-pull** of every footnote on acceptance | Cites must exist, pinpoint, and actually support the sentence |
| Length (encouraged, incl. footnotes) | **Article < 25k**, **Essay < 15k**, **Forum < 10k**; student **Note ~20k** / **Comment ~7k** | Over-length weighs against acceptance |
| Online companion | **YLJ Forum** (since 2005; relaunched 2014) | Short, timely pieces and responses go online |

Volatile specifics (exact caps per volume, fee, season dates, portal mechanics) change — items not
directly confirmed are marked **待核实** in [`resources/official-source-map.md`](resources/official-source-map.md).
**Verify on the official journal page.**

### Publication tracks

- **Articles** — original scholarship by professional authors; encouraged **< 25,000 words** incl. footnotes.
- **Essays** — shorter, more pointed professional pieces; encouraged **< 15,000 words** incl. footnotes.
- **Features** — curated collections / symposium contributions.
- **Notes & Comments** — long- and short-form scholarship by **Yale Law students** (Notes Development support).
- **YLJ Forum** — short, timely online pieces and responses; encouraged **< 10,000 words** incl. footnotes.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/yale-law-journal-skills
/plugin install yale-law-journal-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/yale-law-journal-skills.git
cd yale-law-journal-skills

mkdir -p ~/.claude/skills && cp -R skills/ylj-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/ylj-* ~/.codex/skills/
```

### First Prompt

```
Use ylj-workflow to tell me which skill I should use next for my Yale Law Journal piece.
```

---

## Default Workflow

```text
ylj-topic-selection
        ▼
ylj-thesis-and-contribution
        ▼
ylj-preemption-check
        ▼
ylj-argument-structure
        ▼
ylj-sources-and-bluebook
        ▼
ylj-writing-style              (polish)
        ▼
ylj-placement-strategy
        ▼
ylj-submission
        ▼
ylj-student-editor-review       (on acceptance)
        ▼
ylj-revision-and-editing        (+ YLJ Forum path)
        ▼
ylj-footnotes-and-cite-check    (built throughout; final verify)
```

`ylj-workflow` is the router — it tells you which skill to use next based on stage and track. The
**footnote apparatus is built throughout**, not at the end; `ylj-footnotes-and-cite-check` runs both
before submission and again during the editorial source-pull. If your idea is timely or responds to a
recent YLJ article, route to `ylj-revision-and-editing` for the **Forum** path.

---

## Skills

| Skill | Purpose |
|---|---|
| `ylj-workflow` | Router — decides which sub-skill to invoke next; picks the track |
| `ylj-topic-selection` | Generalist-significance fit; pick Article / Essay / Feature / Note / Comment / Forum |
| `ylj-thesis-and-contribution` | Forge a single contestable claim; name the contribution type |
| `ylj-preemption-check` | SSRN / Westlaw / HeinOnline novelty sweep; write the "what's new" paragraph |
| `ylj-argument-structure` | Sequence Parts as doctrine → theory → normative; steelman objections |
| `ylj-sources-and-bluebook` | Build pinpoint, Bluebook-correct cites for every assertion |
| `ylj-writing-style` | Generalist-legible prose; keep the argument in the text, support in footnotes |
| `ylj-placement-strategy` | Multi-submit + season timing + YLJ's own-portal / no-advantage expedite rules |
| `ylj-student-editor-review` | The anonymized Committee read, Notes Development, and the source-pull |
| `ylj-submission` | YLJ-portal preflight (anonymization, length, apparatus, materials) |
| `ylj-revision-and-editing` | The intensive student edit cycle + the YLJ Forum online path |
| `ylj-footnotes-and-cite-check` | Final footnote audit: existence, support, pinpoint, Bluebook form |

### Resources

- [`resources/external_tools.md`](resources/external_tools.md) — legal-research databases (Westlaw / Lexis / HeinOnline / SSRN / CourtListener / Congress.gov / govinfo) + Bluebook and cite-checking tooling
- [`resources/official-source-map.md`](resources/official-source-map.md) — official YLJ URLs behind every fact, with 待核实 markers on unverified items
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — a before→after YLJ introduction (fictional, illustrative)
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — real, web-verified YLJ pieces by contribution type, with a sibling-review guardrail

---

## What This Repo Does Not Do

- It does not write a submittable manuscript for you
- It does not simulate any specific student editor's or committee's taste
- It does not assert volatile metadata (exact caps per volume, fee, season dates, portal mechanics) — verify on the official page; unverified items are marked 待核实
- It does not decide whether your claim is of general significance — that is the author's call
- It does not give legal advice; it is a scholarship-craft toolkit

---

## Differences vs. sibling law reviews

| Dimension | YLJ | Typical peer-reviewed journal | Many other law reviews |
|---|---|---|---|
| Editors | Yale Law **students** | Faculty peer reviewers | Students (other schools) |
| Review | **Anonymized**, on a finished piece | Peer review, developmental rounds | Often via **Scholastica** |
| Submission portal | **Own online system** | Editorial Manager / OUP etc. | Commonly **Scholastica/ExpressO** |
| Expedite | **No queue advantage** | n/a | Often used to leverage offers |
| Style | **Bluebook** | APA / Chicago / journal style | Bluebook |
| Verification | **Source-pull** of every footnote | Methods/data review | Cite-check varies |

(Yale's *other* student journals — Yale Law & Policy Review, Yale Journal on Regulation, etc. — are
separate venues with their own rules; do not import YLJ's policies to them.)

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [The Yale Law Journal](https://yalelawjournal.org/) — journal home, submissions, the Forum
- [Yale Law School](https://law.yale.edu/) — the Journal's affiliated institution

---

## License

MIT
