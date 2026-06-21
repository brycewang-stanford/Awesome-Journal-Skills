---
name: arsoc-organizing-framework
description: Use when imposing an analytical structure or taxonomy on a sociology literature for an Annual Review of Sociology (ARSoc) review — the "spine" that turns a reading list into an argument about the subfield. Designs the framework; it does not gather the literature (arsoc-literature-synthesis) or judge balance (arsoc-comprehensiveness-and-balance).
---

# Organizing Framework — the Review's Spine (arsoc-organizing-framework)

## When to trigger

- The evidence matrix is built but the draft would read like a list of studies
- Sections are named after methods or eras ("Quantitative studies", "Recent work") rather than ideas
- A reader could not predict what comes next or why studies are grouped as they are
- You cannot state in one sentence the *argument* the review makes about the subfield

## Why the spine is the whole game at ARSoc

The single most-cited reason ARSoc reviews disappoint is that they are **annotated bibliographies**: study-after-study summaries with no organizing idea. A great ARSoc review **imposes a structure the subfield did not have** — a taxonomy, a unifying mechanism, a sequence of questions, or a simple analytic model — that makes scattered work legible to a sociologist from another area. The framework is the contribution; the citations are the evidence. Choose the spine deliberately:

| Spine type | Organizes the subfield by | Best when |
|-----------|---------------------------|-----------|
| **Taxonomy** | mutually-exclusive categories of mechanism / theoretical approach | the area is fragmented into incommensurable camps |
| **Mechanism / process** | the causal or social process linking inputs to outcomes | results disagree because they tap different stages of one process |
| **Levels of analysis** | micro / meso / macro, or individual / organizational / institutional | the field spans levels and the lesson is how they connect |
| **Question sequence** | a logical chain of sub-questions | the area has a natural "first we must know X, then Y" order |
| **Paradigm / debate** | rival theoretical traditions and what divides them | the *contest of perspectives* is itself the subfield's structure |

Pick **one** primary spine; a second axis can be a within-section ordering, but a review with two competing spines reads as two reviews.

## The test of a good framework

- **Exhaustive + exclusive (MECE-ish):** every important study has exactly one natural home, and the categories do not bleed into each other.
- **Generative:** the framework *predicts* where gaps are — empty cells are open questions and the seeds of the forward agenda, not omissions.
- **Reconciling:** apparent contradictions in the literature become *explained* (studies disagree because they sit in different cells / different traditions / different levels of analysis).
- **Portable:** a sociologist from an adjacent subfield can restate the spine after one read and use it to slot a new study they encounter.

Stress-test by trying to place 5 hard cases (studies that resist categorization). If three of them have no home, the spine is wrong — redesign before drafting.

> The framework is also what lets you be *selective without being incomplete*: once each cell is defined, confirmatory studies can be cited in clusters within their cell while the prose discusses only the cell-defining work. A review without a spine cannot do this — it must either summarize everything (bloat) or omit silently (gaps). Design the spine before you decide what to foreground, and note which cells are thin — those become the research agenda the ARSoc voice closes on.

## Checklist

- [ ] One primary spine chosen (taxonomy / mechanism / levels / question-sequence / paradigm-debate)
- [ ] The review's one-sentence *argument about the subfield* is written
- [ ] Every category traces to evidence-matrix rows (no empty rhetorical buckets)
- [ ] The framework reconciles at least one apparent contradiction in the literature
- [ ] Empty/thin cells are surfaced as *open questions* feeding the forward agenda (generativity)
- [ ] 5 hard-case studies each have a natural home
- [ ] Section headings name *ideas / mechanisms / traditions*, not "quantitative vs. qualitative"
- [ ] A cross-subfield sociologist could restate the spine and slot a new study into it

## Anti-patterns

- The annotated bibliography: study-by-study summaries with no organizing idea (the cardinal ARSoc sin)
- Sections named "Theory", "Methods", "Findings", "Other" — categories that carry no analytical content
- Organizing by method (quant section / qual section) instead of by idea — it hides the argument and silos the modes
- A taxonomy whose categories overlap so every study is cited three times in three places
- Two competing spines fighting for control of the same review
- A framework so bespoke only the author can apply it (not portable)
- Hiding the contribution: never stating, in one sentence, what the review argues about the subfield

## Output format

```text
【Spine type】taxonomy / mechanism / levels-of-analysis / question-sequence / paradigm-debate
【Argument about the subfield】"<one sentence the review makes>"
【Categories】<the cells / sub-questions, each MECE>
【Reconciliation】<which contradiction the framework explains>
【Open questions】<empty/thin cells surfaced as gaps for the forward agenda>
【Hard-case test】5 awkward studies each placed? Y/N
【Next step】→ arsoc-comprehensiveness-and-balance (fill cells fairly + even-handedly)
```
