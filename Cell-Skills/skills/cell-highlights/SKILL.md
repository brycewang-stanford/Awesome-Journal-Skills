---
name: cell-highlights
description: Use to produce the three signature Cell front-matter artifacts — Highlights (3–4 bullets, each ≤85 characters), the eTOC/In Brief blurb (~50 words, third-person), and the Graphical Abstract (single-panel visual summary). Late-stage polish.
---

# Highlights, eTOC Blurb & Graphical Abstract (cell-highlights)

## When to trigger

- Significance, framing, figures, and Summary are settled (do this late).
- The submission lacks Highlights, an eTOC/In Brief blurb, or a Graphical Abstract.
- Highlights are full sentences or run over the character limit.
- The Graphical Abstract is a multi-panel figure crammed into one box.

These three artifacts are **mandatory, Cell-specific** deliverables. Editors and the table of contents use them heavily — weak ones hurt at every stage.

## 1. Highlights (exactly 3–4 bullets, each ≤ 85 characters incl. spaces)

Short telegraphic phrases — **not** full sentences — that a scanning reader absorbs in seconds. Each bullet states one finding; together they trace the arc.

Rules:
- [ ] **3 or 4 bullets**, no more, no fewer.
- [ ] **≤ 85 characters including spaces** per bullet (count them).
- [ ] Phrase fragments, present tense, no trailing period, no citations.
- [ ] No undefined acronyms; readable by a general life-scientist.
- [ ] Bullets progress phenomenon → mechanism → causality → significance.

Template:
```
- [Actor] [does] [effect] in [system]                 (≤85 chars)
- [Mechanism]: [molecular cause] of [phenomenon]        (≤85 chars)
- [Perturbation] [reverses/abolishes] [phenotype]       (≤85 chars)
- [Broad implication for field / disease]               (≤85 chars)
```

## 2. eTOC blurb / "In Brief" (~50 words, third-person)

A short paragraph for the online table of contents, written **about** the paper in the **third person** (refer to the authors as "Smith et al." or "the authors"), aimed at **non-specialists**. It explains, in plain language, what was found and why it matters — not a methods recap.

Rules:
- [ ] ~50 words (treat as the ceiling; confirm current cap).
- [ ] Third person — never "we"/"here we show".
- [ ] Plain language; no jargon, no acronyms, minimal gene names.
- [ ] States the take-home significance for a broad reader.

Template:
```
[Author et al.] show that [plain-language finding]. [One sentence of mechanism in
lay terms.] [One sentence on why it matters for the field, biology, or disease.]
```

## 3. Graphical Abstract (single-panel visual summary)

One self-contained image that conveys the take-home message at a glance.

Design rules:
- [ ] **Single panel** — NOT a multi-panel figure; no A/B/C sub-panels.
- [ ] Clear **top-to-bottom or left-to-right** flow (cause → effect).
- [ ] **Minimal text** — short labels only; no paragraphs, no figure legend.
- [ ] Tells the **story**, not the methods; shows the mechanism/outcome.
- [ ] Self-explanatory without the paper.
- [ ] Square-ish format; high resolution (e.g., ~1200 px wide, RGB). Confirm exact size/format in current Cell Press guidelines.
- [ ] Colorblind-safe; consistent with main-figure style.

Avoid: cramming the whole model, tiny fonts, multiple disconnected scenes, decorative clip-art that obscures the message.

## Worked Highlights set (with char counts)

For the XYZ1–ABC2 dormancy story, a compliant four-bullet arc — phenomenon → mechanism → causality → significance:

```
- CRISPR screen identifies XYZ1 as a brake on intestinal stem-cell division   (74)
- XYZ1 phosphorylates ABC2, blocking its entry into the nucleus              (60)
- XYZ1 loss frees ABC2, expanding the stem pool 3.2-fold                      (56)
- A nutrient-gated switch couples niche state to reversible dormancy          (60)
```

Each is a fragment, present tense, no period, no citation, and under 85 characters. Contrast a non-compliant bullet: "In this study, we demonstrate that the kinase XYZ1 phosphorylates ABC2 to restrict its nuclear localization." — that is a full sentence, opens with filler, and runs well over the limit. Trim to the actor-verb-object core and drop "we".

Counting tip: count the rendered string including spaces, not the Markdown. When a bullet lands at 84–85, prefer cutting a word over abbreviating into an undefined acronym — the eTOC audience is broad.

## Worked eTOC blurb (before → after)

Before (first person, jargon, methods recap):

> Here we use organoid CRISPR screens to show that XYZ1 phosphorylates ABC2 and regulates ISC dynamics.

After (third person, lay, significance-forward, ~48 words):

> Smith et al. show how the gut renews itself only when conditions allow. A single enzyme holds intestinal stem cells in a resting state by keeping a growth-driving factor out of the cell's nucleus; releasing that brake expands the stem-cell pool and speeds tissue repair after injury.

The "after" version never says "we", spells out the biology for a non-specialist, drops the gene names into plain description, and closes on why a broad reader should care.

## Output format

```
【Highlights】 3–4 bullets, each with its char count (must be ≤85)
   - "..."  (NN chars)
   - "..."  (NN chars)
   - "..."  (NN chars)
【eTOC blurb】 third-person paragraph (word count: N ≈ 50)
【Graphical Abstract】 described: flow direction, key elements, single-panel? yes/no
【Checks】 bullets ≤85 / blurb third-person / GA single-panel-minimal-text → pass/fail
【Next】 cell-citation
```

## Anti-patterns

- **Do not** write Highlights as full sentences or exceed 85 characters.
- **Do not** write the eTOC blurb in the first person ("we show").
- **Do not** make the Graphical Abstract a busy multi-panel montage.
- **Do not** copy the Summary into the eTOC blurb — the blurb is third-person and lay.

> Character/word limits and Graphical Abstract size are working defaults — confirm against current Cell Press author guidelines.
