---
name: atc-writing-style
description: Use when drafting or revising an ATC (ACM SIGOPS Annual Technical Conference, formerly USENIX ATC) systems paper — writing a self-standing two-page extended abstract for the round-one gate, structuring the implementation-and-measurement narrative, reporting costs beside gains, and holding the two-column 12-page budget.
---

# ATC Writing Style

Write for two audiences in two rounds. In round one, two reviewers read only your **two-page
extended abstract**; in round two, 3-4 reviewers read the full paper. The abstract is **review-only,
not published, and must stand alone**. So ATC writing has a demand no single-round venue makes: the
paper's core argument must fit, self-contained, into two pages *and* expand faithfully into twelve.

## The self-standing extended abstract (round-one surface)

A round-one reviewer who reads only the abstract should finish knowing:

1. **The systems problem** — a pain a builder or operator recognizes, in the first breath.
2. **Why the current design is inadequate** — the specific limitation your work removes.
3. **The contribution** — the system or technique, stated as what it *does*, not "novel."
4. **The evidence** — the real testbed and the headline result (with the metric that matters, e.g.,
   tail latency, throughput at matched cost).
5. **The honest cost** — what the design trades away, named not hidden.

Test it: hand the two pages to a systems colleague *without* the paper and ask them to state the
problem, contribution, testbed, and result. If they cannot, the abstract will lose round one no
matter how strong the paper is. A trimmed introduction can work only if it already reads
self-contained.

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

- **≤ 12 pages** full / **≤ 6** short, excluding references and appendices, in **two-column** 10pt.
  The two-column format is denser than single-column ACM layouts — a figure-heavy systems paper
  fills it fast.
- Recover space **editorially**, never by shrinking the font or margins (a desk-reject ground): cut
  redundant background, merge overlapping figures, and move non-decision-critical detail to an
  appendix (reviewers are not required to read appendices — see `atc-supplementary`).
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

- **A dependent extended abstract** that only makes sense after reading the paper — a round-one
  loss.
- **Average-only evaluation** with no tail or variance — reads as hiding the interesting cases.
- **Novelty-as-argument** — asserting "novel" instead of motivating the design from the problem.
- **Costs quarantined** in a late limitations paragraph instead of reported with the gains.
- **Template tampering** to fit the page budget — recover space by cutting, not shrinking.

## Output format

```text
[Extended abstract] self-standing? problem/contribution/testbed/result/cost all present in 2 pages? yes/no
[Arc] problem -> inadequacy -> contribution -> real-testbed evidence -> what changes: complete? gaps?
[Evidence shape] end-to-end + microbenchmarks? tails + variance? fair baselines? costs beside gains?
[Budget] pages used (body/refs), two-column compliance, editorial cuts available
[Rewrite queue] <ordered edits, highest-leverage first — usually the abstract>
```
