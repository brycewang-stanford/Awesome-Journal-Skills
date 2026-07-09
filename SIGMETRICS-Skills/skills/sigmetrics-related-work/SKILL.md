---
name: sigmetrics-related-work
description: Use when positioning an ACM SIGMETRICS submission against the performance-evaluation literature across SIGMETRICS/POMACS, Performance Evaluation, QUESTA, TON, and the systems/learning/measurement neighbors (NSDI/OSDI, IMC, NeurIPS/ICML), writing delta-first contrast rather than a citation catalog, keeping self-citations double-anonymous, and handling concurrent and prior-version overlap.
---

# SIGMETRICS Related Work

Use this to audit novelty and eligibility. SIGMETRICS reviewers are close to the
performance-evaluation literature and expect to see where your paper sits relative to the nearest
prior model, bound, or measurement — stated as a **delta**, not a list. Reopen the current call for
the simultaneous-submission and prior-publication rules (a paper under one-shot revision counts as
under submission) before advising authors.

## Positioning checks

- **Separate the analytic/measurement novelty from the engineering effort.** What is new: a tighter
  bound, a more general model, a policy that provably beats a known one, a measurement of a system
  nobody had characterized, or a learning algorithm with a new guarantee?
- **Cover the performance-evaluation lanes** (see the table), not just the papers nearest your
  method. A bibliography missing the obvious queueing-theory predecessor or the prior measurement of
  the same system reads as unaware.
- **Write delta-first.** Each closely related paper gets one sentence naming what it did and one
  naming what you do differently — a tighter bound, a weaker assumption, a broader policy class, a
  larger/newer measurement — not a summary.
- **Preserve double-anonymity.** Cite your own prior work in the third person and never link
  reviewers to an identity-revealing preprint, system page, or repository (Operational Systems Track
  excepted).
- **Declare overlap** with any prior conference/workshop version or concurrent submission; do not
  re-submit archival work as new.

## Performance-evaluation literature lanes

| Lane | Typical venues | What SIGMETRICS reviewers check |
|---|---|---|
| Core performance evaluation | SIGMETRICS/POMACS, Performance Evaluation, QUESTA | Whether the nearest model/bound/measurement is compared or distinguished |
| Systems (when you claim a systems payoff) | NSDI, OSDI, SIGCOMM, ATC | Whether the system you improve/measure is credited and fairly baselined |
| Measurement | IMC, PAM, INFOCOM | Whether prior measurements of the same system/workload are engaged |
| Learning (Learning track) | NeurIPS, ICML, COLT | Whether the learning-theoretic predecessor (regret bounds, algorithms) is cited to its origin |
| Networking/queueing journals | IEEE/ACM TON, QUESTA, Stochastic Models | Whether deeper journal-length analyses of the model are engaged |

A bibliography that cites only your own subarea tells a reviewer the delta may be smaller than
claimed; one that reaches the neighboring theory, systems, and measurement venues signals command of
the field.

## Delta-first positioning vignette

Suppose the paper proves a tail-latency bound for a rank-based scheduler. Its nearest neighbors: a
prior analysis of a single age-based policy (one policy, mean latency), a general scheduling
framework (broad class, but no tail bound), and a measurement study of the target system (data, no
policy analysis). The novelty sentence should name all three contrasts — a **tail** bound where the
single-policy analysis gave only mean, a **provable tail guarantee** where the framework gave none,
and a **policy with analysis** where the measurement gave only characterization.

## Concurrent and prior-version judgment calls

```text
[Concurrent arXiv work]   cite neutrally, state the technical difference (tighter bound? weaker
                          assumption? newer measurement?), avoid unverifiable priority claims;
                          keep the citation double-anonymous
[Your workshop version]   usually non-archival and citable, but confirm against the current call
                          wording and phrase so anonymity survives
[Prior short version]     declare the overlap and state what the full paper adds (proofs, validation)
[Paper under one-shot revision] it is under submission to SIGMETRICS -- do not submit it elsewhere
                          before withdrawing
```

## Eligibility red flags

- Substantial text/result overlap with a published paper by the same authors (self-plagiarism risk).
- A "new" analysis that re-derives a known bound without a tighter result or weaker assumption.
- Citations exclusively to non-performance-evaluation venues, signaling the paper may be a systems
  or learning paper rerouted without reframing.

## Output format

```text
[Eligibility] clear / needs declaration / risky
[Lanes covered] <performance-eval / systems / measurement / learning / journals>
[Nearest 3 works] <work -> one-line delta (tighter bound / weaker assumption / broader class / newer data)>
[Archival-overlap risk] <none / declare: what>
[Novelty sentence] <SIGMETRICS-ready contribution contrast against the nearest prior work>
```
