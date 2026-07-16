---
name: molcell-summary
description: Use to write Molecular Cell's Summary — a single unstructured paragraph (~150 words; re-check on the official site) that conveys the molecular question, the mechanism, and its physiological consequence, named and quantified for a molecular-biology readership. Late-stage polish.
---

# Summary / Abstract (molcell-summary)

## When to trigger

- Mechanism, framing, and structure are settled (do this late).
- The abstract reads like a method recap with no molecular mechanism or result.
- It exceeds the word ceiling, uses subheadings, or is dense with undefined acronyms.
- It states *that* something happens but never *how* at the molecular level.

## What Molecular Cell calls it

Molecular Cell's abstract is the **Summary**: a **single, unstructured paragraph** (no subheadings, no citations) of roughly **≤150 words** (treat as a ceiling; confirm the current cap). It is written for a **molecular-biology readership** — you can assume familiarity with the process but must still name the mechanism and quantify. It must convey the molecular question, the mechanism, and why it matters physiologically.

## Five-move structure (no labels in the text)

1. **Molecular context / stakes** (1 sentence) — the process and the step at issue.
2. **Gap / question** (1 sentence) — what molecular event was unknown.
3. **What we did + what we found** (2–3 sentences) — the mechanism, with the key quantified results and the orthogonal evidence that proves it.
4. **Mechanism stated explicitly** — name the molecular cause (residue, base, interface, step), not just the phenotype.
5. **Physiological consequence** (1 sentence) — why the mechanism matters in cells/in vivo.

Because Molecular Cell rewards depth, the Summary should make clear the mechanism is *established* by independent methods, not merely proposed.

## Hard constraints

- [ ] ≤ ~150 words (confirm the current cap on the official site).
- [ ] Single paragraph; **no subheadings, no citations**, no figure/table references.
- [ ] Define any acronym on first use, or avoid it.
- [ ] Names the **molecular mechanism** explicitly (the *how*), not only the observation.
- [ ] At least one **quantified** result (e.g., "10-fold faster," "a 2.9 Å structure," not "significantly").
- [ ] First sentence is legible to a molecular biologist outside the exact subfield.

## Jargon blacklist (rewrite on sight)

- "Herein we report…", "Importantly,", "Interestingly,", "Notably,", "Strikingly,"
- Strings of ≥2 undefined gene/protein/complex acronyms in one sentence.
- "elucidate", "delineate", "interrogate", "dissect", "shed light on" as filler verbs.
- Hedging stacks: "may potentially suggest that it could…".
- Ending on "further studies are needed" — end on the physiological consequence.

## Quantification check

Every effect claim should carry a number somewhere in the paper, and the headline belongs in the Summary: a rate, a fold-change, an affinity, a resolution, an occupancy. A Summary with zero numbers is not finished.

## What the in-house editor reads first

Molecular Cell's initial triage is run by professional in-house scientific editors. They decide in minutes whether the paper goes to review, and the Summary plus the title are usually all they read when they decide. Two questions dominate: (1) is there a *molecular mechanism* here, worked out and validated — or only a phenotype with a proposed cause; and (2) is the mechanism proven by more than one approach. Write the Summary so both answers are visible without the figures. A Summary that names a molecule, a molecular action, and a physiological consequence survives triage; a Summary that lists assays performed does not.

## Worked micro-example (before → after)

Before (method recap, no mechanism, no number, 39 words):

> Here we studied the helicase XYZ using cryo-EM and biochemistry. We solved several structures and performed unwinding assays. XYZ was important for replication. These findings advance our understanding of DNA replication.

After (mechanism named, quantified, physiological stake, ~85 words):

> How replicative helicases couple ATP hydrolysis to strand separation at a stalled fork is unclear. Combining a 2.9 Å cryo-EM structure with single-molecule unwinding, we find that the helicase XYZ grips the lagging strand through a conserved β-hairpin and that hydrolysis at a single subunit ratchets one nucleotide per step. A hairpin point mutant uncouples ATPase from unwinding, slowing fork progression 12-fold and sensitizing cells to replication stress. XYZ thus converts nucleotide hydrolysis into processive, strand-selective translocation that safeguards genome duplication.

The "after" version names the actor (XYZ), the molecular mechanism (β-hairpin grip; single-subunit ratchet), a quantified effect (2.9 Å; 12-fold), orthogonal evidence (structure + single-molecule + mutant), and a physiological consequence.

## Output format

```
【Summary】 single paragraph (word count: N ≤ ~150)
【Five moves present?】 context / gap / approach+result / mechanism named / physiological consequence
【Mechanism explicit?】 yes/no — the named molecular cause
【Quantified headline result?】 yes/no + the number
【Jargon hits removed】 [...]
【Next】 molcell-highlights
```

## Anti-patterns

- **Do not** use subheadings or a structured-abstract format — the Summary is one paragraph.
- **Do not** describe only the phenomenon; name the molecular mechanism.
- **Do not** open with the technique; open with the molecular stake.
- **Do not** pad past the ceiling; the limit is a feature.
- **Do not** confuse the Summary with the eTOC blurb (that one is third-person and lay; see `molcell-highlights`).

> The ~150-word cap is a working default — confirm against the current Molecular Cell information-for-authors page.
