---
name: mlsys-writing-style
description: Use when revising an MLSys paper's prose and structure, building the measured-bottleneck opening, naming the mechanism instead of listing optimizations, writing evaluation sections as answers to research questions, quantifying every performance claim with workload context, and fitting the argument into the venue's 10-page two-column body.
---

# MLSys Writing Style

Use this during drafting and revision. MLSys prose sits between two failure modes: the
ML-paper voice (contribution bullets, related-work-first, benchmarks as decoration) and
the tech-report voice (system tour, feature list, "extensive experiments"). The venue's
own genre is different: a paper here is an *argument about where time, memory, or money
goes* in an ML workload, and how a named idea changes that.

## The first-page arc

1. **Bottleneck, measured.** Open with the profiling fact that justifies the paper —
   a percentage, a stall, a cost line — on a workload the reader recognizes. If the
   introduction's first numbers appear in the evaluation section, the order is wrong.
2. **Why existing designs cannot remove it.** Mechanistic reasons per named system or
   design family, not "prior work is limited."
3. **Insight.** The one observation that unlocks the design, stated in a sentence a
   reader could repeat tomorrow.
4. **Mechanism, named.** Give the technique a noun. Anonymous "several optimizations"
   is how research contributions disappear into engineering.
5. **Payoff with scope.** Ranged improvement, named baseline, stated cost or non-win.

## Sentence-level rewrites

| Draft pattern | MLSys-safe rewrite |
|---|---|
| "achieves up to 3.4x speedup" | "1.6-2.2x goodput at matched p99 across three traces (3.4x peak on the bursty trace)" |
| "significantly reduces memory" | "cuts peak activation memory 38% (Fig. 5), enabling batch 32 on one A100" |
| "our highly optimized implementation" | name the three optimizations and ablate them |
| "extensive experiments demonstrate" | "we answer four questions: (RQ1)..." |
| "existing systems suffer from poor utilization" | "SystemX idles the interconnect 41% of decode time on this trace (§2)" |
| "we believe this generalizes to other accelerators" | state the mechanism's hardware assumptions; claim only what was measured |

## Evaluation sections answer questions

Structure the evaluation as research questions, each mapped to figures that answer it:

```text
6. Evaluation
   RQ1  Does <mechanism> improve end-to-end serving under realistic load?   (6.2)
   RQ2  Where does the gain come from?  [ablation per component]            (6.3)
   RQ3  When does it *not* help?  [load shapes, model sizes, hardware]      (6.4)
   RQ4  What does it cost?  [memory, complexity, build time, $ ]            (6.5)
```

RQ3 and RQ4 are not optional at this venue; their absence is the strongest style-level
predictor of skeptical reviews. A results tour organized by dataset instead of by
question reads as unanalyzed output.

## Numbers discipline

- Every performance number carries its workload, hardware, and variance context on
  first mention; naked speedups are marketing.
- Prefer goodput/latency-constrained framings over raw throughput when serving is
  involved — systems readers discount throughput wins that trash tails.
- Use consistent units and precision; a table mixing ms, s, and "x" invites arithmetic
  audits.
- When a number is estimated (cost models, projections to larger scale), typographically
  separate it from measured results and say how it was estimated.

## Compression into 10 two-column pages

- The design section earns space in proportion to what the evaluation ablates; a
  component never ablated should be described in two sentences, not two columns.
- Background sections rarely deserve more than half a page — MLSys readers know the
  transformer, the GPU memory hierarchy, and the serving stack; spend the space on
  *your* workload characterization instead.
- Architecture diagrams beat prose walkthroughs; one good figure with numbered dataflow
  arrows replaces a column of "then the request is forwarded to."
- Move full configuration matrices to the separately-uploaded appendix, but keep the
  fairness-critical facts (baseline tuning budget) in the body — reviewers are not
  obliged to open the appendix.
- References are excluded from the 10 pages and must list all authors (2026 rule), so
  never compress by mutilating the bibliography.

## Figures and tables carry the paper

Systems reviewers form their judgment from the exhibits, then read prose to confirm it.

- The architecture figure: numbered dataflow, the new components visually distinct from
  inherited infrastructure, and no internal codenames. If a reader cannot locate the
  contribution in this figure, the design section will not save it.
- The money figure: one plot that shows the headline claim with its constraint —
  typically goodput versus load with a p99 ceiling marked, both systems on the same
  axes. Reviewers screenshot this one into their reviews.
- Every performance plot states hardware and trial count in the caption; captions are
  read during skims, body text is not.
- Log-scale axes are honest for spanning regimes but must be labeled loudly; a log axis
  that makes a 1.3x gap look large will be caught and remembered.
- Tables: bold the best number per row only if "best" is defined in the caption;
  include the variance column; never mix measured and projected numbers in one table
  without typographic separation.

## Title and abstract mechanics

- Titles at this venue name the system or mechanism and the setting ("X: <mechanism>
  for <workload class>"); cleverness that hides the topic costs discovery, since
  practitioners search proceedings by problem.
- The abstract must contain at least one measured number with its workload context —
  an abstract with no number reads as a position paper here.
- Spell out the ML property and system constraint being co-designed in the first two
  sentences; abstract readers include the reviewers bidding on papers, and bidding
  mismatch produces the wrong panel (see `mlsys-review-process`).

## Anonymization without lobotomy (research track)

Blinding at a systems venue tempts authors to delete the deployment context that makes
the paper credible. Keep the facts, drop the identity: "a production recommendation
service serving tens of millions of daily requests" survives review; the company name
returns at camera-ready. Scrub cluster hostnames and internal codenames from figures —
profiler screenshots are the classic leak.

## Output format

```text
[Diagnosis] tech-report voice / ML-paper voice / MLSys-ready
[First-page arc] <bottleneck number present? insight? named mechanism? scoped payoff?>
[RQ structure] <RQ list; RQ3 (non-wins) and RQ4 (costs) present?>
[Claim rewrites] <naked number -> contextualized rewrite>
[Compression cuts] <un-ablated design prose, background, config matrices to move>
[Anonymity edits] <identity leaks to fix without deleting context>
```
