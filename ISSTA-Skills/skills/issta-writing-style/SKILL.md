---
name: issta-writing-style
description: Use when revising an ISSTA paper for a clear testing/analysis contribution, covering the threat-model-then-technique structure, the evaluation contract, a threats-to-validity section that is not boilerplate, claims scoped to the subjects tested, double-anonymous phrasing, and 18-page ACM sigconf discipline that survives specialist reviewers.
---

# ISSTA Writing Style

Use this when revising the main paper. An ISSTA paper has to state, early and precisely, what
software behaviour it finds or reasons about, on what it was evaluated, and what the evidence
showed — to a reviewer who already knows the nearest tool and benchmark.

## Revision rules

- Put the contribution on the first page: the problem in a concrete testing/analysis setting, why
  existing techniques miss it, the technique, and what the evaluation showed. Name the technique;
  do not hide it behind "a novel approach."
- State the threat model or analysis scope before the technique. Reviewers judge soundness against
  the scope you set, so an unstated scope is an unbounded claim they will puncture.
- Make the evaluation a contract: subjects, baselines, metric, and statistic, declared before the
  numbers. "Outperforms prior work" without that contract is the single most common weak sentence.
- Pair every claim with evidence: a table, a benchmark result, an artifact path, or a scoped
  limitation. A declarative sentence near a result is something a specialist reviewer will check.
- Write a real threats-to-validity section: internal (confounds in the measurement), external
  (do the subjects generalize), and construct (does the metric measure the property). A boilerplate
  threats paragraph is noticed and counts against presentation.
- Keep double-anonymous phrasing in self-citations, tool names that de-anonymize, repository
  references, and acknowledgements.

## Contribution-presentation discipline

- Scope claims to the subjects tested. "Detects order-dependent flaky tests" is defensible; "detects
  flaky tests" when you tested one subclass is not.
- Separate what the technique guarantees from what it empirically achieves; mixing a soundness claim
  with a benchmark number in one sentence is a credibility leak.
- Define the analysis or measurement once, in one place; two-column ACM pages punish redefinition.
- When a result is best-effort or unsound-but-useful, say so; ISSTA reviewers respect a scoped,
  honest technique over an overclaimed "sound" one.

## Sentence-level rewrites

| Draft pattern | ISSTA-safe rewrite |
|---|---|
| "Our tool significantly outperforms prior work" | "finds X% more true bugs than <baseline> at an equal time budget (paired test, effect size Y)" |
| "We detect flaky tests" | "We detect the order-dependent subclass of flaky tests" |
| "Evaluated on real-world programs" | "Evaluated on <benchmark vN> across N subjects (SHAs in the artifact)" |
| "Our analysis is sound" | "Sound under Assumptions 1-2; native calls are out of scope" |

## Vignette: compressing into 18 ACM pages

A draft with a formal analysis, six subjects' worth of tables, and a sprawling related-work section:
keep the analysis rules, one soundness sketch, the evaluation protocol, and the two decision-critical
tables in the body; compress related work into delta-first contrasts; push complete per-subject
tables and extra configurations into the artifact. The test of a good cut: a specialist reviewer can
judge soundness and evaluation without opening the artifact — the artifact deepens the paper, it does
not complete it.

## What a strong ISSTA opening does

```text
1. names the concrete testing/analysis problem and its cost
2. bounds the scope (which subclass, which language, which assumption)
3. names the technique and its one key idea
4. states the evaluation contract: subjects, baseline, metric, statistic
5. reports the finding, honestly scoped
```

## Output format

```text
[Writing diagnosis] clear / under-scoped / overclaimed / contract-missing
[First-page fix] <new framing>
[Scope statement] <threat model / analysis scope>
[Claim discipline] <claim -> table/artifact/limitation>
[Compression cuts] <move to artifact / delete / merge>
[Anonymity edits] <phrases to rewrite>
```
