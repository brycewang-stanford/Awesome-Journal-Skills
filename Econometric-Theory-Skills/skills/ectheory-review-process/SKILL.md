---
name: ectheory-review-process
description: Use to understand and prepare for the Econometric Theory (ET) review process — single-anonymous refereeing (reviewers see the author), the Article/Miscellanea/ET-Interview article types, and war-gaming the proof-checking referee before submitting.
---

# Review Process (ectheory-review-process)

## When to trigger

- You want to anticipate how ET referees will read a theorem-proof paper before you submit
- Unsure what single-anonymous review means for anonymization and self-citation
- Choosing among ET article types (Article, Miscellanea, and the invited ET Interview)
- War-gaming the objections a careful theory referee will raise

## ET's review model: single-anonymous

ET uses **single-anonymous peer review**: "the author does not know the identity of the reviewers,
but the reviewers know the identity of the author." Practical implications:

- **Do not anonymize the manuscript** the way a double-blind journal requires — your identity is
  visible to referees. Self-citation can be in natural voice, but argue the contribution on merit.
- Editorial leadership transitioned on **1 January 2026** to three joint Editors-in-Chief
  (Guggenberger, Su, Sun), succeeding founding editor Phillips; the program now includes invited
  papers with discussions and themed special issues.

## Article types

- **Articles** — Regular, plus Invited, Themed, and ET-lecture papers; full-length theorem-proof
  contributions (must not exceed 50 pages; overflow → online Supplement).
- **Miscellanea** — short papers presenting one or two key innovations, stated and proved concisely
  (typically <20 pages, often ~15).
- **ET Interviews** — a signature, invited oral-history genre (since the 1985 first issue, which
  opened with Phillips interviewing Denis Sargan). **Invited only — not author-submitted.**

## What an ET referee checks (war-game these)

1. **Every assumption** — is it necessary, minimal, and satisfied by a leading example? Is any
   assumption secretly assuming the conclusion?
2. **Every proof step** — is the hard step (uniformity, the non-standard limit, the edge case)
   actually established, or sketched past?
3. **The limit claims** — correct mode of convergence, rate, and limiting law?
4. **Generality and novelty** — is this more than a special case of known theory? (See
   ectheory-literature-positioning.)
5. **Simulations** — do they probe where the asymptotics are delicate, not just the easy region?

Pre-empt these: tighten assumptions, fill proof gaps, and add the boundary-case simulation *before*
a referee forces it — at a theory journal a single unproven step can sink the paper.

## Checklist

- [ ] Confirmed single-anonymous: manuscript NOT over-anonymized; identity visible is expected
- [ ] Article type chosen (Article vs Miscellanea); invited ET Interview not targeted
- [ ] Each assumption stress-tested for necessity and a leading example
- [ ] Hard proof steps verified, not sketched
- [ ] Limit mode/rate/law double-checked
- [ ] Boundary-case simulations added pre-emptively
- [ ] Novelty over special cases made explicit

## Anti-patterns

- Double-blind-style anonymization for a single-anonymous journal
- Submitting with a known proof gap, hoping referees miss it
- A paper that is a corollary of existing theory framed as a major Article
- Simulations that avoid the regime where the approximation is weakest
- Targeting the invited ET Interview as a submission

## Desk-reject and red-flag screen for theory papers

Before a referee sees it, the handling editor screens the manuscript for whether a *general, proved,
foundational* result is present, in ET's rigorous limit-theory tradition.

| Screen item | Survives | Likely quick reject |
| --- | --- | --- |
| Nature of the result | A theorem with explicit limiting law | An applied estimate with a theory veneer |
| Generality | Moves the result along a known dimension | A relabelled corollary of standard theory |
| Proof completeness | Hard step proved or routed to Supplement | A visible gap at the delicate step |
| Genre | Submitted Article/Miscellanea | Targeting the invited ET Interview |

## War-gaming the proof-checking referee

For a new limit theory for a nonstationary estimator, read adversarially as the referee will: they (1)
check whether the dependence condition is primitive or hides the conclusion; (2) ask whether the o_p(1)
bound at the uniformity step is uniform in the local-to-unity parameter or only pointwise; (3) verify the
normalizing rate matches the claimed limit; (4) ask whether the Monte Carlo visits the near-unit-root
neighborhood; (5) ask "is this the i.i.d. special case of an existing FCLT?" Pre-empt all five — add the
uniformity lemma, the boundary-spanning simulation, and a remark naming the prior result you generalize. The fixes: a proof gap → isolate it as a lemma and prove it; a known special case → state the
generality dimension up front (route `ectheory-literature-positioning`); an over-anonymized manuscript →
restore identity, as ET review is single-anonymous.

Calibration anchor: editorial leadership moved on 1 January 2026 to three joint Editors-in-Chief
(Guggenberger, Su, Sun) succeeding founding editor Phillips; expect demanding technical review, and treat
any specific turnaround or acceptance figures as unverified unless confirmed on the journal's current pages.

## Output format

```
【Review model】single-anonymous (reviewers see author)
【Article type】Article / Miscellanea
【Assumptions stress-tested】[Y/N]
【Proof gaps closed】[Y/N]
【Boundary simulations】added? [Y/N]
【Novelty over special cases】stated? [Y/N]
【Next step】ectheory-submission
```
