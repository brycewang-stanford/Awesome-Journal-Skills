---
name: fast-supplementary
description: Use when deciding what belongs in a USENIX FAST paper body versus its artifact and appendices, covering the USENIX two-column page budget (references excluded), the rule that decision-critical storage evidence stays inside the reviewed pages, double-blind supplementary material, and how to split a storage paper between body and package.
---

# FAST Supplementary

Use this when assembling FAST supplementary material. The governing rule is simple and strict: **the
paper must be judgeable from the reviewed pages alone.** The artifact, traces, and any appendix
support the paper; they do not hold the argument. Reviewers open the artifact at their discretion, so
anything the decision depends on lives in the body.

## What goes where

| Content | Body (within page budget) | Artifact / appendix |
|---|---|---|
| The storage claim and its headline result | Yes | — |
| Core design or study protocol | Yes | Full parameter sweeps, extra configs |
| The testbed: device models, firmware, state | Yes (summary table) | The complete machine/firmware inventory |
| Headline storage metrics + the invariant test | Yes (WA/tail latency/crash test) | Full distributions, per-run logs |
| Crash-consistency evidence for a durability claim | The result + method | The fault-injection / replay harness |
| Workloads and traces | Named + why chosen | The trace archive and replay scripts |
| Raw device counters, logs, scripts | — | Yes |
| Reproduction instructions | A pointer | The README and run scripts |

If a reviewer would need to open the artifact to know whether to accept, the paper is
mis-partitioned — move that evidence into the body.

## The page-budget discipline

FAST's USENIX two-column budget (FAST '27: ≤12 pages long / ≤6 short, **references excluded**) is
firm, and it counts figures and tables. References are uncapped, so a rich bibliography costs no body
space, but everything else competes. Consequences:

- Keep the **headline storage metric, the device table, and the durability/consistency check** in the
  body — they are decision-critical.
- Move long parameter sweeps, per-device breakdowns, and secondary microbenchmarks to the artifact
  with explicit forward references.
- Do not use the artifact to smuggle in a result that would not fit — an argument that only closes
  with material outside the reviewed pages reads as unreviewable.

## Double-blind supplementary rules

```text
[No identity]   no authors, affiliations, acknowledgements, funders, hostnames, cluster paths, or
                repo owners anywhere in the archive or appendix
[Anonymized links] the availability link points at an anonymizing host, not a personal/institutional repo
[Scrub device dumps] SMART/firmware/config dumps can carry serials, hostnames, or datacenter tags — redact them
[Clean archive]  no .git history, .DS_Store, credentials, caches, or huge irrelevant trace dumps
[Opens clean]    verify the archive unzips and the README orients a reader in one minute on a fresh machine
```

## Appendix and artifact-appendix architecture

- Order supplementary sections to mirror the paper's claim/RQ order; reviewers navigate by claim, not
  page number.
- Keep each supplementary section referenced from the body at least once — orphaned material is
  invisible under discretionary review.
- Distinguish the **review-time artifact** (anonymized, for the paper's reviewers) from the **artifact
  appendix** added post-acceptance for the AEC and badges (`fast-artifact-evaluation`); do not
  conflate them.
- Confirm on the current call whether any in-paper appendix counts against the page budget; this
  varies and changes the split.

## Vignette: splitting a file-system design paper

A paper presenting a new file-system layout plus an evaluation: the body keeps the design, the
headline results (write amplification and tail latency on named devices at steady state), the
crash-consistency test summary, and the caveats; the artifact holds the full parameter sweeps, the
complete device/firmware inventory, the aging-workload scripts, the crash-injection harness, the
archived traces with replay scripts, and the analysis notebooks. Nothing decision-critical lives only
in the artifact, because artifact inspection is discretionary and the reviewers judge from the pages.

## Output format

```text
[Supplement status] ready / needs fixes / not ready
[Partition check] anything decision-critical outside the body? <none / move: what>
[Page budget] body within the 12/6-page limit? references excluded correctly? yes/no
[Anonymity] archive + device dumps clean of identity/metadata? passed/issues
[Body dependency] <what a reviewer can decide without opening the artifact>
```
