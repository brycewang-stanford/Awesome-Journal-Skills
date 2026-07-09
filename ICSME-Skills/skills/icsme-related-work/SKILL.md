---
name: icsme-related-work
description: Use when positioning an IEEE ICSME submission against the software-maintenance and evolution literature across ICSME, SANER, MSR, ICPC, SCAM, ICSE/FSE, and the SE journals (TSE, EMSE), writing delta-first contrast rather than a citation catalog, keeping self-citations double-anonymous, and handling replication overlap and prior-version eligibility.
---

# ICSME Related Work

Use this to audit novelty and eligibility. ICSME reviewers are close to the maintenance/evolution
literature and expect to see where your paper sits relative to the nearest prior work — stated as a
**delta**, not a list. Because the venue values replication (the RENE track) and rewards honest
re-examination, "we redo prior work" is a legitimate contribution *when framed as one* — but it
must engage the original explicitly. Reopen the current call for dual-submission, anonymity, and
prior-publication rules before advising.

## Positioning checks

- **Separate the maintenance/evolution novelty from the engineering effort.** What is new: a
  technique, an empirical finding about how software ages, a validated measurement of debt or
  comprehension, a recovered model, or an evidence regime nobody had covered?
- **Cover the maintenance lanes.** ICSME reviewers expect the evolution venues and journals, not
  just the papers nearest your method (see the table). A bibliography missing the obvious sibling
  work reads as unaware of the community.
- **Write delta-first.** Each closely related paper gets one sentence naming what it did and one
  naming what you do differently — not a summary. Position, don't catalog.
- **Preserve double-anonymity.** Cite your own prior maintenance studies in the third person and
  never link reviewers to an identity-revealing preprint, repository, or homepage.
- **Declare overlap** with any prior workshop/short version or a replicated original; for a RENE
  submission, name the exact study you reproduce.

## Maintenance literature lanes

| Lane | Typical venues | What ICSME reviewers check |
|---|---|---|
| Maintenance & evolution core | ICSME, SANER, ICSM (historical) | Whether the nearest evolution technique/study is compared or distinguished |
| Mining software repositories | MSR | Whether prior mining work on your data/phenomenon is acknowledged |
| Comprehension & source analysis | ICPC, SCAM | Whether comprehension or analysis predecessors are credited |
| General-SE flagships | ICSE, ESEC/FSE | Whether the broad-SE technique/study you build on is engaged |
| SE journals | TSE, EMSE | Whether deeper journal-length maintenance studies are engaged |

A bibliography that cites only your own subarea tells a reviewer the delta may be smaller than
claimed; one that reaches the evolution siblings and journals signals command of the field.

## Delta-first positioning vignette

Suppose the paper proposes a *predictor* of technical-debt hotspots plus a study. Its nearest
neighbors: a foundational empirical study characterizing debt accumulation (no predictor), an MSR
tool that mines debt-related commits (detection, not prediction), and a TSE study on debt repayment
economics (scope, no method). The novelty sentence should name all three contrasts — prediction
where the study offered characterization, forward-looking where the tool was retrospective, and a
technique where the journal offered only economics.

## Replication and prior-version judgment calls

```text
[RENE replication]        name the exact original study; state what you kept identical and what you
                          extended (new datasets, new systems); frame reproducibility as the contribution
[Concurrent arXiv work]   cite neutrally, state the technical difference, avoid priority claims;
                          keep the citation double-anonymous
[Your workshop/SANER version] usually citable, but confirm against the current CFP and phrase so
                          anonymity survives; state what the full paper adds
[Prior short/NIER version] declare the overlap and state what the full study adds beyond it
[Archival status unclear] declare the overlap in the submission form rather than guessing
```

## Eligibility red flags

- Substantial text overlap with a published paper by the same authors (self-plagiarism risk).
- A "new" study that re-reports a prior corpus's numbers without a new maintenance question — unless
  submitted to RENE and framed honestly as replication.
- Citations exclusively to non-maintenance venues, signaling a paper rerouted here without reframing.

## Output format

```text
[Eligibility] clear / needs declaration / risky
[Lanes covered] <maintenance-core / mining / comprehension-analysis / flagships / journals>
[Nearest 3 works] <work -> one-line delta>
[Replication framing] <n/a | RENE: original study named + what was extended>
[Novelty sentence] <ICSME-ready contribution contrast against the nearest prior work>
```
