---
name: conext-supplementary
description: Use when deciding what goes in the ACM CoNEXT main body versus the appendix budget versus the artifact — splitting content by decision-criticality so nothing a reviewer needs to accept the paper hides in an appendix or repository, within the acmart limits (long ≤4 appendix pages, short ≤2).
---

# CoNEXT Supplementary

Decide where each piece of content lives: the **reviewed body**, the **appendix budget**, or the
**artifact**. The governing rule at CoNEXT is **decision-criticality** — anything a reviewer must
read to be convinced the paper should be accepted belongs in the body, not in an appendix a reviewer
may skip or an artifact they may not open. CoNEXT's appendix budget is small (long papers ≤4 pages,
short papers ≤2), so this is a real allocation problem, not a dumping ground.

## The three tiers

| Tier | Belongs in | Test |
|---|---|---|
| **Decision-critical** | Main body (≤16 / ≤10 pages) | Would a reviewer's accept/reject flip without it? -> body |
| **Supporting** | Appendix (≤4 / ≤2 pages) | Strengthens or reassures but does not decide -> appendix |
| **Reproducibility / bulk** | Artifact | Needed to *reproduce* but not to *judge* -> artifact |

## What must stay in the body

- The **central claims and the measurements that back them** — a headline result relegated to an
  appendix reads as hidden weakness.
- The **key baseline comparison** and how baselines were tuned.
- The **central limitation** and how you bound it (argue it where the result lives).
- The **evaluation platform description** sufficient to trust the numbers (topology, hardware,
  scale).

Reviewers are not required to read appendices or run artifacts to reach a decision; if acceptance
hinges on it, it is body content.

## What the appendix is for

- Extra results that reinforce a body claim (additional paths, parameter sweeps, secondary metrics).
- Detailed protocol/algorithm listings, proofs, or derivations that support but do not carry the
  contribution.
- Extended methodology detail (full trace-extraction steps, additional testbed configurations).

Keep it within the **acmart appendix budget** and clearly cross-referenced from the body; an
appendix the body never points to is wasted.

## What the artifact is for

- Full traces, configs, testbed scripts, and the raw-to-figure pipeline (see
  [`conext-reproducibility`](../conext-reproducibility/SKILL.md)).
- Large tables, per-run logs, and anything whose purpose is **reproduction** rather than
  **judgment**.
- Interactive or bulky material that cannot fit the page budget.

The artifact supports reproducibility and (if you opted in) badging; it is **not** a place to smuggle
decision-critical evidence past the page limit.

## Common misallocations

| Misallocation | Why it hurts | Fix |
|---|---|---|
| Headline result only in the artifact | Reviewers may not open it; reads as hidden | Bring the result into the body |
| Central limitation buried in an appendix | Misses the chance to pre-empt the objection | Argue it in the body where the result lives |
| Key baseline tuning only in a repo README | Soundness cannot be judged from the paper | Summarize the tuning in the body |
| Appendix overflowing the budget | acmart non-compliance / desk risk | Move bulk to the artifact, keep supporting material |
| Body padded with material that belongs in the artifact | Wastes pages you need for evidence | Push reproduction bulk to the artifact |

## Double-anonymity across tiers

Every tier is a leak surface: an appendix figure showing an internal hostname, or an artifact with
commit metadata, breaks anonymity as surely as the body. Run the anonymity sweep (see
[`conext-submission`](../conext-submission/SKILL.md)) across the body, appendix, and artifact
together.

## Output format

```text
[Allocation] body / appendix / artifact for each major piece of content
[Decision-critical check] anything acceptance depends on living outside the body? -> move it in
[Budget] appendix pages used vs. limit (long ≤4 / short ≤2); acmart compliant?
[Cross-refs] appendix + artifact pointed to from the body? yes/no
[Anonymity] body + appendix + artifact swept together? yes/no
```
