---
name: jimf-writing-style
description: Use when the prose, intro, abstract, or Highlights of a Journal of International Money and Finance (JIMF) manuscript do not land for an international-finance audience. Sharpens the writing and front matter; it does not change the result or the design.
---

# Writing Style (jimf-writing-style)

## When to trigger

- The intro buries the international mechanism and the contribution under a literature tour
- The abstract is over 250 words, vague, or does not state the headline number
- Highlights and keywords are missing or generic (required for Elsevier submission)
- The prose reads like a domestic-finance paper with international words sprinkled in
- A policy reader (central bank / IMF / BIS) cannot extract the takeaway in one read

## The JIMF voice

JIMF prose is **empirical, direct, and policy-aware**. It is not the model-first register of the theory journals nor the corporate-finance register of JFE; it is open-economy macro-finance written for an audience that includes both academics and policy economists. Lead with the international question and the answer; make the mechanism a noun the reader can hold (pass-through, spillover, push factor, the trilemma); and quantify the headline early. Write the abstract and intro last, after the design and robustness settle.

### The intro, JIMF-style (a five-move opening)
1. **The international question** in one or two sentences — frame it as open-economy, not domestic.
2. **Why it matters now** — a policy or market hook (a tightening cycle, a capital-flow surge, a currency crisis, the GFCy debate).
3. **What you do** — the design and the identifying variation, in plain terms (the cleaned surprise, the cross-country interaction, the policy experiment).
4. **The headline finding with a number** — "a 25bp US surprise raises EM spreads by X bp, concentrated in open-account countries," not "we find significant effects."
5. **The contribution against the frontier** — one sentence locating you in the GFCy / DCP-ERPT / spillovers / sovereign program (see `jimf-literature-positioning`).

### Abstract & front matter (Elsevier mechanics)
- **Abstract ≤250 words** (检索于 2026-06；以官网为准), factual, with the headline magnitude and the policy implication. No undefined acronyms.
- **Highlights**: 3–5 short bullets (≤85 characters each is the Elsevier convention — 待核实), each a finding, not a topic.
- **Keywords** plus **JEL codes** (F31, F32, F36, E44, G15 and neighbors are the usual JIMF territory).
- Define every acronym on first use (UIP, ERPT, GFCy, FXI, NEER) — a policy reader may not share the academic shorthand.

## When to invoke this skill (and when not to)

Writing style is a late-stage polish. Do not rewrite the intro or abstract while the identification, the cross-country design, or the headline magnitude are still moving — you will rewrite them again, and a polished claim built on an unsettled result is worse than no polish, because it commits you in prose to a number that may change. Invoke this skill once the empirical layer is stable and the contribution is staked, when the remaining gap is that the paper does not *read* like a JIMF paper. The abstract and intro are genuinely written last, after `jimf-robustness` and `jimf-tables-figures` have settled what the paper actually shows.

## Craft moves

1. **Name the mechanism, repeatedly and consistently.** Pick one term for your channel and use it throughout; do not alternate "spillover," "transmission," and "contagion" loosely — they mean different things in this field.
2. **Quantify in interpretable units.** Basis points per 25bp surprise, percent per 1 s.d. of the global factor, percent of GDP for flows — not raw coefficients.
3. **Separate the economics from the econometrics.** State what the result means for an open economy before the inference details.
4. **Write for the policy reader without dumbing down.** The conclusion should give a central banker or IMF economist a defensible, bounded takeaway and its limits.
5. **Keep the international margin in every section header and topic sentence** so the paper never drifts into reading as domestic.

## Writing for two audiences in one paper

JIMF's readership spans academic international-finance economists and policy economists at central banks, the IMF, and the BIS. Serve both without splitting the paper: keep the *economics* (what the result means for an open economy) in the topic sentences where a policy reader will find it, and keep the *econometrics* (the identification and inference machinery) in the body of each section where a specialist will scrutinize it. The conclusion is the policy reader's section — give a bounded, honestly caveated takeaway ("our estimates imply capital-account management, not the exchange-rate regime, is the binding margin for monetary autonomy in our sample, though the result is identified off open-economy variation and may not extend to closed-account regimes"). A paper that reads as all-econometrics loses the policy reader; one that reads as all-narrative loses the referee.

## Checklist

- [ ] Intro states the international question, the design, and the headline number in the first page
- [ ] The mechanism is one consistent named channel throughout
- [ ] Abstract ≤250 words, factual, with a magnitude and a policy implication
- [ ] Highlights (3–5 finding-bullets), keywords, and JEL codes present
- [ ] Headline effects reported in interpretable units, not raw coefficients
- [ ] Every acronym defined on first use; no domestic-paper drift
- [ ] Field terms used precisely (pass-through, spillover vs. contagion vs. transmission, push/pull, de jure/de facto)
- [ ] Economics in topic sentences for the policy reader; econometrics in the body for the specialist
- [ ] Conclusion gives a bounded takeaway for a policy reader

## Anti-patterns

- An intro that spends two pages on the literature before saying what the paper does
- An abstract that says "we find significant effects" with no number and no policy point
- Missing Highlights/keywords/JEL — an Elsevier submission gap that signals carelessness
- Using "spillover," "contagion," and "transmission" interchangeably when they are distinct claims
- Reporting raw coefficients the reader cannot interpret instead of scaled, unit-bearing magnitudes
- Prose that would read identically if the paper were domestic — the international margin invisible in the writing

## Vocabulary discipline (the international-finance register)

Field terms carry precise meanings; use them exactly. *Pass-through* is the elasticity of prices to the exchange rate, distinct from *exchange-rate disconnect*. *Spillover* is a cross-border effect of a domestic shock; *contagion* implies excess co-movement beyond fundamentals; *transmission* is the channel — do not swap them. *Push* factors are global/external drivers of flows; *pull* factors are domestic. *Sterilized* vs. *unsterilized* FX intervention are different operations. *De jure* vs. *de facto* exchange-rate regime are different classifications. Mixing these is the fastest way to signal that the paper is written from outside the field; getting them right signals the opposite.

## Worked vignette (illustrative)

A draft's abstract reads: "We study capital flows and monetary policy and find significant relationships across countries." The JIMF rewrite: "Foreign monetary tightening drives portfolio outflows from emerging markets, but only where the capital account is open: a 25bp US surprise lowers EM bond inflows by X% of GDP in open-account economies and has no effect in closed ones, sharpening the global-financial-cycle vs. trilemma debate. The result implies capital-account management, not the exchange-rate regime, is the binding margin for monetary autonomy." Now the international mechanism, the magnitude, and the policy stake are all in one paragraph under 250 words.

## Output format

```text
【Journal】Journal of International Money and Finance
【Skill】jimf-writing-style
【Intro】question + design + headline number on page 1? [Y/N]
【Mechanism】one consistent named channel? [Y/N]
【Abstract】≤250 words, factual, magnitude + policy point? [Y/N]
【Front matter】Highlights + keywords + JEL present? [Y/N]
【Units】interpretable magnitudes, not raw coefficients? [Y/N]
【Source status】abstract/Highlights limits verified / 待核实
【Next skill】jimf-submission
```
