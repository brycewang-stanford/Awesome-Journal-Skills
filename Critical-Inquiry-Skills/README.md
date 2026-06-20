# Critical Inquiry Skills

<p align="center">
  <img src="assets/cover.svg" alt="Critical Inquiry cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Critical%20Inquiry-1a1a1a)](https://criticalinquiry.uchicago.edu/)
[![Field](https://img.shields.io/badge/field-Criticism%20%26%20Theory-8c2f39)](https://www.journals.uchicago.edu/journals/ci/about)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for essays targeted at **Critical Inquiry (CI)** — the leading **interdisciplinary
journal of criticism and theory** in the arts and humanities, founded in **1974** by Wayne Booth,
Arthur Heiserman, and Sheldon Sacks, and published by the **University of Chicago Press**. CI is
"associated with no single school of thought, tied to no single discipline." It publishes the best
critical thinking across **literary theory, art and visual culture, film and media, philosophy and
aesthetics, politics and political theory, history, and cultural criticism** — and has been called
"academe's most prestigious theory journal."

This repository is opinionated. It is **not** a generic humanities writing toolbox, and it is **not** a
literature-department close-reading pack. CI is **interdisciplinary theory**: the unit is a **bold
theoretical intervention** that reorients a conversation across fields, tested on **objects read
closely** — texts, images, artworks, films, cases — with **theory doing real work** and **prose worthy
of the claim**. There are **no datasets, no statistics, no replication packages** here.

---

## What Is Critical Inquiry, and Why a Dedicated Stack?

CI's constraints differ from a field journal, a methods journal, or a social-science venue:

| Constraint            | Critical Inquiry                                                              | Implication                                                       |
|-----------------------|-------------------------------------------------------------------------------|------------------------------------------------------------------|
| Scope                 | **Interdisciplinary criticism and theory**, arts & humanities                 | The essay must speak past one department                         |
| Premium on            | A **theoretical intervention** with cross-field stakes                        | A competent close reading with no stakes is off-fit              |
| Evidence              | **Objects read closely** — texts, images, artworks, films, cases (no data)    | No datasets, no statistics, no replication                       |
| Theory                | Used as an **instrument** that does work on the object                        | Jargon-as-decoration is the classic failure                      |
| Publisher             | **University of Chicago Press**; CI founded in 1974                           | Submitted via **Editorial Manager** (`editorialmanager.com/ci/`) |
| Review model          | **Peer-reviewed**; read by editors-in-chief with the editorial team           | Persuade serious generalist critics, not just specialists        |
| Submission rule       | **No multiple / simultaneous submission**                                     | Submit to CI alone                                               |
| Length                | **Article ≤ 9,500 words** (incl. discursive notes + **all** bibliographical info) | Count the notes — they are in the budget                     |
| Other formats         | **Critical Response ≤ 3,000**; **Review ≤ 500**                               | Choose the right format up front                                 |
| Citations             | **Chicago Manual of Style (17th ed.)** footnotes; **no works-cited list**     | Not author-date; full info lives in the notes                    |
| Manuscript / images   | **Microsoft Word**; images as **separate 300 ppi JPEG/TIFF**, author-cleared  | Clear image permissions yourself, early                          |
| Fee                   | No separate submission fee listed; optional Gold OA fee **$2,500**            | Live-check OA only if selecting Gold OA                           |

`resources/official-source-map.md` was refreshed on 2026-06-20 from the CI submissions, overview, and
editorial-staff pages. It records current editors, caps, Gold OA terms, CMOS wording, permissions, and
the live-check items to reopen immediately before upload.

### Three submission formats

- **Article** — the journal's main form: a full interdisciplinary argument, **≤ 9,500 words**
  (including discursive notes and all bibliographical information).
- **Critical Response** — a focused reply to or debate with a published CI piece, **≤ 3,000 words**.
- **Review** — a short notice of a book or exhibition, **≤ 500 words**.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/ci-skills
/plugin install ci-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/ci-skills.git
cd ci-skills

mkdir -p ~/.claude/skills && cp -R skills/ci-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/ci-* ~/.codex/skills/
```

### First Prompt

```
Use ci-workflow to tell me which skill I should use next for my Critical Inquiry essay.
```

---

## Default Workflow

```text
ci-topic-selection
        ▼
ci-scholarly-positioning
        ▼
ci-argument-and-intervention
        ▼
ci-evidence-and-objects
        ▼
ci-theory-and-method
        ▼
ci-structure-and-exposition
        ▼
ci-writing-style            (polish)
        ▼
ci-citation-and-style
        ▼
ci-review-process
        ▼
ci-submission
        ▼
ci-revision-and-response
```

`ci-workflow` is the router — it tells you which skill to use next based on where you are. CI essays
rarely move in a straight line: most loop **argument ↔ objects ↔ theory** several times before the
prose settles. If you are writing a **Critical Response**, the argument and positioning skills carry
most of the weight; a **Review** goes almost directly to writing-style and submission.

---

## Skills

| Skill                          | Purpose                                                                       |
|--------------------------------|-------------------------------------------------------------------------------|
| `ci-workflow`                  | Router — decides which sub-skill to invoke next                               |
| `ci-topic-selection`           | CI fit: a theoretical intervention with cross-field stakes; pick the format   |
| `ci-scholarly-positioning`     | Name the conversation(s) entered across fields; locate the intervention       |
| `ci-argument-and-intervention` | Forge the central claim into a real intervention, not a reading               |
| `ci-evidence-and-objects`      | Choose and read the objects — texts, images, artworks, cases — closely        |
| `ci-theory-and-method`         | Deploy theory as an instrument that does work; make the method visible        |
| `ci-structure-and-exposition`  | Architect long-form humanistic prose (not IMRaD) for a cross-field reader     |
| `ci-writing-style`             | Ambitious, lucid prose within the word cap (notes counted)                    |
| `ci-citation-and-style`        | Chicago (17th ed.) footnotes, no works-cited list; 300 ppi images, permissions|
| `ci-review-process`            | Peer + editorial review, the ambition bar, no-simultaneous-submission rule    |
| `ci-submission`                | Editorial Manager preflight (cap incl. notes, Word file, images, permissions) |
| `ci-revision-and-response`     | Revision strategy + response letter to readers and editors                    |

### Resources

- [`resources/external_tools.md`](resources/external_tools.md) — archives, text and image sources (HathiTrust / museum open access / Artstor / EEBO), the theory and criticism reference shelf, Chicago-notes and image-prep tooling
- [`resources/official-source-map.md`](resources/official-source-map.md) — official CI / University of Chicago Press URLs behind every fact, refreshed 2026-06-20

---

## What This Repo Does Not Do

- It does not write a submittable essay for you
- It does not simulate any specific editor's or reader's taste
- It does not turn criticism into data — no datasets, no statistics, no replication
- It does not freeze volatile metadata forever; reopen the official source map before advising on editors, caps, OA fees, CMOS wording, permissions, or submission routing
- It does not decide whether your idea is a genuine intervention — that is the critic's call

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [Critical Inquiry (journal site)](https://criticalinquiry.uchicago.edu/) — submissions, editors, info
- [Critical Inquiry (University of Chicago Press)](https://www.journals.uchicago.edu/journals/ci/about) — publisher home, about, current issue

---

## License

MIT
