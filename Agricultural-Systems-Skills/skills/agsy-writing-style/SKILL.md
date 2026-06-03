---
name: agsy-writing-style
description: Use when drafting or polishing an Agricultural Systems (AgSy) manuscript so it reads clearly for a systems-science audience, follows the journal's format, and meets front-matter requirements (abstract <= 250 words, Highlights, graphical abstract). Research papers run to about 8,000 words (no hard cap). Tightens prose and format; it does not invent content.
---

# Writing Style (agsy-writing-style)

An AgSy paper must be readable by a broad **systems-science** audience — agronomists, modellers,
economists, and environmental scientists — and prepared with the journal's front matter. This skill is
about communicating a systems analysis clearly and meeting Elsevier's format, not about generating
claims.

## When to trigger

- Drafting the introduction, framing the contribution, or final polish
- Writing the **≤ 250-word abstract**, the **Highlights**, or the **graphical abstract**
- Tightening a long methods/results section toward the ~8,000-word guideline
- Aligning references and format to the journal's style before submission

## Reach the systems-science audience

1. **Front-load the systems contribution.** By the end of the introduction the reader knows the system,
   the interaction/trade-off in question, the modelling approach, and why the result matters. Don't make
   a reader dig for the "so what."
2. **Define the system early.** State boundary, components, and hierarchical level so a non-specialist
   in your exact subsystem can follow (see `agsy-systems-framing-and-modeling`).
3. **Explain the model in plain terms first**, then in detail. A reader should grasp what the model does
   before meeting its equations.
4. **Argument-first prose.** Lead with the systems insight; use model output and statistics to support
   it. Avoid "the model shows…" without saying what it shows about the system and why it matters.
5. **Signpost.** Clear IMRaD-style structure so a reader can navigate framing → model → evaluation →
   trade-offs → implications.

## Format & front matter (verify current requirements)

- **Abstract**: **≤ 250 words**, stating purpose, principal results, and major conclusions.
- **Highlights**: a few short bullet points capturing the core systems findings.
- **Graphical abstract**: one figure summarizing the work for an interdisciplinary audience — often a
  conceptual system diagram or a trade-off result.
- **References**: format to the journal's style; manage with Zotero/Mendeley/BibTeX (Elsevier
  `elsarticle` for LaTeX). 
- **Declarations**: CRediT roles, declaration of competing interest, ORCID (see `agsy-submission`).

## Length discipline (research paper ~8,000 words; no hard cap)

- Move full calibration tables, parameter lists, and exhaustive scenario grids to supplementary material.
- Cut throat-clearing and literature dumps; engage the systems debate, not every paper.
- Prefer one decisive trade-off figure to three redundant tables.

## Anti-patterns

- An intro that never states the systems contribution or the trade-off at stake
- An abstract over 250 words, or one that hides the result; missing Highlights / graphical abstract
- Dropping a model's equations on the reader before explaining what it does
- Describing a single factor as if it were a system; burying the interaction
- Mixed reference styles or missing declarations

## Output format

```
【Systems contribution stated by end of intro?】[Y/N]
【System defined early?】boundary + components + level? [Y/N]
【Abstract】word count (≤250)
【Highlights + graphical abstract】prepared? [Y/N]
【Length】near ~8,000 words; extras moved to supplementary? [Y/N]
【References + declarations】styled + CRediT/COI/ORCID ready? [Y/N]
【Next】agsy-impact-and-implications
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reference managers and Elsevier typesetting tools
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — abstract cap, Highlights, graphical abstract, declarations
