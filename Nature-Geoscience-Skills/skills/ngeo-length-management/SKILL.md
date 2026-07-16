---
name: ngeo-length-management
description: Use when a Nature Geoscience manuscript exceeds the ~3,000-word Article limit, the 4-6 display-item ceiling, or the reference cap, where content must be relocated to online Methods or Supplementary Information. Triages what to cut, compress, or move; does not rewrite content from scratch.
---

# Nature Geoscience Length Management (ngeo-length-management)

## When to trigger

- The main text is over the ~3,000-word Article limit (or you suspect it is)
- You have more than 4–6 display items or more than ~50 references
- You must decide what to cut, compress, or push to online Methods / SI
- A coauthor keeps adding regional detail and sensitivity tests
- Late stage: content, figures, and SI are stable and now must fit the container

## How the Nature Geoscience length limits work

An Article is **short and tightly bounded** (verify current values on the author pages):

- **Main text**: up to ~3,000 words, *excluding* abstract, online Methods, references, and figure legends.
- **Abstract**: up to ~200 words, unreferenced.
- **Title**: up to ~90 characters.
- **Display items**: 4–6 figures and/or tables combined.
- **References**: typically up to ~50 in the main list.
- **Brief Communication** (the short format): ~1,000–1,500 words, ≤2 display items, ≤20 references, ~70-word abstract.

Unlike a deductible page budget, Nature counts these categories **separately**: text, display items, and references each have their own ceiling. The relief valves are the online **Methods** (excluded from the word count) and the **Supplementary Information** — the main text stays lean by pushing the reproducible and extended material outward.

## Triage order (cut from cheapest loss to most painful)

1. **Move protocol to online Methods first.** Instrument detail, model configuration, statistical procedure, and the full uncertainty budget belong in Methods, which does *not* count against the 3,000-word main-text limit. This is usually the largest, lowest-pain saving (see `ngeo-methods`).
2. **Move extended data to SI.** Additional maps, full model ensembles, sensitivity sweeps, secondary proxies → Supplementary Information (see `ngeo-supplementary`).
3. **Merge / cut display items.** Combine related panels; move non-essential figures to SI to get within 4–6.
4. **Prune references** to the works that establish importance or are needed for trust; consolidate where Nature style permits, to stay near ~50.
5. **Tighten prose** (apply `ngeo-writing-style`): remove padding, hedging, regional-setting tours, and figure-transcribing sentences.
6. **Cut scope** as a last resort: demote a supporting result entirely.

## Cost-awareness table

| Element                              | Where the budget bites        | Cheapest fix                              |
|--------------------------------------|-------------------------------|-------------------------------------------|
| Instrument / model-setup paragraph    | main-text word count          | move to online Methods (excluded)         |
| Full uncertainty budget in main text  | main-text word count          | move to online Methods                    |
| Seventh figure / dense map grid       | display-item ceiling          | merge or move to SI                       |
| Regional-setting tour in the opening  | main-text word count          | compress to one sentence                  |
| Over-long reference list              | reference cap (~50)           | prune to importance + trust essentials    |
| Sensitivity sweeps in the body        | main-text word count + figures| move to SI                                |
| Figure legend padding                 | (legends excluded, but tighten)| tighten for clarity                       |

## Checklist

- [ ] Main text is within the ~3,000-word limit (excluding abstract/Methods/refs/legends)
- [ ] Abstract ≤ ~200 words, unreferenced; title ≤ ~90 characters
- [ ] Display items within the 4–6 ceiling
- [ ] References near / under the ~50 cap, pruned to essentials
- [ ] Reproducible protocol and full uncertainty budget are in online Methods, not the main text
- [ ] Extended data and sensitivity tests are in SI
- [ ] Prose padding, hedging, and regional tours removed (cross-check `ngeo-writing-style`)
- [ ] The main text still stands alone after trimming (cross-check `ngeo-supplementary`)

## Anti-patterns

- Counting only words and being surprised the display-item or reference ceiling is blown
- Trimming load-bearing content (the decisive evidence, the headline uncertainty) to fit
- Padding online Methods or SI until the main text no longer stands alone
- Leaving instrument/model detail in the main text that belongs in (excluded) Methods
- Keeping a seventh decorative figure over the 4–6 ceiling
- Discovering the over-length only at submission, after content is frozen

## Output format

```
【Main text vs. ~3,000】over by ~X words (verify current limit)
【Abstract / title within limits】yes / fix
【Display items】N (≤6) — merge/move list
【References】N vs. ~50 — prune list
【Moved to online Methods】list (excluded from word count)
【Moved to SI】list
【Still stands alone】yes / fix
【Next】ngeo-cover-letter or ngeo-submission
```

> The word/display-item/reference limits and content-type definitions are exactly the kind of volatile specifics that change — always verify current limits on the official Nature Geoscience author pages (Checked: 2026-07-16).
