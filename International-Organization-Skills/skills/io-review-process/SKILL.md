---
name: io-review-process
description: Use to understand how International Organization (IO) evaluates a manuscript — double-blind peer review, expert IR referees, anonymous reviews returned to the author, the decision and revise-and-resubmit process, and IO's distinctive verification of quantitative results and formal proofs before final acceptance. Sets expectations and shapes the paper to survive review; it does not contact editors.
---

# Review Process (io-review-process)

Knowing how IO screens, reviews, and verifies lets you pre-empt the failure modes before submitting. IO
is **double-blind**, reviewed by expert international-relations referees, and — distinctively —
**verifies your quantitative results and formal-model proofs before final acceptance**.

## When to trigger

- Before submitting, to stress-test against the likely IR objections
- Interpreting a decision letter and setting expectations
- Understanding what happens between conditional and final acceptance (verification)
- Planning the revision timeline around the verification step

## How IO review works

1. **Double-blind.** Reviewers do not know the authors and authors do not know reviewers. Anonymize the
   manuscript and use **third-person self-citation** (see `io-submission`).
2. **Editorial screening.** Editors assess fit first: is the international/cross-border phenomenon a
   **major cause or effect**, and does the paper offer a **generalizable IR theory**? Papers that are
   really domestic-politics, or descriptive single-case accounts, are at risk early.
3. **Expert IR review.** Manuscripts go to expert referees (commonly two or more); their **reviews are
   returned anonymously to the author**, and the editors write a decision letter.
4. **Decision + R&R.** Outcomes include reject, revise-and-resubmit, and (eventually) accept. As at peer
   flagships, a first-round accept is rare; an R&R is the realistic good outcome for a strong paper.
5. **Verification before final acceptance (the IO step).** After **conditional acceptance**, the
   editorial staff request data/code; **IO staff re-run quantitative results and verify formal-model
   proofs**, and editors **withhold final acceptance until all reported analyses are confirmed** (see
   `io-transparency-and-data-policy`).

> Exact referee counts, desk-rejection rates, and timelines are not published as fixed numbers —
> treat them as **待核实** and confirm on the live page.

## Shape the paper to pass

- Make the **international-level contribution and generalizable theory explicit** up front (avoids the
  "not really IR" / "just a case" screen).
- Engage the relevant IR debate across paradigms (avoids "missed the key literature").
- Anticipate the strongest rival IR explanation and answer it in the design.
- **Engineer reproducibility and clean proofs now** so verification after conditional acceptance is fast.

## Desk-screen failure patterns (where IO papers die first)

IO's editors triage for fit before sending anything out, so the highest-leverage move is surviving the
screen. The recurring desk-stage rejections at this venue cluster as follows:

| Screen verdict | What the editor saw | Repair before submitting |
|----------------|---------------------|--------------------------|
| "Not really IR" | domestic politics with international data bolted on | re-center so the cross-border phenomenon is the cause/effect (`io-topic-selection`) |
| "Descriptive, not theoretical" | a single-institution account, no portable claim | build a generalizable mechanism (`io-theory-building`) |
| "Already known / incremental" | confirms existing IR consensus | sharpen the live disagreement entered (`io-literature-positioning`) |
| "Narrow significance" | a real finding that only IR-subfield specialists would care about | raise the stakes to a general theory of world politics |
| "Wrong venue" | a pure methods or pure-economics contribution | confirm IO's IR/IPE remit fits the payoff |

Because IO is a specialist flagship, the "not really IR" and "descriptive, not theoretical" screens are
the two most common; both are about the *argument*, not the data.

## What an expert IR referee actually scores

IO referees are working international-relations scholars, frequently from a different paradigm than the
author. In practice they weight: (1) **theoretical contribution** — does a portable theory of
international politics emerge, or just a result; (2) **identification / inferential credibility** on the
paper's own methodological terms; (3) **engagement with the rival tradition** they personally hold; and
(4) **broad significance** to the field. A paper can be airtight empirically and still draw a reject if
the theory is thin — at IO the theory premium dominates, and that ordering is the single most reliable
calibration anchor for predicting a referee's verdict (the precise weighting is referee-dependent and
should not be over-read).

## Anti-patterns

- Submitting a domestic-politics or single-IGO descriptive paper to an IR-theory flagship
- Expecting an accept on first submission; under-investing in the R&R
- Leaving an unscripted analysis or incomplete proofs to "fix at acceptance" — verification will stall
- Breaking anonymity with first-person self-references in a double-blind manuscript
- Reading a thin desk-reject letter as a comment on data quality when it is usually about theoretical reach

## Output format

```
【Fit check】international phenomenon = major cause/effect + generalizable theory? [Y/N]
【IR debate engaged】across relevant traditions? [Y/N]
【Strongest rival】answered in the design? [Y/N]
【Verification-ready】code re-runs + proofs complete for the post-conditional check? [Y/N]
【Realistic outcome】reject / R&R / (rare) accept
【Next】io-submission (or io-rebuttal if decided)
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — double-blind review, anonymous reviews to author, verification-before-final-acceptance policy
