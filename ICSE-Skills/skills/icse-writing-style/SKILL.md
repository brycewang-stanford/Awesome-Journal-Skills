---
name: icse-writing-style
description: Use when writing or revising an ICSE research-track paper, covering empirical-SE paper anatomy, research questions as the load-bearing structure, the threats-to-validity section the community expects, practitioner-grounded motivation, calibrated claims, and fitting a complete study into ten IEEE pages.
---

# ICSE Writing Style

ICSE prose is judged by empiricists. The reviewer pool's shared training —
controlled experiments, mining studies, qualitative methods — produces a house
reading style: they locate the research questions, check that the design
answers them, and read the threats-to-validity section as a candor test. Write
for that reading order, not for a general CS audience.

## The load-bearing skeleton

A canonical ICSE technique-plus-evaluation paper spends its ten pages (2027
format: 10 pages main text including all figures/tables/appendices, +2 pages
references only) roughly like this:

| Section | Pages | What reviewers extract from it |
|---|---|---|
| Introduction | 1.5 | The SE problem, who suffers it, the claim, the contributions list |
| Background / motivating example | 1 | One concrete failing case the technique later fixes |
| Approach | 2–2.5 | How it works, precisely enough to reimplement (verifiability) |
| Study design | 1.5 | RQs, subjects, baselines, metrics, protocol — before any results |
| Results, organized by RQ | 2.5 | One answer per RQ, stated then evidenced |
| Discussion + implications | 0.5–1 | What researchers and practitioners should do differently |
| Threats to validity | 0.5 | Honest limits with mitigations |
| Related work + conclusion | 1 | Delta over neighbors (see `icse-related-work`) |

Empirical studies swap Approach for extended methodology; the RQ-driven spine
stays. If a section cannot say which RQ it serves, it is a cut candidate.

## Research questions as contract

State 2–4 RQs in the introduction or design section, then answer them in order
with boxed findings:

```latex
\subsection{RQ1: How often do generated patches overfit the test suite?}
...evidence...
\begin{tcolorbox}
\textbf{RQ1 finding.} 47\% of patches passing the full suite fail held-out
tests; overfitting concentrates in multi-hunk patches.
\end{tcolorbox}
```

Reviewers navigate by these boxes. An RQ that is asked but never answered, or a
finding with no RQ, both read as design drift — a rigor flag.

## The threats-to-validity craft

The section is expected, but its *quality* is what gets scored. Community
convention organizes threats as construct validity (are you measuring the right
thing?), internal validity (could something else explain the result?), external
validity (to what does it generalize?), and — for statistical work — conclusion
validity. Three rules separate a real threats section from ritual:

1. **Name your actual weakest point**, the one a hostile reviewer would find
   anyway. Preempting it converts an attack into a footnote.
2. **Pair every threat with what you did about it** (mitigation) or why it is
   tolerable (bounded impact). A threat with neither is a confession.
3. **Ban imported boilerplate.** "Our results may not generalize to other
   projects" appears in thousands of papers; "our 17 subjects are all Java
   build systems, and the technique reads JVM bytecode, so C# generalization
   is untested" is yours alone.

## Motivation that survives the relevance criterion

ICSE scores relevance to software engineering explicitly. Ground the opening in
an engineering pain that is *evidenced*, not asserted: a quantified cost from a
cited study, a documented incident, an observed practice from your own
formative data. The weakest ICSE openings assert that a problem "is important
and has attracted increasing attention" — citation-mulch that spends the most
valuable half page on nothing.

## Calibrated claims

The verifiability criterion punishes claim/evidence gaps, so calibrate:

- Quantify or delete: "substantially outperforms" → "improves F1 by 0.09–0.14
  across all three benchmarks (Table 3)".
- Scope every generalization: "for the Java projects studied", "in our
  interview population".
- Distinguish observation from causation everywhere except where the design
  licenses causal language (a controlled experiment does; a mining
  correlation does not).
- Make the contributions list checkable — each bullet should name the section
  and, where relevant, the artifact directory that substantiates it.

## The abstract, sentence by sentence

An ICSE abstract that reviewers bid on accurately runs six moves: (1) the
engineering problem with its cost; (2) the gap in how existing work handles
it; (3) the approach in one mechanism-revealing sentence; (4) the study
design in one sentence — subjects, baselines, method; (5) headline results
with numbers, scoped; (6) the availability sentence. Move 4 is the one
authors from other communities omit and SE reviewers miss immediately: at
ICSE the *study* is a first-class part of the contribution, and an abstract
that hides it reads as having something to hide.

## Ten-page compression without desk-reject risk

The IEEE template's formatting rules are desk-reject-enforceable, so recover
space editorially: merge motivating example into the introduction; convert
prose protocol descriptions into a design table; move non-decision-critical
material to the replication package and cite it in the availability statement
(the package, unlike the paper, has no page cap); tighten figures — SE papers
lose half-pages to screenshots that could be 4-line listings. Never touch
`\vspace`, margins, or font sizes.

## Output format

```text
[Structure audit] skeleton section -> present/missing/oversized (page budget)
[RQ contract] each RQ -> design element -> boxed answer (complete? ordered?)
[Threats quality] real weakest point named? mitigations paired? boilerplate found?
[Claim calibration] list of unquantified/over-scoped claims with rewrites
[Space plan] cuts and relocations to reach 10 pages template-clean
```
