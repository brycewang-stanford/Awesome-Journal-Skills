---
name: hpca-writing-style
description: Use when revising an HPCA paper for the mechanism-to-behavior first-page arc, a measured motivation before the fix, a checkable mechanism description, numbers that name their instrument, and 11-page compression that leaves slack for the single rebuttal/revision window.
---

# HPCA Writing Style

Use this to shape an HPCA paper's prose and structure. The house style rewards a
paper built around **one mechanism-to-behavior claim**, motivated by a measured cost
and evidenced on a named instrument. Reopen the current page limit before trusting
the compression advice below.

## The first-page arc

An HPCA first page should carry, in order: **the measured problem → why existing
mechanisms miss it → the mechanism → the behavior it produces → what the numbers rest
on**. A reviewer should finish the abstract and first column knowing what you built,
what it costs, and what it changes — before any implementation detail.

- Lead with the *specific* pathology and a number, not "latency is a bottleneck."
- Name each prior mechanism's specific failure, not "prior work is limited."
- State the mechanism concretely enough that a reviewer could rebuild it.
- Anchor every headline number to its instrument in the same breath.

## Quantify the motivation before the fix

HPCA reviewers distrust a mechanism whose problem is assumed. Characterize the cost
first — measure the wasted traffic, the stall cycles, the energy — so the mechanism
answers a number. A motivation section that is all citation and no measurement is a
common reject signal.

## Describe the mechanism so it is checkable

The mechanism is the paper. Give the structure's size, the policy's logic, and the
hardware cost. If a reviewer has to guess whether your "confidence mechanism" is a
standard counter or something new, the novelty is invisible. A figure of the
datapath plus a precise textual description beats prose alone.

## Every number names its instrument

A speedup with no instrument is unreviewable. State whether it comes from a
cycle-level simulator (which one, at what fidelity, with which validated timing
models) or real silicon (which machine, in which governor/turbo/SMT state), and
report per-workload results with neutral cases marked — not only the mean.

## Style anti-patterns

| Anti-pattern | Why it hurts at HPCA | Fix |
|---|---|---|
| "Latency is a well-known bottleneck" | No measured cost | Lead with the specific pathology and a number |
| "A confidence mechanism" | Mechanism not checkable | Give the structure, logic, and hardware cost |
| "Outperforms in most cases" | Overclaim, no instrument | Per-workload results + named simulator/machine |
| Geomean-only results | Hides where it loses | Report the distribution; mark neutral cases |
| "et al." in the bibliography | Reject trigger (all authors required) | List every author of every reference |
| Roadmap as argument | Signposting replaces substance | Replace with the mechanism-to-behavior claim |

## Compression for the page limit

The 11-page body carries the characterization, the mechanism, and the headline
evidence; exhaustive per-configuration tables, extra sensitivity studies, and the
artifact go to the appendix and the anonymized mirror. Compress by cutting redundant
background, not by trimming author lists or the fidelity contract. Leave a little
slack: the single rebuttal/revision window may require small additions, and a body
already jammed to the last line has no room to answer a reviewer.

## Revision pass

```text
[First-page arc] measured cost -> gap -> mechanism -> behavior -> instrument? (Y/N each)
[Motivation] quantified before the fix? (Y/N)
[Mechanism] rebuildable from the text? (Y/N)
[Numbers] each names its instrument; per-workload reported? (Y/N)
[Bibliography] every reference lists all authors? (Y/N)
[Page pressure] slack left for the window? (Y/N)
[Top three edits] <ordered>
```

Recheck the current CFP: the page cap, font rule, and the all-authors reference
requirement are per-edition and control the compression plan.
