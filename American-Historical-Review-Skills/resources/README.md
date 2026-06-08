# AHR Resources

Action-oriented resources for *The American Historical Review* (AHR) skill pack. The `skills/` give
advice; this directory lets an agent **act** — model an AHR-style section and benchmark against
web-verified exemplars. Pair these with the relevant `skills/ahr-*/SKILL.md`.

The AHR is a **humanities (history)** flagship. Its craft is **archival and primary-source research,
source criticism, historiographical argument, and interpretation** — *not* statistics, datasets, or
code. Accordingly, **this pack ships no code kit**: there is no `code/` directory and nothing to run.
The resources here are reading and modeling aids for prose, argument, and evidence.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of a history-article **introduction** in AHR house style — stakes-first opening, early historiographical intervention, a contestable thesis earned from criticized primary sources, and significance beyond the subfield. Clearly-marked fictional article; no real sources cited. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified AHR articles** organized by field × method. Positioning and craft cues only — no fabricated findings, with a sibling-journal confusion guard. |
| [`official-source-map.md`](official-source-map.md) | **AHR-specific policy & facts:** owner (AHA) / publisher (OUP), ScholarOne submission (Word, no email), ~8,000-word target and ~2:1 text-to-notes guideline, Chicago notes, double-blind review by ≥6 scholars, ~8–10% acceptance, no APCs, alt-text/permissions, and a do-not-misattribute list with 待核实 items. The authoritative pack source. |
| [`external_tools.md`](external_tools.md) | Find archives, finding aids, digitized primary-source databases, reference managers (Chicago notes), paleography/OCR and transcription tools, and manuscript-prep tooling matched to your field, period, and languages. |

## No empirical/code kit (humanities venue)

Unlike the quantitative social-science packs in this repo, the AHR pack does **not** vendor a code
pipeline or link a shared empirical-methods kit. History at the AHR is judged on the **quality and
criticism of primary-source evidence and the strength of the historiographical argument**, not on
estimators or reproducibility scripts. If you came looking for `code/`, there isn't one — and that is by
design for a humanities flagship.

## Suggested workflow

1. **Scope and frame** the project with
   [`../skills/ahr-topic-selection`](../skills/ahr-topic-selection/SKILL.md) (significance beyond the
   subfield) and stake the contribution with
   [`../skills/ahr-historiography-positioning`](../skills/ahr-historiography-positioning/SKILL.md).
2. **Build the argument and evidence** with
   [`../skills/ahr-argument-development`](../skills/ahr-argument-development/SKILL.md) and
   [`../skills/ahr-sources-and-archives`](../skills/ahr-sources-and-archives/SKILL.md), using
   [`external_tools.md`](external_tools.md) to locate and handle primary sources.
3. **Draft the introduction and structure** by modeling
   [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md), guided by
   [`../skills/ahr-structure-and-exposition`](../skills/ahr-structure-and-exposition/SKILL.md) and
   [`../skills/ahr-writing-style`](../skills/ahr-writing-style/SKILL.md).
4. **Benchmark** against verified AHR articles in [`exemplars/library.md`](exemplars/library.md), and
   confirm submission, length, citation, and review policy in
   [`official-source-map.md`](official-source-map.md).
