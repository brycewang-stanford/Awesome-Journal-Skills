---
name: rje-writing-style
description: Use to make a manuscript conform to The RAND Journal of Economics (RJE) Style Guide — author-date citations with no page numbers, references with no issue numbers, numbered sections with unnumbered subsections, flush-right equation numbering, and the journal's distinctive house usage rules. Style and usage polish, not content drafting.
---

# RJE House Style (rje-writing-style)

## When to trigger

- Final language and citation polish before submission to RJE
- Converting a draft from a numbered/footnote citation style to RJE author-date
- Catching the journal's specific usage rules that copy editors enforce

## The RJE Style Guide (verified 2026-06-20)

RJE maintains its own Style Guide (rje.org/styleguide.html), which directs authors to the **Chicago Manual of Style** (the page links to the **18th edition**). Its load-bearing rules:

### Citations and references
- **In-text:** author-date, **name and year only, no page numbers** — e.g., "(Jones, 1991)" or "Jones (1991)".
- **Reference list:** alphabetical, **unnumbered**, at the end of the text, with **no issue numbers** in journal citations.

### Structure and numbering
- **Sections numbered consecutively; subsections are NOT numbered.** This is a frequent slip for authors coming from journals that number 2.1, 2.2.
- **Equations numbered consecutively, flush right**, using **(1a)/(1b)** for multi-part equations.
- **Footnotes kept short** — roughly 50 words / 3 typeset lines each.
- Abstract **<=100 words**; main text **<=40 pp**, total **<=50 pp**, double-spaced.

### Distinctive house usage rules
- Use **"because"** or **"as"** instead of **"since"** when the meaning is causal (reserve *since* for time).
- Use **"whereas"** or **"although"** instead of **"while"** when the meaning is contrastive (reserve *while* for simultaneity).
- Use **"article,"** not **"paper,"** to refer to the manuscript.

## Tone for the IO flagship

Write for an industrial-organization audience: name the **market, the firms' strategic problem, and the policy/welfare stake** plainly. Define the structural primitives or the identifying variation early, and let demand/cost parameters, elasticities, and counterfactual welfare numbers carry the argument. Avoid general-interest throat-clearing; RJE readers want the economics of the market.

## House-usage conversion table (the slips copy editors catch)

These are the RJE-specific edits that betray a draft imported from another journal. Audit each before submission.

| If the draft says | RJE wants | Rule |
|---|---|---|
| "since the merger raised prices" (causal) | "because/as the merger raised prices" | Reserve *since* for time |
| "while prices rose, output fell" (contrast) | "whereas/although prices rose, output fell" | Reserve *while* for simultaneity |
| "in this paper we estimate..." | "in this article we estimate..." | Use "article," not "paper" |
| "Section 2.1 derives demand" | "the demand subsection" (unnumbered) | Subsections are not numbered |
| "(Berry 1994, p. 254)" | "(Berry, 1994)" | No page numbers in in-text cites |
| "J. Econ. 62(3): 880-900" | drop the issue number | No issue numbers in references |

## Worked vignette: converting a paragraph to RJE style

Take a draft sentence from a structural IO article: "Since the platform raised its commission, while restaurant entry fell, we estimate in this paper (using BLP, 1995, p. 60) that markups rose 6%."

Converted to RJE house style: "Because the platform raised its commission, whereas restaurant entry fell, we estimate in this article (using Berry, Levinsohn and Pakes, 1995) that markups rose 6%." The edits — *since*→*because* (causal), *while*→*whereas* (contrastive), *paper*→*article*, dropped page number — are exactly the load-bearing house rules, and they recur throughout a typical draft.

## Tone calibration for the IO reader

- Open each empirical section by naming the market and the firms' strategic problem, then the structural primitive or identifying variation, then let the numbers (elasticities, markups, counterfactual welfare) carry the argument.
- Prefer concrete market language ("the merging brands' markup rose to 38%") over abstract throat-clearing ("the results have important implications").
- Keep footnotes to roughly 50 words / 3 typeset lines; relegate algebra and caveats to the appendix, not sprawling notes.
- These are stylistic conventions; confirm any edition-specific Chicago Manual details against the journal's current Style Guide.

## Anti-patterns

- Page numbers in in-text cites, or issue numbers in the reference list
- Numbered subsections (2.1, 2.2) — RJE leaves subsections unnumbered
- "Since" for causation and "while" for contrast; calling the manuscript a "paper"
- Sprawling footnotes; an over-length abstract
- Left-aligned or inline equation numbers instead of flush-right (1a)/(1b)

## Output format

```
【Citations】author-date, no page numbers? [Y/N]
【References】alphabetical, unnumbered, no issue numbers? [Y/N]
【Numbering】sections numbered, subsections unnumbered, eqns flush-right? [Y/N]
【House usage】because/as, whereas/although, "article" not "paper"? [Y/N]
【Limits】abstract <=100w; footnotes short? [Y/N]
【Next step】rje-replication-and-data-policy → rje-submission
```
