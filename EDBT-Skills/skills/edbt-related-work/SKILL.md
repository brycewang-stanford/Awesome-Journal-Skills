---
name: edbt-related-work
description: Use when positioning an EDBT submission against the data-management literature across SIGMOD, VLDB/PVLDB, ICDE, EDBT, the co-located ICDT, and the database journals (VLDBJ, TODS, TKDE), writing delta-first contrast rather than a citation catalog, and handling the 12-month EDBT resubmission ban, preprints, and prior-version overlap.
---

# EDBT Related Work

Use this to audit novelty and eligibility. EDBT reviewers are close to the data-management
literature and expect to see where your paper sits relative to the nearest prior work — stated as a
**delta**, not a list. Reopen the current call for the resubmission-ban wording, the blind policy,
and dual-submission rules before advising authors.

## Positioning checks

- **Separate the database contribution from the engineering effort.** What is new: a mechanism, a
  scalable algorithm, an empirical/benchmarking finding, an abstraction, or an evaluation regime
  nobody had covered?
- **Cover the data-management lanes.** EDBT reviewers expect the flagship venues and the journals,
  not just the papers nearest your method (see the table). A bibliography missing the obvious SIGMOD
  or VLDB predecessor reads as unaware.
- **Write delta-first.** Each closely related paper gets one sentence naming what it did and one
  naming what you do differently — not a summary. Position, don't catalog.
- **Mind the EDBT/ICDT boundary.** If you cite theory results, cite them to **ICDT** (or the theory
  literature) correctly; do not blur a co-located theory paper into an EDBT systems lineage, and do
  not claim a theory contribution your systems paper does not make.
- **Declare overlap** with any prior workshop/short version or concurrent submission; do not
  re-submit archival work as new.

## Data-management literature lanes

| Lane | Typical venues | What EDBT reviewers check |
|---|---|---|
| DB-systems flagships | SIGMOD, VLDB/PVLDB, ICDE, EDBT | Whether the nearest systems technique/study is compared or distinguished |
| Database theory | ICDT, PODS | Whether borrowed theoretical results are credited to their real origin |
| Specialized / applied | e.g. spatial, temporal, graph, streaming, data-integration venues | Whether prior work on your specific data type or task is acknowledged |
| Database journals | VLDBJ, TODS, TKDE | Whether deeper journal-length treatments of the topic are engaged |
| Adjacent fields (when relevant) | ML, IR, systems (OSDI/SOSP), HPC | Whether methods borrowed from outside DB are cited to their origin |

A bibliography that cites only your own subarea tells a reviewer the delta may be smaller than
claimed; one that reaches the flagships and journals signals command of the field.

## Delta-first positioning vignette

Suppose the paper proposes an adaptive skew-handling operator for distributed joins. Its nearest
neighbors: a flagship paper on static skew-aware partitioning (plan-time, no runtime adaptation), a
journal study characterizing skew prevalence in real workloads (measurement, no operator), and a
streaming system with dynamic repartitioning (different setting, full-reshuffle cost). The novelty
sentence should name all three contrasts — runtime adaptation where the flagship was plan-time,
a mechanism where the journal offered only characterization, and selective re-splitting where the
streaming system reshuffled everything.

## The 12-month resubmission ban and prior-version calls

```text
[EDBT resubmission ban]   work rejected/withdrawn from an EDBT track cannot return to any EDBT
                          track in the SAME paper format for 12 months; confirm status before
                          citing/relying on the earlier version
[Concurrent arXiv work]   cite neutrally, state the technical difference; if the cycle is
                          double-blind, keep the citation anonymous
[Your workshop/short ver] usually citable, but declare the overlap and state what the full paper
                          adds; confirm against the current CFP
[Prior demo/vision]       an EDBT demo or Vision paper on the idea is not the full paper; declare
                          it and state the delta
[Archival status unclear]  declare the overlap in the submission form rather than guessing a
                          chair's interpretation
```

## Eligibility red flags

- Substantial text overlap with a published paper by the same authors (self-plagiarism risk).
- Re-reporting a prior system's numbers without a new mechanism, workload, or question.
- Work still inside the 12-month EDBT same-format resubmission cooldown.
- Citations exclusively to non-DB venues, signaling the paper may be a visitor rerouted without
  reframing — naturalize the framing for a database audience first.

## Output format

```text
[Eligibility] clear / needs declaration / risky (resubmission ban?)
[Lanes covered] <systems flagships / theory / specialized / journals / adjacent>
[Nearest 3 works] <work -> one-line delta>
[EDBT/ICDT boundary] <theory cited to its real origin? yes/no>
[Archival-overlap risk] <none / declare: what>
[Novelty sentence] <EDBT-ready contribution contrast against the nearest prior work>
```
