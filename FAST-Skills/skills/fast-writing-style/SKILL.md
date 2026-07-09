---
name: fast-writing-style
description: Use when revising a USENIX FAST paper for a storage contribution on the first page, a design/mechanism narrative a storage reviewer can follow, an evaluation framed as the storage cost it changes (write amplification, tail latency, endurance, crash consistency), double-blind wording, and disciplined use of the USENIX two-column page budget.
---

# FAST Writing Style

Use this when revising the main paper. FAST papers are read by storage systems people, so they need
a **storage contribution stated on the first page** and an evaluation a storage reviewer trusts. The
failure this skill prevents is a technically fine paper that reads like a general systems demo or a
throughput-bar benchmark with "storage" in the title.

## Revision rules

- **Lead with the storage contribution:** the storage problem a practitioner recognizes, the
  *storage cost* current designs pay (write amplification, tail latency, endurance, space, or a
  consistency gap), your design or finding, real-device evidence, and what changes for storage
  systems.
- **Frame the evaluation as a cost you change, not a speed you win.** State up front which storage
  quantity the paper moves; a reader should know by the end of the intro whether the headline is
  bytes-written, p99 latency, drive lifetime, or recovery correctness.
- **Pair every claim with proportional, real-device evidence** — named drives and firmware, standard
  workloads/traces, a distribution not just a mean, a device counter not an estimate — not
  adjectives.
- **Make the device reality visible early.** A storage reviewer wants to know the hardware and its
  state; a testbed table and a sentence on preconditioning/aging belong near the evaluation's start,
  not buried.
- **Protect the invariant.** If the design defers, batches, or reorders writes, say early that you
  verify crash consistency/durability still holds; do not let the reader wonder.
- **Respect the USENIX page budget** (FAST '27: ≤12 pages long / ≤6 short, references excluded) as a
  design constraint. It is a firm two-column limit; recover space editorially, never by shrinking
  the evaluation or the durability discussion.
- **Maintain double-blind** in self-citations (third person), system/tool names, acknowledgements,
  funding, datacenter names, and trace-hosting URLs.

## Storage paper skeleton

| Section | Job it must do | Common failure |
|---|---|---|
| Intro | Storage problem, the cost paid, contribution, evidence preview, storage payoff — first page | Leads with a technology trend, not a storage cost |
| Background | The device/media/workload reality the design exploits | Generic background not tied to the mechanism |
| Design / Study | The mechanism or the study protocol, reproducibly | Design described too thinly to rebuild |
| Evaluation | Each claim answered with the right storage metric on real devices | Throughput bar standing in for the claimed cost |
| Consistency/durability | The invariant the change risks, tested | Consistency asserted, never crash-tested |
| Related work | Delta-first positioning against storage literature | Citation catalog with no contrast |

## Sentence-level rewrites

| Draft pattern | FAST-safe rewrite |
|---|---|
| "Our system is much faster." | "cuts write amplification from X to Y on <SSD model, firmware> at steady state" |
| "We evaluate on an SSD." | "on <model/capacity/firmware>, preconditioned to steady state, fill Z%, TRIM on" |
| "Low latency." | "p99.9 read latency of ... under <workload>; full distribution in Fig. N" |
| "It is reliable / consistent." | "recovers a consistent state at all <K> injected crash points (§6)" |
| "State-of-the-art throughput." | Claim scoped to the devices, workloads, and state actually tested |
| "We reduce writes by ~2x." | "bytes-written from device counters fell 2.1x (95% CI ...), vs. the tuned baseline" |

## Storage-metric discipline

```text
[Endurance]     report bytes-written / P/E cycles from device counters, not estimates
[Latency]       report the distribution (p50/p99/p99.9) under load, not the mean
[Amplification] separate read vs. write amplification; say how each is measured
[Space]         on-media footprint, including metadata/GC overhead
[Durability]    the crash-consistency invariant and the test that checks it
-> lead each result with the metric that matches the claim; put device+state beside it
```

## Vignette: compressing a design-plus-study paper

A draft with a new cache design, six microbenchmarks, and a sprawling background: keep the design,
the two experiments that carry the headline (miss-ratio-vs-cost and tail latency on real traces),
and a crash-consistency check; move secondary microbenchmarks and full parameter sweeps to the
artifact with forward references; cut background to the media/workload facts the mechanism needs.
The test of a good cut: a reviewer should be able to answer "what storage cost does this change, by
how much, on what hardware, and does it stay correct?" from the body alone.

## Output format

```text
[Writing diagnosis] clear / under-motivated / wrong-metric / device-reality-missing / over-scoped
[First-page fix] <new framing leading with the storage cost the paper changes>
[Metric audit] <claim -> storage metric -> measured on real devices? yes/no>
[Durability check placement] <where the crash-consistency/invariant test is stated>
[Anonymity edits] <system names / self-citations / trace URLs / datacenter names to rewrite>
```
