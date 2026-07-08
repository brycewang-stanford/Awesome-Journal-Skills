---
name: popl-experiments
description: Use when designing the empirical component of a POPL paper — deciding whether evidence should be a mechanization, a prototype, case studies, or benchmarks; reporting proof effort and case-study coverage honestly; and keeping performance numbers in a supporting role so the formal claim stays the paper's center of gravity.
---

# POPL Experiments and Empirical Evidence

POPL welcomes experimental papers, but the evaluation's job differs from a systems
venue: at POPL, evidence **demonstrates that the formal idea is realizable and
relevant**, it does not substitute for the theorem. Calibrate the empirical section
to the claim it supports, and no further. (Venue facts referenced here were checked
2026-07-08; see `resources/official-source-map.md`.)

## Match evidence to claim

| Claim in the paper | Right evidence | Wrong evidence |
|---|---|---|
| "The type system is sound" | Proof (mechanized or on-paper, `popl-reproducibility`) | A test suite that found no counterexample |
| "The analysis is precise enough to be useful" | Case studies on real programs with found/missed counts | One toy example |
| "The logic scales to real proofs" | Proof effort data: LOC, person-time, lemma reuse across case studies | Adjectives ("lightweight," "practical") |
| "Checking is fast enough for interaction" | Timings on stated hardware with input sizes | Asymptotic claims dressed as measurements |
| "The translation preserves behavior" | The theorem, plus differential testing as a sanity layer | Testing alone |

## Proof effort is data at this venue

Papers about logics, tactics, and frameworks make usability claims; the honest
currency is effort accounting. Report it like a measurement, mechanically:

```bash
# Rocq/Coq development: spec vs proof line counts per file
coqwc theories/*.v | tail -5
# Lean 4: declaration counts as a proxy for library size
grep -rcE '^(theorem|lemma|def) ' Src/ | sort -t: -k2 -nr | head
# Case-study table skeleton: program, LOC, proved property, person-days, reused lemmas
```

State what the numbers do not show: person-days depend on author expertise, and
line counts are assistant-specific. An honest caveat paragraph here reads as
maturity, not weakness.

## Case-study discipline

- Choose case studies that stress *different* features of the formalism, and say
  which feature each exercises; three variations on one pattern count as one.
- Report failures and near-misses: the program the analysis could not verify, the
  proof that needed a manual bridge lemma. POPL reviewers trust evaluations that
  contain bad news.
- Distinguish the artifact language from the ambient claim: results for a core
  calculus fragment must not be narrated as results for the full language.
- If a baseline tool exists, compare capability first (what each can express or
  verify) and performance second.

## Performance numbers, when present

Keep them survivable rather than spectacular: fixed machine spec, versioned inputs,
repeated runs with dispersion, scripts in the artifact so evaluators can regenerate
every table (`popl-artifact-evaluation`). A slow but sound prototype is publishable
at POPL; an irreproducible speedup claim is a liability everywhere.

## Output format

```text
[Claim-evidence map] <each empirical claim -> its evidence type; mismatches flagged>
[Effort accounting] <LOC/person-time/case-study table present? caveats stated?>
[Bad-news audit] <failures and limitations reported, or missing>
[Regenerability] <scripts + machine spec + versions for every number>
```
