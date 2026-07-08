---
name: icse-review-process
description: Use when reasoning about how an ICSE research-track submission is evaluated, covering double-anonymous PC review, the four posted criteria, the Accept / Major Revision / Reject decision model, the revision-and-final-decision timeline, and what recent ICSE acceptance statistics imply for strategy.
---

# ICSE Review Process

Model the pipeline before you interpret any single review. ICSE's process
differs from most CS conferences in one structural way: **Major Revision is a
real decision category**, not a euphemism for rejection, and a large share of
accepted papers arrive through it.

## The four scored criteria

The ICSE 2027 call (read 2026-07-08) evaluates each paper on:

1. **Novelty** — originality of solutions, problem formulations, methodologies,
   theories, or evaluations relative to the state of the art.
2. **Rigor** — soundness, clarity, and depth of the technical or theoretical
   contribution, and thoroughness/completeness of the evaluation.
3. **Relevance** — significance and potential impact on software engineering.
4. **Verifiability and Transparency** — whether the paper contains enough
   information to understand how the innovation works, how data was obtained
   and analyzed, and whether independent verification or replication is
   supported.

Read every review comment as an instance of one of these. "The benchmark seems
small" is a Rigor objection; "practitioners would not use this" is Relevance;
"the prompt templates are not shown" is Verifiability. Diagnosing the criterion
tells you whether the cure is new evidence, new framing, or new packaging.

## Decision model and 2027 timeline

| Stage (2027 cycle) | Date | What happens |
|---|---|---|
| Submission closes | Jun 30, 2026 AoE | PC bidding and assignment follow |
| Author response | Sep 2026 | Authors see reviews and reply (format 待核实) |
| First decisions | Oct 20, 2026 | Accept / Major Revision / Reject |
| Revision due | Nov 17, 2026 | Revised paper + response for MR papers |
| Final MR decisions | Dec 18, 2026 | Accept or Reject, no second revision |
| Conference | Apr 25 – May 1, 2027 | Dublin; core days Apr 28–30 |

Two consequences. First, a Major Revision gives you roughly **four weeks** to
execute — reviewers expect the revision plan to be feasible in that window, so
promising a new user study is self-defeating. Second, the December decision is
terminal for the cycle: there is no minor-revision escape hatch after it.

## What the recent numbers say

ICSE 2026 (the last two-cycle year) reported, per its research-track pages:
Cycle 1 — 660 submissions, 60 direct accepts, 101 accepted after Major
Revision; Cycle 2 — 809 submissions, 72 direct accepts, 88 accepted after
Major Revision; 321 of 1,469 total (~22%). The strategic reading: **direct
acceptance is rare (~9%)** — the modal successful path runs through Major
Revision. Write the initial submission so that its weaknesses are *revisable*
(missing analysis, unclear framing) rather than structural (wrong population,
no baseline), because the process is built to reward repairable papers.

## Who reads you

Reviews come from a large research-track Program Committee working
double-anonymously; ICSE also runs a Shadow PC in some years (2027 posts one)
where early-career researchers review in parallel for training — their reviews
do not decide outcomes but signal how a non-expert reads your paper. Expect
three reviews with SE-empiricist instincts: they will look for the threats-to-
validity section, check whether claims outrun evidence, and often open the
replication package.

## Where author leverage exists

```text
[Before submission]   topic tags -> reviewer pool     (largest lever)
[Author response]     factual corrections, criterion-targeted evidence
[Major Revision]      the strongest lever in the system: a tracked-change
                      revision + response letter reviewed by the same PC members
[After final reject]  no appeal lane; reroute (FSE/ASE/ISSTA or journals)
```

Author response moves borderline papers when it corrects a factual
misreading or supplies a number a reviewer said was missing. It does not move
papers when it argues taste. Major Revision moves papers when every requested
change is either made or explicitly declined with a reason — silent omissions
are what turn December into a rejection.

## Reading a review packet

Weight reviews before answering them. Look for: **specificity** — a review
citing your section numbers and exact tables was read closely and will be
read closely again in December; **criterion coverage** — a review that only
discusses novelty has left rigor and verifiability to the others, so answer
those reviewers on those axes; **the question list** — reviewers often end
with explicit questions, and the September response is scored heavily on
whether each got a direct answer. A short, vague, positive review is worth
less protection than a long, critical, specific one: the latter's author is
your likely advocate if the response holds up.

## Misreadings to avoid

- **Treating Major Revision as a soft accept.** ICSE 2026's numbers show most
  MR papers do get in, but the December reject is real; budget the four weeks
  like a deadline, not a formality.
- **Treating the response as a debate stage.** The PC discussion after the
  response is where decisions form; your text is evidence for an advocate, not
  a closing argument to a jury.
- **Assuming reviewer unanimity is required.** Discussion consensus, guided by
  the criteria, decides — one enthusiastic champion with answers to the other
  reviews can carry a paper.
- **Projecting the two-cycle rhythm forward.** 2025 and 2026 ran two cycles;
  2027 posts one. Never infer next year's calendar from last year's.

## Output format

```text
[Process stage] pre-submission / awaiting reviews / response / major revision / final
[Criterion map] each review point -> novelty | rigor | relevance | verifiability
[Decision forecast] direct accept / MR-likely / reject-risk, with reasons
[Leverage plan] what to do at the next stage that can actually change the outcome
```
