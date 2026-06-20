---
name: mathfin-review-process
description: Use when navigating the Mathematical Finance (Wiley) review process — single-blind editor screening, associate-editor handling, and referees who verify proofs line by line. Explains what reviewers at this theory venue check first, common desk-screen failure patterns for theorem-first papers, and how to read review-stage signals.
---

# Review Process (mathfin-review-process)

## When to trigger

- Before submission, to understand the editor and referee lens
- After submission, to interpret review-stage status
- When deciding whether a theorem-first paper is ready for this journal

## Process facts

The accessible Wiley author-guideline text identifies **single-blind peer review**:
the editor screens submissions, suitable papers may be assigned to an Associate
Editor, outside referees may be consulted, and the Associate Editor prepares a
recommendation. The current Wiley product-page metadata checked on 2026-06-20
lists Rama Cont as editor; reopen the live product or editorial-board page before
naming the editor in advice to an author.

## What reviewers evaluate

- Methodological novelty in financial mathematics
- Contribution to financial modelling, not only mathematical difficulty
- Correctness and self-contained completeness of proofs
- Precision of assumptions and notation
- Whether numerical experiments support theory rather than substitute for it
- Fit with the journal's stochastic-analysis and financial-modelling audience

## Desk-risk triggers

- Routine computational application to financial data
- Missing proof for a central claim
- Vague assumptions or unbounded generality
- Contribution framed as pure mathematics with no financial modelling payoff
- Poor LaTeX/source organization that makes review difficult

## What a Mathematical Finance referee reads first

In rough order, before any detailed proof verification:

1. The main theorem statement — is every object in it defined, and is the conclusion sharp
   enough to be interesting to a stochastic-analysis readership?
2. The assumption block — are filtration, integrability, and admissibility conditions stated,
   and do they look both provable and financially sensible?
3. The introduction's novelty claim against the literature the referee knows — usually this
   journal plus *Finance and Stochastics* and the stochastic-analysis canon.
4. The proof of the most surprising step — referees jump straight to the lemma that seems too
   good, and a gap found there colors the entire report.
5. Numerics, if any — only to check they claim nothing the theorems do not license.

Order your own pre-submission read-through the same way.

## Desk-screen failure patterns for theory submissions

- A model proposed with simulations but no theorem about its formal properties.
- The main result is a known theorem re-proved in a cosmetically different model.
- Mathematics with no financial object anywhere in the statements — a probability paper
  wearing a finance title.
- Assumptions scattered through prose so the theorems' scope cannot be reconstructed.
- An abstract promising "applications to trading" that the body never formalizes.

## Reading the silence

Refereeing at proof-checking journals is slow and variable because arguments are verified, not
skimmed; months of quiet carry little signal. Avoid folklore about average handling times —
confirm any expectations against the journal's current author guidelines or recent author
experience. A status query is reasonable after an extended wait; route it through the
editorial office.

## Reviewer packet

Prepare a compact packet before submission:

- One sentence naming the financial modelling problem and the mathematical object solved.
- A theorem map: main result, assumptions, proof tools, and where each proof is located.
- A novelty note against the two or three closest Mathematical Finance-adjacent papers.
- A numerical-evidence note, if present, explaining which theorem or modelling implication the exhibit
  illustrates.
- A weakness note: the strongest assumption, boundary case, or modelling simplification, with a sentence
  explaining why it is acceptable.

This packet is not submitted verbatim; it is a discipline check. If you cannot write it, the paper is not
ready for the single-blind editor/AE/referee chain.

## Decision vocabulary at this venue

Major revision on a theory paper usually means the mathematics is salvageable but at least one
proof needs real work; minor revision means exposition and bookkeeping. A reject-with-
encouragement signal often points at the novelty axis rather than correctness — treat it as a
repositioning task before any re-proof. These labels are not standardized across editors, so
read the AE's summary paragraph, not the label.

## Output format

```text
[Stage] editor screen / AE / referee / decision
[Main risk] novelty / rigor / fit / exposition
[Action] ...
[Next step] mathfin-submission or mathfin-rebuttal
```
