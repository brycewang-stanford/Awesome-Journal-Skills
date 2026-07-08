---
name: micro-writing-style
description: Use when drafting or revising a MICRO paper's prose and structure — building the characterization-motivated introduction, budgeting 11 appendix-free pages, drawing the mechanism walkthrough a microarchitect can re-implement, and pairing every speedup claim with its area, storage, and power cost line.
---

# MICRO Writing Style

A MICRO paper is an engineering argument: *this pattern exists in real workloads,
here is a piece of hardware that exploits it, here is what it costs, here is what it
pays*. The style rules below encode how the microarchitecture community reads.

## The four-beat argument

1. **Characterization beat.** Open with measured evidence that the exploitable
   behavior exists — a miss-pattern histogram, a stall-cycle breakdown, a
   reuse-distance CDF — from real workloads, before any mechanism appears. MICRO
   reviewers trust a paper that observed the machine before modifying it.
2. **Insight beat.** One sentence naming the property your hardware will exploit
   ("dead blocks announce themselves by burst-then-silence access"). If the insight
   sentence could headline three different mechanisms, sharpen it.
3. **Mechanism beat.** A block diagram plus a walkthrough at the level of tables,
   counters, comparators, and state machines — detailed enough that a reader could
   size the SRAM. Include the *storage budget table* (bits per entry × entries).
4. **Accounting beat.** Speedup is half a result. The other half: area or storage
   overhead, power, added latency on the critical path, and what happens on the
   workloads the mechanism does not help (the tax on non-beneficiaries).

## Page budget for 11 content pages, no appendix

The 2026 guidelines permit no appendix, so the body must be self-sufficient — proofs
of concept, sensitivity sweeps, and methodology detail all compete for the same 11
pages (references are unlimited and free).

| Section | Pages | Non-negotiable content |
|---|---|---|
| Intro + characterization | 2.0 | Motivating data figure by page 2 |
| Background / threat model | 1.0 | Only what the mechanism needs |
| Mechanism | 2.5 | Block diagram, walkthrough, storage table |
| Methodology | 1.0 | Simulator, configs, workloads, power model — exact versions |
| Evaluation | 3.0 | Headline result, ablations, sensitivity, overhead accounting |
| Related work + conclusion | 1.5 | Deltas against nearest mechanisms |

Squeezing tricks (`\vspace`, tightened lists, sub-9pt figure text) are barred by the
guidelines and checked visually — recover space by cutting content, not leading.

## Sentence-level calibration

- Tie every performance number to its instrument: "8.4% geomean speedup on SPEC
  CPU2017 rate-1 **in cycle-level simulation**" — never let a simulated number read
  as a silicon number.
- Prefer mechanism verbs (filters, throttles, bypasses, coalesces) over marketing
  verbs (unlocks, revolutionizes, dramatically improves).
- State the baseline aggressively and early: "against an 8-way OoO core with a
  state-of-the-art stride+SMS prefetcher" beats "against a baseline core."
- Quantify the negative space: which workload class regresses, by how much, and why
  the mechanism's guard logic bounds it.

## Figure discipline

```text
Fig. 1  motivating characterization (the "why" figure)   — page 1-2
Fig. 2  mechanism block diagram (the "what" figure)      — mechanism section
Fig. 3  headline bar chart, geomean marked, baseline = 1 — first evaluation page
Fig. 4+ ablation / sensitivity, one question per figure
Every figure: axis labels >= 9pt after scaling; caption states config + workload set.
```

A MICRO reader flips to Fig. 2 and Fig. 3 before reading a word — both must stand
alone with their captions.

## Naming and terminology conventions

- **Name the mechanism once, early, and use the name relentlessly.** MICRO papers
  are remembered by mechanism name (UCP, McPAT, DaDianNao); a design referred to
  as "our approach" for eleven pages has no handle for reviewers to discuss it by.
- Keep the community's units: IPC and speedup for performance, MPKI for
  misses/branch events, KB/mm² for cost, nJ/pJ per access for energy. Converting
  a miss-rate percentage where the reader expects MPKI adds friction.
- "Baseline" means the unmodified reference machine; "prior work" means the best
  published competitor — never blur the two in prose or legends.
- Threat-model vocabulary (for security mechanisms): attacker capability, channel,
  and what is explicitly out of scope, stated before the mechanism, not after.

## Title and abstract conventions

The title should carry the mechanism name plus the structure touched
("Ghostline: Demand-Triggered Dead-Block Reclamation for Shared LLCs") — searchable
by the structure, memorable by the name. The abstract executes the four beats in
miniature, each beat with a number attached; see
`resources/worked-examples/01-introduction.md` for a full before → after.

## Anti-patterns the PC flags

- Characterization-free introductions that open with "Moore's law" boilerplate.
- Mechanisms described only in prose, with no sizeable structure — unimplementable.
- Evaluation sections that tour benchmarks instead of answering ordered questions.
- Overhead numbers missing, or buried in a sentence instead of a table row.
- IPC arithmetic averaged instead of geomean'd, or speedup over an unnamed baseline.
- "Details omitted due to space" — with no appendix allowed, that reads as "details
  do not exist."

## Revision passes, in order

1. **Argument pass** — do the four beats appear, in order, with a number each?
2. **Claim-audit pass** — every performance sentence checked for instrument
   label, baseline name, and metric correctness (geomean, MPKI).
3. **Skeptic pass** — a co-author plays the methodology-forensics reviewer
   (`micro-review-process`) and attacks configs, sampling, and baselines; fix in
   text what they had to ask about.
4. **Compression pass** — apply `micro-supplementary` triage until the body sits
   at 11 pages without squeezing tricks.
5. **Format pass** — the `micro-submission` gate table, on paper, by eye.

## Output format

```text
[Argument beats] characterization / insight / mechanism / accounting: present-missing each
[Insight sentence] <quoted from draft, or ABSENT>
[Storage budget table] present at bit-level: yes / no
[Cost line] area-storage-power-latency all quantified: yes / partial / no
[Page budget] section over/under vs table above
[Figure audit] Fig1 motivates / Fig2 rebuildable / Fig3 geomean+baseline: pass-fail
[Calibration issues] <list of simulated-vs-silicon or baseline-vagueness sentences>
```
