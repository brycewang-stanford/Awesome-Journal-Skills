---
name: ectheory-rebuttal
description: Use when an Econometric Theory (ET) decision letter arrives and a response strategy and letter are needed — handling proof-checking referee objections, fixing assumptions and gaps, and using the online Supplement, then writing a point-by-point response. It structures the revision, not the proofs themselves.
---

# Rebuttal & Revision (ectheory-rebuttal)

## When to trigger

- An ET decision letter arrived: revise-and-resubmit, or major/conditional revision
- You have referee reports challenging assumptions, proof steps, or generality
- You are unsure how to prioritize conflicting referee demands
- The revised manuscript exists and you need to draft the response letter

## ET reality: theory referees challenge the proof

At a theorem-proof journal the referees are checking your **mathematics**, not your causal story.
The handling editor's letter sets priorities; under the editorial leadership from 1 January 2026
(Guggenberger, Su, Sun), expect demanding technical review. Because review is **single-anonymous**,
the referees already know who you are — keep responses on the merits.

## Triage protocol

1. **Decode the editor.** The editor's letter ranks the issues. A point the editor underscores is
   binding; address it fully this round.
2. **Classify every comment.** Tag each: *fundamental* (a gap, an unjustified assumption, an
   incorrect limit claim — requires new math), *clarification* (rewrite/explain the assumption or
   step), or *disagreement* (you will push back, with a precise counter-argument or counterexample).
3. **Sequence the work.** Fix the math first (route fundamentals to
   `ectheory-identification-strategy` for assumptions/proofs, `ectheory-data-analysis` for
   simulations), update exhibits, *then* write the letter.
4. **Use the Supplement.** If closing a gap adds long derivations, move them to the online
   Supplementary Material (already-reviewed, separate labeled file) so the Article stays under 50
   pages — but the new derivations must now have been reviewed before final posting.

## Response-letter structure

- **Opening:** thank the editor and referees; summarize the main changes in a short paragraph.
- **Point-by-point:** quote each comment, then respond. Each response = what you changed
  (weakened assumption, filled step, added lemma, new simulation) + the exact location (theorem/
  lemma/section/page) in the revised paper.
- **Disagreements:** state the referee's point fairly, then give a precise mathematical reason you
  differ — ideally a counterexample, a citation, or a corrected derivation — not rhetoric.
- **Tone:** gracious, concrete, mathematically specific.

## Checklist

- [ ] Editor's binding points decoded and answered fully
- [ ] Every comment classified (fundamental / clarification / disagreement)
- [ ] All fundamental objections resolved with actual math (closed gaps, fixed assumptions), not promises
- [ ] Each response cites the exact theorem/lemma/section/page of the change
- [ ] Disagreements settled with a counterexample/derivation/citation, not assertion
- [ ] New long derivations placed in the Supplement; Article still <=50 pages
- [ ] Tone gracious and precise; no new overclaim introduced

## Anti-patterns

- Writing the response letter before the manuscript's proofs actually reflect the fixes
- Promising to "address in future work" a gap the referee identified
- Hand-waving a disputed step instead of giving a counterexample or corrected proof
- Defensive tone treating a proof-check as an attack
- Letting a fix push the Article past 50 pages instead of using the Supplement

## Mapping referee objections to the venue-specific fix

At a theorem-proof journal the report is a proof check, so each objection maps to a concrete mathematical
remedy, not a rhetorical reply.

| Referee objection | Class | The ET fix this round |
| --- | --- | --- |
| "Conditions too strong / not primitive" | fundamental | primitive moment+dependence pair; show high-level version follows |
| "Rate stated, no distribution theory" | fundamental | add the limiting law (mode, normalizer, functional) with the argument |
| "Hard step (uniformity) sketched" | fundamental | isolate as a named lemma with full proof; overflow to Supplement |
| "Result is a special case of [X]" | disagreement | counter with the dimension you relax, or concede and reframe |

Promising to "address in future work" a gap the referee identified is the classic way to turn a
revise-and-resubmit into a reject — close it with real math this round.

## Worked vignette and the disagreement protocol

A referee objects that the proof assumes finite eighth moments where finite fourth should suffice. The fix:
re-derive the variance bound via a maximal inequality needing only fourth moments, add the weakened
condition as the new Assumption, and verify it in the DGP. The entry reads: *"We have weakened
Assumption 2 to finite fourth moments (p. 7), re-proving the key bound via a maximal inequality (new Lemma
3, Supplement S.2)."* What changed, the new lemma, the exact location — that is what the editor scans for.
Settle disagreements with a counterexample, a corrected derivation, or a citation, never assertion; keep
every response anchored to a theorem, lemma, section, or page.

## Output format

```
【Decision】R&R / major / conditional
【Editor's binding points】[...]
【Classification】fundamental: [...] / clarification: [...] / disagreement: [...]
【Math routed to】ectheory-identification-strategy / ectheory-data-analysis (as needed)
【Letter】point-by-point with exact locations? [Y/N]
【Supplement used】overflow derivations moved, Article <=50pp? [Y/N]
【Next step】resubmit the single PDF via ScholarOne (ectheory-submission for file checks)
```
