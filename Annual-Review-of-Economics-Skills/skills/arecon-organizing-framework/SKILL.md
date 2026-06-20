---
name: arecon-organizing-framework
description: Use when imposing an analytical structure or taxonomy on a literature for an Annual Review of Economics (ARE) review — the "spine" that turns a reading list into an argument about the field. Designs the framework; it does not gather the literature (arecon-literature-synthesis) or appraise evidence and balance (arecon-evidence-standards).
---

# Organizing Framework — the Review's Spine (arecon-organizing-framework)

## When to trigger

- The evidence matrix is built but the draft would read like a list of papers
- Sections are named after topics ("Empirical studies", "Theoretical work") rather than ideas
- A reader could not predict what comes next or why papers are grouped as they are
- You cannot state in one sentence the *argument* the review makes about the field

## Why the spine is the whole game at ARE

The most-cited reason review articles fail is that they are **annotated bibliographies**: paper-after-paper summaries with no organizing idea. A great ARE review **imposes a structure the field did not have** — a taxonomy, a unifying framework, a sequence of questions, or a simple model — that makes scattered work legible to an economist from an adjacent field. The framework is the contribution; the citations are the evidence. ARE's accessibility mandate raises the bar further: the spine must be graspable by a *non-specialist* on one read. Choose it deliberately:

| Spine type | Organizes the field by | Best when |
|-----------|------------------------|-----------|
| **Taxonomy** | mutually-exclusive categories of mechanism/approach | the field is fragmented into incommensurable camps |
| **Unifying model** | a simple framework whose parameters index the studies | results disagree because they estimate different parameters of one structure |
| **Question sequence** | a logical chain of sub-questions | the field has a natural "first know X, then Y" order |
| **Chronological/paradigm** | how thinking evolved and why | the *evolution* of ideas is itself the lesson |
| **Methods spectrum** | from least to most credible designs | the review's value is appraising what is actually known |

Pick **one** primary spine; a second axis can order papers within a section, but a review with two competing spines reads as two reviews.

## The test of a good framework

- **Exhaustive + exclusive (MECE-ish):** every important paper has exactly one natural home, and categories do not bleed.
- **Generative:** the framework *predicts* gaps — empty cells are open questions, not omissions (ARE prizes the forward-looking agenda).
- **Reconciling:** apparent contradictions become *explained* (studies disagree because they sit in different cells / estimate different objects).
- **Portable:** an adjacent economist can restate the spine after one read and slot a new paper into it.

Stress-test by placing 5 hard cases (papers that resist categorization). If three have no home, the spine is wrong — redesign before drafting.

> The spine is also what lets an ARE review be *selective without being incomplete*: once each cell is defined, confirmatory studies can be cited in clusters within their cell while the prose discusses only the cell-defining work. This is how you honor coverage and the ~25–40-page accessibility envelope at once (检索于 2026-06；以官网为准). Design the spine before deciding what to foreground.

## Checklist

- [ ] One primary spine chosen (taxonomy / model / question-sequence / paradigm / methods)
- [ ] The review's one-sentence *argument about the field* is written
- [ ] Every category traces to evidence-matrix rows (no empty rhetorical buckets)
- [ ] The framework reconciles at least one apparent contradiction in the literature
- [ ] Empty cells surfaced as *open questions* (generativity — the future agenda)
- [ ] 5 hard-case papers each have a natural home
- [ ] Section headings name *ideas/mechanisms*, not "theoretical vs. empirical"
- [ ] An adjacent (non-specialist) economist could restate the spine and slot a new paper into it

## Anti-patterns

- The annotated bibliography: paper-by-paper summaries with no organizing idea (the cardinal review sin)
- Sections named "Theory", "Evidence", "Other" — categories that carry no analytical content
- A taxonomy whose categories overlap so every paper is cited three times in three places
- Two competing spines fighting for control of the same review
- A framework so bespoke only the author can apply it (fails ARE's accessibility test)
- Hiding the contribution: never stating, in one sentence, what the review argues about the field

## Output format

```text
【Spine type】taxonomy / unifying-model / question-sequence / paradigm / methods-spectrum
【Argument about the field】"<one sentence the review makes>"
【Categories】<the cells / sub-questions, each MECE>
【Reconciliation】<which contradiction the framework explains>
【Open questions】<empty cells surfaced as the future agenda>
【Hard-case test】5 awkward papers each placed? Y/N
【Accessibility】an adjacent economist can restate the spine? Y/N
【Next step】→ arecon-evidence-standards (appraise study credibility + balance the cells fairly)
```
