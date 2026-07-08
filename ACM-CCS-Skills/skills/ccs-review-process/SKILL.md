---
name: ccs-review-process
description: Use when explaining or planning around ACM CCS peer review, the two-cycle HotCRP workflow, decision categories including minor revision, the rebuttal window, the adversarial reviewer pool, ethics and disclosure scrutiny, meta-review dynamics, and ACM proceedings outcomes.
---

# CCS Review Process

Use this to reason about review-stage strategy. Reopen the current CFP, the cycle's HotCRP
site, the reviewer guidelines if posted, and the ethics policy before making process claims.

## Process model

- CCS runs two review cycles per year on HotCRP, each with abstract registration, full-paper
  submission, review, a rebuttal window, and notification.
- Reviewers assess threat-model soundness, novelty, technical correctness, evidence quality,
  ethics and responsible disclosure, and significance to the security community.
- Decisions are not binary: CCS 2026 used accept, minor revision (authors revise for the same
  cycle under a shepherd or check), and reject. A first-cycle reject cannot return that year.
- An ethics or disclosure concern can sink an otherwise strong paper; the ethics reviewer's
  view carries weight independent of technical scores.
- Accepted papers publish in the ACM Digital Library proceedings, so camera-ready and metadata
  compliance matter as much as the initial decision.

## Who reviews here

- The pool is adversarial by training: expect at least one reviewer to attack your threat
  model, look for the assumption that makes the attack easy, and probe whether the defense was
  tested against an adaptive attacker.
- CCS is broad, so a paper may draw reviewers from an adjacent sub-area; the threat model and
  intro must orient a web-security reviewer to a crypto result and vice versa.
- Borderline papers usually fall on one of three edges: an attacker assumption too strong to
  be interesting, a defense never adapted against, or an ethics gap left unaddressed.

## Scoring leverage table

| Review dimension | What raises it | What sinks it |
|---|---|---|
| Threat model | A tight, realistic adversary stated up front | Capabilities that quietly grow to make the attack work |
| Novelty | An attack class or guarantee the literature lacked | An increment over a cited paper with no new idea |
| Evidence | End-to-end demonstration against a real target | Lab-only results against a strawman |
| Ethics | Disclosure done, harm minimized, reasoned in the paper | Real-world harm with no disclosure or IRB reasoning |

## Stage-by-stage realism

- Initial reviews: triage by what the meta-reviewer will weigh — threat model and evidence —
  not by reviewer tone.
- Rebuttal: the window is short and structured; one crisp answer to the decision-critical
  objection beats an exhaustive point-by-point.
- Decision: the meta-review synthesizes; one unresolved threat-model or ethics objection
  outweighs several resolved clarity complaints.
- Minor revision: treat it as conditional acceptance with a checklist, not a debate; do
  exactly what the shepherd asks within the cycle's timeline.

## Output format

```text
[Current stage] submitted / reviews / rebuttal / decision / revision / camera-ready
[Decision actors] <reviewers / ethics reviewer / meta-reviewer / chairs>
[Likely leverage] <threat model / novelty / evidence / ethics>
[Forbidden moves] <identity leak / new unsupported results / ignoring the shepherd>
[Next response move] <one action>
```
