---
name: vldb-writing-style
description: Use when revising a PVLDB paper's prose, covering the page-one contract for systems readers, scoping performance claims to measured regimes, stating design trade-offs instead of hiding them, terminology and notation discipline across a 12-page budget, and the tone VLDB's builder-reviewers reward.
---

# VLDB Writing Style

Use this during revision passes. The PVLDB reader is a systems builder
deciding, inside the first page, whether your design decision is worth their
evening. Style at this venue is not ornament — it is claim hygiene.

## The page-one contract

By the end of page one the reader must know:

1. **The workload that breaks current systems** — concrete, not "growing data
   volumes."
2. **The design decision** — the bet your system makes that others do not.
3. **What was built** — real system, extension of a named engine, or
   simulation; readers calibrate trust to this immediately.
4. **The headline measurement, scoped** — metric, scale, baseline, hardware
   class, all in one sentence.

A running example introduced early and reused through design and evaluation
sections is the genre's most effective device; pick one query, one tenant, one
failure trace and let it carry the mechanism.

## Claim scoping table

| Unscoped (review bait) | Scoped (survives) |
|---|---|
| "significantly faster than X" | "2.1x median speedup over X (v3.4, tuned per §6.1) on workload W at 1TB" |
| "scales to large clusters" | "near-linear to 64 nodes; efficiency drops to 71% at 128 (Fig. 9)" |
| "negligible overhead" | "adds 3-5% CPU on write-heavy YCSB-A; worst case 11% at 99% writes" |
| "state-of-the-art performance" | delete; name the systems and the regime |

Every superlative either gains a number, a workload, and a baseline — or dies.

## Trade-off candor

Systems reviewers assume every design pays somewhere. A paper that never says
what its mechanism costs reads as unmeasured, not as flawless.

- State the price of the design in the introduction (memory, write path
  latency, generality) and point to the section that measures it.
- Put the loss cases in the main evaluation, not a footnote: the workload
  where the baseline wins is your credibility purchase.
- Prefer "we chose A over B because C, accepting cost D" over passive
  descriptions that hide the decision.

## Budget and terminology discipline

- One name per concept for all 12 pages: a "segment" on page 3 cannot become
  a "chunk" on page 9. Builder-readers parse terminology as architecture.
- Architecture figure by page 3; reviewers reconstruct systems visually.
- Since references are uncapped but appendices are not, spend prose on
  mechanism and measurement, and let citations carry the history compactly.
- Single-blind means writing "we extend our earlier system [12]" is fine —
  clarity about lineage beats coy third-person contortions.

## Self-edit sweep

```text
grep-worthy passes before submission:
  "significant"      -> replace with the number or delete
  "novel"            -> the contribution list should prove it instead
  "to the best of our knowledge" -> keep at most one, verified
  "very large"       -> state the size
  passive "was designed" -> name the decision and its reason
  every Figure N     -> referenced in text, at least one sentence of reading
```

## Output format

```text
[Page-one contract] met / missing elements listed
[Unscoped claims] <count, worst three quoted>
[Trade-off candor] price stated in intro? loss cases in eval?
[Terminology drift] <concept -> competing names found>
[Running example] present / absent (suggested candidate)
[Edit order] <highest-leverage rewrites first>
```
