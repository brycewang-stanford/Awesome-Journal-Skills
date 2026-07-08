---
name: popl-author-response
description: Use when drafting a POPL author response during the optional multi-day window — triaging soundness objections against misread definitions, answering "what does Theorem 3 actually assume" questions with pointers rather than new material, staying concise per the CFP, and protecting the path to conditional acceptance.
---

# POPL Author Response

The POPL 2027 call describes the response phase plainly: authors get a multi-day
period, responding is optional, and a response "must be concise, addressing specific
points raised in the reviews" (read 2026-07-08; exact window dates were not rendered
— 待核实 in `resources/official-source-map.md`). At POPL the response is usually the
last input before the committee decides between reject and *conditional* acceptance,
so its job is to remove doubts, not to renegotiate the paper.

## What POPL reviewers actually dispute

Theory reviews rarely say "weak baselines." They say a definition does not mean what
you think, a side condition is missing, a theorem is unsurprising given prior work,
or the metatheory-to-motivation gap is too wide. Sort every review point into one of
four bins before writing a word:

| Bin | Example objection | Response move |
|---|---|---|
| Soundness doubt | "Lemma 4.2 seems to fail for open terms" | Quote the exact hypothesis that excludes the case; cite the proof line or mechanization file |
| Misread formalism | "Your typing rule allows unrestricted duplication" | Point to the definition as written; concede unclear notation and promise a one-line clarification |
| Significance | "This follows from [X] by standard techniques" | Name the specific step that fails under [X]'s assumptions — technical daylight, not adjectives |
| Presentation | "Section 5 is unreadable" | Accept, state the concrete restructuring you will do in the conditional-acceptance revision |

Soundness doubts come first and get the most space. One unresolved "the proof may be
broken" outweighs every fixed typo.

## Rules of engagement

- Answer the question asked, at the location asked. "See Section 3" without a page,
  definition number, or lemma name reads as evasion.
- No new theorems, no new mechanization claims. If a reviewer's counterexample
  exposes a real gap, say what the repaired statement is and where the fix lands —
  the conditional-acceptance revision exists exactly for that.
- Never hint at who you are; full double-blind holds through this phase, and
  identities unblind only after conditional-acceptance decisions.
- Concede fast and precisely. "R2 is right that Definition 6 omits the well-formedness
  premise; the proofs already assume it (see App. C.1), and we will state it" is a
  strong sentence, not a weak one.

## A skeleton that fits a concise budget

```text
Thank you — responses keyed to review points.

[R1, soundness of Thm 3] The counterexample uses an open term; Thm 3's hypothesis
"Γ ⊢ e : τ with Γ closed" excludes it (Def. 5, p.9). The mechanization checks the
closed case only, as stated in §7. No change needed; we will flag the hypothesis
in the theorem statement.

[R2 + R3, relation to <prior system>] <Prior> requires structural weakening
(their Lemma 2); our substructural setting has no weakening, which is where their
proof method stops. §2 example 2 will make this explicit.

[R3, presentation of §5] Agreed. We will move the auxiliary judgments to the
appendix and open §5 with the main invariant.
```

## Output format

```text
[Response status] drafted / needs-facts / not worth responding
[Bin counts] soundness:<n> misread:<n> significance:<n> presentation:<n>
[Highest-risk point] <the objection that decides the paper, and the one-line rebuttal>
[Concessions] <what is admitted and where the revision fixes it>
[Length check] <concise per CFP? what to cut>
```
