---
name: ecai-author-response
description: Use when writing the ECAI author response (rebuttal) — the single, short, double-blind reply during the response window (IJCAI-ECAI 2026: 7-10 April 2026) that must correct factual misreadings and supply asked-for evidence within a strict length limit, knowing there is no second round and the area chair decides.
---

# ECAI Author Response

ECAI gives you **one** response, and there is **no revision round after it**. This is not a journal
rebuttal that precedes a Major Revision; it is a single, short, double-blind reply that the area
chair reads before the accept/reject discussion. Write it as a **precision instrument**: fix what is
factually wrong, supply the one number a reviewer said was missing, and give the area chair a clean
reason to champion the paper.

For **IJCAI-ECAI 2026** the author-response window is **7-10 April 2026**, after the summary-reject
phase (4 Mar) and before final notification (29 Apr). Verify the exact window and any length limit
on the current call before writing.

## What the response can and cannot do

| The response CAN | The response CANNOT |
|---|---|
| Correct a factual misreading ("the reviewer read Table 2 as X; it reports Y") | Add a new experiment or theorem that changes the contribution |
| Supply a specific number/clarification a reviewer explicitly requested | Re-run the study or promise a revised version — there is no revision round |
| Point to the exact line/lemma/figure that answers an objection | Argue taste or "significance" against a reviewer's judgment |
| Clarify scope a reviewer misjudged | Reveal author identity to make a credibility argument |

## Structure (short and scannable)

Length is tight (verify the cap). Do not spend it on throat-clearing.

1. **One-line framing (optional, ≤1 sentence).** The single most important correction, up front.
2. **Per-reviewer, per-point answers.** Address the specific objections each reviewer raised, in
   their order. Lead each with the reviewer's concern in a few words, then the answer.
3. **Shared-concern block (if two reviewers raised the same point).** Answer once, reference it.

Keep every answer **evidenced and checkable**: a table cell, a lemma number, a definition, a line
in the supplement. An assertion the area chair cannot verify from the existing paper is worth
little in a single-round process.

## Double-blind discipline

The response is read under **double-blind** review. Do not:

- name your group, institution, or prior system;
- write "as we showed in our [X]" in a way that identifies you — cite neutrally;
- link a non-anonymized repository to prove a claim.

A de-anonymizing rebuttal can sink an otherwise-acceptable paper.

## Triage: which points to answer

You cannot fix everything in a few hundred words. Prioritize:

1. **Factual errors** that, uncorrected, justify rejection — highest value; these are winnable.
2. **Missing-number requests** you can answer from work already done (a metric already computed, a
   proof already in the supplement).
3. **Clarifications** of scope or claim the reviewer misread.
4. **Skip** or briefly acknowledge pure-taste objections and requests that would require new work —
   promising future work does not move a single-round decision.

## Worked micro-example (illustrative, fictional)

> **R2 says the completeness proof assumes a finite state space, making it inapplicable.**
> The completeness result (Thm. 1) does not assume finiteness; it requires only that the fallback
> heuristic is admissible and the branching factor is finite, both stated in §3.1. The proof step
> R2 cites (line 214) bounds regret, not the state count. We will make the assumption list explicit
> in the camera-ready.
>
> **R3 asks for the node-expansion numbers on the IPC-2018 domains specifically.**
> These are already in the supplement (Table S4); the median reduction there is reported per domain.
> We will surface a one-line summary in §4 of the camera-ready. *(Answers an explicit request from
> work already done; promises only a minor, camera-ready-legal edit.)*

## Common failure modes

- **Debating the area chair's future decision** instead of arming an advocate with facts.
- **Promising a revised paper** — ECAI has no round in which to deliver it.
- **Spreading the length limit thin** across every minor comment instead of concentrating on the
  reject-driving points.
- **Introducing new claims** the reviewers could not check — often read as moving the goalposts.
- **Leaking identity** to bolster credibility.

## Output format

```text
[Response budget] length cap: <chars/words>; window: <dates>
[Reject-driving points] <list, each mapped to a checkable answer in the existing paper/supplement>
[Per-reviewer answers] R1: ... / R2: ... / R3: ...  (concern -> evidenced reply)
[Camera-ready-legal promises] only minor edits (assumption lists, surfacing an existing number)
[Anonymity check] no author/institution/system identity revealed
```
