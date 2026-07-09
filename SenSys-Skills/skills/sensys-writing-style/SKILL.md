---
name: sensys-writing-style
description: Use when drafting or revising a SenSys paper's abstract, introduction, and system sections — building the sensing-pain to mechanism to measured-behavior arc inside the double-column limit, putting the buildable system on the first page, reporting energy and latency as numbers not adjectives, and pairing every claim with a measurement.
---

# SenSys Writing Style

A SenSys paper reads as an engineer's argument: here is a sensing or embedded problem that hurts
in a specific way, here is why existing systems fail on constrained hardware, here is the
mechanism I built, and here is its measured behavior. The house style rewards concreteness —
energy in joules, latency in a distribution, uptime in days — and penalizes the adjective
("lightweight," "efficient") that stands in for a measurement.

## The first-page arc

Put the system on the first page. The abstract and opening paragraph should already carry:

1. **The sensing/deployment pain** — the physical problem, stated so a systems reader feels it.
2. **Why existing systems fail** — each prior approach's failure named specifically, in embedded
   terms (dies mid-inference, exhausts the energy budget, needs an unavailable radio).
3. **The mechanism** — what you built, in one or two sentences, with the constraint it respects.
4. **The measured behavior** — the headline numbers (energy, latency, accuracy under real
   conditions), each tied to how it was measured.

The worked example in [`../../resources/worked-examples/01-introduction.md`](../../resources/worked-examples/01-introduction.md)
walks a before→after of exactly this arc for a batteryless classifier.

## Numbers, not adjectives

The single highest-leverage edit in a SenSys draft is replacing evaluative adjectives with
measured quantities.

| Weak (adjective) | Strong (SenSys) |
|---|---|
| "Our system is low-power." | "Draws 42 µA average at a 1% duty cycle, measured with a shunt at 10 kHz." |
| "Inference is fast on-device." | "Median 8 ms, 95th-percentile 21 ms, on the target Cortex-M4." |
| "The model is small." | "Quantized to 61 kB, peaking at 18 kB RAM on the MCU." |
| "We deployed for a long time." | "12 nodes over 47 days; two failed on day 9 (battery)." |
| "Accuracy is high." | "F1 0.9x against reference-instrument ground truth (App. A)." |

## Claim → measurement pairing

Every quantitative claim should point to the figure, table, or method that backs it. A reviewer
should never meet a number they cannot trace. Keep a running map as you write:

```text
Claim                                → Evidence
"survives power failures"            → Fig. 3 (termination across N brownouts)
"bounded end-to-end latency"         → Table 2 (latency CDF under harvest trace)
"matches wired accuracy"             → Table 3 (paired, same audio, App. A truth)
"projected 2-year lifetime"          → §4.3 (measured draw + battery spec, not datasheet)
```

If a claim has no evidence pointer, either measure it or soften it to what you can show.

## Structure inside the double-column cap

The body (≤ 12 pages full / ≤ 6 short) holds the core logic; references and appendices are
unlimited and outside the cap, so **the body earns its space by carrying the argument**, not the
exhaustive protocol. Typical shape: motivation and system overview early; the mechanism and its
constraint model in the middle; evaluation organized by the measurement axes
(`sensys-experiments`) — energy, latency, accuracy, deployment — each answering a claim from the
intro. Push full protocols, extra plots, and derivations to appendices (`sensys-supplementary`).

## System-paper discipline

- **Overview figure early.** A systems reader wants the block diagram before the details; one
  clear architecture figure repays its page cost.
- **Design decisions with their alternatives.** State what you chose *and what you rejected and
  why* — SenSys reviewers read for whether you understood the design space.
- **Honesty about limits.** A named limitation (works only above a harvest threshold; degrades
  past N nodes) reads as competence; a paper with no limits reads as under-evaluated.
- **No overclaiming.** "Matches the baseline at lower energy" with error bars beats "outperforms"
  with none. Under-report and let the measurements carry it.

## Revision checklist

```text
[ ] The system is on the first page: pain → gap → mechanism → measured behavior.
[ ] Every "low-power / fast / small / accurate" replaced by a measured quantity.
[ ] Every quantitative claim has a figure/table/method pointer.
[ ] Energy and latency reported with method; latency as a distribution.
[ ] An architecture/overview figure appears before the mechanism details.
[ ] Design choices state their rejected alternatives.
[ ] Limitations named honestly; no unqualified "outperforms."
[ ] Body carries the argument; protocols and extra plots in the appendix.
```

## Output format

```text
[Arc]      first-page arc present? which of the four beats is missing
[Adjectives] list of adjective→measurement edits still needed
[Claims]   claims lacking an evidence pointer
[Energy]   energy/latency reported with method and distribution? pass/gap
[Open]     the one revision that would most raise the paper's systems credibility
```
