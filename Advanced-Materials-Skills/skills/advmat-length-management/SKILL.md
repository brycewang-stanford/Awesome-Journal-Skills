---
name: advmat-length-management
description: Use when an Advanced Materials manuscript must be fit to its article-type format — Communication versus Research Article — where word count and display items are budgeted together against a typeset page limit. Manages the length budget; does not restructure the science or polish prose line by line.
---

# Advanced Materials Length Management (advmat-length-management)

## When to trigger

- You are unsure whether the work is a Communication or a full Research Article
- The manuscript overruns the typeset page limit for its article type
- Figures/schemes are large and you must trade display items against text
- A reviewer or editor asked you to condense to a Communication, or expand to an Article
- You are in late polish, after the science and figures are stable

## Article type sets the budget

Advanced Materials counts length in **typeset published pages**, not manuscript pages — a double-spaced 25-page manuscript may typeset to far fewer pages in the two-column layout. Word count and **display items (figures, schemes, tables) count together** against the page budget. Approximate targets (verify current limits on the author page):

| Article type       | Typeset budget (approx.)     | Abstract                          | Display items (approx.) |
|--------------------|------------------------------|-----------------------------------|-------------------------|
| Communication      | ~4 published pages (~3500 words) | none — opening paragraph acts as abstract | ~4 figures/tables       |
| Research Article   | ~10 published pages (~3000–8000 words) | short abstract (~200 words) + 3–7 keywords | ~3–8 display items       |
| Review / Progress  | longer, by invitation/agreement | structured per type            | many                    |

A large or multi-panel figure consumes a disproportionate slice of the page budget: adding a panel can cost a paragraph of text.

## Choosing Communication vs. Article

- **Communication** — one sharp, urgent advance that a specialist audience needs now; concise, high-impact, no room for exhaustive characterization in the body (it goes to the SI).
- **Research Article** — the same class of advance but requiring the full structure → property → function story, multiple device configurations, or a mechanism study that a Communication cannot hold.
- If your "Communication" needs eight figures to be believed, it is an Article. If your "Article" has one figure and one claim, it is a Communication.

## Trimming order (cut in this sequence)

Trim only *after* the central advance, characterization, and figures are stable, so you cut padding, not evidence:

1. **Hype and boilerplate** — delete "novel/unprecedented/facile/remarkable"; collapse background paragraphs to one sentence (see `advmat-writing-style`).
2. **Redundant prose** — remove sentences that transcribe figure values; interpret instead.
3. **Optimization and secondary data** — move process sweeps, extra samples, and control experiments to the SI (see `advmat-supplementary`).
4. **Display items** — merge panels that prove one link; move non-essential figures to the SI; avoid double-column figures unless the data demand it.
5. **Reference pruning** — keep the citations that establish novelty and support trust; drop padding.

Never trim: the decisive characterization, the benchmarking, or the headline metric's statistics.

## Fit-check routine

- Typeset a draft in the Wiley template to see real page count, not manuscript pages.
- Budget each figure by its printed area; tally figures + text together.
- Leave a margin under the limit so revision additions do not overrun.
- If still over after trimming padding, the honest fixes are: promote to a Research Article, or move a supporting result wholesale to the SI — not shrinking fonts or figures below legibility.

## Checklist

- [ ] Article type chosen deliberately (Communication vs. Research Article) and matches the content
- [ ] Length measured as typeset pages in the Wiley template, not manuscript pages
- [ ] Display items counted together with text against the budget
- [ ] Hype words and background padding removed first
- [ ] Optimization/secondary data moved to the SI, not deleted
- [ ] No double-column figure unless the data require it
- [ ] Abstract/keywords conform to the article type
- [ ] Decisive characterization, benchmarking, and statistics untouched

## Anti-patterns

- Trimming characterization or benchmarking to hit the page limit
- Counting manuscript pages instead of typeset pages and being surprised at proof
- Shrinking figures below legibility to save space
- Forcing a full study into a Communication by hiding the evidence in the SI
- Padding a thin Communication into an Article with filler characterization
- Discovering the overrun only at production, after acceptance

## Output format

```
【Article type】Communication / Research Article — matches content?  yes / reconsider
【Typeset page estimate】within budget?  yes / over by ~X
【Display items】counted with text?  N figures + M tables
【Trim done】hype / prose / secondary-data-to-SI / figures / refs
【Untouched】characterization + benchmarking + statistics intact?  yes
【Next】advmat-cover-letter or advmat-submission
```

> Page limits, word counts, abstract/keyword rules, and display-item allowances differ by article type and change — verify all on the official Wiley Advanced Materials author page.
