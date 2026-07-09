---
name: imc-writing-style
description: Use when drafting or revising the prose of an ACM IMC measurement paper, covering the first-page measurement finding, making vantage points and methodology auditable, longitudinal framing for a moving Internet, arguing limitations rather than reciting them, writing the Ethics section early, and acmart page-budget discipline.
---

# IMC Writing Style

Use this while drafting the body. IMC reviewers are measurement experts who read for **what you
learned about the real Internet and whether the data support it**. The organizing principle is
that the paper is a *measurement* contribution: the finding leads, the vantage points and method
are auditable, and the limitations and ethics are visible from the start — not appended.

## The first-page arc

Put the measurement finding on the first page, in this shape:

1. **A question about the real Internet** a practitioner or researcher recognizes ("how reachable
   / how deployed / how secure / how does X behave in the wild?").
2. **Why current knowledge is inadequate** — prior work measured too few vantage points, a single
   snapshot, a testbed instead of deployment, or a biased input.
3. **The measurement and its vantage points** — what you measured, from where, over what period.
4. **What the data show** — the headline finding, stated as a measured result with uncertainty.
5. **What it means** — for operators, protocol designers, or the community, plus what you release.

Do **not** lead with a system you built or a tool's speed. If the first page is a systems win, the
paper reads as a re-routed NSDI/SIGCOMM submission (`imc-topic-selection`).

## Make vantage points and method auditable

A measurement claim is only as good as the reader's ability to judge the measurement:

- **Name the vantage points:** locations, ASes, probe types, and how many. Summarize in the body,
  detail in the appendix.
- **Argue representativeness explicitly:** why these vantage points support the claim, and where
  they do not. Quantify coverage bias rather than hoping no one asks.
- **Date everything:** measurement windows, cadence, and target-list capture dates. The Internet
  moves; undated results are unfalsifiable.
- **Show the method, not just the tool name:** enough that a reader could re-measure and judge
  soundness.

## Longitudinal and confound awareness

- Distinguish a **snapshot** from a **trend**. If you claim behavior over time, show the window and
  its stability; if you have a snapshot, scope the claim to it.
- Name confounds a moving Internet introduces — diurnal patterns, churn, load-balancing, CDN
  effects, measurement-vantage bias — and instrument to bound them.

## Limitations that argue, not recite

A good IMC limitations discussion is an **argument about validity**, engaged where the results live:

- For each headline result, state the threat to its validity (coverage, ground truth, temporal,
  measurement bias) and how you bounded it.
- Prefer "we observed X from these vantage points; it may not hold for networks unlike them, which
  we quantify in §Y" over a generic "our study has limitations."
- Do not quarantine all caveats into one closing paragraph.

## Write the Ethics section early

The Ethics section is a **required gate**, not a closing courtesy (`imc-submission`). Drafting it
early forces you to design safe active measurement, obtain IRB determinations, and plan disclosure
*before* collecting data — none of which can be retrofitted. Reference it from the introduction so
the reviewer sees the posture immediately.

## Page-budget discipline (acmart)

IMC's `acmart` budget (IMC 2025: up to 13 pages full / 6 pages short of text+figures, plus an
unlimited appendix) is generous but finite for the body. Recover space by **cutting redundancy**,
not by exiling decision-critical evidence to the appendix (`imc-supplementary`). Every figure earns
its space by supporting a claim; a vantage-point map that clarifies coverage is worth more than a
decorative architecture diagram.

## Common prose failures at IMC

| Failure | Why it hurts | Fix |
|---|---|---|
| System/tool leads the first page | Reads as a systems re-route | Lead with the measurement finding |
| Vantage points unnamed or unjustified | Reader cannot judge validity | Name them; argue representativeness |
| Undated, single-snapshot claims | Unfalsifiable on a moving Internet | Date everything; scope or extend temporally |
| Limitations recited generically | No validity argument | Tie each threat to a result and bound it |
| Ethics as an afterthought | Fails the gate | Write and reference it early |

## Output format

```text
[First-page arc] question -> inadequacy -> measurement/vantage points -> finding -> meaning? present/gaps
[Vantage points] named, dated, representativeness argued? yes/no
[Temporal framing] snapshot vs. trend stated correctly? yes/no
[Limitations] argued per-result and bounded? yes/no
[Ethics] section drafted early and referenced up front? yes/no
[Body edits] <ordered list to strengthen the measurement narrative>
```
