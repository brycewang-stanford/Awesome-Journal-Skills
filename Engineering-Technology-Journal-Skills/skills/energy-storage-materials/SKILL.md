---
name: energy-storage-materials
description: Use when targeting Energy Storage Materials or deciding whether an electrochemical-energy-storage materials manuscript fits this venue. Encodes the journal's fit, the materials-structure-property-mechanism bar, characterization rigor, house style, the materials-vs-device routing, official-submission re-check, and desk-reject heuristics.
---

# Energy Storage Materials (energy-storage-materials)

## Journal positioning

Energy Storage Materials (Elsevier) is an archival venue for **materials for
electrochemical energy storage**: electrode and electrolyte materials and their
**structure–property–performance relationships and mechanisms** for batteries and
supercapacitors. Its center of gravity is the **material and the mechanism** — why a
composition, structure, or interface stores charge the way it does — established with
materials-level evidence and connected to electrochemical behavior. Where Journal of
Power Sources rewards an advance read in the cell, this journal rewards a materials
insight: a new storage mechanism, a structure–property law, or a mechanistic
explanation of capacity, kinetics, or stability. A device-engineering paper with no
new materials understanding, or a synthesis paper with a property number and no
mechanism, is a weak fit. This skill is a **fit / venue-selection / re-framing** tool.
It does not replace the journal's current official author guidelines. Before
submitting, re-check the live Energy Storage Materials Guide for Authors on the
Elsevier site.

## When to trigger

- The author names Energy Storage Materials for an electrode/electrolyte-materials
  manuscript centered on structure–property–performance or storage mechanism.
- A paper must be re-framed from "we synthesized a material and measured capacity" into
  a structure–property–mechanism story for charge storage.
- The author is deciding between this materials-mechanism venue and the device venue
  `journal-of-power-sources`, or a structural-materials venue.
- The author needs the journal's materials-characterization and mechanism rigor bar and
  desk-reject heuristics.

## Scope & topic fit

- Electrode materials: cathodes, anodes, and conversion/alloying/intercalation hosts,
  with structure–property–performance relationships and storage mechanisms.
- Electrolytes and interfaces: liquid, solid-state, and quasi-solid electrolytes, SEI/CEI
  formation, and ion-transport and interfacial mechanisms.
- Beyond-lithium and emerging chemistries (Na, K, multivalent, metal-anode, etc.) where
  the materials-level mechanism is the advance.
- Materials for supercapacitors and hybrid storage where charge-storage mechanism and
  structure–property links are central.
- Operando/in-situ and advanced characterization, and materials modeling, when they
  resolve a storage mechanism or structure–property law.
- Design principles and structure–property relationships transferable across a
  materials class, not a single composition.

## Method & evidence bar

- The central claim is a **structure–property–mechanism** result: the materials origin
  of capacity, rate, or stability, supported by direct evidence (operando/in-situ,
  spectroscopy, diffraction, microscopy), not inferred from a capacity curve alone.
- Electrochemical data must be reported with loading, current density, voltage window,
  and electrolyte, and connected to the materials mechanism; honest half-cell/full-cell
  context is required.
- Mechanism must be ruled in by controlled materials variation and characterization, not
  asserted from morphology–performance correlation.
- Performance claims must be benchmarked against the correct materials baseline under
  comparable conditions; trivial-loading or cherry-picked-cycle results are weak.
- Characterization must be statistically representative with sampling reported, and
  computation (DFT/MD) must be tied to or predictive of experiment.

## Structure & house style

- Standard research-article structure (introduction, experimental, results,
  discussion); the journal uses highlights and a graphical abstract — re-check current
  article types and requirements on the live guide.
- The introduction frames the materials/mechanism gap (not the device target); the
  discussion makes the structure–property–mechanism argument explicit and transferable.
- Figures are load-bearing: structure/characterization paired with electrochemistry,
  operando/in-situ evidence, and mechanism schematics grounded in data.
- Supporting information carries full synthesis, extended characterization, and
  computational details; main-text figures must support the mechanism on their own.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and
  `../../resources/official-source-map.md`; start from the Elsevier anchors, then cite
  the current Energy Storage Materials Guide for Authors page you checked.
- Search the live site for "Energy Storage Materials guide for authors" and follow the
  current Elsevier/Editorial Manager version.
- Re-check article types, highlights and graphical-abstract requirements, and
  electrochemical/characterization reporting conventions.
- Confirm data-availability and any deposition requirements for crystallographic or
  computational data.
- Re-check competing-interests, funding, author-contribution (CRediT), and AI-use
  disclosure requirements.
- If the live official instructions conflict with this skill, the official
  instructions win.

## Pre-submission self-check

- [ ] The contribution is a structure–property–mechanism insight, not a synthesis-plus-capacity report.
- [ ] Mechanism is supported by operando/in-situ or controlled-variation evidence, not morphology–performance correlation.
- [ ] Electrochemical data include loading, current density, window, and electrolyte, tied to the materials mechanism.
- [ ] Performance is benchmarked against the correct materials baseline under comparable conditions.
- [ ] Characterization is statistically representative with sampling reported; any computation is tied to experiment.
- [ ] The mechanism/design principle is framed to transfer across a materials class.

## Common desk-reject triggers

- Synthesis-plus-capacity paper with a property number and no storage mechanism.
- Mechanism asserted from morphology–performance correlation with no operando/in-situ or controlled-variation evidence.
- Capacity/rate claims at trivial loadings, cherry-picked cycles, or undisclosed conditions.
- Incremental composition variant with marginal improvement and no transferable insight.
- Device-engineering paper with no new materials understanding (better suited to a device venue).
- Computation-only study with no experimental anchor or tested prediction.

## Re-routing decision

- Cell/electrode/electrolyte engineering and diagnostics read in device metrics → `journal-of-power-sources`.
- Systems-level energy integration / techno-economic scope → `applied-energy`.
- Solid electrolyte/membrane transport as the central separation science → `journal-of-membrane-science`.
- Structural-materials physical-metallurgy mechanism (non-storage) → `acta-materialia`.
- Highest-profile energy-materials breakthrough → `nature-energy`, `joule`, or `nature-catalysis` (different selectivity/format; re-check).

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Energy Storage Materials
[Topic tags] <2–3 closest materials subtopics (electrode/electrolyte/interface)>
[Mechanism] <the structure–property–mechanism claim for charge storage in one line>
[Evidence] <operando/in-situ + controlled-variation support present?>
[Performance] <materials-baseline benchmark + conditions stated?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / highlights / characterization-reporting / data deposition / disclosures>
[Re-route suggestion] <if device/system-level, a better-matched venue>
```
