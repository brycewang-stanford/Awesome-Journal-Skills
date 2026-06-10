---
name: jacs-supplementary
description: Use when assembling the Supporting Information for a Journal of the American Chemical Society (JACS) manuscript — complete procedures, full compound characterization, copies of key spectra, and crystallographic CIFs/CCDC numbers. Builds and audits the SI — it does not decide which experiments to run.
---

# Supporting Information (jacs-supplementary)

## When to trigger

- The main text is set and the SI must be assembled
- A reviewer could ask "where is the procedure / spectrum / CIF?"
- You are unsure what belongs in the SI vs the main text
- Crystal structures need depositing before submission

## What the SI must contain

The SI is where JACS rigor is verified. It should let an independent chemist
**reproduce every result and confirm every structure**.

### General experimental

- [ ] Materials and sources; drying/purification of solvents and reagents
- [ ] Inert-atmosphere / glovebox conditions where relevant
- [ ] Instruments and conditions (NMR field/solvent reference, HRMS mode, IR mode, diffractometer, etc.)
- [ ] Safety/hazard notes for dangerous reagents or procedures

### Per-compound (for every new compound)

- [ ] **Full procedure** — scale, equivalents, temperature, time, workup, purification; isolated yield
- [ ] **Characterization block** — ¹H, ¹³C{¹H} (+ heteronuclear as needed), HRMS (calcd/found), IR, mp/[α]D/UV-vis as appropriate
- [ ] **Purity** — EA (calcd vs found) or HPLC/GC trace
- [ ] **Stereochemistry** — chiral HPLC/GC/SFC traces (racemate + sample), dr determination
- [ ] **Copies of key spectra** — ¹H and ¹³C (and diagnostic 2D/heteronuclear) for each new compound, legible, labeled with compound number

### Crystallography

- [ ] **CIF deposited with CCDC**; CCDC number cited in SI and text
- [ ] Crystal data and refinement table; **checkCIF/PLATON** report addressed
- [ ] Note disorder/restraints and how handled

### Catalysis / mechanism support

- [ ] Control-experiment procedures and results
- [ ] Kinetics data, rate laws, KIE, labeling experiments with raw traces
- [ ] Computational details + optimized coordinates (xyz) and energies, if used

### Data and code

- [ ] Data availability statement consistent with main text
- [ ] Raw-data location (FIDs, chromatograms, diffraction frames) if archived/deposited
- [ ] Computational input/output or scripts where appropriate

## Main text vs SI

| Goes in main text | Goes in SI |
|-------------------|-----------|
| The headline result, key scheme/figure | Full step-by-step procedures |
| Representative scope / mechanism figure | Complete characterization data per compound |
| One or two diagnostic spectra (if essential) | Copies of all spectra |
| Crystal-structure figure + CCDC # | Full crystal/refinement tables, checkCIF |

## Checklist

- [ ] Every new compound has a procedure + characterization + spectra copies
- [ ] Every compound number in the SI matches the main text
- [ ] All CIFs deposited; CCDC numbers present and correct
- [ ] checkCIF alerts resolved or justified in the SI
- [ ] Chiral/purity traces included for stereochemical/purity claims
- [ ] Computational coordinates and details included if computation is used
- [ ] SI is paginated, with a table of contents, and self-consistent with the text

## Anti-patterns

- "Characterization data available on request" — must be in the SI
- Spectra copies missing or illegible for some compounds
- CIF not deposited; CCDC number a placeholder
- SI compound numbering diverging from the main text
- Procedures missing scale/equivalents so yields can't be reproduced
- Computational claims with no coordinates


## Operating pass for Journal of the American Chemical Society

Treat this skill as an executable review pass, not a prose hint. First lock the chemical novelty, characterization chain, controls, and scope or mechanism evidence; then judge whether the current manuscript answers the venue's real reader: chemistry reviewers who expect a molecule/material/reaction claim to be supported by rigorous characterization and mechanistic insight.

- **Do the pass:** Return a claim-evidence-risk ledger rather than a prose-only diagnosis; every recommendation must point to a manuscript location or missing artifact.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against ACS Central Science for broad conceptual reach, Angewandte for communication style, specialized ACS journals for narrower chemistry; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Compounds in SI】N; procedures complete [ ] / missing [...]
【Spectra copies】complete? Y/N — missing: [...]
【Purity/chiral traces】present? Y/N
【CCDC #】[...]; checkCIF addressed? Y/N
【Computation】coords + details included? Y/N / NA
【SI ↔ text consistency】Y/N
【Next】jacs-writing-style → jacs-submission
```

## Related resources

- [`../jacs-submission/templates/checklist.md`](../jacs-submission/templates/checklist.md) — pre-submission self-check
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — CCDC deposition, checkCIF/PLATON, NMR/computation tools
