---
name: rt-desk-reject-risk
description: Use before submitting to score a manuscript against a specific venue's own desk-reject triggers and return a ranked, fixable risk report. Venue-conditional — it reads the target's documented triggers rather than applying generic advice. Run it after rt-submission-readiness clears the mechanical bar and before the paper is uploaded.
---

# Desk-Reject Risk (rt-desk-reject-risk)

Desk rejection is the modal outcome at a strong venue, it arrives before any referee
reads the paper, and it costs weeks for reasons that are almost always documented in
advance. This repository already carries those reasons — **456 of 743 indexed venues
(61%) publish an explicit desk-reject section in their pack** — but nothing turned
them into a check a paper could be scored against.

`rt-submission-readiness` answers *"is the manuscript mechanically complete?"*. This
answers the different and harder question: **"given this specific venue's stated
triggers, what will get this desk-rejected, and what is the cheapest fix?"**

## When to trigger

- A target venue is chosen and the paper is near-final.
- An author asks "will this survive the editor?" or "why did the last one get desked?"
- Immediately after `rt-venue-reframe`, to score the reframed draft against its new home.
- Before a resubmission up the ladder, where the previous desk reject is evidence.

## Method

**Step 1 — locate the venue's triggers.** From
[`venue-index.tsv`](../../../shared-resources/journal-selection/venue-index.tsv), take
the row's `pack_dir` (depth) or `profile_path` (breadth) and read:

- the `## Common desk-reject triggers` section (or the pack's `Desk-reject and triage`
  / `decline-without-review` variant) in its `*-submission`, `*-review-process` and
  `*-topic-selection` skills;
- the scope and format constraints in `resources/official-source-map.md`, **read live** —
  length caps, abstract style, anonymity rules and fee/policy gates are volatile and
  are a large share of real desk rejects.

If the venue publishes no explicit trigger list (about 4 in 10), say so, and fall back
to the venue's fit and house-style skills plus the generic gate in Step 3 — do **not**
invent venue-specific triggers.

**Step 2 — score each trigger.** For every documented trigger, judge the manuscript
against it and assign:

| Level | Meaning |
|---|---|
| **Fatal** | The editor will desk-reject on this alone. Fix before upload or change venue. |
| **Likely** | A common desk cause at this venue; the paper is exposed but not certain to fail. |
| **Watch** | Survivable, but it is the first thing a referee will raise. |
| **Clear** | Documented trigger the paper demonstrably does not hit. |

Cite the *evidence in the manuscript* for each judgement (a section, a table, a claim),
not a general impression. A risk with no located evidence is a hypothesis — mark it as
one, or drop it.

**Step 3 — the universal gate** (applies at every venue, on top of the venue's own):

1. **Scope miss** — the contribution is not the kind of contribution this venue
   publishes. This is the single largest desk cause and the least fixable.
2. **Framing miss** — right result, wrong "why it matters" for this audience.
3. **Format/anonymity breach** — length, abstract, blinding, reference style, ORCID,
   supplementary rules. Mechanical and always worth fixing.
4. **Evidence baseline** — a robustness or design check the venue treats as table
   stakes and the paper omits.
5. **Policy** — data-and-code availability, ethics/IRB, preregistration, conflicts,
   prior dissemination or dual-submission rules.

**Step 4 — return a cost-ranked fix list.** Sort by (severity × 1/effort). Distinguish
fixes that are edits from fixes that need new analysis; say explicitly when the honest
conclusion is *"this venue is wrong for this paper"* and route to `rt-journal-match`.

## Hard rules

1. **Venue-conditional, never generic.** Every Fatal/Likely must trace to a trigger the
   venue's own pack or source map states. Generic advice belongs in Step 3 and must be
   labelled as such.
2. **Volatile constraints are read at scoring time** from
   `resources/official-source-map.md` — never quoted from memory.
3. **No fabricated triggers.** If the pack does not document a trigger list, say so.
4. **Do not present this as a prediction of the editor's decision.** It is a
   documented-risk audit; there is no acceptance-probability number to give, and
   inventing one would be false precision.
5. **Defer scope/fit judgement** to the venue's `*-topic-selection` skill.

## Output format

```
【Venue】<display name>  (pack: <pack_dir | profile_path>)
【Trigger source】<n> documented triggers read from <files>  |  none documented
【Source-map read】<date>
【Fatal】  trigger — evidence in the manuscript — fix (edit | new analysis)
【Likely】 …
【Watch】  …
【Clear】  triggers the paper demonstrably passes
【Cost-ranked fixes】1..n, each: severity · effort · what to change
【Verdict】submit as-is / fix first (n items) / wrong venue → rt-journal-match
```

## Anti-patterns

- Producing a percentage "acceptance chance". The inputs do not support it.
- Listing every trigger as Watch — a report with no ranking is not a report.
- Scoring against a venue's reputation instead of its documented triggers.
- Running this instead of `rt-submission-readiness`; they check different things and
  the mechanical bar comes first.
- Treating a Clear on all triggers as an acceptance signal. Surviving the desk means
  the paper reaches referees, nothing more.

Next: `rt-simulated-referee` once the desk gate is clear, then
`rt-replication-package` for the deposit.
