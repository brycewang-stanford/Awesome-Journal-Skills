---
name: jfm-literature-positioning
description: Use when positioning a Journal of Financial Markets (JFM) manuscript against the microstructure frontier and its broad-finance siblings — staking a contribution the markets-literature insiders will recognize. Positions; it does not invent evidence or citations.
---

# Literature Positioning (jfm-literature-positioning)

## When to trigger

- The contribution sentence is generic ("we study liquidity and X") and a microstructure reader cannot tell what is new
- You are not sure whether the closest prior work is in JFM, JF, JFE, RFS, JFQA, or the Journal of Financial and Quantitative Analysis microstructure issues
- A referee wrote "this is incremental to [known microstructure paper]" or "the canonical citation is missing"
- The theory lineage (Kyle 1985, Glosten-Milgrom 1985, Easley-O'Hara, Amihud-Mendelson) is not anchored
- The paper risks being read as a worse version of a broad-finance result rather than a sharper microstructure one

## Positioning JFM against the broad-finance siblings

JFM referees are specialists; they reward a contribution stated in **microstructure terms** and punish positioning that treats the paper as general finance. The differentiation is not "lower-ranked version of JF" — it is "deeper on market mechanics than JF/RFS would publish."

| Sibling | What they reward | How to position *away* toward JFM |
|---------|------------------|-----------------------------------|
| Journal of Finance (JF) | broad importance, general-interest finance | JFM cut = the *trading-process mechanism*, finer than JF's frame |
| Journal of Financial Economics (JFE) | empirical breadth, often corporate/AP | JFM cut = market-quality / order-flow object, not firm/policy outcome |
| Review of Financial Studies (RFS) | generality + a clean model or design | JFM cut = institutional depth in one market's plumbing |
| JFQA | quantitative finance breadth | JFM cut = microstructure mechanism is the contribution, not a method |

## Building the contribution stack

1. **Anchor the lineage.** Name the canonical microstructure model your result speaks to (information-based: Kyle / Glosten-Milgrom / Easley-O'Hara; inventory: Ho-Stoll / Amihud-Mendelson; liquidity-pricing: Amihud 2002, Pástor-Stambaugh, Acharya-Pedersen). Place your paper as confirming, extending, overturning, or measuring it.
2. **Name the closest 3-5 papers, then the gap.** For each, one sentence of "they show X; we show Y that they could not." Microstructure referees know this literature cold — vagueness reads as ignorance.
3. **State the marginal contribution in trading-process terms.** New measure? New identifying market-structure shock? New venue/asset where the mechanism is tested? New theoretical prediction made testable?
4. **Pre-empt the "incremental" charge.** Show what changes in our understanding of *how markets work* if the result holds — not just a new coefficient.

## Worked positioning (illustrative)

Suppose the result is that a new order type narrows effective spreads. A weak intro says "we study order types and liquidity." A JFM positioning says: Glosten-Milgrom predicts spreads compensate for adverse selection; prior work (name 3-5) shows spreads respond to tick size and to dark trading, but none isolates how *order-type design* alters the adverse-selection component; we exploit the staggered venue rollout to show effective spreads fall by X bps with the permanent (adverse-selection) component falling most, identifying the channel as reduced information leakage rather than inventory cost. That places the paper in the lineage, names the gap, and states the mechanism — exactly what a microstructure referee checks for.

## Common positioning failures and the fix

- *Citing the wrong neighborhood.* A liquidity paper that cites only Fama-French and Carhart but no Amihud / Pástor-Stambaugh / Acharya-Pedersen signals the authors do not know the field. Fix: anchor in the liquidity-pricing lineage first.
- *Survey-style intro.* Twenty citations with no gap statement. Fix: 3-5 closest papers, each with an explicit they/we contrast.
- *Rank-down framing.* "This was not quite enough for JF, so JFM." Fix: position as deeper on mechanism, which JFM rewards and JF would trim.

## Mapping the literature by sub-field

Microstructure has distinct sub-literatures, and positioning means knowing which one you are in and citing its core:

- **Information & adverse selection:** Kyle (1985), Glosten-Milgrom (1985), Easley-O'Hara, PIN/VPIN measurement.
- **Inventory & market making:** Ho-Stoll, Amihud-Mendelson, Stoll's spread decomposition.
- **Liquidity & asset pricing:** Amihud (2002), Pástor-Stambaugh (2003), Acharya-Pedersen (2005), liquidity as a priced risk.
- **Market design & fragmentation:** maker-taker, tick size, dark pools, Reg NMS / MiFID, venue competition.
- **High-frequency / latency:** Hendershott-Jones-Menkveld, Budish-Cramton-Shim, the speed-race literature.

State your sub-field, anchor its core, then bridge to the one or two adjacent sub-fields you touch. A referee from your sub-field will be the one assigned; missing its canon is the fastest credibility loss.

## Checklist

- [ ] The canonical microstructure lineage is cited and the paper is placed relative to it
- [ ] The 3-5 closest papers are named with an explicit "they / we" gap each
- [ ] The contribution is phrased as a trading-process advance, not a generic finance finding
- [ ] The positioning explains why JFM and not JF/JFE/RFS (depth/mechanism, not rank)
- [ ] No canonical microstructure citation is conspicuously missing
- [ ] All cited exemplars are real and verifiable; none invented or marked 待核实 falsely

## Writing the contribution paragraph

The single paragraph that states the contribution is the highest-leverage text in the paper. Build it in four moves: (1) the **open question** in the sub-field, phrased so a specialist nods; (2) **what we do** — the data, setting, and identifying variation in one clause; (3) **what we find** with the headline magnitude in market units; (4) **why it matters for how markets work** — the mechanism the result identifies. Avoid hedged throat-clearing ("we attempt to shed some light on…"); a microstructure editor wants a confident, falsifiable claim. Keep this paragraph verbatim-consistent with the abstract and title so the contribution reads as one idea, not three slightly different ones.

## Citation hygiene the referees check

Microstructure is a tight field; the assigned referee likely authored a paper you should cite. Run a deliberate check: for each sub-field you touch, is the canonical paper present and correctly characterized? Are recent JFM papers on the same mechanism cited (a journal notices when its own literature is ignored)? Is any "first to" claim defensible against a five-minute search? Mischaracterizing a cited paper is worse than omitting it — the author-referee will correct the record sharply. Verify every exemplar against the official archive; never fabricate a citation to fill a gap.

## Anti-patterns

- Citing only broad-finance blockbusters and skipping the microstructure literature the referees wrote
- "First paper to study X" claims a microstructure insider can falsify in one search
- Positioning as a cheaper JF/RFS paper rather than a deeper JFM one
- Burying the contribution in a literature dump with no explicit gap statement
- Listing a general asset-pricing or corporate paper as the closest prior microstructure work

## Output format

```text
【Journal】Journal of Financial Markets (JFM)
【Skill】jfm-literature-positioning
【Canonical lineage】<Kyle / Glosten-Milgrom / Amihud-Mendelson / …>
【Closest work + gap】3-5 papers, each "they show… / we show…"
【Marginal contribution】<new measure / shock / venue / prediction>
【Why JFM not siblings】<depth or mechanism, not rank>
【Source status】verified URL / 待核实 / not asserted
【Next skill】jfm-identification
```
