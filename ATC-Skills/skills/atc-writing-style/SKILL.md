---
name: atc-writing-style
description: Use when drafting or revising an ATC (ACM SIGOPS Annual Technical Conference, formerly USENIX ATC) systems paper — writing first two pages that survive the round-one read on their own, structuring the implementation-and-measurement narrative, reporting costs beside gains, and holding the two-column 12-page budget that now includes appendices.
---

# ATC Writing Style

Write for two audiences in two rounds. In ATC 2027 (call re-verified 2026-11-24) the first round
is **based on the first two pages** of the paper — reviewers may read on but are not obliged to; in
round two, papers that advance get additional, full reviews. So ATC writing has a demand no
single-round venue makes: the paper's core argument must land, self-contained, in its first two
pages *and* expand faithfully into twelve. (ATC 2026 asked for a separate two-page extended abstract
for the same purpose; 2027 drops it, so the burden moves onto your own abstract and introduction.)

## Self-standing first two pages (round-one surface)

The call lists six round-one reject reasons: out of scope (not systems), unclear motivation, a main
idea that is hard to understand, a too-small or incremental contribution, poor placement against
related work, and a non-rigorous evaluation. A round-one reviewer who reads only pages 1-2 should
therefore finish knowing:

1. **The systems problem** — a pain a builder or operator recognizes, in the first breath.
2. **Why the current design is inadequate** — the specific limitation your work removes.
3. **The contribution** — the system or technique, stated as what it *does*, not "novel."
4. **The evidence** — the real testbed and the headline result (with the metric that matters, e.g.,
   tail latency, throughput at matched cost).
5. **The honest cost** — what the design trades away, named not hidden.
6. **The delta and placement** — the closest prior systems and what this paper adds beyond them,
   stated in a sentence or two (the full related work can come later).

Test it: hand pages 1-2 to a systems colleague and ask them to state the problem, idea, delta,
testbed, and result. If they cannot, the paper will lose round one no matter how strong pages 3-12
are. The call itself "strongly encourage[s] authors to make the introduction self-contained."

## The full-paper arc

ATC papers are implementation-and-measurement narratives:

- **Introduction:** problem → inadequacy → contribution as systems claims → real-testbed evidence →
  what changes in practice. Lead with the systems contribution, not a trend sentence.
- **Design:** the mechanism and the *reasons* for each choice, tied to the deployment constraint.
  Reviewers reward a design justified by the problem over one justified by novelty.
- **Implementation:** enough that a reader believes it was built and could be rebuilt — scale (lines,
  components), integration points, and what was hard.
- **Evaluation:** questions first, then answers. End-to-end results *and* microbenchmarks that
  isolate the mechanism; baselines that are fair; tails and variance, not just means.
- **Costs and limitations:** report the trade beside the gain, ideally in the same figure/table. ATC
  reviewers trust evaluations that volunteer their costs.

## Report costs beside gains (the ATC trust move)

Every systems design trades something — CPU on the fast path, memory, write amplification, warm-up,
compatibility. The fastest way to earn a systems reviewer's trust is to **quantify the cost in the
same breath as the win**, at a *matched* operating point (same budget, same load). Concealing the
cost is the fastest way to lose it.

## Page-budget discipline (two columns, 12 pages)

- **≤ 12 pages** long / **≤ 6** short, excluding references but **including appendices**, in
  **two-column** 10pt (`\documentclass[sigplan,10pt]{acmart}` recommended).
  The two-column format is denser than single-column ACM layouts — a figure-heavy systems paper
  fills it fast.
- Recover space **editorially**, never by shrinking the font or margins (a desk-reject ground): cut
  redundant background, merge overlapping figures, and move non-decision-critical detail to the
  artifact — an appendix no longer buys pages, because it counts toward the limit (see
  `atc-supplementary`).
- Keep every claim that decides acceptance inside the body; the appendix and artifact hold support,
  not load-bearing evidence.

## Systems-prose specifics

- **Name the testbed early** — hardware (CPU/NIC/SSD models), OS/kernel versions, and workloads —
  so results are legible.
- **Quantify, don't adjective** — "reduces p99 by X at matched throughput" beats "significantly
  faster."
- **Third-person self-citation** for double-blind — never "our earlier system X"; write it as prior
  work by others.
- **Figures earn their space** — each should answer an evaluation question a reviewer would ask.

## Anti-patterns (ATC-specific)

- **A back-loaded opening** whose idea or evidence first appears on page 4 — a round-one loss.
- **Average-only evaluation** with no tail or variance — reads as hiding the interesting cases.
- **Novelty-as-argument** — asserting "novel" instead of motivating the design from the problem.
- **Costs quarantined** in a late limitations paragraph instead of reported with the gains.
- **Template tampering** to fit the page budget — recover space by cutting, not shrinking.

## Output format

```text
[First two pages] self-standing? problem/idea/delta/testbed/result/cost all present by page 2? yes/no
[Arc] problem -> inadequacy -> contribution -> real-testbed evidence -> what changes: complete? gaps?
[Evidence shape] end-to-end + microbenchmarks? tails + variance? fair baselines? costs beside gains?
[Budget] pages used (body+appendix / refs), two-column compliance, editorial cuts available
[Rewrite queue] <ordered edits, highest-leverage first — usually the first two pages>
```
