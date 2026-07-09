---
name: ipsn-related-work
description: Use when positioning an IPSN-lineage submission against the sensor-networks and information-processing literature (IPSN, SenSys, MobiCom, MobiSys, INFOCOM, and signal-processing venues), writing delta-first contrast rather than a citation catalog, keeping self-citations double-blind, and handling concurrent, preprint, and prior-version overlap.
---

# IPSN Related Work

Use this to audit novelty and eligibility. IPSN reviewers span two literatures — the sensor-systems
world (IPSN/SenSys/MobiCom/MobiSys/INFOCOM) and the information-processing/signal-processing world —
and they expect to see where your paper sits relative to the nearest prior work, stated as a
**delta**, not a list. Because IPSN merged into SenSys, reopen the current successor call for
dual-submission, anonymity, and prior-publication rules before advising.

## Positioning checks

- **Separate the sensing/information-processing novelty from the engineering effort.** What is new:
  a new estimator, a new platform, a new measurement, a new deployment regime, or an on-device
  method nobody had made fit?
- **Cover both lanes.** An IP-track paper still owes the systems lane (has a sensor system done this
  end-to-end?) and the theory lane (is there an estimation/SP result you must cite?). A SPOTS paper
  owes the platform and tools lineage. A bibliography missing the obvious sibling work reads as
  unaware.
- **Write delta-first.** Each closely related paper gets one sentence naming what it did and one
  naming what you do differently — not a summary. Position, don't catalog.
- **Preserve double-blind.** Cite your own prior work in the third person; never link reviewers to an
  identity-revealing preprint, firmware repo, dataset DOI, or homepage.
- **Declare overlap** with any prior workshop/short version or concurrent submission; do not
  re-submit archival work as new.

## Sensing/IP literature lanes

| Lane | Typical venues | What IPSN reviewers check |
|---|---|---|
| Sensor systems flagships | IPSN, SenSys | Whether the nearest end-to-end sensing system is compared or distinguished |
| Mobile/ubiquitous sensing | MobiCom, MobiSys, UbiComp | Whether mobile/wearable predecessors of your modality are credited |
| Networking / measurement | INFOCOM, NSDI | Whether protocol/throughput/measurement predecessors are engaged |
| Information processing / SP | IEEE TSP, ICASSP, SP journals | Whether the estimation/signal-processing result you build on is cited to its origin |
| CPS-IoT Week neighbors | RTAS, ICCPS, HSCC | Whether timing/control/CPS work you border is acknowledged when relevant |

A bibliography that cites only your own subarea tells a reviewer the delta may be smaller than
claimed; one that reaches both the systems flagships and the signal-processing origin signals command
of the field.

## Delta-first positioning vignette

Suppose the paper proposes an on-device acoustic-event detector with an energy budget. Its nearest
neighbors: a SenSys system that detects the same event but wakes the main processor often (systems,
energy-costly), an ICASSP model with high offline accuracy but no on-device story (SP, not deployed),
and an IPSN localization-style cascade idea (related mechanism, different task). The novelty sentence
should name all three contrasts — an energy-bounded cascade where the systems work spent power
freely, an on-device realization where the SP work stayed offline, and a new task where the cascade
idea was applied elsewhere.

## Concurrent and prior-version judgment calls

```text
[Concurrent arXiv work]   cite neutrally, state the technical difference, avoid unverifiable
                          priority claims; keep the citation double-blind
[Your workshop version]   often non-archival and citable, but confirm against the current CFP and
                          phrase so anonymity survives
[Prior poster/demo]       declare the overlap and state what the full paper adds beyond it
[Dataset re-use]          if you reuse a public dataset, cite it and state what is new; a re-report
                          of old numbers with no new question is not a contribution
```

## Eligibility red flags

- Substantial text/result overlap with a published paper by the same authors (self-plagiarism risk).
- A "new" deployment that re-reports a prior dataset's numbers without a new sensing question.
- Citations exclusively to pure-ML or pure-networking venues, signaling a visitor rerouted without
  reframing to the sensing/information-processing contribution.

## Output format

```text
[Eligibility] clear / needs declaration / risky
[Lanes covered] <sensor-systems / mobile-sensing / networking / signal-processing / CPS-neighbors>
[Nearest 3 works] <work -> one-line delta>
[Archival-overlap risk] <none / declare: what>
[Novelty sentence] <IPSN-ready contribution contrast against the nearest prior work, both lanes>
```
