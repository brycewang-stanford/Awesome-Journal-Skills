---
name: icde-related-work
description: Use when positioning an IEEE ICDE submission against the database canon and neighboring venues, running a reinvention audit across SIGMOD, VLDB, EDBT, and shipping systems, handling two-round concurrency, distinguishing engineering delta from genuine novelty, and covering both the literature and production systems an ICDE reviewer expects.
---

# ICDE Related Work

Use this to audit novelty and eligibility. Reopen the current call for the original-work and
prior-publication rules before advising authors.

## Positioning checks

- Separate **genuine novelty** (a new mechanism, access method, protocol, or primitive) from
  **engineering delta** (a faster implementation of a known idea). ICDE rewards the former;
  the latter needs an unusually strong evaluation to survive.
- Run a **reinvention audit** against the deep database canon. Because data management has a
  fifty-year literature, a "new" index or join often has a 1980s or 1990s ancestor; find it and
  state the difference, or a reviewer will.
- Cover **both** the research venues **and shipping systems**. ICDE reviewers expect you to know
  the relevant production databases, not just papers; ignoring a system that already does what
  you claim is a recognizable reject pattern.
- Because ICDE is **single-blind**, cite your own prior work directly and link repositories
  freely — there is no anonymity to preserve in the bibliography.
- State overlap with any prior short/workshop version honestly; the original-work rule bars work
  already published beyond a few double-column pages.

## The venue-ring coverage table

| Literature lane | Typical sources | What ICDE reviewers check |
|---|---|---|
| Core database venues | ICDE, SIGMOD, VLDB/PVLDB, EDBT | Whether the nearest system is compared or explicitly distinguished |
| Journals | IEEE TKDE, The VLDB Journal, ACM TODS | Whether the journal-length predecessor of your idea is acknowledged |
| Systems venues | OSDI, SOSP, FAST, ATC | Whether a systems-community mechanism you rebuild is credited |
| Shipping systems | Commercial and open-source databases | Whether a production system already provides your primitive |

A bibliography citing only recent conference papers tells a builder-heavy committee that a
known technique may be getting rediscovered — no throughput number repairs that impression.

## The concurrency question at ICDE

- ICDE's **two-round** calendar and the tight ICDE/SIGMOD/VLDB overlap mean genuinely concurrent
  work is common. For independently concurrent papers, cite neutrally, state the technical
  difference, and avoid priority claims a reviewer cannot check.
- If a near-identical result appeared at a sibling venue between your rounds, address it head-on
  rather than hoping the reviewers missed it — they did not.

## Positioning vignette

A paper proposes a latch-free variant of a classic index. Its nearest neighbors: the original
B-tree literature, a recent SIGMOD lock-free structure, and a production key-value store's
internal index. The novelty sentence must name all three contrasts — a new mechanism the
classic design lacked, a different hardware assumption from the SIGMOD variant, and a capability
the production store does not expose — so the delta is unmistakable.

## Overlap judgment calls

- Your own workshop or short-paper version: usually citable, but confirm it stays under the
  original-work threshold and declare it.
- When unsure whether a prior venue counts as prior publication, declare the overlap in the
  submission form rather than gambling on a chair's reading.

## Output format

```text
[Eligibility] clear / needs declaration / risky
[Novelty type] new-mechanism / engineering-delta
[Closest lanes] <core-DB / journal / systems / shipping-system>
[Nearest 3 works] <work -> specific distinction>
[Reinvention risk] <ancestor found? y/n>
[Novelty sentence] <ICDE-ready contribution contrast>
```
