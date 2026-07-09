---
name: atc-supplementary
description: Use when deciding what belongs in the ATC (ACM SIGOPS Annual Technical Conference, formerly USENIX ATC) two-page extended abstract, the 12-page paper body, the optional appendix, and the artifact — splitting content by review round and decision-criticality so nothing that decides acceptance lives where a reviewer is not required to read.
---

# ATC Supplementary

ATC gives you four places to put content, each read by a different reviewer under a different rule:
the **two-page extended abstract** (round one, two reviewers), the **12-page body** (round two, 3-4
reviewers), the **appendix** (optional reading), and the **artifact** (opened during round two and
evaluated post-acceptance). Placing content correctly is a strategic decision, not a formatting one,
because reviewers are **not required** to read the appendix and a round-one reviewer may read **only**
the abstract.

## The placement rule

**Anything that decides acceptance goes in a place the deciding reviewer is required to read.**

- Round-one acceptance is decided from the **extended abstract** → the problem, contribution,
  headline result, and honest cost must be *in the abstract*.
- Round-two acceptance is decided from the **body** → every load-bearing design detail, baseline,
  and result must be *in the 12 pages*.
- The **appendix** holds support a curious reviewer *may* consult — extra graphs, proofs, parameter
  tables — never a result the verdict depends on.
- The **artifact** holds runnable evidence and full data — it strengthens trust and earns badges,
  but the paper must be judgeable without executing it.

## What goes where

| Content | Home | Why |
|---|---|---|
| Problem, contribution, testbed, headline result, key cost | **Extended abstract** | The round-one decision surface; must stand alone |
| Design rationale, implementation, main experiments, fair baselines, tails/variance | **Body (≤12 pp)** | The round-two decision surface; nothing acceptance-critical may leave it |
| Extra sensitivity graphs, parameter sweeps, proofs, extended tables | **Appendix** | Optional depth; reviewers not required to read it |
| Full code, traces/datasets, configs, claim-to-experiment scripts | **Artifact** | Runnable evidence + badge material; paper still judged without running it |

## The extended abstract is not a teaser

The most common ATC mistake is treating the extended abstract as a marketing blurb that depends on
the paper. It is a **self-contained argument** that must survive being read *instead of* the paper
(see `atc-writing-style`). Move the real problem, the real contribution, and a real result into it;
do not defer them to "as shown in the paper."

## The appendix is not overflow

The second common mistake is using the appendix to dodge the 12-page limit by exiling results a
reviewer must weigh. If a graph is needed to believe a claim, it belongs in the body; if it is
merely reassuring, it belongs in the appendix. Ask: **would a reviewer who skips this change their
score?** If yes, it is body content.

## Consistency across the four places

- The number in the abstract, the body, the appendix, and the artifact output must **match**.
  Divergent numbers across places are a credibility hit and a frequent reviewer catch.
- The claim-to-experiment map (see `atc-experiments`, `atc-reproducibility`) should let a reviewer
  trace each body claim to an artifact script and each artifact output back to a body figure.
- Keep all four **double-blind**: an appendix or artifact often leaks identity (hostnames, owner
  strings, system names) even when the body is clean.

## Decision procedure

```text
[For each result] which round decides it? -> place it where that round's reviewer must read
[Abstract test]   can a reviewer accept/reject from the 2 pages alone? if not, move content in
[Body test]       is any acceptance-critical claim only in an appendix/artifact? if yes, move it in
[Appendix test]   would skipping this change a score? if yes, it is body content, not appendix
[Consistency]     do the numbers match across abstract/body/appendix/artifact? anonymity intact?
```

## Output format

```text
[Extended abstract] self-standing, decision-complete for round one? yes/no
[Body] all acceptance-critical content inside 12 pages? leaks to appendix/artifact?
[Appendix] optional-only? nothing score-changing exiled here?
[Artifact] runnable evidence + full data; paper judgeable without it? anonymized?
[Move queue] <content to relocate, with target location and reason>
```
