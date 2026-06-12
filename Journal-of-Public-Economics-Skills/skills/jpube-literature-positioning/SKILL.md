---
name: jpube-literature-positioning
description: Use when positioning a Journal of Public Economics (JPubE) manuscript against the public-finance literature — locating the contribution relative to the tax, social-insurance, public-expenditure, and optimal-policy frontier without writing a standalone survey. Positions the paper; it does not frame the core contribution (use jpube-contribution-framing).
---

# Literature Positioning (jpube-literature-positioning)

## When to trigger

- The related-work section reads like a survey, not a staking of claim
- You cannot name the two or three papers you are directly building on or beating
- A reviewer might say "this has been done" or "the optimal-tax connection is missing"
- You are unsure which strand of public economics owns your question

## Positioning at JPubE

JPubE referees are public-finance specialists, and they judge the **contribution against the field's own frontier**, not against general economics. Position the paper inside the relevant strand and against the canonical references that define it:

- **Taxable-income / elasticity strand** — Feldstein-style ETI, the Saez–Slemrod–Giertz synthesis, bunching-based elasticity estimates. Say which estimate yours updates and why.
- **Optimal taxation** — the Mirrlees / Diamond–Saez sufficient-statistics tradition. If you estimate a sufficient statistic, connect it explicitly to the optimal-policy formula it feeds.
- **Social insurance** — the Baily–Chetty optimal-UI / insurance-vs.-moral-hazard frontier; the MVPF welfare-comparison program. State which trade-off your evidence sharpens.
- **Public goods, externalities, fiscal federalism** — Samuelson/Pigou foundations and modern corrective-policy evidence.

Locate your contribution as a precise delta on this frontier: a better-identified parameter, a new margin, a setting that tests external validity, or a theoretical extension.

## Positioning moves

- **Name the frontier paper you advance**, then state your one-sentence delta over it.
- **Distinguish identification, not just topic.** "Prior work used cross-sectional variation; we use a reform discontinuity" is a JPubE-legible improvement.
- **Connect estimates to the policy framework** they discipline (optimal tax / optimal UI / MVPF) so referees see the contribution's reach.
- **Cite within the field, author-date.** JPubE uses name-and-year references; integrate citations into the argument rather than a list.

## Checklist

- [ ] The relevant public-economics strand is named explicitly
- [ ] Two or three frontier papers you build on / improve are identified
- [ ] Your one-sentence delta over each is stated
- [ ] The improvement is in identification or welfare reach, not just a new dataset
- [ ] Citations are author-date and woven into the argument, not a standalone survey

## Anti-patterns

- A chronological literature dump with no stated delta
- Positioning against general economics instead of the public-finance frontier
- Claiming novelty while ignoring the canonical optimal-tax / optimal-UI reference
- "First paper to study X in country Y" as the entire contribution


## Strand-claim grid (worked, illustrative)

Locate the delta as a precise sentence against the strand's canonical anchor.

| Strand | Frontier anchor | Your delta (illustrative) |
|--------|-----------------|----------------------------|
| Taxable-income elasticity | Saez–Slemrod–Giertz synthesis | "Prior ETI uses bracket variation; we identify e off a salient kink, halving the bias from mean reversion" |
| Optimal taxation | Diamond–Saez sufficient statistics | "We estimate the migration elasticity that disciplines the top-rate formula, not just the labor margin" |
| Social insurance | Baily–Chetty optimal-UI | "We separate insurance value from moral hazard at the benefit cliff, tightening the optimal-replacement bound" |

A vignette: a draft on a benefit reform recovers a moral-hazard elasticity but positions against general labor economics. The fix re-anchors it on Baily–Chetty and states the delta as a sharper input to the optimal-UI trade-off — the same evidence, now a frontier advance rather than a topical first.

Hedge: which strand "owns" a hybrid question (e.g. tax-and-transfer interactions) is a judgment call — confirm against recent JPubE issues.

## Positioning pass for Journal of Public Economics

Treat this skill as an executable review pass, not a prose hint. First lock the policy instrument, affected margin, identification design, and welfare or incidence interpretation; then judge whether the current manuscript answers the venue's real reader: public economists who ask whether policy design, fiscal incidence, or welfare interpretation is credible.

- **Do the pass:** Build a three-column map: incumbent conversation, unresolved tension, and this manuscript's delta; include one sibling-venue omission that would make a referee doubt the fit.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against JDE for development policy, JIE for cross-border policy, AEJ Economic Policy for broad policy readership; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Strand】tax-elasticity / optimal-tax / social-insurance / public-goods / externality
【Frontier papers】[author-date, ...]
【Delta】one sentence per frontier paper
【Improvement type】identification / welfare reach / new margin / external validity
【Policy framework linked】optimal-tax / optimal-UI / MVPF / none-yet
【Next step】jpube-identification-strategy
```
