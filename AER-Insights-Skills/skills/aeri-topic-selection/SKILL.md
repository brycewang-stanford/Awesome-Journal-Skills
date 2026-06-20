---
name: aeri-topic-selection
description: Use when deciding whether a project is the ONE crisp, important, well-identified insight that an American Economic Review: Insights (AER: Insights) short-format manuscript requires, rather than a multi-result paper for AER or a field paper for the AEJ family. Tests single-insight fit; it does not run the analysis.
---

# Topic Selection — Single-Insight Fit (aeri-topic-selection)

## When to trigger

- A project has a strong main result but also two or three secondary results
- Unsure whether to send to AER: Insights, AER, or an AEJ field journal
- The draft is creeping past the word cap because there is more than one idea
- A result feels surprising and clean but you are unsure it is "important enough"

## The AER: Insights bar: one idea, AER-level importance, short

AER: Insights publishes **short, self-contained papers built around a single important, well-executed idea**. The decision is not "is this good?" but "**is there exactly ONE crisp, surprising, well-identified insight that can stand alone in a short paper at AER-level importance?**" Three filters:

1. **Single-insight test.** State the paper in **one sentence** with one headline object (one estimate, one theorem, one fact, one method-changes-the-answer result). If you need "and" to describe the contribution, you likely have an AER paper or two AER: Insights papers, not one.
2. **Importance test.** The single insight must clear **AER-level general interest** — a non-specialist economist should care. AER: Insights is *short*, not *minor*; a small or incremental result is a reject regardless of length.
3. **Self-containment test.** The whole argument — setup, identification, headline result, the one or two checks that matter — must fit in **≤7,000 words (minus 200 per exhibit, ≤5 exhibits)** with everything else in the online appendix. If the core argument cannot be made short, it is not an AER: Insights paper.

## Where it goes if it is NOT AER: Insights

| Symptom | Better venue |
|---------|--------------|
| Multiple inter-dependent results that need each other | AER (long, multi-result flagship) |
| One result but field-specific, not general interest | AEJ: Applied / Micro / Macro / Policy |
| Incremental / a robustness note on existing work | a field journal or a comment |
| Pure methods with no substantive payoff in a short paper | a methods/econometrics journal |

## Sharpening a candidate into a single insight

- **Pick the headline.** Of the results you have, which ONE is most surprising and most cleanly identified? Make that the paper; demote the rest.
- **Cut, do not summarize.** Secondary results become appendix material or a future paper — not a compressed in-text paragraph.
- **Name the surprise.** AER: Insights rewards a result that overturns or sharply refines a prior belief; write the prior you are correcting.
- **Confirm identification early** ([`aeri-identification`](../aeri-identification/SKILL.md)) — a clean insight with a shaky design is not publishable short, because there is no room to defend a weak design.

## Common AER: Insights archetypes (and what makes each "one insight")

| Archetype | The single insight is… | Failure mode |
|-----------|------------------------|--------------|
| One clean causal estimate | a single headline effect from a credible design | reporting every heterogeneity split in-text |
| A striking new fact / measurement | one important fact a non-specialist did not know | a descriptive paper with no single takeaway |
| A sharp theory result | one surprising theorem / impossibility | a general framework with the result as a corollary |
| A method that flips an answer | the substantive answer it changes, in few pages | the method shown without a substantive payoff |

## Worked vignette (illustrative)

A fictional project has (a) a clean RCT effect of posted wages on women's applications, (b) a heterogeneity
split by occupation, and (c) a structural extension on wage offers. The AER: Insights paper is **(a) alone** —
one surprising, general-interest, cleanly identified effect. (b) and (c) go to the Supplemental Appendix or
a separate paper. Compressing all three into one short paper would be a "mini-AER" and likely a reject; the
discipline is to make (a) the entire paper and defend it superbly in few pages.

## Going-or-not-going decision

If you cannot pass all three filters — single insight, AER-level importance, self-containment — the honest
move is to route elsewhere (AER for multi-result, an *AEJ* for field interest) rather than force-fit. The
fast, no-R&R process ([`aeri-referee-strategy`](../aeri-referee-strategy/SKILL.md)) punishes a borderline
fit with a quick reject.

## Checklist

- [ ] The paper is stated in **one sentence** with a single headline object
- [ ] The insight clears AER-level **general-interest importance** (not just length-appropriate)
- [ ] A **clear prior belief** is named that the result overturns or sharply refines
- [ ] The full argument plausibly fits the cap with secondary material in the appendix
- [ ] Venue checked vs. AER (multi-result) and AEJ (field) — AER: Insights chosen deliberately
- [ ] Identification is clean enough to defend in a short paper

## Anti-patterns

- A "mini-AER": one main result plus several supporting results kept in-text
- A correct but **incremental** result pitched as short-because-small
- A field-interest result with no general-interest hook
- Splitting one idea across two thin papers, or fusing two ideas into one over-cap paper
- Choosing AER: Insights for speed when the idea genuinely needs AER's length

## Output format

```
【One-sentence insight】<single headline object>
【Importance】why a non-specialist cares (general interest, AER-level)
【Prior overturned】<belief the result corrects>
【Fits short format?】core argument under cap, rest to appendix? [Y/N]
【Venue check】AER: Insights vs AER vs AEJ — chosen because […]
【Next step】aeri-literature-positioning
```
