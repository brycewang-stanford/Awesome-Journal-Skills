---
name: acs-catalysis
description: Use when targeting ACS Catalysis (ACS Catal) or deciding whether a catalysis manuscript fits this primary-research venue spanning heterogeneous, homogeneous, bio-, electro-, and photocatalysis. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# ACS Catalysis (acs-catalysis)

## Journal positioning

ACS Catalysis is a high-impact American Chemical Society journal devoted to primary research across the full breadth of catalysis: heterogeneous, homogeneous, organocatalysis, biocatalysis, electrocatalysis, and photocatalysis. Its defining character is that it rewards work in which a catalytic advance is supported by an interlocking case of activity/selectivity data, characterization, and mechanistic insight — not activity numbers alone, and not characterization without a catalytic payoff. The journal sits at the center of the catalysis community: it expects rigorous, reproducible, and mechanistically grounded studies that move beyond empirical screening toward understanding of how and why a catalyst works. Readership spans synthetic chemists, materials and surface scientists, electrochemists, and enzymologists. This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official guidelines. Before submitting, re-check the live author instructions on the ACS Catalysis site.

## When to trigger

- An author has a primary-research catalysis study and is choosing where mechanism, characterization, and performance together carry the paper.
- A team is deciding between ACS Catalysis and Nature Catalysis or a broad chemistry venue, weighing impact against scope fit.
- A manuscript reports a new catalyst, reaction, or mechanistic understanding and needs the journal's evidence bar — activity plus characterization plus mechanism — clarified before submission.
- An author needs ACS Catalysis' expectations on controls, reproducibility, and mechanistic rigor, plus desk-reject criteria.

## Scope & topic fit

- Heterogeneous catalysis: supported metals, oxides, single-atom catalysts, zeolites — with structure–activity relationships and, ideally, operando/in situ characterization.
- Homogeneous and organometallic catalysis: new catalytic transformations, ligand design, and mechanism established by kinetics, spectroscopy, or computation.
- Electrocatalysis and photocatalysis: energy-relevant reactions (HER, OER, ORR, CO2 reduction, N2 reduction, water/CO2 photoreduction) with rigorous activity metrics and faradaic/quantum-efficiency reporting.
- Biocatalysis and enzyme engineering: engineered or natural enzymes for synthetically or industrially useful transformations, with kinetic and structural support.
- Organocatalysis and asymmetric catalysis: new modes of activation or selectivity with mechanistic and stereochemical analysis.
- Catalysis-enabling methods and theory: computational mechanism, machine-learning descriptors, and characterization advances that yield genuine catalytic understanding.

## Method & evidence bar

- A catalytic claim must rest on the triad of performance, characterization, and mechanism; any single leg alone is typically insufficient.
- Activity and selectivity must be reported with proper normalization (per active site/TOF where possible), conversion and yield, and appropriate controls including blanks and benchmark catalysts.
- Characterization must establish the catalyst's actual state — composition, structure, and active site — with in situ/operando evidence favored over ex situ inference where the mechanism depends on it.
- Mechanistic claims require kinetics, isotope or labeling studies, spectroscopic intermediates, or computation, not speculation; DFT must use justified models and be reconciled with experiment.
- Stability and reproducibility are expected: cycle/durability data for materials, and enough experimental detail (loadings, conditions, error bars, replicates) for reproduction.
- Electro-/photocatalysis must report standardized metrics (iR correction, faradaic efficiency, overpotential at defined current density, quantum/photonic efficiency) and rule out artifacts.

## Structure & house style

- Standard primary-research format (Introduction, Results and Discussion, Conclusions, Experimental/Methods) with a Supporting Information file carrying full procedures, spectra, and supplementary data.
- A clear table-of-contents/abstract graphic is required and should communicate the catalytic advance at a glance.
- Figures should integrate performance with characterization and mechanism; schemes for reactions and proposed cycles are expected where relevant.
- The Introduction must position the work against the catalysis literature and state the specific advance; Results must foreground evidence, not narrative.
- Methods/Experimental must be reproducible: catalyst synthesis, reaction conditions, instrument parameters, and quantification methods fully specified.
- Article types include full Articles and Letters/Communications; re-check current length, figure, and Letter-format limits on the live site.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current ACS Catalysis page you checked.
- Search the live site for "ACS Catalysis author guidelines" and follow the current ACS version.
- Re-check article-type definitions and current word/figure limits, Letter vs Article criteria, and Supporting Information conventions.
- Re-check ACS data-availability, characterization-data (e.g., NMR/crystallographic), and reproducibility-reporting requirements for the relevant catalysis subfield.
- Re-check competing-interests, funding, ORCID, and AI-use disclosure requirements; confirm ChemRxiv preprint policy.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence — the catalytic advance and the mechanistic insight that explains it.
- [ ] Performance, characterization, and mechanism are all present and mutually reinforcing, with appropriate controls and benchmarks.
- [ ] Activity/selectivity metrics are correctly normalized and, for electro-/photocatalysis, reported with standardized parameters.
- [ ] Catalyst state and active site are established by suitable (ideally in situ/operando) characterization.
- [ ] Stability/reproducibility data and full experimental detail are in the SI for independent reproduction.
- [ ] The work is positioned against recent ACS Catalysis / Nature Catalysis literature on the same reaction or catalyst class.

## Common desk-reject triggers

- An activity-screening study reporting performance numbers with no mechanistic insight or characterization of the working catalyst.
- Characterization-heavy materials work with no meaningful catalytic evaluation or with poorly defined catalytic relevance.
- Electro-/photocatalysis lacking standardized metrics, controls, or artifact exclusion (e.g., no faradaic efficiency, no iR correction, no blank).
- Incremental catalyst tweaks without a clear advance over established benchmarks.
- Mechanistic claims unsupported by kinetics, labeling, spectroscopy, or properly validated computation.

## Re-routing decision

- Higher-impact, conceptually transformative catalysis with broad significance: `nature-catalysis`.
- Broad-chemistry primary research where catalysis is one facet of a wider advance: `journal-of-the-american-chemical-society`.
- Authoritative catalysis review rather than primary research: `chemical-reviews` or `chemical-society-reviews`.
- Energy-device-centric electro-/photocatalysis where the system, not the catalyst mechanism, is the contribution: `energy-and-environmental-science` or `joule`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] ACS Catalysis
[Topic tags] <2–3 closest topics>
[Method/evidence] <do performance, characterization, and mechanism together support the catalytic claim, with proper metrics and controls?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article-type limits / characterization & data requirements / standardized metrics / SI / disclosure / preprint>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
