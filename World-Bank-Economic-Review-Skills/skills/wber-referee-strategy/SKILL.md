---
name: wber-referee-strategy
description: Use when anticipating referee and editor objections before submitting to The World Bank Economic Review (WBER) — pre-empting the predictable development-economics pushbacks (external validity, identification, data quality, policy relevance) and writing the cover letter. Plans defenses; it does not run new analysis.
---

# Referee Strategy (wber-referee-strategy)

## When to trigger

- The paper is near submission and you want to surface objections before a referee does
- You are writing the cover letter and choosing how to frame the contribution to the editor
- You suspect one referee will be a hard-identification economist and another a policy reader
- You want to decide which robustness checks to pre-load in the paper vs. hold for the response
- You are unsure whether the framing will survive the "is this a World Bank paper?" reflex

## Who referees WBER — and what they punish

WBER's review is **single-anonymized** (referees are anonymous; your name is on the title page), and editors (Eric Edmonds and Nina Pavcnik, Dartmouth, 检索于 2026-06；以官网为准) draw on a development-economics referee pool that overlaps heavily with JDE, AEJ: Applied, and the AEA journals. Expect **two referee archetypes** and write for both:

- **The identification referee** — sophisticated about staggered-DiD bias, weak IV, RD manipulation, attrition, spillovers. Punishes asserted exclusion restrictions, TWFE on staggered timing, and overreach beyond the estimand.
- **The policy/development referee** — asks "so what for development policy?", "does this generalize?", "what about general equilibrium and cost?". Punishes project-report framing and results with no scale-up relevance.

A paper that satisfies only one archetype is the canonical WBER R&R-or-reject. Pre-empt both.

## The predictable WBER objections (pre-empt in the paper)

| Likely objection | Pre-emption to build in before submitting |
|------------------|-------------------------------------------|
| "This is a project report, not general-interest" | Frame around a transferable mechanism; state external validity explicitly (`wber-topic-selection`, `wber-identification`) |
| "Identification rests on an untested assumption" | Show the diagnostic that could have failed; report design-specific sensitivity (`wber-identification`, `wber-robustness`) |
| "Developing-country data quality is suspect" | Measurement-error and coverage checks against an alternative source (`wber-robustness`) |
| "The LATE won't survive scale-up" | Discuss complier-vs-population, GE channels, fiscal cost (`wber-identification`) |
| "Why WBER and not JDE / World Development?" | One intro sentence on the policy-audience contribution (`wber-literature-positioning`) |
| "Not reproducible" | Have the data/code package and DOI-linked DAS ready (`wber-replication-package`) |

## The cover letter

- **Name the development question and the policy decision** in the first two sentences — give the editor the "why this journal" instantly.
- **State the contribution as a claim** with a magnitude, and the identification in one line.
- **Pre-empt the sibling question:** one sentence on why this is WBER, not JDE/World Development/Research Observer.
- **Note the data/code package** is prepared and the data availability statement is in place.
- **Suggest reviewers honestly** (if the portal asks) across both archetypes; flag genuine conflicts.
- Keep it under a page; do not restate the abstract verbatim.

## Pre-load vs. hold in reserve

Not every check belongs in the submitted paper. Decide deliberately:

- **Pre-load in the paper:** the design diagnostic the identification referee will demand first (balance/pre-trends/density/first-stage), the headline robustness, and the external-validity/cost paragraph. These are cheap insurance against a fast reject.
- **Hold in reserve (ready to run):** exotic robustness a referee *might* ask for, alternative estimators that would bloat the main text, and extended heterogeneity. Have the code ready so you can produce them in one round if asked, without padding the 40 pages now.

The judgment call: anything a competent referee would *certainly* ask goes in the paper; anything they *might* ask is held, code-ready, for the response letter.

## Checklist

- [ ] Both referee archetypes (identification + policy) explicitly addressed in the paper
- [ ] Each predictable objection has a pre-emption already in the text, not held in reserve
- [ ] External validity / scale-up / cost is in the paper, not only the cover letter
- [ ] The "why WBER not a sibling" sentence is in both the intro and the cover letter
- [ ] Data/code package and DOI-linked DAS ready before submission
- [ ] Cover letter names the policy decision in the opening lines and states a magnitude
- [ ] Suggested reviewers (if requested) span both archetypes; conflicts disclosed

## Anti-patterns

- Writing only for the identification referee and ignoring the policy reader (or vice versa)
- Holding back the obvious robustness check, hoping no one asks — they will
- A cover letter that restates the abstract and never says "why WBER"
- Leaving external validity entirely to the cover letter instead of the paper
- Assuming single-anonymized review hides the authors — your name is on the title page; reputation and self-citation are visible
- Suggesting only friendly reviewers from one camp

## Self-citation and the single-anonymized reality

Because WBER review is single-anonymized, referees can see who you are — so the usual double-blind tricks do not apply and can backfire. Do not over-cite yourself to signal authority; do not strip your own relevant prior work to feign novelty (a referee who knows your record will notice). Cite your prior work where it is genuinely the right reference, in the third person, and let the contribution stand on the new result. Treat the referees as informed colleagues who may well know your earlier papers better than you expect.

## Worked vignette (illustrative)

Before submitting an RD evaluation of a subsidy, the authors war-game two reports. The identification referee will challenge manipulation at the eligibility score; they pre-load a Cattaneo–Jansson–Ma density test and a donut check. The policy referee will ask whether a local-at-cutoff effect justifies a national change; they add a paragraph on the complier population and a back-of-envelope fiscal cost at scale. The cover letter opens: "Governments spend billions on means-tested subsidies but lack credible estimates of marginal effects; using [country]'s eligibility threshold we estimate a 5pp enrollment gain at $90 per enrollee." Both archetypes are answered before review begins.

## Output format

```text
【Identification referee】top objection + pre-emption in paper
【Policy referee】top objection + pre-emption in paper
【External validity / cost】in the paper? [Y/N]
【Why-WBER sentence】in intro AND cover letter? [Y/N]
【Package readiness】data/code + DOI DAS ready? [Y/N]
【Cover letter】names policy decision + magnitude in opening? [Y/N]
【Next step】wber-submission
```
