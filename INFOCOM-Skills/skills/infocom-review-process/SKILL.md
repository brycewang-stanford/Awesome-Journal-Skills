---
name: infocom-review-process
description: Use when reasoning about how an IEEE INFOCOM submission is evaluated, covering the large-scale double-blind pipeline, automated paper-reviewer assignment, the two-tier TPC and early-reject phase, the (traditional) absence of an author rebuttal, TPC discussion, and how INFOCOM's process differs from SIGCOMM/NSDI rebuttal-driven reviewing.
---

# INFOCOM Review Process

Model the pipeline before interpreting any single review. INFOCOM's process is **large-scale and
TPC-driven**: thousands of submissions are matched to a broad Technical Program Committee by an
**automated assignment system**, screened through an **early-reject** phase, and decided in TPC
discussion. The most consequential mental shift for authors arriving from SIGCOMM/NSDI is that
INFOCOM has **traditionally offered no author rebuttal** — the submitted PDF must defend itself,
because you likely never get a turn to reply.

## Process model

- Submission and review run on **EDAS** with **double-blind** anonymity: identities are hidden from
  reviewers throughout.
- **Automated review assignment** matches each manuscript to TPC members by comparing the paper's
  content to reviewers' representative publications. Your topic tags and abstract are the levers
  that route you to the right subarea — a mis-tagged paper lands with reviewers who read it as a
  visitor.
- **Early-reject phase.** INFOCOM 2027 posts an **early-reject notification (9 Oct 2026)** weeks
  before the final acceptance notification (8 Dec 2026). Papers that are out of scope, violate the
  double-blind/length rules, or draw uniformly weak initial scores are cut here without reaching the
  full discussion.
- **TPC discussion and final decision** (INFOCOM 2026: 8 Dec 2025). Surviving papers are debated by
  the assigned TPC members, often with an area/vice chair moderating, and accepted or rejected.
- Accepted papers publish in the **IEEE INFOCOM Proceedings and IEEE Xplore**.

## Reading a decision against the categories

| Decision | What it means | Author move |
|---|---|---|
| Early reject | Screened out before full discussion: scope, compliance, or uniformly low scores | Do not appeal; diagnose honestly and reroute or substantially rework |
| Reject (final) | Survived the screen but lost in discussion: a real weakness the reviewers agreed on | Reframe or reroute (SIGCOMM/NSDI/ICNP or a journal); fix the named weakness before resubmitting |
| Accept | Contribution and evidence hold | Camera-ready + IEEE Xplore production; register an author |

Because there is usually no rebuttal, the strategic reading runs **before** submission: anticipate
the reviewer's first objection (an untuned baseline, an unstated assumption, a proof gap) and close
it in the PDF, since you will not get to close it in a reply.

## How INFOCOM differs from its siblings

- **vs. SIGCOMM / NSDI:** those are small, highly selective ACM/USENIX venues with a **rebuttal**
  and a systems-building, artifact-heavy culture. INFOCOM is **large**, IEEE, double-blind on EDAS,
  with **automated assignment**, an **early-reject** screen, and (traditionally) **no rebuttal** —
  and it welcomes analytical/optimization contributions that SIGCOMM often routes elsewhere.
- **vs. ICNP:** ICNP is a smaller IEEE protocols venue; INFOCOM's breadth and scale are its
  identity. Do not assume a shared reviewer pool or timeline.
- **vs. IEEE/ACM ToN or JSAC:** the journals have no page ceiling and a revise-and-resubmit cycle;
  INFOCOM is a single-shot conference decision with a hard nine-page budget. A study too long or too
  incremental for INFOCOM's page limit may belong in the journal.

## Who reads you

Expect a handful of TPC reviewers drawn by the assignment system from your declared subarea. In a
broad venue they may span pure theory to pure systems, so a paper must be legible to both: an
optimization result needs an intuition and a plausible deployment story; a systems result needs its
assumptions and a fair comparison. Vague method descriptions and unfair baselines are the classic
INFOCOM rejects — reviewers in a crowded pool reward papers that are easy to check and hard to
dismiss.

## Where author leverage actually exists

```text
[Before submission]  topic tags + abstract -> reviewer pool via automated assignment  (largest lever)
[In the PDF]         pre-empt the obvious objection; the paper is your only argument
[Early-reject stage] no appeal; treat the cut as signal, not noise
[After reject]       no rebuttal existed to blame; fix the named weakness, reroute or resubmit next cycle
[If a cycle adds a response window]  answer only the decision-critical, verifiable points (待核实)
```

Since the traditional process gives no reply turn, the highest-leverage move is **defensive
writing**: the threats to a claim, the assumption behind a theorem, and the fairness of a baseline
must all be visible in the submitted pages.

## Misreadings to avoid

- **Expecting a rebuttal.** Do not hold back an answer "for the response" — there usually is none
  (verify the current cycle; 待核实).
- **Treating early-reject as a fluke.** It is a deliberate screen; a uniform low score means the
  paper did not read as INFOCOM-ready.
- **Under-tagging the topic.** The automated assignment is only as good as your metadata; wrong
  tags route you to the wrong readers.
- **Assuming SIGCOMM norms.** Artifact-heavy, rebuttal-driven expectations do not transfer.

## Output format

```text
[Process stage] pre-submission / under review / early-reject / final decision / accepted
[Decision category] early-reject / reject / accept, with the criterion driving it
[Assignment risk] do topic tags + abstract route to the right subarea? yes/no
[Defensive-writing gaps] <objections to pre-empt in the PDF, since no rebuttal>
[If response window exists] <the decision-critical points to answer (待核实 the window itself)>
```
