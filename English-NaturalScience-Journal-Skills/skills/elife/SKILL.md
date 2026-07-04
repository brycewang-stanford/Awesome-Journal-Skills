---
name: elife
description: Use when targeting eLife or deciding whether a life-sciences manuscript fits this open-access life-sciences journal. Encodes eLife's unique Reviewed-Preprint model, fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# eLife (elife)

## Journal positioning

eLife is a non-profit open-access journal covering all of life sciences and biomedicine, operated by an independent board and funded by major research foundations. Its defining structural feature is the **Reviewed-Preprint model**: most submissions are posted as preprints on bioRxiv and receive a public eLife assessment plus full peer-review reports — the journal does not issue a binary accept/reject decision in the traditional sense. The eLife assessment uses a controlled vocabulary (landmark, fundamental, important, valuable, useful, incomplete, inadequate) to characterize significance and evidential strength. The readership is the global life-sciences research community, and the ethos strongly favors rigor, reproducibility, transparency, and open science over prestige signaling. This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on elifesciences.org.

## When to trigger

- The author names eLife as the target venue or is considering an open-access life-sciences outlet with public peer review.
- A manuscript is strong on rigor and reproducibility but may not carry the single-advance framing required by Nature/Cell flagship journals.
- The author wants the manuscript posted as a preprint and reviewed publicly, with transparent reviewer reports and eLife assessments visible to readers.
- The author needs guidance on eLife's Reviewed-Preprint workflow, assessment vocabulary, and what determines a "featured" eLife paper.

## Scope & topic fit

- All areas of life sciences and biomedicine: cell biology, developmental biology, neuroscience, evolutionary biology, genetics/genomics, structural biology, microbiology, immunology, computational biology, and clinical/translational work.
- Methods and resources: new tools, datasets, or software with demonstrated utility in life-sciences research are explicitly welcomed as a first-class article type.
- Negative results, replication studies, and resource papers are more welcome here than at flagship journals — eLife's ethos explicitly values rigor over novelty hype; the assessment vocabulary rewards evidential strength independent of whether results are positive.
- Quantitative and computational biology, biophysics, and cross-disciplinary work that does not fit a single specialty journal.
- Review and opinion content is published but typically commissioned; editors select topics where a synthesis would serve the community — unsolicited reviews should be proposed before full preparation.

## Method & evidence bar

- eLife assesses **evidential strength** explicitly using its assessment vocabulary: claims must be matched by appropriate experimental or computational evidence; overclaiming relative to evidence is a primary editorial concern and results in a lower significance or strength rating.
- Reproducibility practices are expected: data deposition (raw data, processed data), code availability, detailed methods — eLife pushes authors toward full transparency more forcefully than most traditional journals.
- Statistical rigor: pre-registration is not mandatory but is valued; sample sizes must be justified; effect sizes and confidence intervals preferred over significance thresholds alone.
- For animal studies, ARRIVE reporting guidelines apply; for human studies, CONSORT/STROBE as appropriate and ethics declarations.
- Revised manuscripts under the Reviewed-Preprint model are re-assessed publicly; the revision letter and author response are posted alongside the paper.
- The assessment distinguishes significance (landmark → important → valuable → useful) from evidential strength (exceptional → compelling → convincing → inadequate) independently — authors should calibrate which dimension their manuscript excels on.

## Structure & house style

- eLife uses a structured-summary abstract format (editor's evaluation is posted separately; author's abstract is standard unstructured).
- Article types include Research Articles, Short Reports, Tools and Resources, Research Advances, Feature Articles, and Reviews — each has distinct scope expectations (verify current definitions on the live site).
- The **eLife digest** (plain-language summary for a non-specialist audience) is expected with most research articles; it is public-facing.
- Figures should be publication-ready and accompanied by source data files (underlying numerical data for each panel).
- The public peer-review reports and author responses form part of the published record — draft the response letter with this in mind from submission.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "eLife author guide" or "eLife submission process" and follow the current version at elifesciences.org.
- Re-check the current Reviewed-Preprint model workflow, including preprint posting consent, assessment timeline, and the distinction between "eLife Reviewed Preprint" and a "Version of Record."
- Confirm data deposition requirements: raw data, processed data, and code repositories (Zenodo, GitHub, Dryad, GEO, SRA, RCSB, etc.) expected before publication.
- Check reporting guidelines: ARRIVE (animal), CONSORT/STROBE (clinical), MIQE (qPCR), or other community standards relevant to the study type.
- Verify open-access licensing (eLife publishes under CC-BY), funding and competing-interests disclosure, and AI-use policy.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence matching the claimed significance level ("landmark," "fundamental," "important," or "valuable") to the actual evidence presented — do not overstate.
- [ ] All raw data, processed data, and analysis code are deposited or will be deposited, with accession numbers/links ready.
- [ ] The eLife digest is drafted and accessible to a scientifically literate non-specialist.
- [ ] The manuscript is posted or is ready to be posted as a preprint (bioRxiv or equivalent); consent for public posting is confirmed.
- [ ] Reporting guidelines relevant to the study type have been applied and a checklist is ready.

## Common desk-reject triggers

- Scope entirely outside life sciences or biomedicine (physics, chemistry without biological application, social science).
- Manuscripts where the significance claim is drastically mismatched with evidential strength — editors use the assessment vocabulary to flag this explicitly.
- Clinical trials or large-scale human studies without the appropriate reporting compliance (registration, CONSORT, ethics).
- Refusal to post a preprint or to participate in the Reviewed-Preprint workflow may affect routing (verify current policy on whether non-preprint submissions are accepted).
- Studies reporting software or databases without working, documented, publicly accessible code/data.

## Re-routing decision

- Flagship-level conceptual advance across life sciences → `nature`, `science`, `cell`, or `pnas`.
- Open-access general biology with a more pronounced methods/transparency culture → `plos-biology`.
- Genomics or computational biology focus → `genome-biology`.
- Neuroscience with field-leading conceptual advance → `nature-neuroscience` or `neuron`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] eLife
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the evidential strength match the claimed significance level per eLife's assessment vocabulary?>
[Top risk] <the single most likely reason for rejection or a weak assessment>
[Official items to re-check] <Reviewed-Preprint workflow / data deposition / reporting checklist / digest / CC-BY / ethics>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
