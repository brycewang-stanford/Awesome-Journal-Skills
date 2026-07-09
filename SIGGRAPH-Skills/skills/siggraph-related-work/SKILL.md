---
name: siggraph-related-work
description: Use when writing or auditing the related-work positioning of a SIGGRAPH / TOG paper, covering the computer-graphics literature lanes (rendering, geometry, animation, simulation, imaging, fabrication, learning-for-graphics), capability-delta positioning against the strongest prior method, and correct attribution across SIGGRAPH, SIGGRAPH Asia, TOG, EG/CGF, and sibling venues.
---

# SIGGRAPH Related Work

At SIGGRAPH, related work is where you convince a domain-expert reviewer that your contribution is
**new capability**, not a rediscovery. Graphics reviewers know the canon and the current
state-of-the-art in your sub-area intimately; a missed or mischaracterized prior method is a fast
reject. Position by **capability delta** — what prior methods cannot do that yours can — not by
chronology. Anchor venue facts to `resources/official-source-map.md`.

## Know the lanes

SIGGRAPH's scope spans distinct sub-communities, each with its own canon and its own reviewers.
Place your paper in the right lane(s) and cover that lane's recent state-of-the-art:

| Lane | What the lane cares about | Adjacent venues to check |
|---|---|---|
| Rendering / light transport | Noise, bias, convergence, speed, physical accuracy | EGSR, HPG, TOG |
| Geometry processing | Robustness on real meshes, guarantees, generality | SGP, TOG |
| Animation / character | Naturalness, control, temporal coherence | SCA, TOG |
| Physical simulation | Stability, energy behavior, time-step, scale | SCA, TOG |
| Imaging / computational photography | Reconstruction quality, artifacts, hardware | ICCP, TOG |
| Geometry/appearance capture, fabrication | Fidelity to real objects, manufacturability | TOG, EG |
| Learning for graphics (neural rendering, generative 3D) | Quality, generality, controllability | CVPR/ICCV overlap, TOG |
| Interaction / VR-AR-MR, HCI-for-graphics | Latency, presence, usability | CHI/UIST overlap, TOG |

A paper often sits in two lanes (e.g., neural rendering = rendering + learning). Cover both; a
reviewer from either lane will check that their canon is represented.

## Capability-delta positioning

For each closest prior method, state the axis on which you differ and by how much:

- **Quality:** "Prior method X leaves visible noise below N samples; ours converges at N/4."
- **Speed:** "X runs offline; ours is real-time at the same quality."
- **Generality:** "X assumes manifold input; ours handles the non-manifold meshes practitioners
  actually have."
- **Robustness:** "X diverges on stiff configurations; ours remains stable."

Never leave the comparison at "we are related to X." Name the axis, and back it with a comparison
in the Results (see `siggraph-experiments`). The strongest baseline must appear both here and in a
head-to-head figure/table.

## Attribution discipline (venue collisions are common)

Graphics ideas migrate across venues; attribute precisely:

- **SIGGRAPH vs SIGGRAPH Asia vs TOG-direct.** All three publish in ACM TOG. Cite the specific
  issue; do not say "SIGGRAPH" for a SIGGRAPH Asia or a rolling TOG paper.
- **SIGGRAPH vs Eurographics (EG/CGF).** Many canonical techniques debuted at Eurographics or in
  Computer Graphics Forum, not SIGGRAPH — check dblp before attributing a method to SIGGRAPH.
- **Specialized venues.** EGSR (rendering), SGP (geometry), SCA (animation/simulation), HPG
  (high-performance graphics), I3D (interactive 3D), ICCP (computational photography) host founding
  papers routinely misattributed to SIGGRAPH.
- **The vision overlap.** Neural rendering / generative-3D work has a large CVPR/ICCV literature;
  cite it, and be clear which contribution is the graphics advance versus the vision one.

## Self-positioning and blinding

SIGGRAPH review has historically been **single-blind** (authors visible), so citing your own prior
work in the natural voice is usually fine — **but confirm the current cycle's policy** (**待核实**
for 2026). If a cycle requires anonymized review, cite your prior work in the third person and
avoid "our previous system X."

## Anti-patterns

- A chronological literature tour with no capability delta.
- Omitting the single strongest baseline because it is inconvenient — the reviewer knows it exists.
- Attributing an Eurographics/EGSR/SCA method to SIGGRAPH (or vice versa) without checking dblp.
- Treating a CVPR neural-rendering line as if it did not exist because "this is a graphics venue."
- Positioning against a strawman instead of the current state-of-the-art in the lane.

## Output format

```text
[Lanes] which sub-community/-ies; is each lane's SOTA covered? yes/no
[Strongest baseline] named here and compared head-to-head in Results? yes/no
[Deltas] <prior method -> axis (quality/speed/generality/robustness) -> magnitude>
[Attribution] SIGGRAPH vs SA vs TOG vs EG/EGSR/SGP/SCA checked on dblp? yes/no
[Blinding] cycle policy confirmed; self-cite voice correct? yes/no
[Fixes] <ordered>
```
