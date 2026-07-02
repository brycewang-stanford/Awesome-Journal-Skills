---
name: cell-summary
description: Use to write Cell's Summary — a single unstructured paragraph of ≤ ~150 words that conveys the complete story, the mechanism, and the broad significance, quantified and readable by a general life-scientist. Late-stage polish.
---

# Summary / Abstract (cell-summary)

## When to trigger

- Significance, framing, and structure are settled (do this late).
- The abstract reads like a method recap with no mechanism or result.
- It exceeds ~150 words, uses subheadings, or is dense with acronyms.
- It states *that* something happens but never *how* (no mechanism).

## What Cell calls it

Cell's abstract is the **Summary**: a **single, unstructured paragraph** (no subheadings, no citations) of roughly **≤150 words**, written for a broad life-sciences readership — not your subfield. It must convey the **complete story**: the question, the mechanism, and why it matters, with quantification.

## Five-move structure (no labels in the text)

1. **Context / stakes** (1 sentence) — the broad biological problem.
2. **Gap / question** (1 sentence) — what was unknown.
3. **What we did + what we found** (2–3 sentences) — the mechanism, with the key quantified results and the converging evidence that makes it a complete story.
4. **Mechanism stated explicitly** — name the molecular/cellular cause, not just the phenotype.
5. **Significance** (1 sentence) — why a broad community should care.

Because Cell demands completeness, the Summary should make clear that the mechanism is *established*, not merely proposed — convey that multiple lines of evidence converge.

## Hard constraints

- [ ] ≤ ~150 words (treat 150 as the ceiling; confirm the current cap).
- [ ] Single paragraph; **no subheadings, no citations**, no figure/table references.
- [ ] Define any acronym on first use, or avoid it.
- [ ] Names the **mechanism** explicitly (the *how*), not only the observation.
- [ ] At least one **quantified** result (e.g., "reduced 3-fold," not "significantly reduced").
- [ ] First sentence is comprehensible to a life-scientist outside the subfield.

## Jargon blacklist (rewrite on sight)

- "Herein we report…", "Importantly,", "Interestingly,", "Notably,", "Strikingly,"
- Strings of ≥2 undefined gene/protein acronyms in one sentence.
- "elucidate", "delineate", "interrogate", "dissect", "leverage" as filler verbs.
- Hedging stacks: "may potentially suggest that it could…".
- Ending on "further studies are needed" — end on significance.

## Quantification check

Every effect claim should carry a number somewhere in the paper, and the headline effect belongs in the Summary: magnitude + unit + (where natural) statistical support. A Summary with zero numbers is not finished.

## What the in-house editor reads first

Cell's initial triage is run by a professional in-house scientific editor, not a rotating academic. That editor decides in minutes whether the paper goes to review, and the Summary plus the title are usually all they have read when they decide. Two questions dominate that read: (1) is there a *complete mechanism* here, or only a phenotype awaiting explanation, and (2) will this move a field beyond the authors' own subspecialty. Write the Summary so both answers are visible without the figures. A Summary that names a molecule, a mechanistic verb, and a cross-field consequence survives triage; a Summary that lists assays performed does not.

Because the editor also weighs breadth, the final sentence carries disproportionate weight — it is the sentence a reviewer-recruiting editor quotes when pitching the paper to a potential referee. Make the closing significance concrete (a process, a disease axis, a conserved principle), never a generic "these findings advance our understanding."

## Worked micro-example (before → after)

Before (method recap, no mechanism, no number, 41 words):

> Here we performed single-cell RNA sequencing and CRISPR screening in mouse intestinal organoids to study stem-cell regulation. We identified several candidate regulators and validated one by knockout, which affected proliferation. These findings advance our understanding of tissue homeostasis.

After (mechanism named, quantified, broad stake, 78 words toward the ≤150 ceiling):

> How intestinal stem cells sense a depleted niche and pause division is unclear. Combining organoid CRISPR screening with lineage tracing, we find that the kinase XYZ1 phosphorylates the transcription factor ABC2, restricting its nuclear entry and holding stem cells in reserve. XYZ1 loss drives ABC2 into the nucleus, expands the stem pool 3.2-fold, and accelerates crypt regeneration after injury. XYZ1-ABC2 thus couples nutrient state to a reversible dormancy switch that safeguards regenerative capacity across self-renewing epithelia.

The "after" version names the actor (XYZ1), the mechanism (phosphorylation gating nuclear entry), a quantified effect (3.2-fold), converging evidence (screen + tracing + loss-of-function), and a stake broader than the intestine.

## Output format

```
【Summary】 single paragraph (word count: N ≤ 150)
【Five moves present?】 context / gap / approach+result / mechanism named / significance
【Mechanism explicit?】 yes/no — the named molecular/cellular cause
【Quantified headline result?】 yes/no + the number
【Jargon hits removed】 [...]
【Next】 cell-highlights
```

## Anti-patterns

- **Do not** use subheadings or a structured-abstract format — Cell's Summary is one paragraph.
- **Do not** describe only the phenomenon; name the mechanism.
- **Do not** open with the organism or assay; open with the biological stake.
- **Do not** pad past ~150 words; the cap is a feature.
- **Do not** confuse the Summary with the eTOC blurb (that one is third-person and lay; see `cell-highlights`).

> The ~150-word cap is a working default — confirm against current Cell Press author guidelines.
