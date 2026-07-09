---
name: conext-review-process
description: Use when reasoning about how an ACM CoNEXT submission is evaluated, covering double-anonymous review, the two-round TPC process with online discussion and a TPC meeting, the Accept / Reject / one-shot "major" revision decision categories, the journal-style revise-and-resubmit re-read by the original reviewers, shepherding, and how CoNEXT's two-cycle process differs from SIGCOMM and NSDI.
---

# CoNEXT Review Process

Model the pipeline before interpreting any single review. CoNEXT's process is **journal-style**:
papers are PACMNET articles, and the **one-shot "major" revision is a first-class decision**, not a
soft rejection. The most consequential mental shift for authors arriving from a plain accept/reject
conference is that a major revision is a genuine revise-and-resubmit round re-read by the same
reviewers — closer to a journal R&R — and that you get exactly **one** shot at it.

## Process model

- Submission and review run on **HotCRP** with **double-anonymity**: authors and reviewers are
  mutually hidden through reviewing.
- Review proceeds in **two rounds** by TPC members, with **online discussion** and a **TPC
  meeting**; strong early-round papers advance, and clearly-below-bar papers may receive an
  **early-reject** notification partway through the cycle.
- First decisions fall into **Accept**, **Reject**, or a **one-shot major revision**. A major
  revision arrives with a **summary of merits** and a list of **minimum necessary changes**;
  authors get roughly **two months** to revise, and the **same reviewers** re-read the revision for
  a final accept/reject.
- Conditionally accepted or revised papers are typically **shepherded** by a designated TPC member
  who confirms the required changes were made before camera-ready.
- Accepted papers publish in **PACMNET**, scheduled to the closest issue, so final metadata,
  camera-ready compliance, and reproducibility follow-through matter as much as the initial verdict.

## Reading a decision against the categories

| Decision | What it means | Author move |
|---|---|---|
| Accept | Contribution and evidence hold; minor polish only | Camera-ready + (optional) badge; do not reopen scope |
| One-shot major revision | Repairable gaps: a missing measurement, an unfair baseline, an unclear claim | Treat as a one-shot R&R: make or explicitly decline every "minimum necessary change," evidenced |
| Reject | Structural: wrong evaluation platform, no credible baseline, thin contribution | Reframe or reroute (SIGCOMM/NSDI/IMC/SIGMETRICS or the other cycle), do not lightly resubmit unchanged |

The strategic reading: write the initial submission so that whatever is weakest is **fixable inside
the revision window** (a measurement you can add, a baseline you can tune) rather than **structural**
(an evaluation platform you cannot rebuild in two months). The process rewards repairable papers, and
because the revision is **one shot**, a half-addressed change list is what turns it into a rejection.

## How CoNEXT differs from its siblings

- **vs. SIGCOMM:** SIGCOMM runs a single annual deadline and its own revision flavor; CoNEXT's
  identity is the **two cycles a year** feeding one program and the **PACMNET** journal framing.
  Never assume the two share a calendar, template, or revision mechanics.
- **vs. NSDI:** NSDI runs multiple deadlines with its own revision path too, but on the USENIX side
  with its own proceedings; CoNEXT's revision lands in a **PACMNET issue**. Do not carry NSDI's
  timing or format across.
- **vs. IMC:** IMC is measurement-focused and single-deadline; a CoNEXT measurement paper is judged
  alongside systems and architecture work in the same program, and can enter via either cycle.

## Who reads you

Expect a panel of networking TPC members matched to your subarea — systems, measurement,
architecture, wireless. They look for evidence on the **real target platform** (a testbed,
deployment, or trace, not a simulation standing in for hardware), check whether claims outrun the
measurements, ask whether baselines are real and fairly tuned, and often open the artifact. Vague
methodology gets caught in the two-round discussion, not skimmed.

## Where author leverage actually exists

```text
[Before submission]  topic tags + cycle choice -> reviewer pool and calendar   (largest lever)
[Round-1/early]      factual corrections, targeted evidence, clarifying misreadings
[One-shot revision]  the strongest lever: a tracked-change revision + point-by-point,
                     anonymous response letter re-read by the same reviewers, checked by a shepherd
[After reject]       no appeal; reroute to a sibling venue or the other cycle
```

A response moves borderline papers when it corrects a factual misreading or supplies a measurement a
reviewer said was missing; it does not move papers when it argues taste. In a one-shot revision,
**silent omissions** — a listed minimum-necessary change neither made nor explicitly declined with a
reason — are what the second read punishes hardest.

## Reading a review packet

Weight reviews before answering. A review that cites your section numbers, figures, and testbed
setup was read closely and will be read closely again in the revision — its author is your likely
advocate if the response holds. A review that discusses only novelty has left soundness and
reproducibility to the others; answer each reviewer on the axis they raised. The major-revision
change list is the scoring rubric for the second read: treat every item as mandatory unless you can
justify declining it.

## Misreadings to avoid

- **Treating a major revision as a guaranteed accept** — the second read is real and one-shot;
  budget the two-month window like a deadline.
- **Treating the response as a debate** — the TPC discussion and shepherd decide; your text is
  evidence for an advocate, not a closing argument.
- **Assuming unanimity is required** — a champion with answers to the other reviews can carry a
  paper through discussion.
- **Projecting one cycle onto the other** — the two cycles share a program but re-post their own
  dates; confirm the one you are in.

## Output format

```text
[Process stage] pre-submission / awaiting reviews / one-shot revision / final / accepted
[Cycle] December / June
[Decision category] accept / one-shot major revision / reject, with the criterion driving it
[Criterion map] each review point -> significance | soundness | measurement quality | baselines | clarity | reproducibility
[Leverage plan] the next-stage action that can actually change the outcome
[Forbidden moves] identity leak (incl. in the response letter) / unsupported new claims
```
