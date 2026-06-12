---
name: ajps-literature-positioning
description: Use when positioning an American Journal of Political Science (AJPS) manuscript against the literature. AJPS is double-blind, so positioning must engage the relevant debates while keeping the manuscript fully anonymized (third-person self-citation, no first-person "we showed"). Stakes the contribution; it does not write the lit review.
---

# Literature Positioning (ajps-literature-positioning)

At AJPS the introduction must do two things at once: place the paper inside a **live empirical or
theoretical debate** that a broad political-science readership recognizes, **and** stay consistent with
**double-blind** review. The second constraint is easy to break — a single "as we demonstrated in our
2021 paper" can identify the authors. Positioning is where the contribution is staked and where
anonymity is most often lost.

## When to trigger

- Drafting or revising the introduction and the "contribution" paragraph
- A reviewer said you "missed obvious work" or "don't engage the debate"
- Distinguishing your contribution from the closest prior papers
- Checking that self-citations are anonymized for double-blind review

## How AJPS wants the literature engaged

1. **Engage a debate, not a citation pile.** Name the live disagreement, the contested estimate, or
   the open mechanism your paper speaks to, and cite the works that *define* it.
2. **Locate the marginal contribution precisely.** "Prior work estimates effect E assuming A; we relax
   A / identify E cleanly / show E is conditional on C." A generalist reader should see the increment.
3. **Pre-empt the obvious rival.** AJPS reviewers are expert and quantitatively literate; name the
   strongest alternative explanation and signal how the design adjudicates it (hand off to
   `ajps-research-design`).
4. **Speak to a broad readership.** AJPS spans subfields; show why a reader outside your niche should
   care, without diluting the specialist contribution.

## Keep positioning double-blind (an AJPS-specific demand)

- **Third-person self-citation.** Cite your own prior work as you would anyone else's — never "in our
  earlier work" or "we previously showed."
- **No identifying tells.** Remove acknowledgments, grant numbers, named datasets you uniquely hold,
  conference-presentation mentions, and "available on my website" links.
- **Watch the bibliography.** A wall of single-author self-cites can de-anonymize even in third person;
  cite only what the argument needs (see `ajps-submission`).

## Anti-patterns

- A "literature dump" with no organizing debate
- First-person self-reference that breaks anonymity ("as we showed in...")
- Strawmanning prior work or hiding the closest competitor paper
- Claiming "first to study" when the contribution is incremental
- Padding citations to signal effort rather than to position the contribution


## Worked micro-example (illustrative)

A paper on close-election incumbency advantage positions against a live debate: prior estimates credit
officeholder resources, while a rival camp argues candidate-quality persistence. The marginal-contribution
sentence: *"Existing RD work estimates a pooled advantage assuming no sorting; we relax that, add a
manipulation test, and show the effect survives — isolating the officeholding channel."* The strongest
rival is named, with a pointer to the adjudicating design. Self-cites stay third-person, preserving
anonymity.

## Referee-pushback patterns and the venue-specific fix

- *"You missed obvious work / don't engage the debate."* -> Replace the citation pile with the 3-6 works
  that *define* the live disagreement and locate your increment against them.
- *"First-person self-cite breaks blinding."* -> Rewrite "as we showed" as a third-person citation; a
  single tell can de-anonymize at AJPS.
- *"This is incremental, not 'first to study.'"* -> Drop the novelty claim; state the delta.

Calibration anchor: AJPS rewards a contribution that travels across political settings and an introduction
engaging a debate a broad readership recognizes; confirm the current anonymizing rules against the
journal's guidelines.

## Positioning pass for American Journal of Political Science

Run this as a concrete capability pass. First lock the political theory, design leverage, measurement validity, and scope condition; then test whether the manuscript addresses political-science reviewers who expect tight theory, transparent design, and a contribution that travels across political settings.

- **Primary move:** Build a three-column map: incumbent conversation, unresolved tension, and this manuscript's delta; include one sibling-venue omission that would make a referee doubt the fit.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against APSR for field-wide breadth, Journal of Politics for broader political-science audience, Political Analysis for methods-first work; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Debate】the live disagreement / contested estimate
【Key works】the 3-6 that define it
【Gap】what is contested / mismeasured / unidentified
【Move】how this paper changes the debate
【Strongest rival】and how the design will adjudicate it
【Anonymity】self-cites in third person, no identifying tells? [Y/N]
【Next】ajps-theory-building
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — double-blind review and anonymizing requirements
