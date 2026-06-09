---
name: science-signaling
description: Use when targeting Science Signaling (Sci. Signal.) or deciding whether a cell-signaling, systems-biology, or signaling-pharmacology manuscript fits this AAAS venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Science Signaling (science-signaling)

## Journal positioning

Science Signaling, published by the American Association for the Advancement of Science (AAAS), is a leading journal dedicated to cellular signal transduction and its regulation in health and disease. Its defining character is mechanistic depth in signaling: it publishes primary research and reviews that elucidate how cells sense, transmit, integrate, and respond to information — receptor biology, kinase and phosphatase networks, second messengers, signaling crosstalk, and the systems-level behavior of signaling pathways. The journal rewards work that defines a new signaling mechanism, maps the dynamics or logic of a network, or connects signaling biology to physiology, disease, or pharmacology. Readership spans cell and molecular biologists, systems biologists, and pharmacologists. It is part of the Science family and carries that expectation of significance and rigor.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Science Signaling (AAAS) site.

## When to trigger

- The author names Science Signaling as the target for a mechanistic signal-transduction or systems-biology-of-signaling paper.
- A study defines a new signaling mechanism, network behavior, or pharmacological modulation of a pathway and the author is choosing between Science Signaling and `science-translational-medicine`, `cell-metabolism`, or a specialized signaling journal.
- A systems-biology paper models signaling-network dynamics and needs a venue that values both mechanism and quantitative analysis.
- The author needs Science Signaling's scope, evidence bar, and desk-reject criteria before submission.

## Scope & topic fit

- Receptor and pathway biology: GPCRs, RTKs, immune and cytokine receptors, nuclear receptors, and the signaling cascades they control.
- Kinase/phosphatase networks, post-translational modification signaling, ubiquitin and second-messenger systems, and signaling spatiotemporal dynamics.
- Systems biology of signaling: quantitative or computational models of network logic, dynamics, feedback, and information processing, validated experimentally.
- Signaling in physiology and disease: how dysregulated signaling drives cancer, immune, metabolic, neurological, or cardiovascular pathology.
- Signaling pharmacology: mechanism of action of pathway-targeting agents, biased agonism, allosteric modulation, and resistance mechanisms.
- Methodological advances that enable new signaling measurements (biosensors, phosphoproteomics workflows) when paired with biological insight.

## Method & evidence bar

- Mechanistic causality is required: correlation of signaling events is insufficient; loss- and gain-of-function, pathway perturbation, and direct biochemical evidence must establish the mechanism.
- Quantitative rigor is expected: replicate numbers and statistics defined, effect sizes shown, and dose/time dependence characterized where relevant.
- Systems-biology claims must be validated experimentally; models should be identifiable and their predictions tested, not merely fit to data.
- Physiological or disease relevance is strengthened by in vivo or primary-cell/patient-sample evidence beyond cell lines.
- Antibody validation, reagent specificity (e.g., inhibitor selectivity), and genetic-perturbation controls are scrutinized.
- Data and code must be deposited per current policy: omics data in appropriate public repositories (GEO, PRIDE, etc.), and computational models/code made available (e.g., GitHub/Zenodo).

## Structure & house style

- Science Signaling uses Science-family formats: Research Articles and shorter Research Resources/Reports, plus commissioned Reviews — re-check current article types and limits on the live site.
- The abstract and introduction must state the signaling question and the advance concisely for a broad cell-biology readership; mechanism, not phenomenology, is foregrounded.
- Figures must carry mechanism: pathway diagrams, quantified perturbation experiments, and network/dynamics panels; each panel must justify its inclusion.
- Methods and supplementary data (additional validations, full datasets, model details) are provided as Supplementary Materials; the main text develops the mechanistic argument.
- Materials and reagent details, antibody catalog/validation, and statistical reporting must be complete enough for reproduction.
- Writing is dense and significance-driven; the relevance to signaling biology must be explicit early.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "Science Signaling author guidelines" and follow the current AAAS version, including article-type word/figure limits.
- Re-check data-availability and code-availability requirements; confirm accepted repositories (GEO/PRIDE/etc.) and model/code deposition expectations.
- Re-check reagent, antibody-validation, and statistics-reporting requirements (Science family checklists).
- Re-check competing-interests, funding, ethics/IRB/IACUC approvals, and AI-use disclosure; confirm preprint policy (bioRxiv posting is generally compatible).
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence — the signaling mechanism or network insight advanced and why it matters broadly.
- [ ] Causality is established by perturbation and direct evidence, not correlation alone.
- [ ] Quantification, replicate numbers, and statistics are complete; key experiments include proper controls and reagent validation.
- [ ] Systems-biology models are validated experimentally and their code is available.
- [ ] Omics data and computational code are deposited in public repositories; accession details are ready.
- [ ] The paper is positioned against recent signaling literature and the disease/physiology relevance is explicit.

## Common desk-reject triggers

- A descriptive study reporting signaling correlations without establishing a causal mechanism.
- A cell-line-only result with no physiological, in vivo, or disease-relevant validation where the claim requires it.
- A computational signaling model with no experimental validation of its predictions.
- A pathway "characterization" that is incremental and lacks broad significance for signaling biology.
- Missing reagent/antibody validation, inadequate statistics, or undeposited required data.

## Re-routing decision

- Translational/clinical advance where the therapeutic or patient outcome is the contribution: `science-translational-medicine`.
- Signaling tightly centered on metabolic pathways and physiology: `cell-metabolism`.
- Broad high-impact mechanistic cell biology beyond signaling: a Cell Press primary journal (`cell`, `molecular-cell`).
- Narrow, specialized signaling result without broad significance: a specialized signaling/biochemistry journal.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Science Signaling
[Topic tags] <2–3 closest signaling topics>
[Method/evidence] <is the signaling mechanism established causally, quantified rigorously, and validated in a relevant system?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <article-type limits / data-code deposition / reagent & antibody validation / statistics / disclosure / preprint policy>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
