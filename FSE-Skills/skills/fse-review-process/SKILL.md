---
name: fse-review-process
description: Use when reasoning about how an ESEC/FSE research submission is evaluated, covering double-anonymous "heavy" review, the at-least-three-reviewer PC model, the Accept / Major Revision / Reject decision categories, the journal-style revise-and-resubmit round of PACMSE, and how FSE's process differs from ICSE's cycles and ISSTA's rounds.
---

# FSE Review Process

Model the pipeline before interpreting any single review. FSE's process is **journal-style**:
papers are PACMSE articles, and **Major Revision is a first-class decision**, not a soft rejection.
The most consequential mental shift for authors arriving from a plain accept/reject conference is
that a Major Revision is a genuine revise-and-resubmit round with the same reviewers, closer to a
journal R&R than to a rebuttal.

## Process model

- Submission and review run on **HotCRP** with **heavy double-anonymity**: identities are hidden
  through all reviewing *and* discussion, and any Major Revision response must itself be anonymous.
- Each paper is read by **at least three** program-committee members (FSE 2027 call), who weigh
  the significance of the SE contribution, soundness of the method, quality and honesty of the
  empirical evidence, threats-to-validity reasoning, clarity, and open-science support.
- First decisions fall into **Accept**, **Major Revision**, or **Reject**. A Major Revision is
  re-reviewed — generally by the original reviewers — against the revision and its response letter.
- Accepted papers publish in **PACMSE**, so final metadata, camera-ready compliance, and artifact
  follow-through matter as much as the initial verdict.

## Reading a decision against the categories

| Decision | What it means | Author move |
|---|---|---|
| Accept | Contribution and evidence hold; minor polish only | Camera-ready + artifact; do not reopen scope |
| Major Revision | Repairable gaps: missing analysis, unclear construct, a needed baseline | Treat as an R&R: make or explicitly decline every request, evidenced |
| Reject | Structural: wrong population, no credible baseline, thin contribution | Reframe or reroute (ICSE/ASE/ISSTA or a journal), do not lightly resubmit unchanged |

The strategic reading: write the initial submission so that whatever is weakest is **revisable in
a revision round** (an analysis you can add, a threat you can bound) rather than **structural** (a
study design you cannot redo in weeks). The process is built to reward repairable papers.

## How FSE differs from its siblings

- **vs. ICSE:** ICSE has run its own cycle structure (a two-cycle model in some years, single in
  others) with an Accept/Major-Revision/Reject flavor too, but on the IEEE side. FSE's identity is
  the **PACMSE journal** framing and the SIGSOFT open-science defaults. Never assume the two share
  a calendar or template.
- **vs. ISSTA:** ISSTA has used multi-round reviewing within a cycle; FSE's revise-and-resubmit is
  a *decision-driven* round (you revise because you were told to), not a scheduled second read of
  every paper.
- **vs. the FSE 2024 dual-deadline year:** FSE once let a Major Revision resubmit to a *later*
  deadline within the same review year. Recent calls advertise a single annual deadline with the
  revision round inside it — confirm the current cadence rather than carrying either forward.

## Who reads you

Expect three SE-empiricist reviewers. They look for the threats-to-validity section, check whether
claims outrun evidence, ask whether subjects and baselines are real and fair, and often open the
artifact. Because FSE spans techniques, empirical studies, and human factors, a paper is usually
matched to reviewers from its own subarea — vague method descriptions get caught, not skimmed.

## Where author leverage actually exists

```text
[Before submission]  topic tags -> reviewer pool           (largest lever)
[Initial reviews]    factual corrections, targeted evidence, clarifying misreadings
[Major Revision]     the strongest lever: a tracked-change revision + point-by-point,
                     anonymous response letter re-read by the same reviewers
[After reject]       no appeal; reroute to a sibling flagship or an SE journal
```

A response moves borderline papers when it corrects a factual misreading or supplies a number a
reviewer said was missing; it does not move papers when it argues taste. In a Major Revision,
**silent omissions** — a requested change neither made nor explicitly declined with a reason — are
what turn the second read into a rejection.

## Reading a review packet

Weight reviews before answering. A review that cites your section numbers, tables, and threats was
read closely and will be read closely again in the revision round — its author is your likely
advocate if the response holds. A review that discusses only novelty has left soundness and
verifiability to the others; answer each reviewer on the axis they raised. Reviewers often end with
an explicit question list; the revision is scored heavily on whether each question got a direct,
evidenced answer.

## Misreadings to avoid

- **Treating Major Revision as a guaranteed accept** — the second read is real; budget the
  revision window like a deadline.
- **Treating the response as a debate** — the PC discussion decides; your text is evidence for an
  advocate, not a closing argument.
- **Assuming unanimity is required** — a champion with answers to the other reviews can carry a
  paper through the discussion.
- **Projecting last year's cadence** — deadline count and revision timing are decided per edition.

## Output format

```text
[Process stage] pre-submission / awaiting reviews / major revision / final / accepted
[Decision category] accept / major revision / reject, with the criterion driving it
[Criterion map] each review point -> significance | soundness | evidence | threats | clarity | open-science
[Leverage plan] the next-stage action that can actually change the outcome
[Forbidden moves] identity leak (incl. in the response letter) / unsupported new claims
```
