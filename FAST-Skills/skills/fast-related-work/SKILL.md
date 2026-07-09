---
name: fast-related-work
description: Use when positioning a USENIX FAST submission against the storage-systems literature across FAST, OSDI, ATC, SOSP, EuroSys, HotStorage, MSST, and the storage journals (ACM TOS), writing delta-first contrast rather than a citation catalog, keeping self-citations double-blind, and handling concurrent, preprint, and prior-version overlap.
---

# FAST Related Work

Use this to audit novelty and eligibility. FAST reviewers are close to the storage literature and
expect to see where your paper sits relative to the nearest prior work — stated as a **delta**, not a
list. Because many landmark storage systems appeared at OSDI, ATC, SOSP, or EuroSys rather than FAST,
covering the right lanes matters. Reopen the current call for concurrent-submission, anonymity, and
prior-publication rules before advising.

## Positioning checks

- **Separate the storage novelty from the engineering effort.** What is new: a design that exploits a
  media property, a mechanism that removes a storage cost, a measurement method, a reliability
  finding, or an evidence regime nobody had covered on real devices?
- **Cover the storage lanes.** FAST reviewers expect the storage venues *and* the storage-relevant
  systems venues, not just the papers nearest your method (see the table). A bibliography missing the
  obvious OSDI/ATC/SOSP predecessor reads as unaware.
- **Write delta-first.** Each closely related system gets one sentence naming what it did and one
  naming what you do differently — often the delta is a storage quantity (it cut reads but paid write
  amplification; it worked in simulation but not on real flash). Position, don't catalog.
- **Preserve double-blind.** Cite your own prior work in the third person and never link reviewers to
  an identity-revealing preprint, repository, homepage, or trace host.
- **Declare overlap** with any prior workshop (e.g. HotStorage) version or concurrent submission; do
  not re-submit archival work as new.

## Storage literature lanes

| Lane | Typical venues | What FAST reviewers check |
|---|---|---|
| Storage flagship | FAST | Whether the nearest storage design/study is compared or distinguished |
| Storage-relevant systems | OSDI, ATC, SOSP, EuroSys | Whether a landmark storage system from a systems venue is credited |
| Storage workshops | HotStorage, MSST | Whether the early or engineering-track predecessor is acknowledged |
| Storage / systems journals | ACM TOS, ACM TOCS | Whether deeper journal-length treatments are engaged |
| Adjacent fields (when relevant) | Architecture (MICRO/ISCA), DB (VLDB/SIGMOD) | Whether borrowed device or workload models are cited to their origin |

A bibliography that cites only your own subarea tells a reviewer the delta may be smaller than
claimed; one that reaches the systems flagships and the storage journals signals command of the
field.

## Delta-first positioning vignette

Suppose the paper proposes an endurance-aware LSM compaction scheduler. Its nearest neighbors: the
key/value-separation FAST design (cut amplification via layout, not scheduling), an OSDI LSM system
(tuned for reads, write cost unaddressed), and a HotStorage note proposing endurance-aware ideas
without an implementation. The novelty sentence should name all three contrasts — scheduling where
one changed layout, endurance-optimization where another optimized reads, and a real-device
evaluation where the workshop note had none.

## Concurrent and prior-version judgment calls

```text
[Concurrent arXiv work]   cite neutrally, state the technical/storage-metric difference, avoid
                          unverifiable priority claims; keep the citation double-blind
[Your HotStorage version] workshop notes are usually non-archival and citable, but confirm against
                          the current CFP wording and phrase so anonymity survives
[Prior short/poster]      declare the overlap and state what the full paper adds beyond it
[Archival status unclear] declare the overlap in the submission form rather than guessing
```

## Eligibility red flags

- Substantial text overlap with a published paper by the same authors (self-plagiarism risk).
- A "new" study that re-reports a prior dataset's numbers without a new storage question.
- Citations exclusively to non-storage venues, signaling the paper may be a systems/architecture/DB
  paper rerouted without reframing its storage core.

## Output format

```text
[Eligibility] clear / needs declaration / risky
[Lanes covered] <storage flagship / systems venues / workshops / journals / adjacent>
[Nearest 3 works] <work -> one-line storage-metric delta>
[Archival-overlap risk] <none / declare: what>
[Novelty sentence] <FAST-ready contribution contrast against the nearest prior storage work>
```
