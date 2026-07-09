---
name: mobisys-writing-style
description: Use when revising a MobiSys paper for a mobile-systems first page, the pain → system-design → on-device-evidence arc, 12-page double-column compression, double-blind wording, and claims disciplined by measured latency, energy, memory, and thermal budgets rather than superlatives, so the draft survives systems-and-services reviewers.
---

# MobiSys Writing Style

Use this when revising the main paper. A MobiSys paper needs a compact statement of the
on-device problem, the system that solves it, and the measurements that prove it — in the
12-page double-column body.

## Revision rules

- Put the mobile-system contribution on the first page: the on-device pain, why current
  systems fail *on the device*, the mechanism, and the measured payoff.
- Name the device budget explicitly. MobiSys reviewers are sensitive to hidden compute,
  energy, latency, memory, and thermal assumptions.
- Pair every major claim with a measurement on real hardware, a design argument, or a
  reproducibility detail — never a superlative.
- Use the 12-page body for the system's spine; move long protocols, extra device sweeps, and
  extended ablations to the appendix without making the main paper unintelligible.
- Avoid overclaiming wins when the distribution is unreported or the gain is inside run-to-run
  spread.
- Maintain double-blind style in self-citations, prior-system references, acknowledgements,
  funding, screenshots, and artifact descriptions.

## System-presentation discipline

- State the **operating point**: the device, the workload, and the budget the system respects.
  A latency number without its device and workload is not interpretable.
- Give each design decision a **why-on-the-device** justification; MobiSys readers audit
  whether a choice is forced by the mobile constraint or merely convenient.
- Report costs as **distributions** — p50/p95 latency, energy-per-operation, memory footprint
  — not single "up to N×" peaks.
- Separate **measured** from **estimated**: an energy figure from a power monitor and an energy
  figure from a model are different claims and must be labeled so.
- Keep the accuracy/quality trade-off honest: a system that is faster or cooler at a cost must
  state the cost in the same breath.

## Sentence-level rewrites

| Draft pattern | MobiSys-safe rewrite |
|---|---|
| "Our system significantly outperforms..." | "cuts p95 latency from X ms to Y ms on <device> over N runs" |
| "Runs efficiently on mobile devices..." | "holds 30 fps within a 3 W budget on <device>, App. A" |
| "Saves substantial energy..." | "reduces energy-per-frame by X mJ (p50), measured on <monitor>" |
| "Achieves real-time performance..." | Claim scoped to the device, workload, and thermal state tested |

## Vignette: compressing into twelve double-column pages

A draft with a runtime design, five device studies, and a sprawling background section: keep
the design, one decision-critical figure (the latency-under-load curve) and one budget figure
(energy-per-frame), and the accuracy-cost table; compress background into the specific failures
current systems show on the device; move three device sweeps and the full protocol to the
appendix with forward references. The test of a good cut: a systems reviewer should
reconstruct the whole system and its evidence without opening the supplement.

## Output format

```text
[Writing diagnosis] clear / under-measured / overclaimed / overloaded
[First-page fix] <new mobile-system framing>
[Claim discipline] <claim -> measurement/design/limitation>
[Compression cuts] <move/delete/merge>
[Anonymity edits] <phrases, screenshots, or repo strings to rewrite>
```
