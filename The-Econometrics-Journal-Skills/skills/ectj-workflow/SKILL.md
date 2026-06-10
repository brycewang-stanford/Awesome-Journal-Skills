---
name: ectj-workflow
description: Use when sequencing a The Econometrics Journal manuscript from venue fit through leading-case framing, asymptotic identification, Monte Carlo, empirical application, 20-page compression, submission, review, replication package, and rebuttal.
---

# EctJ Workflow

Use this as the router for The Econometrics Journal (EctJ). Reopen the current RES/OUP
instructions before deadline-ready advice because fees, editors, and policy wording can
change.

## Route map

- Fit unclear or too incremental: use `ectj-topic-selection`.
- Literature contribution fuzzy: use `ectj-literature-positioning`.
- Identification, assumptions, or asymptotics weak: use `ectj-identification-strategy`.
- Monte Carlo or empirical application thin: use `ectj-data-analysis`.
- Exhibits crowded or not self-contained: use `ectj-tables-figures`.
- Leading-case contribution buried: use `ectj-contribution-framing`.
- Prose too long for the 20-page constraint: use `ectj-writing-style`.
- Data/code not acceptance-ready: use `ectj-replication-and-data-policy`.
- Need to understand one-week screening and three-month target: use `ectj-review-process`.
- Ready for Editorial Express: use `ectj-submission`.
- Decision letter arrived: use `ectj-rebuttal`.

## Resource loading rule

Use the resource layer when routing:

- `resources/worked-examples/01-introduction.md` for opening-page structure.
- `resources/exemplars/library.md` for benchmark style and verified examples.
- `resources/code/README.md` for methods-oriented simulation or replication smoke checks.
- `resources/official-source-map.md` before any deadline, fee, page-limit, proof-placement, or policy claim.

Never answer a volatile submission question from memory. If the source map marks a fact unresolved, say so
and recheck the official page before advising a final submission.

## Stop conditions

Pause the route and repair before moving forward if:

- the paper has no empirical application or applied-value demonstration;
- the theorem/result cannot be stated as a leading case;
- the simulations do not stress the assumption most likely to fail;
- the manuscript cannot fit the compact printed-paper discipline without hiding core proofs;
- the replication package has no command that recreates the main simulation/application exhibits.

## Output format

```text
[Current stage] idea / theory / empirics / drafting / submission / review / R&R / accepted
[Next EctJ skill] <skill name>
[Main bottleneck] <fit, assumptions, application, compression, replication, or response>
[One-week screen risk] <highest conformance or scope issue>
[Next action] <single concrete task>
```
