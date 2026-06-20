---
name: journal-of-membrane-science
description: Use when targeting Journal of Membrane Science or deciding whether a membranes / membrane-process manuscript fits this venue. Encodes the journal's fit, the transport-and-separation-mechanism bar, membrane characterization rigor, house style, the mechanism-vs-application routing, official-submission re-check, and desk-reject heuristics.
---

# Journal of Membrane Science (journal-of-membrane-science)

## Journal positioning

Journal of Membrane Science (Elsevier) is the leading archival venue for **membranes
and membrane processes**: membrane materials and formation, the mechanisms of
transport and separation, separation performance, fouling, and applications in water,
gas, energy, and bio. Its defining expectation is that the **membrane and its
transport/separation mechanism are central** — a paper must explain how the membrane
structure governs permeation and selectivity, not merely report that a new membrane
separated something. Studies that use a commercial membrane as a black box to treat a
feed, or that report a permeance number without structure–transport understanding, are
a weak fit. This skill is a **fit / venue-selection / re-framing** tool. It does not
replace the journal's current official author guidelines. Before submitting, re-check
the live Journal of Membrane Science Guide for Authors on the Elsevier site.

## When to trigger

- The author names Journal of Membrane Science for a membrane-material, transport,
  separation, or fouling manuscript and wants a fit/framing check.
- A paper must be re-framed from "we used a membrane to separate X" into a
  structure–transport–separation mechanism story.
- The author is deciding between this journal and an applied process venue
  (`chemical-engineering-journal`) or a fundamentals venue (`aiche-journal`).
- The author needs the journal's transport-mechanism and characterization rigor bar
  and desk-reject heuristics.

## Scope & topic fit

- Membrane materials and formation: polymeric, inorganic, mixed-matrix, and composite
  membranes; phase inversion, interfacial polymerization, and fabrication
  structure–property control.
- Transport mechanisms: solution–diffusion, pore-flow, facilitated and ion transport;
  the link between membrane structure/chemistry and permeability and selectivity.
- Separation performance and process: reverse osmosis, nanofiltration, ultrafiltration,
  gas separation, pervaporation, membrane distillation, electrodialysis.
- Fouling, wetting, aging, and long-term stability with mechanistic analysis and
  mitigation strategies.
- Membranes for energy and bio applications (fuel-cell/electrolyzer/redox-flow
  membranes, bioseparations) when the membrane transport science is central.

## Method & evidence bar

- The central claim is a **transport/separation mechanism**: how membrane structure and
  chemistry set permeability, selectivity, or fouling resistance — supported by data,
  not asserted.
- Permeation and selectivity must be reported with the membrane thickness/area,
  driving force, and conditions made explicit, and benchmarked against the relevant
  trade-off (e.g., permeability–selectivity) and prior membranes.
- Membrane characterization must be appropriate and quantitative: morphology
  (cross-section, surface), chemistry, porosity/free volume, and stability, with
  sampling and reproducibility reported.
- Fouling/stability claims require realistic feeds and durations, with the fouling
  mechanism analyzed rather than only a flux-decline curve shown.
- Performance must be compared to the correct membrane baseline under equivalent
  conditions; normalized, reproducible metrics are expected.

## Structure & house style

- Standard research-article structure (introduction, materials/methods, results,
  discussion); the journal uses highlights and a graphical abstract — re-check current
  article types and requirements on the live guide.
- The introduction frames the membrane/transport gap and the separation challenge; the
  discussion makes the structure–transport–performance argument explicit.
- Figures are load-bearing: cross-section morphology, permeation/selectivity plots
  against the relevant trade-off line, and fouling/stability data with controls.
- Supporting information carries full fabrication protocols, extended characterization,
  and long-term data; main-text figures must support the transport claim on their own.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and
  `../../resources/official-source-map.md`; start from the Elsevier anchors, then cite
  the current Journal of Membrane Science Guide for Authors page you checked.
- Search the live site for "Journal of Membrane Science guide for authors" and follow
  the current Elsevier/Editorial Manager version.
- Re-check article types, highlights and graphical-abstract requirements, and
  reporting conventions for permeation/selectivity (units, normalization).
- Confirm data-availability and any expectation to report membrane thickness, area, and
  test conditions for reproducibility.
- Re-check competing-interests, funding, author-contribution (CRediT), and AI-use
  disclosure requirements.
- If the live official instructions conflict with this skill, the official
  instructions win.

## Pre-submission self-check

- [ ] The membrane and its transport/separation mechanism are the central contribution, not a black-box separation result.
- [ ] Permeability/selectivity are reported with thickness, area, driving force, and conditions, and benchmarked against the trade-off line.
- [ ] Membrane characterization (morphology, chemistry, porosity/stability) is quantitative and reproducible.
- [ ] Fouling/stability claims use realistic feeds and durations with the mechanism analyzed.
- [ ] Performance is compared to the correct prior membrane under equivalent conditions.
- [ ] Highlights and graphical abstract represent the transport/separation advance.

## Common desk-reject triggers

- Using a commercial/black-box membrane to treat a feed with no membrane-science contribution.
- Permeance/flux numbers reported without thickness, area, conditions, or trade-off benchmarking.
- New membrane with a separation number but no structure–transport mechanism.
- Fouling shown only as a flux-decline curve, with no mechanism or realistic feed.
- Performance compared to a strawman or under non-equivalent conditions.
- Application/process paper where the membrane transport science is incidental.

## Re-routing decision

- Applied water/energy process where the process, not the membrane, is the advance → `chemical-engineering-journal`.
- Fundamental transport/thermodynamics generalizing beyond membranes → `aiche-journal`.
- Systems-level energy/desalination assessment → `applied-energy`.
- Ion-exchange membranes framed as a battery/cell device advance → `journal-of-power-sources`.
- Water-treatment work with environmental-science framing → `environmental-science-and-technology`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Journal of Membrane Science
[Topic tags] <2–3 closest membrane subtopics>
[Mechanism] <the structure–transport–separation claim in one line>
[Performance] <permeability/selectivity vs trade-off + conditions stated?>
[Stability/fouling] <realistic-feed + mechanism evidence present?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / highlights / units-normalization / data policy / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
