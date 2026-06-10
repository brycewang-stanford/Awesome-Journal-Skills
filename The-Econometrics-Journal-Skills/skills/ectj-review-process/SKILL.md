---
name: ectj-review-process
description: Use when interpreting or planning around The Econometrics Journal's one-week editorial screen, editor assignment, three-month decision target, resubmission window, conformance rejection, and replication checks.
---

# EctJ Review Process

Use this to plan around the RES review pipeline. Do not infer the peer-review blinding model;
the current official pages reviewed for this pack do not name it.

## Process model

- RES states that conforming EctJ submissions are screened by the Editor-in-Chief and
  possibly an editor.
- Within about one week, a paper can be desk-rejected or assigned to an editor.
- RES states a target of a decision within about three months.
- Resubmissions are normally expected within one month, sometimes three.
- Formatting nonconformance is not cosmetic; official instructions say nonconforming
  submissions are routinely rejected.
- Replication package compliance becomes decisive after conditional acceptance.

## Planning implications

- Treat the first week as a **scope and conformance gate**: summary, page length, proofs placement, fee,
  application, and template issues can kill the paper before referees see the technical details.
- Treat the three-month target as a reason to submit a complete package. Thin simulations or missing code
  will become a revision bottleneck rather than a harmless omission.
- If desk risk is high, fix the summary and opening two pages first; that is where the editor sees whether
  the paper is leading-case econometrics or a field application with a method appendix.

## Desk-screen packet

Prepare a five-item packet for the editor-facing opening:

1. 150-word-or-less summary that names the econometric object and applied value.
2. First-page theorem/result sentence with the leading-case scope.
3. One paragraph showing the closest incumbent method and what breaks.
4. One sentence identifying the empirical application and why it is not decorative.
5. One sentence on where proofs, simulations, and replication files live.

## Conformance triggers behind one-week desk rejections

The RES conformance-rejection rule makes format failures fatal at the screen, not cosmetic. Map
each trigger to its governing rule before submitting:

| Trigger | Governing RES rule | Pre-screen fix |
|---|---|---|
| Printed paper over the page norm | Not normally exceeding 20 pages including the printed appendix | Compress via `ectj-tables-figures` and `ectj-writing-style` |
| Summary over the word limit | Summary of no more than 150 words | Rewrite around the econometric object plus applied value |
| Proofs parked online | Proofs belong in the main text or printed appendix | Repatriate derivations, rebalance the page budget |
| No empirical application | Application expected even for theory papers | Add a diagnostic application, not an afterthought |
| Wrong template or missing fee | RES/EctJ LaTeX template; flat fee plus VAT | Recompile in template, confirm the fee path on the live page |

## Illustrative pipeline calendar

Plan backwards from the RES timing statements (dates illustrative; confirm policies against the
journal's current author guidelines):

- Week 0: submit via Editorial Express, fee paid, replication restrictions disclosed.
- Week 1: screen outcome — desk rejection or assignment to an editor.
- Months 1-3: referee reports under the three-month decision target; use this time to harden the
  replication package rather than waiting idle.
- Decision plus one month: the normal resubmission window for an R&R; request the three-month
  window early if new simulations are needed, rather than missing the clock silently.

The screen evaluates conformance and leading-case scope; the referee stage evaluates the
theory-simulation-application chain. Preparing for the second stage never substitutes for passing
the first.

## Signals to extract from each stage

- A desk rejection within days usually signals scope or conformance, not refereeing depth;
  re-read the leading-case framing before blaming the method.
- An assignment past the first week means referees will judge the theory-simulation-application
  chain; pre-draft answers for the weakest link now.
- Slippage past the three-month target supports one polite status query through the editorial
  office (ectj@res.org.uk), not serial chasing.
- At conditional acceptance the binding constraint becomes the replication package; schedule the
  full rerun before celebrating.

## Output format

```text
[Stage] pre-screen / under review / R&R / conditional acceptance / accepted
[Screen risk] <scope, format, page, application, fee, or replication>
[Likely editor question] <one sentence>
[Resubmission clock] <deadline or unknown>
[Next move] <specific action>
```
