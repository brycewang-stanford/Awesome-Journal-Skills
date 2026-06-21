---
name: aeja-literature-positioning
description: Use when the marginal contribution of an American Economic Journal: Applied Economics (AEJ: Applied) manuscript is fuzzy or undersold and must be staked precisely against prior applied-micro work. Positions the contribution; it does not fix the identification (aeja-identification) or the prose (aeja-writing-style).
---

# Literature Positioning (aeja-literature-positioning)

## When to trigger

- A referee or co-author asks "what is new here relative to [closely related paper]?"
- The introduction cites a wall of references but never states the marginal addition
- You are unsure whether your contribution is an *answer*, a *design*, a *setting*, or a *measurement*
- The paper risks reading as a replication or a marginal extension of an existing AEJ: Applied / AER paper

## The AEJ: Applied contribution bar

At AEJ: Applied the contribution is judged as: **a credibly identified answer to a question the applied-micro community has not yet settled**, positioned against the *closest* prior work — not the whole field. Editors and referees reward a contribution that is **specific, honest, and load-bearing**. Name your contribution type, then position only against the papers that threaten it.

| Contribution type | What "new" must mean | Positioning move |
|-------------------|----------------------|------------------|
| New **answer** | a magnitude prior work did not credibly estimate | show why prior designs failed to identify it |
| New **design / source of variation** | a cleaner identification of a known question | contrast your design's assumptions vs. the standard one |
| New **setting / population** | external validity that changes the lesson | argue why this setting is informative, not just available |
| New **mechanism** | decomposing a known effect into channels | show the prior literature left the channel ambiguous |
| New **measurement** | a quantity nobody could measure before | establish the measure's validity, not just its novelty |

## Positioning craft

1. **The three-paper test.** Name the three papers closest to yours and write one sentence each on what they establish and what they leave open. Your contribution lives in the "leave open" gaps.
2. **The honest delta.** State the marginal addition in one sentence the closest author would *agree with*. If they would say "we already did that," the delta is too thin.
3. **Position by design, not by topic.** "First paper on X in country Y" is weak; "first credibly identified estimate of X because design D removes confound C" is strong.
4. **Cite siblings correctly.** Distinguish what AER, AEJ: Policy, and field journals have established so you are not re-claiming settled ground.

## Checklist

- [ ] Contribution type named (answer / design / setting / mechanism / measurement)
- [ ] Three closest papers identified, each with "establishes / leaves open" sentences
- [ ] One-sentence honest delta the closest author would accept
- [ ] Positioned by identification, not merely by topic or geography
- [ ] No overclaim of "first" without the design reason prior work left it open
- [ ] Related sibling-journal results acknowledged (AER / AEJ: Policy / field) so nothing settled is re-claimed

## Anti-patterns

- A literature-review "tour" with no stated marginal addition (a top AEJ: Applied referee reflex)
- Claiming "first to study X" when the novelty is only setting or data, not identification
- Positioning against distant papers to dodge the closest competitor
- Inflating the gap by ignoring a recent paper that already partly closed it
- Burying the contribution sentence on page 6 instead of paragraph 1–2 of the intro

## Worked vignette (illustrative)

A draft claims to be "the first study of cash transfers and schooling in [country]." A referee replies that
three RCTs already estimate this effect elsewhere, so geography is not a contribution. The AEJ: Applied fix
is to reposition by *identification and mechanism*: the closest papers estimate the effect where transfers
are conditional, leaving open the unconditional case; this paper exploits an unconditional rollout and shows
the schooling response is half as large (illustrative), isolating the conditionality channel. The
contribution becomes a *mechanism* the closest authors would agree they did not pin down — not a new map pin.

## Referee pushback mapped to the positioning fix

- *"This is incremental relative to [closest paper]."* → State the honest delta in one sentence the closest
  author would accept; show the specific gap their design left open.
- *"You claim 'first' but it is just a new setting."* → Reframe as a cleaner identification or a new
  mechanism, with the design reason prior work left it open.
- *"You ignore [recent paper] that already does this."* → Cite it, state precisely what it settled, and
  position in the residual gap rather than the whole field.

## Output format

```
【Contribution type】answer / design / setting / mechanism / measurement
【Three closest papers】1) ___ (open: ___) 2) ___ (open: ___) 3) ___ (open: ___)
【Honest delta】one sentence the closest author would accept
【Positioned by】identification reason prior work left it open: ___
【Sibling check】settled by AER/AEJ:Policy/field that we do NOT re-claim: ___
【Next step】aeja-identification (or aeja-writing-style if design is settled)
```
