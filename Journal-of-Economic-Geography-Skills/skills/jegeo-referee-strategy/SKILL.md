---
name: jegeo-referee-strategy
description: Use when anticipating referee objections for a Journal of Economic Geography (JEG) manuscript, where the panel typically pairs an economist with a geographer. Maps likely cross-disciplinary objections to fixes; it does not invent results.
---

# Referee Strategy (jegeo-referee-strategy)

## When to trigger

- Before submission, to pre-empt the objections a two-community panel will raise
- The paper leans heavily toward one tradition and you need to armor the side a hostile referee will attack
- You want to decide which robustness/exhibit work is worth doing *now* vs. holding for an R&R
- You are choosing which reviewers to suggest or oppose for a JEG submission

## The defining feature: you will face both communities

JEG's review almost always pairs **an economist** and **a geographer** (the board is drawn from both, and editors deliberately route across the bridge). Their objections are systematically different, and a paper that satisfies one often provokes the other. Plan for both, in one manuscript, under **double-anonymous** review.

| The economist referee tends to attack | The geographer referee tends to attack |
|----------------------------------------|----------------------------------------|
| identification, selection, weak instruments | "where is the geography?" — space as mere fixed effect |
| spatial autocorrelation / overstated inference | absence of mechanism, context, or institutional texture |
| external validity of a single setting | over-formalization that flattens real places |
| whether the model is identified vs. calibrated | a quantitative result with no theory it speaks to |
| magnitude and economic significance | scale/units chosen without geographic reasoning (MAUP) |

## Pre-empting each side

**For the economist referee:** make the identification and inference bulletproof *before* submission — modern staggered estimators, Conley SEs, spillover bounds, a defended instrument (see `jegeo-identification`, `jegeo-robustness`). Report magnitudes, not asterisks. Address external validity head-on.

**For the geographer referee:** make place do real analytical work — name the mechanism in prose, justify the spatial scale substantively, engage the evolutionary/institutional literature, and ensure the maps argue (see `jegeo-theory-model`, `jegeo-tables-figures`). Never let space be only a control.

**The bridge insurance:** the single best defense is a paper where the *mechanism* is the same object both referees can grip — the economist sees it identified, the geographer sees it grounded in place. If you can write that one sentence, you can usually satisfy both.

## Triage: fix now vs. hold for R&R

- **Fix now:** anything that could trigger a desk-reject or a "reject" from either community — missing mechanism, fragile spatial scale, overstated inference, no engagement with half the literature.
- **Anticipate and pre-answer in the text:** known limitations either side will raise — state them and bound them rather than hoping they go unnoticed.
- **Hold for R&R only:** large extensions a referee might request but that are not load-bearing for the current claim; signal willingness without pre-building everything.

## Reviewer suggestions

- Suggest reviewers from **both** communities so the editor can balance the panel; a list skewed to one side signals a one-community paper.
- Oppose reviewers only for genuine conflicts; do not try to engineer an all-friendly panel — JEG editors expect cross-disciplinary scrutiny.

## The cover letter as a routing signal

Under double-anonymous review the cover letter is your one chance to tell the editor how to balance the panel. Use it deliberately:

- Name the paper's contribution in a sentence that signals *both* communities — so the editor knows to seek one economist and one geographer rather than two of either.
- If the paper leans strongly to one tradition, say what it offers the other; this pre-empts the editor reading it as out-of-scope for half the board.
- Suggested and opposed reviewers in the system should reinforce the same message — a balanced list tells the editor you understand JEG is a bridge.

A cover letter that frames the paper as single-community invites a single-community desk read, which at JEG is a fast rejection.

## Checklist

- [ ] Economist-side objections (identification, inference, external validity) pre-empted with specific fixes
- [ ] Geographer-side objections (mechanism, scale, place, literature) pre-empted with specific fixes
- [ ] One mechanism sentence both referees can grip is in the paper
- [ ] Known limitations stated and bounded in-text, not hidden
- [ ] Suggested reviewers span both communities; oppositions are genuine conflicts only
- [ ] Manuscript is double-anonymous-clean (body text, acknowledgments, file metadata)

## Anti-patterns

- Armoring only the side you come from and leaving the other community's objection wide open
- Assuming both referees are economists (or both geographers) — JEG rarely works that way
- A reviewer-suggestion list drawn entirely from one tradition
- Hoping a known spatial-scale or mechanism weakness goes unnoticed rather than pre-answering it
- Trying to stack an all-friendly panel instead of building a paper that survives scrutiny
- Leaving authorship traces that defeat double-anonymity

## Worked vignette (illustrative)

A paper using a quantitative-spatial model to evaluate a transport investment is strong on identification and inference. The author, an economist, armors only that side. Anticipate the geographer referee: they will ask why "region" is the unit (MAUP), where the institutional mechanism is (why do firms actually relocate?), and whether the model flattens real places into representative agents. Pre-empting that side *before* submission — adding a commuting-zone robustness check, a prose mechanism, and a paragraph on heterogeneity across regional contexts — converts a likely split decision into a clean R&R. The economist's questions were already answered; the unanticipated geographer was the real risk.

## A simple pre-submission red-team

Read your own paper twice, once as each referee:

1. **As the economist:** Is anything not identified? Is inference honest under spatial correlation? Would I believe the magnitude? Does it travel beyond this setting?
2. **As the geographer:** Does place do analytical work, or is it a control? Is there a mechanism grounded in real regions and institutions? Is the scale defended? Did the authors engage my literature?

Any "no" in either pass is a risk to fix now or pre-answer in the text — not to discover in the reports.

## Output format

```text
【Journal】Journal of Economic Geography
【Skill】jegeo-referee-strategy
【Economist-side risks】top objections + fix status (now/anticipated/R&R)
【Geographer-side risks】top objections + fix status (now/anticipated/R&R)
【Bridge sentence】the one mechanism both referees can grip
【Reviewer suggestions】names/areas spanning both communities
【Anonymity】double-anonymous clean? [Y/N]
【Next skill】jegeo-submission
```
