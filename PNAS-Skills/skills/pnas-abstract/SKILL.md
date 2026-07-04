---
name: pnas-abstract
description: Use to write the PNAS abstract — a single self-contained paragraph of ~250 words, quantified and accessible to a broad scientific audience. Distinguishes the abstract (what/how/found, for scientists) from the Significance Statement (why-it-matters, for everyone). Late-stage polish.
---

# Abstract (pnas-abstract)

## When to trigger

- Significance, track, structure, figures, stats, and data are settled (do this late).
- The abstract reads like a methods recap with no result.
- The abstract is being confused with, or duplicated from, the Significance Statement.
- The abstract is over ~250 words, structured with subheadings, or jargon-dense.

## The PNAS abstract: ~250 words, single paragraph, self-contained

- **Length:** up to **~250 words** (confirm the exact cap in current PNAS author guidelines).
- **One paragraph, no subheadings**, no reference citations, no figure/table callouts.
- **Self-contained:** a reader who sees only the abstract should understand the question, what was done, what was found (quantified), and what it means.
- **Accessible** to the broad PNAS readership across Biological/Physical/Social Sciences — define or avoid acronyms.

> Do **not** import a Science-style ≤125-word abstract or a one-sentence summary; PNAS abstracts are longer and there is no one-sentence summary. The short, plain artifact PNAS requires is the **Significance Statement** (`pnas-significance`), which is separate.

## Abstract vs Significance Statement (keep them distinct)

| Abstract | Significance Statement (`pnas-significance`) |
|----------|----------------------------------------------|
| **What/how/found**, for scientists | **Why it matters**, for everyone |
| ~250 words, quantified, technical-but-clear | ≤120 words, plain language |
| Stands in for the paper | Stands in for the "so what" |

If the two read the same, the Significance Statement is wrong — fix it in `pnas-significance`.

## Recommended five-move structure (no labels in the text)

1. **Context / stakes** (1–2 sentences) — the broad problem.
2. **Gap / question** (1 sentence) — what was unknown.
3. **What we did** (1–2 sentences) — approach, in plain terms.
4. **Key results, quantified** (2–3 sentences) — the advance, with numbers and uncertainty.
5. **Conclusion / implication** (1 sentence) — what it means for the field.

## Hard constraints

- [ ] ≤ ~250 words (treat 250 as the ceiling; confirm current cap).
- [ ] Single paragraph, no subheadings, no citations, no figure/table references.
- [ ] Define any acronym on first use, or avoid it.
- [ ] At least one **quantified** result — magnitude + unit + uncertainty (CI/P), not "significantly increased".
- [ ] First sentence comprehensible to a scientist outside the field.
- [ ] Distinct in content and register from the Significance Statement.

## Jargon blacklist (rewrite on sight)

- "Herein we report…", "Importantly,", "Interestingly,", "Notably,"
- Strings of ≥2 undefined acronyms in one sentence.
- "elucidate", "delineate", "interrogate", "leverage" as filler verbs.
- Hedging stacks: "may potentially suggest that it could…".

## Before / after: opening a PNAS abstract for a general reader

The first sentence is read by scientists outside your field. Lead with the stake, not the apparatus.

- **Before:** "Using single-molecule FRET with ALEX and HMM state assignment, we interrogated the conformational landscape of protein X to elucidate its allosteric coupling."
- **After:** "How a protein converts a signal at one site into a response at a distant site is a long-standing question across biology. We tracked single molecules of protein X in real time and found that two conformations exchange 40-fold faster when the regulator is bound (rate 12 ± 2 s⁻¹), revealing the coupling step directly."

The revision opens on a cross-division stake, drops the undefined acronym stack, and puts a quantified result with uncertainty where a broad reader can see it.

## Referee-facing checklist for the abstract

A PNAS editor scanning the abstract before assigning reviewers checks:

- [ ] **First sentence is field-general** — a reader from another PNAS division grasps why the question matters.
- [ ] **The headline result is quantified** — magnitude, unit, and uncertainty, not "significantly."
- [ ] **The advance matches the Significance Statement's claim** — no broader promise here than the paper delivers.
- [ ] **Register differs from the Significance Statement** — technical-but-clear here; plain-language why-it-matters there.

## Output format

```
【Abstract】 single paragraph (word count: N ≤ 250)
【Five moves present?】 context / gap / approach / quantified result / implication
【Quantified headline result?】 yes/no + the number
【Distinct from Significance Statement?】 yes/no
【Jargon hits removed】 [...]
【Next】 pnas-citation
```

## Anti-patterns

- **Do not** reuse the ≤120-word Significance Statement as the abstract (or vice versa).
- **Do not** import a Science ≤125-word abstract or one-sentence summary — wrong genre for PNAS.
- **Do not** open with method or organism; open with the stake.
- **Do not** end on "further work is needed" — end on the implication.
- **Do not** add subheadings; PNAS abstracts are single unstructured paragraphs.
