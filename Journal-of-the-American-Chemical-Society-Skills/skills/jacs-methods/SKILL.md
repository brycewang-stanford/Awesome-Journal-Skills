---
name: jacs-methods
description: Use when checking synthesis and characterization rigor for a Journal of the American Chemical Society (JACS) manuscript — purity, NMR/HRMS/IR/UV-vis, elemental analysis or HPLC, single-crystal X-ray/CCDC, and catalysis controls/mechanism/kinetics. Audits experimental rigor — it does not write narrative or polish prose.
---

# Synthesis and Characterization Rigor (jacs-methods)

## When to trigger

- New compounds are reported and you must confirm full characterization
- A reviewer could ask "is this compound pure?" or "where is the X-ray?"
- A mechanism is claimed but only proposed, not tested
- Catalysis scope/selectivity is reported and controls are unclear

## Characterization rigor by claim type

JACS requires that **claims are fully supported by characterization data and
appropriate controls**. Match the data package to what you assert.

### Every new, isolable compound

- [ ] **¹H NMR** — solvent, field; δ (ppm), multiplicity, J (Hz), integration
- [ ] **¹³C{¹H} NMR** — all resolvable carbons (note coincident peaks)
- [ ] Heteronuclear NMR as relevant: **¹⁹F**, **³¹P**, **¹¹B**, etc.; 2D for assignment
- [ ] **HRMS** — ionization mode, calcd vs found m/z for the assigned formula
- [ ] **IR** — diagnostic bands (C=O, N–H, C≡N, M–CO, etc.) when structurally informative
- [ ] **Purity evidence** — at least one of: CHN(S) elemental analysis (calcd vs found, typically within accepted tolerance), or HPLC/GC purity, plus clean NMR
- [ ] Melting point / optical rotation / UV-vis as appropriate to compound class

### Stereochemistry / chirality

- [ ] **ee** by chiral HPLC/GC/SFC (column, eluent, flow, detector; report racemate trace)
- [ ] **dr** by NMR or HPLC; specify how measured
- [ ] Absolute configuration assigned (X-ray, VCD, comparison to known, or derivatization) — state the method

### Solid-state structure

- [ ] **Single-crystal X-ray** for structurally pivotal claims; deposit CIF with **CCDC** and cite the number
- [ ] Crystal/refinement table (formula, space group, R1/wR2, GooF, completeness)
- [ ] **checkCIF/PLATON** run; A/B-level alerts resolved or justified
- [ ] PXRD for bulk-phase identity of solids/materials

### Catalysis

- [ ] **Scope table** — representative, honest substrate range (not only easy cases); note failures
- [ ] **Control experiments** — no-catalyst, no-ligand, no-additive, radical traps/clocks as relevant
- [ ] **Mechanism** — evidence-based: kinetics (orders, rate law), KIE, labeling, intermediates (isolation/spectroscopy), Hammett, ee–ee(cat) correlation
- [ ] Catalyst loading, TON/TOF, and reproducibility (replicate runs) reported
- [ ] Metal/ligand source, purity, and any trace-metal control where relevant

### Materials / physical

- [ ] Composition and phase: PXRD, EDX/XPS, ICP, TGA, BET as appropriate
- [ ] Morphology with **scale bars** and representative-vs-statistical imaging (SEM/TEM/AFM)
- [ ] Property measurement with method, conditions, and error/replication
- [ ] Spectroscopy (UV-vis/PL/Raman/EPR/electrochemistry) tied to the claimed property

### Computation (if used to support mechanism/structure)

- [ ] Functional, basis set/pseudopotentials, solvation model, software + version
- [ ] Stationary points characterized (frequencies; TS has one imaginary mode)
- [ ] Optimized coordinates (xyz) deposited in SI; energies referenced consistently

## The SI data string (write it once, correctly)

Every isolated compound gets a characterization block in the SI in the standard
ACS order. A well-formed entry looks like:

```
(2R)-2-Fluoro-4-phenylbutan-1-ol (3a). Colorless oil, 158 mg (94%). [α]D²⁵ = +12.4
(c 1.0, CHCl₃). ¹H NMR (400 MHz, CDCl₃): δ 7.31–7.18 (m, 5H), 4.52 (dddd, J = 48.9,
8.1, 4.3, 3.9 Hz, 1H), ... ¹³C{¹H} NMR (101 MHz, CDCl₃): δ 141.6, 128.5 (d,
JCF = 5.2 Hz), ... ¹⁹F NMR (376 MHz, CDCl₃): δ −186.3. HRMS (ESI+) m/z: [M + Na]⁺
calcd for C₁₀H₁₃FONa 191.0843; found 191.0841. 97:3 er (Chiralpak IA, 95:5
hexanes/iPrOH, 1.0 mL/min, 210 nm; tR major 14.2 min, minor 16.8 min).
```

Audit each block for: mass **and** percentage yield, physical state, every
nucleus relevant to the structure, coupling constants on diagnostic multiplets,
calcd/found within instrument tolerance, and the full chiral method — not just
the er value.

## Referee rigor probes (pre-empt them)

- "Compound **x** shows a peak at δ 1.56 — water or impurity?" → annotate
  residual-solvent peaks in the SI spectra copies before a referee circles them.
- "Yields are single runs?" → state replicate counts for headline entries; give
  an average with the spread for the model reaction.
- "Could adventitious metal catalyze this?" → for base-metal or 'metal-free'
  claims, report reagent lot ICP data or a deliberate trace-metal spike control.
- "The cycle shows Ni(I)/Ni(III) — where is the evidence?" → every oxidation
  state drawn in a mechanism figure must trace to an EPR/UV-vis/electrochemical
  or kinetic observation, or be labeled as proposed.

## Reproducibility test

Could an independent chemist reproduce each yield, ee, and spectrum from the
written procedure alone? If not, the procedure is incomplete — fix before figures.
The strongest SI procedures also state how the compound was purified (column
eluent, distillation T/p), on what scale the reaction was validated, and any
setup detail on which the outcome hinges (drying of solvent, exclusion of light,
stirring rate for biphasic mixtures).

## Anti-patterns

- New compound reported with no purity criterion (no EA, no HPLC, no clean ¹³C)
- "Pure by NMR" as the only purity statement for a key compound
- Mechanism drawn as a cycle with no kinetic/labeling/control support
- Crystal structure shown but CIF not deposited / no CCDC number
- Scope table that hides failed substrates; idealized yields not reproducible
- HRMS reported without ionization mode or calcd/found pair

## Output format

```
【Compounds】N new; full characterization complete for [ ] / missing for [...]
【Purity basis】EA / HPLC / clean NMR — per compound
【Stereochem】ee/dr method + absolute config method (if chiral)
【X-ray】CCDC # [...]; checkCIF clean? Y/N
【Mechanism】claimed = [...]; evidence = [kinetics/KIE/labeling/controls]
【Reproducible from text?】Y/N — gaps: [...]
【Next】jacs-figures → jacs-supplementary
```

## Related resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — instruments, CCDC/PDB deposition, crystallography and computational software
