---
name: pods-related-work
description: Use when positioning an ACM PODS submission against the database-theory literature across PODS, ICDT, LICS, and the journals (TODS, LMCS, JACM, VLDBJ), writing delta-first contrast that compares results rather than cataloging citations, keeping self-citations double-anonymous, and handling concurrent, arXiv-preprint, and prior-version overlap.
---

# PODS Related Work

Use this to audit novelty and eligibility. PODS reviewers are close to the database-theory literature
and expect to see exactly where your **result** sits relative to the nearest prior **result** — a
comparison of theorems, not a list of papers. Reopen the current PODS call for the resubmission,
anonymity, and prior-publication rules before advising authors.

## Positioning checks

- **Separate the mathematical novelty from the effort.** What is new: a bound that was open, a
  dichotomy that completes a partial classification, a semantics nobody had defined, a lower bound
  matching a known upper bound? Name the theorem-level delta.
- **Cover the theory lanes.** PODS reviewers expect the database-theory venues *and* the relevant
  logic/complexity literature, not only the papers nearest your technique (see the table). A
  bibliography missing the obvious prior classification reads as unaware.
- **Write delta-first at the level of results.** Each closely related paper gets one sentence naming
  what it *proved* and one naming how your result differs — a stronger bound, a broader class, a
  matching lower bound, a removed assumption. Compare theorems, do not summarize abstracts.
- **Preserve lightweight double-anonymity.** Cite your own prior work in the third person and never
  link reviewers to an identity-revealing arXiv preprint, homepage, or named system.
- **Declare overlap** with any prior conference/workshop version, an ICDT/journal version, or a
  concurrent submission; do not re-submit an already-published theorem as new.

## Database-theory literature lanes

| Lane | Typical venues | What PODS reviewers check |
|---|---|---|
| Database theory (symposia) | PODS, ICDT | Whether the nearest prior bound/dichotomy/semantics is compared or subsumed |
| Logic & finite model theory | LICS, ICALP, CSL | Whether the logical tools and expressiveness results are credited to origin |
| Complexity (when a bound rests on it) | STOC, FOCS, CCC | Whether the complexity-theoretic assumption (ETH, OMv, #P) is stated correctly |
| Theory journals | TODS, LMCS, JACM, VLDBJ | Whether the full/journal treatment of a topic is engaged, not just the extended abstract |
| Systems DB (when relevant) | SIGMOD, VLDB, ICDE | Whether a practically motivated problem's systems context is acknowledged |

A bibliography that cites only your own thread of papers tells a reviewer the delta may be smaller than
claimed; one that reaches ICDT, the logic venues, and the journal versions signals command of the field.

## Delta-first positioning vignette

Suppose the paper proves a **dichotomy** for a query-evaluation problem. Its nearest neighbors: an
earlier paper giving tractability for a *sub*-class (positive, but not a classification), a hardness
result for one *specific* query (negative, but isolated), and a journal survey conjecturing the
boundary. The novelty sentence should name all three contrasts — a *complete* classification where the
first had only a sub-class, a *general* lower bound where the second had one query, and a *proof* where
the survey had a conjecture.

## Concurrent and prior-version judgment calls

```text
[Concurrent arXiv work]  cite neutrally, state the precise result-level difference, avoid
                         unverifiable priority claims; keep the citation double-anonymous
[Your ICDT/workshop ver] declare it; state what the PODS paper adds (a matching lower bound, the
                         general case, full proofs) beyond the earlier extended abstract
[Journal full version]   if a journal version exists or is in submission, disclose it; PODS is an
                         extended abstract venue and overlap must be stated
[Archival status unclear] declare the overlap in the submission rather than guessing a chair's reading
```

## Eligibility red flags

- Substantial overlap with a theorem already published by the same authors (self-plagiarism / double
  publication risk).
- A "new" result that re-proves a known bound with a cosmetic change of model and no new consequence.
- Citations exclusively to systems venues, signaling a paper that may be a systems result reframed
  without the theory a PODS reviewer expects.

## Output format

```text
[Eligibility] clear / needs declaration / risky
[Lanes covered] <db-theory / logic-FMT / complexity / journals / systems-when-relevant>
[Nearest 3 results] <prior result -> one-line theorem-level delta>
[Archival-overlap risk] <none / declare: which prior version>
[Novelty sentence] <PODS-ready contribution contrast against the nearest prior theorem>
```
