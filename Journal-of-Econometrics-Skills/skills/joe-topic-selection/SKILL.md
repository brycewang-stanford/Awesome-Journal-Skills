---
name: joe-topic-selection
description: Use when deciding whether a project is a genuine methodological contribution for the Journal of Econometrics (JoE) versus a purely applied result better placed elsewhere. Pressure-tests the idea against JoE's theory-plus-applied-methods scope before months are spent.
---

# Methodological Topic Selection (joe-topic-selection)

## When to trigger

- You have an empirical finding and wonder if there is a "methods paper" inside it
- You have a new estimator/test but are unsure it clears a top methodology bar
- You cannot state in one sentence what econometric problem the paper solves
- You are unsure whether JoE, a field journal, or a pure-theory venue is the right home

## The JoE scope bar

The *Journal of Econometrics* (Elsevier, founded 1973) publishes **substantive contributions to econometric methodology** — identification, estimation, testing, decision, and prediction problems arising in economic research, plus **applications of econometric techniques** to economics. The strong house norm is a **methodological advance with mathematical rigor** (a new estimator, test, identification result, or asymptotic theory, with proofs and/or asymptotic derivations). Purely empirical or applied work **without** a methodological contribution is typically **out of scope**. At the other end, *pure* statistical theory with no econometric/economic motivation may be steered toward more theory-oriented or statistics venues (companion Elsevier outlets such as *Econometrics and Statistics* overlap in scope).

So the test is two-sided. Ask:

1. **What econometric problem does this solve?** Name the estimand, the failure of existing methods, and why it matters for *economic* data (e.g., endogeneity, weak identification, nonstationarity, high dimensionality, clustered/dependent data, heterogeneity).
2. **Is the advance real?** A better estimator (efficiency, robustness, weaker assumptions), a new test with proven size/power properties, a new identification result, or new asymptotics — not a relabeling of a known method.
3. **Is there an economic anchor?** JoE prizes methods *motivated by and useful for* economics, ideally with an empirical illustration, not abstract statistics.

## Three submission tracks shape topic fit

- **Regular Issues** — standalone methodological papers (the default).
- **Annals Issues** — focused volumes on a coherent theme.
- **Themed Issues** — topic-based collections, often conference-originated, where proposers may serve as **Guest Associate Editors**. If your work fits an active theme, that route can be a strong fit; check the live Themes page for current calls.

## Decision shortcuts

- "I have a result but the method is standard" → not JoE; target a field journal
- "I have a new estimator but no economic problem behind it" → tighten the motivation or target a statistics venue
- "New test + proven properties + economic application" → strong JoE fit → `joe-literature-positioning`
- "Pure proof, no application, very abstract" → consider a theory venue; for JoE, add an econometric anchor and illustration

## Anti-patterns

- Dressing an applied paper as methods with a thin "we also propose an estimator" section
- A method with no asymptotic theory and no Monte Carlo — JoE expects both
- Ignoring the closest existing estimator and overclaiming novelty


## Fit pass for Journal of Econometrics

Use this as a second-pass capability check. First lock the estimand or theorem, assumptions, asymptotic/simulation evidence, and applied relevance; then test whether the manuscript addresses econometrics reviewers who expect methodological novelty, assumptions, simulation or empirical illustration, and reproducibility.

- **Primary move:** Score fit, novelty, evidence readiness, and audience ownership; reject prestige-only targeting when a sibling venue owns the contribution.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against Econometric Theory for proof-first work, JBES for applied statistical methods, Quantitative Economics for economics-theory methods; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Econometric problem】one sentence
【Existing methods & their failure】...
【Proposed advance】estimator / test / identification / asymptotics
【Economic anchor / illustration】...
【Track】Regular / Annals / Themed
【Verdict】JoE fit / field journal / theory venue
【Next step】joe-literature-positioning
```
