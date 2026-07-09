---
name: icde-writing-style
description: Use when revising an IEEE ICDE paper for the first-page data-engineering contract, a reconstructable mechanism description, the running-example device, performance claims scoped to the workloads actually run, single-blind first-person phrasing, and 12-page IEEE two-column compression that survives a builder-heavy program committee.
---

# ICDE Writing Style

Use this when revising the main paper. ICDE papers must state, compactly, what
data-engineering primitive is new and give a builder enough to reconstruct it, all inside a
tight IEEE two-column budget.

## Revision rules

- Put the **data-engineering contribution on the first page**: the bottleneck, why current
  systems fall short, the mechanism, the measured evidence, and who can build on it.
- Name the **bottleneck and the operating point**. A systems claim without a workload,
  hardware, and cost metric is unfalsifiable and reads as marketing to an ICDE reviewer.
- Make the **mechanism reconstructable**. The reader should be able to rebuild the core idea
  from the body; "a novel structure" is not a mechanism.
- Pair every performance claim with a **figure, table, or measured crossover**, and disclose
  the **cost** of every gain — ICDE reviewers distrust a win with no accounting.
- Use a **running example** (one concrete workload) introduced early and reused; it carries
  intuition through the paper more efficiently than repeated abstraction.
- Because ICDE is **single-blind**, write in natural first person and cite your own prior work
  directly — do not perform the anonymity contortions a double-blind venue requires.

## Mechanism-presentation discipline

- State the **one idea** in a single sentence before the details ("move ordering off the write
  path"). Everything else is elaboration.
- Give the algorithm as pseudocode or a labeled figure, then walk it on the running example;
  builders read the walk, not the prose.
- Keep **problem-dependent costs visible** — write amplification, memory overhead, tail
  latency; silently omitting the cost of a mechanism is a standing ICDE complaint.
- Define notation and system parameters once, in one place; two-column pages punish redundant
  redefinition.
- Separate **what is measured** from **what is argued**; label conjecture as conjecture.

## Sentence-level rewrites

| Draft pattern | ICDE-safe rewrite |
|---|---|
| "Our system is much faster..." | "sustains 1.2M inserts/s where the LSM baseline stalls above 0.9M (Fig. 4)" |
| "Under realistic workloads..." | "On the fleet-telemetry trace and a swept append-to-scan generator..." |
| "A novel index structure..." | "A two-tier index that defers ordering to read time" |
| "Achieves state-of-the-art..." | Claim scoped to the workloads and hardware actually tested |
| "With negligible overhead..." | "at a memory cost of X and a median read-latency factor of Y (Table 3)" |

## Vignette: compressing into 12 IEEE two-column pages

A draft with a full protocol, six figures, and a sprawling related-work section: keep the
mechanism, the pseudocode, the two decision-critical figures (the throughput plot and the
cost/crossover plot), and the ablation that isolates the mechanism. Compress related work into
contrast sentences, and move secondary sweeps, full trace documentation, and extra baselines to
the supplement with explicit forward references. The test of a good cut: a reviewer can
reconstruct the system and believe the headline number without opening the supplement.

## Output format

```text
[Writing diagnosis] clear / under-specified / overclaimed / overloaded
[First-page fix] <new framing: bottleneck -> mechanism -> evidence>
[Claim discipline] <claim -> figure/table/crossover, with cost disclosed>
[Mechanism clarity] <is the one idea reconstructable? gap if not>
[Compression cuts] <move / delete / merge to fit 12 pages>
```
