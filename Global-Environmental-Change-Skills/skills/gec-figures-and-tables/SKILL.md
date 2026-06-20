---
name: gec-figures-and-tables
description: Use when designing the figures, tables, framework diagrams, and maps for a Global Environmental Change (GEC) manuscript, plus the required Highlights. GEC reaches an interdisciplinary, policy-relevant audience, so exhibits must be self-contained and legible across disciplines. Improves exhibits; it does not fabricate data.
---

# Figures & Tables (gec-figures-and-tables)

GEC exhibits are read by people from many disciplines and by policy-oriented readers. An exhibit must
stand on its own, communicate the human-dimensions point quickly, and survive print and grayscale. This
skill also covers the journal's **Highlights** requirement.

## When to trigger

- Designing main and supplementary figures, tables, framework diagrams, or maps
- A reviewer found an exhibit "hard to read," "overloaded," or "disconnected from the argument"
- Writing the **Highlights** (3-5 bullets) at submission
- Deciding what belongs in the main text vs. supplementary material

## Principles for GEC exhibits

1. **Self-contained.** Title, axes, units, sample, and source are legible without the text. A reader
   from another field should grasp the point from the exhibit and caption alone.
2. **Show the human/policy point.** Foreground the social driver, consequence, distribution, or
   governance outcome — not just a biophysical trend.
3. **Framework diagrams earn their place.** A clear conceptual / systems diagram often carries the
   contribution; keep it uncluttered and consistent with the text's terms.
4. **Maps and scale.** When mapping spatial variation, state the unit and scale; use classed,
   colorblind-safe schemes; avoid implying precision the data lack.
5. **Accessible.** Colorblind-safe palettes, legible in grayscale, vector output (PDF/EPS) for print;
   no information conveyed by color alone.

## Highlights (Elsevier requirement)

- **3-5 bullet points**, each **<=85 characters including spaces**, submitted as a **separate editable
  file** with "highlights" in the file name.
- Capture the **novel results and contribution** in plain language — they are a shop window for an
  interdisciplinary, policy audience.

## Tables

- Report effect sizes and intervals, not stars alone; label units and samples.
- Keep main-text tables focused; move full specifications and diagnostics to supplementary material.
- Ensure every table/figure number matches the analysis workflow (the archive must reproduce them).

## Anti-patterns

- A chart that needs three paragraphs of text to interpret
- Color-only encoding; rainbow scales; unreadable in grayscale
- A framework diagram that contradicts the terms used in the text
- Maps with no scale/unit, or implying spurious precision
- Highlights that restate the title instead of the contribution

## Exhibit-review patterns at GEC and the fix

GEC exhibits face a reader who may not share your discipline, so the editor and referees test whether the human-dimensions point survives translation. These are the recurring objections.

| What a referee flags | Underlying problem | The GEC fix |
|----------------------|--------------------|-------------|
| "I cannot read this exhibit without the text" | Not self-contained | Put sample, unit, scale, and the social variable in the caption; make the point legible standalone |
| "The figure shows a biophysical trend, not the human story" | Foregrounds the wrong half | Plot the social driver, distribution, or governance outcome; relegate the raw biophysical series if needed |
| "The map implies precision the data lack" | Continuous shading on coarse units | Class the scheme, state the spatial unit, and use a colorblind-safe palette |
| "Highlights just restate the title" | Shop-window wasted | Each bullet carries a distinct novel result in plain language |
| "The framework diagram contradicts the text" | Terms drifted | Make every box and arrow use the manuscript's defined concepts |

## Worked micro-example (illustrative — coastal vulnerability map)

A coastal-adaptation paper proposes a single choropleth of "vulnerability" across districts.

- **Weak exhibit:** a smooth rainbow gradient over district outlines, no unit stated, vulnerability undefined in the legend, readable only in colour.
- **GEC-strong exhibit:** five classed quantiles on a colorblind-safe sequential ramp, the legend naming the index components (exposure, sensitivity, adaptive capacity), the district as the stated unit, and a caption noting that the top quantile holds 28% of population but 11% of adaptation spending (illustrative). A paired small-multiple shows the same pattern in grayscale.
- **Payoff:** the inequity — the human-dimensions point — is visible from the exhibit and caption alone, and survives print.

## Calibration anchors (hedged)

- **Self-containment bar:** a non-specialist editor should grasp the contribution from the exhibit plus caption; if they cannot, it is not yet a GEC exhibit.
- **Accessibility bar:** colorblind-safe, grayscale-legible, vector output is the expectation, not a courtesy.
- Re-check figure-format rules on the journal's live author guidelines before filing, as Elsevier
  updates them.

## Output format

```
【Exhibit】figure / table / framework diagram / map
【Point】the one human-dimensions takeaway it must convey
【Self-contained】readable from caption alone? [Y/N]
【Accessible】colorblind-safe + grayscale-legible + vector? [Y/N]
【Highlights】3-5 bullets, <=85 chars each, drafted? [Y/N]
【Next】gec-writing-style
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — plotting, diagramming, and mapping tools
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — Highlights and formatting requirements
