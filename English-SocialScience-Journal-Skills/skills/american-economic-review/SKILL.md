---
name: american-economic-review
description: Use when targeting American Economic Review (AER) or deciding whether an economics manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# American Economic Review (american-economic-review)

## Journal positioning

AER is the flagship general-interest journal of the American Economic Association and one of the economics "top-5" (with QJE, JPE, Econometrica, REStud). It wants papers of broad interest to economists across fields, with a first-order question, a credible answer, and a result that changes how the profession thinks — not an incremental field paper. The audience is the whole discipline, so the contribution must read as important to someone outside your subfield.

A full lifecycle pack for AER ships separately as `AER-skills` (the `aer-*` skills). This profile is the quick fit / venue-selection layer; route into `aer-workflow` for step-by-step drafting and submission.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the AEA site or the editorial-manager submission system.

## When to trigger

- The author names AER (or AER as a stretch target) as the venue.
- A paper has a clean research design and a question of general interest, and the author is choosing between AER and a top field journal.
- A strong field paper needs re-framing so the contribution reads as discipline-wide rather than niche.
- The author needs AER's desk-reject risks and a credible top-5 / top-field alternative list.

## Scope & topic fit

- First-order questions across all fields of economics — micro, macro, labor, public, IO, trade, development, finance-adjacent — judged on general interest.
- Empirical papers with a transparent, defensible identification strategy.
- Theory papers whose results are general and consequential, not a narrow extension.
- Consider the sibling AEJs (`aej-applied-economics`, `aej-macroeconomics`, `aej-microeconomics`, `aej-economic-policy`) and short-format `aer-insights` when the contribution is excellent but narrower than AER's general-interest bar.

## Method & evidence bar

- Identification is the desk filter: naive TWFE on staggered treatment, weak or unjustified instruments, and RDD without density/covariate-smoothness evidence get rejected fast.
- Empirical work is expected to pre-empt the obvious threats (selection, measurement, confounders) with design, not hand-waving; modern DiD estimators, proper inference, and robustness are baseline.
- Structural and theory papers need clearly stated assumptions, identification of structural parameters, and results that generalize.
- Data and code transparency is mandatory; AEA enforces a data and code availability policy with verification.

## Structure & house style

- The introduction must, in its first pages, state the question, the contribution, the approach, and the headline result — and say explicitly why a non-specialist should care.
- Make the marginal contribution non-overlapping: separate the theory/identification advance from the empirical finding from the policy reading.
- AER uses an unstructured abstract, JEL codes, and a tightly disciplined main text with online appendices for everything secondary.
- Exhibits are expected to be self-contained and publication-clean; the headline result should be legible from one table or figure.

## Official-submission checklist

- Search the live site for "American Economic Review submission guidelines" and the AEA "Data and Code Availability Policy" and follow the current versions.
- Re-check submission fee, formatting, abstract/JEL requirements, anonymization expectations, and figure/table standards on the editorial-manager system.
- Re-check the current data/code deposit and verification workflow (openICPSR / AEA Data Editor) — this is enforced before acceptance.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating why an economist outside your field should care about this result.
- [ ] The contribution is stated as identification / theory / measurement, not as statistical significance.
- [ ] The introduction positions the paper against the current top-5 / top-field frontier on this question.
- [ ] Identification threats are addressed by design; inference and DiD/IV/RDD choices are state-of-the-art.
- [ ] Data and code are ready for the AEA availability + verification workflow.

## Common desk-reject triggers

- A well-executed but narrow field paper with no general-interest hook.
- Identification that the profession no longer accepts (TWFE on staggered adoption, weak IV, cosmetic RDD).
- Contribution framed as "first to study X in context Y" without a methodological or conceptual advance.
- Significance treated as the finding; mechanism and external validity left thin.

## Re-routing decision

- Narrower-but-excellent applied → `aej-applied-economics`; macro → `aej-macroeconomics` or `review-of-economic-dynamics`; micro theory → `aej-microeconomics` or `journal-of-economic-theory`; policy → `aej-economic-policy` or `journal-of-public-economics`.
- Short, sharp, single-result papers → `aer-insights`.
- Field-leading specialist work → the relevant top field journal (`journal-of-labor-economics`, `journal-of-development-economics`, `journal-of-public-economics`, `journal-of-finance`, etc.).

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] American Economic Review
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the identification / theory clear AER's general-interest bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / fee / JEL / data-code policy / exhibits>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
