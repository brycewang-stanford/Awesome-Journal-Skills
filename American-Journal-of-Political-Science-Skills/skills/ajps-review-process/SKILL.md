---
name: ajps-review-process
description: Use to understand how the American Journal of Political Science (AJPS) evaluates a manuscript — double-blind peer review, desk screening, decision categories, the methodology-only Research Note and Correspondence routes, and the third-party verification that follows acceptance. Sets expectations and shapes the paper to survive review; it does not contact editors.
---

# Review Process (ajps-review-process)

Knowing how AJPS screens, decides, and then **verifies** lets you pre-empt failure modes before
submitting. AJPS is **double-blind**, published by Wiley for the MPSA, and pairs ordinary peer review
with a **post-acceptance third-party verification** step that no in-house-only journal has (see
`ajps-replication-and-verification`).

## When to trigger

- Before submitting, to stress-test the paper against likely rejection grounds
- Deciding whether the paper is an Article, a methodology/meta-analysis **Research Note**, or a
  **Correspondence**
- Interpreting a decision letter and setting expectations
- Understanding what happens between "accept" and "in print"

## How AJPS review works

1. **Double-blind.** Reviewers do not know the authors and authors do not know reviewers. Anonymize
   accordingly (see `ajps-submission`).
2. **Editorial screening.** The editorial team screens for fit, contribution, and methods before
   sending to external review; weak-fit or out-of-scope papers can be returned without full review.
3. **External review.** Papers passing the screen go to expert reviewers who weigh identification,
   contribution, and rigor.
4. **Decision** (typical): **reject**, **revise and resubmit (R&R)**, or **accept**. Most accepted
   papers pass through at least one R&R.
5. **Then verification.** After acceptance, replication materials are deposited and **re-run by an
   independent verifier** to confirm they reproduce the main-text numbers — publication waits on
   successful verification (see `ajps-replication-and-verification`).

## Type-specific routes

- **Research Note** — reserved for **methodology** (including methodology in normative theory) and
  **meta-analyses**, <= 4,000 words. A short empirical study is **not** a Note.
- **Correspondence** — critical responses to work **already published in AJPS**, <= 4,000 words. A
  Correspondence flagging only a minor error (mislabeled variable, misreported result, coding error)
  may be **desk-rejected**.

## Shape the paper to pass

- Make the contribution and its generalizable payoff explicit and early.
- Match the empirical claim to what the design identifies (avoids the "overclaims causality" rejection).
- Clear ethics/IRB and human-subjects documentation up front (the portal asks for it).
- Engineer the analysis to re-run cleanly now — verification at acceptance is real, not a formality.

## Anti-patterns

- Submitting a short empirical paper as a (methodology-only) Research Note
- Sending a Correspondence about a non-AJPS paper, or over a trivial error
- Overclaiming causal identification the design cannot support
- Leaving reproducibility for "later" — it becomes a hard gate after acceptance


## Review-risk pass for American Journal of Political Science

Run this as a concrete capability pass. First lock the political theory, design leverage, measurement validity, and scope condition; then test whether the manuscript addresses political-science reviewers who expect tight theory, transparent design, and a contribution that travels across political settings.

- **Primary move:** Turn likely reviewer objections into a ledger with response evidence, manuscript location, and the decision-maker who must be convinced first.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against APSR for field-wide breadth, Journal of Politics for broader political-science audience, Political Analysis for methods-first work; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Type fit】Article / Research Note (methodology|meta-analysis) / Correspondence — correct? [Y/N]
【Contribution】generalizable payoff explicit and early? [Y/N]
【Claim vs design】empirical claim matches identification? [Y/N]
【Ethics/IRB】documentation ready? [Y/N]
【Realistic outcome】reject / R&R / (rare) accept
【After accept】verification re-run will match? [Y/N]
【Next】ajps-submission (or ajps-rebuttal if decided)
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — double-blind review, submission types, and verification-after-acceptance
