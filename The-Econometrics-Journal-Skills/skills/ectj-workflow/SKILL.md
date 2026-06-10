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

## Stage gates keyed to the RES pipeline

| Gate | Pass condition | Skill that repairs failure |
|---|---|---|
| Fit gate | Leading case plus applied value both stated in one sentence each | `ectj-topic-selection`, `ectj-contribution-framing` |
| Theory gate | Target object, assumptions, and asymptotic claims traceable; proofs printable | `ectj-identification-strategy` |
| Evidence gate | Every asymptotic claim paired with a finite-sample exhibit; one DGP calibrated to the application | `ectj-data-analysis` |
| Compression gate | Printed paper within the 20-page norm; summary within 150 words | `ectj-writing-style`, `ectj-tables-figures` |
| Conformance gate | Template, fee, proof placement, and replication disclosure verified on live pages | `ectj-submission` |
| Post-decision gate | Response evidence objects assembled; resubmission clock tracked | `ectj-rebuttal`, `ectj-review-process` |

A later gate never compensates for an earlier one: polished exhibits cannot rescue a paper whose
method lacks an empirical use case at this venue.

## Worked routing pass

Illustrative vignette: an author arrives with a machine-learning-assisted estimator for demand
elasticities, strong theory, no application, and 28 draft pages.

- The evidence gate fails first: no empirical illustration, and the simulations use an i.i.d.
  design unrelated to demand data. Route to `ectj-data-analysis` with instructions to calibrate
  one DGP to a public scanner-data application.
- The compression gate fails second: 28 pages against the 20-page norm. Route to
  `ectj-writing-style` only after the application exists, because the application will consume
  pages and the compression plan must account for it.
- Conformance items (template, fee, summary) wait until the science gates close; checking them
  early wastes effort while sections still move.

Ordering principle: repair applied value before the page budget, and the page budget before
portal mechanics.

## Venue facts that gate every route

Keep these EctJ constants loaded while routing, reverifying volatile ones on live pages:

- A Royal Economic Society journal published by Oxford University Press; submission runs through
  Editorial Express with a flat fee plus VAT.
- Roughly 20 printed pages including the printed appendix; summary within 150 words; proofs in
  the main text or printed appendix rather than the online supplement.
- An empirical application is the norm even for theory-led methods papers, and simulation results
  are summarized within about a page of main text.
- The replication package — README, software versions, documented data, seeded code — becomes
  binding conditional on acceptance.
- One-week screen, three-month decision target, one-month normal resubmission window.

## Output format

```text
[Current stage] idea / theory / empirics / drafting / submission / review / R&R / accepted
[Next EctJ skill] <skill name>
[Main bottleneck] <fit, assumptions, application, compression, replication, or response>
[One-week screen risk] <highest conformance or scope issue>
[Next action] <single concrete task>
```
