---
name: the-isme-journal
description: Use when targeting The ISME Journal (ISME J) or deciding whether a microbial-ecology manuscript fits this flagship community-and-function venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# The ISME Journal (the-isme-journal)

## Journal positioning

The ISME Journal is the flagship journal of the International Society for Microbial Ecology, now published with Oxford University Press (formerly Springer Nature). Its defining character is mechanism in microbial ecology: it publishes work on how microbial communities are structured, how they function, and how they evolve and interact with their environments, across habitats from soils and oceans to host-associated microbiomes. The journal rewards studies that move beyond cataloguing taxa to explaining ecological and evolutionary processes — community assembly, biogeochemical function, microbial interactions, adaptation — typically integrating multi-omics with experiments, modeling, or ecological theory. Pure surveys, descriptive amplicon snapshots, and applied or engineered-system studies without ecological insight are poor fits. Readership is the microbial ecology community spanning environmental microbiology, microbiome science, biogeochemistry, and microbial evolution. This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on The ISME Journal OUP site.

## When to trigger

- The author names The ISME Journal as the target for a microbial-ecology study of community structure, function, evolution, or interactions.
- A manuscript explains a microbial-ecological process using multi-omics, experiments, or modeling, and the author is choosing between ISME J, Nature Microbiology, Microbiome, and mSystems.
- A paper links microbial community composition to ecosystem function or biogeochemistry, or tests an ecological/evolutionary mechanism in a microbial system.
- The author needs ISME J's mechanism-and-evidence bar, multi-omics expectations, and desk-reject criteria before submission.

## Scope & topic fit

- Community structure and assembly: drivers of microbial community composition, diversity, succession, and the relative roles of deterministic vs. stochastic assembly processes.
- Microbial function and biogeochemistry: linking community composition or activity to nutrient cycling, carbon/nitrogen/sulfur transformations, and ecosystem processes.
- Microbiome ecology: host-associated communities (human, animal, plant) analyzed for ecological or evolutionary mechanism, not descriptive composition alone.
- Microbial interactions: competition, cooperation, cross-feeding, phage–host dynamics, and the eco-evolutionary consequences of interaction networks.
- Microbial evolution and adaptation: in situ or experimental evolution, population genomics, horizontal gene transfer, and niche adaptation in natural communities.
- Multi-omics and methods that enable ecological inference: metagenomics, metatranscriptomics, metaproteomics, metabolomics, single-cell, and integrative frameworks that deliver process-level understanding.

## Method & evidence bar

- The contribution must be ecological or evolutionary mechanism, not a taxonomic inventory; composition data must be interpreted in terms of process.
- Multi-omics or functional evidence is expected where claims concern function; inferring function from 16S/marker-gene composition alone is generally insufficient.
- Sampling and experimental design must support the inference: adequate replication, appropriate controls, and statistical power for community-level comparisons.
- Bioinformatic pipelines must be current and reproducible; tool versions, parameters, databases, and quality-control steps must be reported, with code available.
- Causal or mechanistic claims should be supported by experiments, manipulations, or modeling, not correlation among omics layers alone.
- Sequence data must be deposited in an appropriate public archive (e.g., INSDC: NCBI/ENA/DDBJ; MGnify where relevant) with accession numbers, and analysis code in a public repository.

## Structure & house style

- ISME J publishes Articles and Brief Communications using standard structure (Abstract, Introduction, Results, Discussion, Methods); re-check current article types and limits on the live site.
- Methods must fully document field/experimental design, wet-lab protocols, sequencing platforms, and the complete bioinformatic workflow with versions and parameters.
- Figures should foreground the ecological/evolutionary result — function, interaction, or process — rather than raw composition bar charts; multi-omics integration should be visually clear.
- The Introduction frames the microbial-ecology question and its general significance; the readership spans habitats, so the conceptual stakes must travel beyond one system.
- Supporting Information carries extended methods, supplementary omics analyses, sensitivity/robustness checks, and additional figures and tables.
- Reporting must enable reproducibility: data-availability and code-availability statements with working accessions and repository links.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "The ISME Journal instructions to authors" and follow the current Oxford University Press version (note the move from Springer Nature).
- Re-check article types (Article, Brief Communication, etc.) and their word, figure, and reference limits; confirm current abstract conventions.
- Re-check data-deposition requirements: appropriate sequence archive (NCBI/ENA/DDBJ, MGnify), accession-at-submission expectations, and code-availability policy.
- Re-check competing-interests, funding, ethics/biosafety, and AI-use disclosure requirements; confirm preprint policy (bioRxiv posting is generally compatible).
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence — the microbial-ecological or evolutionary mechanism advanced and why it matters across systems.
- [ ] Functional claims are backed by multi-omics, experiments, or modeling, not marker-gene composition alone.
- [ ] Design has adequate replication, controls, and power for community-level inference.
- [ ] The full bioinformatic pipeline is reported with versions, parameters, and databases, and the code is available.
- [ ] Sequence data are deposited with accessions ready; data- and code-availability statements are complete.
- [ ] The result is framed as ecological/evolutionary process with significance beyond a single habitat or sample set.

## Common desk-reject triggers

- A descriptive amplicon survey or microbiome census reporting composition without an ecological or evolutionary mechanism.
- Functional or causal claims inferred from 16S/marker-gene data alone, without functional or experimental support.
- Under-replicated or uncontrolled designs that cannot support community-level statistical inference.
- An applied or engineered-system study (e.g., bioreactor optimization, wastewater process performance) without ecological insight.
- Missing or non-reproducible bioinformatics — undocumented pipelines, absent versions, or undeposited sequence data.

## Re-routing decision

- Higher-impact, broad-interest microbiology with strong mechanistic or translational reach: `nature-microbiology`.
- Engineered or applied systems — wastewater, bioremediation, water treatment, contaminant biogeochemistry: `environmental-science-and-technology`.
- Microbiome-focused study where the host–microbiome system and methods are the contribution: Microbiome or mSystems.
- Broad ecological theory tested in a microbial system with brevity at a premium: `ecology-letters`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] The ISME Journal
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the paper deliver microbial-ecological/evolutionary mechanism with multi-omics or experimental support and reproducible bioinformatics — not a descriptive survey?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article-type limits / sequence-archive deposition & accessions / bioinformatics reporting / disclosure / preprint policy>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
