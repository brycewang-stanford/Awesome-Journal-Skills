---
name: atc-supplementary
description: Use when deciding what belongs in an ATC (ACM SIGOPS Annual Technical Conference, formerly USENIX ATC) paper's first two pages, the rest of the 12-page budget, the optional in-limit appendix, and the artifact — splitting content by review round and decision-criticality so nothing that decides acceptance lives where a reviewer is not required to read, now that ATC 2027 counts appendices toward the page limit.
---

# ATC Supplementary

ATC 2027 (call re-verified 2026-11-24) gives you four places to put content, each read under a
different rule: the **first two pages** (the round-one surface), the **rest of the body** (round two),
an **optional appendix** that now sits **inside** the 12/6-page limit, and the **artifact** (opened
during review, evaluated post-acceptance). Placing content correctly is a strategic decision, not a
formatting one: a round-one reviewer may read **only** pages 1-2, and the PC is **not required** to
read supplementary material.

## The placement rule

**Anything that decides acceptance goes in a place the deciding reviewer is required to read.**

- Round-one survival is decided from the **first two pages** → scope, motivation, the main idea, the
  delta over prior work, positioning, and a credible evaluation result must all appear there.
- Round-two acceptance is decided from the **body** → every load-bearing design detail, baseline,
  and result must be in the main text.
- The **appendix** holds material "of interest to some reviewers" but not central — algorithm
  details, proofs, code snippets. In 2027 it **counts toward the 12 (or 6) pages**, so it competes
  with the body for space; it is no longer free overflow.
- The **artifact** holds runnable evidence and full data — it strengthens trust and earns badges,
  but the paper must be judgeable without executing it, and the author response may not lean on it.

## What goes where

| Content | Home | Why |
|---|---|---|
| Problem, idea, delta, positioning, headline result, key cost | **First two pages** | The round-one decision surface; must stand alone |
| Design rationale, implementation, main experiments, fair baselines, tails/variance | **Body** | The round-two decision surface; nothing acceptance-critical may leave it |
| Algorithm details, proofs, code snippets | **Appendix (inside the page limit)** | Optional depth; costs pages, so keep it short |
| Extra sensitivity graphs, parameter sweeps, full code, traces, configs | **Artifact** | Runnable evidence + badge material; the paper is still judged without it |

(History: ATC 2026 placed a separate, unpublished two-page **extended abstract** in front of the
paper and let appendices sit outside the page limit. Neither holds in 2027.)

## The first two pages are not a teaser

The most common ATC mistake is an opening that only makes sense after reading section 4. Round one
may never get there. Move the real problem, the real contribution, and a real measured result into
the abstract and introduction (see `atc-writing-style`); do not defer them to "as shown in §5."

## The appendix is not overflow any more

Because appendices now count toward the limit, exiling material to an appendix saves nothing. If a
graph is needed to believe a claim, it belongs in the body; if it is merely reassuring, it belongs in
the artifact. Ask: **would a reviewer who skips this change their score?** If yes, it is body
content.

## Consistency across the four places

- The number in the opening, the body, the appendix, and the artifact output must **match**.
- The claim-to-experiment map (see `atc-experiments`, `atc-reproducibility`) should let a reviewer
  trace each body claim to an artifact script and each artifact output back to a body figure.
- Keep all four **double-blind**: an appendix or artifact often leaks identity (hostnames, owner
  strings, system names) even when the body is clean.

## Decision procedure

```text
[For each result] which round decides it? -> place it where that round's reviewer must read
[Opening test]    can a reviewer pass/reject from pages 1-2 alone? if not, move content forward
[Body test]       is any acceptance-critical claim only in the appendix/artifact? if yes, move it in
[Budget test]     body + appendix within 12 (long) / 6 (short) pages, references excluded?
[Consistency]     do the numbers match across opening/body/appendix/artifact? anonymity intact?
```

## Output format

```text
[First two pages] self-standing, decision-complete for round one? yes/no
[Body] all acceptance-critical content in the main text? leaks to appendix/artifact?
[Appendix] short, optional-only, and counted inside the page limit?
[Artifact] runnable evidence + full data; paper judgeable without it? anonymized?
[Move queue] <content to relocate, with target location and reason>
```
