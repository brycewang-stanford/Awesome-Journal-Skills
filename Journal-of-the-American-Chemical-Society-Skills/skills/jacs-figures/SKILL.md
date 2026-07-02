---
name: jacs-figures
description: Use when building schemes, spectra, structures, and reaction/mechanism figures in ACS style for a Journal of the American Chemical Society (JACS) manuscript. Designs and audits graphics — it does not generate the underlying data.
---

# Schemes, Structures, and Figures (ACS Style) (jacs-figures)

## When to trigger

- Reaction schemes, mechanism cycles, or structure drawings need building
- Spectra/plots are cluttered, mislabeled, or unreadable
- Figures don't follow ACS conventions (fonts, bond lengths, panel labels)
- The TOC/abstract graphic needs designing

## Figure types and what each must do

| Figure type | Must convey | Common tool |
|-------------|-------------|-------------|
| Reaction scheme | Substrate → product, conditions, yield/ee under the arrow | ChemDraw |
| Scope figure | Generality at a glance; products with yields/ee; failures noted | ChemDraw |
| Mechanism / catalytic cycle | Stoichiometry-balanced steps; oxidation states; key intermediates | ChemDraw |
| Spectra (NMR/IR/UV-vis) | Axes, units, assignments of diagnostic peaks | MestReNova / Origin |
| Crystal structure (ORTEP) | Thermal ellipsoids (with % probability), labeled key atoms, H omitted as stated | Mercury / OLEX2 |
| Property/kinetics plot | Variables, units, error bars, fit + equation | Origin / Matplotlib |
| TOC graphic | The central advance in one glance | ChemDraw + Illustrator |

## ACS drawing conventions (ChemDraw)

- Use ACS document settings (consistent bond length, line width, atom-label font).
- Stereochemistry: explicit wedges/hashes; consistent depiction across all schemes.
- Conditions sit **over the arrow** (reagents) and **under** (solvent, T, time); yields by the product.
- Number compounds in **bold** consistently; the same number means the same structure everywhere.
- Charges, lone pairs, and formal oxidation states shown where mechanistically relevant.

## Spectra and data plots

- Label axes with quantity and unit (δ / ppm; wavenumber / cm⁻¹; m/z; nm).
- Annotate the diagnostic peaks that support the claim; don't dump raw, unlabeled traces in the main text (full spectra go to SI).
- Crystal-structure figures: state ellipsoid probability (e.g., 50%), which H atoms are omitted, and symmetry-generated atoms.
- Plots: include error bars / replicate info and the fitted model; state n.

## TOC graphic craft (the most-seen image of the paper)

The abstract graphic is the paper's storefront — it appears in the issue TOC,
alerts, and search results at thumbnail size. Design for that scale:

- **One idea only.** The single transformation, concept, or property — not a
  collage of every scheme. If the advance is selectivity, show the two possible
  products and mark which one forms.
- **Structures over prose.** A substrate→product pair with one annotated arrow
  beats any sentence; keep text to a few words (e.g., "24 examples, up to 97% ee").
- **Legible at thumbnail.** Bond lines and labels must survive reduction; test
  by zooming the export to ~25%.
- **Match the abstract's claim.** Editors compare the two; a graphic promising
  more than the text is a credibility leak.
- Follow the current ACS size/aspect specification for abstract graphics — check
  the author page rather than reusing an old template.

## Caption discipline (worked micro-edit)

- Before: *"Figure 2. NMR spectra of the reaction."*
- After: *"Figure 2. ¹H NMR spectra (400 MHz, CD₂Cl₂, 25 °C) of the reaction of
  **1** with **2a**: (a) t = 0; (b) t = 30 min, showing the hydride resonance of
  intermediate **3** at δ −8.4 (d, J = 12 Hz)."*

A JACS caption names the technique, conditions, and the diagnostic feature the
reader should find — it argues the claim, it does not merely label the image.

## Scope-figure craft

- Group products by substrate class with a one-line class header; readers scan
  for their own chemistry.
- Print yield and ee/er under every structure; mark limitations honestly
  (footnote lower-yielding or failed cases rather than deleting them).
- Highlight the hardest examples (drug-like, sterically encumbered, previously
  unreactive) — these carry the generality argument, so give them visual room.

## Composition and accessibility

- One consistent color palette; ensure meaning survives grayscale and color-vision deficiency (don't rely on red/green alone).
- Panel labels (a, b, c) match the caption order; captions are self-contained (a reader gets the point without the text).
- Export vector where possible; raster at the resolution ACS specifies per figure type.
- Keep figure count disciplined; merge related panels rather than proliferating figures.

## Checklist

- [ ] Every compound number in figures matches the text and SI
- [ ] Scheme conditions (reagents/solvent/T/time) and yields present
- [ ] Mechanism steps are mass- and charge-balanced
- [ ] ORTEP states ellipsoid % and omitted atoms
- [ ] Spectra/plots have labeled axes, units, and annotated diagnostic peaks
- [ ] Color works in grayscale and for color-blind readers
- [ ] TOC graphic encodes the advance and meets ACS size rules

## Anti-patterns

- Inconsistent compound numbering between scheme, text, and SI
- Catalytic cycle that is not balanced or omits the oxidant/reductant
- Spectra pasted as low-res screenshots with no axis labels
- ORTEP without ellipsoid probability or H-atom statement
- Decorative TOC graphic that doesn't show the chemistry
- Rainbow plots unreadable in grayscale

## Output format

```
【Figures】list with purpose of each
【Numbering consistent?】Y/N
【Schemes】conditions + yields present? Y/N
【Mechanism balanced?】Y/N
【ORTEP】ellipsoid % + omitted atoms stated? Y/N
【Accessibility】grayscale/colorblind safe? Y/N
【TOC graphic】encodes advance? Y/N
【Next】jacs-supplementary (full spectra) → jacs-writing-style
```

## Related resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — ChemDraw, Mercury/ORTEP, plotting and figure-assembly tools
