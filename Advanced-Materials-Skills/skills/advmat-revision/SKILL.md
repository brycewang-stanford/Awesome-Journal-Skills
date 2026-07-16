---
name: advmat-revision
description: Use when responding to Advanced Materials reviewer reports and an editor's decision — major or minor revision, or a rejection with a resubmission or transfer path. Structures the response and the manuscript changes; does not perform the underlying new experiments.
---

# Advanced Materials Revision (advmat-revision)

## When to trigger

- Reviewer reports and an editor decision (major/minor revision, or reject) have arrived
- You need a point-by-point response and a marked-up manuscript
- Referees asked for additional characterization, benchmarking, or stability data
- The decision is a rejection and you must decide: appeal, revise-and-resubmit, or transfer
- A coauthor is drafting rebuttal language before the manuscript has actually changed

## Read the decision before the reports

The editor's letter sets the terms; read it first.

- **Minor revision** — largely presentational or small additions; turn it around promptly and precisely.
- **Major revision** — substantive concerns; usually requires *new data* (added characterization, controls, stability). Address the science first, the prose second.
- **Reject with encouragement to resubmit** — treat as a major revision with a higher bar; the resubmission is judged largely on whether the core objection is truly resolved.
- **Reject** — decide between a reasoned appeal (only if the editor/referee made a clear factual error) and a **transfer** to a sibling Wiley journal (Adv. Funct. Mater., Adv. Sci., Small, AMI), which may carry the reviews with it.

## Response-letter structure

- **Open with thanks and a summary** of the main changes and the new data added.
- **Quote each referee point verbatim**, then respond immediately beneath it.
- For every point: state **what you changed**, **where** (section/figure/SI number), and **the evidence**. "We added X" with a pointer beats a paragraph of argument.
- Where you disagree, do so **with data and courtesy** — concede what is fair, defend what the evidence supports, never dismiss.
- Provide a **marked-up manuscript** (tracked changes or highlighted) alongside the clean version.

## Answering the characteristic materials objections

| Referee asks for...                          | Strongest response                                                    |
|----------------------------------------------|------------------------------------------------------------------------|
| Proof the phase/structure is real            | Add the complementary technique (SAED, EXAFS, Rietveld) they expect    |
| Representative morphology                     | Add distributions/statistics over many particles/devices              |
| Fair benchmarking                             | Add a matched-condition comparison table with cited SOTA references    |
| Stability / durability                        | Add cycling/aging/operational-stability data (often to the SI)         |
| Mechanism, not just correlation               | Add the control or computation that isolates the mechanism             |
| Reproducibility                               | Add batch-to-batch statistics (n, mean ± s.d.) and full recipe in SI   |
| "Why not a lower-tier journal?"               | Sharpen the advance framing and the broad-impact argument              |

Do the experiment when the objection is fair. A rebuttal that argues around missing data rarely survives a second round.

## Scope discipline in revision

- Add what the referees asked for; resist bolting on unrelated new results that reopen the length budget.
- Keep the central advance fixed — a revision that changes the headline claim reads as a new paper.
- Re-run the fit and pointer audits after adding data (see `advmat-length-management`, `advmat-submission`): new figures may push you over the page budget or break cross-references.

## Checklist

- [ ] The editor's decision terms are understood before drafting
- [ ] Every referee point is quoted and answered individually
- [ ] Each response states what changed, where, and the evidence
- [ ] Requested new characterization / benchmarking / stability data actually added
- [ ] Disagreements are backed by data and phrased courteously
- [ ] A marked-up manuscript accompanies the clean version
- [ ] Length budget and all cross-references re-checked after additions
- [ ] The central advance is unchanged; scope creep avoided

## Anti-patterns

- Arguing around a fair request for data instead of providing it
- Drafting rebuttal language before the manuscript and data are actually updated
- Dismissive or defensive tone toward a referee
- Silent changes not flagged in the response letter or the markup
- Adding unrelated new results that reopen length and consistency problems
- Appealing a rejection on preference when the referee raised a valid scientific gap

## Output format

```
【Decision type】minor / major / reject-resubmit / reject → (appeal? transfer?)
【Per-point responses】R1.1 change+location+evidence / R1.2 ... / R2.1 ...
【New data added】characterization / benchmarking / stability / mechanism — list
【Disagreements】point — data-backed rationale
【Markup + clean versions】ready?  yes / fix
【Length & cross-refs re-audited】yes / fix
【Next】advmat-submission (re-preflight) or transfer to sibling journal
```

> Revision formats, appeal routes, and transfer options are set by Wiley and evolve — verify current options on the official Advanced Materials author page and in the editor's letter.
