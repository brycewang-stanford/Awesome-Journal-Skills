---
name: percom-related-work
description: Use when positioning an IEEE PerCom submission against the pervasive/ubiquitous-computing literature across PerCom, ACM UbiComp/IMWUT, MobiCom, MobiSys, SenSys, and IPSN, writing delta-first contrast rather than a citation catalog, keeping self-citations double-blind, and handling concurrent, preprint, and prior-version overlap.
---

# PerCom Related Work

Use this to audit novelty and eligibility. PerCom reviewers are close to the ubicomp literature and
expect to see where your paper sits relative to the nearest prior work — stated as a **delta**, not
a list. Reopen the current call for dual-submission, anonymity, and prior-publication rules before
advising authors.

## Positioning checks

- **Separate the pervasive-computing novelty from the engineering effort.** What is new: a
  recognizer, a sensing modality, a context model, a system, a dataset, or an evidence regime
  (e.g., the first cross-subject / free-living evaluation) nobody had covered?
- **Cover the ubicomp lanes.** PerCom reviewers expect the flagship venues and the IMWUT journal,
  not just the papers nearest your method (see the table). A bibliography missing the obvious
  sibling work reads as unaware.
- **Write delta-first.** Each closely related paper gets one sentence naming what it did and one
  naming what you do differently — not a summary. Position, don't catalog.
- **Preserve double-blindness.** Cite your own prior work in the **third person** (do not omit it),
  and never link reviewers to an identity-revealing preprint, dataset owner, or homepage.
- **Declare overlap** with any prior workshop/WiP version or concurrent submission; do not
  re-submit archival work as new.

## Ubicomp literature lanes

| Lane | Typical venues | What PerCom reviewers check |
|---|---|---|
| Pervasive-computing flagships | IEEE PerCom, ACM UbiComp/IMWUT | Whether the nearest ubicomp recognizer/system/study is compared or distinguished |
| Mobile systems & networking | MobiCom, MobiSys | Whether mobile-systems predecessors are credited (and why yours is human-centric) |
| Networked sensor systems | SenSys, IPSN | Whether prior sensor-platform/sensing work is acknowledged |
| Wearables & activity recognition | ISWC, IMWUT | Whether HAR/wearable predecessors and datasets are engaged |
| Adjacent fields (when relevant) | HCI (CHI), ML venues | Whether borrowed methods are cited to their real origin |

A bibliography that cites only your own subarea tells a reviewer the delta may be smaller than
claimed; one that reaches the flagships, the IMWUT journal, and the relevant datasets signals
command of the field.

## Delta-first positioning vignette

Suppose the paper proposes a **cross-subject** eating-episode recognizer and a released dataset. Its
nearest neighbors: an IMWUT paper on within-subject eating detection (same task, but not
cross-subject), a MobiCom RF-sensing eating study (different modality, infrastructure-bound), and a
prior wrist-HAR dataset (data, no personalization method). The novelty sentence should name all
three contrasts — cross-subject generalization where the IMWUT work stayed within-subject, a
commodity-wearable modality where the RF study needed infrastructure, and a personalization method
plus a new dataset where the prior release offered only data.

## Concurrent and prior-version judgment calls

```text
[Concurrent arXiv work]   cite neutrally, state the technical difference, avoid unverifiable
                          priority claims; keep the citation double-blind
[Your workshop/WiP version] PerCom WiP and workshop papers are short/early -- usually citable, but
                          confirm the current CFP wording and phrase so anonymity survives
[Prior short/poster version] declare the overlap and state what the full paper adds beyond it
[Archival status unclear]  declare the overlap in the submission form rather than guessing a
                          chair's interpretation
```

## Eligibility red flags

- Substantial text overlap with a published paper by the same authors (self-plagiarism risk).
- A "new" recognizer that re-reports a prior dataset's numbers without a new question or split.
- Citations exclusively to non-ubicomp venues, signaling the paper may be a visitor rerouted
  without reframing for a human-centric audience.

## Output format

```text
[Eligibility] clear / needs declaration / risky
[Lanes covered] <ubicomp-flagships / mobile-systems / sensor-systems / wearables-HAR / adjacent>
[Nearest 3 works] <work -> one-line delta>
[Archival-overlap risk] <none / declare: what>
[Novelty sentence] <PerCom-ready contribution contrast against the nearest prior work>
```
