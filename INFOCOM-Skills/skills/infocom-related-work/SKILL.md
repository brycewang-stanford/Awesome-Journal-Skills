---
name: infocom-related-work
description: Use when positioning an IEEE INFOCOM submission against the networking literature across INFOCOM, SIGCOMM, NSDI, MobiCom, ICNP, and the journals (IEEE/ACM ToN, IEEE JSAC/TMC), writing delta-first contrast rather than a citation catalog, keeping self-citations double-blind on EDAS, and handling concurrent, preprint, and prior-version overlap.
---

# INFOCOM Related Work

Use this to audit novelty and eligibility. INFOCOM reviewers are close to the networking literature
across both its analytical and systems wings, and they expect to see where your paper sits relative
to the nearest prior work — stated as a **delta**, not a list. Reopen the current call for
dual-submission, double-blind, and prior-publication rules before advising authors.

## Positioning checks

- **Separate the networking novelty from the engineering effort.** What is new: a formulation, a
  bound/guarantee, a protocol/mechanism, a measurement finding, or an evidence regime nobody had
  covered? A faster implementation of a known scheme is not, by itself, an INFOCOM contribution.
- **Cover the networking lanes.** INFOCOM reviewers expect the flagships and the journals, not just
  the papers nearest your method (see the table). A bibliography missing the obvious sibling work
  reads as unaware in a crowded pool.
- **Write delta-first.** Each closely related paper gets one sentence naming what it did and one
  naming what you do differently — not a summary. Position, don't catalog.
- **Preserve double-blind.** Cite your own prior work in the **third person** and never link
  reviewers to an identity-revealing preprint, repository, or homepage.
- **Declare overlap** with any prior workshop/short version or concurrent submission; do not
  re-submit archival work as new.

## Networking literature lanes

| Lane | Typical venues | What INFOCOM reviewers check |
|---|---|---|
| Broad networking flagship | INFOCOM, IEEE ICC/GLOBECOM | Whether the nearest broad networking technique/study is compared or distinguished |
| Systems networking | ACM SIGCOMM, USENIX NSDI | Whether the built-system predecessor and its deployment claims are engaged |
| Wireless/mobile | ACM MobiCom/MobiSys, IEEE ICNP | Whether wireless/protocol predecessors are credited |
| Theory & optimization | ACM SIGMETRICS, IEEE/ACM ToN theory papers | Whether the modeling/optimization lineage is cited to its origin |
| Networking journals | IEEE/ACM ToN, IEEE JSAC, IEEE TMC | Whether deeper journal-length treatments of the topic are engaged |

A bibliography that cites only your own subarea tells a reviewer the delta may be smaller than
claimed; one that reaches the sibling flagships and the journals signals command of the field.

## Delta-first positioning vignette

Suppose the paper proposes an online scheduling algorithm for edge offloading with a competitive
ratio. Its nearest neighbors: an INFOCOM optimization paper on static offloading (offline, no
online guarantee), a SIGCOMM system that offloads with a heuristic (built and measured, no bound),
and a ToN queueing analysis of edge delay (analysis, different objective). The novelty sentence
names all three contrasts — an online guarantee where the first was offline, a provable ratio where
the system had only a heuristic, and a scheduling objective where the journal analyzed delay.

## Concurrent and prior-version judgment calls

```text
[Concurrent arXiv work]   cite neutrally, state the technical difference, avoid unverifiable
                          priority claims; keep the citation double-blind
[Your workshop version]   usually citable, but confirm against the current CFP wording and phrase
                          so anonymity survives; state what the full paper adds
[Prior short/poster]      declare the overlap and state the delta beyond it
[Archival status unclear] declare the overlap in EDAS rather than guessing a chair's interpretation
```

## Eligibility red flags

- Substantial text overlap with a published paper by the same authors (self-plagiarism risk).
- A "new" result that re-reports a prior model's numbers without a new question or guarantee.
- Citations exclusively to non-networking venues, signaling a paper rerouted without reframing for
  the networking reader.

## Output format

```text
[Eligibility] clear / needs declaration / risky
[Lanes covered] <flagship / systems / wireless / theory-optimization / journals>
[Nearest 3 works] <work -> one-line delta>
[Archival-overlap risk] <none / declare: what>
[Novelty sentence] <INFOCOM-ready contribution contrast against the nearest prior work>
```
