---
name: icalp-author-response
description: Use when writing an ICALP (EATCS) Track B rebuttal in response to initial reviews, or when handling a Track A correctness query — correcting reviewer misreadings of a proof, pointing to the exact lemma or step that answers an objection, conceding real gaps honestly, and staying within the lightweight double-blind rules and the short rebuttal window.
---

# ICALP Author Response

Two very different situations live here, because the tracks differ:

- **Track B** gives you a **rebuttal window** (ICALP 2026: 21-24 March) to respond to initial reviews.
- **Track A** has **no general rebuttal**; authors are contacted **only** if the PC needs to resolve a
  **correctness issue**. If that happens, answer narrowly and precisely.

There is **no revision round** at ICALP (unlike a journal), so the response is your one and only chance
to speak — and it can only move a paper by fixing **misreadings and correctness doubts**, never by
arguing taste.

## Track B rebuttal: what it can and cannot do

A rebuttal moves a borderline paper when it:

- **Corrects a factual misreading** of a definition, hypothesis, or proof step.
- **Points to the exact place** an objection is already answered ("Lemma 4 assumes X, which the
  reviewer's counterexample violates; see line ...").
- **Supplies a missing clarification** a reviewer explicitly asked for (a constant, a boundary case, a
  comparison to a bound they named).

It does **not** move a paper when it:

- Argues the result is more important than the reviewer thinks (taste).
- Promises to add a proof "in the final version" that is not already written.
- Re-derives the whole paper instead of answering the specific point.

## Triage the reviews first

```text
[Correctness doubt] a reviewer questions a specific step -> HIGHEST priority: resolve it exactly
[Misreading]        a reviewer misstates what you proved -> correct crisply, cite the line
[Missing comparison] "how does this compare to [bound]?" -> give the one-sentence comparison
[Significance/taste] "not surprising / incremental"     -> brief, factual context; do not litigate
[Genuine gap]        a real hole they found             -> concede honestly; state what survives
```

Spend your limited words on **correctness and misreadings**, which you can actually change, not on
significance debates, which you usually cannot.

## Answering a correctness doubt (the make-or-break case)

Because there is no revision round, a **real proof gap** is usually fatal — but a **misperceived** gap
is very much winnable:

- If the reviewer **misread**: quote the exact hypothesis/lemma/line that closes their concern, in two
  or three sentences. Precision beats volume.
- If the gap is **real but reparable and the repair is already in the full version**: point to it
  precisely; do not claim a fix you have not written.
- If the gap is **real and open**: say so. State exactly which results still hold and which are
  weakened. Honesty preserves your credibility and the salvageable parts.

## Track A correctness contact

If Track A reaches out about correctness, treat it like a focused Track B correctness answer: address
**only** the step in question, point to the proof, and provide the missing detail. Do not use it to
argue significance or add new claims.

## Form and constraints

- **Stay anonymous.** The rebuttal is part of lightweight double-blind review — no author names,
  institutions, or de-anonymizing "as we did in [our other paper]".
- **Be concise and mapped.** Answer per reviewer and per point; a reviewer should find their concern
  addressed without hunting.
- **Lead with the highest-stakes correctness point**, then misreadings, then clarifications.
- **No new theorems.** You may clarify or point to existing proofs; you may not introduce results the
  referees have not seen.

## Response skeleton (Track B)

```text
Summary (2-3 sentences): what we clarify, and the one correctness point we resolve.

Reviewer 1
  - [Correctness] Concern about Step 3: <exact hypothesis/lemma/line that answers it>.
  - [Misreading] R1 states we assume <X>; we assume <Y> (Def 2). Consequence: <...>.
Reviewer 2
  - [Comparison] vs the bound of [ref]: <one-sentence comparison>.
  - [Clarification] <the requested constant / boundary case>.
Reviewer 3
  - [Conceded] The gap in Lemma 6 is real; Theorems 1-2 are unaffected; Cor 3 weakens to <...>.
```

## Output format

```text
[Track] B (rebuttal window) / A (correctness contact only)
[Triage] correctness doubts / misreadings / comparisons / taste / real gaps — counts
[Priority answers] the correctness/misreading points that can actually change the decision
[Concessions] real gaps, stated honestly, with what survives
[Anonymity] response free of identifying info? yes/no
[Forbidden] new theorems / taste arguments / promised-but-unwritten proofs — present? remove
```
