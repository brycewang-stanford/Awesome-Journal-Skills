---
name: ier-writing-style
description: Use when an International Economic Review (IER) manuscript's prose, intro, or abstract does not land for a rigor-leaning, broad economics audience. Sharpens the model-to-evidence narrative and the intro; it is a late-stage polish, not a content fix.
---

# Writing Style (ier-writing-style)

## When to trigger

- The intro states what the paper does but never what is *new* and *general* by the end of page two
- A theory paper's proofs crowd out the intuition a non-specialist needs
- The abstract describes the topic but not the result and the contribution
- Reviewers (or coauthors) say the writing is correct but the idea does not "come through"
- The draft is over the ≤50-page ceiling and the prose, not the analysis, is the bloat

## The IER voice: rigorous, but legible to a broad audience

IER's audience is **broad and rigor-leaning** — a macro theorist, an econometrician, and an applied microeconomist may all referee it. So the writing must satisfy two masters: it must be *formally precise* (an IER referee will not forgive sloppy statements of results or assumptions) and *legible across fields* (the general reader must follow the mechanism without specialist priors). The house voice is not the breezy importance-pitch of a top-5 intro, nor the terse method-first prose of an Econometric Society paper — it is **clear formal economics with the intuition kept in the text**.

### The introduction, IER-style (a four-move structure)

1. **The question and why it is general.** One paragraph: the economic question and why it matters beyond one field. Resist the policy-importance hook; lead with the intellectual gap.
2. **What is known and what it cannot do.** The frontier and its consequential limit (from `ier-literature-positioning`), in two or three sentences — not a literature dump.
3. **What this paper does and the one result.** State the contribution as a general object and give the headline result *with its magnitude or sign* on page two. Do not make the reader wait for the result.
4. **How (the mechanism) and the roadmap.** The intuition for why the result holds — the load-bearing assumption named in plain words — then a compact roadmap.

### Sentence- and section-level craft

- **Intuition before algebra.** Every formal result gets a plain-English sentence first; the proof goes to the appendix (`ier-replication-package`).
- **State results precisely.** "We show X under condition C" beats "we find evidence consistent with X." Precision is the house currency.
- **Magnitudes, always.** "8% of the cross-country gap" not "a significant effect." Significance is shown in exhibits as SEs/CIs, not asserted in prose.
- **Cut the throat-clearing.** With a ≤50-page ceiling (检索于 2026-06；以官网为准), every paragraph earns its place; the literature review is positioning, not catalog.
- **Abstract: result-first.** Under the journal's short-abstract norm, lead with the contribution and the result, not the setting (exact word limit 待核实 — check the style guidelines, available on request from the editorial office).

### Writing for three referees at once

Because a macro theorist, an econometrician, and an applied microeconomist may all read the paper, the cross-field reader is the binding constraint on the prose. Two habits help: (1) define field-specific notation and jargon the first time it appears, so the econometrician is not lost in the trade theorist's conventions; and (2) give every formal object a one-line economic gloss — "the parameter γ, the elasticity of substitution between varieties" — so a reader from another subfield never has to guess. This is not dumbing down; it is the legibility a general-interest journal requires, and it is what separates an IER intro from a field-journal intro written for specialists.

### Worked example (illustrative)

A theory paper opens with two pages setting up the model before the reader learns what the paper shows. An IER referee skimming the intro cannot tell if it is worth their time. The fix moves the headline forward: paragraph one states the general question and the gap; paragraph two states the main result ("we show that when search frictions exceed a threshold, the efficient allocation is *not* attainable by a uniform tax — a sharp reversal of the frictionless benchmark") with its sign and condition; only then does the model setup begin. The reader knows the payoff by the bottom of page one, which is exactly when an IER referee decides whether to read on.

### The IER intro is not a top-5 intro

A common mistake is importing the top-5 introduction template — the grand-importance opening, the policy hook, the "this is a first-order question." That register can read as overselling to an IER board that values the *intellectual* contribution over topical importance. The IER intro earns its keep by being precise and quick to the result, not by being momentous. Lead with the gap in our understanding and the result that closes it; if the question also happens to be policy-relevant, mention it in passing, but never make policy relevance the load-bearing reason the paper deserves publication. The reason is always the result's correctness and generality.

### Precision as the house dialect

The sentence-level signature of good IER writing is conditional precision. Compare "we find that minimum wages reduce employment" with "we show that, when labor demand is more elastic than θ*, a binding minimum wage reduces employment; below θ* the sign reverses." The second sentence is longer but it states a *result with its boundary* — which is the unit of contribution at IER. Train every key sentence toward this form: name the conclusion, name the condition, and (in exhibits) name the precision. Vague summary verbs — "suggests," "is associated with," "appears to" — are appropriate only where the evidence genuinely is suggestive; where you have a theorem or a clean estimate, use the verb that matches.

## Checklist

- [ ] The headline result (with magnitude/sign) appears by the end of page two
- [ ] The intro follows the four moves: general question → frontier limit → result → mechanism
- [ ] The intro leads with the intellectual gap, not a policy-importance hook (that's a top-5 frame)
- [ ] Every formal result has a plain-English intuition sentence before the math
- [ ] Results are stated precisely ("under condition C"), not as vague "evidence consistent with"
- [ ] Economic magnitudes are in the prose; significance lives in exhibits as SEs/CIs
- [ ] The abstract is result-first and within the journal's limit (待核实)
- [ ] Total length respects the ≤50-page ceiling

## Anti-patterns

- A top-5-style importance pitch ("this is a first-order question for policy") in place of the intellectual gap
- Making the reader reach the results section to learn the headline result
- Proofs or dense algebra in the body where intuition should be
- "Evidence consistent with" hedging where a precise conditional statement is warranted
- A literature review that catalogs rather than positions
- Prose bloat pushing the paper past 50 pages while the analysis is fine

## Referee pushback mapped to the writing fix

- *"I had to read to Section 4 to learn what you found."* → Move the headline result, with its sign and condition, to page two of the intro.
- *"The intro oversells importance."* → Replace the policy-grandeur hook with the intellectual gap and the result that closes it.
- *"As an [other-subfield] reader I got lost in the notation."* → Define field-specific notation on first use; give every formal object a one-line economic gloss.
- *"You hedge where you have a clean result."* → Replace "evidence consistent with" with the precise conditional ("we show X under condition C").

## Output format

```text
【Journal】International Economic Review
【Skill】ier-writing-style
【Result on page two?】[Y/N]
【Intro four moves】general question / frontier limit / result / mechanism — present? [Y/N]
【Intuition-before-algebra】every formal result has plain-English first? [Y/N]
【Precision】results stated as "under condition C", magnitudes in prose? [Y/N]
【Abstract】result-first and within limit (待核实)? [Y/N]
【Length】within ≤50pp ceiling? [Y/N]
【Verdict】lands / needs-work
【Next skill】ier-replication-package
```
