---
name: molcell-highlights
description: Use to produce the three signature Cell Press front-matter artifacts for Molecular Cell — Highlights (3–4 bullets, each ≤85 characters), the eTOC/In Brief blurb (~50 words, third-person), and the Graphical Abstract (single-panel visual summary of the mechanism). Late-stage polish.
---

# Highlights, eTOC Blurb & Graphical Abstract (molcell-highlights)

## When to trigger

- Mechanism, framing, figures, and Summary are settled (do this late).
- The submission lacks Highlights, an eTOC/In Brief blurb, or a Graphical Abstract.
- Highlights are full sentences or run over the character limit.
- The Graphical Abstract is a multi-panel figure crammed into one box.

These three artifacts are **mandatory, Cell Press** deliverables at Molecular Cell. Editors and the table of contents use them heavily — weak ones hurt at every stage.

## 1. Highlights (3–4 bullets, each ≤ 85 characters incl. spaces)

Short telegraphic phrases — **not** full sentences — that a scanning molecular biologist absorbs in seconds. Each bullet states one finding; together they trace the proof of mechanism.

Rules:
- [ ] **3 or 4 bullets**, no more, no fewer.
- [ ] **≤ 85 characters including spaces** per bullet (count them).
- [ ] Phrase fragments, present tense, no trailing period, no citations.
- [ ] No undefined acronyms beyond well-known molecular names; readable across subfields.
- [ ] Bullets progress phenomenon → mechanism → separation-of-function/causality → consequence.

Template:
```
- [Actor] [molecular action] on [substrate]                (≤85 chars)
- [Mechanism]: [residue/interface/step] drives [process]   (≤85 chars)
- [Point mutant] uncouples [activity] from [outcome]        (≤85 chars)
- [Physiological consequence for the process]               (≤85 chars)
```

## 2. eTOC blurb / "In Brief" (~50 words, third-person)

A short paragraph for the online table of contents, written **about** the paper in the **third person** ("Smith et al." / "the authors"), aimed at **readers outside the exact subfield**. It explains what was found and why it matters molecularly — not a methods recap.

Rules:
- [ ] ~50 words (treat as the ceiling; confirm current cap).
- [ ] Third person — never "we"/"here we show".
- [ ] Plain molecular language; minimal undefined acronyms.
- [ ] States the take-home mechanistic significance.

Template:
```
[Author et al.] show that [plain-language molecular finding]. [One sentence of
mechanism in accessible terms.] [One sentence on why it matters for the process
or for disease.]
```

## 3. Graphical Abstract (single-panel visual summary)

One self-contained image that conveys the mechanism at a glance.

Design rules:
- [ ] **Single panel** — NOT a multi-panel figure; no A/B/C sub-panels.
- [ ] Clear **left-to-right or top-to-bottom** flow (cause → mechanism → effect).
- [ ] **Minimal text** — short labels only; no paragraphs, no legend.
- [ ] Shows the **molecular mechanism/outcome**, not the methods.
- [ ] Self-explanatory without the paper.
- [ ] Square-ish, high resolution (e.g., ~1200 px wide, RGB). Confirm exact size/format in current Cell Press guidelines.
- [ ] Colorblind-safe; consistent with main-figure iconography.

Avoid: cramming the whole model, tiny fonts, disconnected scenes, decorative clip-art.

## Worked Highlights set (with char counts)

For the XYZ helicase story, a compliant four-bullet arc — phenomenon → mechanism → causality → consequence:

```
- Cryo-EM captures helicase XYZ gripping the lagging strand           (66)
- A conserved beta-hairpin couples ATP hydrolysis to unwinding        (61)
- A hairpin mutant uncouples ATPase from strand separation            (57)
- Single-subunit hydrolysis paces processive fork unwinding           (58)
```

Each is a fragment, present tense, no period, no citation, under 85 characters. Contrast a non-compliant bullet: "In this study, we show that the helicase XYZ uses a conserved beta-hairpin to couple ATP hydrolysis to DNA unwinding." — that is a full sentence, opens with filler, and runs well over the limit. Trim to the actor-action-object core and drop "we".

Counting tip: count the rendered string including spaces, not the Markdown. When a bullet lands at 84–85, cut a word rather than abbreviate into an undefined acronym.

## Worked eTOC blurb (before → after)

Before (first person, jargon, methods recap):

> Here we use cryo-EM and single-molecule assays to show that XYZ couples ATP hydrolysis to unwinding at the replication fork.

After (third person, accessible, significance-forward, ~48 words):

> Zhang et al. show how a replicative helicase turns chemical energy into motion. The enzyme grips one DNA strand with a small conserved loop and burns ATP one subunit at a time to pry the strands apart, a stepwise mechanism that keeps DNA replication moving through obstacles.

## Output format

```
【Highlights】 3–4 bullets, each with its char count (must be ≤85)
   - "..."  (NN chars)
   - "..."  (NN chars)
   - "..."  (NN chars)
【eTOC blurb】 third-person paragraph (word count: N ≈ 50)
【Graphical Abstract】 described: flow direction, key molecular elements, single-panel? yes/no
【Checks】 bullets ≤85 / blurb third-person / GA single-panel-minimal-text → pass/fail
【Next】 molcell-citation
```

## Anti-patterns

- **Do not** write Highlights as full sentences or exceed 85 characters.
- **Do not** write the eTOC blurb in the first person ("we show").
- **Do not** make the Graphical Abstract a busy multi-panel montage or a re-used figure.
- **Do not** copy the Summary into the eTOC blurb — the blurb is third-person and accessible.

> Character/word limits and Graphical Abstract size are working defaults — confirm against the current Molecular Cell / Cell Press author guidelines.
