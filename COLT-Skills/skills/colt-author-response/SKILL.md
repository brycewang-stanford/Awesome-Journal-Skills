---
name: colt-author-response
description: Use when drafting a COLT (Conference on Learning Theory) rebuttal after initial reviews, handling proof-correctness objections, tightness and novelty-of-technique challenges, the area-chair identity-reveal rule, and concession strategy for theorem-first papers where one unrepaired gap outweighs every polished answer.
---

# COLT Author Response

Use this after COLT reviews arrive. The COLT 2026 CFP (checked 2026-07-08) stated that
initial reviews are sent to authors before final decisions and that authors get an
opportunity to address issues raised — a rebuttal phase, run through CMT in that cycle.
Exact window length, character limits, and attachment rules are announced with the
reviews; read that announcement before writing a word.

## What a COLT rebuttal is for

A COLT review stands or falls on correctness first, then on the significance of the
result and the novelty of the technique. The rebuttal is your one chance to:

- repair a *perceived* gap by pointing at the exact appendix line that closes it;
- concede a *real* gap and show the damage is contained (a weaker constant, an extra
  log factor, a mildly stronger assumption) with a sketch of the fix;
- correct a factual misreading of the model, the adversary, or the oracle access;
- defuse "this follows easily from known results" by naming precisely which step known
  techniques cannot deliver.

It is not a place to announce new theorems. A brand-new result in a rebuttal box is
unverifiable in the time reviewers have, and theory reviewers discount it accordingly;
promise it for the final version only when the argument is a routine extension.

## The identity-reveal rule (distinctively COLT)

Under the 2026 policy, submissions are anonymized and names are withheld from
reviewers, but the area chair knows author identities and *may reveal them to a
reviewer during the rebuttal period upon the reviewer's request*, when the AC judges it
necessary for a proper review — typically to check adjacency to the authors' own prior
work. Consequences for drafting:

- Never write anything inconsistent with your identity becoming known mid-discussion.
- Do not play games with "the authors of [7]" phrasing that collapses if unmasked.
- You still must not de-anonymize yourself proactively; the reveal is the AC's call.

## Objection playbook for theorist reviewers

| Objection | What it usually means | COLT-ready move |
|---|---|---|
| "The proof of Lemma 3 has a gap at (12)" | The reviewer traced the chain and stopped | Give the missing two-line argument verbatim, or concede and show the repaired constant |
| "The bound is not tight; the lower bound is missing" | Result may be a partial story | Point to the matching lower bound if it exists; otherwise scope the claim and cite the open gap honestly |
| "This follows from [X] by a standard reduction" | Novelty-of-technique attack | Exhibit the concrete step where the reduction fails — the exact quantity [X] cannot control |
| "The assumption of bounded losses is restrictive" | Generality probe | Say whether the proof survives sub-Gaussian relaxation, and where it breaks if not |
| "The model is non-standard" | Fit and significance doubt | Anchor the model to a named line of prior COLT/ALT work and state what changes and why |

## Drafting pattern

1. One-line verdict per major objection: *correct as stated*, *misreading*, or
   *conceded with contained damage* — reviewers scan for whether you dodged.
2. Quote the exact display or lemma number; theory reviewers verify pointers, and a
   wrong pointer costs more credibility than a concession.
3. Keep arithmetic in the rebuttal self-contained: if the fix is three inequalities,
   write the three inequalities rather than "this is easy to fix."
4. End each thread with what the final version will say, phrased as revision of
   existing material, not as new claims.

## Worked micro-example

Reviewer: "Theorem 2's regret bound hides the dependence on the action-set diameter D;
for unbounded D the claim is vacuous."

```text
Verdict: misreading, with a wording fix we will make.
The D-dependence is present but implicit: the radius enters through the
self-bounding term in Eq. (9), and Lemma 5 (App. B.2) gives
    R_T <= 4 D sqrt(T log K) + D log T.
D is assumed finite in Section 2 (line 3 of the setup). We agree the theorem
statement should carry D explicitly; the final version will state
R_T = O(D sqrt(T log K)) in Theorem 2 itself rather than in the proof.
```

Four sentences, one display, an exact pointer, one concrete promised edit — the whole
anatomy of a COLT rebuttal thread.

## Rebuttal anti-patterns theorists punish

- **The pointer dodge:** "see Appendix C" with no line number and no restatement of
  the resolving argument. If the referee misread C once, a bare pointer re-serves the
  same meal.
- **The generality retreat:** answering a tightness question by claiming the result
  "still holds in more general settings" — orthogonal to the objection and visibly so.
- **The authority appeal:** "this technique is standard in the literature" without a
  citation containing the actual step; worse if the identity-reveal rule later shows
  you were citing yourself.
- **The scope creep:** using the rebuttal to advertise results proved after
  submission; at best ignored, at worst it signals the submitted version was premature.
- **The wounded tone:** any sentence about the review's fairness rather than its
  mathematics. The AC reads tone as information about how camera-ready fixes would go.
- **The uniform-length trap:** giving every objection equal space, which tells the AC
  you could not identify the decision-critical one.

## Prioritization under a short window

- Rank objections by decision weight: correctness gap > tightness/lower-bound gap >
  novelty-of-technique > model fit > exposition. Answer in that order and cut from the
  bottom when space runs out.
- If two reviewers disagree (one says the technique is standard, the other says the
  model is exotic), answer both in one paragraph that names the technique's new step —
  the AC reads the rebuttal for exactly this synthesis.
- A calm, complete concession of a minor error buys credibility for your defense of
  the main theorem; theorists reward authors who behave like referees of their own work.

## Cycle-volatility warnings

- Rebuttal length limits, whether PDF responses are allowed, and per-reviewer versus
  global response structure change by cycle — read the current instructions (待核实
  each year).
- The identity-reveal mechanism described above is the 2026 wording; verify it in the
  cycle you are in before relying on its exact scope.

## Output format

```text
[Priority objection] <the one that decides the paper>
[Verdict] correct as stated / misreading / conceded, damage contained
[Pointer] <lemma, display, or appendix line>
[Self-contained fix] <inequalities or sketch given in-box>
[Promised final-version edit] <existing-material revision only>
```
