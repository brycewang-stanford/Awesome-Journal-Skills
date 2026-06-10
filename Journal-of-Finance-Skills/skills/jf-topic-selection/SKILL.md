---
name: jf-topic-selection
description: Use when judging whether a research question is general-interest and economically significant enough for The Journal of Finance (JF), and when sharpening the framing. Tests fit and contribution; it does not design the empirics.
---

# Topic Selection & General-Interest Fit (jf-topic-selection)

## When to trigger

- Deciding whether a question is "JF-level" or belongs at a field/subfield journal
- The contribution is sound but narrow, and you must judge its reach
- Choosing among JF, JFE, and RFS for a finished paper

## JF's bar: broad, flagship-level, general-interest

JF is the **flagship general-interest journal of the American Finance Association (AFA)**, founded **1946**, published **bimonthly** by Wiley-Blackwell, reaching 8,000+ readers across asset pricing, corporate finance, banking, microstructure, and household finance. With JFE and RFS it is one of the finance **"top-3"**. The acceptance bar is severe: the editor's reports describe roughly a **~5% acceptance rate** with **~33–45% of submissions desk-rejected** (afajof.org editor reports, accessed 2026-05-30). A paper must matter to the **whole** AFA readership, not one subfield.

### How JF differs from JFE / RFS for topic fit
- **JF**: the most general-interest of the three; rewards a single broad result any finance economist would find important.
- **JFE**: tolerates more specialized, results-driven corporate/empirical papers.
- **RFS**: often rewards methodological/technical depth.
If swapping "JF" for a field journal would not change how the paper reads, the topic is probably too narrow for JF.

## Fit test (run before committing)

- Could a corporate-finance reader and an asset-pricing reader both see why this matters? (general interest)
- Is there a single, statable contribution — a **new fact, mechanism, or method**?
- Is the economic magnitude large enough to be flagship-worthy, not just significant?
- Does it speak to a central question the AFA membership cares about?

## General-interest scoring grid

Before committing a scarce JF submission slot, score the question on the dimensions the editor actually screens for. None is sufficient alone; a flagship paper usually clears most:

| Dimension                     | Field-journal version                        | JF-level version                                     |
|-------------------------------|----------------------------------------------|------------------------------------------------------|
| Audience                      | One subfield cares                           | Both asset-pricing and corporate readers see the stake |
| First-order-ness              | A refinement of a known result               | A first-order question the AFA membership debates    |
| Magnitude                     | Statistically significant                    | Economically large (Sharpe gain, % of value, bps)    |
| Credibility                   | Plausible design                             | Clean identification or a well-understood AP test    |
| Durability                    | Period- or sample-specific                   | Likely to hold and be cited across cycles            |

If the paper scores "field-journal" on audience or first-order-ness, the honest move is JFE/RFS or a field outlet — not a JF gamble.

## Worked vignette — is an anomaly "JF-level"?

*Illustrative.* Two anomaly papers land on the desk. Paper A documents a 12-bp/month spread in a niche segment (t = 2.3) that speaks only to short-horizon traders. Paper B documents a 45-bp/month spread tied to a *mechanism* — mispricing of supply-chain risk — that bears on the cross-section and on how firms manage real exposures, with a Sharpe gain of ~0.4 and t = 3.5 after adjustment. Paper A is a competent field-journal result: narrow audience, modest magnitude. Paper B is JF-plausible: a broad corporate reader sees the stake, the magnitude is large, and the mechanism gives reach beyond an anomaly entry. The fit test is not "is it true?" but "would the whole AFA room lean in?"

### Referee-pushback patterns and the JF-specific fix
| Pushback at the desk                            | JF-specific fix                                                 |
|-------------------------------------------------|-----------------------------------------------------------------|
| "Interesting, but for a field journal"          | Surface the first-order, cross-subfield stake in sentence one   |
| "Statistically significant, so what?"           | Lead with the economic magnitude, not the t-stat                |
| "This reads like a JFE submission"              | Re-center the framing on the general-interest reader            |
| "Hasn't this already been shown?"               | Name the closest paper and the delta (`jf-literature-positioning`) |

## Calibration anchors
- The AFA flagship rewards **one broad result a finance economist would find important** over a bundle of narrow ones; breadth of audience beats depth of subfield novelty.
- "Economically large" has no universal threshold — flagship-level magnitude differs across asset pricing and corporate finance; calibrate against recent JF papers in the area rather than a fixed cutoff.

## Checklist

- [ ] One-sentence, general-interest statement of the contribution exists
- [ ] The result matters beyond a single subfield
- [ ] Economic magnitude (not just significance) is flagship-level
- [ ] JF vs. JFE vs. RFS choice is deliberate, not default
- [ ] Recent JF issues confirm the topic is in scope

## Anti-patterns

- A competent but narrow paper pitched to JF "because it's the best journal"
- Framing borrowed from a JFE/RFS submission without re-centering on broad interest
- Confusing statistical significance with flagship-level economic importance
- Ignoring the ~5% acceptance reality when allocating a scarce submission slot

## Output format

```
【General-interest in one sentence?】...
【Contribution type】new fact / new mechanism / new method
【Matters beyond one subfield?】yes / no
【JF vs JFE vs RFS — why JF?】...
【Next step】jf-literature-positioning
```
