# PMLA Skills

<p align="center">
  <img src="assets/cover.svg" alt="PMLA cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-PMLA-1d5b63)](https://www.cambridge.org/core/journals/pmla)
[![Field](https://img.shields.io/badge/field-Literary%20%26%20Language%20Studies-1f6feb)](https://www.mla.org/Publications/Journals/PMLA)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **PMLA (Publications of the Modern Language
Association)** — the **flagship general-interest journal of the Modern Language Association (MLA)**,
one of the oldest scholarly journals in the United States and published by **Cambridge University
Press**. PMLA publishes essays of interest to **scholars and teachers of language and literature**
across the membership: any period, any language, and **all scholarly methods and theoretical
perspectives** — literary criticism, literary theory, comparative literature, and the study of
languages and literatures broadly.

This repository is opinionated, and it is built for the **humanities**. It is **not** a social-science
pack and it is **not** a data/replication toolbox repurposed for literature. There is no dataset, no
statistics, and no replication package here. A PMLA essay is **argument, close reading, theoretical
framing, and engagement with the critical conversation**, written for a broad membership and formatted
in **MLA style** (in-text citations + a Works Cited list per the MLA Handbook). The text is the
evidence.

---

## What Is PMLA, and Why a Dedicated Stack?

PMLA's constraints differ from a narrow specialist journal or a social-science venue:

| Constraint            | PMLA                                                                          | Implication                                                       |
|-----------------------|-------------------------------------------------------------------------------|------------------------------------------------------------------|
| Field                 | **Literary & language studies** — the whole MLA membership                    | The essay must interest readers beyond your specialty            |
| Premium on            | A **significant problem** + implications drawn out                            | A narrow, specialist-only reading is off-fit                     |
| Evidence              | **The text** — close reading, not data or statistics                          | No dataset, no replication; rigor means precise reading          |
| Method                | **All methods and theoretical perspectives** welcome                          | Theory must illuminate texts, not replace reading                |
| Publisher / owner     | **Cambridge University Press** / **MLA**                                       | Submitted via **PMLA's ScholarOne**, not Editorial Manager       |
| Review model          | **Anonymous (blind)** — ≥ 2 reviewers, Editorial Board decides                | Remove first-person self-identification; use a cover sheet       |
| Eligibility           | **MLA membership required** for the author (and all coauthors)                | Join the MLA before you submit                                   |
| Length                | **Articles 6,000–9,000 words**; discursive notes counted                      | Works Cited and translations are excluded from the count         |
| Style                 | **MLA style** per the most recent **MLA Handbook** (in-text + Works Cited)    | Not Chicago/APA; build entries from the core-elements template   |
| AI disclosure         | Cite, at submission, all content created by an **AI tool**                    | Declare AI assistance up front                                   |
| Distinctive features  | Theories and Methodologies · The Changing Profession · Criticism in Translation · Little-known Documents · special-topic issues | Choose the right venue up front |

Volatile specifics (editor and term, exact caps, special-feature deadlines, membership/fee terms)
change — items not directly confirmed are marked **待核实** in
[`resources/official-source-map.md`](resources/official-source-map.md). **Verify on the official
journal page.**

### Venues

- **Regular article** — the main format; **6,000–9,000 words**, a significant problem argued through
  close reading.
- **Theories and Methodologies** — a timely, shorter piece on recent scholarship or a method.
- **The Changing Profession** — on new and emerging fields and the state of the discipline.
- **Criticism in Translation** — a significant critical text made available in English.
- **Little-known Documents** — an archival find presented with scholarly commentary.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/pmla-skills
/plugin install pmla-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/pmla-skills.git
cd pmla-skills

mkdir -p ~/.claude/skills && cp -R skills/pmla-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/pmla-* ~/.codex/skills/
```

### First Prompt

```
Use pmla-workflow to tell me which skill I should use next for my PMLA essay.
```

---

## Default Workflow

```text
pmla-topic-selection
        ▼
pmla-scholarly-positioning
        ▼
pmla-argument-development
        ▼
pmla-textual-evidence-and-close-reading
        ▼
pmla-theory-and-method
        ▼
pmla-structure-and-exposition
        ▼
pmla-writing-style          (polish)
        ▼
pmla-citation-and-style
        ▼
pmla-review-process
        ▼
pmla-submission
        ▼
pmla-revision-and-response
```

`pmla-workflow` is the router — it tells you which skill to use next based on where you are. If you are
writing a **special feature** (Theories and Methodologies, The Changing Profession, Criticism in
Translation, Little-known Documents), route to `pmla-theory-and-method` or
`pmla-textual-evidence-and-close-reading` early to match the venue's expectations.

---

## Skills

| Skill                                       | Purpose                                                                       |
|---------------------------------------------|-------------------------------------------------------------------------------|
| `pmla-workflow`                             | Router — decides which sub-skill to invoke next                               |
| `pmla-topic-selection`                      | Fit for a generalist membership; pick the right venue                         |
| `pmla-scholarly-positioning`                | Stake the intervention in the critical conversation, across fields            |
| `pmla-argument-development`                 | Turn a reading into a consequential argument with stakes                      |
| `pmla-textual-evidence-and-close-reading`   | Close reading as evidence; quote precisely from reliable editions             |
| `pmla-theory-and-method`                    | Deploy theory to illuminate texts; the special-features home                  |
| `pmla-structure-and-exposition`             | Organize the essay clearly within 6,000–9,000 words                           |
| `pmla-writing-style`                        | Concise, readable prose for the whole membership                              |
| `pmla-citation-and-style`                   | MLA style — in-text citations + Works Cited per the MLA Handbook              |
| `pmla-review-process`                       | Anonymous review, ≥ 2 reviewers, Editorial Board decision, eligibility        |
| `pmla-submission`                           | ScholarOne preflight (anonymization, membership, word range, MLA style)       |
| `pmla-revision-and-response`                | Response to readers' reports while protecting the argument and anonymity      |

### Resources

- [`resources/external_tools.md`](resources/external_tools.md) — texts, editions, archives (EEBO/ECCO, HathiTrust, finding aids), the MLA International Bibliography, JSTOR / Project MUSE, and MLA-style / reference-manager tooling
- [`resources/official-source-map.md`](resources/official-source-map.md) — official MLA / Cambridge URLs behind every fact, with 待核实 markers on unverified items

---

## What This Repo Does Not Do

- It does not write a submittable essay for you
- It does not simulate any specific editor's or reader's taste
- It does not turn literary criticism into a data/statistics exercise — there is no dataset or replication package
- It does not assert volatile metadata (current editor and term, exact caps, deadlines, fee/membership wording) — verify on the official page; unverified items are marked 待核实
- It does not decide whether your problem is significant to the membership — that is the scholar's call

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [PMLA (Cambridge Core)](https://www.cambridge.org/core/journals/pmla) — publisher home
- [PMLA at the MLA](https://www.mla.org/Publications/Journals/PMLA) — owner, submission guidelines, what PMLA values

---

## License

MIT
