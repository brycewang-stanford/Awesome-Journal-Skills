---
name: eurosys-related-work
description: Use when positioning a EuroSys submission in the systems literature — mapping the SOSP/OSDI/NSDI/ATC/ASPLOS neighbor space plus EuroSys's own two-decade proceedings line, handling concurrent arXiv and workshop versions under double-blind rules, and declaring overlap with earlier submissions of the same work.
---

# EuroSys Related Work

Use this to audit novelty positioning before the abstract gate. EuroSys sits
inside a tightly interconnected systems publication circuit; its reviewers
usually know the neighboring venues' recent programs from memory, and the free
reference pages (EuroSys 2027 CFP, rendered 2026-07-08) remove every excuse
for thin citation.

## Search the circuit, not just the venue

| Lane | Venues to sweep | What EuroSys reviewers check |
|---|---|---|
| OS / systems flagships | SOSP, OSDI, EuroSys itself, ATC | Is the nearest mechanism acknowledged and differenced? |
| Networked systems | NSDI, SIGCOMM | Does a networking result already give the win? |
| Architecture boundary | ASPLOS, ISCA/MICRO when relevant | Is the contribution actually a hardware technique? |
| Storage / data | FAST, VLDB/SIGMOD systems tracks | Trace and workload lineage; storage-stack priors |
| Cloud / middleware | SoCC, Middleware | Prior managed-service and runtime designs |
| Fast-moving preprints | arXiv systems + ML-systems feeds | Concurrent designs with the same insight |

EuroSys's own back catalog deserves a dedicated pass — the venue has run since
2006 (`dblp.org/db/conf/eurosys/`), and missing a EuroSys paper at EuroSys is
the most avoidable reviewer annoyance available. Sweep dblp by topic keyword
across at least the last five editions.

## Differencing, the systems way

A EuroSys related-work paragraph earns its space when it states a *technical*
delta, not a topical one:

- Wrong: "Unlike prior caching systems, we consider LLM serving."
- Right: "System X also reuses KV state across requests, but requires prefix
  identity; our fusion step lifts that restriction at the cost of a bounded
  recomputation, which §5 quantifies."

Each of the three to five nearest systems gets: what it does, the assumption
or regime where it stops, and the measurement in your paper that exploits
exactly that gap. If no measurement exploits the gap, either add the
comparison or soften the claim.

## Same-work lineage under EuroSys rules

```text
Decision ladder for earlier versions of this work:
1. Workshop paper (short, non-archival systems workshop)?
   -> usually fine to build on; cite it in third person, do not claim it.
      Confirm the current CFP's wording on prior publication. (待核实 per round)
2. arXiv preprint by the authors?
   -> double-blind survives if the paper does not point at it; do not cite
      your own preprint in a way that de-anonymizes.
3. Prior EuroSys submission of this paper?
   -> rejected at a round: barred until the same round next edition;
      revision offer: this is a resubmission with a condition list, not a
      fresh submission — follow eurosys-author-response.
4. Under review elsewhere right now?
   -> dual submission to another archival venue is prohibited. Full stop.
```

Concurrent third-party work discovered late: cite it, mark it concurrent, and
difference on substance; reviewers respect visible honesty about a photo-finish
far more than silence they then discover themselves.

## Section architecture that works in 1.5 pages

- Organize by *problem dimension*, not by venue or by chronology: one
  paragraph per axis on which systems differ (e.g., what is deferred, what
  is preempted, what information the scheduler sees), with your system
  placed on each axis.
- Lead each paragraph with the axis, not with a system name; reviewers
  scan topic sentences to check whether their own axis is covered.
- Close with the two-sentence synthesis: the combination of positions no
  prior system occupies, and why that combination required a new design
  rather than configuration.
- Keep per-system verdicts consistent with the evaluation section — a
  system dismissed in related work but absent from the baselines is a
  contradiction reviewers notice immediately.
- Resist the completeness urge: fifteen precise contrasts beat forty
  drive-by citations, and the free reference pages already prove you read
  the field.

## Positioning traps specific to this venue

- Comparing only against US-flagship papers while ignoring the European
  systems groups whose members densely populate the EuroSys PC.
- Treating an industrial system's blog post as uncitable — production systems
  are first-class citizens in systems related work; cite the best available
  description.
- Spending the section proving breadth of reading instead of sharpening the
  delta; EuroSys reviewers grade the *contrast*, not the citation count.

## Verification recipe before claiming a citation

Systems folklore mis-shelves famous papers constantly (the pack's
exemplars library keeps a do-not-misattribute list). Before asserting
"X appeared at venue Y" in the paper:

1. Find the entry in dblp and read the venue off the proceedings record.
2. Confirm the DOI resolves to that venue's proceedings.
3. Cite the archival version, not the arXiv mirror, unless the arXiv
   version is the only one or is materially different.
4. When two versions exist (workshop then conference), cite the one whose
   content supports your specific claim.

## Output format

```text
[Nearest neighbors] <3-5 systems, each with its stopping assumption>
[Delta -> evidence] <each claimed difference and the section that measures it>
[Circuit coverage] <lanes swept, incl. EuroSys back catalog via dblp>
[Lineage declaration] <workshop/arXiv/prior-round/dual-submission status>
[Gaps to fix] <missing comparisons or unsupported deltas>
```
