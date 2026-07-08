---
name: asplos-author-response
description: Use when drafting an ASPLOS author response inside the short fixed window — triaging reviews into factual errors versus questions versus disagreements, budgeting for the ~800 words reviewers are expected to read, arguing only from evidence already in the submission, and positioning the paper for the Accept / Major Revision / Reject decision.
---

# ASPLOS Author Response

The 2027 CFP defines the rebuttal's job narrowly: **(1) correct factual errors in
the reviews, and (2) answer the questions reviewers posed.** There is no hard length
cap, but reviewers are **not expected to read past 800 words** (verified
2026-07-08). Both facts should shape every drafting decision below. The 2027
windows are fixed and short — July 6-9, 2026 for the April cycle (open on this
pack's check date) and December 1-4, 2026 for the September cycle.

## Hour one: triage before prose

Sort every review remark into exactly one bucket:

| Bucket | Definition | Response posture |
|---|---|---|
| **Factual error** | The review misstates what the paper says, measures, or assumes | Correct it, with a section/figure/table pointer — highest priority, CFP-sanctioned |
| **Direct question** | The reviewer asked for a clarification | Answer in ≤ 3 sentences, citing where the paper already contains the material |
| **Evidence dispute** | The reviewer doubts a result or baseline | Point to the existing run/ablation that addresses it; concede if none exists |
| **Judgment call** | "Not novel enough", "fit is marginal" | One calm paragraph max, or zero — rebuttals rarely move taste |
| **Revision seed** | A fixable gap you agree with | Acknowledge + state the concrete fix; this is you negotiating the Major Revision terms |

The last bucket is ASPLOS-specific leverage: because the decision set includes
**Major Revision**, a response that shows requested work is *scoped and feasible in
six weeks* gives the committee a reason to choose revision over rejection.

## The 800-word budget

Assume only the first 800 words are read; structure so truncation is harmless:

```text
Words   1- 80   Global note: 1-2 sentences of thanks + the single most
                important correction, stated flatly with a pointer.
Words  80-560   Numbered items, worst objection first. Format per item:
                [R2-Q1] Claim/question -> answer -> evidence pointer (§, Fig, Tab).
Words 560-800   Revision seeds: "If given the opportunity, we will X, Y, Z" —
                each one concrete, bounded, and honest about what exists today.
Overflow        Optional detail annex, clearly marked; assume unread.
```

Write pointers, not paraphrases: "§6.4's ablation isolates the hint register (row 3
of Table 5)" outlasts three sentences of re-argument.

## Rules of evidence

- Argue **only from the submitted PDF and its appendices**. New numbers produced
  during a four-day window read as unreviewable and can poison trust in the
  reviewed ones.
- If a reviewer misread because the paper was unclear, say both halves: the correct
  reading, and that the text will be clarified — the misreading is data about your
  writing.
- Never restate a weakness in stronger words than the reviewer used; answer the
  version they wrote.
- Preserve anonymity: no identifying links, no "as we showed in our earlier paper"
  in the first person.

## Anticipating each decision from the response

- **Toward Accept:** every factual error corrected with pointers; questions
  answered; no new promises needed.
- **Toward Major Revision:** disputes conceded where real, each paired with a
  bounded fix — you are drafting the revision contract's terms in your own
  language before the committee writes them in theirs.
- **Away from Reject:** the response's tone matters most on the margin; a defensive
  or evasive rebuttal confirms a skeptical reviewer's prior. Flat, specific,
  checkable sentences are the house style.

## Team protocol for a 3-4 day window

1. Day 0 (reviews arrive): full-team read; triage table filled; owner per item.
2. Day 1: draft answers with pointers verified against the submitted PDF — not the
   current working draft, which has diverged.
3. Day 2: cut to budget; adversarial read by the author who wrote least of it.
4. Final day: submit early; HotCRP forms have closing times, and AoE arithmetic
   under deadline stress is how windows get missed.

## Sentence patterns, graded

Systems reviewers reward flatness and pointers; they punish advocacy verbs.

- Works: *"R2 states the baseline ran untuned; §6.1 documents the three
  tunables we set and their values, matching the vendor guide."* — correction,
  pointer, checkable.
- Works: *"Yes — the design targets sub-VM granularity; §3.4's interface
  section defines the virtualization behavior R1 asks about."* — direct answer
  first, location second.
- Fails: *"We respectfully disagree with the reviewer's assessment of
  novelty."* — spends words restating the objection, adds no evidence.
- Fails: *"As is well known in the community..."* — condescension detector;
  if it were well known, the reviewer would know it.
- Fails: *"We will completely rewrite Section 5."* — unbounded promise; the
  Major Revision channel rewards bounded, verifiable commitments only.

## When reviews contradict each other

Reviewer A wants the simulator sweep expanded; reviewer B calls simulation the
paper's weakness. Do not privately pick a side: name the tension in one neutral
sentence and resolve it with the claim-instrument logic ("the sweep tests
generality; the silicon runs carry the headline claim — §6.2 vs §6.5"), so the
committee discussion inherits your framing instead of improvising one. A
response that surfaces and resolves a contradiction reads as authors who
understand their own evidence architecture.

## Arming your champion

A response is read most attentively by the reviewer already inclined to argue
for the paper. Give that reviewer portable ammunition: one-sentence answers
they can paste into the discussion, exact figure references, and a crisp
statement of what the paper does *not* claim (scope concessions defuse the
skeptic's strongest line). If no review shows champion potential, the realistic
response goal shifts to securing the Major Revision outcome rather than
outright acceptance — write the revision-seed section accordingly.

## Output format

```text
[Triage] errors: N · questions: N · disputes: N · judgment: N · revision seeds: N
[Budget] main-body words: N/800 · items ordered worst-first: Y/N
[Pointer audit] every answer carries §/Fig/Tab: Y/N
[New-data check] zero unreviewable numbers introduced: Y/N
[Revision terms offered] <the bounded fixes promised, one line each>
[Submission] uploaded with ≥12h margin: Y/N
```
