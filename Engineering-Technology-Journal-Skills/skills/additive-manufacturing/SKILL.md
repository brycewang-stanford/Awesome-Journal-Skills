---
name: additive-manufacturing
description: Use when targeting the journal Additive Manufacturing or deciding whether an AM-science manuscript fits this venue. Encodes the journal's fit, the process–structure–property and qualification bar, AM-specific experimental rigor, the AM-vs-metallurgy and AM-vs-subtractive routing, official-submission re-check, and desk-reject heuristics.
---

# Additive Manufacturing (additive-manufacturing)

## Journal positioning

Additive Manufacturing is a leading archival journal dedicated to the **science of
additive manufacturing**: new AM processes and process physics,
process–structure–property relationships, AM-specific materials, design-for-AM,
and in-situ monitoring and qualification. Its center of gravity is AM as a science —
understanding how the layer-wise process governs structure and performance, and how
to monitor and qualify what is built — established with experimental rigor. The
journal differs from a metallurgy-first venue (where the microstructure mechanism is
the point) and from a precision-machining venue (subtractive/precision). Papers that
print a known part on a commercial machine with no AM-specific insight, or that
report a property with no link to the process, are a weak fit. This skill is a **fit
/ venue-selection / re-framing** tool. It does not replace the journal's current
official author guidelines. Before submitting, re-check the live Additive
Manufacturing Guide for Authors.

## When to trigger

- The author names Additive Manufacturing for an AM-process, AM-materials, or
  AM-qualification manuscript and wants a fit/framing check.
- A paper must be re-framed from "we 3D-printed this part" into an AM
  process–structure–property or qualification contribution.
- The author is deciding between Additive Manufacturing, a metallurgy-first venue
  (`acta-materialia`), and a precision-machining venue
  (`international-journal-of-machine-tools-and-manufacture`).
- The author needs AM's experimental-rigor bar and desk-reject heuristics.

## Scope & topic fit

- New AM processes and process physics: powder-bed fusion, directed energy deposition,
  binder jetting, vat photopolymerization, material extrusion — with new process
  understanding or capability.
- Process–structure–property relationships: how AM parameters govern porosity,
  microstructure, anisotropy, residual stress, and mechanical/functional performance.
- AM materials: alloys, polymers, ceramics, composites, and multi-material/functionally
  graded structures designed or adapted for AM.
- Design-for-AM: lattices, topology-optimized and architected structures realized by AM,
  when the AM realizability and performance are central.
- In-situ monitoring, sensing, and process control: melt-pool/defect monitoring,
  closed-loop control, and data-driven process insight.
- Qualification, repeatability, and defect science: linking process signatures to
  defect formation and to part qualification.

## Method & evidence bar

- The central claim is an **AM-specific advance** — a process capability, a
  process–structure–property link, or a monitoring/qualification method — not a part
  printed on a stock machine.
- Process parameters must be reported completely (machine, feedstock, energy input,
  scan strategy, atmosphere) so the build is reproducible.
- Structure and property characterization must be quantitative and statistically
  representative (porosity sampling, microstructure quantification, mechanical
  statistics), not single images.
- For monitoring/control, demonstrate the signal-to-defect or signal-to-property link
  with validation, not just sensor traces.
- Benchmark against the correct baseline (conventionally made counterpart or
  state-of-the-art AM) and explain the AM mechanism behind any improvement.
- Reproducibility: feedstock characteristics, process window, post-processing, and
  testing protocol reported in enough detail to reproduce the structure and property.

## Structure & house style

- Standard full-length research-article structure; Additive Manufacturing publishes
  archival articles — re-check article types on the live guide.
- The introduction motivates the AM-science gap (process physics, structure control,
  qualification), not a generic application; the discussion makes the
  process–structure–property argument explicit.
- Figures are load-bearing: process schematics, porosity/microstructure quantification,
  in-situ signals with ground truth, and property plots with statistics.
- Notation and units follow AM/materials-engineering conventions; report energy density
  and scan parameters unambiguously.
- Supplementary material carries extended builds, full parameter sets, and monitoring
  data; the main-text figures must support the central AM insight on their own.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and
  `../../resources/official-source-map.md`; start from the Elsevier anchors, then
  cite the current Additive Manufacturing Guide for Authors page you checked.
- Search the live site for "Additive Manufacturing journal guide for authors" and
  follow the current Elsevier/Editorial Manager version.
- Re-check article types, length/figure expectations, and the data-availability policy
  for process, monitoring, and characterization data.
- Confirm highlights, graphical-abstract, and any structured-abstract requirement.
- Re-check competing-interests, funding, author-contribution (CRediT), and AI-use
  disclosure requirements.
- If the live official instructions conflict with this skill, the official
  instructions win.

## Pre-submission self-check

- [ ] The contribution is an AM-specific advance (process / process–structure–property / monitoring–qualification), not a printed part.
- [ ] Process parameters (machine, feedstock, energy input, scan strategy) are reported completely and reproducibly.
- [ ] Structure and property data are quantitative and statistically representative, not single images.
- [ ] Monitoring/control claims demonstrate a validated signal-to-defect or signal-to-property link.
- [ ] Improvements are benchmarked against the correct baseline and explained via the AM mechanism.
- [ ] The article type and length fit Additive Manufacturing's archival format.

## Common desk-reject triggers

- Printing a known part on a commercial machine with no AM-specific process or material insight.
- Property reported with no link to AM process parameters or structure.
- Characterization by representative images only, with no quantification or sampling.
- Monitoring data shown as sensor traces with no validated link to defects or properties.
- Scope mismatch: a metallurgy-first microstructure paper, a subtractive/precision-machining paper, or a pure design-optimization paper with AM as a label.
- Better framed as a physical-metallurgy mechanism study or a precision-manufacturing process study.

## Re-routing decision

- Microstructure mechanism is the point, AM merely the route → `acta-materialia`.
- Subtractive/precision manufacturing or post-machining of AM parts → `international-journal-of-machine-tools-and-manufacture`.
- AM of composite/architected composites with composites as the focus → `composites-part-b-engineering`.
- Constitutive/plasticity modeling of AM material as the core → `international-journal-of-plasticity`.
- Highest-impact conceptual materials advance for a broad audience → `nature-materials`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Additive Manufacturing
[Topic tags] <2–3 closest AM subtopics>
[AM advance] <the process / structure–property / monitoring contribution in one line>
[Method/evidence] <does the AM characterization + reproducibility clear the journal's bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / length / data policy / abstract / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
