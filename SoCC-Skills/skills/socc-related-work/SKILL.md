---
name: socc-related-work
description: Use when positioning an ACM SoCC submission against both the systems literature (OSDI, NSDI, EuroSys, ATC, SOSP, SoCC) and the data-management literature (SIGMOD, VLDB), writing delta-first contrast rather than a citation catalog, keeping self-citations dual-anonymous, and handling concurrent, preprint, and prior-version overlap.
---

# SoCC Related Work

Use this to audit novelty and eligibility. SoCC reviewers come from **both SIGMOD and SIGOPS**, so a
credible related-work section reaches **both** lanes — the systems flagships and the data-management
flagships — and states where your paper sits relative to the nearest prior work as a **delta**, not
a list. A bibliography that cites only one community tells a reviewer from the other that the paper
may be a visitor. Reopen the current call for dual-submission, anonymity, and prior-publication rules
before advising authors.

## Positioning checks

- **Separate the cloud novelty from the engineering effort.** What is new: a mechanism, a
  measurement, a benchmark, a deployment lesson, or a cost model — and is it new to *both*
  communities or only one?
- **Cover both lanes.** SoCC reviewers expect the systems venues (OSDI/NSDI/EuroSys/ATC/SOSP/SoCC)
  *and* the data venues (SIGMOD/VLDB) where relevant, not just the papers nearest your mechanism.
- **Write delta-first.** Each closely related paper gets one sentence naming what it did and one
  naming what you do differently — not a summary. Position, don't catalog.
- **Preserve dual anonymity.** Cite your own prior work in the third person and never link reviewers
  to an identity-revealing preprint, repository, deployment, or homepage.
- **Declare overlap** with any prior workshop version (e.g., a HotCloud/HotStorage short paper) or
  concurrent submission; do not re-submit archival work as new.

## Cloud literature lanes

| Lane | Typical venues | What SoCC reviewers check |
|---|---|---|
| Systems flagships | OSDI, SOSP, NSDI, EuroSys, ATC, SoCC | Whether the nearest systems mechanism is compared or distinguished |
| Data management | SIGMOD, VLDB, ICDE | Whether the data-systems predecessors (storage, query, transactions) are engaged |
| Cloud + big-data infra | SoCC, VLDB, OSDI | Whether prior resource-mgmt / serverless / big-data-systems work is credited |
| Measurement | IMC, SoCC, SIGMETRICS | Whether prior traces/measurement studies on your workload are acknowledged |
| Adjacent (when relevant) | ML-systems (MLSys), networking | Whether borrowed methods are cited to their real origin |

A bibliography spanning the systems flagships **and** the data flagships signals command of SoCC's
joint field; one that cites only your own subarea suggests the delta may be smaller than claimed.

## Delta-first positioning vignette

Suppose the paper proposes a **tail-aware serverless autoscaler** and a supporting measurement. Its
nearest neighbors: a systems-flagship autoscaler that scales on concurrency (mechanism, no tail
target), a SoCC serverless paper on cold starts (adjacent problem, different lever), and a
data/measurement study of function invocation traces (characterization, no mechanism). The novelty
sentence should name all three contrasts — a tail-SLO controller where the flagship used
concurrency, a provisioning lever where the cold-start paper optimized startup, and a built system
where the measurement study offered only characterization.

## Concurrent and prior-version judgment calls

```text
[Concurrent arXiv work]   cite neutrally, state the technical difference, avoid unverifiable
                          priority claims; keep the citation dual-anonymous
[Your workshop version]   a HotCloud/HotStorage-style short paper is usually citable and
                          non-archival, but confirm against the current CFP and phrase so
                          anonymity survives
[Prior short/poster]      declare the overlap and state what the full paper adds beyond it
[Archival status unclear] declare the overlap in the submission form rather than guessing a
                          chair's interpretation
```

## Eligibility red flags

- Substantial text overlap with a published paper by the same authors (self-plagiarism risk).
- A "new" measurement that re-reports a prior trace's numbers without a new question.
- Citations exclusively to one community (all systems or all data), signaling the paper may be a
  visitor rerouted without reframing for SoCC's joint audience.

## Output format

```text
[Eligibility] clear / needs declaration / risky
[Lanes covered] <systems flagships / data management / cloud-infra / measurement / adjacent>
[Nearest 3 works] <work -> one-line delta>
[Archival-overlap risk] <none / declare: what>
[Novelty sentence] <SoCC-ready contribution contrast against the nearest systems AND data prior work>
```
