---
name: revedres-organizing-framework
description: Use when turning a screened, coded corpus into an analytic spine that advances theory or policy for a Review of Educational Research (RER) manuscript. Builds the conceptual contribution beyond a tally; it does not run the search (revedres-literature-synthesis) or appraise robustness/risk-of-bias (revedres-comprehensiveness-and-balance).
---

# Organizing Framework (revedres-organizing-framework)

## When to trigger

- The corpus is complete and coded, but the draft reads as study-after-study
- You can describe what each study found but not what the field, taken together, means
- A reviewer is likely to say "this is a competent summary, but what is the contribution?"
- You need section architecture and cannot decide how to carve the literature

## The RER contribution is the framework, not the tally

The cardinal RER failure mode is the **annotated bibliography**: a competent, even exhaustive, study-by-study summary with no argument about the field. RER wants a **comprehensive, critical, integrative** review — *integrative* means the studies are reorganized under a frame that the reader could not have built from the abstracts alone, and that **advances theory or policy**. A meta-analysis is not exempt: a pooled number with no conceptual account of *why* effects vary is a calculation, not a synthesis.

A good framework is the lens through which scattered findings become a coherent claim. Candidate spines:

| Spine type | When it fits | Example shape |
|---|---|---|
| **Taxonomy / typology** | many studies, no shared map | classify studies by a 2–3 axis scheme so every study has a home |
| **Theoretical model** | a mechanism organizes the field | a model whose links the literature does/doesn't support |
| **Moderator architecture** | a meta-analysis with real heterogeneity | the framework *is* the explanation of variation |
| **Developmental / stage account** | the field has moved through phases | what each phase established and left open |
| **Tensions / competing perspectives** | live theoretical or methodological debate | steelman each camp; locate the evidence between them |
| **Construct clarification** | the field conflates distinct ideas | disentangle the constructs, then re-read the evidence |

## Three tests a framework must pass

1. **MECE-ish.** Categories are reasonably mutually exclusive and collectively exhaustive — every included study has exactly one principled home, and there are no empty "misc" bins doing the real work.
2. **Reconciling.** The frame *explains* apparent contradictions — studies that looked to disagree turn out to sit in different cells (different populations, constructs, designs), or genuinely conflict in a way the frame names.
3. **Generative.** The frame's thin or empty cells become the review's **agenda for theory, research, or policy** — the contribution that makes the review worth citing.

Then make the section architecture **mirror the framework's cells**, so the structure of the paper enacts the argument rather than marching through databases or chronology.

## Building the frame from the coded corpus (not before it)

The frame must be **earned from the evidence**, not imposed on it. Work bottom-up from the coding dataset (`revedres-literature-synthesis`):

1. **Cluster the coded studies** by what actually differentiates their findings — population, construct, design, mechanism, or context — and look for the axis along which the literature naturally separates.
2. **Name the axis (or axes)** that does the most explanatory work; a 2- or 3-axis scheme usually beats a long flat list of themes.
3. **Test the frame against the hard cases** — the studies that seemed to contradict each other. If the frame puts them in different cells *and* explains why, it is reconciling; if it just relabels them, it is not.
4. **Read the empty cells as the agenda.** A cell with no studies is either an untested combination (a research gap) or an impossible one (a boundary condition) — both are contributions if you say which.

A frame discovered this way is defensible because a reviewer can trace it back to the coded studies; a frame asserted in the introduction and never grounded reads as the author's prior, not the field's structure.

## Checklist

- [ ] A one-sentence claim about the field stated up front (not withheld to the conclusion)
- [ ] A named spine (taxonomy / model / moderator architecture / stages / tensions / constructs)
- [ ] Every included study slots into the frame; no junk-drawer "other" category
- [ ] The frame reconciles at least one apparent contradiction in the literature
- [ ] Thin/empty cells are turned into a concrete theory/research/policy agenda
- [ ] Section architecture mirrors the frame, not the search or the calendar
- [ ] The framework advances theory or policy — it is not just a sorting convenience

## Anti-patterns

- An annotated bibliography dressed up with section headings (the named RER sin)
- A "framework" that is really chronology ("early work / recent work") or by-database order
- A meta-analysis that reports a pooled effect and moderators with no conceptual story of *why*
- A taxonomy with a giant "miscellaneous" cell that hides the studies that do not fit
- Centering the frame on the author's own program so it functions as self-promotion
- A frame that sorts but never reconciles conflict or generates an agenda (sorting ≠ integrating)

## Output format

```
【Field claim】<one sentence: what the literature, integrated, shows>
【Spine】<taxonomy | model | moderator architecture | stages | tensions | constructs>
【MECE check】every study has one home; no junk-drawer cell? Y/N
【Reconciles】<an apparent contradiction the frame resolves>
【Generative】<the theory/research/policy agenda the thin cells imply>
【Section map】<how sections mirror the frame's cells>
【Next step】→ revedres-comprehensiveness-and-balance (test coverage, risk-of-bias, robustness)
```
