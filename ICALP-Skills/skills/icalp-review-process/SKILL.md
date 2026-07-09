---
name: icalp-review-process
description: Use when reasoning about how an ICALP (EATCS) submission is evaluated, covering lightweight double-blind review, the separate Track A and Track B program committees, the asymmetric author interaction (Track B rebuttal vs Track A correctness-only contact), correctness-driven acceptance, the single accept/reject decision, and how ICALP's process differs from STOC/FOCS/SODA.
---

# ICALP Review Process

Model the pipeline before interpreting any single review. ICALP's process is **conference-style and
correctness-centered**: a paper is accepted or rejected in one round (no journal-style major
revision), and the reviewers' overriding job is to judge whether the **theorems are significant and
the proofs are correct**. The most consequential thing to internalize is that the two tracks run
**different processes** — Track B gives you a rebuttal, Track A generally does not.

## Process model

- Submission and review run on **HotCRP**, on **separate servers per track**, under **lightweight
  double-blind**: identities are hidden for an unbiased first read, self-references are third person,
  but the regime is deliberately not adversarial about de-anonymization.
- Each paper is refereed by the track's **program committee** (often with sub-reviewers who are
  subject experts), who weigh the **significance** of the result, the **correctness and depth** of the
  proofs, the **improvement over prior bounds**, and clarity.
- **Track A** (Algorithms, Complexity and Games): chairs for ICALP 2026 are **Sayan Bhattacharya** and
  **Danupon Nanongkai** (reported). Authors are contacted **only if a correctness issue** must be
  resolved — otherwise there is no interaction.
- **Track B** (Automata, Logic, Semantics and Theory of Programming): chaired by **Michael Benedikt**
  (reported). There is a **rebuttal period** (ICALP 2026: 21-24 March) where authors respond to
  initial reviews.
- Decisions are **accept / reject** in one round; accepted papers publish open-access in **LIPIcs**.

## Reading a decision against the criteria

| Decision | What it usually means | Author move |
|---|---|---|
| Accept | Result significant, proofs judged correct, improvement over prior work is clear | Camera-ready in LIPIcs; post/refresh the full version; arrange a presenter |
| Reject (borderline) | Correct but incremental, or a proof gap the referees could not close in time | Strengthen or reframe; consider STOC/FOCS/SODA/LICS or a journal (`icalp-topic-selection`) |
| Reject (structural) | A proof is wrong or the model/claim is off | Fix the mathematics before resubmitting anywhere; do not merely re-target |

The strategic reading: because there is **no revision round**, the submission must be **correct and
complete at deadline**. A believable-but-unwritten proof is the classic ICALP rejection — reviewers
cannot accept what they cannot check in the appendix or full version.

## How ICALP differs from its US siblings

- **vs. STOC / FOCS:** those are ACM/IEEE flagships with their own PCs, templates, and calendars, and
  a US-centered community. ICALP is EATCS/European, LIPIcs open-access, and **two-track**. Prestige
  and pool differ; never assume a shared calendar or format.
- **vs. SODA:** SODA is SIAM's algorithms venue with a distinct community and its own reviewing style.
  ICALP Track A overlaps in scope but is a different program committee and audience.
- **vs. journals:** ICALP is single-round accept/reject, not revise-and-resubmit. There is no major
  revision; a paper that needs one belongs in a journal (LMCS, TALG, TCS, JACM) or a later cycle.

## Who reads you

Expect **subject-matter referees** for your specific subarea and track — a matroid result is read by
someone who knows matroid intersection; a VASS result by someone who knows Petri nets. They will
**check the proofs**, not skim them, which is exactly why the full version / appendix must be complete.
A vague proof sketch with "details omitted" and no full version is caught, not trusted.

## Where author leverage actually exists

```text
[Before submission]  track choice + clean model + complete proofs      (largest lever)
[Track A]            essentially none post-submission except a correctness clarification if asked
[Track B rebuttal]   correct factual misreadings; point to the exact lemma answering an objection
[After reject]       no appeal; reroute to a sibling venue or journal, having fixed the mathematics
```

For **Track B**, a rebuttal moves a paper when it fixes a **misread** ("the reviewer thinks Lemma 4
needs X, but the hypothesis already gives it, see line ...") — not when it argues taste. For **Track
A**, the lever is almost entirely **before** submission: get the proofs complete and the exposition
clear, because you will likely not get to speak again.

## Reading a review packet

Weight reviews by how closely the proof was read. A review that cites your lemma numbers and questions
a specific step engaged the mathematics and is your most important reader — answer that step exactly
(Track B) or make sure it is airtight (Track A). A review that discusses only novelty has left
correctness to the others. Reviewers who flag a **potential gap** are giving you the single most
important signal: if they are right, no rebuttal saves it; if they misread, a precise pointer to the
proof can.

## Misreadings to avoid

- **Expecting a revision round** — there is none; the submission is the artifact of record.
- **Assuming a Track A rebuttal** — Track A contacts you only for correctness; do not bank on
  responding.
- **Treating "details in the full version" as sufficient without the full version** — reviewers must
  be able to check the proof at submission time.
- **Projecting a US-venue process onto ICALP** — the two-track split and the rebuttal asymmetry are
  ICALP-specific.

## Output format

```text
[Process stage] pre-submission / under review / Track B rebuttal / notified
[Track] A (correctness-contact only) / B (rebuttal)
[Decision criterion] significance / correctness / improvement-over-prior / clarity
[Proof-check risk] any headline theorem whose full proof a referee cannot currently verify?
[Leverage plan] the next-stage action that can actually change the outcome
[Forbidden moves] shipping an unproved claim / arguing taste in a rebuttal
```
