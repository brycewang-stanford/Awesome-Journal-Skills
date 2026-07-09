---
name: fse-related-work
description: Use when positioning an ESEC/FSE submission against the software-engineering literature across ICSE, FSE, ASE, ISSTA, MSR, and the SE journals (EMSE, TSE, TOSEM), writing delta-first contrast rather than a citation catalog, keeping self-citations double-anonymous, and handling concurrent, preprint, and prior-version overlap.
---

# FSE Related Work

Use this to audit novelty and eligibility. FSE reviewers are close to the SE literature and expect
to see where your paper sits relative to the nearest prior work — stated as a **delta**, not a
list. Reopen the current call for dual-submission, anonymity, and prior-publication rules before
advising authors.

## Positioning checks

- **Separate the software-engineering novelty from the engineering effort.** What is new: a
  technique, an empirical finding, a validated measurement, a design, or an evidence regime nobody
  had covered?
- **Cover the SE lanes.** FSE reviewers expect the flagship venues and the journals, not just the
  papers nearest your method (see the table). A bibliography missing the obvious sibling work reads
  as unaware.
- **Write delta-first.** Each closely related paper gets one sentence naming what it did and one
  naming what you do differently — not a summary. Position, don't catalog.
- **Preserve heavy double-anonymity.** Cite your own prior work in the third person and never link
  reviewers to an identity-revealing preprint, repository, or homepage.
- **Declare overlap** with any prior conference/workshop version or concurrent submission; do not
  re-submit archival work as new.

## SE literature lanes

| Lane | Typical venues | What FSE reviewers check |
|---|---|---|
| General-SE flagships | ICSE, ESEC/FSE | Whether the nearest broad-SE technique/study is compared or distinguished |
| Automation & analysis | ASE, ISSTA | Whether tool-centric or testing/analysis predecessors are credited |
| Mining & evolution | MSR, ICSME | Whether prior empirical/mining work on your data is acknowledged |
| SE journals | EMSE, TSE, TOSEM | Whether deeper journal-length studies on the topic are engaged |
| Adjacent fields (when relevant) | PL, HCI, ML venues | Whether borrowed methods are cited to their real origin |

A bibliography that cites only your own subarea tells a reviewer the delta may be smaller than
claimed; one that reaches the sibling flagships and journals signals command of the field.

## Delta-first positioning vignette

Suppose the paper proposes a flaky-test *classifier* and an accompanying study. Its nearest
neighbors: the foundational flaky-tests empirical study (characterization, no predictor), an ASE
tool that reruns tests to detect flakiness (dynamic, expensive), and a journal study on flaky-test
prevalence (scope, no method). The novelty sentence should name all three contrasts — prediction
where the study offered only characterization, a static filter where the tool required reruns, and
a technique where the journal offered only prevalence.

## Concurrent and prior-version judgment calls

```text
[Concurrent arXiv work]   cite neutrally, state the technical difference, avoid unverifiable
                          priority claims; keep the citation double-anonymous
[Your workshop version]   usually non-archival and citable, but confirm against the current CFP
                          wording and phrase so anonymity survives
[Prior short/NIER version] declare the overlap and state what the full paper adds beyond it
[Archival status unclear]  declare the overlap in the submission form rather than guessing a
                          chair's interpretation
```

## Eligibility red flags

- Substantial text overlap with a published paper by the same authors (self-plagiarism risk).
- A "new" study that re-reports a prior dataset's numbers without a new question.
- Citations exclusively to non-SE venues, signaling the paper may be a visitor rerouted without
  reframing.

## Output format

```text
[Eligibility] clear / needs declaration / risky
[Lanes covered] <flagships / automation-analysis / mining-evolution / journals / adjacent>
[Nearest 3 works] <work -> one-line delta>
[Archival-overlap risk] <none / declare: what>
[Novelty sentence] <FSE-ready contribution contrast against the nearest prior work>
```
