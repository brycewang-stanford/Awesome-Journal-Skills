---
name: phg-tables-figures
description: Use when designing the conceptual exhibits of a Progress in Human Geography (PiHG) review essay — typologies, framework diagrams, concept genealogies, and synthesis tables that do argumentative work. For a review journal these are conceptual, not data graphics. Designs exhibits; it does not build the argument itself.
---

# Conceptual Exhibits (phg-tables-figures)

PiHG is a **review and theory** journal, so its figures and tables are **conceptual, not empirical**. You
are not plotting results (there are none); you are giving the reader a **map of the argument** — a
typology that organizes a field, a framework diagram that shows how your concept links literatures, a
genealogy that periodizes a concept, or a synthesis table that adjudicates camps. A good exhibit **does
synthetic work**; a decorative one wastes a scarce slot in a short essay.

## When to trigger

- Deciding whether an exhibit earns its place in an ~8,000-word essay
- Turning a complex synthesis into a single legible figure or table
- A reviewer said a section is "hard to follow" or "the framework is unclear"
- Building the one diagram readers will screenshot and reuse

## Exhibit types that do work in a review

| Exhibit | What it does | Use when |
|---------|--------------|----------|
| **Typology / matrix** | Organizes a field along 2 dimensions (approach × dimension) | Camps differ on more than one axis |
| **Framework diagram** | Shows how your concept links literatures/relations | The argument is relational and hard to hold in prose |
| **Concept genealogy / timeline** | Periodizes how a concept changed | The essay narrates a conceptual history |
| **Synthesis / comparison table** | Adjudicates camps on shared criteria | Readers need the camps side by side |
| **Agenda table** | Lays out the forward questions by sub-field | The contribution is a program (`phg-contribution-framing`) |

If an exhibit only *lists* what the prose already says, cut it. Every exhibit should let the reader
**see a relationship** faster than the text can tell it.

## Design for synthesis, not decoration

- **The exhibit carries an argument**, not ornament — a reader should grasp your re-ordering from the
  figure alone. Give it a claim-bearing caption ("A relational typology of platform labor," not "Overview").
- **Two dimensions, not ten.** A typology with too many axes is a spreadsheet; pick the two that matter.
- **Name the cells' logic.** A 2×2 must have a reason each quadrant exists, and ideally an under-populated
  cell that reveals a silence (`phg-critical-intervention`).
- **No data dressed as concept.** Do not import bibliometric counts or a VOSviewer map as if it were the
  argument; if you show one, it is evidence of the field's shape, clearly labeled as such.

## Craft and accessibility

- **Legible in grayscale** and colorblind-safe; PiHG figures are often read in print/PDF.
- **Vector formats** (PDF/EPS/SVG) for diagrams and tables-as-figures; avoid low-resolution raster.
- **Self-contained**: readable without the surrounding paragraph; define any coined term in the caption.
- **Count toward the essay's economy** — a review is short; one or two strong exhibits beat five weak ones.

## The "reuse test"

The best PiHG exhibit is the **typology or framework other scholars cite and redraw**. Ask: would a
reader teaching this field put your figure on a slide? If it only restates your prose, it will not travel —
and it is not earning its slot.

## Checklist

- [ ] Each exhibit does synthetic work the prose cannot do as fast
- [ ] Claim-bearing caption; readable without the surrounding text
- [ ] Typologies use the two axes that matter; cell logic is explicit
- [ ] Any empirical/bibliometric graphic is labeled as field-evidence, not the argument
- [ ] Grayscale-legible, colorblind-safe, vector format
- [ ] Exhibit count is disciplined for a short review

## Anti-patterns

- A figure that only restates the prose (decoration in a scarce slot)
- Over-dimensioned typologies that read as spreadsheets
- Importing a data/bibliometric chart and passing it off as the conceptual contribution
- Captions that label ("Framework") instead of claiming ("A relational framework linking control and precarity")
- Low-resolution or color-only figures that fail in grayscale/print

## Output format

```
【Exhibit】typology / framework diagram / genealogy / synthesis table / agenda table
【Work it does】the relationship it lets the reader see
【Caption claim】the one-line argument the exhibit makes
【Reuse test】would a teacher put it on a slide? [Y/N]
【Accessibility】grayscale + colorblind-safe + vector? [Y/N]
【Next】phg-writing-style
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — diagramming and bibliometric-mapping tools (draw.io, VOSviewer, biblioshiny)
- [`../../resources/worked-examples/01-introduction.md`](../../resources/worked-examples/01-introduction.md) — the "circuit" concept as a candidate framework diagram
