---
name: conext-writing-style
description: Use when shaping the prose and structure of an ACM CoNEXT paper — leading with the networking problem and deployment context, tying every claim to a measurement on the real target platform, arguing limitations rather than reciting them, and holding the acmart page budget for long (≤16) and short (≤10) papers.
---

# CoNEXT Writing Style

Write to the CoNEXT reader: a networking systems/measurement expert who wants the **networking
contribution and the evaluation platform on the first page**, evidence **proportional to the claim**
and drawn from the **real target**, and a limitations posture visible from the start. Because CoNEXT
papers are **PACMNET** journal articles judged in a two-round, one-shot-revision process, the draft
must read like a manuscript whose claims are already backed, not a promising sketch.

## The first-page arc

Lead with the arc the worked example demonstrates
([`../../resources/worked-examples/01-introduction.md`](../../resources/worked-examples/01-introduction.md)):

1. **The networking problem, in a real deployment context** — a problem an operator, protocol
   designer, or systems builder recognizes, stated in the first breath.
2. **Why the current state is inadequate** — what existing systems/measurements miss, and why the
   gap matters on real paths or hardware.
3. **The contribution, as networking claims** — a mechanism, a measured phenomenon, or both, not a
   model or a score.
4. **Evidence on the real target** — a testbed run, a deployment, or a trace, each claim paired with
   the measurement that backs it.
5. **What changes for networking + limitations posture** — the payoff for practice, with the central
   threat named up front rather than deferred.

## Claims tied to measurements

- **State the claim as an outcome an operator or protocol cares about** ("completion time for
  throttled short flows drops"), not as an offline metric ("accuracy is high").
- **Pair each claim with its evidence** and its platform: which testbed, which trace, which vantage
  points, which baseline. A claim with no matching measurement is the fastest path to a
  one-shot-revision change-list item.
- **Report uncertainty.** Confidence intervals, multiple runs, and effect sizes read as rigor; a
  single bar with no variance reads as a lab artifact to a measurement reviewer.

## Limitations as argument, not boilerplate

CoNEXT reviewers reward a paper that names its own central threat and bounds it. Put the limitation
**where the result lives**, not only in a closing section:

- If a measurement infers an outcome from a proxy signal, say so and bound it with a ground-truth
  subset.
- If evaluation is on one testbed or one network, scope the generalization claim explicitly.
- If a mechanism assumes hardware behavior, state what breaks if the assumption fails.

A limitations section that only lists generic caveats ("results may not generalize") wastes the one
place you can pre-empt the reviewer's strongest objection.

## Page-budget discipline (acmart)

- **Long papers ≤16 pages** text+figures (+ unlimited references + ≤4 appendix pages); **short
  papers ≤10 pages** (+ unlimited references + ≤2 appendix pages). Verify the current numbers.
- References are unlimited, so never sacrifice a citation for space; compress prose, figures, and
  redundant tables instead.
- The appendix budget is small and for supporting, not deciding, material — nothing a reviewer needs
  to accept the paper should live only there (see [`conext-supplementary`](../conext-supplementary/SKILL.md)).
- Do not alter the `acmart` template to reclaim space; editorial compression is the only safe lever.

## Networking-prose specifics

- **Define the topology and scale early.** A reader should know what network, what hardware, and
  what scale before the evaluation.
- **Name the baselines honestly** and describe how they were tuned; an untuned strawman is a
  soundness flag.
- **Figures earn their space.** A topology diagram, a CDF, or a time series that a reviewer can read
  in one glance is worth more than a paragraph; a decorative architecture box is not.
- **Anonymize as you write** — refer to your own system and prior work in the third person, and do
  not name testbeds, operators, or repositories (double-anonymous review).

## Common CoNEXT-specific failure modes

| Failure | Why it hurts at CoNEXT | Fix |
|---|---|---|
| Simulation stands in for the real platform | Platform-realism is a core CoNEXT expectation | Add a testbed/deployment run, or scope the claim |
| Claim outruns the measurement | The two-round review catches it | Pair each claim with evidence, or soften the claim |
| Limitations deferred to one closing paragraph | Misses the chance to pre-empt objections | Argue the central threat where the result lives |
| Model/leaderboard framing | Reads as an ML paper wearing a networking title | Reframe around the networking lesson (topic-selection) |
| Over-signposted roadmap | Substitutes structure for argument | One-line roadmap; let the contributions carry it |

## Output format

```text
[First-page arc] problem -> inadequacy -> contribution -> real-target evidence -> what changes + limitations
[Claim-evidence pairs] <claim -> measurement + platform + baseline>
[Limitations posture] <central threat named where the result lives? yes/no>
[Budget] pages used (body/appendix), acmart compliant? refs unlimited
[Anonymity] third-person self-reference; no testbed/operator/repo names
```
