# The Art Bulletin Skills

<p align="center">
  <img src="assets/cover.svg" alt="The Art Bulletin cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-The%20Art%20Bulletin-9a7b34)](https://www.collegeart.org/publications/art-bulletin)
[![Field](https://img.shields.io/badge/field-Art%20History-1f6feb)](https://www.tandfonline.com/journals/rcab20)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **The Art Bulletin** — the **leading English-language
journal of art history**, founded in **1913**, owned by the **College Art Association (CAA)** and
published quarterly (March, June, September, December) through **Taylor & Francis / Routledge**. The
Art Bulletin publishes rigorously peer-reviewed scholarship on **all periods and regions** of the
history of art, across methodologies from the historical to the theoretical.

This repository is opinionated, and it is a **humanities** pack — **not** a social-science one. There
are **no datasets, statistics, or replication packages** here. What distinguishes art-historical
publishing is **working with images**: an original argument carried by **close visual and formal
analysis**, grounded in **documentary, archival, and provenance** evidence, and delivered through a
**heavy image-permissions workflow** — securing and paying for **reproduction rights**, supplying
**high-resolution** files — that the author owns and must start early.

---

## What Is The Art Bulletin, and Why a Dedicated Stack?

The Art Bulletin's constraints differ from a social-science journal — the center of gravity is the
**image**, not the dataset:

| Constraint            | The Art Bulletin                                                               | Implication                                                       |
|-----------------------|--------------------------------------------------------------------------------|-------------------------------------------------------------------|
| Field                 | **Art history** — all periods, all regions, all methods                        | Contribution is an art-historical argument, not a finding         |
| Core method           | **Close visual / formal analysis** of objects                                  | The looking must be precise and tied to figures                   |
| Evidence              | Objects, **archives, documents, provenance**, technical art history            | No datasets/statistics — verifiable sources, not assertion        |
| **Distinctive axis**  | **Images: rights clearance + reproduction quality** (author-funded)            | Start permissions early; they are slow and costly                 |
| Owner / publisher     | **College Art Association** / **Taylor & Francis (Routledge)**                  | Submit by e-mail / large-file transfer, not a social-science portal |
| Review model          | **Double-blind**                                                               | Anonymize text *and* notes; submit **Word, not PDF**              |
| Length                | Article **up to 16,000 words including endnotes**                              | Endnotes count — keep the apparatus disciplined                   |
| Abstract / bio        | Abstract **≤ 100 words**; biographical statement **≤ 50 words**                | Tight front matter on a separate cover sheet                      |
| Illustrations         | **Max 20 images** in one Word file **≤ 10 MB**; high-res on acceptance         | Let the argument drive the figure list                            |
| Style                 | **The Chicago Manual of Style** — **endnotes**, not author-date                | Full credit-line captions; CMOS ch. 14                            |
| Fee                   | No submission fee stated; optional OA **APC** (T&F Open Select)                | Do not budget a submission fee                                    |

Volatile specifics (editor, exact caps, illustration/file limits, Chicago edition, fee/APC, fair-use
wording) change — items not directly confirmed are marked **待核实** in
[`resources/official-source-map.md`](resources/official-source-map.md). **Verify on the official
journal page.**

### The image-and-permissions reality

- **The author secures and pays** for reproduction rights and photography — clearance can take months.
- A **public-domain work** can still have a **copyrighted photograph**: clear the actual reproduction.
- At **submission**, illustrations go in one Word file (**≤ 20 images, ≤ 10 MB**); **high-resolution
  files are supplied on acceptance**.
- **Fair use** is the author's call — the **CAA Code of Best Practices in Fair Use for the Visual
  Arts** is the field reference.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/artbull-skills
/plugin install artbull-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/artbull-skills.git
cd artbull-skills

mkdir -p ~/.claude/skills && cp -R skills/artbull-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/artbull-* ~/.codex/skills/
```

### First Prompt

```
Use artbull-workflow to tell me which skill I should use next for my Art Bulletin article.
```

---

## Default Workflow

```text
artbull-topic-selection
        ▼
artbull-scholarly-positioning
        ▼
artbull-argument-development
        ▼
artbull-visual-analysis
        ▼
artbull-evidence-and-sources
        ▼
artbull-images-and-permissions   (start EARLY; runs in parallel)
        ▼
artbull-structure-and-exposition
        ▼
artbull-writing-style-and-citation   (Chicago, endnotes)
        ▼
artbull-review-process
        ▼
artbull-submission
        ▼
artbull-revision-and-response
```

`artbull-workflow` is the router — it tells you which skill to use next based on where you are. Its
standing reminder: run `artbull-images-and-permissions` **in parallel** with the writing, because
rights clearance is the slowest, most expensive, author-owned step.

---

## Skills

| Skill                                | Purpose                                                                       |
|--------------------------------------|-------------------------------------------------------------------------------|
| `artbull-workflow`                   | Router — decides which sub-skill to invoke next                               |
| `artbull-topic-selection`            | Art-historical fit and contribution, not description; feasibility of images   |
| `artbull-scholarly-positioning`      | Historiography and field debates; state the gap; own your method              |
| `artbull-argument-development`       | Build a fresh, warranted thesis from visual + documentary evidence            |
| `artbull-visual-analysis`            | Close visual / formal analysis tied to numbered figures                       |
| `artbull-evidence-and-sources`       | Objects, archives, documents, provenance, technical art history; rigour       |
| `artbull-images-and-permissions`     | **Distinctive** — rights clearance, fair use, reproduction quality, high-res  |
| `artbull-structure-and-exposition`   | Architecture of a ~16,000-word article; figure placement; length discipline   |
| `artbull-writing-style-and-citation` | Chicago Manual of Style; endnotes; full credit-line captions                  |
| `artbull-review-process`             | Double-blind review; what referees weigh; likely outcomes                     |
| `artbull-submission`                 | Preflight — Word-only files, anonymity, caps, illustrations, permissions      |
| `artbull-revision-and-response`      | Revise + respond to referees without diluting the contribution                |

### Resources

- [`resources/external_tools.md`](resources/external_tools.md) — image sources (open-access museums / IIIF / Wikimedia), rights agencies (Art Resource / Bridgeman / Scala / ARS), archives and provenance indexes, technical art history, and Chicago notes tooling
- [`resources/official-source-map.md`](resources/official-source-map.md) — official CAA / Taylor & Francis URLs behind every fact, with 待核实 markers on unverified items

---

## What This Repo Does Not Do

- It does not write a submittable article for you, nor do the looking or the archival research
- It does not analyze data or run statistics — this is art history, not social science
- It does not clear rights, grant permissions, waive fees, or supply images for you
- It does not assert volatile metadata (current editor, exact caps, illustration/file limits, Chicago edition, fee/APC) — verify on the official page; unverified items are marked 待核实
- It does not decide whether your contribution is significant enough for the discipline's flagship — that is the researcher's call

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [The Art Bulletin (College Art Association)](https://www.collegeart.org/publications/art-bulletin) — owner, submission guidelines, preparation
- [The Art Bulletin (Taylor & Francis Online)](https://www.tandfonline.com/journals/rcab20) — publisher home, issues, open access

---

## License

MIT
