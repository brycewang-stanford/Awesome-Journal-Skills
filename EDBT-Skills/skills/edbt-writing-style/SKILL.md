---
name: edbt-writing-style
description: Use when revising an EDBT paper for a data-management contribution on the first page, a reproducibly described mechanism, an evaluation that survives a database-systems reviewer, honest scope, and disciplined use of the per-shape page budget (Regular / Experiments-&-Analysis / Vision) in the OpenProceedings template.
---

# EDBT Writing Style

Use this when revising the main paper. EDBT papers are read by database-systems reviewers and
published open access on OpenProceedings, so they need a **data-management contribution stated on
the first page** and an evaluation a skeptic trusts. The failure this skill prevents is a technically
fine paper that reads like a vague performance claim or a re-skinned ML result with a database title.

## Revision rules

- **Lead with the data-management contribution:** the concrete problem (a storage, query-processing,
  indexing, transaction, integration, or data-quality problem), why current systems fall short, the
  contribution (mechanism and/or study), the evidence on real workloads, and what it enables.
- **Make the mechanism reproducible in prose.** Describe the algorithm, data structures, parameters,
  and system integration precisely enough that a competent reader could reimplement it — vagueness
  here is the "I cannot tell how it works" revise.
- **Pair every claim with proportional evidence** — a real workload, a tuned baseline, a measurement
  at realistic scale with reported variance — not adjectives like "significantly faster."
- **State scope honestly, in the body.** Name where the technique helps, where it is neutral, and its
  overhead or failure cases; quantify them rather than hiding them. A database reviewer's first two
  objections are usually "unfair baseline" and "unrealistic scale" — pre-empt both.
- **Respect the per-shape page budget** as a design constraint (Regular / Experiments-&-Analysis
  ≤12 pages; Vision ≤6; references unlimited — reverify per cycle). References do not count, but
  figures, tables, and appendices in the body do.
- **Use the OpenProceedings/host template,** not `acmart` or `IEEEtran` carried from a US venue.

## Paper-shape skeletons

**Regular / applied-systems paper**

| Section | Job it must do | Common failure |
|---|---|---|
| Intro | Problem, inadequacy, contribution, evidence preview, what it enables — first page | Leads with "data is growing," not a concrete problem |
| Background / Motivation | Why current systems fall short, grounded | Motivation by assertion |
| Approach / System | The mechanism + integration, reproducibly | Described too thinly to reimplement |
| Evaluation | Each claim answered on real workloads vs. tuned baselines | Unnamed dataset, untuned baseline, toy scale |
| Scope / Discussion | Where it helps, is neutral, or costs; quantified | Limits hidden or hand-waved |
| Related work | Delta-first positioning against DB venues | Citation catalog with no contrast |

**Experiments & Analysis paper** — the *study* is the contribution: foreground the methodology
(subjects, metrics, fairness, coverage, repeatability) and treat the findings as the deliverable, not
a new system.

**Vision paper** — a tight argument for a new direction: the problem, why now, the sketch of an
approach, and the research agenda, within the short budget; no need for a full evaluation, but the
argument must be disciplined.

## Sentence-level rewrites

| Draft pattern | EDBT-safe rewrite |
|---|---|
| "Our system is significantly faster." | "reduces median query latency by X% (variance over N runs) vs. <tuned baseline> on <workload>" |
| "We evaluate on a large dataset." | "We evaluate on <named workload/logs>, sizes ..., cluster of ... workers; config in the artifact" |
| "Results show our approach works well." | "Under skew, straggler time drops by ...; on uniform keys, overhead is ...% (Table 2)" |
| "State-of-the-art performance." | Claim scoped to the workloads, metrics, and scale actually tested |
| "Our method scales." | "throughput holds from 8 to 128 workers (Fig. 2); beyond that is untested" |

## Scope discipline

```text
[Where it helps]     name the regime (e.g. concentrated, detectable skew) and show it
[Where it is neutral] show the no-op case (e.g. uniform keys) so the reviewer trusts you
[What it costs]      quantify overhead / memory / setup, not "negligible"
[Where it fails]     state the boundary (e.g. very short queries) and measure it
-> put each of these next to the affected result, not in a deferred paragraph
```

## Vignette: compressing an over-scoped systems paper

A draft with a sprawling background, five contributions, and nine plots: keep the two contributions
the evaluation actually supports, the plots that carry the headline result and the overhead case,
and a tight scope subsection; move parameter sweeps and secondary configurations to the artifact with
explicit forward references. The test of a good cut: a reviewer should be able to answer "what does
it do, on what workloads, versus what baseline, and what does it cost?" from the body alone.

## Output format

```text
[Writing diagnosis] clear / under-motivated / over-claimed / evidence-mismatched / over-scoped
[Shape] Regular / Experiments-&-Analysis / Vision — budget respected?
[First-page fix] <new framing leading with the data-management contribution>
[Claim audit] <claim -> workload/baseline/scale -> where answered -> proportional? yes/no>
[Scope fix] <where-it-helps / neutral / cost / failure, placed by the result>
[Template] host/OpenProceedings template in use? yes/no
```
