---
name: restat-literature-positioning
description: Use when the marginal contribution of a The Review of Economics and Statistics (REStat) manuscript against the closest prior work is fuzzy, generic, or oversold. Stakes the contribution precisely; it does not run analysis or write the full literature review.
---

# Literature Positioning (restat-literature-positioning)

## When to trigger

- The intro's "we contribute to several literatures" reads as a citation dump
- A referee could ask "how is this different from [obvious prior paper]?" and you lack a one-line answer
- The contribution is stated as a topic ("we study X") rather than a delta against named work
- You are unsure whether your measurement / identification advance is genuinely new

## The REStat positioning bar

REStat referees are applied economists who **know the closest five papers cold**. Positioning must be a **precise delta against named work**, not a tour of a literature. Because REStat prizes **measurement and credible identification**, the most persuasive deltas are of two kinds: (1) **identification delta** — your design credibly estimates a parameter prior work could only correlate or estimate under weaker assumptions; (2) **measurement delta** — you measure the object better (new data, less error, a validated index) and that *changes an applied conclusion*. "First to study" is rarely the contribution; "first to credibly identify / cleanly measure, and it overturns/sharpens [conclusion]" is.

## How to stake the contribution

1. **Name the 3–5 closest papers** — the ones a referee will compare you to first, by author-year.
2. **State the delta against each** in one clause: what they did, what you do differently, why it matters.
3. **Classify your delta:** new identification | better measurement | new setting that is itself informative | reconciles conflicting prior estimates.
4. **Quantify the stakes where possible:** "prior estimates range 0.2–0.8 because of [bias]; our design pins it at [X]."
5. **State scope honestly:** what your contribution does *not* claim (external validity, mechanism, generality).

## Positioning patterns that land at REStat

| Pattern | Example shape |
|---------|---------------|
| Identification upgrade | "Prior work used OLS/TWFE; we use [RD / IV / het-robust DID] and the estimate changes" |
| Measurement upgrade | "Prior work proxied [X] with [noisy measure]; our better-measured [X] reverses the sign/magnitude" |
| Reconciliation | "Estimates disagree across studies; we show the gap is [selection / measurement / specification]" |
| Better-powered / wider data | "We bring [bigger / cleaner / linked] data that resolves an under-powered debate" |
| Applied use of a method | "We apply [estimator] to [setting] where its assumptions hold, recovering [parameter]" |

## Checklist

- [ ] 3–5 closest papers named by author-year, not just cited in a block
- [ ] A one-clause delta stated against each closest paper
- [ ] Delta classified (identification / measurement / setting / reconciliation)
- [ ] Stakes quantified or sharply described (what changes if you are right)
- [ ] Scope limits stated — what the contribution does NOT claim
- [ ] No "first to study" claim doing the work a real delta should do

## Anti-patterns

- A literature *tour* (paragraphs of "X did A, Y did B, Z did C") with no delta
- "First to study [topic]" as the contribution (REStat referees discount novelty-of-topic)
- Overclaiming generality a single applied setting cannot support
- Ignoring the single closest paper because it is inconvenient (referees will name it)
- Citing methods papers to look sophisticated while the applied delta stays vague

## Worked vignette: turning a tour into a delta (illustrative)

A draft opens: "A large literature studies the minimum wage's employment effects (A, B, C…). We add to this
literature." A REStat referee reads that as no contribution. The fix is to name the **single closest paper**
and state the delta: *"Paper B estimated this with TWFE across staggered state increases and found a small
disemployment effect; we re-estimate with a heterogeneity-robust estimator on the same variation and a
better-measured teen-employment series, and the effect is statistically indistinguishable from zero — the
earlier negative estimate was driven by forbidden comparisons and measurement error."* That is a delta
(identification + measurement) that **reconciles a contested estimate**, with stakes a referee can weigh.

## Output format

```
【Closest prior work】[paper1 / paper2 / paper3 (/4/5)] by author-year
【Delta vs each】p1: [...]; p2: [...]; p3: [...]
【Delta type】identification | measurement | setting | reconciliation
【Stakes】what changes if we are right: [...]
【Scope NOT claimed】[...]
【Next step】restat-identification
```
