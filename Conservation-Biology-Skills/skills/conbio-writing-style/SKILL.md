---
name: conbio-writing-style
description: Use when drafting or polishing a Conservation Biology manuscript so it reads accessibly for a broad conservation audience, follows the journal Style Guide, and fits the per-type word caps (e.g., Contributed Papers ~6,000–7,000; abstract <= 300 words). Tightens prose and format; it does not invent content.
---

# Writing Style (conbio-writing-style)

A *Conservation Biology* paper must be readable by conservation scientists and practitioners beyond
the author's own system, formatted to the journal **Style Guide**, and disciplined to the per-type word
cap. This skill is about clarity, accessibility, and format — not about generating claims. (Verify the
current per-type caps; they drift between Style Guide versions — see `resources/official-source-map.md`.)

## When to trigger

- Drafting the introduction, framing the contribution, or final polish
- Over the word cap and needing to cut without losing the argument
- Writing the **≤ 300-word abstract**
- Aligning citations/headings/format to the Style Guide before submission

## Reach a broad conservation audience

1. **Front-load the conservation contribution.** By the end of the introduction the reader knows the
   problem, the question, the approach, and **why it matters for conserving biodiversity.** Don't make
   a generalist dig for the "so what."
2. **Minimize system jargon** or define it on first use; a practitioner should follow a population-model
   paper, and a modeler should follow a field study. Spell out acronyms; use accepted species names.
3. **Argument-first prose.** Lead with claims; use evidence to support them. Avoid "the data show…"
   without saying what they show and why it matters for conservation.
4. **Signpost and follow IMRAD.** Contributed Papers, Research Notes, and Practice & Policy follow
   Abstract → Introduction → Methods → Results → Discussion; do not combine Results and Discussion, and
   do not add a separate Conclusion (conclusions belong in the Discussion).

## Format to the Style Guide

- **Citations**: author-date per the journal Style Guide; keep one consistent style (manage with
  Zotero/BibTeX). Literature Cited is included in the word count.
- **Title**: clear and concise; avoid hanging (colon/dash) titles, full-sentence titles, and
  interrogative titles per the Style Guide.
- **Anonymize**: the journal is **double-blind** — no author names/affiliations in the manuscript, and
  neutralize obvious self-references; strip identifying file metadata (see `conbio-submission`).
- **Abstract**: **≤ 300 words**, stating problem, approach, and finding (no abstract for Letters,
  Comments, or Diversity).

## Fit the word cap (count runs from first word of Abstract through last word of Literature Cited)

- Note: the count **excludes tables, figure legends, and text inside tables.** Move full model output,
  balance tables, and extended robustness to **Supporting Information**.
- Cut throat-clearing and literature dumps; engage the debate, not every paper (see
  `conbio-literature-positioning`).
- Prefer one decisive figure to three redundant tables (and respect the ~one-exhibit-per-four-pages rule).

## Anti-patterns

- A system-insider intro that never states conservation relevance
- Burying the contribution in the middle of the paper
- An abstract over 300 words or one that hides the finding
- Hanging/interrogative/full-sentence titles; mixed citation styles
- Self-references that break the double-blind; padding a Research Note toward Contributed-Paper length

## Output format

```
【Conservation contribution stated by end of intro?】[Y/N]
【Reads past the system?】jargon defined / acronyms spelled? [Y/N]
【Abstract】word count (≤300)
【Word count】within the article-type cap (Abstract→Literature Cited)?
【Style Guide + anonymized + title style】[Y/N]
【Next】conbio-conservation-relevance-and-implications
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reference managers and typesetting
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — word/abstract caps, Style Guide, IMRAD, title rules
