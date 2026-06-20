---
name: aejmic-referee-strategy
description: Use when anticipating referee objections or calibrating review expectations for an American Economic Journal: Microeconomics (AEJ: Micro) manuscript before submission. Pre-empts the objections theory referees raise and reads the editorial process; it does not draft the response letter (see aejmic-rebuttal).
---

# Referee Strategy (aejmic-referee-strategy)

## When to trigger

- Before submission, to stress-test the paper against the objections experts will raise
- Deciding whether the contribution clears the desk-reject bar
- Choosing JEL codes / framing that route the paper to the right co-editor
- Unsure what the AEJ: Micro review process looks like

## The AEJ: Micro process (检索于 2026-06；以官网为准)

- AEJ: Micro uses **single-blind** review via the AEA submission system: the referee sees the author, but referees are anonymous to authors. There is no anonymization burden — reputation is visible, so the paper must stand on rigor.
- There is a **submission fee** (AEA member $200 high-income / $100 middle / $0 low; nonmember higher — 检索于 2026-06，volatile), and JEL classification per AEA practice helps route the paper to the right co-editor and expert referees.
- Decisions run the usual ladder: desk reject → reject after review → R&R (minor/major) → accept. Theory referees verify proofs; a flawed or non-tight proof is a common reject reason.
- Re-confirm fee, timelines, and co-editor list on the official AEA AEJ: Micro page (see `resources/official-source-map.md`).

## Objections AEJ: Micro referees actually raise — and the pre-emption

| Likely objection | Pre-empt it by (skill) |
|---|---|
| "The result is a knife-edge artifact of assumption A." | Name the load-bearing assumption; show necessity / a counterexample on failure (`aejmic-identification`) |
| "This is too specialized / maximal-generality for AEJ: Micro." | Re-frame the broad-interest message; cut generality that hides it (`aejmic-topic-selection`, `aejmic-theory-model`) |
| "How does this differ from [closest result]?" | State the theorem-relative delta in one sentence (`aejmic-literature-positioning`) |
| "Does it survive [a continuum / asymmetry / perturbation]?" | Provide the earned extension or a clean negative result (`aejmic-robustness`) |
| "A step in the proof is asserted, not shown." | Complete the lemma scaffolding; self-contained proofs (`aejmic-replication-package`) |
| "The model is overloaded; the mechanism is invisible." | Reduce to the minimal environment; lead with intuition (`aejmic-theory-model`, `aejmic-writing-style`) |
| "This is an empirical paper, not theory." | Either restore the theoretical contribution or redirect to AEJ: Applied (`aejmic-topic-selection`) |
| (Applied) "Identification / inference is shaky; asterisks used." | Branch B/C identification; SEs not asterisks (`aejmic-identification`, `aejmic-tables-figures`) |

## Checklist

- [ ] Listed the three most likely referee objections for *this* paper and mapped each to a fix
- [ ] The load-bearing assumption is named and defended before submission
- [ ] The theorem-relative delta is crisp (one sentence)
- [ ] The broad-interest message is explicit (not specialist-only)
- [ ] Every proof step a referee will check is complete
- [ ] JEL codes chosen to route to the right co-editor (single-blind: no anonymization needed)
- [ ] Decided the venue is right (not actually an AEJ: Applied paper)

## Anti-patterns

- Submitting without anticipating the single most obvious expert objection
- Relying on generality to impress when the audience-fit objection is the real risk
- Leaving a checkable proof gap for a referee to find
- Mis-routing via vague JEL codes so a non-expert co-editor handles it
- Assuming anonymity protects a thin result — single-blind means the referee knows whose work it is

## Worked vignette (illustrative)

Before submitting a matching paper, the author lists likely objections: (1) "rides on substitutability" → already pre-empted in `aejmic-identification` with a counterexample; (2) "how does it differ from the deferred-acceptance literature?" → one-sentence delta ready; (3) "is the existence proof complete?" → lemma scaffolding done. The remaining risk is audience fit, so the intro is rewritten to foreground the broad market-design message rather than the technical condition. JEL codes C78/D47 route it to a market-design co-editor.

## Output format

```
【Top 3 likely objections】[...]  →  【Fix / owning skill】[...]
【Load-bearing assumption defended】[Y/N]
【Delta crisp】[Y/N]   【Broad-interest message explicit】[Y/N]
【Proof gaps closed】[Y/N]
【Routing】JEL codes [...] (single-blind — no anonymization)
【Venue confirmed】AEJ: Micro (not AEJ: Applied)? [Y/N]
【Next step】aejmic-submission
```

## Supplementary resources

- [`../../resources/README.md`](../../resources/README.md) — links to the shared reviewer-objection checklist (applied subset)
