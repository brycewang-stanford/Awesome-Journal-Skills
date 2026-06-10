---
name: red-contribution-framing
description: Use when framing the marginal contribution of a Review of Economic Dynamics (RED) manuscript — stating the quantitative or dynamic advance in terms the SED readership values (a new mechanism, a new method, a new quantitative result, or model-disciplining evidence) and aligning the abstract and introduction around it.
---

# Contribution Framing for RED (red-contribution-framing)

## When to trigger

- Distilling "what is new" before drafting the abstract and introduction
- A paper with several results but no clear single advance
- Translating a technical contribution into something the SED audience immediately grasps

## Framing a RED contribution

RED rewards a sharp, **dynamic/quantitative** contribution. Pick the dominant type and lead with it:

- **New mechanism** — a dynamic force (e.g., a feedback through expectations, distribution, or
  accumulation) that changes the model's predictions; show what turns it on and what it does to key moments.
- **New method** — a solution, estimation, or computational technique that makes a class of dynamic
  models tractable or more accurate; show the gain over the prior state of the art.
- **New quantitative result** — a calibrated/estimated model delivering a magnitude that matters for
  theory or policy; lead with the number and the moment it matches.
- **Model-disciplining evidence** — empirical dynamics that pin down or refute a model element.

State the contribution as a **delta against the closest existing model**, not as a description of the
paper. Make the abstract (≤250 words, stand-alone) carry the headline result and magnitude; the
introduction should make the mechanism legible before the math.

## Checklist

- [ ] One dominant contribution type is chosen and leads the abstract/intro
- [ ] The advance is stated as a quantitative/mechanistic delta with a magnitude where possible
- [ ] The contribution is framed for the SED/dynamic-economics readership
- [ ] No diffuse "we also do X, Y, Z" list crowding out the headline

## Anti-patterns

- Framing the paper as a tour of results rather than one clear advance
- Hiding the magnitude or the mechanism behind notation
- Claiming generality the model or evidence does not support

## Contribution stress test

Before declaring the framing done, write these four objects:

1. **Closest dynamic model**: the predecessor model, method, or calibration the paper changes.
2. **Mechanism delta**: the one force the old model missed and the new model turns on.
3. **Quantitative delta**: the moment, transition path, welfare number, or policy response that moves.
4. **Scope delta**: the class of economies, shocks, agents, or constraints where the result is meant to hold.

If the answer to item 2 is only "we use newer data," the paper is probably not framed as a RED
contribution yet. Route to `red-literature-positioning` or `red-identification-strategy`.

## Worked vignette: framing a HANK liquidity paper

Suppose a draft solves a two-asset HANK model and finds fiscal transfers raise consumption more when
liquid wealth is concentrated near the borrowing constraint. Run the stress test (numbers illustrative):

1. **Closest dynamic model**: a one-asset Bewley–Huggett economy in which the transfer multiplier is small.
2. **Mechanism delta**: the liquid/illiquid portfolio friction puts ~30% of households in a high-MPC region.
3. **Quantitative delta**: the cumulative consumption response to a 1%-of-GDP transfer rises from 0.3 to
   0.55 — substitute the paper's own numbers.
4. **Scope delta**: holds in economies whose liquid-wealth distribution matches SCF moments; knife-edge if
   portfolio adjustment costs go to zero.

The abstract leads with item 3 and names item 2; items 1 and 4 belong in the introduction's second and
closing paragraphs.

## Contribution statement block

Draft the framing as a fill-in block before touching the abstract:

```
【Closest model】[author-year + one-line description of the predecessor economy]
【Mechanism delta】[the dynamic force turned on: friction, shock process, heterogeneity margin]
【Quantitative delta】[moment / transition path / welfare number that moves, with magnitude and units]
【Discipline】[which calibrated or estimated targets pin the new force down]
【Scope】[class of economies where the claim holds; the knife-edge case]
【One-sentence pitch】[the sentence an SED discussant would put on slide 1]
```

If 【Quantitative delta】 is empty, the paper is a theory note — defensible at RED, but the framing must
then lead with the mechanism and its analytic characterization instead of a number.

## Referee pushback on contribution claims

| Pushback heard at RED | Venue-specific fix |
|---|---|
| "The mechanism already exists in [closest paper]" | Show the moment or transition path the predecessor cannot generate, not just a modeling difference |
| "The magnitude is calibration-driven" | Re-run the delta under the predecessor's calibration; separate mechanism from parameter choice |
| "This is a comparative static, not dynamics" | Lead with the transition path or IRF; if a steady-state comparison is the point, argue why adjustment dynamics are second-order |
| "Headline number lacks discipline" | Tie it to explicit targeted moments and show untargeted fit beside it |

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — abstract limit and scope sources
