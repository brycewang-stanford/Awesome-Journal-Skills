---
name: jeea-literature-positioning
description: Use when the contribution of a Journal of the European Economic Association (JEEA) manuscript relative to the frontier is fuzzy, oversold, or undersold. Stakes the marginal contribution for a general-interest readership; it does not fix identification, the model, or prose.
---

# Literature Positioning (jeea-literature-positioning)

## When to trigger

- The "we are the first to…" claim is fragile or unverifiable
- A referee could name three close papers you have not distinguished from
- The contribution paragraph lists what you do, not what is *new*
- The paper reads as incremental relative to an obvious recent reference

## The JEEA positioning bar

JEEA is a **general-interest** journal, so positioning must convince a broad reader — not just subfield specialists — that the **marginal contribution** is real and consequential. Two failure modes are fatal here: (1) the contribution is genuine but framed for insiders, so a general-interest co-editor cannot see it; (2) the contribution is overstated relative to a close paper a referee will instantly recall. Position against the **frontier**, name the closest 2–3 papers explicitly, and state in one sentence what your paper establishes that none of them does.

## Positioning moves

- **Locate the frontier, not a strawman.** Cite the strongest, most recent work on the question; positioning against a dated or weak paper invites a desk objection.
- **Name the delta.** Finish the sentence "Relative to [closest paper], we are the first to show that …" with something a referee cannot already point to.
- **Separate three kinds of novelty:** (i) a new **question/answer**, (ii) a new **identification** of an old question, (iii) a new **theoretical result/mechanism**. JEEA rewards (i) and (iii) most; (ii) must be paired with a substantive payoff.
- **Travel test.** State why the contribution matters beyond the immediate literature — the general-interest lesson — so the paper is not "one more entry" in a niche.
- **Credit honestly.** Acknowledge what close papers got right; over-claiming against them is the single most common referee complaint.

## Contribution paragraph template

1. The question and why it is open at the frontier.
2. The closest 2–3 papers and exactly what they leave unresolved.
3. What this paper establishes that they do not (the delta, in one sentence).
4. Why that delta matters to a general economics reader (the travel test).
5. The scope: what the contribution does **not** claim.

## Checklist

- [ ] Closest 2–3 frontier papers named and distinguished from, not strawmanned
- [ ] One-sentence delta written and survivable against a referee who knows those papers
- [ ] Novelty type identified (question / identification / theory) and matched to the payoff
- [ ] Travel test passed — the contribution matters beyond the niche
- [ ] Scope limits stated; no "first to" claim you cannot defend

## Anti-patterns

- "First to study X" when a quick search finds a close predecessor (instant credibility loss)
- Positioning against a weak strawman instead of the genuine frontier
- A contribution list ("we do A, B, C") with no statement of what is *new*
- Burying the delta under a literature review that reads as a survey
- Over-claiming a marginal identification tweak as a conceptual breakthrough
- A literature review padded to demonstrate reading rather than to locate the gap

## Positioning across JEEA's breadth

Because JEEA is field-agnostic, the *kind* of frontier you position against differs by paper type, and a general-interest co-editor expects you to engage the right one:

- **Theory paper:** position against the closest models, not the closest applications; the delta is a result, a weaker assumption, or a unifying mechanism (route to `jeea-theory-model`).
- **Applied micro / development:** position against the closest *estimates* of the same parameter; the delta is usually a more credible design or a previously unmeasured margin (route to `jeea-identification`).
- **Macro / finance:** position against both the empirical regularity and the model that rationalizes it; the delta often reconciles the two.

In every case the general-interest test is the same: a reader outside the subfield should grasp *why the delta matters* without already knowing the literature.

## Worked vignette (illustrative)

A draft on minimum wages claims to be "the first causal estimate of employment effects." A referee instantly recalls a dozen close papers. The JEEA-grade revision names the three closest recent estimates, concedes what they established (small disemployment effects in their settings), and states the genuine delta in one sentence: "Relative to [X, Y, Z], we are the first to separate the wage-floor effect from the simultaneous benefit-schedule change, using a reform that moved only the floor." The travel test follows: the result tells any policymaker that bundled reforms have been misattributing effects. The contribution is now defensible against the very referees who know the literature best.

## Output format

```
【Frontier papers】[closest 2–3, cited]
【Delta】"Relative to [X], we are the first to show that ___"
【Novelty type】question / identification / theory
【Travel test】why it matters to a general reader
【Scope limit】what we do NOT claim
【Next step】jeea-identification or jeea-theory-model
```
