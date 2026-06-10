---
name: jacs-results-framing
description: Use when the chemical advance and its significance are not yet sharp for a Journal of the American Chemical Society (JACS) manuscript. Shapes the narrative and claims — it does not generate new data or fix characterization gaps.
---

# Framing the Chemical Advance (jacs-results-framing)

## When to trigger

- You have results but the abstract/intro does not land a clear "advance"
- Reviewers (or co-authors) ask "what is genuinely new here?"
- The story reads as a list of experiments rather than one argument
- The significance is asserted ("important", "novel") rather than demonstrated

## The advance, stated as a claim chain

A JACS narrative is a chain where each link is backed by data:

1. **Problem** — the chemical question or limitation, framed for broad interest.
2. **Advance** — the new reaction / structure / material / method / mechanism that addresses it.
3. **Evidence** — the specific data that prove the advance (yields/ee, spectra, X-ray, kinetics).
4. **Generality / mechanism** — why it is not a one-off (scope table; mechanistic basis).
5. **Significance** — what becomes possible now that did not before, across chemistry.

If any link rests on assertion rather than data, route to `jacs-methods`.

## Framing the "broad interest"

Pick the dominant breadth driver and make the intro about it:

| Breadth driver | How to frame it |
|----------------|-----------------|
| Generality | Emphasize substrate/functional-group scope, robustness, predictability |
| Concept | Emphasize the new principle (mode of reactivity, bonding, structure–property law) |
| Enabling utility | Emphasize what synthesis/measurement is newly possible; show a hard target |
| Selectivity | Quantify the selectivity gain (ee, dr, regio-, chemo-) vs prior art |

## Title and abstract discipline

- Title states the chemistry, not the activity ("Catalytic Asymmetric X via Y",
  not "Studies toward X"). Avoid vague boosters.
- Abstract = problem → advance → key quantitative evidence → significance, in a
  few sentences. Put at least one hard number (yield, ee, TON, rate, λ, R-factor).
- The TOC/abstract graphic must visually encode the central advance, not decorate.

## Calibrating novelty claims

- Compare against the closest prior art explicitly; state the delta in one line.
- Use "first" only if you have searched and can defend it; prefer "we show that".
- Match the strength of the claim to the strength of the data (controls, scope, mechanism).

## Checklist

- [ ] One sentence names the advance and its breadth driver
- [ ] Each link in the claim chain points to specific evidence
- [ ] The closest prior art is cited and the delta stated
- [ ] Abstract contains at least one hard quantitative result
- [ ] TOC graphic encodes the central advance
- [ ] No significance claim exceeds what the data show

## Anti-patterns

- "Novel" as a substitute for stating what is new
- Burying the advance under methodological detail in the intro
- Over-claiming generality from a narrow, hand-picked substrate set
- Significance framed as field hype rather than concrete new capability


## Operating pass for Journal of the American Chemical Society

Treat this skill as an executable review pass, not a prose hint. First lock the chemical novelty, characterization chain, controls, and scope or mechanism evidence; then judge whether the current manuscript answers the venue's real reader: chemistry reviewers who expect a molecule/material/reaction claim to be supported by rigorous characterization and mechanistic insight.

- **Do the pass:** Return a claim-evidence-risk ledger rather than a prose-only diagnosis; every recommendation must point to a manuscript location or missing artifact.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against ACS Central Science for broad conceptual reach, Angewandte for communication style, specialized ACS journals for narrower chemistry; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Advance】one-sentence claim
【Breadth driver】generality / concept / utility / selectivity
【Evidence map】advance → [data that proves it]
【Prior-art delta】vs <ref>: <one line>
【Gaps to close】route to jacs-methods if any link is unsupported
【Next】jacs-methods → jacs-figures
```

## Related resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — what evidence each technique provides
