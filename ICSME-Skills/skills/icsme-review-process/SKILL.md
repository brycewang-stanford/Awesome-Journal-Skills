---
name: icsme-review-process
description: Use when reasoning about how an IEEE ICSME research submission is evaluated, covering double-anonymous review, the early-decision cut that issues Accept/Reject before the rebuttal, the "Response Recommended" author-response period, the single-round accept/reject model with no Major Revision, and how ICSME's process differs from FSE's journal-style round and ICSE's cycles.
---

# ICSME Review Process

Model the pipeline before interpreting any single review. ICSME's process is **conference-style
and single-round**: papers are reviewed once, double-anonymously, and the outcome is accept or
reject — there is **no journal-style Major Revision**. The distinctive mechanism authors must plan
for is the **early-decision cut**: before the rebuttal even opens, the strongest and weakest papers
are already decided, and only the middle is asked to respond.

## Process model

- Submission and review run on **EasyChair** with **double-anonymity**: author identities are
  hidden from reviewers throughout.
- Each paper is read by multiple program-committee members who weigh the significance of the
  maintenance/evolution contribution, soundness of method, quality and honesty of the empirical
  evidence (mined data, subject systems, statistics), threats-to-validity reasoning, clarity, and
  open-science support.
- At the **start of the author-response period** the PC issues an early decision:
  - **Accept** — reviewers agree the paper is publishable as is; no response requested.
  - **Reject** — reviewers judge the paper too deficient for a response to change; no response
    requested.
  - **Response Recommended** — the paper is in contention; authors may answer the PC's specific
    questions.
- After responses and PC discussion, a **final accept/reject** is issued. Accepted papers publish
  in **IEEE Xplore**.

## Reading your early decision

| Early decision | What it means | Author move |
|---|---|---|
| Accept | Contribution and evidence hold; polish only | Camera-ready + ROSE artifact; do not reopen scope |
| Response Recommended | Genuinely in contention; specific PC questions decide it | Answer each question with existing evidence; correct misreadings |
| Reject (early) | Structural: wrong scope, no credible baseline, thin/confounded study | Reroute (SANER/SCAM/journal) or rebuild; do not resubmit unchanged |

The strategic reading: because there is no revision round, **write the initial submission so the
evidence is already complete.** An ICSME reviewer cannot ask you to add an analysis and wait — they
either believe the paper now or they do not. The rebuttal moves papers by resolving a specific
doubt, not by promising future work.

## How ICSME differs from its siblings

- **vs. ESEC/FSE:** FSE papers are PACMSE journal articles with a real **Major Revision**
  revise-and-resubmit round. ICSME has **no such round** — it is single-shot with an early-decision
  cut and a rebuttal. Never plan an ICSME submission as if a revision will rescue thin evidence.
- **vs. ICSE:** ICSE is the general-SE flagship on a larger stage with its own (sometimes
  multi-cycle) structure. ICSME is the maintenance/evolution-focused venue; a paper accepted at
  either would differ in framing, not just calendar.
- **vs. MSR/SCAM:** its co-located siblings review mining-for-its-own-sake and source-analysis
  machinery; ICSME reviewers ask what the maintenance *payoff* is.

## Who reads you

Expect maintenance and evolution empiricists. They check whether subject systems are real and
evolving, whether the mined corpus is provenance-pinned, whether baselines are fair, whether the
threats-to-validity section argues rather than recites, and they often open the artifact. Because
ICSME spans techniques, empirical studies, comprehension, and replication, a paper is matched to
reviewers from its own subarea — vague method descriptions get caught, not skimmed.

## Where author leverage actually exists

```text
[Before submission]  topic tags + subject-system realism -> reviewer pool & credibility (largest lever)
[Early-decision cut] nothing to do once issued; it reflects the submitted paper alone
[Response Recommended] the single rebuttal: answer the PC's exact questions with existing evidence
[After reject]       no appeal; reroute to a sibling, a journal, or Registered Reports next cycle
```

A response moves borderline papers when it corrects a factual misreading or supplies a number a
reviewer said was missing *and that already exists in the artifact*; it does not move papers when it
argues taste or promises new experiments. Silence on a PC question the response was invited to
answer is read as inability to answer it.

## Reading a review packet

Weight reviews before answering. A review that cites your section numbers, tables, and threats was
read closely; its author is your likely advocate if the response holds. Because there is no second
read, the PC discussion is where the decision is actually made — write the response as evidence for
that discussion, addressed to the specific questions the PC flagged.

## Misreadings to avoid

- **Expecting a revision round** — there is none; the paper is judged as submitted.
- **Treating "Response Recommended" as bad news** — it means you are in contention and the rebuttal
  matters; an early Accept or Reject is the terminal signal.
- **Treating the response as a debate** — the PC discussion decides; answer questions, do not argue.
- **Projecting last year's cadence** — the early-decision cut and response format are decided per
  edition; confirm they are offered this cycle.

## Output format

```text
[Process stage] pre-submission / awaiting early decision / response period / final / accepted
[Decision category] early accept / response recommended / early reject / final accept / final reject
[Criterion map] each review point -> significance | soundness | evidence | threats | clarity | open-science
[Leverage plan] the response-period answer that can actually change the outcome
[Forbidden moves] identity leak / promising new experiments as if they were done
```
