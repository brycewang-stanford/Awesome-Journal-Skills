---
name: physical-review-applied
description: Use when targeting Physical Review Applied (PRApplied) or deciding whether an applied-physics manuscript bridging fundamental physics and devices, quantum technology, photonics, energy, or sensing fits this APS venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Physical Review Applied (physical-review-applied)

## Journal positioning

Physical Review Applied is the American Physical Society's journal for applied physics that bridges fundamental physics and applications. Its defining character is the explicit link between a physical mechanism and a functional consequence: PRApplied publishes work where rigorous physics enables a device, technology, or measurement capability — quantum hardware, photonic and optoelectronic devices, energy materials and conversion, sensing and metrology, spintronics, and acoustics/metamaterials. The journal sits between the discovery-oriented Physical Review family and pure engineering venues; a strong PRApplied paper is physics-grade in rigor but motivated by, and demonstrated toward, an application. Readership is the applied-physics and quantum-technology community spanning physics, materials science, and electrical engineering. This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Physical Review Applied APS site.

## When to trigger

- The author names Physical Review Applied as the target venue for applied-physics work connecting a physical mechanism to a device or technology.
- A manuscript demonstrates a quantum, photonic, energy, sensing, or spintronic capability grounded in rigorous physics rather than empirical engineering optimization.
- A paper advances an enabling physical principle and the author is choosing between PRApplied, Physical Review X, and an applied-physics specialist venue.
- The author needs PRApplied's application-relevance bar, evidence expectations, and desk-reject criteria before submission.

## Scope & topic fit

- Quantum technology: qubits, quantum sensors, quantum control, error mitigation, and device-level demonstrations where physics enables the capability.
- Photonics and optoelectronics: lasers, detectors, integrated photonics, metasurfaces, and nonlinear optical devices with quantitative performance physics.
- Energy physics: photovoltaics, thermoelectrics, batteries, catalysis, and energy conversion where transport or interface physics is central.
- Sensing and metrology: magnetometry, atomic and optical sensors, precision measurement, and imaging with characterized physical limits.
- Spintronics and magnetism: spin transport, magnetic memory and logic, and domain dynamics with device relevance.
- Acoustics, metamaterials, and mechanics: phononics, wave control, and structured-material devices grounded in wave physics.

## Method & evidence bar

- The paper must establish both the physical mechanism and its application relevance; a device result without physics insight, or physics without a credible application link, is a misfit.
- Experimental demonstrations require characterized performance with uncertainties, benchmarking against the relevant state of the art or physical limits, and reproducibility detail.
- Theoretical/computational device proposals must be quantitatively realistic — material parameters, fabrication feasibility, and noise/loss budgets — not idealized in-principle schemes only.
- Claims of improvement (efficiency, coherence, sensitivity) must be supported by quantitative comparison and, where relevant, statistical analysis across samples or runs.
- Methods must be reproducible: fabrication, measurement setup, calibration, and data processing documented in the paper or Supplemental Material.
- Data and code supporting key results should be available where reproducibility depends on them.

## Structure & house style

- PRApplied uses the standard Physical Review article format with Regular Articles; length follows completeness, and a clear application motivation is expected in the framing.
- Use REVTeX with structured sections; the Introduction should state the physical principle and the targeted application together.
- The abstract states the mechanism, the demonstrated capability, and the quantitative performance result.
- Figures must be quantitative: device schematics, characterized performance curves with uncertainties, and benchmarking comparisons.
- Supplemental Material carries fabrication details, extended characterization, calibration procedures, and supporting derivations.
- Cite both the fundamental-physics and the application/device literature precisely so the bridge the paper builds is explicit.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "Physical Review Applied author guidelines" and follow the current APS version.
- Re-check article-type definitions and current length and figure conventions, and the journal's application-relevance expectations.
- Re-check data-availability and code-availability requirements; confirm Supplemental Material formatting and deposition expectations.
- Re-check competing-interests, funding, and AI-use disclosure requirements; confirm preprint policy (arXiv posting is standard and compatible).
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence — the physical mechanism and the application capability this paper connects.
- [ ] Experimental performance is characterized with uncertainties and benchmarked against the state of the art or physical limits.
- [ ] A device proposal (if theoretical) uses realistic parameters and addresses fabrication/noise feasibility.
- [ ] Improvement claims are backed by quantitative comparison across samples or runs.
- [ ] Fabrication, measurement, and calibration methods are reproducible from the paper or Supplemental Material.
- [ ] The paper is positioned against recent PRApplied / PRX and the relevant device literature.

## Common desk-reject triggers

- A pure device-engineering optimization with no physical insight, or a physics result with no credible application link.
- An idealized theoretical scheme with unrealistic parameters and no path to a real device.
- A performance claim without uncertainties or benchmarking against the relevant state of the art.
- A fundamental-physics study with no application relevance that belongs in PRE, PRB, or PRX.
- An incremental materials or device variation with no new enabling principle or capability.

## Re-routing decision

- Exceptionally broad, transformative result across physics: `physical-review-x`.
- Fundamental condensed-matter physics without device focus: `physical-review-b`.
- Quantum-information-science result with broad significance: `prx-quantum`.
- Discipline-specific applied venue beyond APS scope: Applied Physics Letters / Journal of Applied Physics (AIP), Optica/Optics Express (Optica), or ACS Photonics depending on subfield.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Physical Review Applied
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the paper connect a rigorous physical mechanism to a demonstrated, benchmarked application capability?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article type / length conventions / Supplemental Material / data-code deposition / disclosure / preprint policy>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
