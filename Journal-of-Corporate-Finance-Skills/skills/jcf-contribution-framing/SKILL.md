---
name: jcf-contribution-framing
description: Use when sharpening the stated contribution of a Journal of Corporate Finance (JCF) manuscript — turning a result into a crisp "what is new and why it matters to corporate finance" claim that survives the editor's desk screen. It frames the pitch (abstract, intro, cover letter); it does not run analysis.
---

# Contribution Framing (jcf-contribution-framing)

## When to trigger

- Writing the abstract's contribution sentence and the introduction's "we show / we contribute" arc
- Drafting the cover-letter pitch the handling editor reads first
- Deciding whether the contribution is strong enough to clear active desk-rejection

## What a JCF contribution looks like

JCF runs an **active desk-rejection policy**: the editors state that a non-trivial fraction of papers are rejected without full review. The contribution must be legible in the abstract and first page. A strong JCF contribution typically:

- Identifies a **corporate-finance friction or decision** (structure, governance, payout, contracting, M&A, international) and a **clean answer** to a sharp question.
- States **what is new** relative to the closest 2–3 papers — a new mechanism, a new identification, new data, or a decisive test.
- Says **why it matters** — for theory, for managers/investors, or for policy — without over-claiming.

## Framing checklist

- [ ] One-sentence contribution that names the question, the design, and the result
- [ ] The novelty is **incremental-but-clear**, not "first ever" hyperbole
- [ ] Magnitude (not just sign/significance) is in the headline claim
- [ ] Scope of the claim **matches the design** (no causal language an OLS cannot bear)
- [ ] The "so what" is explicit for at least one audience

## Cover-letter pitch (Editorial Manager)

A tight paragraph: the question, the identification, the headline result with a number, and the fit to JCF's corporate-finance remit. Avoid a multi-page defensive letter — the editor is screening fast.

## Contribution triage for the JCF desk screen

Grade the claim before polishing prose. Editors running an active desk-rejection policy sort contributions fast:

```text
Contribution type                          | JCF desk survival | What to add before submitting
New mechanism for a known firm decision    | Strong            | One decisive test separating it from the old mechanism
New quasi-experimental shock, old question | Strong            | Show prior designs were confounded, not merely older
New hand-collected governance data         | Moderate          | A question only this data answers, plus a real design
Larger sample / newer period, same spec    | Weak              | A reason the answer should differ now — or reframe
Cross-country extension of a US result     | Moderate          | Institutional variation doing genuine identifying work
Methods demonstration on firm data         | Weak              | Route to a methods outlet, or find the finance question
```

If the row reads Weak, repair the contribution before drafting the abstract — wording cannot rescue it at this venue.

## Worked vignette: pitching a payout paper

Hypothetical setup (all numbers illustrative): a dividend-tax reform raises the tax penalty on dividends relative to repurchases for a subset of firms. Pitch v1: "We study payout policy after the reform and find significant effects." That restates the regression. Apply the rules:

- Name the decision: substitution from dividends to repurchases under a tax friction.
- Add the design: difference-in-differences around the reform, treated versus exempt firms, firm and year fixed effects.
- Add the magnitude: treated firms cut dividends by an illustrative 18% of the pre-reform mean and raise repurchases by 0.6 percentage points of assets, leaving total payout roughly flat.
- Add the so-what: payout composition, not payout level, absorbs tax shocks — informing the dividend-clientele debate and repurchase regulation.

Final sentence: "Exploiting a dividend-tax reform in a difference-in-differences design, we show treated firms substitute repurchases for dividends nearly one-for-one — composition, not total payout, absorbs the tax shock." That clears the one-sentence test: question, design, result, magnitude.

## Referee pushback on framing — and the JCF fix

- "The contribution is incremental." → Quantify the increment: state what the closest paper could not rule out and which test here rules it out. Incremental-but-decisive beats novel-but-vague at JCF.
- "This is an asset-pricing/accounting paper." → Re-anchor the headline on the firm decision (financing, investment, payout, governance); demote the returns evidence to a supporting exhibit.
- "Why JCF and not a general outlet?" → The cover letter names the corporate-finance conversation the paper moves; a general-interest framing with no firm friction reads as misrouted.
- "The abstract over-claims causality." → Downgrade verbs to match the design: "consistent with" for matching evidence, causal verbs only for the quasi-experimental estimates.

## Anti-patterns

- "First paper to study X" claims a referee can falsify in one search.
- A contribution that restates the regression instead of the idea.
- Over-claiming causality beyond what the design supports (see jcf-identification-strategy).
- Burying the contribution under literature review.

## Output

```
【Contribution】<one sentence: question + design + result>
【Novelty】<vs. 2–3 closest>  【So what】<audience + payoff>
【Over-claim risk】[low/med/high] + fix
```
