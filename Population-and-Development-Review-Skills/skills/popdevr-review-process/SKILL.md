---
name: popdevr-review-process
description: Use when you need to understand how Population and Development Review (PDR, Wiley / Population Council) evaluates a manuscript — an editorial-committee screen before external review, double-anonymized peer review by at least two referees, and a typical ~3-month time to first decision. Sets expectations and shapes the paper to survive review; it does not contact editors.
---

# Review Process (popdevr-review-process)

Knowing how PDR screens and decides lets you pre-empt the failure modes before submitting. PDR runs an
**editorial / committee screen** first, then **double-anonymized** external review by at least two
referees, with a first decision typically around **three months** (verify current timelines). 待核实.

## When to trigger

- Before submitting, to stress-test against the screen and likely reviewer objections
- Interpreting a decision letter and setting expectations
- Understanding why a paper can be declined without external review
- Deciding how to anonymize and how to frame the population-and-development contribution

## How PDR review works

1. **Editorial / committee screen first.** Editors (with an editorial committee) read every submission
   and decide whether to send it out. A paper can be **declined before review** for poor fit with the
   population-and-development scope or low likelihood of favorable external reviews. This usually happens
   within the first weeks.
2. **Double-anonymized review.** If sent out, the paper goes to **at least two referees**; authors are
   not told reviewer identities and reviewers are not told author identities. **Remove all identifying
   information about all co-authors** so anonymity holds (see `popdevr-submission`).
3. **Expert, cross-field referees.** Reviewers are typically expert demographers and/or development
   scholars; both the population evidence and its development meaning will be scrutinized.
4. **Time to decision.** Authors can expect written comments and a decision roughly **three months** after
   submission (a norm, not a guarantee — confirm on the author page). 待核实.
5. **Decision and revision.** Standard scholarly outcomes (reject / revise-and-resubmit / accept);
   confirm exact categories and any timelines on the official page. 待核实.

## Shape the paper to pass

- Make the **population-and-development connection and broad interest** explicit (avoids the off-fit
  decline) — see `popdevr-topic-selection` and `popdevr-literature-positioning`.
- Get the **method right** (rates, exposure, identification, comparability) so expert referees see rigor.
- Anticipate the strongest rival (reverse causation, selection, comparability) and answer it in the design.
- For a synthetic essay, make the **framework's contribution and boundary** unmistakable — a vague essay
  is the classic decline.

## Anti-patterns

- Submitting a clean estimate with no development/policy payoff (off-fit decline)
- Leaving self-identifying references that compromise double-anonymized review
- A synthetic essay that summarizes rather than reorganizes (low likelihood of favorable reviews)
- Expecting external review for a paper unlikely to earn favorable reviews — that is a decline ground

## Review-risk pass for PDR

Run this as a concrete capability pass. First lock the population process, the development/policy linkage,
the data and time scale, the selection/measurement issue, and the uncertainty; then test whether the
manuscript addresses PDR's broad audience who inspect both the population evidence and its development
meaning.

- **Primary move:** Turn likely reviewer objections into a ledger with response evidence, manuscript
  location, and which audience (demographer vs. development/policy referee) must be convinced first.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the
  manuscript directly.
- **Sibling comparison:** compare against *Demography* and *Population Studies* (methods-forward),
  *Population Research and Policy Review* (applied policy), and *Studies in Family Planning* (programs);
  if a neighbor has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for
  volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Fit check】population-and-development question of broad interest? [Y/N]
【Screen risk】likely to pass the editorial/committee screen? [Y/N + why]
【Method rigor】rates/exposure/identification/comparability defensible to expert referees? [Y/N]
【Anonymity】all co-author identifiers removed? [Y/N]
【Realistic outcome】decline-without-review / R&R / (rare) accept
【Next】popdevr-submission (or popdevr-rebuttal if decided)
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — review-process page (editorial screen, double-anonymized review, ~3-month decision)
