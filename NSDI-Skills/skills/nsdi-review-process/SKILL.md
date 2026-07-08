---
name: nsdi-review-process
description: Use when interpreting where an NSDI submission stands — the per-deadline PC pipeline, the three-way outcome space of accept, one-shot revision, and reject, the cross-deadline resubmission ban, reviewer continuity across revisions, and what each decision letter actually commits the authors to.
---

# NSDI Review Process

NSDI's review machinery differs from single-deadline conferences in one structural
way: decisions are moves in a multi-deadline game, not endpoints. Reading a decision
letter correctly requires knowing which moves it opens and which it closes. Mechanics
below are the NSDI '27 CFP and the NSDI '26 multiple-deadlines page as rendered on
2026-07-08.

## Pipeline shape

Each deadline (spring, fall) runs its own double-blind PC review on its own HotCRP
site, producing its own decision cohort — NSDI even publishes per-cohort
accepted-paper lists before the symposium. Within a cohort:

- Reviews are written against the paper as submitted; the rendered '27 CFP describes
  **no author-response phase** between reviews and decisions (absence 待核实 — check
  the current cycle's pages before relying on it). Plan as if the submission must
  argue for itself (`nsdi-author-response`).
- Review loads are bounded upstream by the **eight-submissions-per-author cap**,
  which exists to protect PC bandwidth — expect enforcement, not flexibility.
- Notifications land on published dates: July 23, 2026 for '27 spring;
  December 8, 2026 for '27 fall.

## The three-way outcome space

| Decision | What it means | What it opens / closes |
|---|---|---|
| Accept | into the cohort's program | final paper, artifact evaluation, presenter duties |
| One-shot revision | conditional path: reviewers issue a list of required issues | resubmit at a subsequent deadline (possibly next year's NSDI); same reviewers where possible; **one** attempt |
| Reject | out, with a ban attached | cannot enter the **next** deadline; spring reject skips same-edition fall, fall reject skips next edition's spring |

The one-shot revision is neither a rebuttal nor journal-style R&R-until-done. Its
grammar: the reviewers' issue list is exhaustive and binding; the revision is judged
on whether those issues are fixed; a revision that dodges them is rejected **without
another revision option**. Institutional continuity is built in — the same reviewers
re-review where possible, and PC members who issue one-shot revisions at a fall
deadline are required to serve as external reviewers the following year, so the
issue list is written by people expecting to check it.

## What reviewers reward and punish

Reading NSDI reviews (and pre-empting them) is easier with the venue's evaluative
axes explicit:

- **Design contribution to networked systems or the stack** — the scope clause
  functions as review criterion; "solid work, wrong venue" is a real NSDI outcome
  (`nsdi-topic-selection`).
- **Practical evaluation** — trace realism, incumbent baselines, tail visibility
  (`nsdi-experiments`).
- **Honesty about limits** — named failure regimes read as strength.
- **Track-contract fulfillment** — operational papers judged on depth of deployed
  experience; frontiers papers on boldness and framing rather than completeness.

## Decoding common letters

```text
"One-shot revision. Required: (1) compare against <deployed system>;
 (2) evaluate under churn; (3) clarify lease-expiry semantics."
   -> A funded offer. Cost it (~2 machine-months + rewrite), reserve the
      testbed now, target the named next deadline. Success odds are good
      *because* the same reviewers check their own list.

"Reject. The contribution is an application of known techniques; the
 networking stack is unchanged."
   -> Scope verdict, not effort verdict. Re-route (SIGCOMM? OSDI?) or
      re-center the design contribution. Ban: skip one NSDI deadline.

"Reject. Evaluation limited to microbenchmarks on a two-node setup."
   -> Evidence-rung verdict. The ban window is exactly the time to climb
      a rung (trace replay, scale-out) before the after-next deadline.
```

## Ban arithmetic, worked

A paper rejected at fall '26 (notified December 9, 2025 — the '26-cycle dates)
could not enter spring '27 (April 2026) and became eligible again at fall '27
(September 2026). Generalize: **a plain rejection costs one deadline ≈ 5 months of
eligibility**, which is precisely why `nsdi-workflow` treats speculative submissions
as spending a real option, and why the strongest response to a borderline draft is
often holding it one gate.

## Signals to mine from the reviews themselves

Whatever the outcome, NSDI reviews carry venue-calibrated information worth
extracting systematically:

- **Which track bar was applied** — reviews that fault a research-track paper for
  missing deployment experience (or vice versa) reveal a track mismatch to fix
  before any resubmission.
- **Which baseline the community considers canonical** — a named "why not X?"
  defines the comparison the next version cannot skip.
- **Repeated confusion across reviewers** — two reviewers misreading the same
  mechanism marks a writing defect, not two reading defects
  (`nsdi-writing-style`).
- **The evidence rung the scores imply** — enthusiasm plus low confidence often
  means the idea landed but the evaluation did not reach the rung the claim needs
  (`nsdi-experiments`).

## Confidentiality and conduct

Reviews and PC deliberations are confidential; submissions are read under
double-blind rules with declared conflicts recused via HotCRP. Do not contact PC
members about a pending paper; process questions go to the program co-chairs
(named on the current conference page; the '27 pair 待核实). Decisions are not
relitigated by email — the sanctioned channel for disagreement is the revision or
the next eligible submission.

## Output format

```text
[Cohort] spring/fall + year; notification date; days remaining
[Outcome] accept / one-shot revision / reject
[If revision] issue list -> cost -> feasible target deadline
[If reject] ban window (dates); scope vs evidence diagnosis; re-route call
[Reviewer continuity] same-reviewer expectations affecting strategy
[Next action] single highest-leverage step, dated
```
