---
name: jacs-writing-style
description: Use when polishing prose to ACS house style and claim discipline for a Journal of the American Chemical Society (JACS) manuscript. Edits language, structure, and nomenclature — it does not add data or design figures.
---

# ACS House Style and Claim Discipline (jacs-writing-style)

## When to trigger

- The data and figures are solid and the manuscript needs language polish
- Prose is wordy, over-claimed, or uses vague boosters ("novel", "very important")
- Nomenclature, units, or abbreviations are inconsistent
- Citation style is not ACS-numbered

## ACS prose conventions

- **Concise and declarative.** State what was done and found; avoid padding and throat-clearing.
- **Tense/voice.** Past tense for what you did and observed; present for established facts. Active voice is acceptable and encouraged in ACS writing where it improves clarity.
- **Compound numbering.** Bold numerals (e.g., **3a**); the same number always means the same structure across text, schemes, and SI.
- **Nomenclature.** Correct IUPAC/ACS names or clearly defined trivial names; consistent throughout.
- **Units and symbols.** SI units, italic variables (e.g., *J*, *T*, *k*), roman unit symbols; spaces between number and unit (5 mol %, 80 °C).
- **Abbreviations.** Define at first use; use standard ACS abbreviations for reagents/solvents.
- **Citations.** ACS numbered style (superscript), references in citation order; abbreviated journal titles.

## Section discipline

| Section | Job | Common failure |
|---------|-----|----------------|
| Abstract | Problem → advance → key numbers → significance | Vague, no quantitative result |
| Introduction | Frame the problem and the gap; end with what this paper shows | Mini-review with no clear thesis |
| Results & Discussion | Evidence in logical order; interpret as you go | Data dump without interpretation |
| Conclusion | What is now established and enabled | Repeats the abstract verbatim |

## Claim discipline (what JACS referees punish)

- Match every adjective to evidence: "general" needs scope; "efficient" needs numbers; "mechanism" needs probes.
- Replace boosters with facts: not "dramatically improved", but "increased yield from 42% to 91%".
- Hedge appropriately where evidence is suggestive ("consistent with", "we propose") vs proven ("we show").
- State the closest prior art and the specific delta; do not imply more novelty than the search supports.

## Booster blacklist (replace with a number or a fact)

`novel` · `very important` · `dramatically` · `unprecedented` (unless defensible) ·
`a variety of` (say how many) · `excellent yield` (give the %) · `mild conditions`
(state T/time) · `clean reaction` (give purity evidence).

## Worked micro-edits (before → after, JACS register)

- **Booster → number.**
  Before: *"The novel catalyst showed excellent activity under mild conditions."*
  After: *"Catalyst **1** (2 mol %) delivered **3a** in 94% yield at 25 °C in 2 h."*
- **Hedge calibrated to evidence.**
  Before: *"These results prove that a Pd(0)/Pd(II) cycle is operative."*
  After: *"A first-order dependence on [**1**] and a KIE of 4.2 are consistent with turnover-limiting C–H cleavage at Pd(0)."*
- **Thesis sentence closing the Introduction.**
  Before: *"C–H activation has attracted much attention in recent years."*
  After: *"Here we show that a confined anionic ligand overrides innate site selectivity, fluorinating the distal methylene of unactivated alkanes with 95:5 er."*
- **Delta vs prior art stated, not implied.**
  Before: *"Unlike all previous work, our system is truly general."*
  After: *"Whereas prior amidation catalysts required directing groups, **1** functionalizes 24 of 27 undirected substrates, including three drug scaffolds."*

## Chemistry typography that referees notice

- Bonds and ranges take an **en dash**: C–H, Pd–O, 25–40 °C; hyphens only in names (*tert*-butyl).
- Isotope and decoupling notation set correctly: ¹³C{¹H}, ²H-labeled, *d*₆-DMSO (or DMSO-*d*₆ — pick one and hold it).
- Locants and descriptors italic: *o*-, *m*-, *p*-, *cis*/*trans*, *E*/*Z*, *R*/*S*, *syn*/*anti*, *N*-methyl.
- Greek letters roman when structural (α,β-unsaturated), italic when variables (λ, δ used as symbols follow ACS conventions).
- "ee" and "er" defined once; report er where the measurement is chromatographic, and be consistent.
- Reaction arrows in prose spelled out ("gave", "afforded", "underwent") — no "→" in running text.

## Checklist

- [ ] Abstract has problem → advance → number → significance
- [ ] Every "general/efficient/selective/mild" is backed by a number or condition
- [ ] Compound numbering and nomenclature consistent text/scheme/SI
- [ ] Units, italics, and spacing follow ACS conventions
- [ ] Citations are ACS-numbered, in order, with abbreviated titles
- [ ] No booster from the blacklist survives unreplaced
- [ ] Conclusion adds the "now enabled", not a copy of the abstract

## Anti-patterns

- Significance asserted by adjective rather than shown by data
- Inconsistent compound numbers or names across the paper
- Introduction that reviews the field but never states the paper's thesis
- Mixed citation styles; non-ACS reference formatting
- "Mild/clean/efficient" with no supporting numbers

## Output format

```
【Abstract structure】OK / fix: [...]
【Booster hits】N — replaced: [...]
【Numbering/nomenclature consistent】Y/N
【Units/ACS conventions】OK / fix: [...]
【Citations ACS-numbered】Y/N
【Next】jacs-length-management → jacs-cover-letter
```

## Related resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — ACS citation styles for Zotero/EndNote, ACS Style Guide
