---
name: ngeo-figures
description: Use when designing or auditing display items for a Nature Geoscience manuscript, where 4-6 figures/tables must carry the Earth-system advance and its uncertainty for a broad readership. Designs figure strategy; does not run the analysis or write prose.
---

# Nature Geoscience Figures (ngeo-figures)

## When to trigger

- You have many candidate maps, sections, and time series and must choose 4–6
- Your lead figure does not convey the Earth-system advance at a glance
- Panels are dense, captions are long, or map/section elements are unreadable at column width
- You are over the display-item ceiling and must merge or relocate
- A coauthor wants to "add one more panel just in case"

## Display-item budget for an Article

A Nature Geoscience Article carries **4–6 display items** (figures and/or tables combined; verify). Every one must earn its place and be legible to a non-specialist. The hierarchy:

- **Lead figure (Fig. 1)** — conveys the headline advance at a glance. A reader skimming should grasp the result, and ideally its uncertainty, from this figure plus its caption alone. Often a map or cross-section that situates the study *and* shows the key signal.
- **Supporting figures** — each makes exactly one additional point (a mechanism, a dependence, a data–model comparison, a time series with error envelope).
- **Everything else** — extended maps, all model members, secondary proxies, raw traces → Supplementary Information (Fig. Sn).

If a display item does not advance the single headline result or one essential support, move it to SI.

## Earth-science lead-figure rules

| Principle                        | Practice                                                          |
|----------------------------------|-------------------------------------------------------------------|
| One glance, one message          | The eye lands on the advance immediately                          |
| Show the uncertainty             | Error bars, shaded confidence envelopes, or stippling for significance |
| Locate the reader                | An inset locator map / schematic orients out-of-subfield readers  |
| Data and model together          | Overlay the decisive comparison, not in separate figures          |
| Honest cartography               | State projection, scale, and data source; avoid misleading color scales |
| Annotate the key feature         | Arrow / label on the anomaly, front, transition, or trend that matters |

## Production standards

- Design for the Nature column grid; check legibility at final printed size.
- Use **perceptually-uniform, color-blind-safe** colormaps (e.g. viridis, cividis, batlow); never rainbow/jet for quantitative fields, and never encode by color alone.
- For maps: label projection and scale; show the color-bar with units; mark significance (stippling/hatching) rather than hiding it.
- Vector formats for line art and schematics; high-resolution raster for satellite imagery and gridded fields.
- Define every symbol, unit, and abbreviation in the caption; match notation to the main text and Methods.
- Tables: reserve for values that cannot be shown graphically; they count against the display-item budget.

## Panel discipline

- Prefer fewer panels with a clear reading order; label (a), (b), (c).
- A dense multi-panel map grid usually signals that supporting panels belong in SI.
- Insets (locator map, zoom, schematic of the mechanism) are powerful but must stay legible.

## Checklist

- [ ] Total display items are within the 4–6 ceiling and each is essential
- [ ] Fig. 1 conveys the Earth-system advance at a glance
- [ ] Uncertainty / significance is shown, not hidden
- [ ] Every figure makes exactly one point
- [ ] Maps state projection, scale, units, and data source
- [ ] Color-blind-safe, perceptually-uniform colormaps; no rainbow/jet; not color-only
- [ ] Decisive data–model comparison shown directly
- [ ] Captions define all symbols/units and are as short as clarity allows
- [ ] Non-essential panels/datasets moved to SI

## Anti-patterns

- A lead figure too dense to parse without the main text
- Multi-panel map grids that bury the headline
- Rainbow/jet colormaps or color-only encoding that fails in grayscale or for color-blind readers
- Maps with no scale, projection, or units
- Hiding uncertainty by plotting only best-estimate fields
- Decorative figures that do not advance the headline result
- Long captions that quietly consume space

## Output format

```
【Display-item count】N (≤6) — each essential?  yes / cut list
【Fig. 1 conveys the advance at a glance】yes / redesign
【Uncertainty shown】yes / fix
【Per-figure single point】list
【Cartography: projection/scale/units】complete / fix
【Colormap: perceptual + color-blind-safe】yes / fix
【Moved to SI】list
【Next】ngeo-supplementary (SI) or ngeo-length-management (fit limit)
```

> Display-item counts, figure specs, and colormap guidance are durable in spirit but specific in detail — verify current Nature Geoscience figure rules on the official author pages (Checked: 2026-07-16).
