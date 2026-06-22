---
name: ylj-topic-selection
description: Use when deciding whether a legal-scholarship idea is a fit for The Yale Law Journal (YLJ) and which track it belongs in. It tests generalist significance, timeliness, and novelty potential; it does not draft the thesis or run the formal preemption search.
---

# Topic Selection & Fit (ylj-topic-selection)

YLJ is the **generalist flagship** of American legal scholarship — read across the whole discipline by
academics, judges, and practitioners. A topic earns a slot only if its claim matters **beyond a single
doctrinal niche**. This skill screens the idea before you invest in a full draft; it does not yet build
the claim (`ylj-thesis-and-contribution`) or prove novelty (`ylj-preemption-check`).

## When to trigger

- You have an idea and want to know if YLJ is the right home (vs. a specialty review)
- Several candidate angles exist and you must pick the one with the widest reach
- Deciding Article vs. Essay vs. Feature vs. (for Yale students) Note/Comment
- A timely development (new statute, circuit split, landmark opinion) might justify the Forum

## Fit test (a topic must clear all four)

1. **Generalist stakes.** A constitutional-law professor and a commercial-litigation partner can both
   say in one sentence why the claim matters. If only specialists in your subfield care, target a
   specialty review instead.
2. **A claim, not a survey.** YLJ wants an argument that changes how readers think about a doctrine,
   theory, or institution — not a doctrinal literature review or a casenote.
3. **Headroom for novelty.** A first scan (Westlaw secondary sources, SSRN, HeinOnline) suggests the
   space is not already occupied. Confirm later with `ylj-preemption-check`.
4. **Right scale for a track.** Big original theory → **Article**; sharp, contained intervention →
   **Essay**; timely reaction to a development or a response to a YLJ piece → **Forum**.

## Fit-gate ledger

Before sending the user onward, write a short keep / reframe / reject ledger. This prevents generic
"top law review" advice from passing as a YLJ fit decision.

| Gate | Pass evidence | If weak |
|------|---------------|---------|
| **Audience travel** | Name two legal audiences outside the subfield and the reason each should care | Reframe the stakes or route to a specialty review |
| **Claim pressure** | State the contestable move, not just the topic | Route to `ylj-thesis-and-contribution` before picking a venue |
| **Novelty headroom** | Identify the first SSRN / Westlaw / HeinOnline scan and the closest near-miss | Route to `ylj-preemption-check` before investing in the draft |
| **Track fit** | Match ambition, timeliness, and length to Article / Essay / Forum / Note / Comment | Split or compress the idea before submission planning |

Use **KEEP** only when all four gates have concrete evidence. Use **REFRAME** when the idea could become
YLJ-shaped after narrowing, broadening, or changing tracks. Use **REJECT** when the only plausible value
is specialist, descriptive, or already preempted.

## Generalist-significance ladder (push the topic up a rung)

| Rung | Example framing | Verdict |
|------|-----------------|---------|
| Doctrinal fix in one circuit | "The Ninth Circuit misreads § X" | Specialty review, not YLJ |
| Doctrine-wide problem | "Courts across circuits misframe X" | Borderline — needs a theory |
| Doctrine ↔ theory | "X reveals a flaw in how we think about Y" | YLJ Essay candidate |
| New framework for an institution | "A new account of how Y should work" | YLJ Article candidate |

## Track sizing

- **Article** — original, ambitious scholarship; encouraged **< 25,000 words incl. footnotes**
  (~50 Journal pages) (检索于 2026-06；以官网为准).
- **Essay** — a pointed contribution; encouraged **< 15,000 words incl. footnotes** (~30 pages).
- **Feature** — curated set / symposium; coordinate with editors via `ylj-placement-strategy`.
- **Note / Comment** — **Yale Law students only**; route to `ylj-student-editor-review` for the Notes
  Development process and the first-time word caps.
- **Forum** — short, timely online piece, encouraged **< 10,000 words incl. footnotes** (~20 pages).

## Checklist

- [ ] One-sentence statement of why a generalist reader cares
- [ ] The idea is a *claim* that changes a reader's mind, not a summary
- [ ] Quick scan suggests novelty headroom (formal check deferred to preemption)
- [ ] Timeliness assessed — is this an Article (durable) or a Forum (time-sensitive)?
- [ ] Track chosen and its encouraged length is realistic for the idea

## Anti-patterns

- Pitching a casenote, doctrinal survey, or student-seminar paper as a generalist Article
- Choosing a topic so timely it will be stale by the print cycle (that is a Forum piece)
- Picking a niche only specialists value, then hoping prestige carries it
- Ignoring that an over-length manuscript weighs **against** acceptance regardless of quality

## Output format

```
【Topic】one line
【Generalist stakes】who outside the subfield cares, and why
【Fit gate】KEEP / REFRAME / REJECT + weakest gate
【Track】Article / Essay / Feature / Note / Comment / Forum (length realistic? Y/N)
【Novelty headroom】initial read (formal check pending)
【Next】ylj-thesis-and-contribution to sharpen the claim
```

## Supplementary resources

- [`../../resources/exemplars/library.md`](../../resources/exemplars/library.md) — landmark YLJ pieces by type, for calibrating ambition
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official YLJ track/length facts
