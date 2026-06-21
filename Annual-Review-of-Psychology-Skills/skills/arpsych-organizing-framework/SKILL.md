---
name: arpsych-organizing-framework
description: Use when imposing an analytical structure or taxonomy on a psychology literature for an Annual Review of Psychology (ARPsych) review — the "spine" that turns a reading list into an argument about the field. Designs the framework; it does not gather the literature (arpsych-literature-synthesis) or judge coverage and balance (arpsych-comprehensiveness-and-balance).
---

# Organizing Framework — the Review's Spine (arpsych-organizing-framework)

## When to trigger

- The evidence matrix is built but the draft would read like a list of studies
- Sections are named after methods ("fMRI studies", "behavioral studies") rather than ideas
- A reader could not predict what comes next or why studies are grouped as they are
- You cannot state in one sentence the *argument* the review makes about the field

## Why the spine is the whole game at ARPsych

The most-cited reason review articles fail is that they are **annotated bibliographies**: study-after-study summaries with no organizing idea. A great ARPsych review **imposes a structure the field did not have** — a taxonomy, a unifying model, a sequence of questions, or a process diagram — that makes scattered work legible to a psychologist from an adjacent area. The framework is the contribution; the citations are the evidence. ARPsych's accessibility mandate raises the bar: the spine must be graspable by a *non-specialist psychologist* (a social psychologist reading a memory review) on one read. Choose it deliberately:

| Spine type | Organizes the field by | Best when |
|-----------|------------------------|-----------|
| **Taxonomy** | mutually-exclusive categories of mechanism/construct | the field is fragmented into incommensurable subliteratures |
| **Process model** | stages of a mechanism (input → process → output) | the topic is a pathway (e.g., emotion generation, encoding→retrieval) |
| **Levels of analysis** | from neural to behavioral to social | the value is integrating across explanatory levels |
| **Question sequence** | a logical chain of sub-questions | the field has a natural "first know X, then Y" order |
| **Paradigm/era** | how thinking evolved and why | the *evolution* of ideas is itself the lesson |
| **Theory contest** | rival accounts of the same phenomenon | progress hinges on adjudicating competing theories |

Pick **one** primary spine; a second axis can order studies within a section, but a review with two competing spines reads as two reviews.

## The test of a good framework

- **Exhaustive + exclusive (MECE-ish):** every important study has exactly one natural home, and categories do not bleed.
- **Generative:** the framework *predicts* gaps — empty cells are open questions, not omissions (ARPsych prizes the forward-looking agenda).
- **Reconciling:** apparent contradictions become *explained* (studies disagree because they sit in different cells / measure different constructs / use different paradigms).
- **Portable:** an adjacent psychologist can restate the spine after one read and slot a new study into it.

Stress-test by placing 5 hard cases (studies that resist categorization). If three have no home, the spine is wrong — redesign before drafting.

> The spine is also what lets an ARPsych review be *selective without being incomplete*: once each cell is defined, confirmatory studies can be cited in clusters within their cell while the prose discusses only the cell-defining work. This is how you honor coverage and the assigned-length envelope at once (检索于 2026-06；以官网为准). Design the spine before deciding what to foreground.

## Checklist

- [ ] One primary spine chosen (taxonomy / process / levels / question-sequence / paradigm / theory-contest)
- [ ] The review's one-sentence *argument about the field* is written
- [ ] Every category traces to evidence-matrix rows (no empty rhetorical buckets)
- [ ] The framework reconciles at least one apparent contradiction in the literature
- [ ] Empty cells surfaced as *open questions* (the future agenda ARPsych expects)
- [ ] 5 hard-case studies each have a natural home
- [ ] Section headings name *ideas/mechanisms*, not "fMRI vs. behavioral"
- [ ] An adjacent psychologist could restate the spine and slot a new study into it

## Anti-patterns

- The annotated bibliography: study-by-study summaries with no organizing idea (the cardinal sin)
- Sections named by method ("Neuroimaging", "Behavioral", "Other") — carry no analytical content
- A taxonomy whose categories overlap so every study is cited in three places
- Two competing spines fighting for control of the same review
- A framework so bespoke only the author can apply it (fails the accessibility test)
- Hiding the contribution: never stating, in one sentence, what the review argues about the field

## Output format

```text
【Spine type】taxonomy / process / levels / question-sequence / paradigm / theory-contest
【Argument about the field】"<one sentence the review makes>"
【Categories】<the cells / stages / sub-questions, each MECE>
【Reconciliation】<which contradiction the framework explains>
【Open questions】<empty cells surfaced as the future agenda>
【Hard-case test】5 awkward studies each placed? Y/N
【Accessibility】an adjacent psychologist can restate the spine? Y/N
【Next step】→ arpsych-comprehensiveness-and-balance (cover the cells fairly)
```
