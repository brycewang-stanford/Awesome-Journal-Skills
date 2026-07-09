---
name: cav-writing-style
description: Use when revising a CAV (Computer Aided Verification) paper for a precise verification contribution on the first page, an explicit soundness/completeness statement, theorem-and-proof discipline in the LNCS page budget, fair benchmark claims, honest scope and limits, and double-blind wording for the anonymized categories.
---

# CAV Writing Style

Use this when revising the main paper. CAV papers are Springer LNCS chapters read by verification
researchers, so they need a **precise verification contribution stated on the first page** and a
**formal guarantee** a reviewer can check. The failure this skill prevents is a technically fine
paper that reads like a systems demo or a heuristic with a benchmark table but no stated property.

## Revision rules

- **Lead with the verification contribution and its guarantee:** the problem (what property, of what
  system), why current methods fall short, the contribution (technique and/or tool), **what is
  formally guaranteed** (soundness, completeness, an equisatisfiability/refinement claim), the
  benchmark evidence, and the scope.
- **State the formal claim precisely.** Name the property, the assumptions, and the theorem. A paper
  whose "contribution" is only "faster on benchmarks" with no guarantee reads as a tool note, not a
  Regular Paper.
- **Give proofs their place.** Key proofs go in the body; long proofs may go to a clearly-marked
  appendix — but reviewers are not obliged to read appendices, so the proof *idea* must be in the
  body (see `cav-supplementary`).
- **Make benchmark claims falsifiable.** Every empirical claim names the benchmark set (with
  revision), the baseline tools and versions, and the resource limits (time/memory) — adjectives
  like "significantly faster" without these are not evidence (see `cav-experiments`).
- **State scope and limits as your own, not as a closing apology.** Say which logics, system sizes,
  or property classes the method covers and where it stops. Over-claimed generality is the fastest
  way to lose a verification reviewer's trust.
- **Maintain double-blind wording** for Regular and Application papers: anonymize self-citations,
  the tool/solver name, benchmark paths, acknowledgements, and repository links. (Tool and
  Industrial papers are not anonymized.)

## Verification-paper skeleton

| Section | Job it must do | Common failure |
|---|---|---|
| Intro | Problem, inadequacy, contribution, the guarantee, benchmark preview, scope — first page | Leads with "SMT/model checking is important," not a precise problem |
| Preliminaries | The formal setting: logic, semantics, the property class | Notation dumped without motivating the model |
| Approach | The technique/algorithm, stated so it can be re-implemented | Algorithm described too thinly to reproduce |
| Correctness | The theorem(s) and proof idea; soundness/completeness | A "clearly sound" claim with no argument |
| Evaluation | Benchmarks, baselines, resource limits, per-instance data | "Strong results" with no set revision or limits |
| Related work | Delta-first positioning against the verification literature | Citation catalog with no contrast |

## Sentence-level rewrites

| Draft pattern | CAV-safe rewrite |
|---|---|
| "Our tool is significantly faster." | "solves N previously-timed-out instances and reduces mean time by X% on the fixed-revision <set> under a 20-min/8-GB limit vs. <tool vA.B>" |
| "Our method is sound." | "Theorem 1: the procedure preserves equisatisfiability under <assumptions>; proof in §4 (full proof, App. A)" |
| "We evaluate on standard benchmarks." | "We evaluate on the <division> of <benchmark set, revision R>, listed in the artifact" |
| "Our approach scales." | "runs to completion on instances up to <size/metric>; beyond that, <stated limit>" |
| "The solver handles all cases." | Claim scoped to the logic/theory and property class actually supported |

## Correctness-and-scope discipline

```text
[Guarantee]   name the property (sound? complete? terminating?) and the assumptions it needs
[Proof]       proof idea in the body; full proof in the body or a clearly-marked appendix
[Checkability] where possible, emit a witness/certificate a reviewer can independently check
[Scope]       state the logics/theories/system-sizes/property-classes covered — and the boundary
-> put the limit next to the claim, not only in a closing paragraph
```

## Vignette: compressing a technique-plus-tool paper

A draft with a long preliminaries section, three theorems, and a sprawling evaluation: keep the
motivating problem and the main soundness theorem with its proof idea in the body; move two
supporting lemmas' full proofs and the per-instance benchmark table to the appendix/artifact with
explicit forward references; keep the headline benchmark comparison (with limits) in the body. The
test of a good cut: a reviewer should be able to answer "what is guaranteed, and how much faster/more
capable is it, under what budget?" from the body alone.

## Output format

```text
[Writing diagnosis] clear / no-stated-guarantee / over-claimed / unfalsifiable-benchmarks / over-scoped
[First-page fix] <new framing leading with the contribution and its guarantee>
[Claim audit] <claim -> theorem or benchmark evidence -> where -> falsifiable? yes/no>
[Scope fix] <the boundary to state next to the claim>
[Anonymity edits] <tool/solver names / self-citations / benchmark paths to rewrite (if anonymized)>
```
