---
name: jop-writing-style
description: Use when shaping prose, length, and formatting for a The Journal of Politics (JOP) manuscript. JOP counts pages, not words — Research Article <= 35 and Short Article <= 10, double-spaced 12-point, inclusive of notes, references, and exhibits — and follows the JOP Style Guide under double-blind review. Polishes and fits to length; it does not draft the substance.
---

# Writing Style & Length (jop-writing-style)

JOP's binding constraint is **pages, not words**. The same paper that clears an APSR or AJPS word cap can
still overflow JOP's **35-page** (Research Article) or **10-page** (Short Article) budget — because the
count is **double-spaced, 12-point** and **includes notes, references, and exhibits**. This skill makes
the paper read for a general audience and **fit the page**, in **JOP Style Guide** form, kept anonymous.

## When to trigger

- Polishing a draft for clarity and general-interest readability
- The manuscript is over the page budget and must be cut
- Formatting references and headings to the JOP Style Guide
- A final anonymity pass before `jop-submission`

## Fit the page budget (the JOP-specific discipline)

- **Count pages, not words.** Format to JOP's spec — **double-spaced, 12-pt, one-inch margins** — and
  measure the real page count, because exhibits, footnotes, and the reference list all count.
- **Move overflow to the Online Appendix (≤ 25 pp).** Robustness, derivations, extra cases, and method
  detail belong there; the main text must still stand on its own.
- **Cut footnotes hard.** Notes count toward the limit — fold what matters into the text, drop the rest.
- **Trim the reference list to what you engage.** A bloated bibliography costs real pages.
- **For a Short Article (≤ 10 pp)**, write one argument, one clean analysis, minimal apparatus.

## Write for the general reader

- State the question, contribution, and finding in the first page — a non-specialist should grasp the
  stakes without subfield jargon.
- Define terms and acronyms on first use; avoid insider shorthand.
- Lead each section with its point; prefer short, declarative sentences over hedged paragraphs.

## JOP Style Guide & anonymity

- Follow the **JOP Style Guide** (house author-date) consistently for citations, headings, and
  references; pick one and do not mix conventions.
- Abstract **≤ 150 words** (question + approach + findings, no citations); **4–5 keywords**.
- **Double-blind**: no author names, affiliations, acknowledgments, or first-person self-citation in the
  anonymous file; a separate title/abstract page carries identifying details.

## Anti-patterns

- Editing to a word target and discovering the page count is over at submission
- Hiding overflow in dense single-spaced tables to "save pages" (violates the format spec)
- Subfield jargon that loses the general JOP reader
- Mixing citation styles or leaving self-identifying phrasing in the anonymous manuscript

## Output format

```
【Category】Research Article (≤35 pp) / Short Article (≤10 pp)
【Measured length】pages at double-spaced 12-pt (incl. notes/refs/exhibits)
【Over budget?】what moves to the Online Appendix
【Abstract】≤150 words, no citations? [Y/N]  Keywords: 4–5? [Y/N]
【Style + anonymity】JOP Style Guide consistent; anonymous file clean? [Y/N]
【Next】jop-replication-and-data-policy
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reference managers, typesetting, page-budget conventions
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — JOP page limits, abstract cap, Style Guide, double-blind policy
