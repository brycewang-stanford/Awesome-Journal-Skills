---
name: epsl-writing-style
description: Use when drafting or compressing prose for an Earth and Planetary Science Letters (EPSL) manuscript. The letters format demands a main text near the 6,500-word cap, a process-forward title and abstract, and prose legible to geochemists, geophysicists, and planetary scientists at once. It guides writing and cutting; it does not invent content.
---

# Writing Style (epsl-writing-style)

EPSL prose has a recognizable gait: it opens on the process question, lands the decisive number
early, and spends its limited words on interpretation rather than inventory. The house constraints
are the **word cap on the main text** (about 6,500 words, introduction through conclusions — re-check
the exact figure on the official site), an author–date reference style (re-check the current
formatting instructions), and a readership that spans four sub-fields, so every specialist term costs
you part of the audience.

## When to trigger

- Drafting the title, abstract, or introduction
- Cutting an over-length draft down to the letters cap
- De-jargonizing prose for the cross-disciplinary readership
- Deciding what moves from the main text to the supplement

## Structure & style EPSL expects

1. **Title names the process, not the place.** "Slab dehydration depth controls arc volatile flux"
   travels; "Geochemistry of lavas from the X arc, Country Y" announces a regional study — the
   desk-screen tell.
2. **Abstract = the whole Letter in miniature.** Question, approach, headline number with uncertainty
   and units, and the process-level consequence — a reader should be able to cite you from the
   abstract alone.
3. **Introduction closes on the discriminating test.** Two to four paragraphs from the open question,
   through the tension in existing constraints, to "here we test A against B using C."
4. **Methods lean, supplement full.** The main text carries what a reader needs to judge the logic;
   the traceability chain lives in the supplement (see `epsl-reporting-and-reproducibility`).
5. **Interpret; never inventory.** "Sample 14 has 5.2 ppm; sample 15 has 4.8 ppm…" is a table
   pretending to be prose. Lead each results paragraph with what the pattern means.
6. **Write across sub-fields.** Expand acronyms at first use, gloss method-specific quantities in one
   clause ("MSWD, a χ²-like measure of scatter"), and keep the physical picture in view.

## Where the word budget goes

| Section | Budget instinct | Common failure |
|---------|-----------------|----------------|
| Abstract | dense; every sentence load-bearing | vague "implications are discussed" |
| Introduction | short arc to the test | a regional literature tour |
| Methods | minimum for logic; rest → supplement | protocol dumps eating 1,500 words |
| Results | patterns + the discriminating comparison | analysis-by-analysis inventory |
| Discussion | the process consequence + limits | re-narrating results with adjectives |
| Conclusions | 3–5 sentences, portable claims | a second abstract |

## Worked micro-example (illustrative — compressing a regional opener)

- **Before:** "The X Basin, located in northern Y, has been studied since the 1960s. Previous workers
  described its stratigraphy (refs), structure (refs), and geochemistry (refs). Here we present new
  detrital-zircon data from the basin." — three sentences, zero process, reads regional.
- **After:** "How quickly eroded mountains appear in the sedimentary record sets the resolution of
  detrital archives everywhere, yet the lag between exhumation and deposition has never been measured
  directly. We date both sides of the conveyor — bedrock cooling and basin deposition — in a single
  system." — the same paper, now framed as a portable question.

Compression tactic that recovers the most words at EPSL: convert every results-inventory paragraph
into one topic sentence plus a pointer to the figure, and move its detail to the supplement.

## Referee-pushback patterns and the venue-specific fix

- *"Reads like a regional report."* → Rewrite title + abstract + intro close around the process; the
  data sections usually survive intact.
- *"Inaccessible outside the authors' specialty."* → Gloss method terms; add one physical-picture
  sentence per technical paragraph.
- *"Over length."* → Cut methods detail and results inventory to the supplement before touching the
  discussion; the interpretation is why EPSL accepted the paper.

## Anti-patterns

- A place-name title for a process paper
- An abstract that withholds the headline number ("we discuss the implications…")
- Introduction as chronological literature history rather than a tension to be resolved
- Jargon walls: unexpanded acronyms, unglossed δ-notation, sub-field slang
- Blowing the cap with in-text protocol and inventory instead of using the supplement
- Conclusions that hedge the portable claim the abstract promised

## Output format

```
【Title】process-forward? [Y/N + suggested rewrite]
【Abstract】question + approach + number±σ + consequence? [Y/N]
【Intro close】discriminating test stated? [Y/N]
【Word count】main text vs ~6,500 cap (re-check) [count]
【Cross-field legibility】acronyms/notation glossed? [Y/N]
【Next】epsl-cover-letter
```

## Supplementary resources

- [`../../resources/worked-examples/01-introduction.md`](../../resources/worked-examples/01-introduction.md) — a before→after EPSL-style abstract + introduction
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — Guide for Authors: length, reference style, structure
