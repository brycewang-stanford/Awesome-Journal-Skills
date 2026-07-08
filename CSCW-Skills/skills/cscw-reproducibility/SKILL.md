---
name: cscw-reproducibility
description: Use when strengthening the transparency of a CSCW paper — auditable qualitative analysis trails, documented trace pipelines, codebooks and instruments, and honest data-availability statements when community and participant data cannot ethically be shared.
---

# CSCW Reproducibility and Transparency

Reproducibility at CSCW cannot mean "rerun my script, get my table" — most of the
venue's evidence is people, and much of it must never leave the research team. The
venue's real standard is **auditability**: a skeptical reader should be able to see
how you got from data to claims, and to *build on* the work, even where they cannot
re-execute it. Different strands of a paper owe different transparency debts.

## What each strand owes

| Evidence strand | Shareable | Auditable instead of shareable |
| --- | --- | --- |
| Interviews / fieldwork | Interview guide, recruitment text, codebook with definitions and example (paraphrased) excerpts | The analysis trail: coding approach, memo practice, how disagreements were resolved, how themes stabilized |
| Trace / log analysis | Pipeline code, query definitions, aggregated datasets, synthetic samples | Exact API/version/date of collection; filtering decisions with counts at each step; bot/deletion handling |
| Surveys | Full instrument, scale provenance, analysis scripts | Sampling frame, response/nonresponse accounting |
| Deployments | System code or architecture description, condition assignment logic | Site-selection reasoning; what the deployment context makes non-portable |
| Statistics anywhere | Analysis scripts keyed to each table/figure | Pre-specification vs. exploration, stated honestly |

## The qualitative transparency trail

You cannot share transcripts; you can share how you thought. The auditable minimum
for interpretive work:

- **A codebook that could be picked up by a stranger** — code names, definitions,
  inclusion/exclusion notes, and one paraphrased exemplar each. Whether inter-rater
  statistics belong depends on the tradition; *saying which tradition and why* is
  the transparency act.
- **A decision log** of analytic turning points: when categories merged, what
  disconfirming cases forced revisions. Two paragraphs in an appendix outperform a
  ritual "themes emerged."
- **Quote provenance discipline:** every quotation traceable (internally) to a
  participant and context, with the paraphrase/alteration policy stated in the
  paper.

## The trace-pipeline ledger

Platform data rots. Reviewers and future researchers need the ledger even when the
data cannot travel:

```text
[Source]     platform, endpoint/API version, collection dates
[Scope]      query terms / community list / time window, with the WHY
[Attrition]  rows at each filter step: raw → deduplicated → bot-filtered →
             analysis set (counts, not adjectives)
[Constructs] each analysis variable → the raw field(s) it derives from →
             the practice it is claimed to measure
[Fragility]  what breaks if the platform changes (API terms, deletion policy)
[Release]    what is shared: code / aggregates / synthetic sample / nothing + reason
```

## Honest availability statements

Write the data statement as a truth-telling exercise, not boilerplate. Three honest
shapes:

1. "Analysis code and aggregated measures are available at <archive>; raw traces
   cannot be redistributed under the platform's terms and our ethics protocol."
2. "The codebook, interview guide, and consent materials are provided; transcripts
   are not shareable under the consent participants gave — we chose consent terms
   that protected candor over shareability, and say so."
3. "A synthetic dataset preserving the marginal distributions is provided for
   pipeline verification."

What never survives review twice (remember the same reviewers return at R&R):
"data available upon reasonable request" with no request path, and claims of
sharing that the supplement does not actually contain.

## Preregistration and its limits

For confirmatory quantitative strands, preregistration strengthens the paper —
link it anonymized (registries support anonymous view links). Do not force
exploratory or interpretive work into a preregistration costume; labeling
exploration honestly *is* the venue's norm.

## Transparency audit

```text
[Per strand]   shareable artifacts listed and actually present? y/n
[Qualitative]  codebook + decision log exist? tradition named? y/n
[Trace]        ledger complete incl. attrition counts? y/n
[Statement]    availability text matches reality exactly? y/n
[Ethics gate]  every shared artifact re-checked against consent scope? y/n
```

Run the gate last and strictly: a transparency package that violates a consent
agreement is not a reproducibility win, it is a research-ethics failure that
`cscw-artifact-evaluation` exists to prevent.
