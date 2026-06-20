---
name: joe-review-process
description: Use to understand and navigate the Journal of Econometrics (JoE) editorial process — single-anonymized review, editor screening before a minimum of two referees, the three submission tracks (Regular/Annals/Themed), Guest Associate Editors, and what referees of a methods paper look for.
---

# Review Process (joe-review-process)

## When to trigger

- You want to know how JoE evaluates a methodological submission, end to end
- You are choosing among the Regular / Annals / Themed Issue tracks
- You are anticipating referee objections before submitting or after a revision request
- You are unsure who decides (editors, Co-Editors, Guest Associate Editors)

## How JoE review works

- **Single-anonymized review:** referees know the authors' identities; authors do **not** know the referees.
- **Editor screening first:** editors screen submissions; suitable papers are sent to a **minimum of two independent expert referees**, and the editors make the **final decision**. Unsuitable or out-of-scope papers are desk-screened out.
- **Co-Editors-in-Chief:** Michael Jansson (UC Berkeley) and Aureo de Paula (UCL), supported by a set of Co-Editors. Check the live board page for the complete current roster before naming a handling editor.

## The three submission tracks

- **Regular Issues** — standard standalone methodological papers; the default route.
- **Annals Issues** — focused volumes assembled around a coherent theme.
- **Themed Issues** — topic-based collections, often originating from conferences. Proposal **organizers may serve as Guest Associate Editors** who make recommendations to the Co-Editors; Themed Issues still go through the **regular editorial process**. If your work matches an active theme, this can be a strong, well-matched route (check the journal's Themes page for current calls).

Pick the track deliberately: a standalone advance → Regular; a contribution that fits an active call → Themed/Annals, where a Guest Associate Editor close to the topic may handle it.

## What methods referees look for

1. **Genuine methodological contribution** with mathematical rigor — proofs/asymptotics, not a relabeled method.
2. **Primitive, verifiable assumptions** and honest asymptotics (no smuggling the conclusion).
3. **Monte Carlo** that reports size and size-adjusted power and stresses the assumptions.
4. **Precise positioning** against the nearest estimator/test.
5. **Reproducibility** — runnable estimator and a `run_all` pipeline.
6. **Scope fit** — a methodological advance, not a purely applied result.

## Practical reading of the process

- A clean editor screen rewards a contribution stated plainly in the abstract/intro (see `joe-contribution-framing`, `joe-writing-style`).
- Because referees are specialists, the closest-competitor comparison and the boundary-case Monte Carlo are where reports are won or lost.
- Expect detailed, technical referee reports; a revision request usually means "make the theory/Monte Carlo airtight," handled in `joe-rebuttal`.

## Editor-screen packet

Before submission, assemble a four-item packet for the first editorial read:

| Packet item | What it must show | Where it appears |
| --- | --- | --- |
| One-sentence method advance | The estimator/test/theorem is not a relabeling of an existing method | Abstract and first introduction paragraph |
| Closest-competitor contrast | Exactly which estimator, test, or asymptotic result is improved | Introduction table or paragraph |
| Formal-core promise | Identification, assumptions, rate, and inference are all proved or clearly delegated to appendices | Theory section map |
| Finite-sample credibility | Monte Carlo stresses the boundary cases where the method should matter | Simulation design summary |

If the packet cannot be filled without hedging, the paper is not ready for JoE screening. Fix the formal core before investing in formatting.

## Anti-patterns

- Treating JoE like a double-anonymized journal and over-anonymizing (it is single-anonymized)
- Submitting to a Themed Issue whose scope your paper does not actually match
- Ignoring that editors screen first — a buried contribution dies at the screen
- Assuming a purely applied paper will survive referees here
- Letting a simulation-heavy paper hide the absence of a formal methodological advance

## Output format

```
【Review model】single-anonymized; editor screen → ≥2 referees
【Track】Regular / Annals / Themed (+ Guest AE if themed)
【Handling editor】Co-Editor / Guest AE; final call by editors
【Referee hot spots】assumptions / asymptotics / size-power / positioning / reproducibility
【Editor-screen packet】advance / competitor / formal core / finite-sample credibility
【Scope check】methodological advance present? [Y/N]
【Next step】joe-submission
```
