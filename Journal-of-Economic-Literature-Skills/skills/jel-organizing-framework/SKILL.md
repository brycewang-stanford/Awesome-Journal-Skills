---
name: jel-organizing-framework
description: Use when imposing an analytical structure or taxonomy on a literature for a Journal of Economic Literature (JEL) survey — the "spine" that turns a reading list into an argument about the field. Designs the framework; it does not gather the literature (jel-literature-synthesis) or judge balance (jel-comprehensiveness-and-balance).
---

# Organizing Framework — the Survey's Spine (jel-organizing-framework)

## When to trigger

- The evidence matrix is built but the draft would read like a list of papers
- Sections are named after topics ("Empirical studies", "Theoretical work") rather than ideas
- A reader could not predict what comes next or why papers are grouped as they are
- You cannot state in one sentence the *argument* the survey makes about the field

## Why the spine is the whole game at JEL

The single most-cited reason JEL surveys fail is that they are **annotated bibliographies**: paper-after-paper summaries with no organizing idea. A great JEL survey **imposes a structure the field did not have** — a taxonomy, a unifying framework, a sequence of questions, or a simple model — that makes scattered work legible. The framework is the contribution; the citations are the evidence. Choose the spine deliberately:

| Spine type | Organizes the field by | Best when |
|-----------|------------------------|-----------|
| **Taxonomy** | mutually-exclusive categories of mechanism/approach | the field is fragmented into incommensurable camps |
| **Unifying model** | a simple framework whose parameters index the studies | results disagree because they estimate different parameters of one structure |
| **Question sequence** | a logical chain of sub-questions | the field has a natural "first we must know X, then Y" order |
| **Chronological/paradigm** | how thinking evolved and why | the *evolution* of ideas is itself the lesson |
| **Methods spectrum** | from least to most credible designs | the survey's value is appraising what is actually known |

Pick **one** primary spine; a second axis can be a within-section ordering, but a survey with two competing spines reads as two surveys.

## The test of a good framework

- **Exhaustive + exclusive (MECE-ish):** every important paper has exactly one natural home, and the categories do not bleed into each other.
- **Generative:** the framework *predicts* where gaps are — empty cells are open questions, not omissions.
- **Reconciling:** apparent contradictions in the literature become *explained* (studies disagree because they sit in different cells / estimate different objects).
- **Portable:** a non-specialist can restate the spine after one read and use it to slot a new paper they encounter.

Stress-test by trying to place 5 hard cases (papers that resist categorization). If three of them have no home, the spine is wrong — redesign before drafting.

> The framework is also what lets you be *selective without being incomplete*: once each cell is defined, confirmatory studies can be cited in clusters within their cell while the prose discusses only the cell-defining work. A survey without a spine cannot do this — it must either summarize everything (bloat) or omit silently (gaps). Design the spine before you decide what to foreground.

## Checklist

- [ ] One primary spine chosen (taxonomy / model / question-sequence / paradigm / methods)
- [ ] The survey's one-sentence *argument about the field* is written
- [ ] Every category traces to evidence-matrix rows (no empty rhetorical buckets)
- [ ] The framework reconciles at least one apparent contradiction in the literature
- [ ] Empty cells are surfaced as *open questions* (generativity)
- [ ] 5 hard-case papers each have a natural home
- [ ] Section headings name *ideas/mechanisms*, not "theoretical vs. empirical"
- [ ] A non-specialist could restate the spine and slot a new paper into it

## Anti-patterns

- The annotated bibliography: paper-by-paper summaries with no organizing idea (the cardinal JEL sin)
- Sections named "Theory", "Evidence", "Other" — categories that carry no analytical content
- A taxonomy whose categories overlap so every paper is cited three times in three places
- Two competing spines fighting for control of the same survey
- A framework so bespoke only the author can apply it (not portable)
- Hiding the contribution: never stating, in one sentence, what the survey argues about the field

## Output format

```
【Spine type】taxonomy / unifying-model / question-sequence / paradigm / methods-spectrum
【Argument about the field】"<one sentence the survey makes>"
【Categories】<the cells / sub-questions, each MECE>
【Reconciliation】<which contradiction the framework explains>
【Open questions】<empty cells surfaced as gaps>
【Hard-case test】5 awkward papers each placed? Y/N
【Next step】→ jel-comprehensiveness-and-balance (fill cells fairly + even-handedly)
```
